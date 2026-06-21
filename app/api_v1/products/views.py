from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db_helper

from . import crud
from .schemas import Product, ProductCreate

router = APIRouter(prefix="/products", tags=["Products"])
SessionDep = Annotated[AsyncSession, Depends(db_helper.session_dependency)]


@router.get("/", response_model=list[Product])
async def get_products(session: SessionDep):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(session: SessionDep, product_in: ProductCreate):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}", response_model=Product)
async def get_product(session: SessionDep, product_id: int):
    product = await crud.get_product(session=session, product_id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    return product
