from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Task, Submission

User = get_user_model()

class DashboardTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.task = Task.objects.create(title='Sample Task', description='Test description')

    def test_login_required_for_dashboard(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 302)  # redirects to login

    def test_login_and_dashboard_access(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_submission_creation(self):
        self.client.login(username='testuser', password='testpass123')
        self.client.post('/explore/', {'task_id': self.task.id})
        self.assertTrue(Submission.objects.filter(user=self.user, task=self.task).exists())

        from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from users.models import User
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        # Runs before every single test below — sets up fresh fake data
        self.client = APIClient()
        self.staff_user = User.objects.create_user(
            username='teststaff', password='pass12345', role='staff'
        )
        self.normal_user = User.objects.create_user(
            username='testuser', password='pass12345', role='user'
        )
        self.task = Task.objects.create(
            title='Sample Task', description='Sample', status='pending'
        )

    def test_normal_user_cannot_create_task(self):
        self.client.login(username='testuser', password='pass12345')
        response = self.client.post('/api/tasks/', {
            'title': 'New Task', 'description': 'Test', 'status': 'pending'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_staff_user_can_create_task(self):
        self.client.login(username='teststaff', password='pass12345')
        response = self.client.post('/api/tasks/', {
            'title': 'New Task', 'description': 'Test', 'status': 'pending'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_authenticated_user_can_read_tasks(self):
        self.client.login(username='testuser', password='pass12345')
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from users.models import User
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.staff_user = User.objects.create_user(
            username='teststaff', password='pass12345', role='staff'
        )
        self.normal_user = User.objects.create_user(
            username='testuser', password='pass12345', role='user'
        )
        self.task = Task.objects.create(
            title='Sample Task', description='Sample description'
        )

    def test_normal_user_cannot_create_task(self):
        self.client.login(username='testuser', password='pass12345')
        response = self.client.post('/api/tasks/', {
            'title': 'New Task', 'description': 'Test description'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_staff_user_can_create_task(self):
        self.client.login(username='teststaff', password='pass12345')
        response = self.client.post('/api/tasks/', {
            'title': 'New Task', 'description': 'Test description'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_authenticated_user_can_read_tasks(self):
        self.client.login(username='testuser', password='pass12345')
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)