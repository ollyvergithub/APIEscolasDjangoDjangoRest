from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from escola.api.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from escola.models import Aluno, Curso, Matricula


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    # @action(methods=['get'], detail=True)
    # def matriculas(self, request, pk=None):
    #     id = self.request.query_params.get('id', None)
    #     queryset = Matricula.objects.filter(aluno_id=pk)
    #     serializer = ListaMatriculasAlunoSerializer(queryset)
    #     return Response(serializer.data)
    #     # id = self.request.query_params.get('id', None)
    #     # queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    #     # return queryset.toJson()


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas por id de aluno"""
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer


class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando todos os alunos matriculados em um determinado curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer





