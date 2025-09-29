from django.shortcuts import render, redirect, HttpResponse
from users.forms import CustomRegistrationForm, LoginForm , AssignRoleForm, CreateGroupForm
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User, Group
from django.contrib.auth import login , logout
from events.models import Event
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test


def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_organizer(user):
    return user.groups.filter(name='Organizer').exists()

def is_participant(user):
    return user.groups.filter(name='Participant').exists()

def user_registration(request):
    if request.method == 'GET':
        form = CustomRegistrationForm()
    elif request.method == 'POST':
        form = CustomRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.is_active = False
            user.save()
            messages.success(request, 'Verification Mail is already sent your mail.please check and acivate your account')

    return render(request, 'user_registration.html', {'form': form})


def activate_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user , token):
            user.is_active = True
            user.save()
            return redirect('sign-in')
        else:
            return HttpResponse('Token is invalid')
    except User.DoesNotExist:
        return HttpResponse('User Not Found')


def app_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html', {'form':form})

@login_required
def app_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sign-in')
@login_required
@user_passes_test(is_admin , login_url='home')
def admin_dashboard(request):
    users = User.objects.prefetch_related('groups').all()
    for user in users:
        if user.groups.exists():
            user.group_name = user.groups.first().name
        else:
            user.group_name = 'No Group Assigned'

    return render(request, 'dashboard.html', {'users':users})

@login_required
@user_passes_test(is_admin, login_url='home')
def assign_role(request, id):
    user = User.objects.get(id=id)
    form = AssignRoleForm()

    if request.method == 'POST':
        form = AssignRoleForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('role')
            user.groups.clear()
            user.groups.add(role)
            messages.success(request, f'Role Changed for {user.username}')
            return redirect('admin-dashboard')

    return render(request, 'assign_role.html', {'form':form})

@login_required
@user_passes_test(is_admin, login_url='home')
def create_group(request):
    form = CreateGroupForm()
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            messages.success(request, f'{group.name} is created')
            return redirect('admin-dashboard')

    return render(request, 'create_group.html', {'form':form})

@login_required
@user_passes_test(is_admin, login_url='home')
def group_list(request):
    groups = Group.objects.prefetch_related('permissions').all()
    return render(request, 'group_list.html', {'groups':groups})

def home(request):
    return HttpResponse('This is page is not for you')