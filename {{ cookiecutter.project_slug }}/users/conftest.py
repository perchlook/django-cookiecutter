import pytest

from .models import User


@pytest.fixture
def user1():
    user = User.objects.create(username='a@b.com', first_name='A', email='a@b.com')
    return user
