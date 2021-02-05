from django import forms#importing forms model

"""This is the form for adding spending"""
class ExpanseForm(forms.Form):
    title = forms.CharField()
    amount = forms.IntegerField()
