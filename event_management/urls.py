from django.contrib import admin
from django.urls import path, include
from events.views import home, other


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('others/', other),
    path('events/',include("events.urls"))
]
