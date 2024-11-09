import pytest
from rest_framework import status
from accounts.models import User
from utils.permissions import UserRole

@pytest.mark.django_db
class TestAuthentication:
    def test_user_signup(self, api_client):
        signup_data = {
            "username": "test_user",
            "password": "test_password09",
            "nickname": "test_nickname"
        }
        
        response = api_client.post('/api/accounts/signup/', signup_data)
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['username'] == signup_data['username']
        assert response.data['nickname'] == signup_data['nickname']
        assert response.data['roles'] == UserRole.USER.value
        
        user = User.objects.get(username=signup_data['username'])
        assert user.nickname == signup_data['nickname']
        assert user.has_role(UserRole.USER)

    def test_user_login(self, api_client, test_user, test_password):
        user = test_user()
        login_data = {
            "username": user.username,
            "password": test_password
        }
        
        response = api_client.post('/api/accounts/login/', login_data)
        
        assert response.status_code == status.HTTP_200_OK
        assert 'token' in response.data
