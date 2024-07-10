from django.contrib import admin

from .models import PersonalInfo, WorkExperience, Education, Service, Skill, Project, Volunteering, ContactMessage


class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'linkedin', 'github', 'youtube', 'country', 'created', 'is_deleted')
    search_fields = ('full_name', 'email', 'phone')
    list_filter = ('country', 'is_deleted')


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'created', 'is_deleted')
    search_fields = ('title', 'company')
    list_filter = ('company', 'is_deleted')


class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date', 'grade', 'created', 'is_deleted')
    search_fields = ('degree', 'institution')
    list_filter = ('institution', 'is_deleted')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created', 'is_deleted')
    search_fields = ('name',)
    list_filter = ('is_deleted',)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created', 'is_deleted')
    search_fields = ('name',)
    list_filter = ('is_deleted',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'technologies_used', 'github_link', 'created', 'is_deleted')
    search_fields = ('title', 'category')
    list_filter = ('category', 'is_deleted')


class VolunteeringAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'start_date', 'end_date', 'created', 'is_deleted')
    search_fields = ('title', 'organization')
    list_filter = ('organization', 'is_deleted')


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'created', 'is_deleted')
    search_fields = ('first_name', 'last_name', 'email', 'subject')
    list_filter = ('is_deleted',)


admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Volunteering, VolunteeringAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
