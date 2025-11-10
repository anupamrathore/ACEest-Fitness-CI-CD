from app import create_app
app = create_app()

def test_home():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert b"Welcome to the Gym Management System" in res.data

def test_members():
    client = app.test_client()
    res = client.get('/members')
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert len(data) == 2
