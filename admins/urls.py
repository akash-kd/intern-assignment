from django.urls import path,include
from .views import createAdvisor


''' ADMINS '''
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('advisor/',createAdvisor,name = 'admin-advisor'),
]