import requests
from django.conf import settings

from core import models
from kt_team_test.celery import app


@app.task(bind=True)
def update_rates(self):
    # Get for single rate only, no multiple rates support yet
    RATE_ID = 1

    res = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id={}'.format(RATE_ID),
                       headers={
                            'X-CMC_PRO_API_KEY': settings.COIN_MARKET_CAP_API_KEY,
                            'Accept': 'application/json'
                        }).json()

    rates_data = res['data'][str(RATE_ID)]['quote']

    # There is no multi currencies support yet, so just get a USD
    usd_rate = rates_data['USD']

    models.Rate.objects.create(source_currency='btc', dest_currency='usd',
                               price=usd_rate['price'], rate_updated_at=usd_rate['last_updated'])
