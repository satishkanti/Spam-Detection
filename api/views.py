from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Contact, User
from .serializers import UserSerializer, ContactSerializer

#Viewset for User model.
class UserViewSet(viewsets.ModelViewSet):
   
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def get_permissions(self):
        # Allow unauthenticated users to create new accounts, but require authentication for other actions
        if self.action == 'create':
            return []
        return [IsAuthenticated()]

#Viewset for Contact model.
class ContactViewSet(viewsets.ModelViewSet):
    
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter contacts by the authenticated user
        user = self.request.user
        return Contact.objects.filter(user=user)
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    #Custom action to mark a contact as spam.
    @action(detail=True, methods=['post'])
    def mark_as_spam(self, request, pk=None):
        
        try:
            # Get the contact object
            contact = self.get_object()
            # Update the is_spam field and save
            contact.is_spam = True
            contact.save()
            return Response({'status': 'Contact marked as spam'}, status=status.HTTP_200_OK)
        except Contact.DoesNotExist:
            # Handle case where the contact does not exist
            return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)

#View to search contacts by name or phone number.
class SearchContactView(generics.ListAPIView):

    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the search query from request parameters
        query = self.request.query_params.get('search', '')
        # Filter contacts by name or phone number containing the search query
        queryset = Contact.objects.filter(
            Q(name__icontains=query) | Q(phone_number__icontains=query)
        ).order_by('name')
        return queryset
