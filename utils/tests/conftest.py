import pytest
from rest_framework.test import APIClient
from accounts.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_password():
    return 'test_password09'


@pytest.fixture
def test_user(test_password):
    def create_user(username='test_user', nickname='test_nickname'):
        user = User.objects.create_user(
            username=username,
            password=test_password,
            nickname=nickname,
        )
        return user
    return create_user
