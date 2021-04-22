# SimpleTestCase which is a special subset of Django's TestCase that is designed for webpages that do not have a model included.
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


# It is best to be overly descriptive with our unit test names but
# be aware that each method must start with test to be run by the Django test suite.
class HomePageTests(SimpleTestCase):

    # Since the unit tests are executed top-to-bottom we can add a setup method that will be run before every test.
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    # We check that the HTTP status code for the homepage equals 200, that it means it exists.
    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_url_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    # To confirm that is uses the correct template
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")
        
    # Testing HTML: if our homepage has the correct HTML code and also doesn't have incorrect text.
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Homepage")
        
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")
        
    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

# docker-compose exec web python manage.py test (to run all the tests)
# docker-compose exec web python manage.py test pages (to run the tests only for the pages app)
