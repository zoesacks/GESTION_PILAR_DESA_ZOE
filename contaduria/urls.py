from django.urls import path

from contaduria.views import *

urlpatterns = [
    path('aplicaciones/', aplicaciones_contaduria, name='aplicaciones'),
    path('ingresos/', ingresos_contaduria, name='ingresos'),
    path('gastos/', gastos_contaduria, name='gastos'),
    path('gastos/asientosgasto/', asientos_gastos, name='asientosgastos'),
    path('gastos/proyecciongasto/', proyeccion_gastos, name='proyecciongasto'),
    path('prestamos/', prestamos, name='prestamos'),
    path('ingresos/asientosingresos/', asientosingresos, name='asientosingresos'),
    path('ingresos/proyeccioningresos/', proyeccioningresos, name='proyeccioningresos'),
    path('redeterminaciones/', aplicaciones_redeterminaciones, name='redeterminaciones'),
]

'''
urlpatterns = [
    path('aplicaciones/', aplicaciones_contaduria, name='aplicaciones'),
  
    path('ingresos/', ingresos_contaduria, name='ingresos'),
    
    path('prestamos/', prestamos, name='prestamos'),
    path('ingresos/asientosingreso/', asientosingreso, name='asientosingreso'),
    path('ingresos/proyeccioningreso/', proyeccioningresos, name='proyeccioningresos'),
    path('gastos/asientosgasto/', asientosgasto, name='asientosgasto'),
    path('gastos/proyecciongasto/', proyecciongasto, name='proyecciongasto'),
    
]
'''