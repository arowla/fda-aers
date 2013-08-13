from celery import task
from django.db.transaction import commit_on_success


import unicodecsv
import datetime

from reports.models import Case, Report, Demographic, Drug, Reaction, Outcome, Report_Source, Therapy, Indications

def datetime_validator(value):
    if value:
        try:
            return datetime.datetime.strptime(value, '%Y%m%d')
        except:
            return None
            
def boolean_validator(value):
    if value == "Y":
        return True
    if value == "N":
        return False
    else:
        return None

def float_validator(value):
    try:
        value = float(value)
        return value
    except:
        return None           
            
def integer_validator(value):
    try:
        value = int(value)
        return value
    except:
        return None
        
def isr_validator(value):
    try:
        value = int(value)
        return value
    except:
        pass

def string_validator(value):
    try:
        value = str(value)
        return value
    except:
        return None

def import_demographics():
    with open('/home/sean/aers/importer/csv/DEMO12Q3.TXT', 'rb') as file:
        demo = unicodecsv.reader(file, delimiter='$')
        firstline = True
        x = 0
        print 'Starting Demographics'
        for row in demo:
            if firstline:
                firstline = False
                x = x+1
                print x
                continue
            else:
                try:
                    demographic = Demographic()
                    isr = isr_validator(row[0])
                    case_number = integer_validator(row[1])
                    case = Case.objects.get_or_create(number=case_number)[0]
                    report = Report.objects.get_or_create(isr=isr, case=case)[0]
                    demographic.isr = report
                    demographic.i_f_cod = string_validator(row[2])
                    demographic.image = string_validator(row[4])
                    demographic.event_dt = datetime_validator(row[5])
                    demographic.mfr_dt = datetime_validator(row[6])
                    demographic.fda_dt = datetime_validator(row[7])
                    demographic.rept_cod = string_validator(row[8])
                    demographic.mfr_num = string_validator(row[9])
                    demographic.mfr_sndr = string_validator(row[10])
                    demographic.age = float_validator(row[11])
                    demographic.age_cod = string_validator(row[12])
                    demographic.gndr_cod = string_validator(row[13])
                    demographic.e_sub = boolean_validator(row[14])
                    demographic.wt = float_validator(row[15])
                    demographic.wt_cod = string_validator(row[16])
                    demographic.rept_dt = datetime_validator(row[17])
                    demographic.occp_cod = string_validator(row[18])
                    demographic.death_dt = datetime_validator(row[19])
                    demographic.to_mfr = boolean_validator(row[20])
                    demographic.confid = boolean_validator(row[21])
                    demographic.reporter_country = string_validator(row[22])
                    demographic.save()
                    x = x+1
                except:
                    print 'Demographic Error Line %s' % (x)
                    x = x+1
                    continue

def import_drugs():
    with open('/home/sean/aers/importer/csv/DRUG12Q3.TXT', 'rb') as file:
        drug = unicodecsv.reader(file, delimiter='$')
        firstline = True
        x = 0
        print 'Starting Drugs'
        for row in drug:
            if firstline:
                firstline = False
                x = x+1
                continue
            else:
                try:
                    drug = Drug()
                    isr = isr_validator(row[0])
                    report = Report.objects.get(isr=isr)
                    drug.isr = report
                    try:
                        drug.drug_seq = integer_validator(row[1])
                    except:
                        pass
                    try:
                        drug.role_cod = string_validator(row[2])
                    except:
                        pass
                    try:
                        drug.drugname = string_validator(row[3])
                    except:
                        pass
                    try:
                        drug.val_vbm  = string_validator(row[4])
                    except:
                        pass
                    try:
                        drug.route    = string_validator(row[5])
                    except:
                        pass
                    try:
                        drug.dose_vbm = string_validator(row[6])
                    except:
                        pass
                    try:
                        drug.dechal   = string_validator(row[7])
                    except:
                        pass
                    try:
                        drug.rechal   = string_validator(row[8])
                    except:
                        pass
                    try:
                        drug.lot_num  = string_validator(row[9])
                    except:
                        pass
                    try:
                        drug.exp_dt   = datetime_validator(row[10])
                    except:
                        pass
                    try:
                        drug.nda_num  = string_validator(row[11])
                    except:
                        pass
                    drug.save()
                    x = x+1
                except:
                    print 'Drug Error Line %s' % (x)
                    x = x+1
                    continue
                        
                
