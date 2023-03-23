from django.core.cache import cache


def get_events() -> list[str]:
    return cache.keys("*")