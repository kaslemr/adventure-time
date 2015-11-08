from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from atus.models import Respondent, ActivityResponse
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
    return HttpResponse(serializers.serialize("json", qs) content_type="application/json"))


class RespondentSerializer(ModelSerializer):

    class Meta:
        model = Respondent


class RespondentListView(ListAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer


class RespondentDetailView(RetrieveAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer


class ActivityResponseSerializer(ModelSerializer):

    class Meta:
        model = ActivityResponse


class ActivityResponseListView(ListAPIView):
    queryset = ActivityResponse.objects.all()
    serializer_class = ActivityResponseSerializer


class ActivityResponseDetailView(RetrieveAPIView):
    queryset = ActivityResponse.objects.all()
    serializer_class = ActivityResponseSerializer
