from . import views
from django.conf.urls import url

urlpatterns = [ url(r'^$', views.index, name='index'),

                url(r'^past/30days/4.5$', views.past_thirty_day_four_plus),
                url(r'^past/30days/2.5$', views.past_day_two_plus),


                url(r'^past/7days/4.5$', views.past_thirty_day_four_plus),
                url(r'^past/7days/2.5$', views.past_day_two_plus),

                url(r'^past/1days/4.5$', views.past_thirty_day_four_plus),
                url(r'^past/1days/2.5$', views.past_day_two_plus),

                url(r'^past/1hr/4.5$', views.past_thirty_day_four_plus),
                url(r'^past/1hr/2.5$', views.past_day_two_plus),

                ]
