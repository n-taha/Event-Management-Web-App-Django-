import os
import django
import random
from faker import Faker
from datetime import timedelta, datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

from events.models import Participant, Category, Event

fake = Faker()

def create_categories():
    categories = [
        {'name': 'Music', 'description': 'Music related events'},
        {'name': 'Sports', 'description': 'Sports related events'},
        {'name': 'Tech', 'description': 'Technology related events'},
        {'name': 'Art', 'description': 'Art and culture events'},
        {'name': 'Education', 'description': 'Educational seminars and workshops'},
    ]
    for cat in categories:
        Category.objects.get_or_create(name=cat['name'], defaults={'description': cat['description']})

def create_participants(n=20):
    for _ in range(n):
        name = fake.name()
        email = fake.unique.email()
        Participant.objects.get_or_create(name=name, email=email)

def create_events(n=10):
    location_choices = [loc[0] for loc in Event.location]
    categories = list(Category.objects.all())
    participants = list(Participant.objects.all())

    for _ in range(n):
        name = fake.sentence(nb_words=3)
        description = fake.paragraph(nb_sentences=3)
        date = fake.date_between(start_date='-1y', end_date='+1y')
        time = fake.time()
        location = random.choice(location_choices)
        category = random.choice(categories)

        event = Event.objects.create(
            name=name,
            description=description,
            date=date,
            time=time,
            locations=location,
            category=category
        )

        event.participants.set(random.sample(participants, k=random.randint(3, 7)))
        event.save()

if __name__ == '__main__':
    print("Creating categories...")
    create_categories()
    print("Creating participants...")
    create_participants()
    print("Creating events...")
    create_events()
    print("Done.")
