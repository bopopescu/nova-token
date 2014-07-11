begin_unit
comment|'# Copyright 2013 Mirantis, Inc.'
nl|'\n'
comment|'# Copyright 2013 OpenStack Foundation'
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
name|'cinderclient'
name|'import'
name|'exceptions'
name|'as'
name|'cinder_exception'
newline|'\n'
name|'import'
name|'mock'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'cinder'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeCinderClient
name|'class'
name|'FakeCinderClient'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|class|Volumes
indent|'    '
name|'class'
name|'Volumes'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|get
indent|'        '
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'id'"
op|':'
name|'volume_id'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|list
dedent|''
name|'def'
name|'list'
op|'('
name|'self'
op|','
name|'detailed'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'id1'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'id2'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
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
string|"'id'"
op|':'
string|"'created_id'"
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'volumes'
op|'='
name|'self'
op|'.'
name|'Volumes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_snapshots'
op|'='
name|'self'
op|'.'
name|'volumes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CinderApiTestCase
dedent|''
dedent|''
name|'class'
name|'CinderApiTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'CinderApiTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'='
name|'cinder'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cinderclient'
op|'='
name|'FakeCinderClient'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ctx'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cinder'
op|','
string|"'cinderclient'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cinder'
op|','
string|"'_untranslate_volume_summary_view'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cinder'
op|','
string|"'_untranslate_snapshot_summary_view'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get
dedent|''
name|'def'
name|'test_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_id'
op|'='
string|"'volume_id1'"
newline|'\n'
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'_untranslate_volume_summary_view'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
op|'{'
string|"'id'"
op|':'
string|"'volume_id1'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_failed
dedent|''
name|'def'
name|'test_get_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_id'
op|'='
string|"'volume_id'"
newline|'\n'
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'cinder_exception'
op|'.'
name|'NotFound'
op|'('
string|"''"
op|')'
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'cinder_exception'
op|'.'
name|'BadRequest'
op|'('
string|"''"
op|')'
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndRaise'
op|'('
nl|'\n'
name|'cinder_exception'
op|'.'
name|'ConnectionError'
op|'('
string|"''"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'VolumeNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'get'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInput'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'get'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CinderConnectionFailed'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'get'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'_untranslate_volume_summary_view'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
op|'{'
string|"'id'"
op|':'
string|"'created_id'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
number|'1'
op|','
string|"''"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_failed
dedent|''
name|'def'
name|'test_create_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'cinder_exception'
op|'.'
name|'BadRequest'
op|'('
string|"''"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInput'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
number|'1'
op|','
string|"''"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.volume.cinder.cinderclient'"
op|')'
newline|'\n'
DECL|member|test_create_over_quota_failed
name|'def'
name|'test_create_over_quota_failed'
op|'('
name|'self'
op|','
name|'mock_cinderclient'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_cinderclient'
op|'.'
name|'return_value'
op|'.'
name|'volumes'
op|'.'
name|'create'
op|'.'
name|'side_effect'
op|'='
op|'('
nl|'\n'
name|'cinder_exception'
op|'.'
name|'OverLimit'
op|'('
number|'413'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'OverQuota'
op|','
name|'self'
op|'.'
name|'api'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
nl|'\n'
number|'1'
op|','
string|"''"
op|','
string|"''"
op|')'
newline|'\n'
name|'mock_cinderclient'
op|'.'
name|'return_value'
op|'.'
name|'volumes'
op|'.'
name|'create'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
number|'1'
op|','
name|'user_id'
op|'='
name|'None'
op|','
name|'imageRef'
op|'='
name|'None'
op|','
name|'availability_zone'
op|'='
name|'None'
op|','
nl|'\n'
name|'volume_type'
op|'='
name|'None'
op|','
name|'display_description'
op|'='
string|"''"
op|','
name|'snapshot_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'display_name'
op|'='
string|"''"
op|','
name|'project_id'
op|'='
name|'None'
op|','
name|'metadata'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all
dedent|''
name|'def'
name|'test_get_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'_untranslate_volume_summary_view'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'id1'"
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'id1'"
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'_untranslate_volume_summary_view'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'id2'"
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'id2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'id1'"
op|','
string|"'id2'"
op|']'
op|','
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_all'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_attach_volume_status_error
dedent|''
name|'def'
name|'test_check_attach_volume_status_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
op|'{'
string|"'status'"
op|':'
string|"'error'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidVolume'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'check_attach'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
name|'volume'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_attach_volume_already_attached
dedent|''
name|'def'
name|'test_check_attach_volume_already_attached'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
op|'{'
string|"'status'"
op|':'
string|"'available'"
op|'}'
newline|'\n'
name|'volume'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|'"attached"'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidVolume'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'check_attach'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
name|'volume'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_attach_availability_zone_differs
dedent|''
name|'def'
name|'test_check_attach_availability_zone_differs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
op|'{'
string|"'status'"
op|':'
string|"'available'"
op|'}'
newline|'\n'
name|'volume'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|'"detached"'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|"'availability_zone'"
op|':'
string|"'zone1'"
op|','
string|"'host'"
op|':'
string|"'fakehost'"
op|'}'
newline|'\n'
nl|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'cinder'
op|'.'
name|'az'
op|','
string|"'get_instance_availability_zone'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'lambda'
name|'context'
op|','
nl|'\n'
name|'instance'
op|':'
string|"'zone1'"
op|')'
name|'as'
name|'mock_get_instance_az'
op|':'
newline|'\n'
nl|'\n'
indent|'            '
name|'cinder'
op|'.'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'cinder_cross_az_attach'"
op|','
name|'False'
op|')'
newline|'\n'
name|'volume'
op|'['
string|"'availability_zone'"
op|']'
op|'='
string|"'zone1'"
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'self'
op|'.'
name|'api'
op|'.'
name|'check_attach'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'volume'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
name|'mock_get_instance_az'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
name|'instance'
op|')'
newline|'\n'
name|'mock_get_instance_az'
op|'.'
name|'reset_mock'
op|'('
op|')'
newline|'\n'
name|'volume'
op|'['
string|"'availability_zone'"
op|']'
op|'='
string|"'zone2'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidVolume'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'check_attach'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
name|'volume'
op|','
name|'instance'
op|')'
newline|'\n'
name|'mock_get_instance_az'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
name|'instance'
op|')'
newline|'\n'
name|'mock_get_instance_az'
op|'.'
name|'reset_mock'
op|'('
op|')'
newline|'\n'
name|'del'
name|'instance'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'volume'
op|'['
string|"'availability_zone'"
op|']'
op|'='
string|"'zone1'"
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'self'
op|'.'
name|'api'
op|'.'
name|'check_attach'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'ctx'
op|','
name|'volume'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
name|'mock_get_instance_az'
op|'.'
name|'assert_not_called'
op|'('
op|')'
newline|'\n'
name|'volume'
op|'['
string|"'availability_zone'"
op|']'
op|'='
string|"'zone2'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidVolume'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'check_attach'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
name|'volume'
op|','
name|'instance'
op|')'
newline|'\n'
name|'mock_get_instance_az'
op|'.'
name|'assert_not_called'
op|'('
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'CONF'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_attach
dedent|''
dedent|''
name|'def'
name|'test_check_attach'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
op|'{'
string|"'status'"
op|':'
string|"'available'"
op|'}'
newline|'\n'
name|'volume'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|'"detached"'
newline|'\n'
name|'volume'
op|'['
string|"'availability_zone'"
op|']'
op|'='
string|"'zone1'"
newline|'\n'
name|'instance'
op|'='
op|'{'
string|"'availability_zone'"
op|':'
string|"'zone1'"
op|','
string|"'host'"
op|':'
string|"'fakehost'"
op|'}'
newline|'\n'
name|'cinder'
op|'.'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'cinder_cross_az_attach'"
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'cinder'
op|'.'
name|'az'
op|','
string|"'get_instance_availability_zone'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'lambda'
name|'context'
op|','
name|'instance'
op|':'
string|"'zone1'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'self'
op|'.'
name|'api'
op|'.'
name|'check_attach'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'ctx'
op|','
name|'volume'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cinder'
op|'.'
name|'CONF'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_detach
dedent|''
name|'def'
name|'test_check_detach'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
op|'{'
string|"'status'"
op|':'
string|"'available'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidVolume'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'check_detach'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
name|'volume'
op|')'
newline|'\n'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'='
string|"'non-available'"
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'self'
op|'.'
name|'api'
op|'.'
name|'check_detach'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
name|'volume'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reserve_volume
dedent|''
name|'def'
name|'test_reserve_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|','
nl|'\n'
string|"'reserve'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|'.'
name|'reserve'
op|'('
string|"'id1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'reserve_volume'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
string|"'id1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unreserve_volume
dedent|''
name|'def'
name|'test_unreserve_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|','
nl|'\n'
string|"'unreserve'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|'.'
name|'unreserve'
op|'('
string|"'id1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'unreserve_volume'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
string|"'id1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_begin_detaching
dedent|''
name|'def'
name|'test_begin_detaching'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|','
nl|'\n'
string|"'begin_detaching'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|'.'
name|'begin_detaching'
op|'('
string|"'id1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'begin_detaching'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
string|"'id1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_roll_detaching
dedent|''
name|'def'
name|'test_roll_detaching'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|','
nl|'\n'
string|"'roll_detaching'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|'.'
name|'roll_detaching'
op|'('
string|"'id1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'roll_detaching'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
string|"'id1'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.volume.cinder.cinderclient'"
op|')'
newline|'\n'
DECL|member|test_attach
name|'def'
name|'test_attach'
op|'('
name|'self'
op|','
name|'mock_cinderclient'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_volumes'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_cinderclient'
op|'.'
name|'return_value'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
name|'volumes'
op|'='
name|'mock_volumes'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'attach'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
string|"'id1'"
op|','
string|"'uuid'"
op|','
string|"'point'"
op|')'
newline|'\n'
nl|'\n'
name|'mock_cinderclient'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
newline|'\n'
name|'mock_volumes'
op|'.'
name|'attach'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'id1'"
op|','
string|"'uuid'"
op|','
string|"'point'"
op|','
nl|'\n'
name|'mode'
op|'='
string|"'rw'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.volume.cinder.cinderclient'"
op|')'
newline|'\n'
DECL|member|test_attach_with_mode
name|'def'
name|'test_attach_with_mode'
op|'('
name|'self'
op|','
name|'mock_cinderclient'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_volumes'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_cinderclient'
op|'.'
name|'return_value'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
name|'volumes'
op|'='
name|'mock_volumes'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'attach'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
string|"'id1'"
op|','
string|"'uuid'"
op|','
string|"'point'"
op|','
name|'mode'
op|'='
string|"'ro'"
op|')'
newline|'\n'
nl|'\n'
name|'mock_cinderclient'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
newline|'\n'
name|'mock_volumes'
op|'.'
name|'attach'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'id1'"
op|','
string|"'uuid'"
op|','
string|"'point'"
op|','
nl|'\n'
name|'mode'
op|'='
string|"'ro'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach
dedent|''
name|'def'
name|'test_detach'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|','
nl|'\n'
string|"'detach'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|'.'
name|'detach'
op|'('
string|"'id1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'detach'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
string|"'id1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_initialize_connection
dedent|''
name|'def'
name|'test_initialize_connection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|','
nl|'\n'
string|"'initialize_connection'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|'.'
name|'initialize_connection'
op|'('
string|"'id1'"
op|','
string|"'connector'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'initialize_connection'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
string|"'id1'"
op|','
string|"'connector'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_terminate_connection
dedent|''
name|'def'
name|'test_terminate_connection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|','
nl|'\n'
string|"'terminate_connection'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|'.'
name|'terminate_connection'
op|'('
string|"'id1'"
op|','
string|"'connector'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'terminate_connection'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
string|"'id1'"
op|','
string|"'connector'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete
dedent|''
name|'def'
name|'test_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|','
nl|'\n'
string|"'delete'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|'.'
name|'delete'
op|'('
string|"'id1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
string|"'id1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update
dedent|''
name|'def'
name|'test_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'update'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
string|"''"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_snapshot
dedent|''
name|'def'
name|'test_get_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'snapshot_id'
op|'='
string|"'snapshot_id'"
newline|'\n'
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'_untranslate_snapshot_summary_view'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'snapshot_id'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_snapshot'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_snapshot_failed
dedent|''
name|'def'
name|'test_get_snapshot_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'snapshot_id'
op|'='
string|"'snapshot_id'"
newline|'\n'
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'cinder_exception'
op|'.'
name|'NotFound'
op|'('
string|"''"
op|')'
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndRaise'
op|'('
nl|'\n'
name|'cinder_exception'
op|'.'
name|'ConnectionError'
op|'('
string|"''"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'SnapshotNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_snapshot'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CinderConnectionFailed'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_snapshot'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_snapshots
dedent|''
name|'def'
name|'test_get_all_snapshots'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'_untranslate_snapshot_summary_view'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'id1'"
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'id1'"
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'_untranslate_snapshot_summary_view'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'id2'"
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'id2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'id1'"
op|','
string|"'id2'"
op|']'
op|','
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_all_snapshots'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_snapshot
dedent|''
name|'def'
name|'test_create_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'_untranslate_snapshot_summary_view'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'created_id'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'create_snapshot'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
op|'{'
string|"'id'"
op|':'
string|"'id1'"
op|'}'
op|','
string|"''"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_force
dedent|''
name|'def'
name|'test_create_force'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'_untranslate_snapshot_summary_view'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'created_id'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'create_snapshot_force'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
op|'{'
string|"'id'"
op|':'
string|"'id1'"
op|'}'
op|','
string|"''"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_snapshot
dedent|''
name|'def'
name|'test_delete_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volume_snapshots'
op|','
nl|'\n'
string|"'delete'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volume_snapshots'
op|'.'
name|'delete'
op|'('
string|"'id1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'delete_snapshot'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
string|"'id1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_volume_metadata
dedent|''
name|'def'
name|'test_get_volume_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_volume_metadata'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_volume_metadata_value
dedent|''
name|'def'
name|'test_get_volume_metadata_value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_volume_metadata_value'
op|','
string|"''"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_volume_metadata
dedent|''
name|'def'
name|'test_delete_volume_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'delete_volume_metadata'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
string|"''"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_volume_metadata
dedent|''
name|'def'
name|'test_update_volume_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'update_volume_metadata'
op|','
name|'self'
op|'.'
name|'ctx'
op|','
string|"''"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_snapshot_status
dedent|''
name|'def'
name|'test_update_snapshot_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volume_snapshots'
op|','
nl|'\n'
string|"'update_snapshot_status'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volume_snapshots'
op|'.'
name|'update_snapshot_status'
op|'('
nl|'\n'
string|"'id1'"
op|','
op|'{'
string|"'status'"
op|':'
string|"'error'"
op|','
string|"'progress'"
op|':'
string|"'90%'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'update_snapshot_status'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
string|"'id1'"
op|','
string|"'error'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_volume_encryption_metadata
dedent|''
name|'def'
name|'test_get_volume_encryption_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'ctx'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|','
nl|'\n'
string|"'get_encryption_metadata'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cinderclient'
op|'.'
name|'volumes'
op|'.'
name|'get_encryption_metadata'
op|'('
op|'{'
string|"'encryption_key_id'"
op|':'
string|"'fake_key'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_volume_encryption_metadata'
op|'('
name|'self'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'encryption_key_id'"
op|':'
nl|'\n'
string|"'fake_key'"
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
