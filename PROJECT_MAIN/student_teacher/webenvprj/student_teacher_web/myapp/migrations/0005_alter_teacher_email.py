# Generated by Django 5.1.1 on 2024-10-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_coursesenrolled_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default='abc@gmail.com', max_length=35, unique=True),
        ),
    ]
