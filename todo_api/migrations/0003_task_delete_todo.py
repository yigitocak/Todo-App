# Generated by Django 5.0.4 on 2024-04-09 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0002_alter_todo_created_at_alter_todo_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('priority', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]