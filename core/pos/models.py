from datetime import datetime

# from config.settings import AUTH_USER_MODEL
from django.db import models
from django.db.models import Sum, F, FloatField
from django.db.models.functions import Coalesce
from django.forms import model_to_dict

from config import settings
from core.pos.choices import tipoPago_choices


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=150, verbose_name='Descripción', unique=False)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    image = models.ImageField(upload_to='product%Y%m%d', null=True, blank=True, verbose_name='Imagen')
    is_inventoried = models.BooleanField(default=True, verbose_name='¿Es inventariado?')
    stock = models.IntegerField(default=1, verbose_name='Stock')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')
    cto = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de costo')
    link = models.CharField(max_length=150, verbose_name='link')

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = self.__str__()
        item['category'] = self.category.toJSON()
        item['image'] = self.get_image()
        item['pvp'] = f'{self.pvp:.2f}'
        item['cto'] = f'{self.cto:.2f}'
        return item

    def get_image(self):
        if self.image:
            return f'{settings.MEDIA_URL}{self.image}'
        return f'{settings.STATIC_URL}img/empty.png'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class CiudadProvincia(models.Model):
    nombre = models.CharField(max_length=150, primary_key=True, help_text='Ciudad - Provincia')

    def __str__(self):
        return self.nombre


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres completos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Número de cedula')
    telefono = models.CharField(max_length=13, default='+593', unique=True, verbose_name='Número de teléfono')
    correo = models.CharField(max_length=150, unique=True, verbose_name='Correo electrónico')
    address = models.CharField(max_length=150, null=False, blank=False, verbose_name='Dirección')
    ciudad = models.ForeignKey(CiudadProvincia, on_delete=models.CASCADE, verbose_name='Ciudad - Provincia')

    # dniA = models.ImageField(upload_to='dniA%Y%m%d', null=True, blank=True, verbose_name='DNI Anverso')
    # dniR = models.ImageField(upload_to='dniR%Y%m%d', null=True, blank=True, verbose_name='DNI Reverso')

    def __str__(self):
        return self.names

    # def get_dniA(self):
    #     if self.dniA:
    #         return '{}{}'.format(MEDIA_URL, self.dniA)
    #     return '{}{}'.format(STATIC_URL, 'img/empty.png')

    # def get_dniR(self):
    #     if self.dniR:
    #         return '{}{}'.format(MEDIA_URL, self.dniR)
    #     return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def get_full_name(self):
        return f'{self.names} ({self.dni})'

    def toJSON(self):
        item = model_to_dict(self)
        # item['dniA'] = self.get_dniA()
        # item['dniR'] = self.get_dniR()
        item['full_name'] = self.get_full_name()
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Supplier(models.Model):
    names = models.CharField(max_length=150, verbose_name='Razón Social')
    dni = models.CharField(max_length=13, unique=True, verbose_name='RUC / Cédula')
    telefono = models.CharField(max_length=13, default='+593', unique=True, verbose_name='Número de teléfono')
    contacto = models.CharField(max_length=30, null=False, blank=False, verbose_name='Contacto')
    address = models.CharField(max_length=150, null=False, blank=False, verbose_name='Dirección')
    ciudad = models.ForeignKey(CiudadProvincia, on_delete=models.CASCADE, verbose_name='Ciudad - Provincia')

    def __str__(self):
        return self.names

    def get_full_name(self):
        return f'{self.names} ({self.dni})'

    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = self.get_full_name()
        return item

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['id']


