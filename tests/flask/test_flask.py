''' test_flask.py - Tests for Flask server '''

import requests

def test_server_not_running():
    ''' Tests if the server is not running.'''
    try:
        response = requests.get("http://localhost:5000/")
        assert response.status_code != 200
    except requests.exceptions.ConnectionError:
        assert True
