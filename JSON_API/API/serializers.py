from rest_framework import serializers
from .models import Pd, Pvl, Pins, Cldr, Docu, Run, Zm, Zuo


class PdSerializers(serializers.ModelSerializer):
    '''Данні компанії PD'''

    class Meta:
        model = Pd
        fields = '__all__'


class CldrSerializers(serializers.ModelSerializer):
    '''Данні компанії PD'''

    class Meta:
        model = Cldr
        fields = '__all__'


class DocuSerializers(serializers.ModelSerializer):
    '''Данні компанії PD'''

    class Meta:
        model = Docu
        fields = '__all__'


class PinsSerializers(serializers.ModelSerializer):
    '''Данні компанії PD'''

    class Meta:
        model = Pins
        fields = '__all__'


class PvlSerializers(serializers.ModelSerializer):
    '''Данні компанії PD'''

    class Meta:
        model = Pvl
        fields = '__all__'


class RunSerializers(serializers.ModelSerializer):
    '''Данні компанії PD'''

    class Meta:
        model = Run
        fields = '__all__'


class ZmSerializers(serializers.ModelSerializer):
    '''Данні компанії PD'''

    class Meta:
        model = Zm
        fields = '__all__'


class ZuoSerializers(serializers.ModelSerializer):
    '''Данні компанії PD'''

    class Meta:
        model = Zuo
        fields = '__all__'