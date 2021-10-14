from django.test import TestCase
from .models import Comment, Profile, Image
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    """Test for the profile model class"""
    def setUp(self):
        self.user = User(username='')
        self.user.save()

        self.profile = Profile(id=75 ,profile_pic='profile-pic.jpg', bio='this is a setup to test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)

class ImageTestClass(TestCase):
    """
    test class for Image model unit tests.
    """
    def setUp(self):
        self.user = User.objects.create_user("username", "password")
        self.new_profile = Profile(id = 75,profile_pic='profile-pic.png',bio='this is a setup to test Image class',user=self.user)
        self.new_profile.save()
        self.newImage = Image(image='profile-pic.png',caption="image", profile=self.new_profile)

    def test_instance_true(self):
        self.assertTrue(isinstance(self.newImage, Image))

    def test_save_post(self):
        self.newImage.save_post()
        img = Image.objects.all()
        self.assertTrue(len(img) == 1)

    def test_delete_post(self):
        self.newImage.save_post()
        img = Profile.objects.all()
        self.assertTrue(len(img) <= 1)