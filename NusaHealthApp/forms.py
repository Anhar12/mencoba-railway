from django import forms
from .models import Blogs, Activities

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'category', 'body', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title', 'id': 'title'}),
            'category': forms.Select(attrs={'class': 'form-select', 'id': 'category'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here', 'rows': 5, 'id': 'body'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'image'}),
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title or title.strip() == '':
            raise forms.ValidationError("Title cannot be empty.")
        return title
    
    def clean_categories(self):
        categories = self.cleaned_data.get('categories')
        if not categories:
            raise forms.ValidationError("Categories cannot be empty.")
        return categories
    
    def clean_body(self):
        body = self.cleaned_data.get('body')
        if not body or body.strip() == '':
            raise forms.ValidationError("Body cannot be empty.")
        return body
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("An image is required.")
        if image and not image.content_type.startswith('image/'):
            raise forms.ValidationError("Uploaded file must be an image.")
        return image

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = ['title', 'body', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title', 'id': 'title'}),
            'category': forms.Select(attrs={'class': 'form-select', 'id': 'category'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here', 'rows': 5, 'id': 'body'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'image'}),
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title or title.strip() == '':
            raise forms.ValidationError("Title cannot be empty.")
        return title
    
    def clean_body(self):
        body = self.cleaned_data.get('body')
        if not body or body.strip() == '':
            raise forms.ValidationError("Body cannot be empty.")
        return body
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("An image is required.")
        if image and not image.content_type.startswith('image/'):
            raise forms.ValidationError("Uploaded file must be an image.")
        return image

