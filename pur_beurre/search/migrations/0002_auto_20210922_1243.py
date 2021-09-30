# Generated by Django 3.2.6 on 2021-09-22 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='aliment',
            name='url',
            field=models.URLField(unique=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='favorites',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.aliment'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='aliment',
            name='pnns_groups_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.category'),
        ),
        migrations.AlterUniqueTogether(
            name='favorites',
            unique_together={('user_id', 'product_id')},
        ),
    ]