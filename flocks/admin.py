from django.contrib import admin
from .models import *

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

class CountryAdmin(ImportExportModelAdmin):
    list_display = ['name']


class FlockAdmin(ImportExportModelAdmin):
    # a list of displayed columns name.
    list_display = ['name', 'house', 'id', 'breed', 'stage', 'date_hatched', 'date_in', 'date_out', 'birds_placed',
                    'status']
    search_fields = ['name', 'house', 'id', 'breed', 'stage', 'date_hatched', 'date_in', 'date_out', 'birds_placed',
                     'status']
    list_filter = ['name', 'house', 'breed', 'stage', 'date_hatched', 'date_out', 'status']


class HouseAdmin(ImportExportModelAdmin):
    # a list of displayed columns name.
    list_display = ['name', 'id', 'site']
    search_fields = ['name', 'site']
    list_filter = ['name', 'site']
    

class BreedAdmin(ImportExportModelAdmin):
    list_display = ['breed_name', 'target']
    search_fields = ['breed_name', 'target']
    list_filter = ['breed_name', 'target']


class BreedTypeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']


class FarmAdmin(ImportExportModelAdmin):
    list_display = ['name', 'owner', 'id', 'address', 'country', 'farm_attendant']
    search_fields = ['owner', 'name', 'address', 'country']
    list_filter = ['owner', 'name', 'address', 'country']


class SiteAdmin(ImportExportModelAdmin):
    list_display = ['name', 'id', 'farm']
    search_fields = ['name', 'id', 'farm']
    list_filter = ['name', 'id', 'farm']

class OwnerAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    list_filter = ['id', 'name']

class RecordAdmin(ImportExportModelAdmin):
    # a list of displayed columns name.
    list_display = ['flock', 'date', 'deaths_mortality', 'deaths_culls', 'body_weight', 'body_uniformity', 'feed_consumed', 'feed_delivered', 'feed_formula', 'water_consumed',  'temperature_inside', 'eggs_broken', 'eggs_sold', 'eggs_produced', 'notes']
    search_fields = ['flock', 'date', 'deaths_mortality', 'deaths_culls', 'body_weight', 'body_uniformity', 'feed_consumed', 'feed_delivered', 'feed_formula', 'water_consumed',  'temperature_inside', 'eggs_broken', 'eggs_sold', 'eggs_produced', 'notes']
    list_filter = ['flock', 'notes']

class TargetAdmin(ImportExportModelAdmin):
    # a list of displayed columns name.
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

class TargetDetailsAdmin(ImportExportModelAdmin):
    # a list of displayed columns name.
    list_display = ['name', 'target', 'body_weight', 'body_uniform', 'feed_rate', 'feed_formula', 'water_rate', 'lay_rate','liveability', 'death_mortality', 'egg_weight', 'age_week', 'age_daily']
    search_fields = ['name', 'target', 'body_weight', 'body_uniform', 'feed_rate', 'feed_formula', 'water_rate', 'lay_rate','liveability', 'death_mortality', 'egg_weight', 'age_week', 'age_daily']
    list_filter = ['name', 'target', 'body_weight', 'body_uniform', 'feed_rate', 'feed_formula', 'water_rate', 'lay_rate','liveability', 'death_mortality', 'egg_weight', 'age_week', 'age_daily']

class VaccinationAdmin(ImportExportModelAdmin):
    # a list of displayed columns name.
    list_display = ['flock', 'vaccine', 'date', 'date_expiration']
    search_fields = ['flock', 'vaccine', 'date', 'date_expiration']
    list_filter = ['flock', 'vaccine', 'date', 'date_expiration']

class VaccineAdmin(ImportExportModelAdmin):
    # a list of displayed columns name.
    list_display = ['name', 'description', 'method']
    search_fields = ['name', 'description', 'method']
    list_filter = ['name', 'description', 'method']


class FeedFormulaAdmin(ImportExportModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class FarmAttendentAdmin(admin.ModelAdmin):
    list_display = ['name', ]

class AdjustmentAdmin(admin.ModelAdmin):
    list_display = ['date', 'flock', 'quantity', 'adjustment', 'notes']
    list_filter = ['date', 'flock', 'adjustment', 'notes']



admin.site.register(Adjustment, AdjustmentAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(FarmAttendent, FarmAttendentAdmin)
admin.site.register(Flock, FlockAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Farm, FarmAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(FeedFormula, FeedFormulaAdmin)
admin.site.register(BreedType, BreedTypeAdmin)
admin.site.register(Breed, BreedAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Target, TargetAdmin)
admin.site.register(TargetDetails, TargetDetailsAdmin)
admin.site.register(Vaccination, VaccinationAdmin)
admin.site.register(Vaccine, VaccineAdmin)

# Register your models here.
