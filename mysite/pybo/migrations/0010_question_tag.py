# Generated by Django 4.0.3 on 2022-08-02 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0009_answer_voter_question_voter_alter_answer_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
