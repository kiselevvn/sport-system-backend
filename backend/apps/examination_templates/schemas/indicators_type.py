from pydantic import BaseModel


class IntegerIndiactorSchema(BaseModel):
    value: int
    type_indicator: str


class FloatIndiactorSchema(BaseModel):
    value: float
    type_indicator: str


# class ListIndiactorSchema(BaseModel):
#     value: float
#     type_indicator: str
