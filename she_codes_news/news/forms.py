from django import forms
from django.forms import ModelForm
from .models import NewsStory
from django.contrib.auth.forms import UserCreationForm

class StoryForm(ModelForm):
  class Meta:
    model = NewsStory
    fields = ['title', 'pub_date', 'content', 'img_url']
    widgets = {
      'pub_date': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
    }

class FilterForm(forms.Form):
  selectedAuthor = forms.ModelChoiceField(queryset=NewsStory.objects.all().order_by('-pub_date'), required=True)