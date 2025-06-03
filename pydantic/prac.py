from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = 'John Doe'

user = User(id = 12)
print(user)