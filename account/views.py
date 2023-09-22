from rest_framework import generics, permissions,response


from .models import CustomUser

from .serializers import UserRegisterSerializer, UserEditSerializer




class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.filter(is_active=True, is_deleted=False)
    permission_classes = (permissions.IsAuthenticated,)
    def get_object(self):
        obj = CustomUser.objects.filter(
            email=self.request.user.email
        ).select_related('profile').prefetch_related('experiences').first()
        return obj
    


class UserEditAPIView(generics.UpdateAPIView):
    queryset = CustomUser.objects.filter(is_active=True, is_deleted=False)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserEditSerializer

    def get_object(self):
        return CustomUser.objects.get(email=self.request.user.email)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = request.user
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return response.Response(serializer.data)



