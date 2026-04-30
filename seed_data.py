"""
Reset & reseed — run with:  Get-Content seed_data.py | python manage.py shell
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_core.settings')

from django.contrib.auth.models import User
from gym_app.models import GymClass, Booking
from django.utils import timezone
from datetime import timedelta

# ── Wipe existing data ─────────────────────────────────────────
Booking.objects.all().delete()
GymClass.objects.all().delete()
User.objects.all().delete()
print('  Cleared existing data.')

# ── Create demo users (all male) ───────────────────────────────
def make_user(username, first, last, email, password, is_admin=False):
    u = User.objects.create_user(username, email, password,
                                 first_name=first, last_name=last)
    if is_admin:
        u.is_staff = True
        u.is_superuser = True
        u.save()
    print(f'  Created user: {username}')
    return u

admin   = make_user('admin',  'Abdullah', 'Al-Rashid', 'admin@FitLed.com',  'admin123', is_admin=True)
member1 = make_user('khalid', 'Khalid',   'Al-Omar',   'khalid@example.com', 'pass1234')
member2 = make_user('faisal', 'Faisal',   'Al-Harbi',  'faisal@example.com', 'pass1234')

# ── Create gym classes (all male instructors) ──────────────────
now = timezone.now()

classes_data = [
    dict(name='Morning Power Yoga',
         description='Start your day with an energising yoga flow designed to build strength, flexibility and mental clarity. Suitable for all levels.',
         instructor='Tariq Al-Mansour',
         category='yoga', schedule=now + timedelta(days=1, hours=7),
         duration=60, capacity=15, location='Studio A', difficulty='beginner'),

    dict(name='HIIT Inferno',
         description='High-intensity interval training that torches calories and builds cardiovascular endurance. Bring a towel — you\'ll need it.',
         instructor='Mohammed Al-Rashid',
         category='hiit', schedule=now + timedelta(days=1, hours=18),
         duration=45, capacity=20, location='Main Gym Floor', difficulty='advanced'),

    dict(name='Strength & Conditioning',
         description='Compound movements and progressive overload to build real-world functional strength. Barbells, dumbbells and kettlebells.',
         instructor='Ahmed Al-Saud',
         category='strength', schedule=now + timedelta(days=2, hours=10),
         duration=75, capacity=12, location='Weight Room', difficulty='intermediate'),

    dict(name='Spin Cycle Blast',
         description='Indoor cycling session with music-driven intervals. Great for fat burning and leg power. All bikes are adjustable.',
         instructor='Yousef Al-Ghamdi',
         category='cycling', schedule=now + timedelta(days=2, hours=19),
         duration=50, capacity=18, location='Cycling Studio', difficulty='intermediate'),

    dict(name='Core & Pilates',
         description='Precision-based pilates movements targeting the core, posture, and deep stabiliser muscles. Low impact, high results.',
         instructor='Salman Al-Dosari',
         category='pilates', schedule=now + timedelta(days=3, hours=9),
         duration=55, capacity=10, location='Studio B', difficulty='beginner'),

    dict(name='Boxing Fundamentals',
         description='Learn the sweet science. This session covers stance, footwork, jabs, crosses, hooks and basic combinations on heavy bags.',
         instructor='Omar Al-Harbi',
         category='boxing', schedule=now + timedelta(days=3, hours=17),
         duration=60, capacity=14, location='Boxing Ring', difficulty='intermediate'),

    dict(name='Aqua Cardio',
         description='Low-impact, high-fun water aerobics class perfect for joint recovery and cardio conditioning. All swimming levels welcome.',
         instructor='Nasser Al-Qahtani',
         category='swimming', schedule=now + timedelta(days=4, hours=8),
         duration=45, capacity=16, location='Pool Deck', difficulty='beginner'),

    dict(name='Advanced HIIT & Strength',
         description='The ultimate full-body session combining weighted circuits with explosive plyometrics. For experienced athletes only.',
         instructor='Mohammed Al-Rashid',
         category='hiit', schedule=now + timedelta(days=5, hours=6, minutes=30),
         duration=90, capacity=10, location='Main Gym Floor', difficulty='advanced'),
]

for data in classes_data:
    GymClass.objects.create(**data)
    print(f'  Created class: {data["name"]}')

print('\n✅ Reseed complete!')
print('   Superuser → username: admin  /  password: admin123')
print('   Member    → username: khalid /  password: pass1234')
print('   Member    → username: faisal /  password: pass1234')
