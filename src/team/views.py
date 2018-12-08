from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import team.methods as methods

# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def team(request, member_id=None):
    if request.method == 'GET':
        status, response = methods.get_members(member_id)
    elif request.method == 'POST':
        status, response = methods.add_member(member_id, request.data)
    elif request.method == 'PUT':
        status, response = methods.edit_member(member_id, request.data)
    elif request.method == 'DELETE':
        status, response = methods.delete_member(member_id)
    return Response(status=status, data=response)
