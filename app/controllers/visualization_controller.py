"""
visualization_controller.py

This module defines the API routes for generating visualizations of user expenses or income using FastAPI. It includes an endpoint for generating and streaming plots based on user data.

Modules Imported:
    - io: Input/Output operations.
    - fastapi.FastAPI, Depends, APIRouter: FastAPI classes for creating the application instance, handling dependencies, and routing.
    - fastapi.HTTPException: Exception class for handling HTTP errors.
    - starlette.responses.StreamingResponse: Response class for streaming data.
    - models.expenses.Expenses: Pydantic model for expenses data.
    - services.expensesService, services.incomeService: Service functions for retrieving expenses and income data by user ID.
    - validations.expenses_validations: Validation functions for checking user ID existence.
    - matplotlib.pyplot: Matplotlib module for plotting data.

Routes:
    - GET /{user_id}/{what_to_show}: Generate a visualization of expenses or income for a specific user.


"""

import io
from fastapi import FastAPI, Depends, APIRouter
from fastapi import HTTPException
from starlette.responses import StreamingResponse
from app.models.expenses import Expenses
from app.services.expenses_service import get_expenses_by_user_id
from app.services.income_service import get_income_by_user_id
from validations.expenses_validations import check_id_exist
import matplotlib.pyplot as plt

from validations.visualization_validations import check_what_to_show_correct

visualization_Router = APIRouter()


@visualization_Router.get("/{user_id}/{what_to_show}")
async def Show_visually(what_to_show: str = Depends(check_what_to_show_correct),
                        user_id: int = Depends(check_id_exist)):
    """
  Generate a visualization of expenses or income for a specific user.

  Args:
      what_to_show (str): Type of data to visualize ("expenses" or "income").
      user_id (int): ID of the user for whom to generate the visualization.

  Returns:
      StreamingResponse: Streamed image of the generated plot.

  Raises:
      HTTPException: If an error occurs during visualization generation.
  """
    try:
        if what_to_show == "expenses":
            result = await get_expenses_by_user_id(user_id)
        else:
            result = await get_income_by_user_id(user_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

    dates = [item['date'] for item in result]
    amounts = [item['amount'] for item in result]

    # Create a plot
    plt.figure()
    plt.plot(dates, amounts)
    plt.title(f'{what_to_show.capitalize()} of User {user_id}')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return StreamingResponse(img, media_type="image/png")
