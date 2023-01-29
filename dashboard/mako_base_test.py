from django.views.generic import View
from libs.base_render import render_to_response


class Base(View):
    def get(self, request):
        data = {'info': 'This is a test!'}
        return render_to_response(request, 'dashboard/mako_base_test.html', data)
