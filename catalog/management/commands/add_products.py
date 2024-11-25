from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='electrics', description='"Электрика для дома')

        products = [
            {'name': 'розетка', 'description': '220 вольт, 15 ампер', 'image': '', 'category': category,
             'purchase_price': '300'},
            {'name': 'лампочка', 'description': 'патрон Е27', 'image': '', 'category': category,
             'purchase_price': '150'},
            {'name': 'кабель', 'description': '10 метров 3х2.5', 'image': '', 'category': category,
             'purchase_price': '1500'}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {product.name}'))