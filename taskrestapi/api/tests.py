from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # User 1
        self.user1 = User.objects.create_user(username='harsh', password='password')
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        self.task1 = Task.objects.create(title='Task 1 by harsh', description='Description', due_date='2023-12-31', status='Pending', user=self.user1)

        # User 2
        self.user2 = User.objects.create_user(username='test', password='testpassword')
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)
        self.task2 = Task.objects.create(title='Task 2 by test', description='Description', due_date='2023-12-31', status='Pending', user=self.user2)

    def test_authentication(self):
        # Unauthenticated user shouldn't be able to access tasks
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Authenticated user should be able to access tasks
        response = self.client1.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task_authenticated(self):
        # Authenticated user should be able to create a task
        data = {'title': 'New Task by harsh', 'description': 'Description', 'due_date': '2023-12-31', 'status': 'Pending', 'user': self.user1.id}
        response = self.client1.post('/api/tasks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task_by_non_owner(self):
        # User 2 (test) shouldn't be able to update User 1's (harsh) task
        updated_data = {'title': 'Attempt to update Task 1 by test'}
        response = self.client2.put(f'/api/tasks/{self.task1.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_task_by_owner(self):
        # User 1 (harsh) should be able to delete their task
        response = self.client1.delete(f'/api/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # User 2 (test) should be able to delete their task
        response = self.client2.delete(f'/api/tasks/{self.task2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_task_by_non_owner(self):
        # User 2 (test) shouldn't be able to delete User 1's (harsh) task
        response = self.client2.delete(f'/api/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


