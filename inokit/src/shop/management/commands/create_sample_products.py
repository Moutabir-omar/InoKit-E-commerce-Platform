from django.core.management.base import BaseCommand
from shop.models import Product
from django.core.files import File
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Creates sample products'

    def handle(self, *args, **kwargs):
        # Delete existing products
        Product.objects.all().delete()
        
        products = [
            {
                'name': 'Arduino UNO',
                'description': 'Arduino UNO R3 board - perfect for beginners and advanced projects.',
                'price': 24.99,
                'stock': 50,
                'image': 'arduino_uno.jpg'
            },
            {
                'name': 'Raspberry Pi',
                'description': 'Raspberry Pi 4 Model B - A powerful single-board computer.',
                'price': 45.99,
                'stock': 30,
                'image': 'raspberry_pi.jpg'
            },
            {
                'name': 'Breadboard',
                'description': 'Solderless breadboard for prototyping electronic circuits.',
                'price': 5.99,
                'stock': 100,
                'image': 'breadboard.jpg'
            },
            {
                'name': 'Sensor Kit',
                'description': 'Collection of various sensors for Arduino and Raspberry Pi projects.',
                'price': 29.99,
                'stock': 40,
                'image': 'sensors.jpg'
            },
            {
                'name': 'LED Kit',
                'description': 'Assorted LED lights with different colors and resistors.',
                'price': 12.99,
                'stock': 75,
                'image': 'led_kit.jpg'
            }
        ]

        for product_data in products:
            # Try to find the image in media/product_images first
            image_path = os.path.join(settings.BASE_DIR, 'media', 'product_images', product_data['image'])
            
            # If not found in media, try static/images
            if not os.path.exists(image_path):
                image_path = os.path.join(settings.BASE_DIR, 'static', 'images', product_data['image'])
            
            if os.path.exists(image_path):
                product = Product.objects.create(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    stock=product_data['stock']
                )
                with open(image_path, 'rb') as img_file:
                    product.image.save(product_data['image'], File(img_file), save=True)
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Image not found for {product_data["name"]}: {image_path}')) 