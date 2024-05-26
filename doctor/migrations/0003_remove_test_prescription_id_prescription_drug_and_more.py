# Generated by Django 5.0.2 on 2024-05-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_prescription_diagnosis_prescription_symptoms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='prescription_id',
        ),
        migrations.AddField(
            model_name='prescription',
            name='drug',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='test',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Drug',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]