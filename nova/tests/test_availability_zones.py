begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 Netease Corporation'
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
string|'"""\nTests for availability zones\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'availability_zones'
name|'as'
name|'az'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
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
name|'import_opt'
op|'('
string|"'internal_service_availability_zone'"
op|','
nl|'\n'
string|"'nova.availability_zones'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'default_availability_zone'"
op|','
nl|'\n'
string|"'nova.availability_zones'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AvailabilityZoneTestCases
name|'class'
name|'AvailabilityZoneTestCases'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for aggregate based availability zone."""'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'AvailabilityZoneTestCases'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
string|"'me'"
newline|'\n'
name|'self'
op|'.'
name|'availability_zone'
op|'='
string|"'nova-test'"
newline|'\n'
name|'self'
op|'.'
name|'default_az'
op|'='
name|'CONF'
op|'.'
name|'default_availability_zone'
newline|'\n'
name|'self'
op|'.'
name|'default_in_az'
op|'='
name|'CONF'
op|'.'
name|'internal_service_availability_zone'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'agg'
op|'='
name|'self'
op|'.'
name|'_create_az'
op|'('
string|"'az_agg'"
op|','
name|'self'
op|'.'
name|'availability_zone'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'aggregate_delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'agg'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'super'
op|'('
name|'AvailabilityZoneTestCases'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_az
dedent|''
name|'def'
name|'_create_az'
op|'('
name|'self'
op|','
name|'agg_name'
op|','
name|'az_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agg_meta'
op|'='
op|'{'
string|"'name'"
op|':'
name|'agg_name'
op|'}'
newline|'\n'
name|'agg'
op|'='
name|'db'
op|'.'
name|'aggregate_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'agg_meta'
op|')'
newline|'\n'
nl|'\n'
name|'metadata'
op|'='
op|'{'
string|"'availability_zone'"
op|':'
name|'az_name'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_metadata_add'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'agg'
op|'['
string|"'id'"
op|']'
op|','
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'agg'
newline|'\n'
nl|'\n'
DECL|member|_update_az
dedent|''
name|'def'
name|'_update_az'
op|'('
name|'self'
op|','
name|'aggregate'
op|','
name|'az_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
op|'{'
string|"'availability_zone'"
op|':'
name|'az_name'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'aggregate'
op|'['
string|"'id'"
op|']'
op|','
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_service_with_topic
dedent|''
name|'def'
name|'_create_service_with_topic'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'host'
op|','
name|'disabled'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'{'
nl|'\n'
string|"'binary'"
op|':'
string|"'bin'"
op|','
nl|'\n'
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'topic'"
op|':'
name|'topic'
op|','
nl|'\n'
string|"'disabled'"
op|':'
name|'disabled'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'service_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_destroy_service
dedent|''
name|'def'
name|'_destroy_service'
op|'('
name|'self'
op|','
name|'service'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'service'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_add_to_aggregate
dedent|''
name|'def'
name|'_add_to_aggregate'
op|'('
name|'self'
op|','
name|'service'
op|','
name|'aggregate'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'aggregate_host_add'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'aggregate'
op|'['
string|"'id'"
op|']'
op|','
name|'service'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_delete_from_aggregate
dedent|''
name|'def'
name|'_delete_from_aggregate'
op|'('
name|'self'
op|','
name|'service'
op|','
name|'aggregate'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'aggregate_host_delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'aggregate'
op|'['
string|"'id'"
op|']'
op|','
name|'service'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rest_availability_zone_reset_cache
dedent|''
name|'def'
name|'test_rest_availability_zone_reset_cache'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'az'
op|'.'
name|'reset_cache'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'az'
op|'.'
name|'_get_cache'
op|'('
op|')'
op|'.'
name|'get'
op|'('
string|"'cache'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_availability_zone_compute_service
dedent|''
name|'def'
name|'test_set_availability_zone_compute_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test for compute service get right availability zone."""'
newline|'\n'
name|'service'
op|'='
name|'self'
op|'.'
name|'_create_service_with_topic'
op|'('
string|"'compute'"
op|','
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
comment|'# The service is not add into aggregate, so confirm it is default'
nl|'\n'
comment|'# availability zone.'
nl|'\n'
name|'new_service'
op|'='
name|'az'
op|'.'
name|'set_availability_zones'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'services'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'new_service'
op|'['
string|"'availability_zone'"
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'default_az'
op|')'
newline|'\n'
nl|'\n'
comment|'# The service is added into aggregate, confirm return the aggregate'
nl|'\n'
comment|'# availability zone.'
nl|'\n'
name|'self'
op|'.'
name|'_add_to_aggregate'
op|'('
name|'service'
op|','
name|'self'
op|'.'
name|'agg'
op|')'
newline|'\n'
name|'new_service'
op|'='
name|'az'
op|'.'
name|'set_availability_zones'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'services'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'new_service'
op|'['
string|"'availability_zone'"
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'availability_zone'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_destroy_service'
op|'('
name|'service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_availability_zone_unicode_key
dedent|''
name|'def'
name|'test_set_availability_zone_unicode_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test set availability zone cache key is unicode."""'
newline|'\n'
name|'service'
op|'='
name|'self'
op|'.'
name|'_create_service_with_topic'
op|'('
string|"'network'"
op|','
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'new_service'
op|'='
name|'az'
op|'.'
name|'set_availability_zones'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'services'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'type'
op|'('
name|'services'
op|'['
number|'0'
op|']'
op|'['
string|"'host'"
op|']'
op|')'
op|','
name|'unicode'
op|')'
newline|'\n'
name|'cached_key'
op|'='
name|'az'
op|'.'
name|'_make_cache_key'
op|'('
name|'services'
op|'['
number|'0'
op|']'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'type'
op|'('
name|'cached_key'
op|')'
op|','
name|'str'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_destroy_service'
op|'('
name|'service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_availability_zone_not_compute_service
dedent|''
name|'def'
name|'test_set_availability_zone_not_compute_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test not compute service get right availability zone."""'
newline|'\n'
name|'service'
op|'='
name|'self'
op|'.'
name|'_create_service_with_topic'
op|'('
string|"'network'"
op|','
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'new_service'
op|'='
name|'az'
op|'.'
name|'set_availability_zones'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'services'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'new_service'
op|'['
string|"'availability_zone'"
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'default_in_az'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_destroy_service'
op|'('
name|'service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_host_availability_zone
dedent|''
name|'def'
name|'test_get_host_availability_zone'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test get right availability zone by given host."""'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'default_az'
op|','
nl|'\n'
name|'az'
op|'.'
name|'get_host_availability_zone'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'host'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'service'
op|'='
name|'self'
op|'.'
name|'_create_service_with_topic'
op|'('
string|"'compute'"
op|','
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_to_aggregate'
op|'('
name|'service'
op|','
name|'self'
op|'.'
name|'agg'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'availability_zone'
op|','
nl|'\n'
name|'az'
op|'.'
name|'get_host_availability_zone'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'host'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_host_availability_zone
dedent|''
name|'def'
name|'test_update_host_availability_zone'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test availability zone could be update by given host."""'
newline|'\n'
name|'service'
op|'='
name|'self'
op|'.'
name|'_create_service_with_topic'
op|'('
string|"'compute'"
op|','
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
comment|'# Create a new aggregate with an AZ and add the host to the AZ'
nl|'\n'
name|'az_name'
op|'='
string|"'az1'"
newline|'\n'
name|'agg_az1'
op|'='
name|'self'
op|'.'
name|'_create_az'
op|'('
string|"'agg-az1'"
op|','
name|'az_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_to_aggregate'
op|'('
name|'service'
op|','
name|'agg_az1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'az_name'
op|','
nl|'\n'
name|'az'
op|'.'
name|'get_host_availability_zone'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'host'
op|')'
op|')'
newline|'\n'
comment|'# Update AZ'
nl|'\n'
name|'new_az_name'
op|'='
string|"'az2'"
newline|'\n'
name|'self'
op|'.'
name|'_update_az'
op|'('
name|'agg_az1'
op|','
name|'new_az_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'new_az_name'
op|','
nl|'\n'
name|'az'
op|'.'
name|'get_host_availability_zone'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'host'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_host_availability_zone
dedent|''
name|'def'
name|'test_delete_host_availability_zone'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test availability zone could be deleted successfully."""'
newline|'\n'
name|'service'
op|'='
name|'self'
op|'.'
name|'_create_service_with_topic'
op|'('
string|"'compute'"
op|','
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
comment|'# Create a new aggregate with an AZ and add the host to the AZ'
nl|'\n'
name|'az_name'
op|'='
string|"'az1'"
newline|'\n'
name|'agg_az1'
op|'='
name|'self'
op|'.'
name|'_create_az'
op|'('
string|"'agg-az1'"
op|','
name|'az_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_to_aggregate'
op|'('
name|'service'
op|','
name|'agg_az1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'az_name'
op|','
nl|'\n'
name|'az'
op|'.'
name|'get_host_availability_zone'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'host'
op|')'
op|')'
newline|'\n'
comment|'# Delete the AZ via deleting the aggregate'
nl|'\n'
name|'self'
op|'.'
name|'_delete_from_aggregate'
op|'('
name|'service'
op|','
name|'agg_az1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'default_az'
op|','
nl|'\n'
name|'az'
op|'.'
name|'get_host_availability_zone'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'host'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_availability_zones
dedent|''
name|'def'
name|'test_get_availability_zones'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test get_availability_zones."""'
newline|'\n'
nl|'\n'
comment|'# When the param get_only_available of get_availability_zones is set'
nl|'\n'
comment|'# to default False, it returns two lists, zones with at least one'
nl|'\n'
comment|'# enabled services, and zones with no enabled services,'
nl|'\n'
comment|'# when get_only_available is set to True, only return a list of zones'
nl|'\n'
comment|'# with at least one enabled servies.'
nl|'\n'
comment|'# Use the following test data:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# zone         host        enabled'
nl|'\n'
comment|'# nova-test    host1       Yes'
nl|'\n'
comment|'# nova-test    host2       No'
nl|'\n'
comment|'# nova-test2   host3       Yes'
nl|'\n'
comment|'# nova-test3   host4       No'
nl|'\n'
comment|'# <default>    host5       No'
nl|'\n'
nl|'\n'
name|'agg2'
op|'='
name|'self'
op|'.'
name|'_create_az'
op|'('
string|"'agg-az2'"
op|','
string|"'nova-test2'"
op|')'
newline|'\n'
name|'agg3'
op|'='
name|'self'
op|'.'
name|'_create_az'
op|'('
string|"'agg-az3'"
op|','
string|"'nova-test3'"
op|')'
newline|'\n'
nl|'\n'
name|'service1'
op|'='
name|'self'
op|'.'
name|'_create_service_with_topic'
op|'('
string|"'compute'"
op|','
string|"'host1'"
op|','
nl|'\n'
name|'disabled'
op|'='
name|'False'
op|')'
newline|'\n'
name|'service2'
op|'='
name|'self'
op|'.'
name|'_create_service_with_topic'
op|'('
string|"'compute'"
op|','
string|"'host2'"
op|','
nl|'\n'
name|'disabled'
op|'='
name|'True'
op|')'
newline|'\n'
name|'service3'
op|'='
name|'self'
op|'.'
name|'_create_service_with_topic'
op|'('
string|"'compute'"
op|','
string|"'host3'"
op|','
nl|'\n'
name|'disabled'
op|'='
name|'False'
op|')'
newline|'\n'
name|'service4'
op|'='
name|'self'
op|'.'
name|'_create_service_with_topic'
op|'('
string|"'compute'"
op|','
string|"'host4'"
op|','
nl|'\n'
name|'disabled'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_service_with_topic'
op|'('
string|"'compute'"
op|','
string|"'host5'"
op|','
nl|'\n'
name|'disabled'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_add_to_aggregate'
op|'('
name|'service1'
op|','
name|'self'
op|'.'
name|'agg'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_to_aggregate'
op|'('
name|'service2'
op|','
name|'self'
op|'.'
name|'agg'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_to_aggregate'
op|'('
name|'service3'
op|','
name|'agg2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_to_aggregate'
op|'('
name|'service4'
op|','
name|'agg3'
op|')'
newline|'\n'
nl|'\n'
name|'zones'
op|','
name|'not_zones'
op|'='
name|'az'
op|'.'
name|'get_availability_zones'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'zones'
op|','
op|'['
string|"'nova-test'"
op|','
string|"'nova-test2'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'not_zones'
op|','
op|'['
string|"'nova-test3'"
op|','
string|"'nova'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'zones'
op|'='
name|'az'
op|'.'
name|'get_availability_zones'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'zones'
op|','
op|'['
string|"'nova-test'"
op|','
string|"'nova-test2'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_instance_availability_zone_default_value
dedent|''
name|'def'
name|'test_get_instance_availability_zone_default_value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test get right availability zone by given an instance."""'
newline|'\n'
name|'fake_inst_id'
op|'='
number|'162'
newline|'\n'
name|'fake_inst'
op|'='
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
name|'fake_inst_id'
op|','
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'default_az'
op|','
nl|'\n'
name|'az'
op|'.'
name|'get_instance_availability_zone'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fake_inst'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_instance_availability_zone_from_aggregate
dedent|''
name|'def'
name|'test_get_instance_availability_zone_from_aggregate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test get availability zone from aggregate by given an instance."""'
newline|'\n'
name|'host'
op|'='
string|"'host170'"
newline|'\n'
name|'service'
op|'='
name|'self'
op|'.'
name|'_create_service_with_topic'
op|'('
string|"'compute'"
op|','
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_to_aggregate'
op|'('
name|'service'
op|','
name|'self'
op|'.'
name|'agg'
op|')'
newline|'\n'
nl|'\n'
name|'fake_inst_id'
op|'='
number|'174'
newline|'\n'
name|'fake_inst'
op|'='
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
name|'fake_inst_id'
op|','
name|'host'
op|'='
name|'host'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'availability_zone'
op|','
nl|'\n'
name|'az'
op|'.'
name|'get_instance_availability_zone'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fake_inst'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
