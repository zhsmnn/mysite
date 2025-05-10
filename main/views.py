from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Profile

# Главная страница
def index(request):
    return render(request, 'main/index.html')

# Страница проектов
def projects(request):
    return render(request, 'main/projects.html')

# Страница организаторам
def about(request):
    return render(request, 'main/about.html')

# Страница контактов
def contact(request):
    return render(request, 'main/contact.html')


# Регистрация нового пользователя
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # создаем профиль
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

# Профиль пользователя
@login_required
def profile(request):
    return render(request, 'main/profile.html')

def logout_view(request):
    logout(request)
    return redirect('index')
