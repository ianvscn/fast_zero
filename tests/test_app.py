from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_hello_world(client):
    response = client.get("/")  # act (ação)
    assert response.status_code == HTTPStatus.OK  # assert (garantir)
    assert response.json() == {"message": "Hello World"}  # assert


def test_create_user(client):
    response = client.post(  # UserSchema
        "/users/",
        json={
            "username": "testusername",
            "password": "password",
            "email": "test@test.com",
        },
    )

    # voltou o status code correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPublic
    assert response.json() == {
        "username": "testusername",
        "email": "test@test.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "testusername",
                "email": "test@test.com",
                "id": 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "password": "123",
            "username": "testusername2",
            "email": "test@test.com",
            "id": 1,
        },
    )

    assert response.json() == {
        "username": "testusername2",
        "email": "test@test.com",
        "id": 1,
    }


def test_delete_user(client):
    response = client.delete(
        "/users/1",
    )

    assert response.json() == {"message": "user deleted"}
