# Generated by Django 2.1.2 on 2018-10-05 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20181005_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Захиалга илгээгдсэн', 'Захиалга илгээгдсэн'), ('Төлбөр хүлээгдэж байна', 'Төлбөр хүлээгдэж байна'), ('Төлбөр хийгдсэн', 'Төлбөр хийгдсэн'), ('Захиалга хийгдсэн', 'Захиалга хийгдсэн'), ('Захиалга хүргэгдсэн', 'Захиалга хүргэгдсэн')], default='Захиалга илгээгдсэн', max_length=50),
        ),
    ]
