# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capcalera', models.TextField()),
                ('descripcio', models.TextField()),
                ('horari', models.TextField()),
                ('dataPublicacio', models.DateTimeField(auto_now=True)),
                ('categoria', models.CharField(choices=[('0', "Administraci\xf3 d'empreses"), ('1', 'Administraci\xf3 p\xfablica'), ('2', 'Atenci\xf3 al client'), ('3', 'I+D'), ('4', 'Magatzem'), ('5', 'Disseny i arts gr\xe0fiques'), ('6', 'Educaci\xf3'), ('7', 'Banca'), ('8', 'Inform\xe0tica'), ('9', 'Telecomunicacions'), ('10', 'Ingenier t\xe8cnic'), ('11', 'Immobiliaria'), ('12', 'Advocacia'), ('13', 'Marketing'), ('14', 'Altres'), ('15', 'Art'), ('16', 'RRHH'), ('17', 'Sanitat'), ('18', 'Sector farmaceutic'), ('19', 'Turisme'), ('20', 'Restauraci\xf3')], max_length=100)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa')),
            ],
        ),
    ]
