from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class TestIsUp(APIView):

  @staticmethod
  def get(request: Request):

    response = {
      "status": "OK"
    }

    return Response(response, status=200)
