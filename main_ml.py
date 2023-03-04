import json
from transformers import pipeline


def lambda_handler(event, context):
    """Classifies the sentiment of a phrase received in the event payload.
    :param event: input event received
    :param context: context for the function
    :return: dict with status and message
    """
    if not event.get('phrase'):
        status = 400
        response = "No phrase to classify"
    else:
        pipe = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
        response = pipe(event['phrase'])
        status = 200
    return {
        'statusCode': status,
        'body': json.dumps(response)
    }