from pydantic import BaseModel, field_validator


class Product(BaseModel):
    id: int
    name: str
    sku: str

    @field_validator("sku")
    def validate_sku(cls, value):
        if not isinstance(value, str):
            raise ValueError("SKU must be a string")
        if not (8 <= len(value) <= 12) or not all(
            c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_" for c in value
        ):
            raise ValueError(
                "SKU must be 8 to 12 characters long and contain only uppercase letters, numbers, underscores, or hyphens"
            )
        return value
