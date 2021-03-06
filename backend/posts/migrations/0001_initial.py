# Generated by Django 3.1.7 on 2021-05-12 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('missions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='post_pics')),
                ('video_url', models.URLField(blank=True, null=True)),
                ('category', models.CharField(choices=[('Actu', 'Actu'), ('Med', 'Médiation'), ('Onboard', 'À bord')], max_length=20)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='missions.mission')),
                ('mission_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='users.missionuser')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='missions_pics')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.mission')),
            ],
        ),
    ]
