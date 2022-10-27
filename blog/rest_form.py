from django import forms
from blog.models import Restaurants
class RestaurantsForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = "__all__"