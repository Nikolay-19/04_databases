import os
import django
from django.db.models import Q, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Create and run your queries within functions
from main_app.models import Director, Actor, Movie


def get_directors(search_name, search_nationality):
    if search_name and search_nationality:
        directors = Director.objects.filter(Q(full_name__contains=search_name.lower()) | Q(nationality__contains=search_nationality.lower()))
    elif not search_nationality:
        directors = Director.objects.filter(full_name__contains=search_name.lower())
    elif not search_name:
        directors = Director.objects.filter(nationality__contains=search_nationality.lower())

    result = [f"Director: {el.full_name}, nationality: {el.nationality}, experience: {el.years_of_experience}" for el in directors]
    if result:
        return "\n".join(str(el) for el in result)
    else:
        return ""


def get_top_director():
    pass


def get_top_actor():
    pass
