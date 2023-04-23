from django.shortcuts import render
from rest_framework import generics
from .models import Persona
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import PersonaForm
from django.contrib import messages
from .serializers import PersonaSerializer


def index(request):
    return render(request, 'django_application/index.html')


class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class PersonaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class PersonaCreate(generics.CreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class PersonaUpdate(generics.UpdateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class PersonaDelete(generics.DestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class PersonCreateView(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'django_application/person_create.html'
    success_url = reverse_lazy('person_success')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '¡Person created successfully!')
        return response


def person_success(request):
    return render(request, 'django_application/success.html')
