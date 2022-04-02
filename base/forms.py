from dataclasses import field
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author','message']
        # widgets = {
        #     'image' : 12,
        #     'email': 
        # }