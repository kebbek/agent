from random import randint

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import User
SIZES = (
        ('L', 'L'),
        ('M', 'M'),
        ('S', 'S'),
        ('XXXL', 'XXXL'),
        ('XXL', 'XXXL'),
        ('XL', 'XL'),
        ('XS', 'XS')
)

STATUS = (
    ('Захиалга илгээгдсэн', 'Захиалга илгээгдсэн'),
    ('Төлбөр хүлээгдэж байна', 'Төлбөр хүлээгдэж байна'),
    ('Төлбөр хийгдсэн', 'Төлбөр хийгдсэн'),
    ('Захиалга хийгдсэн', 'Захиалга хийгдсэн'),
    ('Захиалга хүргэгдсэн', 'Захиалга хүргэгдсэн')
)


def unique_no():
    while True:
        no = randint(1000000, 10000000)
        if not Order.objects.filter(order_no=no).exists():
            return no


class Order(models.Model):
    user = models.ForeignKey(
        User, related_name='orders', on_delete=models.CASCADE)
    order_no = models.IntegerField(default=unique_no, editable=False)
    url = models.URLField(_('Холбоос'))
    product_name = models.CharField(_('Барааны нэр'), max_length=20)
    product_count = models.PositiveSmallIntegerField(_('Тоо ширхэг'))
    size = models.CharField(_('Хэмжээ'), max_length=8, choices=SIZES)
    color = models.CharField(_('Өнгө'), max_length=15)
    cost = models.IntegerField(null=True, blank=True)
    address = models.TextField(_('Хаяг'))
    status = models.CharField(
        max_length=50, choices=STATUS, default=STATUS[0][0])
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(_('Тайлбар'))

    def __str__(self):
        return self.product_name

    def get_icon(self):
        if self.status == 'Захиалга илгээгдсэн':
            return 'glyphicon-s'

    def get_cost(self):
        try:
            price = Price.objects.get(order_id=self.id)
            return price.total

        except ObjectDoesNotExist:
            return 'Төлбөр бодогдож байна.'


class Inbox(models.Model):
    order = models.ForeignKey(
        Order, related_name='inboxs', on_delete=models.CASCADE)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.message


class Price(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    cost = models.IntegerField(_('Үнэ'))
    trans_cost = models.IntegerField(_('Тээврийн зардал'))
    trans_to_cost = models.IntegerField(
        _('Хятад - Улаанбаатар хотод ирэх тээврийн зардал'))
    service_fee = models.IntegerField(_('Үйлчилгээний хөлс'))
    exchange = models.IntegerField(_('Ханш'))
    total = models.FloatField(_('Нийт'), editable=False)

    def save(self, *args, **kwargs):

        order = self.order
        if order.status == STATUS[0][0]:
            order.status = STATUS[1][0]
            order.save()

        self.total = (self.cost + self.trans_cost +
                      self.trans_to_cost) * self.exchange + self.service_fee

        super().save(*args, **kwargs)
