from django.contrib.auth.base_user import BaseUserManager

from models import Worker

class WorkerBackend(object):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Worker.objects.get(email=username)
            if user.check_password(password):
                return user
        except Worker.DoesNotExist:
            return None


class WorkerManager(BaseUserManager):
    model = Worker
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Поле email должно быть установлено')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user