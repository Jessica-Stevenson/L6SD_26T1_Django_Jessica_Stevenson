from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Notice
from .forms import NoticeForm
from .models import Notice, Profile
from .forms import NoticeForm, UserUpdateForm, ProfileUpdateForm

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    user_notices = Notice.objects.filter(user=request.user).order_by('-created_at')

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(request, 'board/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'notices': user_notices
    })

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