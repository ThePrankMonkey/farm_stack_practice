from bson import ObjectId
from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field
from pydantic_mongo import ObjectIdField
# from app.helpers.models import PyObjectId

class Post(BaseModel):
    # id: ObjectId = Field(alias="_id")
    user: str
    title: str
    body: str
    timestamp: datetime = datetime.now()

    model_config = ConfigDict(arbitrary_types_allowed=True)