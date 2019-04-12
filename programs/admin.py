from django.contrib import admin

from .models import College, Program, Requirement, Application


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'country', 'city')
    list_filter = ('country', 'city')
    search_fields = ('name', 'short_name', 'summary')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'college',
        'degree_type',
        'application_start_date',
        'application_end_date'
    )
    list_filter = (
        'degree_type',
        'application_start_date',
        'application_end_date'
    )
    search_fields = ('title', 'summary')


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('program', 'name', 'is_optional')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'program', 'status')
    list_filter = ('status', 'started_at')
