from django.contrib.auth import user_logged_in
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .utils import get_client_ip

# if users logins for the first time then a new UserSession object will be created
@receiver(user_logged_in)
def send_new_device_alert(sender, user, request, **kwargs):
	# remove other sessions
	Session.objects.filter(usersession__user=user).delete()

	# save current session
	user.session.save()

	try:
		message = render_to_string('candidates/emails/welcome_email.html', {
			'user': user
		})
		email = EmailMessage(
			subject="[Security Alert] DjangoLogin from a new Device",
			body=message,
			from_email="Example <noreply@example.com>",  # example email for file based emails in django
			to=[user.email],
			reply_to=["support@example.com"]  # <- your support email
		)
		email.content_subtype = "html"
		email.send()
	except Exception as e:
		# log the error to sentry or any other service.
		print(str(e))

	user_session = UserSession.objects.get_or_create(user=user)
	user_session.session = user.session
	user_session.ip_address = get_client_ip(request)
	user_session.save()
