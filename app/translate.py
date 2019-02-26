# import json
import json
import requests
from flask import current_app
from flask_babel import _


def translate(text, dest_language):
    if 'YA_KEY' not in current_app.config or \
            not current_app.config['YA_KEY']:
        return _('Error: the translation service is not configured.')
    r = requests.get(
        'https://translate.yandex.net/api/v1.5/tr.json/translate'
        '?key={}&text={}&lang={}&options=1'.format(current_app.config['YA_KEY'], text, dest_language))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return r.json()['text'][0]