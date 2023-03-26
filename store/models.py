from django.db import models
from django.utils import timezone


class Store(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logo_images/', null=True)

    address = models.TextField(null=False, blank=False)
    city = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=20)

    tables_count = models.PositiveSmallIntegerField()
    subscription_factor = models.DecimalField(max_digits=5, decimal_places=2)

    instagram_page_link = models.CharField(max_length=255)
    telegram_channel_link = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            return super().save(*args, **kwargs)
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Collection(models.Model):
    title = models.CharField(max_length=255)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='collections')
    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            return super().save(*args, **kwargs)
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.store}.{self.title}"


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products_images/', null=True)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    inventory = models.PositiveSmallIntegerField()
    is_available = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='products')

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            return super().save(*args, **kwargs)
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.store}.{self.title}"


class Comment(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            return super().save(*args, **kwargs)
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product} from {self.name} : {self.amount}"


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='orders')
