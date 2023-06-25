# Generated by Django 4.2.2 on 2023-06-17 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline_Companies',
            fields=[
                ('iata_code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('country_code', models.CharField(max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=15, unique=True)),
                ('credit_card_no', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('departure_time', models.DateTimeField()),
                ('landing_time', models.DateTimeField()),
                ('remaining_tickets', models.IntegerField()),
                ('airline_company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bingo.airline_companies')),
                ('destination_country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_flights', to='Bingo.countries')),
                ('origin_country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_flights', to='Bingo.countries')),
            ],
        ),
        migrations.CreateModel(
            name='User_Roles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('image', models.ImageField(default='static/defaultuser.png', null=True, upload_to='users/')),
                ('user_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bingo.user_roles')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bingo.customers')),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bingo.flights')),
            ],
        ),
        migrations.AddField(
            model_name='customers',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bingo.users', unique=True),
        ),
        migrations.AddField(
            model_name='airline_companies',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bingo.countries'),
        ),
        migrations.AddField(
            model_name='airline_companies',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bingo.users', unique=True),
        ),
        migrations.CreateModel(
            name='Administrators',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bingo.users', unique=True)),
            ],
        ),
    ]
