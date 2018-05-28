from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized


class ApiAuthorization(Authorization):
    # Allow updating only if current user is superuser
    def is_authorized(self, request, object=None):
        return bundle.request.user.is_superuser
