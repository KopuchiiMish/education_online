# Generated by Django 4.2.7 on 2023-11-19 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название курса')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание курса')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/', verbose_name='Изображение курса')),
                ('price', models.PositiveIntegerField(default=1000, verbose_name='Стоимость курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название урока')),
                ('description', models.TextField(verbose_name='Описание урока')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/lessons/', verbose_name='Изображение урока')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата платежа')),
                ('payment_method', models.CharField(choices=[('1', 'Наличные'), ('2', 'Безнал')], max_length=1, verbose_name='Метод платежа')),
                ('is_successful', models.BooleanField(default=False, verbose_name='Статус платежа')),
                ('session', models.CharField(blank=True, max_length=150, null=True, verbose_name='Сессия для оплаты')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
                'ordering': ('-payment_date',),
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_subscriptions', to='education.course')),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
            },
        ),
    ]
