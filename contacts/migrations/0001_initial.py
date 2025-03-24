# Generated by Django 5.0.13 on 2025-03-24 20:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('title', models.SmallIntegerField(db_column='CNTTTL_0', default=1)),
                ('type', models.SmallIntegerField(db_column='CNTTYP_0', default=1)),
                ('date_of_birth', models.DateTimeField(blank=True, db_column='CNTBIR_0')),
                ('language', models.CharField(db_column='CNTLAN_0', default='POR', max_length=3)),
                ('professional_category', models.CharField(db_column='CNTCSP_0', default='', max_length=20)),
                ('country', models.CharField(db_column='CRY_0', default='', max_length=3)),
                ('country_name', models.CharField(db_column='CRYNAM_0', default='', max_length=40)),
                ('address_0', models.CharField(db_column='ADD_0', default='', max_length=50)),
                ('address_1', models.CharField(db_column='ADD_1', default='', max_length=50)),
                ('address_2', models.CharField(db_column='ADD_2', default='', max_length=50)),
                ('postal_code', models.CharField(db_column='ZIP_0', default='', max_length=10)),
                ('city', models.CharField(db_column='CTY_0', default='', max_length=40)),
                ('state', models.CharField(db_column='SAT_0', default='', max_length=35)),
                ('landline', models.CharField(db_column='CNTETS_0', default='', max_length=40)),
                ('fax', models.CharField(db_column='CNTFAX_0', default='', max_length=40)),
                ('cell_phone', models.CharField(db_column='CNTMOB_0', default='', max_length=40)),
                ('is_mailing_prohibited', models.SmallIntegerField(db_column='CNTFBDMAG_0', default=1)),
                ('create_user', models.CharField(db_column='CREUSR_0', default='INTER', max_length=5)),
                ('create_date', models.DateTimeField(db_column='CREDAT_0', default=django.utils.timezone.now)),
                ('update_user', models.CharField(db_column='UPDUSR_0', default='INTER', max_length=5)),
                ('update_date', models.DateTimeField(db_column='UPDDAT_0', default=django.utils.timezone.now)),
                ('export_number', models.IntegerField(db_column='EXPNUM_0', default=0)),
                ('create_datetime', models.DateTimeField(auto_now_add=True, db_column='CREDATTIM_0')),
                ('update_datetime', models.DateTimeField(auto_now=True, db_column='UPDDATTIM_0')),
                ('auuid', models.TextField(db_column='AUUID_0')),
                ('identity_card', models.CharField(db_column='UIDCRDNUM_0', default='', max_length=1)),
                ('social_security_fund', models.DecimalField(db_column='SSCNUM_0', decimal_places=8, default=0, max_digits=28)),
                ('visa', models.CharField(db_column='RDEPITNUM_0', default='', max_length=1)),
                ('id', models.AutoField(db_column='ROWID', primary_key=True, serialize=False)),
                ('code', models.CharField(db_column='CNTNUM_0', max_length=15, unique=True)),
                ('full_name', models.CharField(db_column='CNTFULNAM_0', max_length=60)),
                ('last_name', models.CharField(db_column='CNTLNA_0', max_length=35)),
                ('first_name', models.CharField(db_column='CNTFNA_0', max_length=20)),
                ('email', models.EmailField(db_column='CNTEMA_0', default='', max_length=80, unique=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'db_table': 'CONTACTCRM',
                'managed': False,
            },
        ),
    ]
