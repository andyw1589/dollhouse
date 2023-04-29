from django import forms
from characters.models import Character 

class CharacterForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, required=False)
    physical_description = forms.CharField(widget=forms.Textarea, required=False)
    clothing = forms.CharField(widget=forms.Textarea, required=False)
    medical_history = forms.CharField(widget=forms.Textarea, required=False)
    criminal_record = forms.CharField(widget=forms.Textarea, required=False)
    education = forms.CharField(widget=forms.Textarea, required=False)
    forming_events = forms.CharField(widget=forms.Textarea, required=False)
    romance = forms.CharField(widget=forms.Textarea, required=False)
    relationships = forms.CharField(widget=forms.Textarea, required=False)
    employment = forms.CharField(widget=forms.Textarea, required=False)
    pets = forms.CharField(widget=forms.Textarea, required=False)
    hopes_and_dreams = forms.CharField(widget=forms.Textarea, required=False)
    fears = forms.CharField(widget=forms.Textarea, required=False)
    hobbies = forms.CharField(widget=forms.Textarea, required=False)
    likes = forms.CharField(widget=forms.Textarea, required=False)
    dislikes = forms.CharField(widget=forms.Textarea, required=False)
    personality = forms.CharField(widget=forms.Textarea, required=False)
    skills = forms.CharField(widget=forms.Textarea, required=False)
    weaknesses = forms.CharField(widget=forms.Textarea, required=False)

    tags = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comma-separated tags'}), max_length=2000, required=False)  # comma-separated string of tags that will be processed
    class Meta:
        model = Character 
        exclude = ["owner", "created"]