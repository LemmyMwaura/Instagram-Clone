from django.test import TestCase
from .models import Post, Profile, Comment
from django.contrib.auth.models import User

class InstagramClone(TestCase):
    @classmethod
    def setUpTestData(cls):
        '''
        Sets up the default ID field for the Object below in the database. (Django doesn't reset auto ID fields 
        for each test case)
        Saves the new objects id.
        '''
        cls.obj_id = User.objects.create_user(
            username='testdata',
            email='test@test.com',
            password='test1234'
        ).pk 

    def setUp(self):
        '''
        The setup method will run before each test case
        '''
        self.user = User.objects.create_user(
            username='lemmy',
            email='lemmy@lemmy.com',
            password='lemmy1234'
        )
        login = self.client.login(username='lemmy',password='lemmy1234')

        self.profile = Profile.objects.get(
            user_profile=User.objects.get(username='lemmy'),
            profile_photo='/images/stored',
            bio='Today is a good day',
        )
        self.post = Post.objects.create(
            image='image/link',
            image_name='image of a car',
            caption='Today is a good day',
            author=Profile.objects.get(bio='Today is a good day'),
            user_posts=User.objects.get(username='lemmy'),
        )
        self.comment = Comment.objects.create(
            user= User.objects.get(username='lemmy'),
            post_to_comment = Post.objects.get(caption='Today is a good day'),
            body='This is a comment'
        )

    def tearDown(self):
        '''
        The teardown method does the cleanup after each test has run.
        '''
        User.objects.all().delete()
        Profile.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()

    def test_instance(self):
        '''
        Test the instance of each object
        '''
        self.assertTrue(isinstance(self.user, User))
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertTrue(isinstance(self.post, Post))
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_objects(self):
        '''
        test_save_image test case to test if the image object is saved into
        the db.
        '''
        self.post = Post.objects.create(
            image='image/link',
            image_name='image of a car',
            caption='Today is a good day',
            author=Profile.objects.get(bio='Today is a good day',),
            user_posts=User.objects.get(username='lemmy'),
        )
        self.post.save_image()

        posts = Post.objects.all()
        self.assertEqual(len(posts), 2)

    def test_delete_objects(self):
        '''
        test_delete_image test case to test if the image object is removed from
        the db.
        '''
        # Images
        self.post.delete_image()
        posts = Post.objects.all()
        self.assertEqual(len(posts), 0)

