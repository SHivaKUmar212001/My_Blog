from django import forms
from django.forms import ModelForm, DateInput
from .models import Post
class EventForm(forms.ModelForm):
  class Meta:
    model = Post
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'created_at': DateInput(),
         }
    fields = '__all__'
