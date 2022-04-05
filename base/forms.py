from .models import Post
from django.forms import ClearableFileInput, ModelForm, TextInput, Textarea
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author','user_posts','likes']
        widgets = {
            'image' :  ClearableFileInput (attrs={'class':'post-form-image'}),
            'image_name' : TextInput(attrs={'class':'post-form-imagename'}),
            'caption' : Textarea(attrs={'class':'post-form-caption', 'rows':4, 'cols':35}),
        }
