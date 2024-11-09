import pytest
from accounts.models import User
from utils.permissions import UserRole
from rest_framework import status


@pytest.mark.django_db
class TestUserRoles:
    def test_default_user_role(self, test_user):
        user = test_user()
        assert user.roles == UserRole.USER.value
        assert user.has_role(UserRole.USER)
        
    def test_custom_user_role(self, api_client):
        signup_data = {
            "username": "vipuser",
            "password": "test_password09",
            "nickname": "vipnick",
            "roles": UserRole.VIP.value
        }
        
        response = api_client.post('/api/accounts/signup/', signup_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['roles'] == UserRole.VIP.value
        
        user = User.objects.get(username="vipuser")
        assert user.has_role(UserRole.VIP)