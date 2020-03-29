from django.core.management.base import BaseCommand
from Restapi import models
class Command(BaseCommand):

    def handle(self, *args, **options):
        models.ShoeColor.objects.create (color_name = "Red")
        models.ShoeColor.objects.create (color_name = "Orange")
        models.ShoeColor.objects.create (color_name = "Yellow")
        models.ShoeColor.objects.create (color_name = "Green")
        models.ShoeColor.objects.create (color_name = "Blue")
        models.ShoeColor.objects.create (color_name = "Indigo")
        models.ShoeColor.objects.create (color_name = "Violet")
        models.ShoeColor.objects.create (color_name = "White")
        models.ShoeColor.objects.create (color_name = "Black")
        
        models.ShoeType.objects.create (style = "sneaker")
        models.ShoeType.objects.create (style = "boot")
        models.ShoeType.objects.create (style = "sandal")
        models.ShoeType.objects.create (style = "dress")
        models.ShoeType.objects.create (style = "other")

