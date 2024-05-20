import io

from fastapi import FastAPI, Depends, APIRouter
from fastapi import  HTTPException
from starlette.responses import StreamingResponse

from models.expenses import Expenses
from services.expensesService import get_expenses_by_user_id
from services.incomeService import get_income_by_user_id
from validations.expenses_validations import check_id_exist
import matplotlib.pyplot as plt

from validations.visualization_validations import check_what_to_show_correct

visualization_Router = APIRouter()

@visualization_Router.get("/{user_id}/{what_to_show}")
async def Show_visually(what_to_show:str=Depends(check_what_to_show_correct) ,user_id:int=Depends(check_id_exist)):
  try:
    if what_to_show=="expenses":
      result=await get_expenses_by_user_id(user_id)
    else:
      result=await get_income_by_user_id(user_id)
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

