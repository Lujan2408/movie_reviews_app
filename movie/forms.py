from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm): 
  # Bootstrap classes for form fields 
  def __init__(self, *args, **kwargs) : 
    super(ModelForm, self).__init__(*args, **kwargs)
    self.fields['text'].widget.attrs.update({
      'class': 'form-control'
    })
    self.fields['watchAgain'].widget.attrs.update({
      'class': 'form-check-input'
    })
  
  # specify which model the form is for and the fields we want in the form:
  class Meta: 
    model = Review
    fields = ['text', 'watchAgain'] # The fields we want to have/create
    labels = {
      'watchAgain': ('Watch Again') # This is what user is gonna see
    }
    widgets = {
      'text': Textarea(attrs={'rows': 4})
    }