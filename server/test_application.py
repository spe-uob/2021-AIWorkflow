from itsdangerous import json
import pytest
from server import application

json = application.JSONResponse

def test_api():
    assert json == {"message": "app is running", "success": True}
