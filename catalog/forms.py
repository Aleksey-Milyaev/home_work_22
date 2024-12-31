from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name.lower() in self.forbidden_words:
            raise ValidationError(f'Запрещенные слова для названия продукта: {', '.join(self.forbidden_words)}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if set(description.lower().split()).intersection(self.forbidden_words):
            raise ValidationError(f'Эти слова не должны присутствовать в описании: {', '.join(self.forbidden_words)}')
        return description
