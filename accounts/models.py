from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.sessions.models import Session
from django.conf import settings

class UserSession(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	session = models.OneToOneField(Session, on_delete=models.CASCADE,
		blank=True, null=True)
	ip_address = models.GenericIPAddressField(blank=True, null=True)

	def __str__(self):
		return self.user.username
