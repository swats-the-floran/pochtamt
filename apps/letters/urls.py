from django.urls import path

from .views import LetterCreateView, LetterListView, LetterDetailView

urlpatterns = [
    path('', LetterListView.as_view(), name='letter-list'),
    path('new', LetterCreateView.as_view(), name='letter-new'),
    path('<pk>', LetterDetailView.as_view(), name='letter-detail'),
]
