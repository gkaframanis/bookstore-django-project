# $ docker-compose exec web python manage.py test accounts

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView

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


class SinglePageTests(TestCase):

    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")
        
    def test_signup_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")
        
    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
