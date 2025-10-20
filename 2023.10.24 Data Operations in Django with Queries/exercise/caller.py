import os
import django
from django.db.models import F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

# Create queries within functions
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


def create_pet(name, species):
    Pet.objects.create(name=name, species=species)
    return f"{name} is a very cute {species}!"

# print(create_pet("Buddy", "Dog"))
# print(create_pet("Whiskers", "Cat"))
# print(create_pet("Rocky", "Hamster"))


def create_artifact(name, origin, age, description, is_magical):
    Artifact.objects.create(name=name, origin=origin, age=age, description=description, is_magical=is_magical)
    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
    Artifact.objects.all().delete()

# print(create_artifact("Ancient Sword", "Lost Kingdom", 500, "A legendary sword with a rich history", True))
# print(create_artifact("Crystal Amulet", "Mystic Forest", 300, "A magical amulet believed to bring good fortune", True))
# print(create_artifact("Stone Tablet", "Ruined Templ", 1000, "An ancient tablet covered in mystreious inscriptions", False))
# delete_all_artifacts()


def show_all_locations():
    locations = Location.objects.all().order_by("-id")
    result = []
    for location in locations:
        result.append(f"{location.name} has a population of {location.population}!")
    return "\n".join(str(el) for el in result)


def new_capital():
    first = Location.objects.first()
    first.is_capital = True
    first.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values("name")


def delete_first_location():
    Location.objects.first().delete()

# Location.objects.create(name="Sofia", region="Sofia Region", population=1329000,description="The capital of Bulgaria and the largest city in the country", is_capital=False)
# Location.objects.create(name="Plovdiv", region="Plovdiv Region", population=346942, description="The second-largest city in Bulgaria with a rich historical heritage", is_capital=False)
# Location.objects.create(name="Varna", region="Varna Region", population=330486, description="A city known for its sea breeze and beautiful beaches on the Black Sea", is_capital=False)
# print(show_all_locations())
# print(new_capital())
# print(get_capitals())


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        car.price_with_discount = float(car.price) - (float(car.price) * (sum(map(int, str(car.year))) / 100))
        car.save()


def get_recent_cars():
    return Car.objects.all().filter(year__gte=2020).values("model", "price_with_discount")


def delete_last_car():
    Car.objects.last().delete()

# Car.objects.create(model="Mercedes C63 AMG", year=2019, color="white", price=120000)
# Car.objects.create(model="Audi Q7 S line", year=2023, color="black", price=183900)
# Car.objects.create(model="Chevrolet Corvette", year=2021, color="dark grey", price=199999)
# apply_discount()
# print(get_recent_cars())


def show_unfinished_tasks():
    tasks = [el for el in Task.objects.all() if not el.is_finished]
    result = []
    for task in tasks:
        result.append(f"Task - {task.title} needs to be done until {task.due_date}!")

    return "\n".join(str(el) for el in result)


def complete_odd_tasks():
    tasks = Task.objects.all()
    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text, task_title):
    tasks = Task.objects.filter(title=task_title)
    decoded_text = "".join(chr(ord(el) - 3) for el in text)

    for task in tasks:
        task.description = decoded_text
        task.save()

# Task.objects.create(title="Sample task", description="This is a sample task description", due_date="2023-10-31", is_finished=False)
# encode_and_replace("Zdvk#wkh#glvkhv$", "Sample Task")
# print(Task.objects.get(title='Sample Task').description)


def get_deluxe_rooms():
    rooms = HotelRoom.objects.all().filter(room_type="Deluxe")
    res = []

    for room in rooms:
        if room.id % 2 == 0:
            res.append(f"Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!")

    return "\n".join(str(el) for el in res)


def increase_room_capacity():
    rooms = HotelRoom.objects.all().order_by("id")
    previous_capacity = None
    for room in rooms:
        if not room.is_reserved:
            continue
        if previous_capacity:
            room.capacity += previous_capacity
        else:
            room.capacity += room.id
        previous_capacity = room.capacity
        room.save()


def reserve_first_room():
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()


def delete_last_room():
    room = HotelRoom.objects.last()
    if room.is_reserved:
        room.delete()

# HotelRoom.objects.create(room_number=101, room_type="Standard", capacity=2, amenities="Tv", price_per_night=100)
# HotelRoom.objects.create(room_number=201, room_type="Deluxe", capacity=3, amenities="Wi-Fi", price_per_night=200)
# HotelRoom.objects.create(room_number=501, room_type="Deluxe", capacity=6, amenities="Jacuzzi", price_per_night=400)
# print(get_deluxe_rooms())
# reserve_first_room()
# print(HotelRoom.objects.get(room_number=101).is_reserved)


def update_characters():
    Character.objects.filter(class_name='Mage').update(level=F('level')+3, intelligence=F('intelligence')-7)
    Character.objects.filter(class_name='Warrior').update(hit_points=F('hit_points')/2, dexterity=F('dexterity')+4)
    Character.objects.filter(class_name__in=["Assassin", "Scout"]).update(inventory="The inventory is empty")


def fuse_characters(first_character, second_character):
    new_name = f"{first_character.name} {second_character.name}"
    new_class = "Fusion"
    new_level = int((first_character.level + second_character.level) // 2)
    new_strength = int((first_character.strength + second_character.strength) * 1.2)
    new_dexterity = int((first_character.dexterity + second_character.dexterity) * 1.4)
    new_intelligence = int((first_character.intelligence + second_character.intelligence) * 1.5)
    new_hit_points = int(first_character.hit_points + second_character.hit_points)

    if first_character.class_name in ["Mage", "Scout"]:
        new_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    elif first_character.class_name in ["Warrior", "Assassin"]:
        new_inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(name=new_name, class_name=new_class, level=new_level, strength=new_strength,
                             dexterity=new_dexterity, intelligence=new_intelligence, hit_points=new_hit_points,
                             inventory=new_inventory)
    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.update(dexterity=30)


def grand_intelligence():
    Character.objects.update(intelligence=40)


def grand_strength():
    Character.objects.update(strength=50)


def delete_characters():
    Character.objects.filter(inventory="The inventory is empty").delete()

# character1 = Character.objects.create(name="Gandalf", class_name="Mage", level=10, strength=15, dexterity=20,
#                                       intelligence=25, hit_points=100, inventory="Staff of Magic, Spellbook")
# character2 = Character.objects.create(name="Hector", class_name="Warrior", level=12, strength=30, dexterity=15,
#                                       intelligence=10, hit_points=150, inventory="Sword of Troy, Shield of Protection")
# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)
