from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    def test_create_user(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(email='user@user.com', password='user')
        self.assertEqual(user.email, 'user@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            user_model.objects.create_user()
        with self.assertRaises(TypeError):
            user_model.objects.create_user(email='')
        with self.assertRaises(ValueError):
            user_model.objects.create_user(email='', password="user")

    def test_create_superuser(self):
        user_model = get_user_model()
        admin_user = user_model.objects.create_superuser('superuser@user.com', 'user')
        self.assertEqual(admin_user.email, 'superuser@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            user_model.objects.create_superuser(
                email='superuser@user.com', password='user', is_superuser=False)
