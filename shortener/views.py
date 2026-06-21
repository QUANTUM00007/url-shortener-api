from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import ShortURL
from .serializers import ShortURLSerializer 

class CreateShortURL(APIView):

    def post(self, request):

        serializer = ShortURLSerializer(data=request.data)
        if serializer.is_valid():
            
            url = serializer.save()

            return Response(
                {
                    "message": "URL shortened successfully",
                    "short_code": url.short_code,
                    "short_url": f"http://localhost:8000/{url.short_code}"
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def redirect_url(request, code):
    try:
        url = ShortURL.objects.get(short_code=code)

        url.clicks += 1
        url.save()

        return redirect(url.original_url)
    
    except ShortURL.DoesNotExist:
        return HttpResponse(
            "URL not found",
            status=status.HTTP_404_NOT_FOUND
            )  


class AnalyticsView(APIView):

    def get(self, request, code):

        try:
            url = ShortURL.objects.get(short_code=code)

            return Response({
                "original_url": url.original_url,
                "short_code": url.short_code,
                "clicks": url.clicks,
                "created_at": url.created_at
            })
        
        except ShortURL.DoesNotExist:
            return Response(
                {"error": "URL not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        