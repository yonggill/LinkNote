# -*- coding:utf-8 -*-

from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy


def check_permissions(user, permissions):
    """
    Permissions can be a list or a tuple of lists. If it is a tuple,
    every permission lists will be evaluated and the outcome will be checked
    for truthiness.
    Each item of the list(s) must be either a valid Django permission name
    (model.codename) or an attribute on the User model
    (e.g. 'is_active', 'is_superuser').

    Example usage:
    - permissions_required(['is_staff', ])
      would replace staff_member_required
    - permissions_required(['is_anonymous', ])
      would replace login_forbidden
    - permissions_required((['is_staff', ], ['client.dashboard_access']))
      allows both staff users and users with the above permission
    """
    def _check_one_permission_list(perms):
        regular_permissions = [perm for perm in perms if '.' in perm]
        conditions = [perm for perm in perms if '.' not in perm]
        if conditions and ['is_active', 'is_anonymous'] not in conditions:
            # always check for is_active where appropriate
            conditions.append('is_active')
        passes_conditions = all([getattr(user, perm) for perm in conditions])
        return passes_conditions and user.has_perms(regular_permissions)

    if permissions is None:
        return True
    elif isinstance(permissions, list):
        return _check_one_permission_list(permissions)
    else:
        return any(_check_one_permission_list(perm) for perm in permissions)


def permissions_required(permissions, login_url=None):
    """
    Decorator that checks if a user has the given permissions.
    Accepts a list or tuple of lists of permissions (see check_permissions
    documentation).
    If the user is not logged in and the test fails, she is redirected to a
    login page. If the user is logged in, she gets a HTTP 403 Permission Denied
    message, analogue to Django's permission_required decorator.
    """
    if login_url is None:
        login_url = reverse_lazy('login')

    def _check_permissions(user):
        outcome = check_permissions(user, permissions)
        if not outcome and user.is_authenticated():
            raise PermissionDenied
        else:
            return outcome

    return user_passes_test(_check_permissions, login_url=login_url)
