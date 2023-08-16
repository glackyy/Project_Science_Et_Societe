from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import RegistrationForm, SearchForm, LoginForm
from .models import Page, BlogPost, ContactInfo
from .models import UserProfile


def home(request):
    return render(request, 'main/base.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})


def update_page(request, page_id):
    page = Page.objects.get(id=page_id)
    if request.method == 'POST':
        page.title = request.POST['title']
        page.content = request.POST['content']
        page.save()
        return redirect('page_detail', page_id=page_id)
    return render(request, 'main/update_page.html', {'page': page})


def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            results = User.objects.filter(username__icontains=search_query)
            return render(request, 'main/search.html', {'form': form, 'results': results})
        else:
            form = SearchForm()
        return render(request, 'main/search.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Invalid email or password'
    else:
        form = LoginForm()
        error_message = None
    
    context = {'form': form, 'error_message': error_message}
    return render(request, 'main/login.html', context)
# Create your views here.
