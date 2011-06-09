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
name|'nova'
name|'import'
name|'compute'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'volume'
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
name|'instance_types'
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
nl|'\n'
nl|'\n'
DECL|class|QuotaTestCase
name|'class'
name|'QuotaTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|class|StubImageService
indent|'    '
name|'class'
name|'StubImageService'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|show
indent|'        '
name|'def'
name|'show'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|'"properties"'
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
dedent|''
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
name|'QuotaTestCase'
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
name|'quota_instances'
op|'='
number|'2'
op|','
nl|'\n'
name|'quota_cores'
op|'='
number|'4'
op|','
nl|'\n'
name|'quota_volumes'
op|'='
number|'2'
op|','
nl|'\n'
name|'quota_gigabytes'
op|'='
number|'20'
op|','
nl|'\n'
name|'quota_floating_ips'
op|'='
number|'1'
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
string|"'admin'"
op|','
string|"'admin'"
op|','
string|"'admin'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'='
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
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'project'
op|'='
name|'self'
op|'.'
name|'project'
op|','
nl|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'user'
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
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'delete_project'
op|'('
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'delete_user'
op|'('
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'super'
op|'('
name|'QuotaTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_instance
dedent|''
name|'def'
name|'_create_instance'
op|'('
name|'self'
op|','
name|'cores'
op|'='
number|'2'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a test instance"""'
newline|'\n'
name|'inst'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'inst'
op|'['
string|"'image_id'"
op|']'
op|'='
number|'1'
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
string|"'r-fakeres'"
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'user'
op|'.'
name|'id'
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
newline|'\n'
name|'inst'
op|'['
string|"'instance_type_id'"
op|']'
op|'='
string|"'3'"
comment|'# m1.large'
newline|'\n'
name|'inst'
op|'['
string|"'vcpus'"
op|']'
op|'='
name|'cores'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_create_volume
dedent|''
name|'def'
name|'_create_volume'
op|'('
name|'self'
op|','
name|'size'
op|'='
number|'10'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a test volume"""'
newline|'\n'
name|'vol'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vol'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'user'
op|'.'
name|'id'
newline|'\n'
name|'vol'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
newline|'\n'
name|'vol'
op|'['
string|"'size'"
op|']'
op|'='
name|'size'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_instance_type
dedent|''
name|'def'
name|'_get_instance_type'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_types'
op|'='
op|'{'
nl|'\n'
string|"'m1.tiny'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'512'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'0'
op|','
name|'flavorid'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
string|"'m1.small'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'2048'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'20'
op|','
name|'flavorid'
op|'='
number|'2'
op|')'
op|','
nl|'\n'
string|"'m1.medium'"
op|':'
nl|'\n'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'4096'
op|','
name|'vcpus'
op|'='
number|'2'
op|','
name|'local_gb'
op|'='
number|'40'
op|','
name|'flavorid'
op|'='
number|'3'
op|')'
op|','
nl|'\n'
string|"'m1.large'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'8192'
op|','
name|'vcpus'
op|'='
number|'4'
op|','
name|'local_gb'
op|'='
number|'80'
op|','
name|'flavorid'
op|'='
number|'4'
op|')'
op|','
nl|'\n'
string|"'m1.xlarge'"
op|':'
nl|'\n'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'16384'
op|','
name|'vcpus'
op|'='
number|'8'
op|','
name|'local_gb'
op|'='
number|'160'
op|','
name|'flavorid'
op|'='
number|'5'
op|')'
op|'}'
newline|'\n'
name|'return'
name|'instance_types'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_quota_overrides
dedent|''
name|'def'
name|'test_quota_overrides'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure overriding a projects quotas works"""'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_instance_type'
op|'('
string|"'m1.small'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'2'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
string|"'instances'"
op|','
number|'10'
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_instance_type'
op|'('
string|"'m1.small'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'4'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
string|"'cores'"
op|','
number|'100'
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_instance_type'
op|'('
string|"'m1.small'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'10'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
string|"'ram'"
op|','
number|'3'
op|'*'
number|'2048'
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_instance_type'
op|'('
string|"'m1.small'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'3'
op|')'
newline|'\n'
nl|'\n'
comment|'# metadata_items'
nl|'\n'
name|'too_many_items'
op|'='
name|'FLAGS'
op|'.'
name|'quota_metadata_items'
op|'+'
number|'1000'
newline|'\n'
name|'num_metadata_items'
op|'='
name|'quota'
op|'.'
name|'allowed_metadata_items'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'too_many_items'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_metadata_items'
op|','
name|'FLAGS'
op|'.'
name|'quota_metadata_items'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
string|"'metadata_items'"
op|','
number|'5'
op|')'
newline|'\n'
name|'num_metadata_items'
op|'='
name|'quota'
op|'.'
name|'allowed_metadata_items'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'too_many_items'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_metadata_items'
op|','
number|'5'
op|')'
newline|'\n'
nl|'\n'
comment|'# Cleanup'
nl|'\n'
name|'db'
op|'.'
name|'quota_destroy_all_by_project'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unlimited_instances
dedent|''
name|'def'
name|'test_unlimited_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_instances'
op|'='
number|'2'
newline|'\n'
name|'FLAGS'
op|'.'
name|'quota_ram'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'FLAGS'
op|'.'
name|'quota_cores'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'instance_type'
op|'='
name|'self'
op|'.'
name|'_get_instance_type'
op|'('
string|"'m1.small'"
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
nl|'\n'
name|'instance_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'2'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
string|"'instances'"
op|','
name|'None'
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
nl|'\n'
name|'instance_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'100'
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'101'
op|','
nl|'\n'
name|'instance_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'101'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unlimited_ram
dedent|''
name|'def'
name|'test_unlimited_ram'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_instances'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'FLAGS'
op|'.'
name|'quota_ram'
op|'='
number|'2'
op|'*'
number|'2048'
newline|'\n'
name|'FLAGS'
op|'.'
name|'quota_cores'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'instance_type'
op|'='
name|'self'
op|'.'
name|'_get_instance_type'
op|'('
string|"'m1.small'"
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
nl|'\n'
name|'instance_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'2'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
string|"'ram'"
op|','
name|'None'
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
nl|'\n'
name|'instance_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'100'
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'101'
op|','
nl|'\n'
name|'instance_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'101'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unlimited_cores
dedent|''
name|'def'
name|'test_unlimited_cores'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_instances'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'FLAGS'
op|'.'
name|'quota_ram'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'FLAGS'
op|'.'
name|'quota_cores'
op|'='
number|'2'
newline|'\n'
name|'instance_type'
op|'='
name|'self'
op|'.'
name|'_get_instance_type'
op|'('
string|"'m1.small'"
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
nl|'\n'
name|'instance_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'2'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
string|"'cores'"
op|','
name|'None'
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
nl|'\n'
name|'instance_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'100'
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'101'
op|','
nl|'\n'
name|'instance_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'101'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unlimited_volumes
dedent|''
name|'def'
name|'test_unlimited_volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_volumes'
op|'='
number|'10'
newline|'\n'
name|'FLAGS'
op|'.'
name|'quota_gigabytes'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'volumes'
op|'='
name|'quota'
op|'.'
name|'allowed_volumes'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volumes'
op|','
number|'10'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
string|"'volumes'"
op|','
name|'None'
op|')'
newline|'\n'
name|'volumes'
op|'='
name|'quota'
op|'.'
name|'allowed_volumes'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volumes'
op|','
number|'100'
op|')'
newline|'\n'
name|'volumes'
op|'='
name|'quota'
op|'.'
name|'allowed_volumes'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'101'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volumes'
op|','
number|'101'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unlimited_gigabytes
dedent|''
name|'def'
name|'test_unlimited_gigabytes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_volumes'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'FLAGS'
op|'.'
name|'quota_gigabytes'
op|'='
number|'10'
newline|'\n'
name|'volumes'
op|'='
name|'quota'
op|'.'
name|'allowed_volumes'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volumes'
op|','
number|'10'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
string|"'gigabytes'"
op|','
name|'None'
op|')'
newline|'\n'
name|'volumes'
op|'='
name|'quota'
op|'.'
name|'allowed_volumes'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volumes'
op|','
number|'100'
op|')'
newline|'\n'
name|'volumes'
op|'='
name|'quota'
op|'.'
name|'allowed_volumes'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'101'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volumes'
op|','
number|'101'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unlimited_floating_ips
dedent|''
name|'def'
name|'test_unlimited_floating_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_floating_ips'
op|'='
number|'10'
newline|'\n'
name|'floating_ips'
op|'='
name|'quota'
op|'.'
name|'allowed_floating_ips'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'floating_ips'
op|','
number|'10'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
string|"'floating_ips'"
op|','
name|'None'
op|')'
newline|'\n'
name|'floating_ips'
op|'='
name|'quota'
op|'.'
name|'allowed_floating_ips'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'floating_ips'
op|','
number|'100'
op|')'
newline|'\n'
name|'floating_ips'
op|'='
name|'quota'
op|'.'
name|'allowed_floating_ips'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'101'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'floating_ips'
op|','
number|'101'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unlimited_metadata_items
dedent|''
name|'def'
name|'test_unlimited_metadata_items'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_metadata_items'
op|'='
number|'10'
newline|'\n'
name|'items'
op|'='
name|'quota'
op|'.'
name|'allowed_metadata_items'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'items'
op|','
number|'10'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
string|"'metadata_items'"
op|','
name|'None'
op|')'
newline|'\n'
name|'items'
op|'='
name|'quota'
op|'.'
name|'allowed_metadata_items'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'items'
op|','
number|'100'
op|')'
newline|'\n'
name|'items'
op|'='
name|'quota'
op|'.'
name|'allowed_metadata_items'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'101'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'items'
op|','
number|'101'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_instances
dedent|''
name|'def'
name|'test_too_many_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'FLAGS'
op|'.'
name|'quota_instances'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'instance_ids'
op|'.'
name|'append'
op|'('
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'inst_type'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
string|"'m1.small'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'quota'
op|'.'
name|'QuotaError'
op|','
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'min_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'max_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'instance_type'
op|'='
name|'inst_type'
op|','
nl|'\n'
name|'image_href'
op|'='
number|'1'
op|')'
newline|'\n'
name|'for'
name|'instance_id'
name|'in'
name|'instance_ids'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_cores
dedent|''
dedent|''
name|'def'
name|'test_too_many_cores'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
name|'cores'
op|'='
number|'4'
op|')'
newline|'\n'
name|'instance_ids'
op|'.'
name|'append'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'inst_type'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
string|"'m1.small'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'quota'
op|'.'
name|'QuotaError'
op|','
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'min_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'max_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'instance_type'
op|'='
name|'inst_type'
op|','
nl|'\n'
name|'image_href'
op|'='
number|'1'
op|')'
newline|'\n'
name|'for'
name|'instance_id'
name|'in'
name|'instance_ids'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_volumes
dedent|''
dedent|''
name|'def'
name|'test_too_many_volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'FLAGS'
op|'.'
name|'quota_volumes'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'volume_ids'
op|'.'
name|'append'
op|'('
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'quota'
op|'.'
name|'QuotaError'
op|','
nl|'\n'
name|'volume'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'size'
op|'='
number|'10'
op|','
nl|'\n'
name|'snapshot_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'name'
op|'='
string|"''"
op|','
nl|'\n'
name|'description'
op|'='
string|"''"
op|')'
newline|'\n'
name|'for'
name|'volume_id'
name|'in'
name|'volume_ids'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_gigabytes
dedent|''
dedent|''
name|'def'
name|'test_too_many_gigabytes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
name|'size'
op|'='
number|'20'
op|')'
newline|'\n'
name|'volume_ids'
op|'.'
name|'append'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'quota'
op|'.'
name|'QuotaError'
op|','
nl|'\n'
name|'volume'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'size'
op|'='
number|'10'
op|','
nl|'\n'
name|'snapshot_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'name'
op|'='
string|"''"
op|','
nl|'\n'
name|'description'
op|'='
string|"''"
op|')'
newline|'\n'
name|'for'
name|'volume_id'
name|'in'
name|'volume_ids'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
newline|'\n'
DECL|member|test_too_many_addresses
name|'def'
name|'test_too_many_addresses'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'address'
op|'='
string|"'192.168.0.100'"
newline|'\n'
name|'db'
op|'.'
name|'floating_ip_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
op|'{'
string|"'address'"
op|':'
name|'address'
op|','
string|"'host'"
op|':'
name|'FLAGS'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'quota'
op|'.'
name|'QuotaError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_floating_ip'
op|','
nl|'\n'
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
name|'floating_ip_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_metadata_items
dedent|''
name|'def'
name|'test_too_many_metadata_items'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'FLAGS'
op|'.'
name|'quota_metadata_items'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'['
string|"'key%s'"
op|'%'
name|'i'
op|']'
op|'='
string|"'value%s'"
op|'%'
name|'i'
newline|'\n'
dedent|''
name|'inst_type'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
string|"'m1.small'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'quota'
op|'.'
name|'QuotaError'
op|','
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'min_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'max_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'instance_type'
op|'='
name|'inst_type'
op|','
nl|'\n'
name|'image_href'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_default_allowed_injected_files
dedent|''
name|'def'
name|'test_default_allowed_injected_files'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_max_injected_files'
op|'='
number|'55'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'quota'
op|'.'
name|'allowed_injected_files'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|')'
op|','
number|'55'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_overridden_allowed_injected_files
dedent|''
name|'def'
name|'test_overridden_allowed_injected_files'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_max_injected_files'
op|'='
number|'5'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
string|"'injected_files'"
op|','
number|'77'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'quota'
op|'.'
name|'allowed_injected_files'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|')'
op|','
number|'77'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unlimited_default_allowed_injected_files
dedent|''
name|'def'
name|'test_unlimited_default_allowed_injected_files'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_max_injected_files'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'quota'
op|'.'
name|'allowed_injected_files'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|')'
op|','
number|'100'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unlimited_db_allowed_injected_files
dedent|''
name|'def'
name|'test_unlimited_db_allowed_injected_files'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_max_injected_files'
op|'='
number|'5'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
string|"'injected_files'"
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'quota'
op|'.'
name|'allowed_injected_files'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|')'
op|','
number|'100'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_default_allowed_injected_file_content_bytes
dedent|''
name|'def'
name|'test_default_allowed_injected_file_content_bytes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_max_injected_file_content_bytes'
op|'='
number|'12345'
newline|'\n'
name|'limit'
op|'='
name|'quota'
op|'.'
name|'allowed_injected_file_content_bytes'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'23456'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'limit'
op|','
number|'12345'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_overridden_allowed_injected_file_content_bytes
dedent|''
name|'def'
name|'test_overridden_allowed_injected_file_content_bytes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_max_injected_file_content_bytes'
op|'='
number|'12345'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'injected_file_content_bytes'"
op|','
number|'5678'
op|')'
newline|'\n'
name|'limit'
op|'='
name|'quota'
op|'.'
name|'allowed_injected_file_content_bytes'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'23456'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'limit'
op|','
number|'5678'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unlimited_default_allowed_injected_file_content_bytes
dedent|''
name|'def'
name|'test_unlimited_default_allowed_injected_file_content_bytes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_max_injected_file_content_bytes'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'limit'
op|'='
name|'quota'
op|'.'
name|'allowed_injected_file_content_bytes'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'23456'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'limit'
op|','
number|'23456'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unlimited_db_allowed_injected_file_content_bytes
dedent|''
name|'def'
name|'test_unlimited_db_allowed_injected_file_content_bytes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'quota_max_injected_file_content_bytes'
op|'='
number|'12345'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'injected_file_content_bytes'"
op|','
name|'None'
op|')'
newline|'\n'
name|'limit'
op|'='
name|'quota'
op|'.'
name|'allowed_injected_file_content_bytes'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'23456'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'limit'
op|','
number|'23456'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_with_injected_files
dedent|''
name|'def'
name|'_create_with_injected_files'
op|'('
name|'self'
op|','
name|'files'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'image_service'
op|'='
string|"'nova.image.fake.FakeImageService'"
newline|'\n'
name|'api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
name|'image_service'
op|'='
name|'self'
op|'.'
name|'StubImageService'
op|'('
op|')'
op|')'
newline|'\n'
name|'inst_type'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
string|"'m1.small'"
op|')'
newline|'\n'
name|'api'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'min_count'
op|'='
number|'1'
op|','
name|'max_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'instance_type'
op|'='
name|'inst_type'
op|','
name|'image_href'
op|'='
string|"'3'"
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'files'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_injected_files
dedent|''
name|'def'
name|'test_no_injected_files'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'image_service'
op|'='
string|"'nova.image.fake.FakeImageService'"
newline|'\n'
name|'api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
name|'image_service'
op|'='
name|'self'
op|'.'
name|'StubImageService'
op|'('
op|')'
op|')'
newline|'\n'
name|'inst_type'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
string|"'m1.small'"
op|')'
newline|'\n'
name|'api'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_type'
op|'='
name|'inst_type'
op|','
name|'image_href'
op|'='
string|"'3'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_max_injected_files
dedent|''
name|'def'
name|'test_max_injected_files'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'files'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'FLAGS'
op|'.'
name|'quota_max_injected_files'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'files'
op|'.'
name|'append'
op|'('
op|'('
string|"'/my/path%d'"
op|'%'
name|'i'
op|','
string|"'config = test\\n'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_create_with_injected_files'
op|'('
name|'files'
op|')'
comment|'# no QuotaError'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_injected_files
dedent|''
name|'def'
name|'test_too_many_injected_files'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'files'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'FLAGS'
op|'.'
name|'quota_max_injected_files'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'files'
op|'.'
name|'append'
op|'('
op|'('
string|"'/my/path%d'"
op|'%'
name|'i'
op|','
string|"'my\\ncontent%d\\n'"
op|'%'
name|'i'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'quota'
op|'.'
name|'QuotaError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_create_with_injected_files'
op|','
name|'files'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_max_injected_file_content_bytes
dedent|''
name|'def'
name|'test_max_injected_file_content_bytes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'max'
op|'='
name|'FLAGS'
op|'.'
name|'quota_max_injected_file_content_bytes'
newline|'\n'
name|'content'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
op|'['
string|"'a'"
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'max'
op|')'
op|']'
op|')'
newline|'\n'
name|'files'
op|'='
op|'['
op|'('
string|"'/test/path'"
op|','
name|'content'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_create_with_injected_files'
op|'('
name|'files'
op|')'
comment|'# no QuotaError'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_injected_file_content_bytes
dedent|''
name|'def'
name|'test_too_many_injected_file_content_bytes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'max'
op|'='
name|'FLAGS'
op|'.'
name|'quota_max_injected_file_content_bytes'
newline|'\n'
name|'content'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
op|'['
string|"'a'"
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'max'
op|'+'
number|'1'
op|')'
op|']'
op|')'
newline|'\n'
name|'files'
op|'='
op|'['
op|'('
string|"'/test/path'"
op|','
name|'content'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'quota'
op|'.'
name|'QuotaError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_create_with_injected_files'
op|','
name|'files'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allowed_injected_file_path_bytes
dedent|''
name|'def'
name|'test_allowed_injected_file_path_bytes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'quota'
op|'.'
name|'allowed_injected_file_path_bytes'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'quota_max_injected_file_path_bytes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_max_injected_file_path_bytes
dedent|''
name|'def'
name|'test_max_injected_file_path_bytes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'max'
op|'='
name|'FLAGS'
op|'.'
name|'quota_max_injected_file_path_bytes'
newline|'\n'
name|'path'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
op|'['
string|"'a'"
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'max'
op|')'
op|']'
op|')'
newline|'\n'
name|'files'
op|'='
op|'['
op|'('
name|'path'
op|','
string|"'config = quotatest'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_create_with_injected_files'
op|'('
name|'files'
op|')'
comment|'# no QuotaError'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_injected_file_path_bytes
dedent|''
name|'def'
name|'test_too_many_injected_file_path_bytes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'max'
op|'='
name|'FLAGS'
op|'.'
name|'quota_max_injected_file_path_bytes'
newline|'\n'
name|'path'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
op|'['
string|"'a'"
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'max'
op|'+'
number|'1'
op|')'
op|']'
op|')'
newline|'\n'
name|'files'
op|'='
op|'['
op|'('
name|'path'
op|','
string|"'config = quotatest'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'quota'
op|'.'
name|'QuotaError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_create_with_injected_files'
op|','
name|'files'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
