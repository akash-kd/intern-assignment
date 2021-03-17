from django.urls import path,include
from .views import *
''' USERS '''

urlpatterns = [
    # # path('admin/', admin.site.urls),
    path('login/',signin.as_view(),name='login'),
    path('register/',register.as_view(),name='create-user'),
    path('<int:userId>/advisor',listAdvisor,name='list-advisor'),
    path('<int:userid>/advisor/<int:advid>/',bookAdvisor,name='book-advisor'),
    path('<int:userid>/advisor/booking/',booking,name='booking'),
    # path('/user/<int:userId>/advisor',),
    # path('/user/<int:userId>/advisor/<int:advisorId>/',),
]