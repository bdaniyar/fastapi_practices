from typing import Annotated
from fastapi import Depends, Path, HTTPException, status

from app.core.models import Product

from . import crud
from sqlalchemy.ext.asyncio import AsyncSession
from app.core import db_helper

SessionDep = Annotated[AsyncSession, Depends(db_helper.session_dependency)]


async def product_by_id(product_id: Annotated[int, Path], session: SessionDep) -> Product:
    product = await crud.get_product(session=session, product_id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    return product