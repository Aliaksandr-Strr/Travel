from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import TrainForm
from .models import Train


def home(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 2)
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    return render(request, 'trains/home.html', {'objects_list': trains, })


class TrainCreatView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('train:home')
    success_message = 'Поезд успешно создан'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    context_object_name = 'object'
    template_name = 'trains/detail.html'


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('train:home')
    success_message = 'Поезд успешно отредактирован'


class TrainDeleteView(DeleteView):
    model = Train
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('train:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Поезд успешно удален!')
        return self.post(request, *args, **kwargs)
