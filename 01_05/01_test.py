from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {"id": "123", "signup_ts": "2024-06-18 10:00", "friends": [1, 2, "3"]}

user1 = User(**external_data)
print(user1.id)
print(user1.signup_ts)
print(user1)
print(user1.model_dump())
