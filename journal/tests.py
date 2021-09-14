from django.test import TestCase

# Create your tests here.
from journal.models import Resources
from journal.views import delete_resource, ResourceCreate
from django.test import RequestFactory


class ObjectTests(TestCase):

    def setUp(self):
        Resources.objects.create(
            name='Google',
            description_name='Social Media platform',
            url='https://www.google.com')

        Resources.objects.create(
            name='Python',
            description_name='Programming Language',
            url='https://www.python.org/',
            topic='Developing'
        )
        self.factory = RequestFactory()
        self.res_id = Resources.id

    def test_create_resource(self):
        google = Resources.objects.get(name="Google")
        python = Resources.objects.get(name="Python")
        self.assertEqual(google.description_name, "Social Media platform")
        self.assertEqual(google.name, "Google")
        self.assertEqual(google.url, "https://www.google.com")
        self.assertEqual(google.topic, 'other')
        self.assertEqual(python.description_name, "Programming Language")
        self.assertEqual(python.name, "Python")
        self.assertEqual(python.url, "https://www.python.org/")
        self.assertEqual(python.topic, 'Developing')

    def test_home_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_search_url(self):
        response = self.client.get('/search/?q=google')
        self.assertEqual(response.status_code, 200)

    def test_add_resource_url(self):
        response = self.client.get('/journal/resource_create/')
        self.assertEqual(response.status_code, 200)

    def test_resources_delete(self):
        request = self.factory.post('/delete_resource/' + str(self.res_id))
        response = delete_resource(request, self.res_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Resources.objects.filter(name='Google').count(), 0)

    def test_add_resources(self):
        request = self.factory.get('/resource_create/')
        response = ResourceCreate.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(Resources.objects.filter(name='Google').count(), 1)
