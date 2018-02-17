from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

decorators = [login_required, ]


@method_decorator(decorators, name='dispatch')
class DashboardView(generic.TemplateView):
    template_name = 'main/dashboard.html'
