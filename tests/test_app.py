from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_hello_world():
    client = TestClient(app)  # arrange (organização)
    response = client.get('/')  # act (ação)
    assert response.status_code == HTTPStatus.OK  # assert (garantir)
    assert response.json() == {"message": "Hello World"}  # assert
