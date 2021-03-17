from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets 
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework.exceptions import ValidationError, ParseError

from .serializer import UserSerializer, RegisterSerializer,BookingSerializer

from admins.models import Advisor
from admins.serializer import AdvisorSerializer
from .models import Booking





# Register API
class register(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class signin(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(signin, self).post(request, format=None)

@api_view(['GET'])
def listAdvisor(request,userId):
    advisor = Advisor.objects.all()
    serializer = AdvisorSerializer(advisor,many=True)

    return Response(serializer.data)




@api_view(['POST'])
def bookAdvisor(request,userid,advid):
    try:
        user = User.objects.all().filter(id = userid)[0]
        adv = Advisor.objects.all().filter(id = advid)[0]
        booking = Booking(username = user.username,userid = userid,advisorname = adv.advisor_name,advisorid=advid)
        booking.save()

        # searializer = BookingSerializer(data=request.data)
        # searializer.is_valid(raise_exception=True)
        # searializer.save()
        data = {}
        data['username'] = user.username
        data['userid'] = userid
        data['advisorname'] = adv.advisor_name
        data['advisorid'] = advid
        data['time'] = booking.time
    except:
        raise ParseError
    return Response(data)


@api_view(['GET'])
def booking(request,userid):
    data = Booking.objects.all().filter(userid = userid)
    serializer = BookingSerializer(data,many = True)
    

    return Response(serializer.data)



