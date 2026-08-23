from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task, Submission
from rest_framework.decorators import api_view
from rest_framework.response import Response

#for DRF
from rest_framework import viewsets
from .serializers import TaskSerializer, SubmissionSerializer
from .permissions import IsAdminOrStaffOrReadOnly



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('explore')
        else:
            return render(request, 'dashboard/login.html', {'error': 'Invalid credentials'})
    return render(request, 'dashboard/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def explore_view(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        task_id = request.POST['task_id']
        task = Task.objects.get(id=task_id)
        Submission.objects.get_or_create(user=request.user, task=task)
        return redirect('dashboard')
    return render(request, 'dashboard/explore.html', {'tasks': tasks})

@login_required
def dashboard_view(request):
    submissions = Submission.objects.filter(user=request.user).select_related('task')
    return render(request, 'dashboard/dashboard.html', {'submissions': submissions})

#for api
@api_view(['GET'])
def api_tasks(request):
    tasks = Task.objects.values('id', 'title', 'description')
    return Response(list(tasks))


def home_view(request):
    if request.user.is_authenticated:
        return redirect('explore')
    return redirect('login')


#------------------------------------------------


#for DRF

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrStaffOrReadOnly]

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.select_related('task', 'user').all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAdminOrStaffOrReadOnly]