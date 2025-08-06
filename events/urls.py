from django.urls import path
from events.views import show_event,home, user,admin,create_event,update_event, delete_event , event_details
urlpatterns = [
    path('show-event/', show_event),
    path('user/', user, name='user'),
    path('admin/',admin , name='admin'),
    path('create-event/', create_event, name='create-event'),
    path('update-event/<int:id>/', update_event, name='update-event' ),
    path('delete-event/<int:id>/', delete_event, name='delete-event'),
    path('event-details/<int:id>/', event_details, name='event-details')
]
