from django import forms
from .models import *

class FolderForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Folder
        fields = ["parent", "name", "description", "private"]