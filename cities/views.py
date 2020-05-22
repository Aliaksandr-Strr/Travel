from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from .forms import CityForm
from .models import City


def home(request):
    if request.method == 'POST':
        form = CityForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
    form = CityForm()
    city = request.POST.get('name')
    cities = City.objects.all()
    return render(request, 'cities/home.html', {'objects_list': cities, 'cities': form})


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'


class CityCreatView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('city:home')


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('city:home')


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('city:home')
