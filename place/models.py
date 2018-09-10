from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	image = models.ImageField(upload_to='mainImage', null=True, blank=True)
	creater = models.DateField(auto_now=True, null=True, blank=True)
	def __str__(self):
		return self.name


class UserExperience(models.Model):
	User = models.ForeignKey(User, on_delete=models.CASCADE)
	Place = models.ForeignKey(Place, on_delete=models.CASCADE)
	Description = models.TextField()
	Best_time_to_visit = models.CharField(max_length=255)
	Dont_miss = models.TextField()
	Things_to_avoid = models.TextField()
	Means_of_transport = models.TextField()

	def __str__(self):
		return "{}-{}".format(self.Place.name, self.User.username)

class Comment(models.Model):
	user_exp = models.ForeignKey(UserExperience, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment_text = models.TextField()
	likes = models.IntegerField(default=0)
		
class CommentNext(models.Model):
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
	comment_text = models.TextField()
	likes = models.IntegerField(default=0)

class Image(models.Model):
	user_exp = models.ForeignKey(UserExperience, on_delete=models.CASCADE)
	img = models.ImageField(upload_to='placeImage')
				

		
				

		

