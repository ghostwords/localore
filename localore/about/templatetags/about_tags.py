from django import template

from about.models import AboutMissionPage, AboutTeamPage, AboutContactPage
from localore_admin.models import PageAlias

register = template.Library()


@register.assignment_tag
def get_about_index_page():
    # TODO make more robust
    return PageAlias.objects.live().filter(title="About").first()


@register.assignment_tag
def get_about_mission_page():
    return AboutMissionPage.objects.live().first()


@register.assignment_tag
def get_about_team_page():
    return AboutTeamPage.objects.live().first()


@register.assignment_tag
def get_about_contact_page():
    return AboutContactPage.objects.live().first()
