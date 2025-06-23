from django.contrib.auth.forms import UserCreationForm

# We create a new form that extends from UserCreationForm

#  We will also set help_text of the form's fields to None to remove them: self.fields[fieldname].help_text = None

class UserCreateForm(UserCreationForm): 
  def __init__(self, *args, **kwargs): 
    super(UserCreateForm, self).__init__(*args, **kwargs)
    for fieldname in ['username', 'password1', 'password2']:
      self.fields[fieldname].help_text = None # type: ignore
      self.fields[fieldname].widget.attrs.update({ 
        'class': 'form-control'
      })