from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from rest_framework import viewsets, status, mixins
from rest_framework.parsers import FileUploadParser, MultiPartParser, JSONParser
from rest_framework.views import Response
from . import models
from . import serializers
from . import filters


# Create your views here.

class CasamentoView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):

    queryset = models.Casamento.objects.all()
    serializer_class = serializers.CasamentoSerializer
    parser_classes = [JSONParser, MultiPartParser]
    filter_class = filters.CasamentoFilter
    
    def bad_request(self, message):
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'detail': message} if message is not None else None)
    
    def create(self, request, *args, **kwargs):
        files = request.FILES
        if files.get('image', None) is None:
            return self.bad_request(_('The file is required.'))
        img = files['image']
        instance = models.Casamento(image=img)
        try:
            instance.save()
        except Exception:
            return self.bad_request(_('Erro while saving image'))
        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        
        response_instance = serializer.save()
        response_serializer = self.serializer_class(response_instance, context=self.get_serializer_context())
        return Response(status=status.HTTP_200_OK, data=response_serializer.data)