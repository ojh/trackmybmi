from django.conf.urls import include, patterns, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from measurements.views import MeasurementViewSet


router = DefaultRouter()
router.register(r'measurements', MeasurementViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trackmybmi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
)
