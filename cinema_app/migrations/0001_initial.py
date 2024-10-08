# Generated by Django 5.1.1 on 2024-10-07 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='missing_movie_image.jpg', upload_to='media/')),
            ],
        ),
    ]
