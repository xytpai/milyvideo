from mako.lookup import TemplateLookup
from django.template import RequestContext
from django.conf import settings
from django.template.context import Context
from django.http import HttpResponse


def render_to_response(request, template, data=None):
    '''How to use?
    data = {'name': 'Tom', 'age': 20}
    retrun render_to_response(request, 'index.html', data)
    -> Html: <body>${name}, ${age}</body>
    -> Html: <%! from django.conf import settings %>
    -> Html:  <body>${settings.TEMPLATES[0]['DIRS'][0]}</body>
    '''
    context_instance = RequestContext(request)
    lookup = TemplateLookup(
        directories=[settings.TEMPLATES[0]['DIRS'][0]],
        output_encoding='utf-8',
        input_encoding='utf-8',
    )
    mako_template = lookup.get_template(template)
    if not data:
        data = {}
    if context_instance:
        context_instance.update(data)
    else:
        context_instance = Context(data)
    result = {}
    for d in context_instance:
        result.update(d)
    result['csrf_token'] = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(
        request.META.get('CSRF_COOKIE', ''))
    return HttpResponse(mako_template.render(**result))
