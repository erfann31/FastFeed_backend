from django.db import models
from django.utils import timezone


# from django.contrib.auth.models import AbstractUser
# import requests
# import random
# from FastFeedBackend import settings


class BusinessOwner(models.Model):
    phone_number = models.CharField(max_length=20, unique=True, verbose_name="شماره تلفن")
    first_name = models.CharField(max_length=31, blank=True, null=True, verbose_name="نام(اختیاری)")
    last_name = models.CharField(max_length=31, blank=True, null=True, verbose_name="نام خانوادگی(اختیاری)")
    # username = models.CharField(max_length=50, unique=True)
    # password = models.CharField(max_length=50)
    # verification_code = models.CharField(max_length=6, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(editable=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "صاحبان فروشگاه"
        verbose_name = "صاحب فروشگاه"

    def __str__(self):
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.phone_number}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            # self.verification_code = self.generate_verification_code()
            # self.send_verification_sms
        else:
            self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    # @staticmethod
    # def generate_verification_code():
    #     return str(random.randint(100000, 999999))
    #
    # def send_verification_sms(self):
    #     payload = {
    #         'Messages': [f"Your verification code for FastFeed is: {self.verification_code}"],
    #         'MobileNumbers': [self.phone_number],
    #         'LineNumber': settings.SMSIR_PHONE_NUMBER,
    #         'CanContinueInCaseOfError': 'true'
    #     }
    #     headers = {
    #         'Content-Type': 'application/json',
    #         'x-sms-ir-secure-token': settings.SMSIR_API_KEY
    #     }
    #     response = requests.post(settings.SMSIR_API_URL, json=payload, headers=headers)
    #     if response.status_code != 200:
    #         raise Exception("Failed to send SMS")
