# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_config import cfg
from oslo_config import fixture as config_fixture

from patron import config
from patron import ipv6
from patron import paths
from patron.tests.unit import utils

CONF = cfg.CONF
CONF.import_opt('use_ipv6', 'patron.netconf')
CONF.import_opt('host', 'patron.netconf')
CONF.import_opt('scheduler_driver', 'patron.scheduler.manager')
CONF.import_opt('fake_network', 'patron.network.linux_net')
CONF.import_opt('network_size', 'patron.network.manager')
CONF.import_opt('num_networks', 'patron.network.manager')
CONF.import_opt('floating_ip_dns_manager', 'patron.network.floating_ips')
CONF.import_opt('instance_dns_manager', 'patron.network.floating_ips')
CONF.import_opt('policy_file', 'patron.openstack.common.policy')
CONF.import_opt('compute_driver', 'patron.virt.driver')
CONF.import_opt('api_paste_config', 'patron.wsgi')


class ConfFixture(config_fixture.Config):
    """Fixture to manage global conf settings."""
    def setUp(self):
        super(ConfFixture, self).setUp()
        self.conf.set_default('api_paste_config',
                              paths.state_path_def('etc/patron/api-paste.ini'))
        self.conf.set_default('host', 'fake-mini')
        self.conf.set_default('compute_driver',
                              'patron.virt.fake.SmallFakeDriver')
        self.conf.set_default('fake_network', True)
        self.conf.set_default('flat_network_bridge', 'br100')
        self.conf.set_default('floating_ip_dns_manager',
                              'patron.tests.unit.utils.dns_manager')
        self.conf.set_default('instance_dns_manager',
                              'patron.tests.unit.utils.dns_manager')
        self.conf.set_default('network_size', 8)
        self.conf.set_default('num_networks', 2)
        self.conf.set_default('use_ipv6', True)
        self.conf.set_default('vlan_interface', 'eth0')
        self.conf.set_default('auth_strategy', 'noauth2')
        config.parse_args([], default_config_files=[])
        self.conf.set_default('connection', "sqlite://", group='database')
        self.conf.set_default('connection', "sqlite://", group='api_database')
        self.conf.set_default('sqlite_synchronous', False, group='database')
        self.conf.set_default('sqlite_synchronous', False,
                group='api_database')
        self.conf.set_default('fatal_exception_format_errors', True)
        self.conf.set_default('enabled', True, 'osapi_v3')
        self.conf.set_default('force_dhcp_release', False)
        self.conf.set_default('periodic_enable', False)
        self.addCleanup(utils.cleanup_dns_managers)
        self.addCleanup(ipv6.api.reset_backend)
