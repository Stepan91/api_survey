from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

QUESTION_CHOICES = [
    ('text', 'ответ текстом'),
    ('single_value', 'ответ с выбором одного значения'),
    ('multi_value', 'ответ с выбором нескольких вариантов')
]


class Survey(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    date_start = models.DateTimeField(
        'Дата начала',
        auto_now_add=True,
        db_index=True
    )
    date_finish = models.DateTimeField(
        'Дата окончания',
        auto_now_add=True,
        db_index=True
    )
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    text = models.TextField(verbose_name='Текст вопроса')
    type_question = models.CharField(
        max_length=30,
        choices=QUESTION_CHOICES,
        verbose_name='Тип вопроса'
    )
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Опрос'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    title = models.TextField(verbose_name='Вариант ответа')
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices',
        verbose_name='Вопрос'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'


class Answer(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        null=True,
        related_name='answers',
        verbose_name='Вопрос'
    )
    text = models.TextField(
        blank=True,
        verbose_name='Ответ текстом'
    )
    single_value = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE,
        null=True,
        related_name='single_value_answers',
        verbose_name='Ответ с выбором одного значения'
    )
    multi_value = models.ManyToManyField(
        Choice,
        blank=True,
        verbose_name='Ответ с выбором нескольких вариантов'
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


# вспомогательная модель
# для отображения many2many в админке
class AnswerChoiseUnite(models.Model):
    choice = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE,
        verbose_name='Вариант ответа'
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        verbose_name='Вопрос'
    )
    date_answer = models.DateField()

    class Meta:
        verbose_name = 'Связь Answer-Choice'
        verbose_name_plural = 'Связи Answer-Choice'
