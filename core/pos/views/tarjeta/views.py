from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.pos.forms import TarjetaForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.pos.models import Tarjeta


class TarjetaListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Tarjeta
    template_name = 'tarjeta/list.html'
    permission_required = 'view_tarjeta'
    url_redirect = reverse_lazy('dashboard')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                for i in Tarjeta.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de tarjetas'
        context['create_url'] = reverse_lazy('tarjeta_create')
        context['list_url'] = reverse_lazy('tarjeta_list')
        context['entity'] = 'Tarjetas'
        return context


class TarjetaCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Tarjeta
    form_class = TarjetaForm
    template_name = 'tarjeta/create.html'
    success_url = reverse_lazy('tarjeta_list')
    permission_required = 'add_tarjeta'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una tarjeta'
        context['entity'] = 'Tarjetas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class TarjetaUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Tarjeta
    form_class = TarjetaForm
    template_name = 'tarjeta/create.html'
    success_url = reverse_lazy('tarjeta_list')
    permission_required = 'change_tarjeta'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una tarjeta'
        context['entity'] = 'Tarjetas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class TarjetaDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Tarjeta
    template_name = 'tarjeta/delete.html'
    success_url = reverse_lazy('tarjeta_list')
    permission_required = 'delete_tarjeta'
    url_redirect = success_url

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una tarjeta'
        context['entity'] = 'Tarjetas'
        context['list_url'] = self.success_url
        return context
