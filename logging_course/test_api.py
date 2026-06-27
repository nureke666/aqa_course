from api_clients import api_call


def test_reqres_api():
    api_call("GET", "https://reqres.in/api/users/2")
    api_call("POST", "https://reqres.in/api/register", json={"email": "sydney@fife"})
    assert 1 == 0
