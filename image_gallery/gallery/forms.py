from django import forms


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50,help_text='Enter a category name')

class ImageForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField(max_length=100)
    category = forms.CharField(max_length=50)

