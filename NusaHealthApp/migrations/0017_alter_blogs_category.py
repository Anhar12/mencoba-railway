# Generated by Django 5.1.3 on 2024-11-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NusaHealthApp', '0016_remove_activities_tags_remove_blogs_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='category',
            field=models.CharField(choices=[('Technology', 'Technology'), ('Sports', 'Sports'), ('Health', 'Health'), ('science', 'Science'), ('Science', 'Services'), ('News', 'News'), ('Diseases', 'Diseases'), ('Events', 'Events'), ('Education', 'Education'), ('LifeStyle', 'LifeStyle'), ('Medicine', 'Medicine')], default='health', max_length=100),
        ),
    ]
