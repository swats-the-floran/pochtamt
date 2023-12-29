from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UserSignupForm(UserCreationForm):

	email = forms.EmailField(required=True)

	def save(self, commit=True):
		user = super(UserSignupForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()

		return user

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")


class UserSigninForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                _("This account is inactive."),
                code="inactive",
            )

