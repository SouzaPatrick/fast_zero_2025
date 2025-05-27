from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from src.schemas import MessageSchema, UserDB, UserList, UserPublic, UserSchema

app = FastAPI(title="Minha API BALA!", version="v1.0.0")

database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=MessageSchema)
def read_root():
    return {"message": "Olar mundos!"}


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        **user.model_dump(),
        id=len(database) + 1,
    )

    database.append(user_with_id)

    return user_with_id


@app.get("/users/", status_code=HTTPStatus.OK, response_model=UserList)
def list_users():
    return {"users": database}


@app.get(
    "/users/{user_id}/", status_code=HTTPStatus.OK, response_model=UserPublic
)  # noqa E501
def get_user(user_id: int):
    return database[user_id - 1]


@app.put(
    "/users/{user_id}/", status_code=HTTPStatus.OK, response_model=UserPublic
)  # noqa E501
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(
        **user.model_dump(),
        id=user_id,
    )

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="User not found!!!",
        )

    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete(
    "/users/{user_id}/",
    status_code=HTTPStatus.NO_CONTENT,
)  # noqa E501
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="User not found!!!",
        )

    database.pop(user_id - 1)
