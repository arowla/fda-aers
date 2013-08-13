# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Case'
        db.create_table(u'reports_case', (
            ('number', self.gf('django.db.models.fields.IntegerField')(max_length=125, primary_key=True)),
        ))
        db.send_create_signal(u'reports', ['Case'])

        # Adding model 'Report'
        db.create_table(u'reports_report', (
            ('isr', self.gf('django.db.models.fields.IntegerField')(max_length=10, primary_key=True)),
            ('case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Case'], null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['Report'])

        # Adding model 'Demographic'
        db.create_table(u'reports_demographic', (
            ('isr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Report'], primary_key=True)),
            ('i_f_cod', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('foll_seq', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('event_dt', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('mft_dt', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fda_dt', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('rept_cod', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('mfr_num', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('mfr_sndr', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('age', self.gf('django.db.models.fields.FloatField')(max_length=125, null=True, blank=True)),
            ('age_cod', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('gndr_cod', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('e_sub', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wt', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('wt_cod', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('rept_dt', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('occp_cod', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('death_dt', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('to_mfr', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('confid', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('reporter_country', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
        ))
        db.send_create_signal(u'reports', ['Demographic'])

        # Adding model 'Drug'
        db.create_table(u'reports_drug', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Report'])),
            ('drug_seq', self.gf('django.db.models.fields.IntegerField')(max_length=125)),
            ('role_cod', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('drugname', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('val_vbm', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('route', self.gf('django.db.models.fields.CharField')(max_length=125, null=True, blank=True)),
            ('dose_vbm', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('dechal', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('rechal', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('lot_num', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('exp_dt', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('nda_num', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
        ))
        db.send_create_signal(u'reports', ['Drug'])

        # Adding model 'Reaction'
        db.create_table(u'reports_reaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Report'])),
            ('pt', self.gf('django.db.models.fields.CharField')(max_length=125)),
        ))
        db.send_create_signal(u'reports', ['Reaction'])

        # Adding model 'Outcome'
        db.create_table(u'reports_outcome', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Report'])),
            ('outc_cod', self.gf('django.db.models.fields.CharField')(max_length=125)),
        ))
        db.send_create_signal(u'reports', ['Outcome'])

        # Adding model 'Report_Source'
        db.create_table(u'reports_report_source', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Report'])),
            ('rspr_cod', self.gf('django.db.models.fields.CharField')(max_length=125)),
        ))
        db.send_create_signal(u'reports', ['Report_Source'])

        # Adding model 'Therapy'
        db.create_table(u'reports_therapy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Report'])),
            ('drug_seq', self.gf('django.db.models.fields.IntegerField')(max_length=125)),
            ('start_dt', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_dt', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('dur', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dur_cod', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
        ))
        db.send_create_signal(u'reports', ['Therapy'])

        # Adding model 'Indications'
        db.create_table(u'reports_indications', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Report'])),
            ('drug_seq', self.gf('django.db.models.fields.IntegerField')(max_length=125)),
            ('indi_pt', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'reports', ['Indications'])


    def backwards(self, orm):
        # Deleting model 'Case'
        db.delete_table(u'reports_case')

        # Deleting model 'Report'
        db.delete_table(u'reports_report')

        # Deleting model 'Demographic'
        db.delete_table(u'reports_demographic')

        # Deleting model 'Drug'
        db.delete_table(u'reports_drug')

        # Deleting model 'Reaction'
        db.delete_table(u'reports_reaction')

        # Deleting model 'Outcome'
        db.delete_table(u'reports_outcome')

        # Deleting model 'Report_Source'
        db.delete_table(u'reports_report_source')

        # Deleting model 'Therapy'
        db.delete_table(u'reports_therapy')

        # Deleting model 'Indications'
        db.delete_table(u'reports_indications')


    models = {
        u'reports.case': {
            'Meta': {'object_name': 'Case'},
            'number': ('django.db.models.fields.IntegerField', [], {'max_length': '125', 'primary_key': 'True'})
        },
        u'reports.demographic': {
            'Meta': {'object_name': 'Demographic'},
            'age': ('django.db.models.fields.FloatField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'age_cod': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'confid': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'death_dt': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'e_sub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'event_dt': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fda_dt': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'foll_seq': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'gndr_cod': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'i_f_cod': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'isr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Report']", 'primary_key': 'True'}),
            'mfr_num': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'mfr_sndr': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'mft_dt': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'occp_cod': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'reporter_country': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'rept_cod': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'rept_dt': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'to_mfr': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'wt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'wt_cod': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'})
        },
        u'reports.drug': {
            'Meta': {'object_name': 'Drug'},
            'dechal': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'dose_vbm': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'drug_seq': ('django.db.models.fields.IntegerField', [], {'max_length': '125'}),
            'drugname': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'exp_dt': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Report']"}),
            'lot_num': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'nda_num': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'rechal': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'role_cod': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'route': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'val_vbm': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'})
        },
        u'reports.indications': {
            'Meta': {'object_name': 'Indications'},
            'drug_seq': ('django.db.models.fields.IntegerField', [], {'max_length': '125'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indi_pt': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'isr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Report']"})
        },
        u'reports.outcome': {
            'Meta': {'object_name': 'Outcome'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Report']"}),
            'outc_cod': ('django.db.models.fields.CharField', [], {'max_length': '125'})
        },
        u'reports.reaction': {
            'Meta': {'object_name': 'Reaction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Report']"}),
            'pt': ('django.db.models.fields.CharField', [], {'max_length': '125'})
        },
        u'reports.report': {
            'Meta': {'object_name': 'Report'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Case']", 'null': 'True', 'blank': 'True'}),
            'isr': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'primary_key': 'True'})
        },
        u'reports.report_source': {
            'Meta': {'object_name': 'Report_Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Report']"}),
            'rspr_cod': ('django.db.models.fields.CharField', [], {'max_length': '125'})
        },
        u'reports.therapy': {
            'Meta': {'object_name': 'Therapy'},
            'drug_seq': ('django.db.models.fields.IntegerField', [], {'max_length': '125'}),
            'dur': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dur_cod': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'end_dt': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Report']"}),
            'start_dt': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['reports']