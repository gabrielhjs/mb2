import json

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class TestIsUp(APIView):

  @staticmethod
  def get(request: Request) -> Response:

    with open("test.json") as file:
      response = json.load(file)

    return Response(response, status=200)

  @staticmethod
  def post(request: Request) -> Response:
    data = request.data
    print(data)

    with open("test.json", "r") as file:
      file_data = json.load(file)
      file.close()

    file_data.update(data)

    with open("test.json", "w") as file:
      json.dump(file_data, file)
      file.close()

      return Response(file_data, status=301)


