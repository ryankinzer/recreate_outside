from django.db import models

# Create your models here.

class Menu(models.Model):

	meal_choices = [
		('breakfast', 'Breakfast'),
		('lunch', 'Lunch'),
		('dinner', 'Dinner'),
		('dessert', 'Dessert'),
	]

	category_choices = [
		('pasta', 'Pasta'),
		('chicken', 'Chicken'),
		('beef', 'Beef'),
		('pork', 'Pork'),
		('fish', 'Fish'),
		('rice', 'Rice'),
		('vegetarian', 'Vegetarian'),
		('vegan', 'Vegan'),
	]

	equipment_choices = [
		('grill', "Grill"),
		('stove', "Stove"),
		('dutchoven', "Dutch Oven"),
	]

	name = models.CharField(max_length=200)
	description = models.TextField()
	meal = models.CharField(max_length=25, choices = meal_choices)
	category = models.CharField(max_length=25, choices = category_choices)
	directions = models.TextField()
	special_equipment = models.CharField(max_length=25, choices = equipment_choices,
		null = True, blank = True)
	image1 = models.ImageField(null=True, blank=True, upload_to='images/')
	#submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	submitted_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name

class MenuItems(models.Model):

	units = [
		('oz', 'Ounces'),
		('whole', 'Whole'),
		('slices', 'Slices'),
		('lbs', 'Pounds'),
	]

	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	item = models.CharField(max_length=200)
	amount = models.DecimalField(max_digits = 4, decimal_places = 2)
	unit = models.CharField(max_length=25, choices = equipment_choices)
	refridgerated = models.BooleanField()

