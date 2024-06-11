import re
from django.core.exceptions import ValidationError


def validate_youtube_link(value):
    youtube_regex = (
        r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$'
    )
    if not re.match(youtube_regex, value):
        raise ValidationError('Invalid URL. Only YouTube links are allowed.')
