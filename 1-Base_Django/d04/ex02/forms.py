from django import forms

class TextInputForm(forms.Form):
    text_input = forms.CharField(
        label='',
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Entrez votre texte ici'})
    )