from django.contrib import admin
from .models import Question, TrueAnswer, WrongAnswer


class ReviewTrueAnswer(admin.StackedInline):
    """Review true answer for question"""
    model = TrueAnswer
    extra = 1


class ReviewWrongAnswer(admin.StackedInline):
    """Review wrong answer for question"""
    model = WrongAnswer
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Registration question admin model"""
    list_display = ('id', 'title')
    list_display_links = ('title',)
    inlines = [ReviewTrueAnswer, ReviewWrongAnswer]


@admin.register(WrongAnswer,TrueAnswer)
class AnswerAdmin(admin.ModelAdmin):
    """Registration wrong answer and true answer admin model"""
    list_display = ('id', 'title', 'question')
    list_display_links = ('title',)
    list_filter = ('question',)

