# Generated by Django 2.0.4 on 2018-04-24 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
    ]
