from django.shortcuts import render, get_object_or_404

from app.models import (
    PersonalInfo,
    WorkExperience,
    Education,
    Service,
    Skill,
    Project,
    Volunteering,
    ContactMessage
)


def index(request):
    # Fetching PersonalInfo with error handling using get_object_or_404
    personal_info = get_object_or_404(PersonalInfo, id=1)

    # Filtering other models for non-deleted objects
    work_experience = WorkExperience.objects.filter(is_deleted=False)
    education = Education.objects.filter(is_deleted=False)
    service = Service.objects.filter(is_deleted=False)
    skill = Skill.objects.filter(is_deleted=False)
    project = Project.objects.filter(is_deleted=False)
    volunteering = Volunteering.objects.filter(is_deleted=False)
    contact_message = ContactMessage.objects.filter(is_deleted=False)

    context = {
        'personal_info': personal_info,
        'work_experience': work_experience,
        'education': education,
        'service': service,
        'skill': skill,
        'project': project,
        'volunteering': volunteering,
        'contact_message': contact_message
    }

    return render(request, 'index.html', context=context)
