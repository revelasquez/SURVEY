# Generated by Django 4.2.1 on 2023-05-12 14:34

import api_survey.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_survey', '0006_alter_employee_picture_alter_question_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
        migrations.AddField(
            model_name='answeroption',
            name='image',
            field=models.ImageField(null=True, upload_to=api_survey.utils.rename_question_image),
        ),
        migrations.AlterField(
            model_name='employee',
            name='identity_card',
            field=models.IntegerField(unique=True, verbose_name='Carnet de Identidad'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='code',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Codigo'),
        ),
    ]
