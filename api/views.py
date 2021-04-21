from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404
from .models import Survey, Question, Choice, Answer
from .serializers import (
    SurveySerializer, QuestionSerializer, ChoiceSerializer,
    AnswerSerializer, TextAnswerSerializer, SingleValueAnswerSerializer,
    MultipleValueAnswerSerializer, UserSurveySerializer
)
from rest_framework.permissions import (
    IsAdminUser, AllowAny, IsAuthenticated
)
from datetime import datetime


# получение/добавление/изменение/удаление опросов
class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [IsAdminUser]


# получение/добавление/изменение/удаление опросов в вопросе
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        survey_id = self.kwargs['survey_id']
        survey = get_object_or_404(Survey, id=survey_id)
        return survey.questions

    def perform_create(self, serializer):
        survey_id = self.kwargs['survey_id']
        survey = get_object_or_404(Survey, id=survey_id)
        serializer.save(survey=survey)


# получение/добавление/изменение/удаление вариантов ответа
class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        question = get_object_or_404(Question, id=question_id)
        return question.choices

    def perform_create(self, serializer):
        question_id = self.kwargs['question_id']
        question = get_object_or_404(
            Question,
            id=question_id,
            survey__id=self.kwargs['id'],
        )
        serializer.save(question=question)


# список активных вопросов
class ActiveSurveyListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Survey.objects.filter(
        date_finish__gte=datetime.today()
    )
    serializer_class = SurveySerializer
    permission_classes = [AllowAny]


# ответ на вопрос
class CreateAnswerViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        question_id = self.kwargs['question_id']
        question = get_object_or_404(
            Question,
            id=question_id,
            survey__id=self.kwargs['survey_id'],
        )
        if question.type_question == 'text':
            return TextAnswerSerializer
        elif question.type_question == 'single_value':
            return SingleValueAnswerSerializer
        else:
            return MultipleValueAnswerSerializer

    def perform_create(self, serializer):
        question_id = self.kwargs['question_id']
        question = get_object_or_404(
            Question,
            id=question_id,
            survey__id=self.kwargs['survey_id'],
        )
        serializer.save(author=self.request.user, question=question)


# список пройденных опросов с детализацией по ответам
class UserSurveyListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSurveySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Survey.objects.filter(
            questions__answers__author__id=user_id
        )
        return queryset
