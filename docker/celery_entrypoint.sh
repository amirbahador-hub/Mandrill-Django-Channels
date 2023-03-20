echo "--> Starting celery process"
celery -A workgenius.tasks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
