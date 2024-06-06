import json
import os
import subprocess

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EvaluationSerializer


class EvaluationApi(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EvaluationSerializer(data=request.data)
        if serializer.is_valid():
            data = json.dumps(serializer.validated_data)

            try:
                current_directory = os.getcwd()
                absolute_path = os.path.join(os.path.join(os.path.join(current_directory, 'math_wiz'), 'math_app'),
                                             'math_wiz_app')
                process = subprocess.Popen([absolute_path, '-j', str(data)],
                                           stdin=subprocess.PIPE,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)

                stdout, stderr = process.communicate(input=json.dumps(data).encode())

                output_data = json.loads(stdout)

                if output_data.get('type') == 'error':
                    return Response(output_data, status=status.HTTP_400_BAD_REQUEST)

                return Response(output_data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
