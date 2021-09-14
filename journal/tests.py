from django.test import TestCase


# Create your tests here.
from journal.models import Resources


class ObjectTests(TestCase):

    def setUp(self):
        Resources.objects.create(
            name='Google',
            description_name = 'Social Media platform',
            url='http://www.google.com'
        )

        Resources.objects.create(
            name='Python',
            description_name='Programming Language',
            url='https://www.python.org/',
            topic='Developing'
        )

    def test_create_resource(self):
        google = Resources.objects.get(name="Google")
        python = Resources.objects.get(name="Python")
        print(google)
        self.assertEqual(str(google.description_name()), 'Programming Language')
        self.assertEqual(python.topic(), 'Developing')

