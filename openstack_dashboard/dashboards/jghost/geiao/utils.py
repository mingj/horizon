__author__ = 'geiao'

from openstack_dashboard import api


def get_instances_data(request):
    instances = api.nova.server_list(request, all_tenants=True)

    # Get the useful data... thanks Nova :-P
    # if instances:
    #     correlate_flavors(request, instances)
    #     correlate_tenants(request, instances)
    #     correlate_users(request, instances)
    #     calculate_ages(instances)

    return instances