from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from .services import check_authentication
from django.core.exceptions import PermissionDenied

import logging

logger = logging.getLogger(__name__)


class CommunicationView(APIView):
    @staticmethod
    def authenticate(request):
        jwt = request.headers["AUTHORIZATION"].split()[1]
        print(f"CommunicationView called META : {jwt}")
        if not check_authentication(jwt):
            raise PermissionDenied


class Echo(CommunicationView):
    def post(self, request, format=None):
        logger.info("echo api called")
        self.authenticate(request)
        return Response(request.data)


class Time(CommunicationView):
    def get(self, request, format=None):
        logger.info("time api called")
        super().authenticate(request)
        return Response(datetime.now())
