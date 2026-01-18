from django.urls import path
from events.views import show_event,home, user,organizer,create_event,update_event, delete_event , event_details, rsvp_event,participated_events,dashboard, CreateEvent, UpdateEvent, DeleteEvent, Organizer,UserDashboard
urlpatterns = [
    path('show-event/', show_event),
    # path('user/', user, name='user'),
    path("user/", UserDashboard.as_view(), name="user"),
    # path('organizer/',organizer , name='organizer'),
    path("organizer/", Organizer.as_view(), name="organizer"),
    path('create-event/', CreateEvent.as_view(), name='create-event'),
    path('update-event/<int:id>/', UpdateEvent.as_view(), name='update-event' ),
    # path('delete-event/<int:id>/', delete_event, name='delete-event'),
    path('delete-event/<int:id>/', DeleteEvent.as_view(), name='delete-event'),
    path('event-details/<int:id>/', event_details, name='event-details'),
    path('rsvp-event/<int:event_id>/', rsvp_event, name='rsvp-event'),
    path('participated-event/<int:user_id>/', participated_events, name='participated-event'),
    path('dashboard/', dashboard, name='dashboard')
]
