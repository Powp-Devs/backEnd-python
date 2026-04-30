from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/pedidos", tags=["Rotas para os pedidos"])

