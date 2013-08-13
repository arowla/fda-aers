from .models import *
from django.contrib import admin

class DemographicInline(admin.TabularInline):
    model = Demographic
    
class DrugInline(admin.TabularInline):
    model = Drug

class ReactionInline(admin.TabularInline):
    model = Reaction

class OutcomeInline(admin.TabularInline):
    model = Outcome

class Report_SourceInline(admin.TabularInline):
    model = Report_Source
    
class TherapyInline(admin.TabularInline):
    model = Therapy
    
class IndicationsInline(admin.TabularInline):
    model = Indications

    
class ReportAdmin(admin.ModelAdmin):
    inlines = [
        DemographicInline,
        DrugInline,
        ReactionInline,
        OutcomeInline,
        Report_SourceInline,
        TherapyInline,
        IndicationsInline,
    ]

    
admin.site.register(Report, ReportAdmin)