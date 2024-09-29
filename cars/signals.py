import os
import google.generativeai as genai
from dotenv import load_dotenv
from django.db.models.signals import post_save, post_delete, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory

load_dotenv()

GEMINI_AI_API_KEY = os.getenv('GEMINI_AI_API_KEY')

genai.configure(api_key=GEMINI_AI_API_KEY)

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("Me de uma descrição sobre o carro {} da marca {} do ano {}, de no máximo 250 caractéres. Fale especificamente sobre esse carro".format(instance.model, instance.brand, instance.model_year))
        instance.bio = response.text