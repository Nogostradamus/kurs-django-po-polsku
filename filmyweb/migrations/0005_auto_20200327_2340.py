# Generated by Django 3.0.4 on 2020-03-27 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0004_auto_20200327_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Komedia'), (0, 'Inne'), (3, 'Sci-fi'), (4, 'Drama'), (1, 'Horror')], default=0),
        ),
        migrations.CreateModel(
            name='Ocena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recenzja', models.TextField(blank=True, default='')),
                ('gwiazdki', models.PositiveSmallIntegerField(default=5)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmyweb.Film')),
            ],
        ),
    ]
