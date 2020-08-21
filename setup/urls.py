from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.api.viewsets import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAluno, ListaAlunosMatriculados

router = routers.DefaultRouter()

router.register(r'alunos', AlunosViewSet, basename='Alunos')
router.register(r'cursos', CursosViewSet, basename='Cursos')
router.register(r'matriculas', MatriculasViewSet, basename='Matriculas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('api/curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
]
