from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'intro', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            "intro": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduction'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of the article'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of publication'
            })

        }
