from functools import wraps

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from arestro_app.restro.models import CustomUser

MyUser = get_user_model()


def login_credentials(f):
    @wraps(f)
    def decorated_function(*args):
        try:
            request = args[1]
            email = request.data.get("email")
            password = request.data.get('password')

            email = email.strip()
            if not password:
                return JsonResponse({
                    'status': HTTP_400_BAD_REQUEST,
                    'message': 'Password required.',
                })

            if not email:
                return JsonResponse({
                    'status': HTTP_400_BAD_REQUEST,
                    'message': 'Email/Phone required.',
                })

            context = {'email': email, 'password': password}
            return f(args[0], request, context)

        except Exception as e:
            return JsonResponse({
                'status': HTTP_400_BAD_REQUEST,
                'message': 'Server problem' + str(e),
            })

    return decorated_function


class CustomUserCheck(object):

    @staticmethod
    def check_user(email):
        try:
            user = CustomUser.objects.filter(email=email).first()
            if user:
                return user
            return None

        except MyUser.DoesNotExist:
            return None


class CustomAuthenticationBackend(object):

    @staticmethod
    def authenticate(email=None, password=None):
        try:
            user = CustomUser.objects.filter(email=email).first()

            if user:
                if user.check_password(password):
                    return user
            return None

        except MyUser.DoesNotExist:
            return None
