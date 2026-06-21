from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
    