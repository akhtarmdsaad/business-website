from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control col-sm-6'
    class Meta:
        model = Order
        fields = ["materials","payment_mode"]
        
