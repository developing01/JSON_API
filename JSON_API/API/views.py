from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Pd, Pvl, Pins, Cldr, Docu, Run, Zm, Zuo

from .serializers import PdSerializers, CldrSerializers, DocuSerializers, PinsSerializers, PvlSerializers, RunSerializers, ZmSerializers, ZuoSerializers


class PdView(APIView):
    '''Данні компанії PD'''
    def get(self, request):
        data = Pd.objects.all()
        serializer = PdSerializers(data, many=True)
        return Response(serializer.data)


class CldrView(APIView):
    '''Данні компанії CLDR'''
    def get(self, request):
        data = Cldr.objects.all()
        serializer = CldrSerializers(data, many=True)
        return Response(serializer.data)


class DocuView(APIView):
    '''Данні компанії DOCU'''
    def get(self, request):
        data = Docu.objects.all()
        serializer = DocuSerializers(data, many=True)
        return Response(serializer.data)


class PinsView(APIView):
    '''Данні компанії PINS'''
    def get(self, request):
        data = Pins.objects.all()
        serializer = PinsSerializers(data, many=True)
        return Response(serializer.data)


class PvlView(APIView):
    '''Данні компанії PVL'''
    def get(self, request):
        data = Pvl.objects.all()
        serializer = PvlSerializers(data, many=True)
        return Response(serializer.data)


class RunView(APIView):
    '''Данні компанії RUN'''
    def get(self, request):
        data = Run.objects.all()
        serializer = RunSerializers(data, many=True)
        return Response(serializer.data)


class ZmView(APIView):
    '''Данні компанії ZM'''
    def get(self, request):
        data = Zm.objects.all()
        serializer = ZmSerializers(data, many=True)
        return Response(serializer.data)


class ZuoView(APIView):
    '''Данні компанії ZUO'''
    def get(self, request):
        data = Zuo.objects.all()
        serializer = ZuoSerializers(data, many=True)
        return Response(serializer.data)


