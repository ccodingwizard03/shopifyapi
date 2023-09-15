from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from src.shopifyproduct.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        "name",
        # "cocation", 
        "artist_inspired_by",
        "artist",
        "tags",
        "description",
        "orientation",
        "subject",
        "inspired_by",     
        "fa_wa",
        "style",
        "genre",
        "artwork_id",
        "decor",
        "medium"
        ]
