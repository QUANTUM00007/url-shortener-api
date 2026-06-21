from django.db import models
import string
import random


def generate_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=6))


class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(
        max_length=10,
        unique=True,
        default=generate_code
    )
    clicks = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.short_code
