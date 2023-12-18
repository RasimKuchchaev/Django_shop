from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    student_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
