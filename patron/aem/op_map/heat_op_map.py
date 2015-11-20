
# op map for heat.
op_map = \
{(8004, '/v1', '/resource_types', 'GET', ''): ('list_resource_types',),
 (8004, '/v1', '/resource_types/%NAME%', 'GET', ''): ('resource_schema',),
 (8004, '/v1', '/resource_types/%NAME%/template', 'GET', ''): ('generate_template',),
 (8004, '/v1', '/software_configs', 'POST', ''): ('create',),
 (8004, '/v1', '/software_configs/%UUID%', 'DELETE', ''): ('delete',),
 (8004, '/v1', '/software_configs/%UUID%', 'GET', ''): ('show',),
 (8004, '/v1', '/software_deployments', 'GET', ''): ('index',),
 (8004, '/v1', '/software_deployments', 'POST', ''): ('create',),
 (8004, '/v1', '/software_deployments/%NAME%/%NAME%', 'GET', ''): ('metadata',),
 (8004, '/v1', '/software_deployments/%UUID%', 'DELETE', ''): ('delete',),
 (8004, '/v1', '/software_deployments/%UUID%', 'GET', ''): ('show',),
 (8004, '/v1', '/software_deployments/%UUID%', 'PUT', ''): ('update',),
 (8004, '/v1', '/stacks', 'GET', ''): ('index',),
 (8004, '/v1', '/stacks', 'POST', ''): ('create',),
 (8004, '/v1', '/stacks/%NAME%', 'GET', ''): (),
 (8004, '/v1', '/stacks/%NAME%/%UUID%', 'DELETE', ''): ('delete',),
 (8004, '/v1', '/stacks/%NAME%/%UUID%', 'GET', ''): ('show',),
 (8004, '/v1', '/stacks/%NAME%/%UUID%/actions', 'POST', ''): ('action',),
 (8004, '/v1', '/stacks/%NAME%/%UUID%/events', 'GET', ''): ('index',),
 (8004, '/v1', '/stacks/%NAME%/%UUID%/resources', 'GET', ''): ('index',),
 (8004, '/v1', '/stacks/%NAME%/%UUID%/resources/%NAME%', 'GET', ''): ('show',),
 (8004, '/v1', '/stacks/%NAME%/%UUID%/resources/%NAME%/events', 'GET', ''): ('index',),
 (8004, '/v1', '/stacks/%NAME%/%UUID%/resources/%NAME%/events/%UUID%', 'GET', ''): ('show',),
 (8004, '/v1', '/stacks/%NAME%/%UUID%/resources/%NAME%/metadata', 'GET', ''): ('metadata',),
 (8004, '/v1', '/stacks/%NAME%/%UUID%/template', 'GET', ''): ('template',),
 (8004, '/v1', '/stacks/%UUID%', 'GET', ''): (),
 (8004, '/v1', '/validate', 'POST', ''): ('validate_template',)}