def import_reactions():
    with open('/home/sean/aers/importer/csv/REAC12Q3.TXT', 'rb') as file:
        reaction = unicodecsv.reader(file, delimiter='$')
        firstline = True
        x = 0
        print 'Starting Reactions'
        for row in reaction:
            if firstline:
                firstline = False
                x = x+1
                continue
            else:
                try:
                    reaction = Reaction()
                    isr = isr_validator(row[0])
                    report = Report.objects.get(isr=isr)
                    reaction.isr = report
                    try:
                        reaction.pt = string_validator(row[1])
                    except:
                        pass
                    reaction.save() 
                    x = x+1
                except:
                    print 'Reactions Error Line %s' % (x)
                    x = x+1
                    continue
                
def import_outcomes():
    with open('/home/sean/aers/importer/csv/OUTC12Q3.TXT', 'rb') as file:
        outcome = unicodecsv.reader(file, delimiter='$')
        firstline = True
        x = 0
        print 'Starting Outcomes'
        for row in outcome:
            if firstline:
                firstline = False
                x = x+1
                continue
            else:
                try:
                    outcome = Outcome()
                    isr = isr_validator(row[0])
                    report = Report.objects.get_or_create(isr=isr)[0]
                    outcome.isr = report
                    try:
                        outcome.outc_cod = string_validator(row[1])
                    except:
                        pass
                    outcome.save()
                    x=x+1
                except:
                    print 'Outcomes Error Line %s' % (x)
                    x = x+1
                    continue
                
def import_report_sources():
    with open('/home/sean/aers/importer/csv/RPSR12Q3.TXT', 'rb') as file:
        report_source = unicodecsv.reader(file, delimiter='$')
        firstline = True
        x = 0
        print 'Starting Report Sources'
        for row in report_source:
            if firstline:
                firstline = False
                x = x+1
                continue
            else:
                try:
                    report_source = Report_source()
                    isr = isr_validator(row[0])
                    report = Report.objects.get(isr=isr)
                    report_source.isr = report
                    try:
                        report_source.rspr_cod = string_validator(row[1])
                    except:
                        pass
                    report_source.save()
                    x = x+1
                except:
                    print 'Report Sources Error Line %s' % (x)
                    x = x+1
                    continue

@task                
def import_therapies():
    with open('/home/sean/aers/importer/csv/THER12Q3.TXT', 'rb') as file:
        therapy = unicodecsv.reader(file, delimiter='$')
        firstline = True
        x = 0
        print 'Starting Therapies'
        for row in therapy:
            if firstline:
                firstline = False
                x = x+1
                continue
            else:
                try:
                    therapy = Therapy()
                    isr = isr_validator(row[0])
                    report = Report.objects.get(isr=isr)
                    therapy.isr = report
                    therapy.drug_seq = integer_validator(row[1])
                    therapy.start_dt = datetime_validator(row[2])
                    therapy.end_dt  = datetime_validator(row[3])
                    therapy.dur = float_validator(row[4])
                    therapy.dur_cod = string_validator(row[5])
                    therapy.save()
                except:
                    print 'Therapies Error Line %s' % (x)
                    x = x+11
                    x = x+1
                    continue
                
def import_indications():
    with open('/home/sean/aers/importer/csv/INDI12Q3.TXT', 'rb') as file:
        indication = unicodecsv.reader(file, delimiter='$')
        firstline = True
        x = 0
        print 'Starting Indications'
        for row in indication:
            if firstline:
                firstline = False
                x = x+1
                continue
            else:
                try:
                    indication = Indications()
                    isr = isr_validator(row[0])
                    report = Report.objects.get(isr=isr)
                    indication.isr = report
                    try:
                        indication.drug_seq = integer_validator(row[1])
                    except:
                        pass
                    try:
                        indication.indi_pt = string_validator(row[3])
                    except:
                        pass
                    indication.save()
                    x=x+1
                except:
                    print 'Indications Error Line %s' % (x)
                    x = x+1
                    continue
                

        

@task
@commit_on_success
def importer():
    import_demographics()
    import_drugs()
    import_reactions()
    import_outcomes()
    import_report_sources()
    import_therapies()
    import_indications()
    