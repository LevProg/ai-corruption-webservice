from django.urls import include
from django.urls import path,re_path
from .views import my_view, delete

urlpatterns = [
    path('', my_view, name='my-view'),
    path('delete/<int:id>/', delete),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]