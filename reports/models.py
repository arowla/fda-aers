from django.db import models
from django.utils.translation import gettext as _

from model_utils import Choices

class Case(models.Model):
    number = models.IntegerField(max_length=125, primary_key=True)
    
    def __unicode__(self):
        return u"%s" % (self.number)

class Report(models.Model):
    isr = models.IntegerField("Individual Safety Report Number", max_length=10, primary_key=True)
    case = models.ForeignKey(Case, blank=True, null=True)
    
    def __unicode__(self):
        return u"%s" % (self.isr)
    
class Demographic(models.Model):
    
    # This is the data that comes from the Demographic and Administrative Information
    
    isr = models.ForeignKey(Report, primary_key=True)
    i_f_cod_choices = Choices(('I', 'initial', _('Initial')), ('F', 'followup', _('Followup')))
    i_f_cod = models.CharField("Report Status", max_length=1, choices=i_f_cod_choices, blank=True)
    foll_seq = models.CharField("Sequence Number", max_length=2, blank=True)
    image = models.CharField("Report Image Identifier", max_length=12, blank=True)
    event_dt = models.DateField("Event Date", blank=True, null=True)
    mft_dt = models.DateField("Manufacturer Received Date", blank=True, null=True)
    fda_dt = models.DateField("FDA Received Date", blank=True, null=True)
    rept_cod_choices = Choices(('EXP', 'expedited', _('Expedited (15-Day)')), ('PER', 'periodic', _('Periodic')), ('DIR', 'direct', _('Direct')))
    rept_cod = models.CharField("Report Type", max_length=125, choices=rept_cod_choices, blank=True)
    mfr_num = models.CharField("Manufacturer Report Identifier", max_length=125, blank=True)
    mfr_sndr = models.CharField("Manufacturer Sending Report Name", max_length=125, blank=True)
    age = models.FloatField("Age of Patient", max_length=125, blank=True, null=True)
    age_cod_choices = Choices(('DEC', 'decade', _('Decade')), ('YR', 'year', _('Year')), ('MON', 'month', _('Month')), ('WK', 'week', _('Week')), ('DY', 'day', _('Day')), ('HR', 'hour', _('Hour')))
    age_cod = models.CharField("Age Unit", max_length=125, choices=age_cod_choices, blank=True)
    gndr_cod_choices = Choices(('UNK', 'unknown', _('Unknown')), ('M', 'male', _('Male')), ('F', 'female', _('Female')), ('NS', 'not_specified', _('Not Specified')))
    gndr_cod = models.CharField("Patient Sex", max_length=125, choices=gndr_cod_choices, blank=True)
    e_sub = models.BooleanField("Report Submitted Under Elecronic Sumissions Procedure")
    wt = models.FloatField("Patient Weight", blank=True, null=True)
    wt_cod_choices = Choices(('KG', 'kilograms', _('Kilograms')), ('LBS', 'pounds', _('Pounds')), ('GMS', 'grams', _('Grams')))
    wt_cod = models.CharField("Patient Weight Unit", max_length=125, choices=wt_cod_choices, blank=True)
    rept_dt = models.DateField("Date Report Sent", blank=True, null=True)
    occp_cod_choices = Choices(('MD', 'physician', _('Physician')), ('PH', 'pharmacist', _('Pharmacist')), ('OT', 'other_health_professional', _('Other health-professional')), ('LW', 'lawyer', _('Lawyer')), ('CN', 'consumer', _('Consumer')))
    occp_cod = models.CharField("Reporter's Occupation", max_length=125, choices=occp_cod_choices, blank=True)
    death_dt = models.DateField("Patient Death Date", blank=True, null=True)
    to_mfr = models.NullBooleanField("Voluntary Reporter Notified Manufacturer", blank=True)
    confid = models.NullBooleanField("Voluntary Reporter stated identify should not be disclosed", blank=True)
    reporter_country = models.CharField("Reporter Country or Address", max_length=125, blank=True)
    
    def __unicode__(self):
        return u"%s" % (self.isr)
        
