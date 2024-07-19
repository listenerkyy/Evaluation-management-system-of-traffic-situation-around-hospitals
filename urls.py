from django.urls import path
from . import views
from myapp import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('user/search', views.get_all_users, name='get_all_users'),
    path('hospital/search', views.get_hospitals, name='get_hospitals'),
    path('hospital/add', views.add_hospital, name='add_hospital'),
    path('hospital/alter', views.alter_hospital, name='alter_hospital'),
    path('hospital/delete/<int:yid>/', views.delete_hospital, name='delete_hospital'),
    path('GovernanceReport/search', views.get_governance_reports, name='get_governance_reports'),
    path('GovernanceReport/add', views.add_governance_report, name='add_governance_report'),
    path('GovernanceReport/alter', views.alter_governance_report, name='alter_governance_report'),
    path('GovernanceReport/delete/<int:gid>/', views.delete_governance_report, name='delete_governance_report'),
    path('SurveyReport/search', views.get_survey_reports, name='get_survey_reports'),
    path('SurveyReport/add', views.add_survey_report, name='add_survey_report'),
    path('SurveyReport/alter', views.alter_survey_report, name='alter_survey_report'),
]
