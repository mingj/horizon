__author__ = 'geiao'

from django.utils.translation import ugettext_lazy as _

from horizon import exceptions

from horizon import tabs

from .tables import GeiaoInstancesTable
from openstack_dashboard.dashboards.jghost.geiao import utils


class JghostTab(tabs.Tab):
    name = _("Jghost..")
    slug = "jgho"
    template_name = "jghost/geiao/_flocking.html"

    def get_context_data(self, request):
        return None

class DataTab(tabs.TableTab):
    name = _("Data")
    slug = "data"
    table_classes = (GeiaoInstancesTable,)
    template_name = "horizon/common/_detail_table.html"
    preload = False

    def get_instances_data(self):
        try:
            instances = utils.get_instances_data(self.tab_group.request)
        except:
            instances = []
            exceptions.handle(self.tab_group.request,
                              _('Unable to retrieve instance list.'))
        return instances

class JghostTabs(tabs.TabGroup):
    slug = "geiao"
    tabs = (JghostTab,DataTab)
