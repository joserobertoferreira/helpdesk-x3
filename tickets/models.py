from django.db import models


class Ticket(models.Model):
    updtick_0 = models.IntegerField(db_column='UPDTICK_0')
    srenum_0 = models.CharField(db_column='SRENUM_0', unique=True, max_length=20)
    srenumbpc_0 = models.CharField(db_column='SRENUMBPC_0', max_length=20)
    sreinumbpc_0 = models.IntegerField(db_column='SREINUMBPC_0')
    salfcy_0 = models.CharField(db_column='SALFCY_0', max_length=5)
    sredoo_0 = models.CharField(db_column='SREDOO_0', max_length=15)
    srebpc_0 = models.CharField(db_column='SREBPC_0', max_length=15)
    srebpaadd_0 = models.CharField(db_column='SREBPAADD_0', max_length=5)
    sreccn_0 = models.CharField(db_column='SRECCN_0', max_length=15)
    srebpcinv_0 = models.CharField(db_column='SREBPCINV_0', max_length=15)
    srebpcpyr_0 = models.CharField(db_column='SREBPCPYR_0', max_length=15)
    srebpcgru_0 = models.CharField(db_column='SREBPCGRU_0', max_length=15)
    srepjt_0 = models.CharField(db_column='SREPJT_0', max_length=40)
    srerep_0 = models.CharField(db_column='SREREP_0', max_length=15)
    srerep_1 = models.CharField(db_column='SREREP_1', max_length=15)
    sremac_0 = models.CharField(db_column='SREMAC_0', max_length=20)
    sremacpbl_0 = models.CharField(db_column='SREMACPBL_0', max_length=20)
    stofcy_0 = models.CharField(db_column='STOFCY_0', max_length=5)
    srevacbpr_0 = models.CharField(db_column='SREVACBPR_0', max_length=5)
    sstentcod_0 = models.CharField(db_column='SSTENTCOD_0', max_length=10)
    srechgtyp_0 = models.SmallIntegerField(db_column='SRECHGTYP_0')
    sreprityp_0 = models.SmallIntegerField(db_column='SREPRITYP_0')
    srecur_0 = models.CharField(db_column='SRECUR_0', max_length=3)
    srepte_0 = models.CharField(db_column='SREPTE_0', max_length=15)
    sredep_0 = models.CharField(db_column='SREDEP_0', max_length=5)
    die_0 = models.CharField(db_column='DIE_0', max_length=3)
    die_1 = models.CharField(db_column='DIE_1', max_length=3)
    die_2 = models.CharField(db_column='DIE_2', max_length=3)
    die_3 = models.CharField(db_column='DIE_3', max_length=3)
    die_4 = models.CharField(db_column='DIE_4', max_length=3)
    die_5 = models.CharField(db_column='DIE_5', max_length=3)
    die_6 = models.CharField(db_column='DIE_6', max_length=3)
    die_7 = models.CharField(db_column='DIE_7', max_length=3)
    die_8 = models.CharField(db_column='DIE_8', max_length=3)
    die_9 = models.CharField(db_column='DIE_9', max_length=3)
    die_10 = models.CharField(db_column='DIE_10', max_length=3)
    die_11 = models.CharField(db_column='DIE_11', max_length=3)
    die_12 = models.CharField(db_column='DIE_12', max_length=3)
    die_13 = models.CharField(db_column='DIE_13', max_length=3)
    die_14 = models.CharField(db_column='DIE_14', max_length=3)
    die_15 = models.CharField(db_column='DIE_15', max_length=3)
    die_16 = models.CharField(db_column='DIE_16', max_length=3)
    die_17 = models.CharField(db_column='DIE_17', max_length=3)
    die_18 = models.CharField(db_column='DIE_18', max_length=3)
    die_19 = models.CharField(db_column='DIE_19', max_length=3)
    cce_0 = models.CharField(db_column='CCE_0', max_length=15)
    cce_1 = models.CharField(db_column='CCE_1', max_length=15)
    cce_2 = models.CharField(db_column='CCE_2', max_length=15)
    cce_3 = models.CharField(db_column='CCE_3', max_length=15)
    cce_4 = models.CharField(db_column='CCE_4', max_length=15)
    cce_5 = models.CharField(db_column='CCE_5', max_length=15)
    cce_6 = models.CharField(db_column='CCE_6', max_length=15)
    cce_7 = models.CharField(db_column='CCE_7', max_length=15)
    cce_8 = models.CharField(db_column='CCE_8', max_length=15)
    cce_9 = models.CharField(db_column='CCE_9', max_length=15)
    cce_10 = models.CharField(db_column='CCE_10', max_length=15)
    cce_11 = models.CharField(db_column='CCE_11', max_length=15)
    cce_12 = models.CharField(db_column='CCE_12', max_length=15)
    cce_13 = models.CharField(db_column='CCE_13', max_length=15)
    cce_14 = models.CharField(db_column='CCE_14', max_length=15)
    cce_15 = models.CharField(db_column='CCE_15', max_length=15)
    cce_16 = models.CharField(db_column='CCE_16', max_length=15)
    cce_17 = models.CharField(db_column='CCE_17', max_length=15)
    cce_18 = models.CharField(db_column='CCE_18', max_length=15)
    cce_19 = models.CharField(db_column='CCE_19', max_length=15)
    invdtaamt_0 = models.DecimalField(
        db_column='INVDTAAMT_0', max_digits=20, decimal_places=5
    )
    invdtaamt_1 = models.DecimalField(
        db_column='INVDTAAMT_1', max_digits=20, decimal_places=5
    )
    invdtaamt_2 = models.DecimalField(
        db_column='INVDTAAMT_2', max_digits=20, decimal_places=5
    )
    invdtaamt_3 = models.DecimalField(
        db_column='INVDTAAMT_3', max_digits=20, decimal_places=5
    )
    invdtaamt_4 = models.DecimalField(
        db_column='INVDTAAMT_4', max_digits=20, decimal_places=5
    )
    invdtaamt_5 = models.DecimalField(
        db_column='INVDTAAMT_5', max_digits=20, decimal_places=5
    )
    invdtaamt_6 = models.DecimalField(
        db_column='INVDTAAMT_6', max_digits=20, decimal_places=5
    )
    invdtaamt_7 = models.DecimalField(
        db_column='INVDTAAMT_7', max_digits=20, decimal_places=5
    )
    invdtaamt_8 = models.DecimalField(
        db_column='INVDTAAMT_8', max_digits=20, decimal_places=5
    )
    invdtaamt_9 = models.DecimalField(
        db_column='INVDTAAMT_9', max_digits=20, decimal_places=5
    )
    invdtaamt_10 = models.DecimalField(
        db_column='INVDTAAMT_10', max_digits=20, decimal_places=5
    )
    invdtaamt_11 = models.DecimalField(
        db_column='INVDTAAMT_11', max_digits=20, decimal_places=5
    )
    invdtaamt_12 = models.DecimalField(
        db_column='INVDTAAMT_12', max_digits=20, decimal_places=5
    )
    invdtaamt_13 = models.DecimalField(
        db_column='INVDTAAMT_13', max_digits=20, decimal_places=5
    )
    invdtaamt_14 = models.DecimalField(
        db_column='INVDTAAMT_14', max_digits=20, decimal_places=5
    )
    invdtaamt_15 = models.DecimalField(
        db_column='INVDTAAMT_15', max_digits=20, decimal_places=5
    )
    invdtaamt_16 = models.DecimalField(
        db_column='INVDTAAMT_16', max_digits=20, decimal_places=5
    )
    invdtaamt_17 = models.DecimalField(
        db_column='INVDTAAMT_17', max_digits=20, decimal_places=5
    )
    invdtaamt_18 = models.DecimalField(
        db_column='INVDTAAMT_18', max_digits=20, decimal_places=5
    )
    invdtaamt_19 = models.DecimalField(
        db_column='INVDTAAMT_19', max_digits=20, decimal_places=5
    )
    invdtaamt_20 = models.DecimalField(
        db_column='INVDTAAMT_20', max_digits=20, decimal_places=5
    )
    invdtaamt_21 = models.DecimalField(
        db_column='INVDTAAMT_21', max_digits=20, decimal_places=5
    )
    invdtaamt_22 = models.DecimalField(
        db_column='INVDTAAMT_22', max_digits=20, decimal_places=5
    )
    invdtaamt_23 = models.DecimalField(
        db_column='INVDTAAMT_23', max_digits=20, decimal_places=5
    )
    invdtaamt_24 = models.DecimalField(
        db_column='INVDTAAMT_24', max_digits=20, decimal_places=5
    )
    invdtaamt_25 = models.DecimalField(
        db_column='INVDTAAMT_25', max_digits=20, decimal_places=5
    )
    invdtaamt_26 = models.DecimalField(
        db_column='INVDTAAMT_26', max_digits=20, decimal_places=5
    )
    invdtaamt_27 = models.DecimalField(
        db_column='INVDTAAMT_27', max_digits=20, decimal_places=5
    )
    invdtaamt_28 = models.DecimalField(
        db_column='INVDTAAMT_28', max_digits=20, decimal_places=5
    )
    invdtaamt_29 = models.DecimalField(
        db_column='INVDTAAMT_29', max_digits=20, decimal_places=5
    )
    invdtatyp_0 = models.SmallIntegerField(db_column='INVDTATYP_0')
    invdtatyp_1 = models.SmallIntegerField(db_column='INVDTATYP_1')
    invdtatyp_2 = models.SmallIntegerField(db_column='INVDTATYP_2')
    invdtatyp_3 = models.SmallIntegerField(db_column='INVDTATYP_3')
    invdtatyp_4 = models.SmallIntegerField(db_column='INVDTATYP_4')
    invdtatyp_5 = models.SmallIntegerField(db_column='INVDTATYP_5')
    invdtatyp_6 = models.SmallIntegerField(db_column='INVDTATYP_6')
    invdtatyp_7 = models.SmallIntegerField(db_column='INVDTATYP_7')
    invdtatyp_8 = models.SmallIntegerField(db_column='INVDTATYP_8')
    invdtatyp_9 = models.SmallIntegerField(db_column='INVDTATYP_9')
    invdtatyp_10 = models.SmallIntegerField(db_column='INVDTATYP_10')
    invdtatyp_11 = models.SmallIntegerField(db_column='INVDTATYP_11')
    invdtatyp_12 = models.SmallIntegerField(db_column='INVDTATYP_12')
    invdtatyp_13 = models.SmallIntegerField(db_column='INVDTATYP_13')
    invdtatyp_14 = models.SmallIntegerField(db_column='INVDTATYP_14')
    invdtatyp_15 = models.SmallIntegerField(db_column='INVDTATYP_15')
    invdtatyp_16 = models.SmallIntegerField(db_column='INVDTATYP_16')
    invdtatyp_17 = models.SmallIntegerField(db_column='INVDTATYP_17')
    invdtatyp_18 = models.SmallIntegerField(db_column='INVDTATYP_18')
    invdtatyp_19 = models.SmallIntegerField(db_column='INVDTATYP_19')
    invdtatyp_20 = models.SmallIntegerField(db_column='INVDTATYP_20')
    invdtatyp_21 = models.SmallIntegerField(db_column='INVDTATYP_21')
    invdtatyp_22 = models.SmallIntegerField(db_column='INVDTATYP_22')
    invdtatyp_23 = models.SmallIntegerField(db_column='INVDTATYP_23')
    invdtatyp_24 = models.SmallIntegerField(db_column='INVDTATYP_24')
    invdtatyp_25 = models.SmallIntegerField(db_column='INVDTATYP_25')
    invdtatyp_26 = models.SmallIntegerField(db_column='INVDTATYP_26')
    invdtatyp_27 = models.SmallIntegerField(db_column='INVDTATYP_27')
    invdtatyp_28 = models.SmallIntegerField(db_column='INVDTATYP_28')
    invdtatyp_29 = models.SmallIntegerField(db_column='INVDTATYP_29')
    invdta_0 = models.SmallIntegerField(db_column='INVDTA_0')
    invdta_1 = models.SmallIntegerField(db_column='INVDTA_1')
    invdta_2 = models.SmallIntegerField(db_column='INVDTA_2')
    invdta_3 = models.SmallIntegerField(db_column='INVDTA_3')
    invdta_4 = models.SmallIntegerField(db_column='INVDTA_4')
    invdta_5 = models.SmallIntegerField(db_column='INVDTA_5')
    invdta_6 = models.SmallIntegerField(db_column='INVDTA_6')
    invdta_7 = models.SmallIntegerField(db_column='INVDTA_7')
    invdta_8 = models.SmallIntegerField(db_column='INVDTA_8')
    invdta_9 = models.SmallIntegerField(db_column='INVDTA_9')
    invdta_10 = models.SmallIntegerField(db_column='INVDTA_10')
    invdta_11 = models.SmallIntegerField(db_column='INVDTA_11')
    invdta_12 = models.SmallIntegerField(db_column='INVDTA_12')
    invdta_13 = models.SmallIntegerField(db_column='INVDTA_13')
    invdta_14 = models.SmallIntegerField(db_column='INVDTA_14')
    invdta_15 = models.SmallIntegerField(db_column='INVDTA_15')
    invdta_16 = models.SmallIntegerField(db_column='INVDTA_16')
    invdta_17 = models.SmallIntegerField(db_column='INVDTA_17')
    invdta_18 = models.SmallIntegerField(db_column='INVDTA_18')
    invdta_19 = models.SmallIntegerField(db_column='INVDTA_19')
    invdta_20 = models.SmallIntegerField(db_column='INVDTA_20')
    invdta_21 = models.SmallIntegerField(db_column='INVDTA_21')
    invdta_22 = models.SmallIntegerField(db_column='INVDTA_22')
    invdta_23 = models.SmallIntegerField(db_column='INVDTA_23')
    invdta_24 = models.SmallIntegerField(db_column='INVDTA_24')
    invdta_25 = models.SmallIntegerField(db_column='INVDTA_25')
    invdta_26 = models.SmallIntegerField(db_column='INVDTA_26')
    invdta_27 = models.SmallIntegerField(db_column='INVDTA_27')
    invdta_28 = models.SmallIntegerField(db_column='INVDTA_28')
    invdta_29 = models.SmallIntegerField(db_column='INVDTA_29')
    sfisstcod_0 = models.CharField(db_column='SFISSTCOD_0', max_length=20)
    sfisstcod_1 = models.CharField(db_column='SFISSTCOD_1', max_length=20)
    sfisstcod_2 = models.CharField(db_column='SFISSTCOD_2', max_length=20)
    sfisstcod_3 = models.CharField(db_column='SFISSTCOD_3', max_length=20)
    sfisstcod_4 = models.CharField(db_column='SFISSTCOD_4', max_length=20)
    sfisstcod_5 = models.CharField(db_column='SFISSTCOD_5', max_length=20)
    sfisstcod_6 = models.CharField(db_column='SFISSTCOD_6', max_length=20)
    sfisstcod_7 = models.CharField(db_column='SFISSTCOD_7', max_length=20)
    sfisstcod_8 = models.CharField(db_column='SFISSTCOD_8', max_length=20)
    sfisstcod_9 = models.CharField(db_column='SFISSTCOD_9', max_length=20)
    sfisstcod_10 = models.CharField(db_column='SFISSTCOD_10', max_length=20)
    sfisstcod_11 = models.CharField(db_column='SFISSTCOD_11', max_length=20)
    sfisstcod_12 = models.CharField(db_column='SFISSTCOD_12', max_length=20)
    sfisstcod_13 = models.CharField(db_column='SFISSTCOD_13', max_length=20)
    sfisstcod_14 = models.CharField(db_column='SFISSTCOD_14', max_length=20)
    sfisstcod_15 = models.CharField(db_column='SFISSTCOD_15', max_length=20)
    sfisstcod_16 = models.CharField(db_column='SFISSTCOD_16', max_length=20)
    sfisstcod_17 = models.CharField(db_column='SFISSTCOD_17', max_length=20)
    sfisstcod_18 = models.CharField(db_column='SFISSTCOD_18', max_length=20)
    sfisstcod_19 = models.CharField(db_column='SFISSTCOD_19', max_length=20)
    sfisstcod_20 = models.CharField(db_column='SFISSTCOD_20', max_length=20)
    sfisstcod_21 = models.CharField(db_column='SFISSTCOD_21', max_length=20)
    sfisstcod_22 = models.CharField(db_column='SFISSTCOD_22', max_length=20)
    sfisstcod_23 = models.CharField(db_column='SFISSTCOD_23', max_length=20)
    sfisstcod_24 = models.CharField(db_column='SFISSTCOD_24', max_length=20)
    sfisstcod_25 = models.CharField(db_column='SFISSTCOD_25', max_length=20)
    sfisstcod_26 = models.CharField(db_column='SFISSTCOD_26', max_length=20)
    sfisstcod_27 = models.CharField(db_column='SFISSTCOD_27', max_length=20)
    sfisstcod_28 = models.CharField(db_column='SFISSTCOD_28', max_length=20)
    sfisstcod_29 = models.CharField(db_column='SFISSTCOD_29', max_length=20)
    typmac_0 = models.SmallIntegerField(db_column='TYPMAC_0')
    macflt_0 = models.CharField(db_column='MACFLT_0', max_length=20)
    macfltint_0 = models.SmallIntegerField(db_column='MACFLTINT_0')
    srettr_0 = models.CharField(db_column='SRETTR_0', max_length=80)
    sredes_0 = models.CharField(db_column='SREDES_0', max_length=250)
    typfuldes_0 = models.CharField(db_column='TYPFULDES_0', max_length=10)
    numfuldes_0 = models.CharField(db_column='NUMFULDES_0', max_length=30)
    sredesflg_0 = models.SmallIntegerField(db_column='SREDESFLG_0')
    sreass_0 = models.SmallIntegerField(db_column='SREASS_0')
    sredet_0 = models.CharField(db_column='SREDET_0', max_length=20)
    sreinvflg_0 = models.SmallIntegerField(db_column='SREINVFLG_0')
    sredatass_0 = models.DateTimeField(db_column='SREDATASS_0')
    srehouass_0 = models.CharField(db_column='SREHOUASS_0', max_length=6)
    sresat_0 = models.CharField(db_column='SRESAT_0', max_length=20)
    tskrepcre_0 = models.SmallIntegerField(db_column='TSKREPCRE_0')
    sregralev_0 = models.CharField(db_column='SREGRALEV_0', max_length=20)
    srepiolev_0 = models.CharField(db_column='SREPIOLEV_0', max_length=20)
    conspt_0 = models.CharField(db_column='CONSPT_0', max_length=20)
    conspttyp_0 = models.CharField(db_column='CONSPTTYP_0', max_length=8)
    consptflg_0 = models.SmallIntegerField(db_column='CONSPTFLG_0')
    srepblgrp_0 = models.CharField(db_column='SREPBLGRP_0', max_length=20)
    sretimspg_0 = models.SmallIntegerField(db_column='SRETIMSPG_0')
    timspgday_0 = models.IntegerField(db_column='TIMSPGDAY_0')
    timspghou_0 = models.IntegerField(db_column='TIMSPGHOU_0')
    timspgmnt_0 = models.IntegerField(db_column='TIMSPGMNT_0')
    ctimspgday_0 = models.IntegerField(db_column='CTIMSPGDAY_0')
    ctimspghou_0 = models.IntegerField(db_column='CTIMSPGHOU_0')
    ctimspgmnt_0 = models.IntegerField(db_column='CTIMSPGMNT_0')
    sreesc_0 = models.SmallIntegerField(db_column='SREESC_0')
    sreesc2_0 = models.SmallIntegerField(db_column='SREESC2_0')
    sreesc3_0 = models.SmallIntegerField(db_column='SREESC3_0')
    sreresdat_0 = models.DateTimeField(db_column='SRERESDAT_0')
    srereshou_0 = models.CharField(db_column='SRERESHOU_0', max_length=6)
    manupd_0 = models.SmallIntegerField(db_column='MANUPD_0')
    srelok_0 = models.SmallIntegerField(db_column='SRELOK_0')
    sreresren_0 = models.CharField(db_column='SRERESREN_0', max_length=80)
    ovrcov_0 = models.SmallIntegerField(db_column='OVRCOV_0')
    ovrcovren_0 = models.SmallIntegerField(db_column='OVRCOVREN_0')
    ovrcovtyp_0 = models.CharField(db_column='OVRCOVTYP_0', max_length=8)
    srecov_0 = models.SmallIntegerField(db_column='SRECOV_0')
    sretypcov_0 = models.SmallIntegerField(db_column='SRETYPCOV_0')
    srecovnum_0 = models.CharField(db_column='SRECOVNUM_0', max_length=20)
    srecovaut_0 = models.SmallIntegerField(db_column='SRECOVAUT_0')
    srecovaus_0 = models.CharField(db_column='SRECOVAUS_0', max_length=5)
    covauscla_0 = models.CharField(db_column='COVAUSCLA_0', max_length=30)
    srecovctl_0 = models.CharField(db_column='SRECOVCTL_0', max_length=5)
    solnum_0 = models.CharField(db_column='SOLNUM_0', max_length=20)
    rep_0 = models.CharField(db_column='REP_0', max_length=5)
    sreori_0 = models.SmallIntegerField(db_column='SREORI_0')
    sreorivcr_0 = models.CharField(db_column='SREORIVCR_0', max_length=20)
    sreorivcrl_0 = models.IntegerField(db_column='SREORIVCRL_0')
    sretpl_0 = models.CharField(db_column='SRETPL_0', max_length=20)
    tsdcod_0 = models.CharField(db_column='TSDCOD_0', max_length=20)
    tsdcod_1 = models.CharField(db_column='TSDCOD_1', max_length=20)
    tsdcod_2 = models.CharField(db_column='TSDCOD_2', max_length=20)
    tsdcod_3 = models.CharField(db_column='TSDCOD_3', max_length=20)
    tsdcod_4 = models.CharField(db_column='TSDCOD_4', max_length=20)
    trscod_0 = models.CharField(db_column='TRSCOD_0', max_length=20)
    entcod_0 = models.CharField(db_column='ENTCOD_0', max_length=5)
    trsfam_0 = models.CharField(db_column='TRSFAM_0', max_length=20)
    nbrmanupd_0 = models.IntegerField(db_column='NBRMANUPD_0')
    creusr_0 = models.CharField(db_column='CREUSR_0', max_length=5)
    credat_0 = models.DateTimeField(db_column='CREDAT_0')
    crehou_0 = models.CharField(db_column='CREHOU_0', max_length=6)
    updusr_0 = models.CharField(db_column='UPDUSR_0', max_length=5)
    upddat_0 = models.DateTimeField(db_column='UPDDAT_0')
    credattim_0 = models.DateTimeField(db_column='CREDATTIM_0')
    upddattim_0 = models.DateTimeField(db_column='UPDDATTIM_0')
    auuid_0 = models.BinaryField(db_column='AUUID_0')
    rowid = models.BigAutoField(db_column='ROWID', primary_key=True)

    class Meta:
        managed = False
        db_table = 'SERREQUEST'
        unique_together = (
            ('credat_0', 'srenum_0'),
            ('sreresdat_0', 'srereshou_0', 'sreass_0', 'srenum_0'),
        )
