from django.utils.translation import ugettext_lazy as _

import horizon


class Jghost(horizon.Dashboard):
    name = _("Jghost")
    slug = "jghost"
    panels = ('geiao',)  # Add your panels here.
    default_panel = 'geiao'  # Specify the slug of the dashboard's default panel.


horizon.register(Jghost)
