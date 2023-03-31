# Generated by Django 3.0.5 on 2020-05-08 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0030_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='newfriends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='friends.friends')),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
