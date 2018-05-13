from django import forms

class GroupForm(forms.Form):
	slug = forms.CharField()