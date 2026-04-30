from django.db import models
from django.contrib.auth.models import User


class GymClass(models.Model):
    CATEGORY_CHOICES = [
        ('yoga', 'Yoga'),
        ('cardio', 'Cardio'),
        ('strength', 'Strength Training'),
        ('pilates', 'Pilates'),
        ('hiit', 'HIIT'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('boxing', 'Boxing'),
    ]

    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='cardio')
    schedule = models.DateTimeField()
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    capacity = models.PositiveIntegerField()
    location = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='intermediate')
    created_at = models.DateTimeField(auto_now_add=True)

    members = models.ManyToManyField(
        User,
        through='Booking',
        blank=True,
        related_name='gym_classes',
    )

    class Meta:
        ordering = ['schedule']

    def __str__(self):
        return self.name

    def spots_remaining(self):
        return self.capacity - self.booking_set.count()

    def booking_count(self):
        return self.booking_set.count()

    def is_full(self):
        return self.booking_set.count() >= self.capacity


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gym_class = models.ForeignKey(GymClass, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'gym_class')

    def __str__(self):
        return f'{self.user.username} — {self.gym_class.name}'
