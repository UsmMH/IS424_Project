from django.contrib import admin
from .models import GymClass, Booking


@admin.register(GymClass)
class GymClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'instructor', 'schedule', 'capacity', 'difficulty']
    list_filter = ['category', 'difficulty']
    search_fields = ['name', 'instructor']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'gym_class', 'booked_at']
    list_filter = ['gym_class']
    search_fields = ['user__username', 'gym_class__name']
