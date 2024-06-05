"""Module for sorting utilities."""
from typing import Callable, Optional, Type

from fastapi import Query
from pydantic import BaseModel, ConfigDict
from sqlalchemy.sql.expression import UnaryExpression, asc, desc


class SortBy(BaseModel):
    """Model for sorting criteria."""
    field: Optional[str] = None
    order: Callable[[str], UnaryExpression[str]] = asc

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @staticmethod
    def create(fields: list[str]) -> str:
        """Create a regex pattern for allowed sort options."""
        return "|".join(f"^{field}(:asc|:desc)?$" for field in fields)

    @staticmethod
    def parse(sort_value: str) -> "SortBy":
        """Parse a sort value string into a SortBy object."""
        parts = sort_value.split(":", 1)
        field = parts[0]
        order = desc if len(parts) >= 2 and parts[1].lower() == "desc" else asc
        return SortBy(field=field, order=order)

    def clause(self) -> Optional[UnaryExpression[str]]:
        """Return the SQL ORDER BY clause."""
        return self.order(self.field) if self.field else None  # pylint: disable=too-many-function-args


def parse_sort(model: Type[BaseModel]) -> Callable[[str], SortBy]:
    """Factory function to create a sort parser for the given model."""
    fields = list(model.model_fields.keys())

    def _parse_sort(sort: str = Query(None, description=f"Sort by '{{field}}:asc | desc'<br>Allowed fields: {fields}",
                                      pattern=SortBy.create(fields))) -> SortBy:
        return SortBy.parse(sort) if sort else SortBy()

    return _parse_sort
