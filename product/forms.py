from django import forms
from .models import Product,ProductImages


class AddProductsPost(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','condition','category','brand','price','image']
        widgets = {
            'name': forms.TextInput(attrs={'class':'phone'}),
            'description':forms.Textarea(attrs={'class':'mess','placeholder':'Write few lines about your product'}),
            'image':forms.ClearableFileInput(attrs={'id':'fileselect','multiple':'multiple'}),
            'price': forms.TextInput(attrs={'class': 'phone'}),

        }




class AddImageForm(forms.ModelForm):
    class Meta:
        model = ProductImages
        fields = ['image']