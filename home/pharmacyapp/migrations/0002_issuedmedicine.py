# Generated by Django 4.2.6 on 2023-10-13 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuedMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_number', models.CharField(max_length=100)),
                ('quantity_issued', models.PositiveIntegerField()),
                ('issued_date', models.DateField(auto_now_add=True)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacyapp.medicine')),
            ],
        ),
    ]
