"""Pagination models."""
from typing import Self

from pydantic import BaseModel, Field, computed_field, model_validator

from ..api.utils.sorting import SortBy

SIZE_DESCRIPTION = "Number of objects per page (0 = all)."


class Pagination(BaseModel):
    """Pagination class."""
    page: int = Field(description="Current page number (0 indexed).", examples=[0])
    size: int = Field(description="Number of objects per page (0 = all).", examples=[100])
    result_count: int = Field(description="Total count of objects in filtered result set.", examples=[200])
    total_count: int = Field(description="Total count of objects before filtering.", examples=[200])
    sort: SortBy = Field(description="Sorted by field.", examples=["id"])

    @computed_field  # type: ignore
    @property
    def total_pages(self) -> int:
        """Total number of pages."""
        return (self.result_count + self.size - 1) // self.size

    @computed_field  # type: ignore
    @property
    def last_page(self) -> int:
        """Last page number (0 indexed)."""
        return max(0, self.total_pages - 1)

    @model_validator(mode="after")
    def overwrite_pagination(self) -> Self:
        """Overwrite page and size if all entries are requested."""
        if self.size == 0:
            self.page = 0
            self.size = self.result_count
        return self

    def offset(self) -> int:
        """Calculate offset."""
        return (self.page * self.size) if self.size != 0 else 0

    def limit(self) -> int:
        """Calculate limit."""
        return self.size if self.size != 0 else self.result_count
