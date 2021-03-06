from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create a model named Review which will correspondingly create a table in database with the following fields.

class Review(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	book_name=models.CharField(max_length=200)
	author_name=models.CharField(max_length=200)
	comments=models.TextField(null=True,blank=True)
	rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
	post_date=models.DateTimeField(auto_now_add=True)
# Create the object into string to interact with the database
	def __str__(self):
		return self.book_name

	class Meta:
		ordering: ['rating']
