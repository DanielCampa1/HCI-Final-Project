from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'project_apps/home.html')