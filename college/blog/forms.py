from django import forms

from .models import Post
from .models import student



class studentForm(forms.ModelForm):

    class Meta:
        model = student
        fields = ('classs', 'name','std_id','mobile','email','department')
