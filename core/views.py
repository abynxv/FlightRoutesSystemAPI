# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Route, Airport
from .serializers import RouteSerializer
from django.shortcuts import get_object_or_404

class NthNodeAPIView(APIView):
    def get(self, request):
        n = int(request.GET.get('n', 1))
        direction = request.GET.get('direction', 'right')
        
        routes = list(Route.objects.order_by('position'))
        
        if direction == 'left':
            routes = routes[::-1]

        if 1 <= n <= len(routes):
            node = routes[n-1]
            serializer = RouteSerializer(node)
            return Response(serializer.data)
        return Response({"error": "Node not found"}, status=status.HTTP_404_NOT_FOUND)


class LongestNodeAPIView(APIView):
    """
    Find the node with the longest duration
    """
    def get(self, request):
        node = Route.objects.order_by('-duration').first()
        if node:
            serializer = RouteSerializer(node)
            return Response(serializer.data)
        return Response({"error": "No routes found"}, status=status.HTTP_404_NOT_FOUND)


class ShortestNodeBetweenAPIView(APIView):
    """
    Find shortest duration between two airports
    """
    def get(self, request):
        start_code = request.GET.get('start')
        end_code = request.GET.get('end')

        try:
            start_pos = Route.objects.get(airport__code=start_code).position
            end_pos = Route.objects.get(airport__code=end_code).position
        except Route.DoesNotExist:
            return Response({"error": "Airport not found"}, status=status.HTTP_404_NOT_FOUND)

        if start_pos > end_pos:
            start_pos, end_pos = end_pos, start_pos

        nodes = Route.objects.filter(position__gte=start_pos, position__lte=end_pos)
        node = nodes.order_by('duration').first()
        serializer = RouteSerializer(node)
        return Response(serializer.data)
