from rest_framework.serializers import HyperlinkedModelSerializer
from Restapi.models import Shoe, ShoeColor, Manufacturer, ShoeType

class ShoeSerializers (HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            "size","brand_name", "manufacturer", "color", "material", "shoe_type", "fasten_type", "id"
        ]


class ShoeColorSerializers (HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = [
            "color_name","id"
        ] 

class ManufacturerSerializers (HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            "name", "website", "id"
        ]                     

class ShoeTypeSerializers (HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = [
            "style", "id"
        ]           