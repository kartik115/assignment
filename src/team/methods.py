from .models import Team
from .serializers import TeamSerializer
from rest_framework.exceptions import ValidationError


def get_members(member_id):
    if member_id is not None:
        response = Team.objects.filter(pk=member_id)
        if response.count() == 0:
            return 404, None
        else:
            response = response.values().first()
    else:
        response = Team.objects.values()
    return 200, response


def add_member(member_id, data):
    if member_id is not None:
        raise ValidationError("Might be you are looking for PUT request")
    team_serializer = TeamSerializer(data=data)
    team_serializer.is_valid(raise_exception=True)
    team_serializer.save()
    response = team_serializer.data
    return 200, response


def edit_member(member_id, data):
    member = Team.objects.filter(pk=member_id)
    if member.count() == 0:
        return 404, None
    else:
        member = member.first()
        print(member)
    team_serializer = TeamSerializer(instance=member, data=data, partial=True)
    team_serializer.is_valid(raise_exception=True)
    team_serializer.save()
    response = team_serializer.data
    return 200, response


def delete_member(member_id):
    member = Team.objects.filter(pk=member_id)
    if member.count() == 0:
        return 404, None
    else:
        member.delete()
        return 200, None
