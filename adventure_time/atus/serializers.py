from rest_framework import serializers
from atus.models import HouseholdMember, Respondent, ActivityTitle, ActivityResponse

class RespondentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Respondent
