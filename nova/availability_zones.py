begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#    a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#    under the License.'
nl|'\n'
nl|'\n'
string|'"""Availability zone helper functions."""'
newline|'\n'
nl|'\n'
name|'import'
name|'collections'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'memorycache'
newline|'\n'
nl|'\n'
comment|"# NOTE(vish): azs don't change that often, so cache them for an hour to"
nl|'\n'
comment|'#             avoid hitting the db multiple times on every request.'
nl|'\n'
DECL|variable|AZ_CACHE_SECONDS
name|'AZ_CACHE_SECONDS'
op|'='
number|'60'
op|'*'
number|'60'
newline|'\n'
DECL|variable|MC
name|'MC'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|variable|availability_zone_opts
name|'availability_zone_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'internal_service_availability_zone'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'internal'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The availability_zone to show internal services under'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_availability_zone'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Default compute node availability_zone'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'availability_zone_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_cache
name|'def'
name|'_get_cache'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'MC'
newline|'\n'
nl|'\n'
name|'if'
name|'MC'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'MC'
op|'='
name|'memorycache'
op|'.'
name|'get_client'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'MC'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|reset_cache
dedent|''
name|'def'
name|'reset_cache'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Reset the cache, mainly for testing purposes and update\n    availability_zone for host aggregate\n    """'
newline|'\n'
nl|'\n'
name|'global'
name|'MC'
newline|'\n'
nl|'\n'
name|'MC'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_make_cache_key
dedent|''
name|'def'
name|'_make_cache_key'
op|'('
name|'host'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|'"azcache-%s"'
op|'%'
name|'host'
op|'.'
name|'encode'
op|'('
string|"'utf-8'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_build_metadata_by_host
dedent|''
name|'def'
name|'_build_metadata_by_host'
op|'('
name|'aggregates'
op|','
name|'hosts'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'hosts'
name|'and'
name|'not'
name|'isinstance'
op|'('
name|'hosts'
op|','
name|'set'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hosts'
op|'='
name|'set'
op|'('
name|'hosts'
op|')'
newline|'\n'
dedent|''
name|'metadata'
op|'='
name|'collections'
op|'.'
name|'defaultdict'
op|'('
name|'set'
op|')'
newline|'\n'
name|'for'
name|'aggregate'
name|'in'
name|'aggregates'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'host'
name|'in'
name|'aggregate'
op|'.'
name|'hosts'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'hosts'
name|'and'
name|'host'
name|'not'
name|'in'
name|'hosts'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'metadata'
op|'['
name|'host'
op|']'
op|'.'
name|'add'
op|'('
name|'aggregate'
op|'.'
name|'metadata'
op|'.'
name|'values'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_build_metadata_by_key
dedent|''
name|'def'
name|'_build_metadata_by_key'
op|'('
name|'aggregates'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'metadata'
op|'='
name|'collections'
op|'.'
name|'defaultdict'
op|'('
name|'set'
op|')'
newline|'\n'
name|'for'
name|'aggregate'
name|'in'
name|'aggregates'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'aggregate'
op|'.'
name|'metadata'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'['
name|'key'
op|']'
op|'.'
name|'add'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_availability_zones
dedent|''
name|'def'
name|'set_availability_zones'
op|'('
name|'context'
op|','
name|'services'
op|')'
op|':'
newline|'\n'
comment|"# Makes sure services isn't a sqlalchemy object"
nl|'\n'
indent|'    '
name|'services'
op|'='
op|'['
name|'dict'
op|'('
name|'service'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
name|'for'
name|'service'
name|'in'
name|'services'
op|']'
newline|'\n'
name|'hosts'
op|'='
name|'set'
op|'('
op|'['
name|'service'
op|'['
string|"'host'"
op|']'
name|'for'
name|'service'
name|'in'
name|'services'
op|']'
op|')'
newline|'\n'
name|'aggregates'
op|'='
name|'objects'
op|'.'
name|'AggregateList'
op|'.'
name|'get_by_metadata_key'
op|'('
name|'context'
op|','
nl|'\n'
string|"'availability_zone'"
op|','
name|'hosts'
op|'='
name|'hosts'
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'_build_metadata_by_host'
op|'('
name|'aggregates'
op|','
name|'hosts'
op|'='
name|'hosts'
op|')'
newline|'\n'
comment|'# gather all of the availability zones associated with a service host'
nl|'\n'
name|'for'
name|'service'
name|'in'
name|'services'
op|':'
newline|'\n'
indent|'        '
name|'az'
op|'='
name|'CONF'
op|'.'
name|'internal_service_availability_zone'
newline|'\n'
name|'if'
name|'service'
op|'['
string|"'topic'"
op|']'
op|'=='
string|'"compute"'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'metadata'
op|'.'
name|'get'
op|'('
name|'service'
op|'['
string|"'host'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'az'
op|'='
string|"u','"
op|'.'
name|'join'
op|'('
name|'list'
op|'('
name|'metadata'
op|'['
name|'service'
op|'['
string|"'host'"
op|']'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'az'
op|'='
name|'CONF'
op|'.'
name|'default_availability_zone'
newline|'\n'
comment|'# update the cache'
nl|'\n'
name|'update_host_availability_zone_cache'
op|'('
name|'context'
op|','
nl|'\n'
name|'service'
op|'['
string|"'host'"
op|']'
op|','
name|'az'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'service'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'az'
newline|'\n'
dedent|''
name|'return'
name|'services'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_host_availability_zone
dedent|''
name|'def'
name|'get_host_availability_zone'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'conductor_api'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'conductor_api'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
name|'conductor_api'
op|'.'
name|'aggregate_metadata_get_by_host'
op|'('
nl|'\n'
name|'context'
op|','
name|'host'
op|','
name|'key'
op|'='
string|"'availability_zone'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'aggregates'
op|'='
name|'objects'
op|'.'
name|'AggregateList'
op|'.'
name|'get_by_host'
op|'('
name|'context'
op|','
name|'host'
op|','
nl|'\n'
name|'key'
op|'='
string|"'availability_zone'"
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'_build_metadata_by_key'
op|'('
name|'aggregates'
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'availability_zone'"
name|'in'
name|'metadata'
op|':'
newline|'\n'
indent|'        '
name|'az'
op|'='
name|'list'
op|'('
name|'metadata'
op|'['
string|"'availability_zone'"
op|']'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'az'
op|'='
name|'CONF'
op|'.'
name|'default_availability_zone'
newline|'\n'
dedent|''
name|'return'
name|'az'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|update_host_availability_zone_cache
dedent|''
name|'def'
name|'update_host_availability_zone_cache'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'availability_zone'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'availability_zone'
op|':'
newline|'\n'
indent|'        '
name|'availability_zone'
op|'='
name|'get_host_availability_zone'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
dedent|''
name|'cache'
op|'='
name|'_get_cache'
op|'('
op|')'
newline|'\n'
name|'cache_key'
op|'='
name|'_make_cache_key'
op|'('
name|'host'
op|')'
newline|'\n'
name|'cache'
op|'.'
name|'delete'
op|'('
name|'cache_key'
op|')'
newline|'\n'
name|'cache'
op|'.'
name|'set'
op|'('
name|'cache_key'
op|','
name|'availability_zone'
op|','
name|'AZ_CACHE_SECONDS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_availability_zones
dedent|''
name|'def'
name|'get_availability_zones'
op|'('
name|'context'
op|','
name|'get_only_available'
op|'='
name|'False'
op|','
nl|'\n'
name|'with_hosts'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return available and unavailable zones on demand.\n\n        :param get_only_available: flag to determine whether to return\n            available zones only, default False indicates return both\n            available zones and not available zones, True indicates return\n            available zones only\n        :param with_hosts: whether to return hosts part of the AZs\n        :type with_hosts: bool\n    """'
newline|'\n'
name|'enabled_services'
op|'='
name|'objects'
op|'.'
name|'ServiceList'
op|'.'
name|'get_all'
op|'('
name|'context'
op|','
name|'disabled'
op|'='
name|'False'
op|')'
newline|'\n'
name|'enabled_services'
op|'='
name|'set_availability_zones'
op|'('
name|'context'
op|','
name|'enabled_services'
op|')'
newline|'\n'
nl|'\n'
name|'available_zones'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
op|'('
name|'zone'
op|','
name|'host'
op|')'
name|'in'
op|'['
op|'('
name|'service'
op|'['
string|"'availability_zone'"
op|']'
op|','
name|'service'
op|'['
string|"'host'"
op|']'
op|')'
nl|'\n'
name|'for'
name|'service'
name|'in'
name|'enabled_services'
op|']'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'with_hosts'
name|'and'
name|'zone'
name|'not'
name|'in'
name|'available_zones'
op|':'
newline|'\n'
indent|'            '
name|'available_zones'
op|'.'
name|'append'
op|'('
name|'zone'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'with_hosts'
op|':'
newline|'\n'
indent|'            '
name|'_available_zones'
op|'='
name|'dict'
op|'('
name|'available_zones'
op|')'
newline|'\n'
name|'zone_hosts'
op|'='
name|'_available_zones'
op|'.'
name|'setdefault'
op|'('
name|'zone'
op|','
name|'set'
op|'('
op|')'
op|')'
newline|'\n'
name|'zone_hosts'
op|'.'
name|'add'
op|'('
name|'host'
op|')'
newline|'\n'
comment|'# .items() returns a view in Py3, casting it to list for Py2 compat'
nl|'\n'
name|'available_zones'
op|'='
name|'list'
op|'('
name|'_available_zones'
op|'.'
name|'items'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'get_only_available'
op|':'
newline|'\n'
indent|'        '
name|'disabled_services'
op|'='
name|'objects'
op|'.'
name|'ServiceList'
op|'.'
name|'get_all'
op|'('
name|'context'
op|','
name|'disabled'
op|'='
name|'True'
op|')'
newline|'\n'
name|'disabled_services'
op|'='
name|'set_availability_zones'
op|'('
name|'context'
op|','
name|'disabled_services'
op|')'
newline|'\n'
name|'not_available_zones'
op|'='
op|'['
op|']'
newline|'\n'
name|'azs'
op|'='
name|'available_zones'
name|'if'
name|'not'
name|'with_hosts'
name|'else'
name|'dict'
op|'('
name|'available_zones'
op|')'
newline|'\n'
name|'zones'
op|'='
op|'['
op|'('
name|'service'
op|'['
string|"'availability_zone'"
op|']'
op|','
name|'service'
op|'['
string|"'host'"
op|']'
op|')'
nl|'\n'
name|'for'
name|'service'
name|'in'
name|'disabled_services'
nl|'\n'
name|'if'
name|'service'
op|'['
string|"'availability_zone'"
op|']'
name|'not'
name|'in'
name|'azs'
op|']'
newline|'\n'
name|'for'
op|'('
name|'zone'
op|','
name|'host'
op|')'
name|'in'
name|'zones'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'with_hosts'
name|'and'
name|'zone'
name|'not'
name|'in'
name|'not_available_zones'
op|':'
newline|'\n'
indent|'                '
name|'not_available_zones'
op|'.'
name|'append'
op|'('
name|'zone'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'with_hosts'
op|':'
newline|'\n'
indent|'                '
name|'_not_available_zones'
op|'='
name|'dict'
op|'('
name|'not_available_zones'
op|')'
newline|'\n'
name|'zone_hosts'
op|'='
name|'_not_available_zones'
op|'.'
name|'setdefault'
op|'('
name|'zone'
op|','
name|'set'
op|'('
op|')'
op|')'
newline|'\n'
name|'zone_hosts'
op|'.'
name|'add'
op|'('
name|'host'
op|')'
newline|'\n'
comment|'# .items() returns a view in Py3, casting it to list for Py2'
nl|'\n'
comment|'#   compat'
nl|'\n'
name|'not_available_zones'
op|'='
name|'list'
op|'('
name|'_not_available_zones'
op|'.'
name|'items'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
op|'('
name|'available_zones'
op|','
name|'not_available_zones'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'available_zones'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instance_availability_zone
dedent|''
dedent|''
name|'def'
name|'get_instance_availability_zone'
op|'('
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return availability zone of specified instance."""'
newline|'\n'
name|'host'
op|'='
name|'str'
op|'('
name|'instance'
op|'.'
name|'get'
op|'('
string|"'host'"
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'host'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'cache_key'
op|'='
name|'_make_cache_key'
op|'('
name|'host'
op|')'
newline|'\n'
name|'cache'
op|'='
name|'_get_cache'
op|'('
op|')'
newline|'\n'
name|'az'
op|'='
name|'cache'
op|'.'
name|'get'
op|'('
name|'cache_key'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'az'
op|':'
newline|'\n'
indent|'        '
name|'elevated'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'az'
op|'='
name|'get_host_availability_zone'
op|'('
name|'elevated'
op|','
name|'host'
op|')'
newline|'\n'
name|'cache'
op|'.'
name|'set'
op|'('
name|'cache_key'
op|','
name|'az'
op|','
name|'AZ_CACHE_SECONDS'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'az'
newline|'\n'
dedent|''
endmarker|''
end_unit
