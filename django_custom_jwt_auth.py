# Get access token from cookies instead of Authorization header

from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        raw_token = request.COOKIES.get('access')
        if raw_token is None:
            return None
        
        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token
