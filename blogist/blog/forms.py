from django import forms
from .models import Category, Tag, Image, Article
from tinymce.widgets import TinyMCE

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image','caption')

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20},))
    status  = forms.ChoiceField(choices=Article.StatusChoice.choices, widget=forms.RadioSelect)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select Category')
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
    duration = forms.DurationField(widget=forms.TimeInput(attrs={'type': 'time'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = Article
        fields = ('title','content','category','tags','status','duration')
        