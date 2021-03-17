from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Advisor

from .serializer import AdvisorSerializer

@api_view(['POST'])
def createAdvisor(request):
    serializer = AdvisorSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    
    return Response(serializer.data)


