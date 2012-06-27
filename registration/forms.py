from django import forms
import datetime
from models import *

class StudentForm(forms.Form):
    barcode = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=35)
