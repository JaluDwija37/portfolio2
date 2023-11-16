from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
# from rest_framework.viewsets import ModelViewSet

from about.models import AboutModel
from certificates.models import CertificateModel
from programing_language.models import ProgLangModel
from skills.models import SkillModel
from educations.models import EducationModel
from projects.models import ProjectModel

from api.serializers import *


class AboutModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutModel.objects.all()
    serializer_class = AboutModelSerializer

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()  # Dapatkan objek yang akan diperbarui
    #     # Gunakan serializer untuk memperbarui objek
    #     serializer = self.get_serializer(instance, data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()  # Simpan perubahan ke basis data
    #         # Kirim respons dengan data yang telah diperbarui
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=400)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = []
        return [permission() for permission in permission_classes]


class CertificateModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CertificateModel.objects.all()
    serializer_class = CertificateModelSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = []
        return [permission() for permission in permission_classes]


class ProgLangModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProgLangModel.objects.all()
    serializer_class = ProgLangModelSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = []
        return [permission() for permission in permission_classes]


class SkillModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SkillModel.objects.all()
    serializer_class = SkillModelSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = []
        return [permission() for permission in permission_classes]


class EducationModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EducationModel.objects.all()
    serializer_class = EducationModelSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = []
        return [permission() for permission in permission_classes]


class ProjectModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = []
        return [permission() for permission in permission_classes]
