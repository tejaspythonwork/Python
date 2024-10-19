from django.db import models

# Create your models here.
class ProductMst(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.product_name


class ProductSubCategory(models.Model):
    product = models.ForeignKey(ProductMst, on_delete=models.CASCADE)  # Foreign key to ProductMst
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    product_model = models.CharField(max_length=100)
    product_ram = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product.product_name} - {self.product_model}"
