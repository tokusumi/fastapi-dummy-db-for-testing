from starlette.testclient import TestClient
from users.main import app, get_db


def temp_db(f):
    def func(SessionLocal, *args, **kwargs):
        # テスト用のDBに接続するためのsessionmaker instanse
        #  (SessionLocal) をfixtureから受け取る

        def override_get_db():
            try:
                db = SessionLocal()
                db.begin(subtransactions=True)
                yield db
            finally:
                db.rollback()
                db.close()

        # fixtureから受け取るSessionLocalを使うようにget_dbを強制的に変更
        app.dependency_overrides[get_db] = override_get_db
        # Run tests
        f(*args, **kwargs)
        # get_dbを元に戻す
        app.dependency_overrides[get_db] = get_db

    return func


client = TestClient(app)


@temp_db
def test_create_user():
    response = client.post("/users/", json={"email": "foo", "password": "fo"})
    assert response.status_code == 200


@temp_db
def test_create_user_2():
    response = client.post("/users/", json={"email": "foo", "password": "fo"})
    assert response.status_code == 200
