from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.jghost import dashboard


class Geiao(horizon.Panel):
    name = _("Geiao")
    slug = "geiao"


dashboard.Jghost.register(Geiao)


