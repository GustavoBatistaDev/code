# Generated by Django 4.1.5 on 2023-01-28 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_merge_0002_alter_user_is_active_0002_perfilusuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertaDeCrise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, choices=[('P', 'Pânico'), ('D', 'Depressão'), ('A', 'Ansiedade')], default='A', max_length=1, null=True)),
                ('inicio', models.DateTimeField()),
                ('fim', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Péssimo'), ('R', 'Ruim'), ('B', 'Bom'), ('E', 'Excelente')], default='P', max_length=1)),
                ('data', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ContatoAjuda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.perfilusuario')),
            ],
        ),
        migrations.CreateModel(
            name='Anotacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('P', 'Positivo'), ('N', 'Negativo')], default='P', max_length=1)),
                ('anotacao', models.TextField()),
                ('avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.avaliacao')),
            ],
        ),
    ]
