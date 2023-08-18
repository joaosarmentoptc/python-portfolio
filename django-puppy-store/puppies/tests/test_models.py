from django.test import TestCase
from ..models import Puppy

class PuppyTest(TestCase):
    def setUp(self):
        Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black'
        )
        Puppy.objects.create(
            name='Noah', age=6, breed='N/A', color='Yellow'
        )


    def test_puppy_breed(self):
        puppy_casper=Puppy.objects.get(name='Casper')
        puppy_noah=Puppy.objects.get(name='Noah')

        self.assertEquals(puppy_casper.get_breed(), 'Casper belongs to Bull Dog breed.')
        self.assertEquals(puppy_noah.get_breed(), 'Noah belongs to N/A breed.')
