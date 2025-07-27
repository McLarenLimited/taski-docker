"""Модуль тестирования API для управления задачами."""
from http import HTTPStatus

from api import models
from django.test import Client, TestCase


class TaskiAPITestCase(TestCase):
    """Тест-кейсы для проверки работы API задач."""

    def setUp(self):
        """Инициализация тестового клиента перед каждым тестом."""
        self.guest_client = Client()

    def test_list_exists(self):
        """Проверка доступности эндпоинта списка задач."""
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Проверка создания новой задачи через API."""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.guest_client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
