# Generated by Django 4.0.6 on 2022-07-23 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_note_book_note_user_tracking_book_tracking_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_choices', models.CharField(choices=[('RD', 'Read'), ('RDING', 'Reading'), ('WTR', 'Want to read')], default='WTR', max_length=10)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_statuses', to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_statuses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Tracking',
        ),
    ]
