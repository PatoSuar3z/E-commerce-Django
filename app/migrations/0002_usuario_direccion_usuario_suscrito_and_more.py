# Generated by Django 4.0.4 on 2022-06-26 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='suscrito',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Subscripcion',
        ),
        migrations.DeleteModel(
            name='TipoSubscripcion',
        ),
    ]