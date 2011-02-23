begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
name|'from'
name|'base64'
name|'import'
name|'b64decode'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'from'
name|'M2Crypto'
name|'import'
name|'BIO'
newline|'\n'
name|'from'
name|'M2Crypto'
name|'import'
name|'RSA'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'crypto'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'cloud'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objectstore'
name|'import'
name|'image'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.cloud'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Temp dirs for working with image attributes through the cloud controller'
nl|'\n'
comment|'# (stole this from objectstore_unittest.py)'
nl|'\n'
DECL|variable|OSS_TEMPDIR
name|'OSS_TEMPDIR'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
name|'prefix'
op|'='
string|"'test_oss-'"
op|')'
newline|'\n'
DECL|variable|IMAGES_PATH
name|'IMAGES_PATH'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'OSS_TEMPDIR'
op|','
string|"'images'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'IMAGES_PATH'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(termie): these tests are rather fragile, they should at the lest be'
nl|'\n'
comment|'#               wiping database state after each run'
nl|'\n'
DECL|class|CloudTestCase
name|'class'
name|'CloudTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
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
name|'CloudTestCase'
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
name|'flags'
op|'('
name|'connection_type'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'images_path'
op|'='
name|'IMAGES_PATH'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'rpc'
op|'.'
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# set up our cloud'
nl|'\n'
name|'self'
op|'.'
name|'cloud'
op|'='
name|'cloud'
op|'.'
name|'CloudController'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# set up services'
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'compute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'scheduter'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'scheduler'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'network'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'admin'"
op|','
string|"'admin'"
op|','
string|"'admin'"
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'proj'"
op|','
string|"'admin'"
op|','
string|"'proj'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user'
op|'='
name|'self'
op|'.'
name|'user'
op|','
nl|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'network'
op|'.'
name|'get_network_host'
op|'('
name|'self'
op|'.'
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
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
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'network_disassociate'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'CloudTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_key
dedent|''
name|'def'
name|'_create_key'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): create depends on pool, so just call helper directly'
nl|'\n'
indent|'        '
name|'return'
name|'cloud'
op|'.'
name|'_gen_key'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'.'
name|'id'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_describe_regions
dedent|''
name|'def'
name|'test_describe_regions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes sure describe regions runs without raising an exception"""'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'describe_regions'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'result'
op|'['
string|"'regionInfo'"
op|']'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'regions'
op|'='
name|'FLAGS'
op|'.'
name|'region_list'
newline|'\n'
name|'FLAGS'
op|'.'
name|'region_list'
op|'='
op|'['
string|'"one=test_host1"'
op|','
string|'"two=test_host2"'
op|']'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'describe_regions'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'result'
op|'['
string|"'regionInfo'"
op|']'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'FLAGS'
op|'.'
name|'region_list'
op|'='
name|'regions'
newline|'\n'
nl|'\n'
DECL|member|test_describe_addresses
dedent|''
name|'def'
name|'test_describe_addresses'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes sure describe addresses runs without raising an exception"""'
newline|'\n'
name|'address'
op|'='
string|'"10.10.10.10"'
newline|'\n'
name|'db'
op|'.'
name|'floating_ip_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|"'address'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'network'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'allocate_address'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'describe_addresses'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'release_address'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'public_ip'
op|'='
name|'address'
op|')'
newline|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0.3'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'floating_ip_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_disassociate_address
dedent|''
name|'def'
name|'test_associate_disassociate_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Verifies associate runs cleanly without raising an exception"""'
newline|'\n'
name|'address'
op|'='
string|'"10.10.10.10"'
newline|'\n'
name|'db'
op|'.'
name|'floating_ip_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|"'address'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'network'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'allocate_address'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'inst'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'fixed'
op|'='
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_fixed_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'ec2_id'
op|'='
name|'cloud'
op|'.'
name|'id_to_ec2_id'
op|'('
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'associate_address'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'ec2_id'
op|','
nl|'\n'
name|'public_ip'
op|'='
name|'address'
op|')'
newline|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0.3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'disassociate_address'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'public_ip'
op|'='
name|'address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'release_address'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'public_ip'
op|'='
name|'address'
op|')'
newline|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0.3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixed'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'floating_ip_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_describe_volumes
dedent|''
name|'def'
name|'test_describe_volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes sure describe_volumes works and filters results."""'
newline|'\n'
name|'vol1'
op|'='
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'vol2'
op|'='
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'describe_volumes'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'result'
op|'['
string|"'volumeSet'"
op|']'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'volume_id'
op|'='
name|'cloud'
op|'.'
name|'id_to_ec2_id'
op|'('
name|'vol2'
op|'['
string|"'id'"
op|']'
op|','
string|"'vol-%08x'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'describe_volumes'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|'='
op|'['
name|'volume_id'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'result'
op|'['
string|"'volumeSet'"
op|']'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'cloud'
op|'.'
name|'ec2_id_to_id'
op|'('
name|'result'
op|'['
string|"'volumeSet'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'volumeId'"
op|']'
op|')'
op|','
nl|'\n'
name|'vol2'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol1'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol2'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_describe_availability_zones
dedent|''
name|'def'
name|'test_describe_availability_zones'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes sure describe_availability_zones works and filters results."""'
newline|'\n'
name|'service1'
op|'='
name|'db'
op|'.'
name|'service_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'host'"
op|':'
string|"'host1_zones'"
op|','
nl|'\n'
string|"'binary'"
op|':'
string|'"nova-compute"'
op|','
nl|'\n'
string|"'topic'"
op|':'
string|"'compute'"
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|'"zone1"'
op|'}'
op|')'
newline|'\n'
name|'service2'
op|'='
name|'db'
op|'.'
name|'service_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'host'"
op|':'
string|"'host2_zones'"
op|','
nl|'\n'
string|"'binary'"
op|':'
string|'"nova-compute"'
op|','
nl|'\n'
string|"'topic'"
op|':'
string|"'compute'"
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|'"zone2"'
op|'}'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'describe_availability_zones'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'result'
op|'['
string|"'availabilityZoneInfo'"
op|']'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'service1'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'service2'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_describe_instances
dedent|''
name|'def'
name|'test_describe_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes sure describe_instances works and filters results."""'
newline|'\n'
name|'inst1'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'reservation_id'"
op|':'
string|"'a'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host1'"
op|'}'
op|')'
newline|'\n'
name|'inst2'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'reservation_id'"
op|':'
string|"'a'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host2'"
op|'}'
op|')'
newline|'\n'
name|'comp1'
op|'='
name|'db'
op|'.'
name|'service_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'zone1'"
op|','
nl|'\n'
string|"'topic'"
op|':'
string|'"compute"'
op|'}'
op|')'
newline|'\n'
name|'comp2'
op|'='
name|'db'
op|'.'
name|'service_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'host'"
op|':'
string|"'host2'"
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'zone2'"
op|','
nl|'\n'
string|"'topic'"
op|':'
string|'"compute"'
op|'}'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'describe_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'result'
op|'='
name|'result'
op|'['
string|"'reservationSet'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'result'
op|'['
string|"'instancesSet'"
op|']'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'instance_id'
op|'='
name|'cloud'
op|'.'
name|'id_to_ec2_id'
op|'('
name|'inst2'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'describe_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|'='
op|'['
name|'instance_id'
op|']'
op|')'
newline|'\n'
name|'result'
op|'='
name|'result'
op|'['
string|"'reservationSet'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'result'
op|'['
string|"'instancesSet'"
op|']'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|"'instancesSet'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'instanceId'"
op|']'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|"'instancesSet'"
op|']'
op|'['
number|'0'
op|']'
nl|'\n'
op|'['
string|"'placement'"
op|']'
op|'['
string|"'availabilityZone'"
op|']'
op|','
string|"'zone2'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst1'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst2'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'comp1'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'comp2'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_console_output
dedent|''
name|'def'
name|'test_console_output'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
name|'FLAGS'
op|'.'
name|'default_image'
newline|'\n'
name|'instance_type'
op|'='
name|'FLAGS'
op|'.'
name|'default_instance_type'
newline|'\n'
name|'max_count'
op|'='
number|'1'
newline|'\n'
name|'kwargs'
op|'='
op|'{'
string|"'image_id'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'instance_type'
op|','
nl|'\n'
string|"'max_count'"
op|':'
name|'max_count'
op|'}'
newline|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'run_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0.3'
op|')'
newline|'\n'
name|'instance_id'
op|'='
name|'rv'
op|'['
string|"'instancesSet'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'instanceId'"
op|']'
newline|'\n'
name|'output'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'get_console_output'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|'='
op|'['
name|'instance_id'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'b64decode'
op|'('
name|'output'
op|'['
string|"'output'"
op|']'
op|')'
op|','
string|"'FAKE CONSOLE OUTPUT'"
op|')'
newline|'\n'
comment|'# TODO(soren): We need this until we can stop polling in the rpc code'
nl|'\n'
comment|'#              for unit tests.'
nl|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0.3'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'terminate_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'['
name|'instance_id'
op|']'
op|')'
newline|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0.3'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ajax_console
dedent|''
name|'def'
name|'test_ajax_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
name|'FLAGS'
op|'.'
name|'default_image'
newline|'\n'
name|'kwargs'
op|'='
op|'{'
string|"'image_id'"
op|':'
name|'image_id'
op|'}'
newline|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'run_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'instance_id'
op|'='
name|'rv'
op|'['
string|"'instancesSet'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'instanceId'"
op|']'
newline|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0.3'
op|')'
newline|'\n'
name|'output'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'get_ajax_console'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|'='
op|'['
name|'instance_id'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'output'
op|'['
string|"'url'"
op|']'
op|','
nl|'\n'
string|"'%s/?token=FAKETOKEN'"
op|'%'
name|'FLAGS'
op|'.'
name|'ajax_console_proxy_url'
op|')'
newline|'\n'
comment|'# TODO(soren): We need this until we can stop polling in the rpc code'
nl|'\n'
comment|'#              for unit tests.'
nl|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0.3'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'terminate_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'['
name|'instance_id'
op|']'
op|')'
newline|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0.3'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_key_generation
dedent|''
name|'def'
name|'test_key_generation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'_create_key'
op|'('
string|"'test'"
op|')'
newline|'\n'
name|'private_key'
op|'='
name|'result'
op|'['
string|"'private_key'"
op|']'
newline|'\n'
name|'key'
op|'='
name|'RSA'
op|'.'
name|'load_key_string'
op|'('
name|'private_key'
op|','
name|'callback'
op|'='
name|'lambda'
op|':'
name|'None'
op|')'
newline|'\n'
name|'bio'
op|'='
name|'BIO'
op|'.'
name|'MemoryBuffer'
op|'('
op|')'
newline|'\n'
name|'public_key'
op|'='
name|'db'
op|'.'
name|'key_pair_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'test'"
op|')'
op|'['
string|"'public_key'"
op|']'
newline|'\n'
name|'key'
op|'.'
name|'save_pub_key_bio'
op|'('
name|'bio'
op|')'
newline|'\n'
name|'converted'
op|'='
name|'crypto'
op|'.'
name|'ssl_pub_to_ssh_pub'
op|'('
name|'bio'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
comment|'# assert key fields are equal'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'public_key'
op|'.'
name|'split'
op|'('
string|'" "'
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|','
nl|'\n'
name|'converted'
op|'.'
name|'split'
op|'('
string|'" "'
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_describe_key_pairs
dedent|''
name|'def'
name|'test_describe_key_pairs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_key'
op|'('
string|"'test1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_key'
op|'('
string|"'test2'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'describe_key_pairs'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'keys'
op|'='
name|'result'
op|'['
string|'"keypairsSet"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filter'
op|'('
name|'lambda'
name|'k'
op|':'
name|'k'
op|'['
string|"'keyName'"
op|']'
op|'=='
string|"'test1'"
op|','
name|'keys'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filter'
op|'('
name|'lambda'
name|'k'
op|':'
name|'k'
op|'['
string|"'keyName'"
op|']'
op|'=='
string|"'test2'"
op|','
name|'keys'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_key_pair
dedent|''
name|'def'
name|'test_delete_key_pair'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_key'
op|'('
string|"'test'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'delete_key_pair'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'test'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_instances
dedent|''
name|'def'
name|'test_run_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'FLAGS'
op|'.'
name|'connection_type'
op|'=='
string|"'fake'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Can\'t test instances without a real virtual env."'
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'image_id'
op|'='
name|'FLAGS'
op|'.'
name|'default_image'
newline|'\n'
name|'instance_type'
op|'='
name|'FLAGS'
op|'.'
name|'default_instance_type'
newline|'\n'
name|'max_count'
op|'='
number|'1'
newline|'\n'
name|'kwargs'
op|'='
op|'{'
string|"'image_id'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'instance_type'
op|','
nl|'\n'
string|"'max_count'"
op|':'
name|'max_count'
op|'}'
newline|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'run_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
comment|'# TODO: check for proper response'
nl|'\n'
name|'instance_id'
op|'='
name|'rv'
op|'['
string|"'reservationSet'"
op|']'
op|'['
number|'0'
op|']'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'instance'
op|'='
name|'rv'
op|'['
string|"'reservationSet'"
op|']'
op|'['
number|'0'
op|']'
op|'['
name|'instance_id'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Need to watch instance %s until it\'s running..."'
op|')'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'instance_id'"
op|']'
op|')'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'_get_instance'
op|'('
name|'instance'
op|'['
string|"'instance_id'"
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'info'
op|'['
string|"'state'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'info'
op|'['
string|"'state'"
op|']'
op|'=='
name|'power_state'
op|'.'
name|'RUNNING'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assert_'
op|'('
name|'rv'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'connection_type'
op|'!='
string|"'fake'"
op|':'
newline|'\n'
indent|'            '
name|'time'
op|'.'
name|'sleep'
op|'('
number|'45'
op|')'
comment|'# Should use boto for polling here'
newline|'\n'
dedent|''
name|'for'
name|'reservations'
name|'in'
name|'rv'
op|'['
string|"'reservationSet'"
op|']'
op|':'
newline|'\n'
comment|'# for res_id in reservations.keys():'
nl|'\n'
comment|'#     LOG.debug(reservations[res_id])'
nl|'\n'
comment|'# for instance in reservations[res_id]:'
nl|'\n'
indent|'            '
name|'for'
name|'instance'
name|'in'
name|'reservations'
op|'['
name|'reservations'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'instance_id'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Terminating instance %s"'
op|')'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_describe_instances
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_describe_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes sure describe_instances works."""'
newline|'\n'
name|'instance1'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'host'"
op|':'
string|"'host2'"
op|'}'
op|')'
newline|'\n'
name|'comp1'
op|'='
name|'db'
op|'.'
name|'service_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'host'"
op|':'
string|"'host2'"
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'zone1'"
op|','
nl|'\n'
string|"'topic'"
op|':'
string|'"compute"'
op|'}'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'describe_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|"'reservationSet'"
op|']'
op|'['
number|'0'
op|']'
nl|'\n'
op|'['
string|"'instancesSet'"
op|']'
op|'['
number|'0'
op|']'
nl|'\n'
op|'['
string|"'placement'"
op|']'
op|'['
string|"'availabilityZone'"
op|']'
op|','
string|"'zone1'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance1'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'comp1'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_fake_set_image_description
name|'def'
name|'_fake_set_image_description'
op|'('
name|'ctxt'
op|','
name|'image_id'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'from'
name|'nova'
op|'.'
name|'objectstore'
name|'import'
name|'handler'
newline|'\n'
nl|'\n'
DECL|class|req
name|'class'
name|'req'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'request'
op|'='
name|'req'
op|'('
op|')'
newline|'\n'
name|'request'
op|'.'
name|'context'
op|'='
name|'ctxt'
newline|'\n'
name|'request'
op|'.'
name|'args'
op|'='
op|'{'
string|"'image_id'"
op|':'
op|'['
name|'image_id'
op|']'
op|','
nl|'\n'
string|"'description'"
op|':'
op|'['
name|'description'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'resource'
op|'='
name|'handler'
op|'.'
name|'ImagesResource'
op|'('
op|')'
newline|'\n'
name|'resource'
op|'.'
name|'render_POST'
op|'('
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_user_editable_image_endpoint
dedent|''
name|'def'
name|'test_user_editable_image_endpoint'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pathdir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'images_path'
op|','
string|"'ami-testing'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'mkdir'
op|'('
name|'pathdir'
op|')'
newline|'\n'
name|'info'
op|'='
op|'{'
string|"'isPublic'"
op|':'
name|'False'
op|'}'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'pathdir'
op|','
string|"'info.json'"
op|')'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'json'
op|'.'
name|'dump'
op|'('
name|'info'
op|','
name|'f'
op|')'
newline|'\n'
dedent|''
name|'img'
op|'='
name|'image'
op|'.'
name|'Image'
op|'('
string|"'ami-testing'"
op|')'
newline|'\n'
comment|"# self.cloud.set_image_description(self.context, 'ami-testing',"
nl|'\n'
comment|"#                                  'Foo Img')"
nl|'\n'
comment|"# NOTE(vish): Above won't work unless we start objectstore or create"
nl|'\n'
comment|'#             a fake version of api/ec2/images.py conn that can'
nl|'\n'
comment|'#             call methods directly instead of going through boto.'
nl|'\n'
comment|'#             for now, just cheat and call the method directly'
nl|'\n'
name|'self'
op|'.'
name|'_fake_set_image_description'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'ami-testing'"
op|','
nl|'\n'
string|"'Foo Img'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'Foo Img'"
op|','
name|'img'
op|'.'
name|'metadata'
op|'['
string|"'description'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_fake_set_image_description'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'ami-testing'"
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'img'
op|'.'
name|'metadata'
op|'['
string|"'description'"
op|']'
op|')'
newline|'\n'
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'pathdir'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_of_instance_display_fields
dedent|''
name|'def'
name|'test_update_of_instance_display_fields'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'ec2_id'
op|'='
name|'cloud'
op|'.'
name|'id_to_ec2_id'
op|'('
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'update_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'ec2_id'
op|','
nl|'\n'
name|'display_name'
op|'='
string|"'c00l 1m4g3'"
op|')'
newline|'\n'
name|'inst'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'c00l 1m4g3'"
op|','
name|'inst'
op|'['
string|"'display_name'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_of_instance_wont_update_private_fields
dedent|''
name|'def'
name|'test_update_of_instance_wont_update_private_fields'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'update_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'mac_address'
op|'='
string|"'DE:AD:BE:EF'"
op|')'
newline|'\n'
name|'inst'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'None'
op|','
name|'inst'
op|'['
string|"'mac_address'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_of_volume_display_fields
dedent|''
name|'def'
name|'test_update_of_volume_display_fields'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vol'
op|'='
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'update_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'cloud'
op|'.'
name|'id_to_ec2_id'
op|'('
name|'vol'
op|'['
string|"'id'"
op|']'
op|','
string|"'vol-%08x'"
op|')'
op|','
nl|'\n'
name|'display_name'
op|'='
string|"'c00l v0lum3'"
op|')'
newline|'\n'
name|'vol'
op|'='
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'c00l v0lum3'"
op|','
name|'vol'
op|'['
string|"'display_name'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_of_volume_wont_update_private_fields
dedent|''
name|'def'
name|'test_update_of_volume_wont_update_private_fields'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vol'
op|'='
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'update_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'cloud'
op|'.'
name|'id_to_ec2_id'
op|'('
name|'vol'
op|'['
string|"'id'"
op|']'
op|','
string|"'vol-%08x'"
op|')'
op|','
nl|'\n'
name|'mountpoint'
op|'='
string|"'/not/here'"
op|')'
newline|'\n'
name|'vol'
op|'='
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'None'
op|','
name|'vol'
op|'['
string|"'mountpoint'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
