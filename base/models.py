from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Post(models.Model):
    image = CloudinaryField('image')
    image_name = models.TextField()
    caption = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    message = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True)

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

class Profile(models.Model):
    profile_photo = CloudinaryField('profile_photo')
    bio = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

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
        return self.body[:50]

    class Meta:
        ordering = ['updated', 'created']
