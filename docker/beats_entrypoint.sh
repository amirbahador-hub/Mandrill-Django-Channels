echo "--> Starting beats process"
celery -A workgenius.tasks worker -l info --without-gossip --without-mingle --without-heartbeat
