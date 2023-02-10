from django.contrib import admin

from .models import Course, Lesson, Unit, Exercise
from courses.batch_upload.down_images import down_images


class InLineLesson(admin.TabularInline):
    model = Lesson
    extra = 1
    max_num = 3


class InLineUnits(admin.TabularInline):
    model = Unit
    extra = 1
    max_num = 3


class InLineExercise(admin.TabularInline):
    model = Exercise
    extra = 1
    max_num = 3


class CourseAdmin(admin.ModelAdmin):
    def down_images(self, request, queryset):
        down_images()

    # inlines = [InLineLesson]
    list_display = ('title', 'description', 'slug')
    list_display_links = ('title', 'slug')
    list_filter = ('title',)
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': (
                'slug',
                'title',
                'thumbnail',
                'thumbnail_name',
                'description',
            )
        }),
    )
    actions = ['down_images']


class UnitAdmin(admin.ModelAdmin):
    inlines = [InLineLesson]
    list_display = ('course', 'position', 'title', 'description')
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
    inlines = [InLineExercise]
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
                'thumbnail_name',
                'course',
                'unit',
                'position',
                'video',
                'video_additional',
                'is_free',
            )
        }),
    )

admin.site.register(Course, CourseAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Exercise)