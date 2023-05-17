from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.pos.forms import PurchasePaidForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.pos.models import PurchasePaid


class PurchasePaidListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = PurchasePaid
    template_name = 'purchasePaid/list.html'
    permission_required = 'view_purchasePaid'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in PurchasePaid.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Pago de Compras'
        context['create_url'] = reverse_lazy('purchasePaid_create')
        context['list_url'] = reverse_lazy('purchasePaid_list')
        context['entity'] = 'Pagos'
        return context


class PurchasePaidCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = PurchasePaid
    form_class = PurchasePaidForm
    template_name = 'purchasePaid/create.html'
    success_url = reverse_lazy('purchasePaid_list')
    permission_required = 'add_purchasePaid'
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
        context['title'] = 'Creación de un Egreso'
        context['entity'] = 'Pagos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class PurchasePaidUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = PurchasePaid
    form_class = PurchasePaidForm
    template_name = 'purchasePaid/create.html'
    success_url = reverse_lazy('purchasePaid_list')
    permission_required = 'change_purchasePaid'
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
        context['title'] = 'Edición de un Egreso'
        context['entity'] = 'Pagos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class PurchasePaidDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = PurchasePaid
    template_name = 'purchasePaid/delete.html'
    success_url = reverse_lazy('purchasePaid_list')
    permission_required = 'delete_purchasePaid'
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
        context['title'] = 'Eliminación de un Egreso'
        context['entity'] = 'Pagos'
        context['list_url'] = self.success_url
        return context
