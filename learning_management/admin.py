from django.contrib import admin

from .models import Profile, LearningPlan, LearningLog


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'bio')
    list_display_links = ('user', 'avatar', 'bio')
    list_filter = ('user', 'avatar', 'bio')
    search_fields = ('user', 'avatar', 'bio')
    fieldsets = (
        (None, {
            'fields': (
                'user',
                'avatar',
                'bio',
            )
        }),
    )


class LearningPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'thumbnail', 'is_public')
    list_display_links = ('title', 'description', 'thumbnail', 'is_public')
    list_filter = ('title', 'description', 'thumbnail', 'is_public')
    search_fields = ('title', 'description', 'thumbnail', 'is_public')
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'description',
                'thumbnail',
                'is_public',
            )
        }),
    )


class LearningLogAdmin(admin.ModelAdmin):
    list_display = ('slug', )
    list_display_links = ('slug', )
    list_filter = ('slug', )
    search_fields = ('slug', )
    fieldsets = (
        (None, {
            'fields': (
                'slug',
            )
        }),
    )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(LearningPlan, LearningPlanAdmin)
admin.site.register(LearningLog, LearningLogAdmin)