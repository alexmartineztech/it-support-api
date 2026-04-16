from fastapi import FastAPI
from pydantic import BaseModel
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI(title="IT Support API")

# ---- Models ----
class User(BaseModel):
    name: str
    role: str

class Ticket(BaseModel):
    title: str
    description: str
    status: str = "open"

# ---- Fake DB ----
users = []
tickets = []

# ---- Routes ----
@app.get("/")
def root():
    return {"message": "IT Support API is running"}

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/users")
def create_user(user: User):
    users.append(user)
    logging.info(f"User created: {user}")
    return {"message": "User created", "user": user}

@app.get("/users")
def get_users():
    return users

@app.post("/tickets")
def create_ticket(ticket: Ticket):
    tickets.append(ticket)
    logging.info(f"Ticket created: {ticket}")
    return {"message": "Ticket created", "ticket": ticket}

@app.get("/tickets")
def get_tickets():
    return tickets
