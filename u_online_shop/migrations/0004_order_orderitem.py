# Generated by Django 4.0.6 on 2022-07-10 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('u_online_shop', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sellers', models.ManyToManyField(related_name='orders', to='u_online_shop.seller')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_pay', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='u_online_shop.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='u_online_shop.product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='u_online_shop.seller')),
            ],
        ),
    ]
