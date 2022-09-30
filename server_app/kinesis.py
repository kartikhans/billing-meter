import json, boto3

from decouple import config

KINESIS_REGION_NAME = config('AWS_REGION')


class KinesisStream(object):

    def __init__(self, stream):
        self.stream = stream

    def _connected_client(self):
        """ Connect to Kinesis Streams """
        return boto3.client('firehose',
                            region_name=KINESIS_REGION_NAME,
                            aws_access_key_id=config('AWS_ACCESS_KEY'),
                            aws_secret_access_key=config('AWS_SECRET_KEY'))

    def send_stream(self, data):
        """
        data: python dict containing your data.
        """
        client = self._connected_client()
        k = client.put_record(
            DeliveryStreamName=self.stream,
            Record={'Data': json.dumps(data)},
        )
        return k.get('ResponseMetadata', {}).get('HTTPStatusCode')
