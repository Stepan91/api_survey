from rest_framework import serializers
from .models import Survey, Question, Choice, Answer


class SurveySerializer(serializers.ModelSerializer):
    questions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Survey
        fields = [
            'title',
            'date_start',
            'date_finish',
            'description',
            'questions'
            ]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


# вопросы с ответами
class QuestionWithAnswersSerializer(serializers.ModelSerializer):
    answers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = ['text', 'answers']


# опросы с ответами
class UserSurveySerializer(serializers.ModelSerializer):
    questions = QuestionWithAnswersSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = [
            'title', 'date_start', 'date_finish', 'description', 'questions'
            ]


# ответ в виде текста
class TextAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text']


# вспомогательный фильтр конкретного вопроса
class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):

    def get_queryset(self):
        question_id = (
            self.context.get('request').parser_context['kwargs']['question_id']
        )
        request = self.context.get('request', None)
        queryset = super(
            UserFilteredPrimaryKeyRelatedField, self
            ).get_queryset()  
        if not request or not queryset:
            return None
        return queryset.filter(question_id=question_id)


# ответ с одним вариантом
class SingleValueAnswerSerializer(serializers.ModelSerializer):
    single_value = UserFilteredPrimaryKeyRelatedField(
        queryset=Choice.objects.all(),
        many=False
    )

    class Meta:
        model = Answer
        fields = ['single_value']


# ответ с множеством вариантов
class MultipleValueAnswerSerializer(serializers.ModelSerializer):
    multi_value = UserFilteredPrimaryKeyRelatedField(
        queryset=Choice.objects.all(),
        many=True,
    )

    class Meta:
        model = Answer
        fields = ['multi_value']
