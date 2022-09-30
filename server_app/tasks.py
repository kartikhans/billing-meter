from celery import current_app
import boto3
from django.core.cache import cache
from .kinesis import KinesisStream
import logging

log = logging.getLogger(__name__)

CELERY_DEFAULT_MAX_RETRIES = 10
CELERY_DEFAULT_RETRY_DELAY_IN_SECONDS = 120  # 2 minutes
STREAM = 'zenskar-stream'

kinesis_client = boto3.client('kinesis', region_name='ap-south-1')


class BillMetering(current_app.Task):
    name = "server_app.tasks.BillMetering"
    acks_late = True
    max_retries = CELERY_DEFAULT_MAX_RETRIES
    default_retry_delay = CELERY_DEFAULT_RETRY_DELAY_IN_SECONDS

    def run(self, *args, **kwargs):
        try:
            if not cache.get(kwargs.get('uniqueKey')):
                status = KinesisStream(stream=STREAM).send_stream(data=kwargs)
                if status == 200:
                    cache.set(kwargs.get('uniqueKey'), kwargs.get('bytes'), 3600 * 24)
                else:
                    self.retry()
                log.info(f"{kwargs.get('uniqueKey')} new key created")
            else:
                log.info(f"{kwargs.get('uniqueKey')} key already present")
        except Exception as e:
            self.retry()
            raise e


current_app.register_task(BillMetering)
