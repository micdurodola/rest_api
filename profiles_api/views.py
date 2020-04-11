from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        """Return list of API Features"""
        an_apiview=[
            'Uses method as function(get,post,patch,put,delete)'
            'Is similar to traditional Django view'
            'Gives you most control over your application'
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
        