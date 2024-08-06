from datetime import datetime
from typing import Optional

from pydantic import BaseModel, constr


class MessagesModel(BaseModel):
    user_id: str
    first_name: constr(min_length=1, max_length=255) = None
    last_name: Optional[constr(min_length=1, max_length=255)] = None
    user_name: Optional[constr(min_length=1, max_length=255)] = None
    chat_id: Optional[constr(min_length=1, max_length=100)] = None
    message_id: Optional[constr(min_length=1, max_length=100)] = None
    text: str
    date: datetime

    @classmethod
    def from_mongo(cls, document):
        return cls(
            id=str(document["_id"]),
            user_id=document["user_id"],
            first_name=document["first_name"],
            last_name=document["last_name"],
            user_name=document["user_name"],
            chat_id=document["chat_id"],
            message_id=document["message_id"],
            text=document["text"],
            date=document["date"],
        )


