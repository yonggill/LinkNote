# -*- coding:utf-8 -*-

######
# Wishket Module Import
######
from linknote.core.decorators import permissions_required

# This code copied from
# https://github.com/tangentlabs/django-oscar/blob/master/oscar/core/application.py


class Application(object):
    """
    apps 내 각 url 들을 하나의 Application 으로 병합하는 Class
    """

    #: Namespace name
    name = None

    #: A name that allows that functionality within this app to be disabled
    hidable_feature_name = None

    #: Maps view names to a tuple or list of permissions
    permissions_map = {}

    #: Default permission for any view not in permissions_map
    default_permissions = None

    def __init__(self, app_name=None, **kwargs):
        self.app_name = app_name
        # Set all kwargs as object attributes
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

    def get_urls(self):
        """
        Return the url patterns for this app.
        """
        return []

    def post_process_urls(self, urlpatterns):
        """
        Customize URL patterns.

        This method allows decorators to be wrapped around an apps URL
        patterns.

        By default, this only allows custom decorators to be specified, but you
        could override this method to do anything you want.

        Args:
            urlpatterns (list): A list of URL patterns

        """
        # Test if this the URLs in the application instance should be
        # available. If the feature is hidden then we don't include the URLs.

        for pattern in urlpatterns:
            if hasattr(pattern, 'url_patterns'):
                self.post_process_urls(pattern.url_patterns)
            if not hasattr(pattern, '_callback'):
                continue
            # Look for a custom decorator
            decorator = self.get_url_decorator(pattern)
            if decorator:
                # Nasty way of modifying a RegexURLPattern
                pattern._callback = decorator(pattern._callback)
        return urlpatterns

    def get_permissions(self, url):
        """
        Return a list of permissions for a given URL name

        Args:
            url (str): A URL name (eg ``project.project``)

        Returns:
            list: A list of permission strings.
        """
        # url namespaced?
        if url is not None and ":" in url:
            view_name = url.split(':')[1]
        else:
            view_name = url
        return self.permissions_map.get(view_name, self.default_permissions)

    def get_url_decorator(self, pattern):
        """
        Return the appropriate decorator for the view function with the passed
        URL name. Mainly used for access-protecting views.

        It's possible to specify:

        - no permissions necessary: use None
        - a st of permissions: use a list
        - two set of permissions (`or`): use a two-tuple of lists

        See permission_required decorator for details
        """
        permissions = self.get_permissions(pattern.name)
        return permissions_required(permissions)

    @property
    def urls(self):
        # We set the application and instance namespace here
        return self.get_urls(), self.app_name, self.name
