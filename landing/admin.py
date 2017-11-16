from django.contrib import admin
from .models import *
# Register your models here.


class SubscriberAdmin(admin.ModelAdmin):
# list_display = ["name", "email"]
# the same

    list_display = [field.name for field in Subscriber._meta.fields if field.name != "id"]
    list_filter = ["name", "email"]
    search_fields = ["name", "email"]
    exclude = [""]

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
