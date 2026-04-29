from pydantic import BaseModel, Field


class GourmetSearchParams(BaseModel):
    keyword: str | None = None
    large_area: str | None = None
    middle_area: str | None = None
    small_area: str | None = None
    lat: float | None = None
    lng: float | None = None
    range: int | None = Field(default=None, ge=1, le=5)
    genre: str | None = None
    budget: str | None = None
    count: int = Field(default=10, ge=1, le=100)
    start: int = Field(default=1, ge=1)
    private_room: bool = False
    free_drink: bool = False
    free_food: bool = False
    lunch: bool = False
    non_smoking: bool = False
