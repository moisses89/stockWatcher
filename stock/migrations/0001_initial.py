# Generated by Django 4.0.3 on 2022-03-16 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import strategy_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('strategy', strategy_field.fields.StrategyField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductWatcher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=500)),
                ('minimum_stock', models.IntegerField()),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.market')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
