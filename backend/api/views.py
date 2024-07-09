from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, VideoUrlSerializer, PlaylistUrlSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .main.RunPlaylistUrl import process_analysis_request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

    
class ProcessPlaylistURL(APIView):
    serializer_class = PlaylistUrlSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        print("At least came inside post")
        if serializer.is_valid():
            print(serializer.data.get('playlisturl'))
            positive , negative = process_analysis_request(serializer.data.get('playlisturl'), "playlist")
            chart_data = {
                "positive" : positive,
                "negative" : negative
            }
            print("back inside the views..")
            print(positive + negative)
            return Response(data=chart_data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ProcessVideoURL(APIView):
    serializer_class = VideoUrlSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            positive , negative = process_analysis_request(serializer.data.get('videourl'), "video")
            chart_data = {
                "positive" : positive,
                "negative" : negative
            }
            print("back inside the views..")
            print(positive + negative)
            return Response(data=chart_data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
