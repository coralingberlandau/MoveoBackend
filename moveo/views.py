from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from .models import Codeblock
from .serializer import CodeblockSerializer
from rest_framework.decorators import action

@api_view(['GET'])
def index(req):
    """
    A basic test function that returns a simple response for development or testing purposes.
    """
    return Response({'hello': 'world'})

@api_view(['GET'])
def test(req):
    """
    Another test function that returns a 'success' response.
    """
    return Response({'test': 'success'})

class CodeblockViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Codeblock objects:
    Provides CRUD (Create, Read, Update, Delete) functionality.
    """
    queryset = Codeblock.objects.all()  
    serializer_class = CodeblockSerializer  

    @action(detail=False, methods=['GET'], url_path='title/(?P<title>.+)')
    def get_by_title(self, request, title=None):
        """
        Retrieve a Codeblock by its title:
        Performs a query to find an object based on the provided title.
        """
        try:
            codeblock = Codeblock.objects.get(title=title)
            serializer = self.get_serializer(codeblock) 
            print('Debug log: Codeblock fetched successfully') 
            print(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except Codeblock.DoesNotExist:
            return Response({"error": "Codeblock not found"}, status=status.HTTP_404_NOT_FOUND)