class Company(models.Model):
    name = models.CharField(max_length=150, verbose_name='Razón Social')
    ruc = models.CharField(max_length=13, verbose_name='Ruc')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    mobile = models.CharField(max_length=13, default='+593', verbose_name='Teléfono Celular')
    phone = models.CharField(max_length=13, default='+593', verbose_name='Teléfono Convencional')
    website = models.CharField(max_length=150, default='https://', verbose_name='Website')
    image = models.ImageField(upload_to='company%Y%m%d', null=True, blank=True, verbose_name='Imagen')

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return f'{settings.MEDIA_URL}{self.image}'
        return f'{settings.STATIC_URL}img/empty.png'

    def toJSON(self):
        item = model_to_dict(self)
        item['image'] = self.get_image()
        return item

    class Meta:
        verbose_name = 'Compañia'
        verbose_name_plural = 'Compañias'
        default_permissions = ()
        permissions = (
            ('change_company', 'Can change Company'),
        )
        ordering = ['id']


class Sale(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total_iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client.names

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        if Company.objects.all().exists():
            self.company = Company.objects.first()
            # self.usuario = self.request.user
        super(Sale, self).save(*args, **kwargs)

    def get_number(self):
        return f'{self.id:06d}'

    def toJSON(self):
        item = model_to_dict(self)
        item['number'] = self.get_number()
        item['client'] = self.client.names
        item['subtotal'] = f'{self.subtotal:.2f}'
        item['iva'] = f'{self.iva:.2f}'
        item['total_iva'] = f'{self.total_iva:.2f}'
        item['total'] = f'{self.total:.2f}'
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['saleproduct'] = [i.toJSON() for i in self.saleproduct_set.all()]
        return item

    def delete(self, using=None, keep_parents=False):
        for detail in self.saleproduct_set.filter(product__is_inventoried=True):
            detail.product.stock += detail.cant
            detail.product.save()
        super(Sale, self).delete()

    def calculate_invoice(self):
        subtotal = self.saleproduct_set.all().aggregate(
            result=Coalesce(Sum(F('price') * F('cant')), 0.00, output_field=FloatField())).get('result')
        self.subtotal = subtotal
        self.total_iva = self.subtotal * float(self.iva)
        self.total = float(self.subtotal) + float(self.total_iva)
        self.save()

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.product.name

    def toJSON(self):
        item = model_to_dict(self, exclude=['sale'])
        item['product'] = self.product.toJSON()
        item['price'] = f'{self.price:.2f}'
        item['subtotal'] = f'{self.subtotal:.2f}'
        return item

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        default_permissions = ()
        ordering = ['id']


class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total_iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.supplier.names

    def get_number(self):
        return f'{self.id:06d}'

    def toJSON(self):
        item = model_to_dict(self)
        item['number'] = self.get_number()
        item['supplier'] = self.supplier.names
        item['subtotal'] = f'{self.subtotal:.2f}'
        item['iva'] = f'{self.iva:.2f}'
        item['total_iva'] = f'{self.total_iva:.2f}'
        item['total'] = f'{self.total:.2f}'
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['purchaseproduct'] = [i.toJSON() for i in self.purchaseproduct_set.all()]
        return item

    def delete(self, using=None, keep_parents=False):
        for detail in self.purchaseproduct_set.filter(product__is_inventoried=True):
            detail.product.stock += detail.cant
            detail.product.save()
        super(Purchase, self).delete()

    def calculate_invoice(self):
        subtotal = self.purchaseproduct_set.all().aggregate(
            result=Coalesce(Sum(F('price') * F('cant')), 0.00, output_field=FloatField())).get('result')
        self.subtotal = subtotal
        self.total_iva = self.subtotal * float(self.iva)
        self.total = float(self.subtotal) + float(self.total_iva)
        self.save()

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['id']


class PurchaseProduct(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.product.name

    def toJSON(self):
        item = model_to_dict(self, exclude=['purchase'])
        item['product'] = self.product.toJSON()
        item['price'] = f'{self.price:.2f}'
        item['subtotal'] = f'{self.subtotal:.2f}'
        return item

    class Meta:
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalle de Compras'
        default_permissions = ()
        ordering = ['id']


# class Tarjeta(models.Model):
#     numero_tarjeta = models.CharField(max_length=16, unique=True, blank=False, null=False,
#                                       verbose_name='Número de Tarjeta')
#     tipTar = models.CharField(max_length=10, choices=tipTar_choices, default='Visa', verbose_name='Tipo Tarjeta')
#     bcoEmi = models.CharField(max_length=20, choices=bancoEmi_choices, default='Pichincha', verbose_name='Emisor')
#     mes_vencimiento = models.CharField(max_length=2, verbose_name='Mes de Vencimiento')
#     ano_vencimiento = models.CharField(max_length=4, verbose_name='Año de Vencimiento')
#     cod_seguridad = models.CharField(max_length=4, verbose_name='Código de Seguridad')
#     client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
#
#     def __str__(self):
#         return self.get_full_name()
#
#     def get_full_name(self):
#         return '{} / {} {}'.format(self.client.names, self.numero_tarjeta, self.tipTar)
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         item['full_name'] = self.get_full_name()
#         item['tipTar'] = {'id': self.tipTar, 'name': self.get_tipTar_display()}
#         item['bcoEmi'] = {'id': self.bcoEmi, 'name': self.get_bcoEmi_display()}
#         item['client'] = self.client.names
#         return item
#
#     class Meta:
#         verbose_name = 'Tarjeta'
#         verbose_name_plural = 'Tarjetas'
#         ordering = ['id']


class SalePaid(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name='Cliente')
    voucher = models.CharField(max_length=10, default='0', unique=True, blank=True, null=True, verbose_name='Voucher')
    # tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha del Voucher')
    tipPago = models.CharField(max_length=10, choices=tipoPago_choices, default='Corriente', verbose_name='Tipo Pago')
    cuotas = models.CharField(max_length=2, null=False, blank=False, verbose_name='Coutas')
    valor = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Valor')
    regTel = models.FileField(upload_to='regTel%Y%m%d', null=True, blank=True, verbose_name='Registro Telefónico')
    regWA = models.FileField(upload_to='regWA%Y%m%d', null=True, blank=True, verbose_name='Registro WhatsApp')
    regPaid = models.FileField(upload_to='regPaid%Y%m%d', null=True, blank=True, verbose_name='Registro Pago')

    def __str__(self):
        return self.voucher

    def get_regTel(self):
        if self.regTel:
            return f'{settings.MEDIA_URL}{self.regTel}'
        return f'{settings.STATIC_URL}img/empty.png'

    def get_regWA(self):
        if self.regWA:
            return f'{settings.MEDIA_URL}{self.regWA}'
        return f'{settings.STATIC_URL}img/empty.png'

    def get_regPaid(self):
        if self.regPaid:
            return f'{settings.MEDIA_URL}{self.regPaid}'
        return f'{settings.STATIC_URL}img/empty.png'

    def toJSON(self):
        item = model_to_dict(self)
        item['sale'] = self.sale.get_number()
        # item['tarjeta'] = self.tarjeta.numero_tarjeta
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['tipPago'] = {'id': self.tipPago, 'name': self.get_tipPago_display()}
        item['valor'] = f'{self.valor:.2f}'
        item['regTel'] = self.get_regTel()
        item['regWA'] = self.get_regWA()
        item['regPaid'] = self.get_regPaid()
        return item

    class Meta:
        verbose_name = 'Pago de Venta'
        verbose_name_plural = 'Pago de Ventas'
        ordering = ['id']


class PurchasePaid(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, verbose_name='Número Factura')
    factura = models.CharField(max_length=10, default='0', unique=True, blank=True, null=True, verbose_name='Factura')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de la factura')
    valor = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Valor')

    def __str__(self):
        return self.factura

    def toJSON(self):
        item = model_to_dict(self)
        item['purchase'] = self.purchase.get_number()
        item['valor'] = f'{self.valor:.2f}'
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Pago de Compra'
        verbose_name_plural = 'Pago de Compras'
        ordering = ['id']
