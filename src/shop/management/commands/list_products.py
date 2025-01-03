from django.core.management.base import BaseCommand
from shop.models import Product

class Command(BaseCommand):
    help = 'Lists all products in the database'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        self.stdout.write('Products in database:')
        for product in products:
            self.stdout.write(f'- {product.name} (Current price: {product.price} DH)') 