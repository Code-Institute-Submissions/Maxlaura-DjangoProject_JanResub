
from django.conf.urls import url
from newspaper.views import get_news_list, get_premium_news, stripe_config, checkout_session, success, cancel, premium_news_success

urlpatterns = [
    url(r'^$', get_news_list, name='home'),
    url(r'^premium/$', get_premium_news, name='premium'),
    url(r'^config/$', stripe_config, name='config'),
    url(r'^checkout/$', checkout_session, name='checkout'),

    url(r'^success/$', success),
    url(r'^cancelled/$', cancel),
    url(r'^premiumNewsSuccess/$', premium_news_success),
]
