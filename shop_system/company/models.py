from django.db import models
from django.conf import settings
from django.dispatch import receiver 
from django.http import  HttpRequest
from django.middleware.csrf import get_token
from allauth.account.views import PasswordResetView

from profiles.models import User


class Company(models.Model):
	title = models.CharField(max_length=50);
	description = models.CharField(max_length=250);
	logo = models.ImageField(upload_to = 'media')
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	# @receiver(models.signals.post_save, sender=settings.AUTH_USER_MODEL)
	# def send_reset_password_email(sender, instance, created, **kwargs):
	# 	if created:			
	# 		request = HttpRequest()
	# 		request.method = 'POST'			
	# 		if settings.DEBUG:
	# 			request.META['HTTP_HOST'] = '127.0.0.1:8000'
	# 		else:
	# 			request.META['HTTP_HOST'] = 'www.example.com'			
	# 		request.POST = {
	# 			'email': instance.email,
	# 			'csrfmiddlewaretoken': get_token(HttpRequest())
	# 		}		
	# 		PasswordResetView.as_view()#(request) 		