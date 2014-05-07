from django.utils.translation import ugettext_lazy as _

import horizon



class InstanceJghost(horizon.PanelGroup):
    name = _("Instance Jghost")
    slug = "instance_jghost"
    panels = ('geiao',)




class Jghost(horizon.Dashboard):
    name = _("Jghost")
    slug = "jghost"
    panels = (InstanceJghost,)  # Add your panels here.
    default_panel = 'geiao'  # Specify the slug of the dashboard's default panel.


horizon.register(Jghost)
