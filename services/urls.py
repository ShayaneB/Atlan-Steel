from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name = 'services'),
    path('Slabs', views.Slabs, name = 'Slabs'),
    path('Plates', views.Plates, name = 'Plates'),
    path('Coils', views.Coils, name = 'Coils'),
    # path('pipe', views.pipe, name = 'pipe'),
    # path('tanks', views.tanks, name = 'tanks'),
    # path('stacks', views.stacks, name = 'stacks'),
]