from django.contrib import admin
from .models import Question, Choice

<<<<<<< HEAD
=======
class ChoiceInline(admin.TabularInline):  # 또는 admin.StackedInline
    model = Choice
    extra = 3

>>>>>>> d93dcd757aa16030377cf7fbdc0c23a154f4442d
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
<<<<<<< HEAD
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
     ]

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
=======
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
>>>>>>> d93dcd757aa16030377cf7fbdc0c23a154f4442d
