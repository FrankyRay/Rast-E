from django.forms import ModelForm
from main.models import Shop

class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = [ "name", "price", "description", "rating" ]
