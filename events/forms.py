from django import forms
from events.models import Event, Category


class FormMixin:
    default_class = 'text-gray-800 border border-gray-200 mt-5 shadow-lg rounded-md w-full'

    def apply_class(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_class
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class':self.default_class
                })
            elif isinstance(field.widget, forms.DateField):
                field.widget.attrs.update({
                    'class':self.default_class
                })
            elif isinstance(field.widget, forms.TimeField):
                field.widget.attrs.update({
                    'class':self.default_class
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class':self.default_class
                })
            else:
                field.widget.attrs.update({
                    'class':self.default_class
                })



class EventModelForm( FormMixin ,forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'locations', 'participants']
        widgets = {
            'date': forms.SelectDateWidget,
            'participants': forms.CheckboxSelectMultiple,
         }

    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        self.apply_class()

class CategoryModelForm(FormMixin ,forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter The category of event'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_class()

