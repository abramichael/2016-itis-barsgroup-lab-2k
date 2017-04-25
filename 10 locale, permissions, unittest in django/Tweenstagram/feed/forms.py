from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from feed.models import Post, Tweet


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)


class MultiEmailField(forms.CharField):
    def to_python(self, value):
        return value.split(",")

    def validate(self, value):
        super(MultiEmailField, self).validate(value)
        for email in value:
            validators.validate_email(email)

def MeetingValidator(value):
    if "meeting" in value:
        raise ValidationError("NO MEETINGS PLEASE!")

class SettingsForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    #email = forms.EmailField()
    other_emails = MultiEmailField()
    receiveDirect = forms.BooleanField()
    about = forms.CharField(widget=forms.Textarea, validators=[MeetingValidator])


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["text", "image"]