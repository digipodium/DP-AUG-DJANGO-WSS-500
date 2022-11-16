from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from products.models import Product

@api_view(['GET'])
def get_product_list(request):
    pds = Product.objects.all()
    slr = ProductSerializer(pds, many=True)
    return Response(slr.data)
