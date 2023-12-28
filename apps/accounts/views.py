from typing import Any
from urllib.parse import urlparse
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView

from .forms import UserSigninForm, UserSignupForm


class NotAuthenticatedMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class SignupView(CreateView):

    form_class = UserSignupForm
    template_name = 'accounts/user_signup.html'
    success_url = reverse_lazy('signin')

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)

        if not request.user.is_anonymous:
            raise Http404

        return handler


class SigninView(LoginView):

    form_class = UserSigninForm
    template_name = 'accounts/user_signin.html'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('letter-list')


class SignoutView(LogoutView):

    @method_decorator(never_cache)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        super().dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('signin'))
