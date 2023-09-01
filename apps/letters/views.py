from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import Http404, HttpResponse
from django.views.generic import CreateView, DetailView, ListView

from .models import Letter


class LetterCreateView(CreateView):

    model = Letter
    template_name = 'letters/letter_create.html'
    fields = [
        'addressee',
        'title',
        'text',
    ]

    def form_valid(self, form) -> HttpResponse:
        """Fill the author automatically."""
        form.instance.author = self.request.user

        return super().form_valid(form)


class LetterDetailView(DetailView):

    model = Letter
    template_name = 'letters/letter_detail.html'

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        letter = self.get_object()
        if not (letter.author == user or letter.addressee == user):
            raise Http404
        return handler


class LetterListView(LoginRequiredMixin, ListView):

    model = Letter
    context_object_name = 'letter_list'
    paginate_by = 25
    template_name = 'letters/letter_list.html'

    def get_queryset(self) -> QuerySet:
        return Letter.objects.my_letters(self.request.user)
