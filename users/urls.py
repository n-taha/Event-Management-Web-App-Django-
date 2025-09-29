from django.urls import path
from users.views import user_registration, activate_user, app_login, app_logout,admin_dashboard, assign_role,create_group,group_list,home

urlpatterns = [
    path('sign-up/', user_registration, name='sign-up'),
    path('activate/<int:user_id>/<str:token>/', activate_user),
    path('sign-in/', app_login, name='sign-in'),
    path('logout/', app_logout, name='logout'),
    path('admin_dashboard', admin_dashboard, name='admin-dashboard'),
    path('change-role/<int:id>/', assign_role, name='assign-role'),
    path('create-group/', create_group , name='create-group'),
    path('group-list/', group_list, name='group-list'),
    path('home/' , home , name='home')
]
