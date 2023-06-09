from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Participation
from .forms import ParticipationForm


class ParticipationListView(ListView):
    model = Participation
    template_name = 'home.html'


class ParticipationRegistrationView(ListView):
    model = Participation
    form_class = ParticipationForm
    template_name = 'registration.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form})