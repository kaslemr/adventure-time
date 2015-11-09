from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from atus.models import Respondent, ActivityResponse, ActivityTitle, HouseholdMember
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.serializers import ModelSerializer


def hello(request):
    all_respondents = Respondent.objects.all()
    serialized_data = serializers.serialize("json", all_respondents)
    return HttpResponse(serialized_data, content_type="application/json")

@csrf_exempt
def api_respondent_list_view(request):
    qs = Respondent.objects.all()
    return HttpResponse(serializers.serialize("json", qs), content_type="application/json")

@csrf_exempt
def api_respondent_detail_view(request, model_pk):
    qs = Respondent.objects.filter(id=model_pk)
    return HttpResponse(serializers.serialize("json", qs), content_type="application/json")

@csrf_exempt
def api_activitytitle_list_view(request):
    qs = ActivityTitle.objects.all()
    return HttpResponse(serializers.serialize("json", qs), content_type="application/json")

@csrf_exempt
def api_householdmember_list_view(request):
    qs = HouseholdMember.objects.all()
    return HttpResponse(serializers.serialize("json", qs), content_type="application/json")


@csrf_exempt
def api_householdmember_detail_view(request, model_pk):
    qs = HouseholdMember.objects.filter(id=model_pk)
    return HttpResponse(serializers.serialize("json", qs), content_type="application/json")



class RespondentSerializer(ModelSerializer):

    class Meta:
        model = Respondent
        lookup_field = 'respondent'


class RespondentListView(ListAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer


class RespondentDetailView(RetrieveAPIView):
    queryset = Respondent.objects.filter()
    serializer_class = RespondentSerializer
    lookup_field = 'respondent'


class ActivityResponseSerializer(ModelSerializer):

    class Meta:
        model = ActivityResponse


class ActivityTitleSerializer(ModelSerializer):

    class Meta:
        model = ActivityTitle
        lookup_field = 'code'


class ActivityResponseListView(ListAPIView):
    queryset = ActivityResponse.objects.all()
    serializer_class = ActivityResponseSerializer



class ActivityResponseDetailView(RetrieveAPIView):
    queryset = ActivityResponse.objects.all()
    serializer_class = ActivityResponseSerializer



class ActivityTitleListView(ListAPIView):
    queryset = ActivityTitle.objects.all()
    serializer_class = ActivityTitleSerializer



class ActivityTitleDetailView(RetrieveAPIView):
    queryset = ActivityTitle.objects.all()
    serializer_class = ActivityTitleSerializer
    lookup_field = 'code'


class HouseholdMemberSerializer(ModelSerializer):

    class Meta:
        model = HouseholdMember
        lookup_field = 'respondent'



class HouseholdMemberListView(ListAPIView):
    serializer_class = HouseholdMemberSerializer
    queryset = HouseholdMember.objects.all()



class HouseholdMemberDetailView(RetrieveAPIView):
    serializer_class = HouseholdMemberSerializer
    queryset = HouseholdMember.objects.all()
    lookup_field = 'respondent'

    #def get_queryset(self):
        #respondent = self.kwargs['respondent']
        #return HouseholdMember.objects.filter(respondent=respondent)





