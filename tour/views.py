import os
import requests

from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import APIException

from .serializers import TourAddSerializer, TourProgramSerializer, PriceSerializer, TipsSerializer, PhotoSerializer
from .models import TourAdd, TourProgram, Price, Tips, Photo


class TourAddViewSet(viewsets.ModelViewSet):
    queryset = TourAdd.objects.all()
    serializer_class = TourAddSerializer
    permission_classes = [IsAdminUser]

    def create(self, request):
        serializer = TourAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            responce_201 = {
                "message": "Tour added successfully",
            }
            return Response(responce_201, status=status.HTTP_201_CREATED)
        response_400 = {
            "message": "Tour not added",
        }
        return Response(response_400, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            tour = TourAdd.objects.get(pk=pk)
            serializer = TourAddSerializer(tour, data=request.data)
            if serializer.is_valid():
                serializer.save()
                responce_200 = {
                    "message": "Tour updated successfully",
                }
                return Response(responce_200, status=status.HTTP_200_OK)
            response_400 = {
                "message": "Tour not updated",
            }
            return Response(response_400, status=status.HTTP_400_BAD_REQUEST)
        except TourAdd.DoesNotExist:
            responce_404 = {
                "message": "Tour not found",
            }
            return Response(responce_404, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            tour = TourAdd.objects.get(pk=pk)
            tour.delete()
            responce_204 = {
                "message": "Tour deleted successfully",
            }
            return Response(responce_204, status=status.HTTP_204_NO_CONTENT)
        except TourAdd.DoesNotExist:
            responce_404 = {
                "message": "Tour not found",
            }
            return Response(responce_404, status=status.HTTP_404_NOT_FOUND)


class TourProgramViewSet(viewsets.ModelViewSet):
    queryset = TourProgram.objects.all()
    serializer_class = TourProgramSerializer
    permission_classes = [IsAdminUser]

    def create(self, request):
        serializer = TourProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            responce_201 = {
                "message": "Program added successfully",
            }
            return Response(responce_201, status=status.HTTP_201_CREATED)
        response_400 = {
            "message": "Program not added",
        }
        return Response(response_400, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            program = TourProgram.objects.get(pk=pk)
            serializer = TourProgramSerializer(program, data=request.data)
            if serializer.is_valid():
                serializer.save()
                responce_200 = {
                    "message": "Program updated successfully",
                }
                return Response(responce_200, status=status.HTTP_200_OK)
            response_400 = {
                "message": "Program not updated",
            }
            return Response(response_400, status=status.HTTP_400_BAD_REQUEST)
        except TourProgram.DoesNotExist:
            responce_404 = {
                "message": "Program not found",
            }
            return Response(responce_404, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            program = TourProgram.objects.get(pk=pk)
            program.delete()
            responce_204 = {
                "message": "Program deleted successfully",
            }
            return Response(responce_204, status=status.HTTP_204_NO_CONTENT)
        except TourProgram.DoesNotExist:
            responce_404 = {
                "message": "Program not found",
            }
            return Response(responce_404, status=status.HTTP_404_NOT_FOUND)


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = [IsAdminUser]

    def create(self, request):
        serializer = PriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            responce_201 = {
                "message": "Price added successfully",
            }
            return Response(responce_201, status=status.HTTP_201_CREATED)
        response_400 = {
            "message": "Price not added",
        }
        return Response(response_400, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            price = Price.objects.get(pk=pk)
            serializer = PriceSerializer(price, data=request.data)
            if serializer.is_valid():
                serializer.save()
                responce_200 = {
                    "message": "Price updated successfully",
                }
                return Response(responce_200, status=status.HTTP_200_OK)
            response_400 = {
                "message": "Price not updated",
            }
            return Response(response_400, status=status.HTTP_400_BAD_REQUEST)
        except Price.DoesNotExist:
            responce_404 = {
                "message": "Price not found",
            }
            return Response(responce_404, status=status.HTTP_404_NOT_FOUND)


    def destroy(self, request, pk=None):
        try:
            price = Price.objects.get(pk=pk)
            price.delete()
            responce_204 = {
                "message": "Price deleted successfully",
            }
            return Response(responce_204, status=status.HTTP_204_NO_CONTENT)
        except Price.DoesNotExist:
            responce_404 = {
                "message": "Price not found",
            }
            return Response(responce_404, status=status.HTTP_404_NOT_FOUND)


class TipsViewSet(viewsets.ModelViewSet):
    queryset = Tips.objects.all()
    serializer_class = TipsSerializer
    permission_classes = [IsAdminUser]

    def create(self, request):
        serializer = TipsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            responce_201 = {
                "message": "Tips added successfully",
            }
            return Response(responce_201, status=status.HTTP_201_CREATED)
        response_400 = {
            "message": "Tips not added",
        }
        return Response(response_400, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        try:
            tips = Tips.objects.get(pk=pk)
            serializer = TipsSerializer(tips, data=request.data)
            if serializer.is_valid():
                serializer.save()
                responce_200 = {
                    "message": "Tips updated successfully",
                }
                return Response(responce_200, status=status.HTTP_200_OK)
            response_400 = {
                "message": "Tips not updated",
            }
            return Response(response_400, status=status.HTTP_400_BAD_REQUEST)
        except Tips.DoesNotExist:
            responce_404 = {
                "message": "Tips not found",
            }
            return Response(responce_404, status=status.HTTP_404_NOT_FOUND)


    def destroy(self, request, pk=None):
        try:
            tips = Tips.objects.get(pk=pk)
            tips.delete()
            responce_204 = {
                "message": "Tips deleted successfully",
            }
            return Response(responce_204, status=status.HTTP_204_NO_CONTENT)
        except Tips.DoesNotExist:
            responce_404 = {
                "message": "Tips not found",
            }
            return Response(responce_404, status=status.HTTP_404_NOT_FOUND)


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAdminUser]

    def create(self, request):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            responce_201 = {
                "message": "Photo added successfully",
            }
            return Response(responce_201, status=status.HTTP_201_CREATED)
        response_400 = {
            "message": "Photo not added",
        }
        return Response(response_400, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            photo = Photo.objects.get(pk=pk)
            serializer = PhotoSerializer(photo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                responce_200 = {
                    "message": "Photo updated successfully",
                }
                return Response(responce_200, status=status.HTTP_200_OK)
            response_400 = {
                "message": "Photo not updated",
            }
            return Response(response_400, status=status.HTTP_400_BAD_REQUEST)
        except Photo.DoesNotExist:
            responce_404 = {
                "message": "Photo not found",
            }
            return Response(responce_404, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            photo = Photo.objects.get(pk=pk)
            photo.delete()
            responce_204 = {
                "message": "Photo deleted successfully",
            }
            return Response(responce_204, status=status.HTTP_204_NO_CONTENT)
        except Photo.DoesNotExist:
            responce_404 = {
                "message": "Photo not found",
            }
            return Response(responce_404, status=status.HTTP_404_NOT_FOUND)



