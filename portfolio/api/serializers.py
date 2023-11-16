from rest_framework.serializers import ModelSerializer

from about.models import AboutModel
from certificates.models import CertificateModel
from programing_language.models import ProgLangModel
from skills.models import SkillModel
from educations.models import EducationModel
from projects.models import ProjectModel


class AboutModelSerializer(ModelSerializer):
    class Meta:
        model = AboutModel
        fields = ['id', 'name', 'short_description', 'long_description']


class CertificateModelSerializer(ModelSerializer):
    class Meta:
        model = CertificateModel
        fields = ['id', 'name', 'date', 'intitution', 'image']


class ProgLangModelSerializer(ModelSerializer):
    class Meta:
        model = ProgLangModel
        fields = ['id', 'name', 'description', 'image']


class SkillModelSerializer(ModelSerializer):
    class Meta:
        model = SkillModel
        fields = ['id', 'program', 'level']


class EducationModelSerializer(ModelSerializer):
    class Meta:
        model = EducationModel
        fields = ['id', 'name', 'major', 'grade', 'year_start', 'year_end']


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = ['id', 'name', 'program', 'description', 'link_src', 'image']
