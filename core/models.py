from django.db import models


class Rate(models.Model):
    SOURCE_CURRENCY_CHOICES = (
        ('btc', "BTC"),

    )
    DEST_CURRENCY_CHOICES = (
        ('usd', 'USD'),
    )

    source_currency = models.CharField(choices=SOURCE_CURRENCY_CHOICES, max_length=3)
    dest_currency = models.CharField(choices=DEST_CURRENCY_CHOICES, max_length=3)

    # It is usually bad idea to store money in float, but source API has a floating point too
    price = models.FloatField()

    # Updated date from API
    rate_updated_at = models.DateTimeField()

    # Time when rate was parsed
    created_at = models.DateTimeField(auto_now_add=True)
