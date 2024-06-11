from rest_framework.test import APITestCase
from .models import Task
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
# Create your tests here.
class TaskTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        user_class = get_user_model()
        cls.user = user_class.objects.create(username="john", email="foo@bar.com")
        cls.task = Task.objects.create(
            name="My Task", description="My task description", user=cls.user
        )
        refresh = RefreshToken.for_user(cls.user)
        cls.token = str(refresh.access_token)

    @classmethod
    def tearDownClass(cls):
        cls.task.delete()
        cls.user.delete()

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_get_task_list(self):
        url = reverse("task-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)

    def test_get_task_detail(self):
        url = reverse("task-detail", kwargs={"pk": self.task.id})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), self.task.name)
    
    def test_create_task(self):
        url = reverse("task-list")
        data = {"name": "New Task", "description": "New Task Description", "priority": "high"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("name"), "New Task")
    
    def test_update_task(self):
        url = reverse("task-detail", kwargs={"pk": self.task.id})
        data = {"name": "Updated Task", "description": "Updated Task Description", "priority": "medium","completed": False}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), "Updated Task")
    def test_partial_update_task(self):
        url = reverse("task-detail", kwargs={"pk": self.task.id})
        data = {"name": "Partially Updated Task"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), "Partially Updated Task")
    
    def test_delete_task(self):
        url = reverse("task-detail", kwargs={"pk": self.task.id})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())    