class Drug(models.Model):
    isr = models.ForeignKey(Report)
    drug_seq = models.IntegerField("Drug Sequence Number", max_length=125)
    role_cod_choices = Choices(('PS', 'primary_suspect_drug', _('Primary Suspect Drug')), ('SS', 'secondary_suspect_drug', _('Secondary Suspect Drug')), ('C', 'concomitant', _('Concomitant')), ('I', 'interacting', _('Interacting')))
    role_cod = models.CharField("Role Code", max_length=125, choices=role_cod_choices, blank=True)
    drugname = models.CharField('Drug Name', max_length=125, blank=True)
    val_vbm_choices = Choices(('1', 'validated_trade_name_used', _('Validated Trade Name Used')), ('2', 'verbatim_name_used', _('Verbatim Name Used')))
    val_vbm = models.CharField("Source of Drug Name", max_length=125, choices=val_vbm_choices, blank=True)
    route = models.CharField('Route of Drug Administration', max_length=125, blank=True, null=True)
    dose_vbm = models.TextField('Verbatim text for dose, frequency, and route, exactly as entered on report', blank=True)
    dechal_choices = Choices(('Y', 'positive_dechallenge', _('Positive dechallenge')), ('N', 'negative_dechallenge', _('Negative dechallenge')), ('U', 'unknown', _('Unknown')), ('D', 'does_not_apply', _('Does Not Apply')))
    dechal = models.CharField('Dechallenge code', max_length=125, choices=dechal_choices, blank=True)
    rechal_choices = Choices(('Y', 'positive_rechallenge', _('Positive rechallenge')), ('N', 'negative_rechallenge', _('Negative rechallenge')), ('U', 'unknown', _('Unknown')), ('D', 'does_not_apply', _('Does Not Apply')))
    rechal = models.CharField('Rechallenge code', max_length=125, choices=rechal_choices, blank=True)
    lot_num = models.CharField('Lot Number of the Drug', max_length=125, blank=True)
    exp_dt = models.DateField("Expiration date of the drug", blank=True, null=True)
    nda_num = models.CharField('Verbatim NDA Number', max_length=125, blank=True)
    
class Reaction(models.Model):
    isr = models.ForeignKey(Report)
    pt = models.CharField('Preferred Term medical terminology describing the event', max_length=125)
    
class Outcome(models.Model):
    isr = models.ForeignKey(Report)
    outcome_cod_choices = Choices(('DE', 'death', _('Death')), ('LT', 'life_threatening', _('Life-Threatening')), ('HO', 'hospitalization', _('Hospitalization - Initial or Prolonged')), ('DS', 'disability', _('Disability')), ('CA', 'cogenital_anomaly', _('Cogenital Anomaly')), ('RI', 'required_intervention', _('Required Intervention to Prevent Permanent Impairment/Damage')), ('OT', 'other', _('Other')))
    outc_cod = models.CharField('Patient Outcome', max_length=125, choices=outcome_cod_choices)
    
class Report_Source(models.Model):
    isr = models.ForeignKey(Report)
    rspr_cod_choices = Choices(('FGN', 'foreign', _('Foreign')), ('SDY', 'study', _('Study')), ('LIT', 'literature', _('Literature')), ('CSM', 'consumer', _('Consumer')), ('HP', 'health_professional', _('Health Professional')), ('UF', 'user_facility', _('User Facility')), ('CR', 'company_representative', _('Company Representative')), ('DT', 'distributor', _('Distributor')), ('OTH', 'other', _('Other')))
    rspr_cod = models.CharField('Initial Source of Report', max_length=125, choices=rspr_cod_choices)
    
class Therapy(models.Model):
    isr = models.ForeignKey(Report)
    drug_seq = models.IntegerField("Drug Sequence Number", max_length=125)
    start_dt = models.DateField("Date therapy was started (or re-started) for this drug", blank=True, null=True)
    end_dt = models.DateField("Date therapy was stopped for this drug", null=True, blank=True)
    dur = models.FloatField("Numeric value for the duration (length) of therapy", blank=True, null=True)
    dur_cod_choices = Choices(('YR', 'years', _('Years')), ('MON', 'months', _('Months')), ('WK', 'weeks', _('Weeks')), ('DAY', 'days', _('Days')), ('HR', 'hours', _('Hours')), ('MIN', 'minutes', _('Minutes')),  ('SEC', 'seconds', _('Seconds')))
    dur_cod = models.CharField('Unit abbreviation for duration of therapy', max_length=125, choices=dur_cod_choices, blank=True)
    
class Indications(models.Model):
    isr = models.ForeignKey(Report)
    drug_seq = models.IntegerField("Drug Sequence Number", max_length=125)
    indi_pt = models.CharField("Preferred term medical terminology describing the Indication for use", max_length=300)
    
    