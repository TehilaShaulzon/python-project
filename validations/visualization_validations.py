from fastapi import HTTPException


def check_what_to_show_correct(what_to_show):
    if what_to_show!="expenses" and what_to_show!="income":
        raise HTTPException(status_code=404, detail="error! try again")
    return what_to_show