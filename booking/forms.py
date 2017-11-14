from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Session
from offering.models import Timeslot
from django.utils import timezone
import decimal, pytz, datetime


class TutorForm(forms.Form):
    SCHOOL_CHOICES = (('0', 'All Universities'), ('1', 'University of Hong Kong'),('2', 'Hong Kong University of Science and Technology'),
        ('3', 'Chinese University of Hong Kong'), ('4', 'City University of Hong Kong'), 
        ('5', 'The Hong Kong Polytechnic University'), ('6', 'Hong Kong Baptist University'))
    univserity = forms.ChoiceField(label=("univserity"), required=False, choices=SCHOOL_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    course = forms.CharField(label=("course"), required=False, max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label=("name"), required=False, max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label=("subject"), required=False, max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    IDENTITY_CHOICES = (('A', 'All'),('T', 'Private Tutor'),('C', 'Contracted Tutor'))
    identity = forms.ChoiceField(label=("identity"), required=False, choices=IDENTITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    price_min = forms.DecimalField(label=("price_min"), required=False, max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price_max = forms.DecimalField(label=("price_max"), required=False, max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    available_only = forms.BooleanField(label=("available_only"), required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input'}))

class BookingForm(forms.Form):
    slots = forms.ModelChoiceField(queryset=Timeslot.objects.all(), widget=forms.RadioSelect, empty_label=None)
    def __init__(self, TutorID, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        utcCurrentTime = timezone.now()
        timezonelocal = pytz.timezone('Asia/Hong_Kong')
        currentTime = timezone.localtime(utcCurrentTime, timezonelocal)

        endTime = currentTime + datetime.timedelta(days=7)
        if currentTime.minute < 30:
            mintime = datetime.datetime(currentTime.year, currentTime.month, currentTime.day+1, currentTime.hour, 30, 0, 0)
            maxtime = datetime.datetime(endTime.year, endTime.month, endTime.day, endTime.hour+1, 30, 0, 0)
        else:
            mintime = datetime.datetime(currentTime.year, currentTime.month, currentTime.day+1, currentTime.hour+1, 0, 0, 0)
            maxtime = datetime.datetime(endTime.year, endTime.month, endTime.day, endTime.hour+1, 0, 0, 0)
        self.fields['slots'].queryset = Timeslot.objects.filter(tutor__id=TutorID, status='Available', start__lte=maxtime, start__gte=mintime)
    def save(self, Student):
        timeslot = self.cleaned_data['slots']
        timeslot.status = 'Booked'
        timeslot.save()
        session = Session(student=Student, tutor=timeslot.tutor, start=timeslot.start, end=timeslot.end, status='Pending')
        session.save()
        return session.id
        