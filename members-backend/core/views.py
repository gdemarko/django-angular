from rest_framework import viewsets
from core.models import Member
from core.serializers import (
    MemberSerializer, MemberSimpleSerializer
)
from rest_framework.response import Response


class MemberViewSet(viewsets.ModelViewSet):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def list(self, request, *args, **kwargs):
        queryset = Member.objects.all()
        serializer = MemberSimpleSerializer(queryset, many=True)

        return Response(serializer.data)
