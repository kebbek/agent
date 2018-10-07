from django.contrib import admin
from accounts.models import User
from post.models import Post
from .models import Order, Price, Inbox

admin.site.register(Post)


class InboxInlineAdmin(admin.StackedInline):
    model = Inbox


class PriceInlineAdmin(admin.TabularInline):
    model = Price


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin, InboxInlineAdmin]

    list_display = ['order_no', 'product_name',
                    'status', 'created_date', 'user']
