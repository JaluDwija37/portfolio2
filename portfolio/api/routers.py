from rest_framework.routers import DefaultRouter
from api.views import *

router: DefaultRouter = DefaultRouter()

router.register(r'about', AboutModelViewSet)
router.register(r'certificate', CertificateModelViewSet)
router.register(r'program', ProgLangModelViewSet)
router.register(r'skill', SkillModelViewSet)
router.register(r'education', EducationModelViewSet)
router.register(r'project', ProjectModelViewSet)
