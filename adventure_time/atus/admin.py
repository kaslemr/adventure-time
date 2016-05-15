from django.contrib import admin

# Register your models here.

from atus.models import Respondent, HouseholdMember, ActivityResponse, ActivityTitle

admin.site.register(Respondent)
admin.site.register(HouseholdMember)
admin.site.register(ActivityResponse)
admin.site.register(ActivityTitle)