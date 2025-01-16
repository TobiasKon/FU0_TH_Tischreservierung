from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/tables")
def get_free_tables():
    return "GET on /tables is working"

@app.post("reservations")
def book_table():
    return "POST on /reservations is working"

@app.delete("/reservations")
def cancel_reservation():
    return "DELETE on /reservations is working"

@app.get("/reservations")
def get_all_reservations():
    return "GET on /reservations is working"