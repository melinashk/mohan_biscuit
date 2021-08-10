from django.forms import DateField, widgets
from captcha.fields import CaptchaField
from .models import *

from django import forms

RATE_CHOICES = (
    ('', 'Rate Your Experience'), ('1', '1 - Needs Improvement'), ('2', '2 - Fair'), ('3', '3 - Good'),
    ('4', '4 - Very Good'),
    ('5', '5 - Excellent'))


class Rateform(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'box', 'required': 'required', 'placeholder': 'Name'}), required=True,
        label='')
    rating = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(attrs={'class': 'box'}), required=True,
                               label='')
    review = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'materialize-textarea', 'placeholder': 'Write your review'}),
        required=True, label='')

    class Meta:
        model = Rating
        fields = '__all__'


class CareerForm(forms.ModelForm):
    type = forms.ChoiceField(choices=CHOICE, widget=forms.Select(attrs={'class': 'box'}), required=True, label='')
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'box', 'required': 'required', 'placeholder': 'Name'}), required=True,
        label='')
    number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'box', 'required': 'required', 'placeholder': 'Number'}), required=True,
        label='')
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'box', 'required': 'required', 'placeholder': 'Address'}), required=True,
        label='')
    date = DateField(label='D.O.B', widget=widgets.DateInput(attrs={'type': 'date'}))
    # cv = forms.ImageField(label='',widget=widgets.Im)
    recaptcha = CaptchaField()

    class Meta:
        model = Career
        fields = '__all__'
