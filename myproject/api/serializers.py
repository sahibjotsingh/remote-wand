from __future__ import print_function
from wand.image import Image
from wand.display import display
from django.core.files import File
import base64
from rest_framework import serializers
from .models import ImageModel

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    image_file = serializers.ImageField(max_length = None, use_url=True)

    class Meta:
        model = ImageModel
        fields = ('id', 'image_file')

class ImageManipulateSerializer(serializers.ModelSerializer):

    base64_image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ImageModel
        fields = ('base64_image', 'id')

    def get_base64_image(self, obj):
        with open(obj.image_file.path, 'rb') as f:
            with Image(file=f) as img:
                with img.clone() as i:
                    request_object = self.context['request']

                    # resize image
                    w = request_object.query_params.get('width')
                    h = request_object.query_params.get('height')
                    try:
                        _w = int(w,10)
                        _h = int(h,10)
                        i.resize(int(i.width * _w * 0.01), int(i.height * _h * 0.01))
                    except:
                       pass

                    # crop image
                    left = request_object.query_params.get('left')
                    right = request_object.query_params.get('right') 
                    top = request_object.query_params.get('top')
                    bottom = request_object.query_params.get('bottom')
                    try:
                        _left = int(left,10)
                        _right = int(right,10)
                        _top = int(top,10)
                        _bottom = int(bottom,10)
                        i.crop(int(_left), int(_right), int(_top), int(_bottom))
                    #i.crop(int(i.width * left1 * 0.01), int(i.width * right1 * 0.01), int(i.height * top1 * 0.01), int(i.height * bottom1 * 0.01))
                    except:
                        pass         

                    # charcol transform
                    radius = request_object.query_params.get('radius')
                    sigma = request_object.query_params.get('sigma')
                    try:
                        _radius = float(radius)
                        _sigma = float(sigma)
                        i.charcoal(radius=_radius, sigma=_sigma)
                        #i.charcoal(radius=radius, sigma=sigma)
                        img.extent(width=img.width*2)
                        img.composite(i, top=0, left=i.width) 
                    except:
                        pass              

                    # rotate 
                    angle = request_object.query_params.get('rotate_by')
                    try:
                        _angle=float(angle)
                        i.rotate(_angle)
                    except:
                        pass

                    #evaluate expression
                    operator = request_object.query_params.get('operator')
                    value = request_object.query_params.get('value')
                    channel = request_object.query_params.get('channel')
                    try:
                        _operator = str(operator)
                        _value = float(value)
                        _channel=str(channel)
                        i.evaluate(operator=_operator, value=1, channel=_channel)
                    except:
                        pass

                    i.save(filename='waste.png')
                    waste = open('waste.png', 'rb')
                    image = File(waste)
                    data = base64.b64encode(image.read())
                    waste.close()
                    return data

"""        with Image(filename=obj.image_file.path) as img:
            for r in 1, 2, 3:
                with img.clone() as i:
                    i.resize(int(i.width * r * 0.25), int(i.height * r * 0.25))
                    i.rotate(90 * r)
                    data = base64.b64encode(i)
                    return data"""

"""
def get_base64_image(self, obj):
        f = open(obj.image_file.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data
"""