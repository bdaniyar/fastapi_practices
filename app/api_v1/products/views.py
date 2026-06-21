from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db_helper
from app.core.models import Product as ProductModel

from . import crud
from .dependencies import product_by_id
from .schemas import Product, ProductCreate, ProductPartialUpdate, ProductUpdate

router = APIRouter(prefix="/products", tags=["Products"])
SessionDep = Annotated[AsyncSession, Depends(db_helper.session_dependency)]
ProductDep = Annotated[ProductModel, Depends(product_by_id)]


@router.get("/", response_model=list[Product])
async def get_products(session: SessionDep):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(session: SessionDep, product_in: ProductCreate):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}", response_model=Product)
async def get_product(product: ProductDep):
    return product


@router.put("/{product_id}/", response_model=Product)
async def update_product(
    product_update: ProductUpdate,
    session: SessionDep,
    product: ProductDep,
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )


@router.patch("/{product_id}/", response_model=Product)
async def update_product_partial(
    product_update: ProductPartialUpdate,
    session: SessionDep,
    product: ProductDep,
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=True,
    )
