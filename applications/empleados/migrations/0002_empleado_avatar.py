# Generated by Django 3.2 on 2023-03-02 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='empleado', verbose_name='Avatar'),
        ),
    ]