from django import forms
from .models import Feedback

class MyForm(forms.ModelForm):
  class Meta:
    model = Feedback
    fields = ["client","mobie_no","email","comment","image"]
    labels = { "client":"client","mobie_no": "Mobile Number","email":"Email","comment":"Comment","image":"Image"}