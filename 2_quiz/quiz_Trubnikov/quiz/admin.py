from django.contrib import admin
from quiz.models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'que_text']


class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'que_id',
        'ans_text',
        'freq']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
