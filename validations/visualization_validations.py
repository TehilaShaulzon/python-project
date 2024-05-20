"""
validations/visualization_validations.py

This module defines validation functions related to visualization operations.

Modules Imported:
    - fastapi.HTTPException: Exception class for handling HTTP errors.

Functions:
    - check_what_to_show_correct: Check if the specified visualization type is valid.


"""

from fastapi import HTTPException


def check_what_to_show_correct(what_to_show: str):
    """
    Check if the specified visualization type is valid.

    Args:
        what_to_show (str): Type of visualization.

    Returns:
        str: Validated visualization type.

    Raises:
        HTTPException: If an error occurs during validation.
    """
    if what_to_show != "expenses" and what_to_show != "income":
        raise HTTPException(status_code=404, detail="Error! Try again")
    return what_to_show
