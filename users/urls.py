from django.urls import path
from users.views import user_registration, activate_user, app_login, app_logout,admin_dashboard, assign_role,create_group,ProfileView, group_list,home, EditProfileView, CustomPasswordChangeView, CustomPasswordResetView, CustomPasswordResetConfirmView
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path('sign-up/', user_registration, name='sign-up'),
    path('activate/<int:user_id>/<str:token>/', activate_user),
    path('sign-in/', app_login, name='sign-in'),
    path('logout/', app_logout, name='logout'),
    path('admin_dashboard', admin_dashboard, name='admin-dashboard'),
    path('change-role/<int:id>/', assign_role, name='assign-role'),
    path('create-group/', create_group , name='create-group'),
    path('group-list/', group_list, name='group-list'),
    path('home/' , home , name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path("edit-profile/", EditProfileView.as_view(), name="edit-profile"),
    path('change-password/', CustomPasswordChangeView.as_view(template_name='User/password_change.html'), name='password-change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='User/password_reset_done.html'), name='password-change-done'),
    path("password-reset/", CustomPasswordResetView.as_view(), name="password-reset"),
    path('password-reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm')
]
