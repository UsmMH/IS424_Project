from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import GymClass, Booking
from .forms import CustomLoginForm, CustomRegisterForm, GymClassForm


def login_view(request):
    """Requirement #2 — Login page."""
    if request.user.is_authenticated:
        return redirect('class_list')

    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('class_list')
    else:
        form = CustomLoginForm()

    return render(request, 'gym_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    """Requirement #3 — Registration page."""
    if request.user.is_authenticated:
        return redirect('class_list')

    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('class_list')
    else:
        form = CustomRegisterForm()

    return render(request, 'gym_app/register.html', {'form': form})


@login_required(login_url='login')
def class_list_view(request):
    """Requirement #4 — All classes list page (home after login)."""
    category_filter = request.GET.get('category', '')
    difficulty_filter = request.GET.get('difficulty', '')

    classes = GymClass.objects.all()
    if category_filter:
        classes = classes.filter(category=category_filter)
    if difficulty_filter:
        classes = classes.filter(difficulty=difficulty_filter)
    classes = classes.order_by('schedule')

    user_booked_ids = set(
        Booking.objects.filter(user=request.user).values_list('gym_class_id', flat=True)
    )

    categories = GymClass.CATEGORY_CHOICES
    difficulties = GymClass.DIFFICULTY_CHOICES

    return render(request, 'gym_app/class_list.html', {
        'classes': classes,
        'user_booked_ids': user_booked_ids,
        'categories': categories,
        'difficulties': difficulties,
        'category_filter': category_filter,
        'difficulty_filter': difficulty_filter,
    })


@login_required(login_url='login')
def class_detail_view(request, pk):
    """Requirement #5 — Specific class detail + book/cancel action."""
    gym_class = get_object_or_404(GymClass, pk=pk)
    is_booked = Booking.objects.filter(user=request.user, gym_class=gym_class).exists()

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'book' and not is_booked:
            if not gym_class.is_full():
                Booking.objects.create(user=request.user, gym_class=gym_class)
        elif action == 'cancel' and is_booked:
            Booking.objects.filter(user=request.user, gym_class=gym_class).delete()
        return redirect('class_detail', pk=pk)

    booked_members = gym_class.booking_set.select_related('user').order_by('booked_at')

    return render(request, 'gym_app/class_detail.html', {
        'gym_class': gym_class,
        'is_booked': is_booked,
        'booked_members': booked_members,
    })


@login_required(login_url='login')
def class_add_view(request):
    """Requirement #6 — Add a new class. Staff only."""
    if not request.user.is_staff:
        return redirect('class_list')

    if request.method == 'POST':
        form = GymClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = GymClassForm()

    return render(request, 'gym_app/class_add.html', {'form': form})


@login_required(login_url='login')
def class_update_view(request, pk):
    """Requirement #7 — Update an existing class. Staff only."""
    if not request.user.is_staff:
        return redirect('class_detail', pk=pk)

    gym_class = get_object_or_404(GymClass, pk=pk)

    if request.method == 'POST':
        form = GymClassForm(request.POST, instance=gym_class)
        if form.is_valid():
            form.save()
            return redirect('class_detail', pk=pk)
    else:
        # Pre-format datetime for the datetime-local input
        form = GymClassForm(instance=gym_class)
        if gym_class.schedule:
            form.initial['schedule'] = gym_class.schedule.strftime('%Y-%m-%dT%H:%M')

    return render(request, 'gym_app/class_update.html', {
        'form': form,
        'gym_class': gym_class,
    })


@login_required(login_url='login')
def my_bookings_view(request):
    """Bonus — user's personal bookings."""
    bookings = Booking.objects.filter(user=request.user).select_related('gym_class').order_by('gym_class__schedule')
    return render(request, 'gym_app/my_bookings.html', {'bookings': bookings})
