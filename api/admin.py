from django.contrib import admin
from api import models

admin.site.register(models.Category)
admin.site.register(models.SubCategory)
admin.site.register(models.Product)
admin.site.register(models.Order)