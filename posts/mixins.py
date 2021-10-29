from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin



class OwnerOnlyMixin(LoginRequiredMixin, PermissionRequiredMixin):

    owner = None # name of the user foreignkey field name
    permission_denied_message = 'Only owner is allowed to perform this operation'
    def has_permission(self):
        object = self.get_object()
        owner = getattr(object,self.owner)
        #return True if the authenticated user is the owner !
        return self.request.user == owner
            

    