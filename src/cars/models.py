from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL


def set_delete_user():
	User = get_user_model()
	return User.objects.get_or_create(username='deleted')[0]

def limit_car_choices():
	Q = models.Q
	# return {"is_staff": True}
	return Q(username__icontains="e") | Q(username__icontains="c")


class Car(models.Model):
	# user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	# user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
	user = models.ForeignKey(
		User, 
		on_delete=models.SET(set_delete_user),
		limit_choices_to = limit_car_choices,
		)

	updated_by = models.ForeignKey(User, related_name="updated_car_user", null=True, blank=True)
	# first_owner = models.OneToOneField(User)
	# user = models.ForeignKey(User)
	# driver = models.ManyToManyField(User)
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name


# car_1 = Car.objects.first()

# cfe = car_1.first_owner

# User = cfe.__class__




# car_1 = Car.objects.first()
# user_qs = car_1.drivers.all()  # returns queryset of users

# cfe = user_qs.first()
# cfe.car_set.all()


# Car.objects.filter(drivers=cfe)

# Car.objects.filter(drivers__in= user_qs )









# ForeignKey = ManyToOneField() #Many Users can have any car, car can only have 1 user

# car_obj = Car.objects.first()
# car_obj.user

# User = car_obj.user.__class__

# abc = User.objects.all().last() # filter querysets

# user_cars = abc.car_set.all() 

# user_cars_qs = Car.objects.filter(user=abc)


# class Comment(models.Model):
#     user    = models.ForeignKey(User) 
#     content = models.CharField(max_length=120)


# comments = abc.comment_set.all()
# comments_qs = Comment.objects.filter(user=abc)

