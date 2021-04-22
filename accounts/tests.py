# $ docker-compose exec web python manage.py test

from django.contrib.auth import get_user_model
from django.test import TestCase

# https://docs.djangoproject.com/en/3.2/ref/contrib/auth/


class CustomUserTests(TestCase):
    # test_create_user confirms that a new user can be created
    def test_create_user(self):
        User = get_user_model()
        # First we set our user model to the variable User and then create one via the manager method
        # create_user which does the actual work of creating a new user with the proper permissions.
        user = User.objects.create_user(
            username="codetron", email="codetron@email.com", password="testpass123"
        )

        self.assertEqual(user.username, "codetron")
        self.assertEqual(user.email, "codetron@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="testpass123"
        )

        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)