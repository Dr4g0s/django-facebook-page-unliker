# Generated by Django 3.2.18 on 2023-04-13 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_id', models.CharField(max_length=100)),
                ('page_name', models.CharField(max_length=100)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialaccount.socialaccount')),
            ],
        ),
    ]
