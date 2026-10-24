from typing import Generic, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")

class PaginationParams(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=20, ge=1, le=200)

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.size

    @property
    def limit(self) -> int:
        return self.size

    def filters_only(self) -> dict:
        return self.model_dump(
            exclude={"page", "size", "offset", "limit", "order_by"},
            exclude_unset=True,
        )


class PageMeta(BaseModel):
    page: int = Field(ge=1)
    size: int = Field(ge=1)
    total: int = Field(ge=0)
    pages: int = Field(ge=0)
    has_next: bool
    has_prev: bool

    @classmethod
    def from_total(cls, *, page: int, size: int, total: int):
        pages = (total + size - 1) // size if size else 0
        return cls(
            page=page,
            size=size,
            total=total,
            pages=pages,
            has_next=page < pages,
            has_prev=page > 1,
        )


class PaginatedResponse(BaseModel, Generic[T]):
    meta: PageMeta
    items: list[T]

    @classmethod
    def build(cls, *, items: list[T], params: PaginationParams, total: int):
        meta = PageMeta.from_total(
            page=params.page,
            size=params.size,
            total=total
        )
        return cls(items=items, meta=meta)
