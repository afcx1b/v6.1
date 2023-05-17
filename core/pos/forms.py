from django import forms
from django.forms import ModelForm

from core.pos.models import *


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'desc': forms.TextInput(attrs={'placeholder': 'Ingrese una descripción'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ingrese un nombre',
            }),
            'category': forms.Select(attrs={
                'class': 'select2',
                'style': 'width: 100%'
            }),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre completo'}),
            'dni': forms.TextInput(attrs={'placeholder': 'Ingrese un número de cedula'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese un número de teléfono'}),
            'correo': forms.TextInput(attrs={'placeholder': 'Ingrese el correo electrónico'}),
            'address': forms.TextInput(attrs={'placeholder': 'Ingrese una dirección'}),
            'ciudad': forms.Select(attrs={
                'class': 'select2',
                'style': 'width: 100%'
            }),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class SupplierForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Supplier
        fields = '__all__'
        widgets = {
            'names': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre completo'}),
            'dni': forms.TextInput(attrs={'placeholder': 'Ingrese un número de cedula'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese un número de teléfono'}),
            'contacto': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del contacto'}),
            'address': forms.TextInput(attrs={'placeholder': 'Ingrese una dirección'}),
            'ciudad': forms.Select(attrs={
                'class': 'select2',
                'style': 'width: 100%'
            }),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.none()

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'client': forms.Select(attrs={
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
            'date_joined': forms.DateInput(format='%Y-%m-%d', attrs={
                'value': datetime.now().strftime('%Y-%m-%d'),
                'autocomplete': 'off',
                'class': 'form-control datetimepicker-input',
                'id': 'date_joined',
                'data-target': '#date_joined',
                'data-toggle': 'datetimepicker'
            }
                                           ),
            'iva': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'subtotal': forms.TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'total': forms.TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            })
        }


class PurchaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].queryset = Supplier.objects.none()

    class Meta:
        model = Purchase
        fields = '__all__'
        widgets = {
            'supplier': forms.Select(attrs={
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
            'date_joined': forms.DateInput(format='%Y-%m-%d', attrs={
                'value': datetime.now().strftime('%Y-%m-%d'),
                'autocomplete': 'off',
                'class': 'form-control datetimepicker-input',
                'id': 'date_joined',
                'data-target': '#date_joined',
                'data-toggle': 'datetimepicker'
            }
                                           ),
            'iva': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'subtotal': forms.TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'total': forms.TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            })
        }


class CompanyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese la Razón Social o Nombre completo'}),
            'ruc': forms.TextInput(attrs={'placeholder': 'Ingrese RUC / Cédula'}),
            'address': forms.TextInput(attrs={'placeholder': 'Ingrese una dirección'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Ingrese un teléfono celular'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ingrese un teléfono convencional'}),
            'website': forms.TextInput(attrs={'placeholder': 'Ingrese una dirección web'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class TarjetaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero_tarjeta'].widget.attrs['autofocus'] = True

    class Meta:
        model = Tarjeta
        fields = '__all__'
        widgets = {
            'numero_tarjeta': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el número de la tarjeta',
                }
            ),
            'mes_vencimiento': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el mes de vencimiento Ej: 03',
                }
            ),
            'ano_vencimiento': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el año de vencimiento Ej: 2028',
                }
            ),
            'cod_seguridad': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el código de seguridad de 3 dígitos',
                }
            ),
            'tipTar': forms.Select(),
            'bcoEmi': forms.Select()
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class SalePaidForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sale'].widget.attrs['autofocus'] = True

    class Meta:
        model = SalePaid
        fields = '__all__'
        widgets = {
            'sale': forms.Select(
                attrs={
                    'class': 'custom-select select2',
                }
            ),
            'voucher': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el número del voucher'
                }
            ),
            'tarjeta': forms.Select(),
            'date_joined': forms.DateInput(format='%Y-%m-%d',
                                           attrs={
                                               'value': datetime.now().strftime('%Y-%m-%d'),
                                           }
                                           ),
            'tipPago': forms.Select(),
            'cuotas': forms.TextInput(
                attrs={
                    'placeholder': '# de Cuotas'
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class PurchasePaidForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['purchase'].widget.attrs['autofocus'] = True

    class Meta:
        model = PurchasePaid
        fields = '__all__'
        widgets = {
            'purchase': forms.Select(attrs={
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
            'factura': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el número de factura'
                }
            ),
            'date_joined': forms.DateInput(format='%Y-%m-%d',
                                           attrs={
                                               'value': datetime.now().strftime('%Y-%m-%d'),
                                           }
                                           ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
