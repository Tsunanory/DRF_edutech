import re
from django.core.exceptions import ValidationError


class YoutubeLinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, attrs):
        value = attrs.get(self.field)
        youtube_regex = r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$'
        if value and not re.match(youtube_regex, value):
            raise ValidationError({self.field: 'Invalid URL. Only YouTube links are allowed.'})
