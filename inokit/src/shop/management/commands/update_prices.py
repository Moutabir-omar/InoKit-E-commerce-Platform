from django.core.management.base import BaseCommand
from shop.models import Product

class Command(BaseCommand):
    help = 'Updates product prices'

    def handle(self, *args, **kwargs):
        price_updates = {
            'Raspberry Pi': 700,
            'LED Kit': 20,
            'Arduino UNO': 100,
            'Breadboard': 15,
        }

        for product_name, new_price in price_updates.items():
            try:
                product = Product.objects.get(name__exact=product_name)
                product.price = new_price
                product.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully updated price for {product_name} to {new_price} DH'))
            except Product.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Product {product_name} not found')) 