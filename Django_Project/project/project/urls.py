from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('pages/', include('django.contrib.flatpages.urls')),
#    path('', TemplateView.as_view(template_name='home.html'), name='home'),
#]

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    #path('pages/', include('django.contrib.flatpages.urls')),  # Подключение flatpages
    path('', TemplateView.as_view(template_name='default.html')),  # Главная страница
]