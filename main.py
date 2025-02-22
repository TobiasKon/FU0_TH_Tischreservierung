from typing import Annotated, Union
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
app = FastAPI()


class Tables(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    seatings: int = Field(index=True)
    
class Reservations(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    table_id: int = Field(foreign_key="Tables.id")
    time: str
    date: str
    cancellation_pin: str

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/tables")
def get_free_tables():
    return "GET on /tables is working"

@app.post("/reservations")
def book_table():
    return "POST on /reservations is working"

@app.delete("/reservations")
def cancel_reservation():
    return "DELETE on /reservations is working"

@app.get("/reservations")
def get_all_reservations():
    return "GET on /reservations is working"