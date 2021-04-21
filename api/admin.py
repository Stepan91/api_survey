from django.contrib import admin
from .models import Survey, Question, Choice, Answer, AnswerChoiseUnite


class AnswerChoiceUniteInLine(admin.TabularInline):
    model = Answer.multi_value.through
    extra = 1


class SurveyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_start',
        'date_finish',
        'description',
    )
    search_fields = ('title',)
    list_filter = ('date_start', 'date_finish',)
    empty_value_display = '-пусто-'


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'type_question', 'survey',)
    search_fields = ('survay',)
    empty_value_display = '-пусто-'


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'question',)
    search_fields = ('question',)
    empty_value_display = '-пусто-'


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'question',
    )
    search_fields = ('question',)
    empty_value_display = '-пусто-'
    inlines = (AnswerChoiceUniteInLine,)


admin.site.register(AnswerChoiseUnite)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
