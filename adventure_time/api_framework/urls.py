
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views
from api_framework.views import api_respondent_detail_view, api_respondent_list_view, hello, RespondentListView, \
    RespondentDetailView, ActivityTitleListView, ActivityTitleDetailView, HouseholdMemberListView, \
    HouseholdMemberDetailView

urlpatterns = [
    url(r'respondent/$', RespondentListView.as_view(), name="api_respondent_list_view"),
    url(r'respondent/(?P<respondent>\d+)/$', RespondentDetailView.as_view(), name="api_respondent_detail_view"),
    url(r'activity/$', ActivityTitleListView.as_view(), name="api_activitytitle_list_view"),
    url(r'activity/(?P<code>\w+)/$', ActivityTitleDetailView.as_view(), name="api_activitytitle_detail_view"),
    url(r'household/$', HouseholdMemberListView.as_view(), name="api_householdmember_list_view"),
    url(r'household/(?P<respondent>\d+)/$', HouseholdMemberDetailView.as_view(), name="api_householdmember_detail_view"),
    ]


