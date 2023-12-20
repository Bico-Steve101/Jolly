# models.py

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    GENDER_CHOICES = [
        ('Boy', 'Boy'),
        ('Girl', 'Girl'),
    ]

    name = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='subcategory_images/', default='subcategory_images/default.jpg')

    def __str__(self):
        return self.name


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} likes {self.product.title}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} commented on {self.product.title}: {self.text}'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=255)
    description = models.TextField()
    main_image = models.ImageField(upload_to='product_images/main/')
    image1 = models.ImageField(upload_to='product_images/reference/', blank=True, null=True)
    image2 = models.ImageField(upload_to='product_images/reference/', blank=True, null=True)
    available_colors = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    neckline = models.CharField(max_length=255)
    closure = models.CharField(max_length=255)
    design = models.CharField(max_length=255)
    special_features = models.TextField()
    care_instructions = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    likes = models.ManyToManyField(User, through=Like, related_name='liked_products')
    comments = models.ManyToManyField(User, through=Comment, related_name='commented_products')

    # size = models.CharField(max_length=2, choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')])
    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.likes.count()

    @property
    def comment_count(self):
        return self.comments.count()

    def toggle_like(self, user):
        if user in self.likes.all():
            self.likes.remove(user)
        else:
            self.likes.add(user)


class ProductSize(models.Model):
    size = models.CharField(max_length=2, choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')])

    def __str__(self):
        return self.size


class ProductSizeQuantity(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


class ProductColor(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.color


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class FirstCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
