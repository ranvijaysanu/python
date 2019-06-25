# Generated by Django 2.2 on 2019-06-24 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0002_auto_20190624_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('post', models.TextField(max_length=100)),
                ('date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.AddUser')),
            ],
        ),
    ]