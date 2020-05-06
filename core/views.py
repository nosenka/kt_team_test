from rest_framework import views, viewsets, mixins, response

from core import models

from . import serializers, tasks


class RateViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Rate.objects.all()
    serializer_class = serializers.RateSerializer


class UpdateRatesView(views.APIView):

    def get(self, request):
        tasks.update_rates.delay()
        return response.Response()
