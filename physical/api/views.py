# -*- coding: utf-8 -*-
import base64

from rest_framework import views
from rest_framework.response import Response
from .. import camera


class ImageAPIView(views.APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        data = camera.capture_image()
        return Response({
            'img': "data:image/jpeg;base64,{}".format(
                base64.b64encode(data.getvalue())
            )
        })
