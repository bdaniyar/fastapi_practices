from typing import Annotated
from fastapi import APIRouter, Path 

router = APIRouter(prefix="/items", tags=["items"])


@router.get("")
def list_items():
    """Get all items."""
    return {"items": ["item1", "item2", "item3"]}


@router.get("/last")
def get_last_item():
    """Get the last item."""
    return {"item_id": 3}


@router.get("/{item_id}")
def get_item(item_id: Annotated[int, Path(gt=1, lt=100000)]):
    """Get item by ID."""
    return {"item_id": item_id}
