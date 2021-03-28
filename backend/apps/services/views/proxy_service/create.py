from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response


class ProxyServiceCreateAPIView(CreateAPIView):
    """
    Set "service_class" field for use

    Replaces the method call

    self.perform_create(serializer)

    with

    self.service_class.execute(serializer), in
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        self.service_class.execute(self, serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    # def perform_create(self, serializer):
    #     serializer.save()