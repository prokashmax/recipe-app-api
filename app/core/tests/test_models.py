from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_email_successful(self):
        """Test create a new user with an email is successful"""
        email = 'prokashpul@gmail.com'
        password ='prokash2'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalized(self):
        """Test create a new user with an email is successful"""
        email = 'prokashpul2@GMAIL.com'
        password ='prokash2'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email.lower())
    def test_create_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "prokash2")

    def test_create_user_new_superuser(self):
        """test creating superuser"""
        user = get_user_model().objects.create_superuser(
            'prokashpul2@gmail.com',
            'prokash2'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)