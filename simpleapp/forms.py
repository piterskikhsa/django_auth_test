from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class SingUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'checkin-form__input'
            visible.field.widget.attrs['placeholder'] = ' '


class SimpleUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email',)


class SimpleUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)
