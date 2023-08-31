from django.urls import include, path

from .views import LetterListView, LetterDetailView

urlpatterns = [
    path('', LetterListView.as_view(), name='letter-list'),
    path('<pk>', LetterDetailView.as_view(), name='letter-detail')
]
