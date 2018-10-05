from django.contrib import admin
from accounts.models import User
from post.models import Post
from .models import Order, Price

admin.site.register(Post)


class PriceInlineAdmin(admin.TabularInline):
    model = Price


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]
