from django.urls import path

from core.contabilidad.main import views

app_name = 'main'
urlpatterns = [
    path('cuentas/', views.CuentasView.as_view(), name='cuentas'),
    path('cuentas/pag/<int:pag>/', views.CuentasView.as_view(), name='cuentas_pagina'),
    path('cuentas/modificar/<str:num>/', views.ModificarCuentaView.as_view(), name='modificar_cuenta'),
    path('cuentas/borrar/<slug:pk>/', views.borrar_cuenta, name='borrar_cuenta'),
    path('cuentas/borrar/', views.borrar_multiples_cuentas, name='borrar_cuenta_multiple'),
    path('cuentas/cargar/', views.CargarCuentas.as_view(), name='cargar_cuentas'),
    path('cuentas/filtro/', views.filtro_cuentas, name='filtro_cuentas'),
    path('cuentas/etiqueta/gestionar/', views.gestionar_etiqueta, name='gestionar_etiqueta'),

    path('asientos/', views.AsientosView.as_view(), name='asientos'),
    path('asientos/pag/<int:pag>/', views.AsientosView.as_view(), name='asientos_pagina'),
    path('asientos/modificar/<int:num>/', views.ModificarAsientoView.as_view(), name='modificar_asiento'),
    path('asientos/cargar/', views.CargarAsientos.as_view(), name='cargar_asientos'),
    path('asientos/filtro/', views.filtro_asientos, name='filtro_asientos'),

    path('movimiento/anadir/<int:num>/<slug:fecha>/', views.anadir_movimiento, name='anadir_movimiento'),
    path('movimiento/borrar/<int:pk>/<slug:pagina>/', views.borrar_movimiento, name='borrar_movimiento'),
    path('movimiento/borrar/<int:pk>/<slug:pagina>/<int:num_asiento>/', views.borrar_movimiento,
         name='borrar_movimiento_complejo'),
    path('movimiento/borrar/', views.borrar_multiples_movimientos, name='borrar_movimiento_multiple'),

    path('', views.IndexView.as_view(), name='conta'),
    path('cambiar/orden/<str:tipo>/<str:campo>/', views.cambiar_orden, name='cambiar_orden'),
    path('informes/', views.InformesView.as_view(), name='informes'),
]
