from django.contrib import admin
from .models import *


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    search_fields = ('mentor__name', )
    list_display = ('name', 'main_work', 'phone_number', 'level')

    @admin.display(description='level')
    def level(self, obj):
        if obj.experience  >= 3:
            return 'middle'
        else:
            return 'strong junior'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_filter = ('language', 'mentor')
    list_display = ('name', 'date_started', 'student', 'mentor', 'language')
    search_fields = ('student__name', 'mentor__name')


admin.site.register(Student)