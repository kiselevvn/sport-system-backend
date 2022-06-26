from pydantic import BaseModel


class IntegerIndiactorSchema(BaseModel):
    value: int
    max_value: int
    min_value: int


class FloatIndiactorSchema(BaseModel):
    value: float
    max_value: float
    min_value: float


# class ListIndiactorSchema(BaseModel):
#     value: float
#     type_indicator: str
