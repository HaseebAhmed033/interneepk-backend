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