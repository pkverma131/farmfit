from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Crop
from .serializers import CropSerializer


@csrf_exempt
def crop_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        crop = Crop.objects.all()
        serializer = CropSerializer(crop, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CropSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)