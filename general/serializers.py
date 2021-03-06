from rest_framework import serializers

from general.models import *

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('__all__')


class FullPropertySerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()
    # rooms = serializers.SerializerMethodField()

    def get_photos(self, obj):
        return PhotoSerializer(obj.photos.all(), many=True).data

    def get_attributes(self, obj):
        return PropertyAttributeSerializer(obj.attributes.first()).data

    def get_rooms(self, obj):
        return PropertyRoomSerializer(obj.rooms.all(), many=True).data

    class Meta:
        model = Property
        fields = ('__all__')
        read_only_fields = ('photos', 'attributes')


class PropertyAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAttribute
        fields = ('remarks', 'confidential_remarks', 'additional_remarks')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo_url', 'thumbnail_url', 'display_order', 'caption']


class MlsAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MlsAgent
        fields = ('__all__')


class MlsOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MlsOffice
        fields = ('__all__')


class OpenHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenHouse
        fields = ('__all__')


class PropertyRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyRoom
        fields = ('__all__')
