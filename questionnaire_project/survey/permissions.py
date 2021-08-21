from django.contrib.auth.models import User, AnonymousUser
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        group = None
        if isinstance(request.user,User):
            group = request.user.groups.all()[0].name
        if group == 'admin' and request.method in ['GET','POST','PUT','DELETE']:
            return True



class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        group =  None
        if isinstance(request.user,User):
            group = request.user.groups.all()[0].name
        if group == 'user' or isinstance(request.user,AnonymousUser):
            return True

