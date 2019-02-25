# import json
import requests

from flask_babel import _

from app import app


def translate(text, dest_language):
    if 'YA_KEY' not in app.config or \
            not app.config['YA_KEY']:
        return _('Error: the translation service is not configured.')
    r = requests.get(
        'https://translate.yandex.net/api/v1.5/tr.json/translate'
        '?key={}&text={}&lang={}&options=1'.format(app.config['YA_KEY'], text, dest_language))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return r.json()['text'][0]