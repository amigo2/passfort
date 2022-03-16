from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.test import Client

from django.contrib.auth.models import User


class AccountTest(APITestCase, URLPatternsTestCase):

    urlpatterns = [
        path('create/', include('rest_framework.urls')),
        path('api-auth/', include('rest_framework.urls')),
    ]

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        self.client = Client()
        self.user = User(username="testuser", email="testemail@test.com")
        self.user.is_staff = True
        self.user.set_password('secret')
        self.user.save()

    def test_login(self):
        """
        Ensure user can login.
        """
        user = User.objects.create_user(username='test1', password='testpass')
        self.client.login(username=user.username, password='testpass')


class DocumentTest(APITestCase):

    def test_documents(self):
        """
        Connection success with documents
        """
        user = User.objects.create_user(username='test1', password='testpass')
        self.client.login(username=user.username, password='testpass')
        response = self.client.get('http://0.0.0.0:8000/documents')
        self.assertEqual(response.status_code, 200)


    def test_create_document(self):
        pass


