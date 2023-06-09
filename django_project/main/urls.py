from django.urls import path
from .views import ParticipationListView, ParticipationRegistrationView

urlpatterns = [
    path('', ParticipationListView.as_view(), name='home'),
    path('registration/', ParticipationRegistrationView.as_view(), name='registration'),
]