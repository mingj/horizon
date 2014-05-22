from django.utils.translation import ugettext_lazy as _

from horizon import tables
from horizon import tabs
from horizon import exceptions
import  json
from django import http
from .tables import GeiaoInstancesTable
from .tabs import JghostTabs
from openstack_dashboard.dashboards.jghost.geiao import utils

class IndexView(tabs.TabbedTableView):
    tab_group_class = JghostTabs
    table_class = GeiaoInstancesTable
    template_name = 'jghost/geiao/index.html'

    def get_data(self, request, *args, **kwargs):
        if self.request.is_ajax() and self.request.GET.get("json", False):
            try:
                # instances = utils.get_instances_data(self.request)
                # Uncomment the following line to use fake test data.
                instances = utils.get_fake_instances_data(self.request)
            except:
                instances = []
                exceptions.handle(request,
                                  _('Unable to retrieve instance list.'))
            data = json.dumps([i._apiresource._info for i in instances])
            return http.HttpResponse(data)
        else:
            return super(IndexView, self).get(request, *args, **kwargs)
