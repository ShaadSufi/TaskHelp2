from django.http import HttpResponse
import json


class ResponseNotFound(HttpResponse):
    def __init__(self, *args, **kwargs):
        content = kwargs.get('content', None)
        if content is None:
            raise Exception("not a valid response")
        js_content = json.dumps(content)
        kwargs.pop('content')
        super().__init__(content_type='json/application', status=404, content=js_content, *args, **kwargs)

class ResponseNotAuth(HttpResponse):
    def __init__(self, *args, **kwargs):
        content = kwargs.get('content', None)
        if content is None:
            raise Exception("not a valid response")
        js_content = json.dumps(content)
        kwargs.pop('content')
        super().__init__(content_type='json/application', status=401, content=js_content, *args, **kwargs)