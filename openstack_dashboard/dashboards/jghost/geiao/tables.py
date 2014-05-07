__author__ = 'geiao'

from django.utils.translation import ugettext_lazy as _


# from horizon import tables
#
#
# class GeiaoInstancesTable(tables.DataTable):
#     host = tables.Column("OS-EXT-SRV-ATTR:host",verbose_name=_("Host"))
#     tenant = tables.Column('tenant_name', verbose_name=_("Tenant"))
#     user = tables.Column('user_name', verbose_name=_("user"))
#     vcpus = tables.Column('flavor_vcpus', verbose_name=_("VCPUs"))
#     memory = tables.Column('flavor_memory', verbose_name=_("Memory"))
#     age = tables.Column('age', verbose_name=_("Age"))
#
#
#     class Meta:
#         name = "instance"
#         verbose_name = _("Instance")