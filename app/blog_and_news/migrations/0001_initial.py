# Generated by Django 4.1.7 on 2023-06-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('News', 'News'), ('Blog', 'Blog')], max_length=100)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='blog_images')),
                ('content', models.TextField(verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Добавить пост или новость',
                'verbose_name_plural': 'Добавить посты или новости',
            },
        ),
    ]
