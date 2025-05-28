from enum import IntEnum
from pydantic import BaseModel, Field
from typing import List, Optional

from fastapi import FastAPI, HTTPException

api = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1
    
    
class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=512, description='Name of the todo.')
    todo_desc: str = Field(..., description="Description of the todo")
    priority: Priority = Field(default=Priority.LOW, description="Priority of the todo")
    
    
#This is just good practice to create a class for pydantic validation 
# even if the content is the same as the base class, just create a class, inherit from base and pass
class TodoCreate(TodoBase):
    pass


#Create a separate class for each api request so that all the details entered can ve properly validated
class Todo(TodoBase):
    todo_id: int = Field(..., description="Unique ID of the todo")

class TodoUpdate(TodoBase):
    todo_name: Optional[str] = Field(None, min_length=3, max_length=512, description="Name of the todo")
    todo_desc: Optional[str] = Field(None, description="Description of the todo.")
    priority: Optional[Priority] =  Field(None, description="Priority of the todo.")

all_todos=[
    Todo(todo_id=1, todo_name='Clean House', todo_desc='Cleaning the house thoroughly', priority=Priority.HIGH),
    Todo(todo_id=2, todo_name='Sports', todo_desc='Go to the Gym', priority=Priority.MEDIUM),
    Todo(todo_id=3, todo_name='Read', todo_desc='Read 10 pages of the book', priority=Priority.LOW),
    Todo(todo_id=4, todo_name='Work', todo_desc='Complete project documentation', priority=Priority.HIGH),
    Todo(todo_id=5, todo_name='Study', todo_desc='Prepare for the upcoming exams', priority=Priority.LOW)
]

@api.get('/')
def index():
    return {"message": "Hello World"}


@api.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
        
    raise HTTPException(status_code=404, detail="Todo not found")
    
        
        
@api.get("/todos", response_model=List[Todo])
def get_todos(first_n:int=None): #Setting up the query parameters, basically makes the URL look like this
                        # localhost 8000/todos?first_n=3 will give only the first 3 values from the list, everything after the '?' is part of the query before the next '/'
    if first_n:
        return all_todos[:first_n]
    
    else:
        return all_todos
    
    
@api.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(t.todo_id for t in all_todos) + 1
    new_todo = Todo(
        todo_id=new_todo_id,
        todo_name=todo.todo_name,
        todo_desc=todo.todo_desc,
        priority=todo.priority
    )

    all_todos.append(new_todo)
    return new_todo


@api.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id==todo_id:
            todo.todo_name = updated_todo.todo_name
            todo.todo_desc = updated_todo.todo_desc
            todo.priority = updated_todo.priority
            return todo
        
    raise HTTPException(status_code=404, detail="Todo not found")


@api.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            del_todo = all_todos.pop(index)
            return del_todo
        
    raise HTTPException(status_code=404, detail="Todo not found")
    