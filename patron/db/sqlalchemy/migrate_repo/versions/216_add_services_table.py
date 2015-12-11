# Copyright 2015 OpenStack
# All Rights Reserved
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

from oslo_log import log as logging
from migrate.changeset import UniqueConstraint
from sqlalchemy import MetaData, Table
from sqlalchemy import Boolean, BigInteger, Column, DateTime, Enum, Float
from sqlalchemy import ForeignKey, Index, Integer, MetaData, String, Table

from patron.i18n import _LE

LOG = logging.getLogger(__name__)

# def _populate_services(services):
#     default_inst_types = {
#         1: dict(created_at = DateTime(), updated_at = DateTime(), host)
#         'm1.tiny': dict(mem=512, vcpus=1, root_gb=1, eph_gb=0, flavid=1),
#         'm1.small': dict(mem=2048, vcpus=1, root_gb=20, eph_gb=0, flavid=2),
#         'm1.medium': dict(mem=4096, vcpus=2, root_gb=40, eph_gb=0, flavid=3),
#         'm1.large': dict(mem=8192, vcpus=4, root_gb=80, eph_gb=0, flavid=4),
#         'm1.xlarge': dict(mem=16384, vcpus=8, root_gb=160, eph_gb=0, flavid=5)
#         }
#
#     try:
#         i = services.insert()
#         for name, values in default_inst_types.iteritems():
#             i.execute({'name': name, 'memory_mb': values["mem"],
#                         'vcpus': values["vcpus"], 'deleted': 0,
#                         'root_gb': values["root_gb"],
#                         'ephemeral_gb': values["eph_gb"],
#                         'rxtx_factor': 1,
#                         'swap': 0,
#                         'flavorid': values["flavid"],
#                         'disabled': False,
#                         'is_public': True})
#     except Exception:
#         LOG.info(repr(services))
#         LOG.exception(_LE('Exception while seeding services table'))
#         raise

def upgrade(migrate_engine):
    """Function creates services table."""
    meta = MetaData(bind=migrate_engine)

    services = Table('services', meta,
        Column('created_at', DateTime),
        Column('updated_at', DateTime),
        Column('deleted_at', DateTime),
        Column('id', Integer, primary_key=True, nullable=False),
        Column('host', String(length=255)),
        Column('binary', String(length=255)),
        Column('topic', String(length=255)),
        Column('report_count', Integer, nullable=False),
        Column('disabled', Boolean),
        Column('deleted', Integer),
        Column('disabled_reason', String(length=255)),
        mysql_engine='InnoDB',
        mysql_charset='utf8'
    )

    # create all tables
    tables = [services]

    for table in tables:
        try:
            table.create()
        except Exception:
            LOG.info(repr(table))
            LOG.exception(_LE('Exception while creating table.'))
            raise

    # services
    UniqueConstraint('host', 'topic', 'deleted',
                     table=services,
                     name='uniq_services0host0topic0deleted').create()
    UniqueConstraint('host', 'binary', 'deleted',
                     table=services,
                     name='uniq_services0host0binary0deleted').create()

    # populate initial instance types
    # _populate_services(services)


def downgrade(migrate_engine):
    """Function drops services table"""
    meta = MetaData(bind=migrate_engine)
    meta.reflect(migrate_engine)

    table_names = ['services']
    for table_name in table_names:
        table = Table(table_name, meta)
        table.drop(checkfirst=True)
