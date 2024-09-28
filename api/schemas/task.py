from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str | None = Field(None, example = "クリーニングを取りに行く")

class TaskSchema(TaskBase):
    id: int
    done: bool = Field(False, description = "完了フラグ")

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id:int

    
class DoneResponse(BaseModel):
    id: int

class Config:
    orm_model = True
