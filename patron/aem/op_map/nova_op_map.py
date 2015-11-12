
# op map for nova.
op_map = \
{(8774, '/v2', '/extensions', 'GET', ''): (),
 (8774, '/v2', '/extensions/os-consoles', 'GET', ''): (),
 (8774, '/v2', '/flavors', 'GET', ''): (),
 (8774, '/v2', '/flavors', 'POST', ''): ('compute_extension:flavormanage',
                                         'compute_extension:flavor_swap',
                                         'compute_extension:flavor_rxtx',
                                         'compute_extension:flavor_access',
                                         'compute_extension:flavorextradata',
                                         'compute_extension:flavor_disabled'),
 (8774, '/v2', '/flavors/%NAME%', 'DELETE', ''): ('compute_extension:flavormanage',),
 (8774, '/v2', '/flavors/%NAME%', 'GET', ''): ('compute_extension:flavor_swap',
                                               'compute_extension:flavor_rxtx',
                                               'compute_extension:flavor_access',
                                               'compute_extension:flavorextradata',
                                               'compute_extension:flavor_disabled'),
 (8774, '/v2', '/flavors/%NAME%/action', 'POST', 'addTenantAccess'): ('compute_extension:flavor_access:addTenantAccess',),
 (8774, '/v2', '/flavors/%NAME%/action', 'POST', 'removeTenantAccess'): ('compute_extension:flavor_access:removeTenantAccess',),
 (8774, '/v2', '/flavors/%NAME%/os-extra_specs', 'GET', ''): ('compute_extension:flavorextraspecs:index',),
 (8774, '/v2', '/flavors/%NAME%/os-extra_specs', 'POST', ''): ('compute_extension:flavorextraspecs:create',),
 (8774, '/v2', '/flavors/%NAME%/os-extra_specs/%NAME%', 'DELETE', ''): ('compute_extension:flavorextraspecs:delete',),
 (8774, '/v2', '/flavors/%NAME%/os-extra_specs/%NAME%', 'GET', ''): ('compute_extension:flavorextraspecs:show',),
 (8774, '/v2', '/flavors/%NAME%/os-extra_specs/%NAME%', 'PUT', ''): ('compute_extension:flavorextraspecs:update',),
 (8774, '/v2', '/flavors/%NAME%/os-flavor-access', 'GET', ''): ('compute_extension:flavor_access',),
 (8774, '/v2', '/flavors/%UUID%', 'DELETE', ''): ('compute_extension:flavormanage',),
 (8774, '/v2', '/flavors/%UUID%', 'GET', ''): ('compute_extension:flavor_swap',
                                               'compute_extension:flavor_rxtx',
                                               'compute_extension:flavor_access',
                                               'compute_extension:flavorextradata',
                                               'compute_extension:flavor_disabled'),
 (8774, '/v2', '/flavors/detail', 'GET', ''): ('compute_extension:flavor_swap',
                                               'compute_extension:flavor_rxtx',
                                               'compute_extension:flavor_access',
                                               'compute_extension:flavorextradata',
                                               'compute_extension:flavor_disabled'),
 (8774, '/v2', '/flavors?limit=%VALUE%', 'GET', ''): (),
 (8774, '/v2', '/flavors?marker=%VALUE%', 'GET', ''): (),
 (8774, '/v2', '/flavors?minDisk=%VALUE%', 'GET', ''): (),
 (8774, '/v2', '/flavors?minRam=%VALUE%', 'GET', ''): (),
 (8774, '/v2', '/images', 'DELETE', ''): (),
 (8774, '/v2', '/images', 'GET', ''): (),
 (8774, '/v2', '/images/%NAME%', 'DELETE', ''): (),
 (8774, '/v2', '/images/%NAME%', 'GET', ''): (),
 (8774, '/v2', '/images/%UUID%', 'DELETE', ''): (),
 (8774, '/v2', '/images/%UUID%', 'GET', ''): (),
 (8774, '/v2', '/images/%UUID%/metadata', 'GET', ''): (),
 (8774, '/v2', '/images/%UUID%/metadata', 'POST', ''): (),
 (8774, '/v2', '/images/%UUID%/metadata', 'PUT', ''): (),
 (8774, '/v2', '/images/%UUID%/metadata/os_distro', 'DELETE', ''): (),
 (8774, '/v2', '/images/%UUID%/metadata/os_distro', 'GET', ''): (),
 (8774, '/v2', '/images/%UUID%/metadata/os_distro', 'PUT', ''): (),
 (8774, '/v2', '/images/%UUID%/metadata/os_version', 'DELETE', ''): (),
 (8774, '/v2', '/images/%UUID%/metadata/os_version', 'GET', ''): (),
 (8774, '/v2', '/images/%UUID%/metadata/os_version', 'PUT', ''): (),
 (8774, '/v2', '/images/detail', 'GET', ''): ('compute_extension:image_size',
                                              'compute_extension:disk_config'),
 (8774, '/v2', '/limits', 'GET', ''): (),
 (8774, '/v2', '/os-agents', 'GET', ''): ('compute_extension:agents',),
 (8774, '/v2', '/os-agents', 'POST', ''): ('compute_extension:agents',),
 (8774, '/v2', '/os-agents/%NAME%', 'DELETE', ''): ('compute_extension:agents',),
 (8774, '/v2', '/os-agents/%NAME%', 'PUT', ''): ('compute_extension:agents',),
 (8774, '/v2', '/os-agents?hypervisor=%VALUE%', 'GET', ''): ('compute_extension:agents',),
 (8774, '/v2', '/os-aggregates', 'GET', ''): ('compute_extension:aggregates',),
 (8774, '/v2', '/os-aggregates', 'POST', ''): ('compute_extension:aggregates',),
 (8774, '/v2', '/os-aggregates/%NAME%', 'DELETE', ''): ('compute_extension:aggregates',),
 (8774, '/v2', '/os-aggregates/%NAME%', 'GET', ''): ('compute_extension:aggregates',),
 (8774, '/v2', '/os-aggregates/%NAME%', 'PUT', ''): ('compute_extension:aggregates',),
 (8774, '/v2', '/os-aggregates/%NAME%/action', 'POST', 'host'): ('compute_extension:aggregates',),
 (8774, '/v2', '/os-aggregates/%NAME%/action', 'POST', 'metadata'): ('compute_extension:aggregates',),
 (8774, '/v2', '/os-availability-zone', 'GET', ''): ('compute_extension:availability_zone:list',),
 (8774, '/v2', '/os-availability-zone/detail', 'GET', ''): ('compute_extension:availability_zone:detail',),
 (8774, '/v2', '/os-certificates', 'POST', ''): ('compute_extension:certificates',),
 (8774, '/v2', '/os-certificates/root', 'GET', ''): ('compute_extension:certificates',),
 (8774, '/v2', '/os-floating-ips', 'POST', ''): ('compute_extension:floating_ips',),
 (8774, '/v2', '/os-floating-ips-bulk', 'GET', ''): ('compute_extension:floating_ips_bulk',),
 (8774, '/v2', '/os-floating-ips-bulk', 'POST', ''): ('compute_extension:floating_ips_bulk',),
 (8774, '/v2', '/os-floating-ips-bulk/delete', 'PUT', ''): ('compute_extension:floating_ips_bulk',),
 (8774, '/v2', '/os-floating-ips/%UUID%', 'GET', ''): ('compute_extension:floating_ips',),
 (8774, '/v2', '/os-hosts', 'GET', ''): ('compute_extension:hosts',),
 (8774, '/v2', '/os-hosts/%NAME%', 'GET', ''): (),
 (8774, '/v2', '/os-hosts/%NAME%', 'PUT', ''): ('compute_extension:hosts',),
 (8774, '/v2', '/os-hosts/%NAME%/reboot', 'GET', ''): ('compute_extension:hosts',),
 (8774, '/v2', '/os-hosts/%NAME%/shutdown', 'GET', ''): ('compute_extension:hosts',),
 (8774, '/v2', '/os-hosts/%NAME%/startup', 'GET', ''): ('compute_extension:hosts',),
 (8774, '/v2', '/os-hosts?zone=%VALUE%', 'GET', ''): ('compute_extension:hosts',),
 (8774, '/v2', '/os-hypervisors', 'GET', ''): ('compute_extension:hypervisors',),
 (8774, '/v2', '/os-hypervisors/%NAME%', 'GET', ''): ('compute_extension:hypervisors',),
 (8774, '/v2', '/os-hypervisors/%NAME%/search', 'GET', ''): ('compute_extension:hypervisors',),
 (8774, '/v2', '/os-hypervisors/%NAME%/servers', 'GET', ''): ('compute_extension:hypervisors',),
 (8774, '/v2', '/os-hypervisors/%NAME%/uptime', 'GET', ''): ('compute_extension:hypervisors',),
 (8774, '/v2', '/os-hypervisors/%UUID%', 'GET', ''): ('compute_extension:hypervisors',),
 (8774, '/v2', '/os-hypervisors/%UUID%/servers', 'GET', ''): ('compute_extension:hypervisors',),
 (8774, '/v2', '/os-hypervisors/%UUID%/uptime', 'GET', ''): ('compute_extension:hypervisors',),
 (8774, '/v2', '/os-hypervisors/detail', 'GET', ''): ('compute_extension:hypervisors',),
 (8774, '/v2', '/os-instance_usage_audit_log', 'GET', ''): ('compute_extension:instance_usage_audit_log',),
 (8774, '/v2', '/os-instance_usage_audit_log/%NAME%', 'GET', ''): ('compute_extension:instance_usage_audit_log',),
 (8774, '/v2', '/os-keypairs', 'GET', ''): ('compute_extension:keypairs:index',),
 (8774, '/v2', '/os-keypairs', 'POST', ''): ('compute_extension:keypairs:create',),
 (8774, '/v2', '/os-keypairs/%NAME%', 'DELETE', ''): ('compute_extension:keypairs:delete',),
 (8774, '/v2', '/os-keypairs/%NAME%', 'GET', ''): ('compute_extension:keypairs:show',),
 (8774, '/v2', '/os-migrations', 'GET', ''): ('compute_extension:migrations:index',),
 (8774, '/v2', '/os-networks', 'GET', ''): ('compute_extension:networks:view',),
 (8774, '/v2', '/os-networks/%UUID%', 'GET', ''): ('compute_extension:networks:view',),
 (8774, '/v2', '/os-quota-sets/%ID%', 'GET', ''): ('compute_extension:quotas:show',),
 (8774, '/v2', '/os-quota-sets/%ID%', 'PUT', ''): ('compute_extension:quotas:update',),
 (8774, '/v2', '/os-security-group-rules', 'POST', ''): ('compute_extension:security_groups',),
 (8774, '/v2', '/os-security-group-rules/%UUID%', 'DELETE', ''): ('compute_extension:security_groups',),
 (8774, '/v2', '/os-security-groups', 'DELETE', ''): (),
 (8774, '/v2', '/os-security-groups', 'GET', ''): ('compute_extension:security_groups',),
 (8774, '/v2', '/os-security-groups', 'POST', ''): ('compute_extension:security_groups',),
 (8774, '/v2', '/os-security-groups/%UUID%', 'DELETE', ''): ('compute_extension:security_groups',),
 (8774, '/v2', '/os-security-groups/%UUID%', 'GET', ''): ('compute_extension:security_groups',),
 (8774, '/v2', '/os-security-groups/%UUID%', 'PUT', ''): ('compute_extension:security_groups',),
 (8774, '/v2', '/os-server-groups', 'GET', ''): ('compute_extension:server_groups',),
 (8774, '/v2', '/os-server-groups', 'POST', ''): ('compute_extension:server_groups',),
 (8774, '/v2', '/os-server-groups/%UUID%', 'DELETE', ''): ('compute_extension:server_groups',),
 (8774, '/v2', '/os-server-groups/%UUID%', 'GET', ''): ('compute_extension:server_groups',),
 (8774, '/v2', '/os-services', 'GET', ''): ('compute_extension:services',),
 (8774, '/v2', '/os-services?binary=%VALUE%', 'GET', ''): ('compute_extension:services',),
 (8774, '/v2', '/os-services?binary=%VALUE%&host=%VALUE%', 'GET', ''): ('compute_extension:services',),
 (8774, '/v2', '/os-services?host=%VALUE%', 'GET', ''): ('compute_extension:services',),
 (8774, '/v2', '/os-services?xxx=%VALUE%', 'GET', ''): ('compute_extension:services',),
 (8774, '/v2', '/os-simple-tenant-usage/%ID%', 'GET', ''): ('compute_extension:simple_tenant_usage:show',),
 (8774, '/v2', '/os-simple-tenant-usage/%NAME%', 'GET', ''): (),
 (8774, '/v2', '/os-simple-tenant-usage?detailed=%VALUE%&start=%VALUE%&end=%VALUE%', 'GET', ''): ('compute_extension:simple_tenant_usage:list',),
 (8774, '/v2', '/os-tenant-networks', 'GET', ''): ('compute_extension:os-tenant-networks',),
 (8774, '/v2', '/os-tenant-networks/%UUID%', 'GET', ''): ('compute_extension:os-tenant-networks',),
 (8774, '/v2', '/servers', 'POST', ''): ('compute_extension:disk_config',
                                         'compute:create'),
 (8774, '/v2', '/servers/%ID%/action', 'POST', 'createImage'): (),
 (8774, '/v2', '/servers/%NAME%', 'POST', ''): (),
 (8774, '/v2', '/servers/%UUID%/os-virtual-interfaces', 'GET', ''): ('compute_extension:virtual_interfaces',)}

