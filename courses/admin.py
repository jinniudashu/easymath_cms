from django.contrib import admin

from .models import Course, Lesson, Unit, Exercises
from courses.batch_upload.batch_upload import batch_upload


class InLineLesson(admin.TabularInline):
    model = Lesson
    extra = 1
    max_num = 3


class InLineUnits(admin.TabularInline):
    model = Unit
    extra = 1
    max_num = 3


class InLineExercises(admin.TabularInline):
    model = Exercises
    extra = 1
    max_num = 3


class CourseAdmin(admin.ModelAdmin):
    def batch_upload(self, request, queryset):
        batch_upload()

    inlines = [InLineLesson]
    list_display = ('title', 'description', 'combine_title_and_slug')
    list_display_links = ('title', 'combine_title_and_slug')
    list_filter = ('title',)
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': (
                'slug',
                'title',
                'thumbnail',
                'description',
            )
        }),
    )
    actions = ['batch_upload']

    def combine_title_and_slug(self, obj):
        return "{} - {}".format(obj.title, obj.slug)


class UnitAdmin(admin.ModelAdmin):
    inlines = [InLineLesson]
    list_display = ('position', 'title', 'description', 'course')
    list_display_links = ('title', 'description')
    list_editable = ('course', )
    list_filter = ('title', 'description', 'course')
    search_fields = ('title', 'description', 'course')
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'description',
                'course',
            )
        }),
    )


class LessonAdmin(admin.ModelAdmin):
    inlines = [InLineExercises]
    list_display = ('course', 'unit', 'position', 'title', 'description', 'is_free')
    list_display_links = ('title', 'description')
    list_filter = ('title', 'description', 'course', 'unit', 'position', 'is_free')
    search_fields = ('title', 'description', 'course', 'unit', 'position', 'is_free')
    fieldsets = (
        (None, {
            'fields': (
                'slug',
                'title',
                'description',
                'thumbnail',
                'course',
                'unit',
                'position',
                'video',
                'is_free',
            )
        }),
    )

admin.site.register(Course, CourseAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Exercises)