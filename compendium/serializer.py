from django.core.serializers.python import Serializer as PythonSerializer
from django.core.serializers.python import Deserializer as PythonDeserializer

class MySerializer(PythonSerializer):
    def end_object( self, obj ):
        self._current['id'] = obj._get_pk_val()
        self.objects.append( self._current )

    def end_serialization(self):
        cleaned_objects = []

        for obj in self.objects:
            del obj['pk']
            cleaned_objects.append(obj)
