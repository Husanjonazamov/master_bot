from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.template.defaultfilters import safe
from import_export.admin import ExportMixin, ImportExportActionModelAdmin, ImportExportModelAdmin

from apps.api.models import Delivered, Veterinarian,Placing, Registration
from apps.api.resource import VeterinarianResource, DeliveredResource


# Register your models here.
class DeliveredAdmin(ImportExportModelAdmin):
    list_display = ["user", 'first_name', 'phone', 'custom_location', "product_count", "custom_addition"]
    search_fields = ["user", 'first_name', 'phone', 'location', "product_count", "addition"]
    resource_class = DeliveredResource

    def custom_addition(self, obj):
        return safe("<a href='/media/{}' target='_blank'>Ochish</a>".format(obj.addition))

    def custom_location(self, obj):
        return safe("<a href='http://maps.google.com/?ll={},{}' target='_blank'>google</a>".format(obj.location.lat,
                                                                                                   obj.location.lon))

    custom_location.allow_tags = True
    custom_location.short_description = "Joylashuv"

    custom_addition.allow_tags = True
    custom_addition.short_description = "Xulosa file"

class PlacingAdmin(ImportExportModelAdmin):
    list_display = ["name","phone","day","product_count","location"]
    search_fields = ["name","phone","day","product_count","location"]

    def custom_location(self, obj):
        return safe("<a href='http://maps.google.com/?ll={},{}' target='_blank'>google</a>".format(obj.location.lat,
                                                                                                   obj.location.lon))

    custom_location.allow_tags = True
    custom_location.short_description = "Joylashuv"


class RegistrationAdmin(ImportExportModelAdmin):
    list_display = ["name","phone"]
    search_fields = ["name", "phone"]

class VeterinarianAdmin(ImportExportModelAdmin):
    list_display = ["user", 'first_name', 'custom_location', "custom_addition"]
    search_fields = ["first_name", "user__first_name", "user__username"]
    list_filter = ['user__username', "user__first_name"]
    resource_class = VeterinarianResource

    def custom_addition(self, obj):
        return safe("<a href='/media/{}' target='_blank'>Ochish</a>".format(obj.addition))

    def custom_location(self, obj):
        return safe("<a href='http://maps.google.com/?ll={},{}' target='_blank'>google</a>".format(obj.location.lat,
                                                                                                   obj.location.lon))

    custom_location.allow_tags = True
    custom_location.short_description = "Joylashuv"

    custom_addition.allow_tags = True
    custom_addition.short_description = "Xulosa file"


admin.site.register(Delivered, DeliveredAdmin)
admin.site.register(Placing, PlacingAdmin)
admin.site.register(Veterinarian, VeterinarianAdmin)
admin.site.register(Registration, RegistrationAdmin)
