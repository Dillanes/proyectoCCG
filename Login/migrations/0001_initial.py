# Generated by Django 3.0.8 on 2022-05-30 22:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cp',
            fields=[
                ('cp', models.IntegerField(primary_key=True, serialize=False)),
                ('fk_mpiodel', models.IntegerField(blank=True, db_column='fk_MpioDel', null=True)),
            ],
            options={
                'db_table': 'CP',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idestado', models.AutoField(db_column='idEstado', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=25)),
                ('iso', models.CharField(blank=True, db_column='ISO', max_length=4, null=True)),
                ('fk_pais', models.IntegerField(db_column='fk_Pais')),
            ],
            options={
                'db_table': 'Estado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invitado',
            fields=[
                ('idinvitado', models.AutoField(db_column='idInvitado', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
                ('paterno', models.CharField(blank=True, db_column='Paterno', max_length=45, null=True)),
                ('materno', models.CharField(blank=True, db_column='Materno', max_length=45, null=True)),
                ('cargo', models.CharField(blank=True, db_column='Cargo', max_length=60, null=True)),
                ('cel', models.CharField(blank=True, db_column='Cel', max_length=12, null=True)),
                ('orgprocedencia', models.CharField(blank=True, db_column='orgProcedencia', max_length=60, null=True)),
                ('descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=200, null=True)),
            ],
            options={
                'db_table': 'Invitado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mundeleg',
            fields=[
                ('idmundeleg', models.AutoField(db_column='idMunDeleg', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=45)),
                ('fk_estado', models.IntegerField(blank=True, db_column='fk_Estado', null=True)),
            ],
            options={
                'db_table': 'MunDeleg',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Omniclass23',
            fields=[
                ('idomc23', models.AutoField(db_column='idOmc23', primary_key=True, serialize=False)),
                ('nummat', models.IntegerField(blank=True, db_column='numMat', null=True)),
                ('codigo', models.CharField(db_column='Codigo', max_length=18)),
                ('descrieng', models.CharField(blank=True, db_column='descriEng', max_length=120, null=True)),
                ('descrispa', models.CharField(blank=True, db_column='descriSpa', max_length=120, null=True)),
                ('nivel', models.IntegerField(db_column='Nivel')),
                ('regfinal', models.BooleanField(blank=True, db_column='regFinal', null=True)),
            ],
            options={
                'db_table': 'Omniclass23',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('idpais', models.AutoField(db_column='idPais', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=45)),
                ('iso', models.CharField(db_column='ISO', max_length=2)),
            ],
            options={
                'db_table': 'Pais',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('idpersonal', models.AutoField(db_column='idPersonal', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
                ('paterno', models.CharField(blank=True, db_column='Paterno', max_length=45, null=True)),
                ('materno', models.CharField(blank=True, db_column='Materno', max_length=45, null=True)),
                ('genero', models.CharField(blank=True, db_column='Genero', max_length=1, null=True)),
                ('fechanac', models.DateField(blank=True, db_column='fechaNac', null=True)),
                ('lugarnac', models.CharField(blank=True, db_column='lugarNac', max_length=45, null=True)),
                ('rfc', models.CharField(blank=True, db_column='RFC', max_length=13, null=True)),
                ('curp', models.CharField(blank=True, db_column='CURP', max_length=18, null=True)),
                ('cel', models.CharField(blank=True, db_column='Cel', max_length=10, null=True)),
                ('calle', models.CharField(blank=True, db_column='Calle', max_length=45, null=True)),
                ('noint', models.IntegerField(blank=True, db_column='noInt', null=True)),
                ('noext', models.IntegerField(blank=True, db_column='noExt', null=True)),
                ('fk_usuario', models.IntegerField(blank=True, db_column='fk_Usuario', null=True)),
                ('fk_cp', models.IntegerField(blank=True, db_column='fk_CP', null=True)),
            ],
            options={
                'db_table': 'Personal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.AutoField(db_column='idUsuario', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_column='Correo', max_length=50, null=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=20, null=True)),
                ('rol', models.CharField(blank=True, choices=[('Empleado', 'Empleado'), ('Visitante', 'Visitante')], db_column='Rol', max_length=15, null=True)),
                ('fechacreacion', models.DateTimeField(auto_now=True, db_column='fechaCreacion', null=True)),
                ('fechaact', models.DateTimeField(db_column='fechaAct', default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Usuario',
                'managed': False,
            },
        ),
    ]
