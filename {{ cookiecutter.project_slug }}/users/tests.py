import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertRedirects
from .models import User


@pytest.mark.django_db
def test_users():
    u = User.objects.create(username='testuser', email='test@email.com')

    with pytest.raises(Exception):
        u.set_manager(u)


@pytest.mark.django_db
def test_signup(client, user1):
    url = reverse('users:signup')
    resp = client.get(url)
    assertTemplateUsed(resp, 'users/signup.html')

    client.force_login(user1)

    resp = client.get(url)
    assertRedirects(resp, '/dashboard')


@pytest.mark.django_db
def test_login(client, user1):
    url = reverse('users:login')
    resp = client.get(url)
    assertTemplateUsed(resp, 'slack/login.html')

    client.force_login(user1)

    resp = client.get(url)
    assertTemplateUsed(resp, 'slack/login.html')


@pytest.mark.django_db
def test_logout(client, user1):
    logout_url = reverse('users:logout')
    login_url = reverse('users:login')
    dashboard_url = reverse('dashboard:dashboard')

    client.force_login(user1)
    resp = client.get(logout_url)
    assertRedirects(resp, login_url)

    resp = client.get(dashboard_url)
    assertRedirects(resp, login_url + '?next=' + dashboard_url)
