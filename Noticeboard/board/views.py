from django.shortcuts import render, redirect
from .models import Notice
from .forms import NoticeForm

#Home page view
def home_view(request):
    notices = Notice.objects.all().order_by('-created_at')[:10]
    return render(request, 'board/home.html', {'notices': notices})

#About page view
def about_view(request):
    return render(request, 'board/about.html')

#Notices page view
def notices(request):
    """
    Handles:
    - Displaying all notices
    - Creating new notices via form submission
    """
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()  #Save the new notice to the database
            return redirect('notices')  #Reload the page to show the new notice
    else:
        form = NoticeForm()  #Empty form for GET request

    #Fetch all notices from the database, newest first
    all_notices = Notice.objects.all().order_by('-created_at')

    #Render the template with the form and all notices
    return render(request, 'board/notices.html', {
        'form': form,
        'notices': all_notices
    })