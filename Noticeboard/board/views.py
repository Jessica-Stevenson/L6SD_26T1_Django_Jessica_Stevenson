from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Notice
from .forms import NoticeForm

#Home Page View
def home_view(request):
    #Show latest 10 notices
    notices = Notice.objects.all().order_by('-created_at')[:10]
    return render(request, 'board/home.html', {'notices': notices})

#About Page View
def about_view(request):
    return render(request, 'board/about.html')

#Sign Up View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

#Notices Page View
@login_required
def notices(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.user = request.user
            notice.save()
            return redirect('notices')
    else:
        form = NoticeForm()

    all_notices = Notice.objects.all().order_by('-created_at')

    return render(request, 'board/notices.html', {
        'form': form,
        'notices': all_notices
    })