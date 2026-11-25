# pytest test any file or folder beging with name test
from app import app


def test_home():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.data == "Flask App Up and Running!"
