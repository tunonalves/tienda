# Generated by Django 4.0.1 on 2022-06-08 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, default='./ProyectoWebApp/static/ProyectoWebApp/img/2.jpg', null=True, upload_to='blog'),
        ),
    ]