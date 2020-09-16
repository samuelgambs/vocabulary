from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from . serializers import TextSerializers
from . models import Texts
from utils.nlp import *


class TextCreateApiView(ListCreateAPIView):
    serializer_class = TextSerializers
    queryset = Texts.objects.all()

    def perform_create(self, serializer):
        try:
            process_text = NLP(
                self.request.data['primary_text'], self.request.data['second_text'])

            serializer.save(
                primary_text=self.request.data['primary_text'],
                second_text=self.request.data['second_text'],
                result=process_text.process()
            )
        except Texts.DoesNotExist:
            raise Http404()
