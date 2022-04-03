from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Profile(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('profile_photo', blank=True)
    bio = models.TextField(blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['updated', 'created']

    def __str__(self):
        return self.user_profile.username

class Post(models.Model):
    image = CloudinaryField('image')
    image_name = models.TextField()
    caption = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile , on_delete=models.CASCADE)
    user_posts = models.ForeignKey(User , on_delete=models.CASCADE, null=True, blank=True)
    message = models.ForeignKey("Comment", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ['-updated', '-created']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls,pk):
        return cls.objects.get(id=pk)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]

    class Meta:
        ordering = ['updated', 'created']

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['updated', 'created']
