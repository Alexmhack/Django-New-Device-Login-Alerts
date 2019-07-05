from django import forms

from captcha.fields import CaptchaField

from .models import Blog

class BlogForm(forms.ModelForm):
	captcha = CaptchaField()
	
	class Meta:
		model = Blog
		fields = '__all__'
