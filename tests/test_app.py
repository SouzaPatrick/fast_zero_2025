from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olar mundos!"}


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "alice",
            "password": "secret",
            "email": "alice@exemple.com",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "email": "alice@exemple.com",
        "username": "alice",
    }


def test_list_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "id": 1,
                "email": "alice@exemple.com",
                "username": "alice",
            }
        ]
    }


def test_get_users(client):
    user_id = 1
    response = client.get(f"/users/{user_id}")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "email": "alice@exemple.com",
        "username": "alice",
    }


def test_update_user(client):
    user_id = 1
    response = client.put(
        f"/users/{user_id}",
        json={
            "email": "bob@exemple.com",
            "username": "bob",
            "password": "new_secret",
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "email": "bob@exemple.com",
        "username": "bob",
    }


def test_update_user_not_found(client):
    user_id = 0
    response = client.put(
        f"/users/{user_id}/",
        json={
            "email": "bob@exemple.com",
            "username": "bob",
            "password": "new_secret",
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        "detail": "User not found!!!",
    }


def test_delete_user(client):
    user_id = 1
    response = client.delete(
        f"/users/{user_id}/",
    )

    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_user_not_found(client):
    user_id = 1
    response = client.delete(
        f"/users/{user_id}/",
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        "detail": "User not found!!!",
    }
