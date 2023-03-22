from django.core.cache import cache


def get_events():
    return cache.keys("*")