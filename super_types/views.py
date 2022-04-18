from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SuperType
from .serializers import SuperTypeserializer

@api_view(['GET'])
def super_type_list(request):
    super_type = SuperType.objects.all()
    serializer = SuperTypeserializer(super_type, many=True)
    

    return Response(serializer.data)