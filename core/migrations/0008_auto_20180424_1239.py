# Generated by Django 2.0.4 on 2018-04-24 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(default='', null=''),
        ),
    ]
