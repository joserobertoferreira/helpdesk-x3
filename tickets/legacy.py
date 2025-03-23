# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Serrequest(models.Model):
    updtick_0 = models.IntegerField(db_column='UPDTICK_0')  # Field name made lowercase.
    srenum_0 = models.CharField(db_column='SRENUM_0', unique=True, max_length=20)  # Field name made lowercase.
    srenumbpc_0 = models.CharField(db_column='SRENUMBPC_0', max_length=20)  # Field name made lowercase.
    sreinumbpc_0 = models.IntegerField(db_column='SREINUMBPC_0')  # Field name made lowercase.
    salfcy_0 = models.CharField(db_column='SALFCY_0', max_length=5)  # Field name made lowercase.
    sredoo_0 = models.CharField(db_column='SREDOO_0', max_length=15)  # Field name made lowercase.
    srebpc_0 = models.CharField(db_column='SREBPC_0', max_length=15)  # Field name made lowercase.
    srebpaadd_0 = models.CharField(db_column='SREBPAADD_0', max_length=5)  # Field name made lowercase.
    sreccn_0 = models.CharField(db_column='SRECCN_0', max_length=15)  # Field name made lowercase.
    srebpcinv_0 = models.CharField(db_column='SREBPCINV_0', max_length=15)  # Field name made lowercase.
    srebpcpyr_0 = models.CharField(db_column='SREBPCPYR_0', max_length=15)  # Field name made lowercase.
    srebpcgru_0 = models.CharField(db_column='SREBPCGRU_0', max_length=15)  # Field name made lowercase.
    srepjt_0 = models.CharField(db_column='SREPJT_0', max_length=40)  # Field name made lowercase.
    srerep_0 = models.CharField(db_column='SREREP_0', max_length=15)  # Field name made lowercase.
    srerep_1 = models.CharField(db_column='SREREP_1', max_length=15)  # Field name made lowercase.
    sremac_0 = models.CharField(db_column='SREMAC_0', max_length=20)  # Field name made lowercase.
    sremacpbl_0 = models.CharField(db_column='SREMACPBL_0', max_length=20)  # Field name made lowercase.
    stofcy_0 = models.CharField(db_column='STOFCY_0', max_length=5)  # Field name made lowercase.
    srevacbpr_0 = models.CharField(db_column='SREVACBPR_0', max_length=5)  # Field name made lowercase.
    sstentcod_0 = models.CharField(db_column='SSTENTCOD_0', max_length=10)  # Field name made lowercase.
    srechgtyp_0 = models.SmallIntegerField(db_column='SRECHGTYP_0')  # Field name made lowercase.
    sreprityp_0 = models.SmallIntegerField(db_column='SREPRITYP_0')  # Field name made lowercase.
    srecur_0 = models.CharField(db_column='SRECUR_0', max_length=3)  # Field name made lowercase.
    srepte_0 = models.CharField(db_column='SREPTE_0', max_length=15)  # Field name made lowercase.
    sredep_0 = models.CharField(db_column='SREDEP_0', max_length=5)  # Field name made lowercase.
    die_0 = models.CharField(db_column='DIE_0', max_length=3)  # Field name made lowercase.
    die_1 = models.CharField(db_column='DIE_1', max_length=3)  # Field name made lowercase.
    die_2 = models.CharField(db_column='DIE_2', max_length=3)  # Field name made lowercase.
    die_3 = models.CharField(db_column='DIE_3', max_length=3)  # Field name made lowercase.
    die_4 = models.CharField(db_column='DIE_4', max_length=3)  # Field name made lowercase.
    die_5 = models.CharField(db_column='DIE_5', max_length=3)  # Field name made lowercase.
    die_6 = models.CharField(db_column='DIE_6', max_length=3)  # Field name made lowercase.
    die_7 = models.CharField(db_column='DIE_7', max_length=3)  # Field name made lowercase.
    die_8 = models.CharField(db_column='DIE_8', max_length=3)  # Field name made lowercase.
    die_9 = models.CharField(db_column='DIE_9', max_length=3)  # Field name made lowercase.
    die_10 = models.CharField(db_column='DIE_10', max_length=3)  # Field name made lowercase.
    die_11 = models.CharField(db_column='DIE_11', max_length=3)  # Field name made lowercase.
    die_12 = models.CharField(db_column='DIE_12', max_length=3)  # Field name made lowercase.
    die_13 = models.CharField(db_column='DIE_13', max_length=3)  # Field name made lowercase.
    die_14 = models.CharField(db_column='DIE_14', max_length=3)  # Field name made lowercase.
    die_15 = models.CharField(db_column='DIE_15', max_length=3)  # Field name made lowercase.
    die_16 = models.CharField(db_column='DIE_16', max_length=3)  # Field name made lowercase.
    die_17 = models.CharField(db_column='DIE_17', max_length=3)  # Field name made lowercase.
    die_18 = models.CharField(db_column='DIE_18', max_length=3)  # Field name made lowercase.
    die_19 = models.CharField(db_column='DIE_19', max_length=3)  # Field name made lowercase.
    cce_0 = models.CharField(db_column='CCE_0', max_length=15)  # Field name made lowercase.
    cce_1 = models.CharField(db_column='CCE_1', max_length=15)  # Field name made lowercase.
    cce_2 = models.CharField(db_column='CCE_2', max_length=15)  # Field name made lowercase.
    cce_3 = models.CharField(db_column='CCE_3', max_length=15)  # Field name made lowercase.
    cce_4 = models.CharField(db_column='CCE_4', max_length=15)  # Field name made lowercase.
    cce_5 = models.CharField(db_column='CCE_5', max_length=15)  # Field name made lowercase.
    cce_6 = models.CharField(db_column='CCE_6', max_length=15)  # Field name made lowercase.
    cce_7 = models.CharField(db_column='CCE_7', max_length=15)  # Field name made lowercase.
    cce_8 = models.CharField(db_column='CCE_8', max_length=15)  # Field name made lowercase.
    cce_9 = models.CharField(db_column='CCE_9', max_length=15)  # Field name made lowercase.
    cce_10 = models.CharField(db_column='CCE_10', max_length=15)  # Field name made lowercase.
    cce_11 = models.CharField(db_column='CCE_11', max_length=15)  # Field name made lowercase.
    cce_12 = models.CharField(db_column='CCE_12', max_length=15)  # Field name made lowercase.
    cce_13 = models.CharField(db_column='CCE_13', max_length=15)  # Field name made lowercase.
    cce_14 = models.CharField(db_column='CCE_14', max_length=15)  # Field name made lowercase.
    cce_15 = models.CharField(db_column='CCE_15', max_length=15)  # Field name made lowercase.
    cce_16 = models.CharField(db_column='CCE_16', max_length=15)  # Field name made lowercase.
    cce_17 = models.CharField(db_column='CCE_17', max_length=15)  # Field name made lowercase.
    cce_18 = models.CharField(db_column='CCE_18', max_length=15)  # Field name made lowercase.
    cce_19 = models.CharField(db_column='CCE_19', max_length=15)  # Field name made lowercase.
    invdtaamt_0 = models.DecimalField(db_column='INVDTAAMT_0', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_1 = models.DecimalField(db_column='INVDTAAMT_1', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_2 = models.DecimalField(db_column='INVDTAAMT_2', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_3 = models.DecimalField(db_column='INVDTAAMT_3', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_4 = models.DecimalField(db_column='INVDTAAMT_4', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_5 = models.DecimalField(db_column='INVDTAAMT_5', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_6 = models.DecimalField(db_column='INVDTAAMT_6', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_7 = models.DecimalField(db_column='INVDTAAMT_7', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_8 = models.DecimalField(db_column='INVDTAAMT_8', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_9 = models.DecimalField(db_column='INVDTAAMT_9', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_10 = models.DecimalField(db_column='INVDTAAMT_10', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_11 = models.DecimalField(db_column='INVDTAAMT_11', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_12 = models.DecimalField(db_column='INVDTAAMT_12', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_13 = models.DecimalField(db_column='INVDTAAMT_13', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_14 = models.DecimalField(db_column='INVDTAAMT_14', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_15 = models.DecimalField(db_column='INVDTAAMT_15', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_16 = models.DecimalField(db_column='INVDTAAMT_16', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_17 = models.DecimalField(db_column='INVDTAAMT_17', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_18 = models.DecimalField(db_column='INVDTAAMT_18', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_19 = models.DecimalField(db_column='INVDTAAMT_19', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_20 = models.DecimalField(db_column='INVDTAAMT_20', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_21 = models.DecimalField(db_column='INVDTAAMT_21', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_22 = models.DecimalField(db_column='INVDTAAMT_22', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_23 = models.DecimalField(db_column='INVDTAAMT_23', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_24 = models.DecimalField(db_column='INVDTAAMT_24', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_25 = models.DecimalField(db_column='INVDTAAMT_25', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_26 = models.DecimalField(db_column='INVDTAAMT_26', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_27 = models.DecimalField(db_column='INVDTAAMT_27', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_28 = models.DecimalField(db_column='INVDTAAMT_28', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtaamt_29 = models.DecimalField(db_column='INVDTAAMT_29', max_digits=20, decimal_places=5)  # Field name made lowercase.
    invdtatyp_0 = models.SmallIntegerField(db_column='INVDTATYP_0')  # Field name made lowercase.
    invdtatyp_1 = models.SmallIntegerField(db_column='INVDTATYP_1')  # Field name made lowercase.
    invdtatyp_2 = models.SmallIntegerField(db_column='INVDTATYP_2')  # Field name made lowercase.
    invdtatyp_3 = models.SmallIntegerField(db_column='INVDTATYP_3')  # Field name made lowercase.
    invdtatyp_4 = models.SmallIntegerField(db_column='INVDTATYP_4')  # Field name made lowercase.
    invdtatyp_5 = models.SmallIntegerField(db_column='INVDTATYP_5')  # Field name made lowercase.
    invdtatyp_6 = models.SmallIntegerField(db_column='INVDTATYP_6')  # Field name made lowercase.
    invdtatyp_7 = models.SmallIntegerField(db_column='INVDTATYP_7')  # Field name made lowercase.
    invdtatyp_8 = models.SmallIntegerField(db_column='INVDTATYP_8')  # Field name made lowercase.
    invdtatyp_9 = models.SmallIntegerField(db_column='INVDTATYP_9')  # Field name made lowercase.
    invdtatyp_10 = models.SmallIntegerField(db_column='INVDTATYP_10')  # Field name made lowercase.
    invdtatyp_11 = models.SmallIntegerField(db_column='INVDTATYP_11')  # Field name made lowercase.
    invdtatyp_12 = models.SmallIntegerField(db_column='INVDTATYP_12')  # Field name made lowercase.
    invdtatyp_13 = models.SmallIntegerField(db_column='INVDTATYP_13')  # Field name made lowercase.
    invdtatyp_14 = models.SmallIntegerField(db_column='INVDTATYP_14')  # Field name made lowercase.
    invdtatyp_15 = models.SmallIntegerField(db_column='INVDTATYP_15')  # Field name made lowercase.
    invdtatyp_16 = models.SmallIntegerField(db_column='INVDTATYP_16')  # Field name made lowercase.
    invdtatyp_17 = models.SmallIntegerField(db_column='INVDTATYP_17')  # Field name made lowercase.
    invdtatyp_18 = models.SmallIntegerField(db_column='INVDTATYP_18')  # Field name made lowercase.
    invdtatyp_19 = models.SmallIntegerField(db_column='INVDTATYP_19')  # Field name made lowercase.
    invdtatyp_20 = models.SmallIntegerField(db_column='INVDTATYP_20')  # Field name made lowercase.
    invdtatyp_21 = models.SmallIntegerField(db_column='INVDTATYP_21')  # Field name made lowercase.
    invdtatyp_22 = models.SmallIntegerField(db_column='INVDTATYP_22')  # Field name made lowercase.
    invdtatyp_23 = models.SmallIntegerField(db_column='INVDTATYP_23')  # Field name made lowercase.
    invdtatyp_24 = models.SmallIntegerField(db_column='INVDTATYP_24')  # Field name made lowercase.
    invdtatyp_25 = models.SmallIntegerField(db_column='INVDTATYP_25')  # Field name made lowercase.
    invdtatyp_26 = models.SmallIntegerField(db_column='INVDTATYP_26')  # Field name made lowercase.
    invdtatyp_27 = models.SmallIntegerField(db_column='INVDTATYP_27')  # Field name made lowercase.
    invdtatyp_28 = models.SmallIntegerField(db_column='INVDTATYP_28')  # Field name made lowercase.
    invdtatyp_29 = models.SmallIntegerField(db_column='INVDTATYP_29')  # Field name made lowercase.
    invdta_0 = models.SmallIntegerField(db_column='INVDTA_0')  # Field name made lowercase.
    invdta_1 = models.SmallIntegerField(db_column='INVDTA_1')  # Field name made lowercase.
    invdta_2 = models.SmallIntegerField(db_column='INVDTA_2')  # Field name made lowercase.
    invdta_3 = models.SmallIntegerField(db_column='INVDTA_3')  # Field name made lowercase.
    invdta_4 = models.SmallIntegerField(db_column='INVDTA_4')  # Field name made lowercase.
    invdta_5 = models.SmallIntegerField(db_column='INVDTA_5')  # Field name made lowercase.
    invdta_6 = models.SmallIntegerField(db_column='INVDTA_6')  # Field name made lowercase.
    invdta_7 = models.SmallIntegerField(db_column='INVDTA_7')  # Field name made lowercase.
    invdta_8 = models.SmallIntegerField(db_column='INVDTA_8')  # Field name made lowercase.
    invdta_9 = models.SmallIntegerField(db_column='INVDTA_9')  # Field name made lowercase.
    invdta_10 = models.SmallIntegerField(db_column='INVDTA_10')  # Field name made lowercase.
    invdta_11 = models.SmallIntegerField(db_column='INVDTA_11')  # Field name made lowercase.
    invdta_12 = models.SmallIntegerField(db_column='INVDTA_12')  # Field name made lowercase.
    invdta_13 = models.SmallIntegerField(db_column='INVDTA_13')  # Field name made lowercase.
    invdta_14 = models.SmallIntegerField(db_column='INVDTA_14')  # Field name made lowercase.
    invdta_15 = models.SmallIntegerField(db_column='INVDTA_15')  # Field name made lowercase.
    invdta_16 = models.SmallIntegerField(db_column='INVDTA_16')  # Field name made lowercase.
    invdta_17 = models.SmallIntegerField(db_column='INVDTA_17')  # Field name made lowercase.
    invdta_18 = models.SmallIntegerField(db_column='INVDTA_18')  # Field name made lowercase.
    invdta_19 = models.SmallIntegerField(db_column='INVDTA_19')  # Field name made lowercase.
    invdta_20 = models.SmallIntegerField(db_column='INVDTA_20')  # Field name made lowercase.
    invdta_21 = models.SmallIntegerField(db_column='INVDTA_21')  # Field name made lowercase.
    invdta_22 = models.SmallIntegerField(db_column='INVDTA_22')  # Field name made lowercase.
    invdta_23 = models.SmallIntegerField(db_column='INVDTA_23')  # Field name made lowercase.
    invdta_24 = models.SmallIntegerField(db_column='INVDTA_24')  # Field name made lowercase.
    invdta_25 = models.SmallIntegerField(db_column='INVDTA_25')  # Field name made lowercase.
    invdta_26 = models.SmallIntegerField(db_column='INVDTA_26')  # Field name made lowercase.
    invdta_27 = models.SmallIntegerField(db_column='INVDTA_27')  # Field name made lowercase.
    invdta_28 = models.SmallIntegerField(db_column='INVDTA_28')  # Field name made lowercase.
    invdta_29 = models.SmallIntegerField(db_column='INVDTA_29')  # Field name made lowercase.
    sfisstcod_0 = models.CharField(db_column='SFISSTCOD_0', max_length=20)  # Field name made lowercase.
    sfisstcod_1 = models.CharField(db_column='SFISSTCOD_1', max_length=20)  # Field name made lowercase.
    sfisstcod_2 = models.CharField(db_column='SFISSTCOD_2', max_length=20)  # Field name made lowercase.
    sfisstcod_3 = models.CharField(db_column='SFISSTCOD_3', max_length=20)  # Field name made lowercase.
    sfisstcod_4 = models.CharField(db_column='SFISSTCOD_4', max_length=20)  # Field name made lowercase.
    sfisstcod_5 = models.CharField(db_column='SFISSTCOD_5', max_length=20)  # Field name made lowercase.
    sfisstcod_6 = models.CharField(db_column='SFISSTCOD_6', max_length=20)  # Field name made lowercase.
    sfisstcod_7 = models.CharField(db_column='SFISSTCOD_7', max_length=20)  # Field name made lowercase.
    sfisstcod_8 = models.CharField(db_column='SFISSTCOD_8', max_length=20)  # Field name made lowercase.
    sfisstcod_9 = models.CharField(db_column='SFISSTCOD_9', max_length=20)  # Field name made lowercase.
    sfisstcod_10 = models.CharField(db_column='SFISSTCOD_10', max_length=20)  # Field name made lowercase.
    sfisstcod_11 = models.CharField(db_column='SFISSTCOD_11', max_length=20)  # Field name made lowercase.
    sfisstcod_12 = models.CharField(db_column='SFISSTCOD_12', max_length=20)  # Field name made lowercase.
    sfisstcod_13 = models.CharField(db_column='SFISSTCOD_13', max_length=20)  # Field name made lowercase.
    sfisstcod_14 = models.CharField(db_column='SFISSTCOD_14', max_length=20)  # Field name made lowercase.
    sfisstcod_15 = models.CharField(db_column='SFISSTCOD_15', max_length=20)  # Field name made lowercase.
    sfisstcod_16 = models.CharField(db_column='SFISSTCOD_16', max_length=20)  # Field name made lowercase.
    sfisstcod_17 = models.CharField(db_column='SFISSTCOD_17', max_length=20)  # Field name made lowercase.
    sfisstcod_18 = models.CharField(db_column='SFISSTCOD_18', max_length=20)  # Field name made lowercase.
    sfisstcod_19 = models.CharField(db_column='SFISSTCOD_19', max_length=20)  # Field name made lowercase.
    sfisstcod_20 = models.CharField(db_column='SFISSTCOD_20', max_length=20)  # Field name made lowercase.
    sfisstcod_21 = models.CharField(db_column='SFISSTCOD_21', max_length=20)  # Field name made lowercase.
    sfisstcod_22 = models.CharField(db_column='SFISSTCOD_22', max_length=20)  # Field name made lowercase.
    sfisstcod_23 = models.CharField(db_column='SFISSTCOD_23', max_length=20)  # Field name made lowercase.
    sfisstcod_24 = models.CharField(db_column='SFISSTCOD_24', max_length=20)  # Field name made lowercase.
    sfisstcod_25 = models.CharField(db_column='SFISSTCOD_25', max_length=20)  # Field name made lowercase.
    sfisstcod_26 = models.CharField(db_column='SFISSTCOD_26', max_length=20)  # Field name made lowercase.
    sfisstcod_27 = models.CharField(db_column='SFISSTCOD_27', max_length=20)  # Field name made lowercase.
    sfisstcod_28 = models.CharField(db_column='SFISSTCOD_28', max_length=20)  # Field name made lowercase.
    sfisstcod_29 = models.CharField(db_column='SFISSTCOD_29', max_length=20)  # Field name made lowercase.
    typmac_0 = models.SmallIntegerField(db_column='TYPMAC_0')  # Field name made lowercase.
    macflt_0 = models.CharField(db_column='MACFLT_0', max_length=20)  # Field name made lowercase.
    macfltint_0 = models.SmallIntegerField(db_column='MACFLTINT_0')  # Field name made lowercase.
    srettr_0 = models.CharField(db_column='SRETTR_0', max_length=80)  # Field name made lowercase.
    sredes_0 = models.CharField(db_column='SREDES_0', max_length=250)  # Field name made lowercase.
    typfuldes_0 = models.CharField(db_column='TYPFULDES_0', max_length=10)  # Field name made lowercase.
    numfuldes_0 = models.CharField(db_column='NUMFULDES_0', max_length=30)  # Field name made lowercase.
    sredesflg_0 = models.SmallIntegerField(db_column='SREDESFLG_0')  # Field name made lowercase.
    sreass_0 = models.SmallIntegerField(db_column='SREASS_0')  # Field name made lowercase.
    sredet_0 = models.CharField(db_column='SREDET_0', max_length=20)  # Field name made lowercase.
    sreinvflg_0 = models.SmallIntegerField(db_column='SREINVFLG_0')  # Field name made lowercase.
    sredatass_0 = models.DateTimeField(db_column='SREDATASS_0')  # Field name made lowercase.
    srehouass_0 = models.CharField(db_column='SREHOUASS_0', max_length=6)  # Field name made lowercase.
    sresat_0 = models.CharField(db_column='SRESAT_0', max_length=20)  # Field name made lowercase.
    tskrepcre_0 = models.SmallIntegerField(db_column='TSKREPCRE_0')  # Field name made lowercase.
    sregralev_0 = models.CharField(db_column='SREGRALEV_0', max_length=20)  # Field name made lowercase.
    srepiolev_0 = models.CharField(db_column='SREPIOLEV_0', max_length=20)  # Field name made lowercase.
    conspt_0 = models.CharField(db_column='CONSPT_0', max_length=20)  # Field name made lowercase.
    conspttyp_0 = models.CharField(db_column='CONSPTTYP_0', max_length=8)  # Field name made lowercase.
    consptflg_0 = models.SmallIntegerField(db_column='CONSPTFLG_0')  # Field name made lowercase.
    srepblgrp_0 = models.CharField(db_column='SREPBLGRP_0', max_length=20)  # Field name made lowercase.
    sretimspg_0 = models.SmallIntegerField(db_column='SRETIMSPG_0')  # Field name made lowercase.
    timspgday_0 = models.IntegerField(db_column='TIMSPGDAY_0')  # Field name made lowercase.
    timspghou_0 = models.IntegerField(db_column='TIMSPGHOU_0')  # Field name made lowercase.
    timspgmnt_0 = models.IntegerField(db_column='TIMSPGMNT_0')  # Field name made lowercase.
    ctimspgday_0 = models.IntegerField(db_column='CTIMSPGDAY_0')  # Field name made lowercase.
    ctimspghou_0 = models.IntegerField(db_column='CTIMSPGHOU_0')  # Field name made lowercase.
    ctimspgmnt_0 = models.IntegerField(db_column='CTIMSPGMNT_0')  # Field name made lowercase.
    sreesc_0 = models.SmallIntegerField(db_column='SREESC_0')  # Field name made lowercase.
    sreesc2_0 = models.SmallIntegerField(db_column='SREESC2_0')  # Field name made lowercase.
    sreesc3_0 = models.SmallIntegerField(db_column='SREESC3_0')  # Field name made lowercase.
    sreresdat_0 = models.DateTimeField(db_column='SRERESDAT_0')  # Field name made lowercase.
    srereshou_0 = models.CharField(db_column='SRERESHOU_0', max_length=6)  # Field name made lowercase.
    manupd_0 = models.SmallIntegerField(db_column='MANUPD_0')  # Field name made lowercase.
    srelok_0 = models.SmallIntegerField(db_column='SRELOK_0')  # Field name made lowercase.
    sreresren_0 = models.CharField(db_column='SRERESREN_0', max_length=80)  # Field name made lowercase.
    ovrcov_0 = models.SmallIntegerField(db_column='OVRCOV_0')  # Field name made lowercase.
    ovrcovren_0 = models.SmallIntegerField(db_column='OVRCOVREN_0')  # Field name made lowercase.
    ovrcovtyp_0 = models.CharField(db_column='OVRCOVTYP_0', max_length=8)  # Field name made lowercase.
    srecov_0 = models.SmallIntegerField(db_column='SRECOV_0')  # Field name made lowercase.
    sretypcov_0 = models.SmallIntegerField(db_column='SRETYPCOV_0')  # Field name made lowercase.
    srecovnum_0 = models.CharField(db_column='SRECOVNUM_0', max_length=20)  # Field name made lowercase.
    srecovaut_0 = models.SmallIntegerField(db_column='SRECOVAUT_0')  # Field name made lowercase.
    srecovaus_0 = models.CharField(db_column='SRECOVAUS_0', max_length=5)  # Field name made lowercase.
    covauscla_0 = models.CharField(db_column='COVAUSCLA_0', max_length=30)  # Field name made lowercase.
    srecovctl_0 = models.CharField(db_column='SRECOVCTL_0', max_length=5)  # Field name made lowercase.
    solnum_0 = models.CharField(db_column='SOLNUM_0', max_length=20)  # Field name made lowercase.
    rep_0 = models.CharField(db_column='REP_0', max_length=5)  # Field name made lowercase.
    sreori_0 = models.SmallIntegerField(db_column='SREORI_0')  # Field name made lowercase.
    sreorivcr_0 = models.CharField(db_column='SREORIVCR_0', max_length=20)  # Field name made lowercase.
    sreorivcrl_0 = models.IntegerField(db_column='SREORIVCRL_0')  # Field name made lowercase.
    sretpl_0 = models.CharField(db_column='SRETPL_0', max_length=20)  # Field name made lowercase.
    tsdcod_0 = models.CharField(db_column='TSDCOD_0', max_length=20)  # Field name made lowercase.
    tsdcod_1 = models.CharField(db_column='TSDCOD_1', max_length=20)  # Field name made lowercase.
    tsdcod_2 = models.CharField(db_column='TSDCOD_2', max_length=20)  # Field name made lowercase.
    tsdcod_3 = models.CharField(db_column='TSDCOD_3', max_length=20)  # Field name made lowercase.
    tsdcod_4 = models.CharField(db_column='TSDCOD_4', max_length=20)  # Field name made lowercase.
    trscod_0 = models.CharField(db_column='TRSCOD_0', max_length=20)  # Field name made lowercase.
    entcod_0 = models.CharField(db_column='ENTCOD_0', max_length=5)  # Field name made lowercase.
    trsfam_0 = models.CharField(db_column='TRSFAM_0', max_length=20)  # Field name made lowercase.
    nbrmanupd_0 = models.IntegerField(db_column='NBRMANUPD_0')  # Field name made lowercase.
    creusr_0 = models.CharField(db_column='CREUSR_0', max_length=5)  # Field name made lowercase.
    credat_0 = models.DateTimeField(db_column='CREDAT_0')  # Field name made lowercase.
    crehou_0 = models.CharField(db_column='CREHOU_0', max_length=6)  # Field name made lowercase.
    updusr_0 = models.CharField(db_column='UPDUSR_0', max_length=5)  # Field name made lowercase.
    upddat_0 = models.DateTimeField(db_column='UPDDAT_0')  # Field name made lowercase.
    credattim_0 = models.DateTimeField(db_column='CREDATTIM_0')  # Field name made lowercase.
    upddattim_0 = models.DateTimeField(db_column='UPDDATTIM_0')  # Field name made lowercase.
    auuid_0 = models.TextField(db_column='AUUID_0')  # Field name made lowercase. This field type is a guess.
    rowid = models.AutoField(db_column='ROWID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SERREQUEST'
        unique_together = (('credat_0', 'srenum_0'), ('sreresdat_0', 'srereshou_0', 'sreass_0', 'srenum_0'),)
