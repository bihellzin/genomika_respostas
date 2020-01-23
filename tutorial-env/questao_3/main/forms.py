from django import forms


class GetDiseases(forms.Form):
    diseases_to_search = forms.CharField(required=True, widget=forms.Textarea(attrs={"placeholder": "Digite a doença"}))


class Login(forms.Form):
    username = forms.CharField(required=True, max_length=20)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
