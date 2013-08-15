begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
name|'import'
name|'datetime'
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
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'objects'
name|'import'
name|'test_compute_node'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
nl|'\n'
DECL|variable|NOW
name|'NOW'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'replace'
op|'('
name|'microsecond'
op|'='
number|'0'
op|')'
newline|'\n'
DECL|variable|fake_service
name|'fake_service'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'NOW'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fake-host'"
op|','
nl|'\n'
string|"'binary'"
op|':'
string|"'fake-service'"
op|','
nl|'\n'
string|"'topic'"
op|':'
string|"'fake-service-topic'"
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'disabled'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
name|'None'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compare
name|'def'
name|'compare'
op|'('
name|'obj'
op|','
name|'db_obj'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'allow_missing'
op|'='
op|'('
string|"'availability_zone'"
op|','
string|"'compute_node'"
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'obj'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
name|'in'
name|'allow_missing'
name|'and'
name|'not'
name|'obj'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'key'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'obj_val'
op|'='
name|'obj'
op|'['
name|'key'
op|']'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'obj_val'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'obj_val'
op|'='
name|'obj_val'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'None'
op|')'
newline|'\n'
dedent|''
name|'db_val'
op|'='
name|'db_obj'
op|'['
name|'key'
op|']'
newline|'\n'
name|'assert'
name|'db_val'
op|'=='
name|'obj_val'
op|','
string|"'%s != %s'"
op|'%'
op|'('
name|'db_val'
op|','
name|'obj_val'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestServiceObject
dedent|''
dedent|''
name|'class'
name|'_TestServiceObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|_test_query
indent|'    '
name|'def'
name|'_test_query'
op|'('
name|'self'
op|','
name|'db_method'
op|','
name|'obj_method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
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
name|'db'
op|','
name|'db_method'
op|')'
newline|'\n'
name|'getattr'
op|'('
name|'db'
op|','
name|'db_method'
op|')'
op|'('
name|'ctxt'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'fake_service'
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
name|'obj'
op|'='
name|'getattr'
op|'('
name|'service'
op|'.'
name|'Service'
op|','
name|'obj_method'
op|')'
op|'('
name|'ctxt'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'compare'
op|'('
name|'obj'
op|','
name|'fake_service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_id
dedent|''
name|'def'
name|'test_get_by_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_query'
op|'('
string|"'service_get'"
op|','
string|"'get_by_id'"
op|','
number|'123'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_host_and_topic
dedent|''
name|'def'
name|'test_get_by_host_and_topic'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_query'
op|'('
string|"'service_get_by_host_and_topic'"
op|','
nl|'\n'
string|"'get_by_host_and_topic'"
op|','
string|"'fake-host'"
op|','
string|"'fake-topic'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_compute_host
dedent|''
name|'def'
name|'test_get_by_compute_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_query'
op|'('
string|"'service_get_by_compute_host'"
op|','
string|"'get_by_compute_host'"
op|','
nl|'\n'
string|"'fake-host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_args
dedent|''
name|'def'
name|'test_get_by_args'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_query'
op|'('
string|"'service_get_by_args'"
op|','
string|"'get_by_args'"
op|','
string|"'fake-host'"
op|','
nl|'\n'
string|"'fake-service'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_with_compute_node
dedent|''
name|'def'
name|'test_with_compute_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
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
name|'db'
op|','
string|"'service_get'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'compute_node_get_by_service_id'"
op|')'
newline|'\n'
name|'_fake_service'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'fake_service'
op|','
name|'compute_node'
op|'='
op|'['
name|'test_compute_node'
op|'.'
name|'fake_compute_node'
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_get'
op|'('
name|'ctxt'
op|','
number|'123'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'_fake_service'
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
name|'service_obj'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'get_by_id'
op|'('
name|'ctxt'
op|','
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'service_obj'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'compute_node'"
op|')'
op|')'
newline|'\n'
name|'compare'
op|'('
name|'service_obj'
op|'.'
name|'compute_node'
op|','
name|'test_compute_node'
op|'.'
name|'fake_compute_node'
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
name|'ctxt'
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
name|'db'
op|','
string|"'service_create'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_create'
op|'('
name|'ctxt'
op|','
op|'{'
string|"'host'"
op|':'
string|"'fake-host'"
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'fake_service'
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
name|'service_obj'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
op|')'
newline|'\n'
name|'service_obj'
op|'.'
name|'host'
op|'='
string|"'fake-host'"
newline|'\n'
name|'service_obj'
op|'.'
name|'create'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_service'
op|'['
string|"'id'"
op|']'
op|','
name|'service_obj'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save
dedent|''
name|'def'
name|'test_save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
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
name|'db'
op|','
string|"'service_update'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_update'
op|'('
name|'ctxt'
op|','
number|'123'
op|','
op|'{'
string|"'host'"
op|':'
string|"'fake-host'"
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'fake_service'
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
name|'service_obj'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
op|')'
newline|'\n'
name|'service_obj'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'service_obj'
op|'.'
name|'host'
op|'='
string|"'fake-host'"
newline|'\n'
name|'service_obj'
op|'.'
name|'save'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_destroy
dedent|''
name|'def'
name|'_test_destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
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
name|'db'
op|','
string|"'service_destroy'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'ctxt'
op|','
number|'123'
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
name|'service_obj'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
op|')'
newline|'\n'
name|'service_obj'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'service_obj'
op|'.'
name|'destroy'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy
dedent|''
name|'def'
name|'test_destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# The test harness needs db.service_destroy to work,'
nl|'\n'
comment|"# so avoid leaving it broken here after we're done"
nl|'\n'
indent|'        '
name|'orig_service_destroy'
op|'='
name|'db'
op|'.'
name|'service_destroy'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_test_destroy'
op|'('
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'service_destroy'
op|'='
name|'orig_service_destroy'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_topic
dedent|''
dedent|''
name|'def'
name|'test_get_by_topic'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
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
name|'db'
op|','
string|"'service_get_all_by_topic'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_get_all_by_topic'
op|'('
name|'ctxt'
op|','
string|"'fake-topic'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
name|'fake_service'
op|']'
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
name|'services'
op|'='
name|'service'
op|'.'
name|'ServiceList'
op|'.'
name|'get_by_topic'
op|'('
name|'ctxt'
op|','
string|"'fake-topic'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'services'
op|')'
op|')'
newline|'\n'
name|'compare'
op|'('
name|'services'
op|'['
number|'0'
op|']'
op|','
name|'fake_service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_host
dedent|''
name|'def'
name|'test_get_by_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
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
name|'db'
op|','
string|"'service_get_all_by_host'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_get_all_by_host'
op|'('
name|'ctxt'
op|','
string|"'fake-host'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
name|'fake_service'
op|']'
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
name|'services'
op|'='
name|'service'
op|'.'
name|'ServiceList'
op|'.'
name|'get_by_host'
op|'('
name|'ctxt'
op|','
string|"'fake-host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'services'
op|')'
op|')'
newline|'\n'
name|'compare'
op|'('
name|'services'
op|'['
number|'0'
op|']'
op|','
name|'fake_service'
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
name|'ctxt'
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
name|'db'
op|','
string|"'service_get_all'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'ctxt'
op|','
name|'disabled'
op|'='
name|'False'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'fake_service'
op|']'
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
name|'services'
op|'='
name|'service'
op|'.'
name|'ServiceList'
op|'.'
name|'get_all'
op|'('
name|'ctxt'
op|','
name|'disabled'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'services'
op|')'
op|')'
newline|'\n'
name|'compare'
op|'('
name|'services'
op|'['
number|'0'
op|']'
op|','
name|'fake_service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_with_az
dedent|''
name|'def'
name|'test_get_all_with_az'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
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
name|'db'
op|','
string|"'service_get_all'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'aggregate_host_get_by_metadata_key'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'ctxt'
op|','
name|'disabled'
op|'='
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
name|'dict'
op|'('
name|'fake_service'
op|','
name|'topic'
op|'='
string|"'compute'"
op|')'
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_host_get_by_metadata_key'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'key'
op|'='
string|"'availability_zone'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'{'
name|'fake_service'
op|'['
string|"'host'"
op|']'
op|':'
op|'['
string|"'test-az'"
op|']'
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
name|'services'
op|'='
name|'service'
op|'.'
name|'ServiceList'
op|'.'
name|'get_all'
op|'('
name|'ctxt'
op|','
name|'set_zones'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'services'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'test-az'"
op|','
name|'services'
op|'['
number|'0'
op|']'
op|'.'
name|'availability_zone'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_compute_node
dedent|''
name|'def'
name|'test_compute_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
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
name|'db'
op|','
string|"'compute_node_get_by_service_id'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'compute_node_get_by_service_id'
op|'('
name|'ctxt'
op|','
number|'123'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'test_compute_node'
op|'.'
name|'fake_compute_node'
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
name|'service_obj'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
op|')'
newline|'\n'
name|'service_obj'
op|'.'
name|'_context'
op|'='
name|'ctxt'
newline|'\n'
name|'service_obj'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'compare'
op|'('
name|'service_obj'
op|'.'
name|'compute_node'
op|','
name|'test_compute_node'
op|'.'
name|'fake_compute_node'
op|')'
newline|'\n'
comment|"# Make sure it doesn't re-fetch this"
nl|'\n'
name|'service_obj'
op|'.'
name|'compute_node'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestServiceObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestServiceObject
name|'_TestServiceObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestRemoteServiceObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteServiceObject
name|'_TestServiceObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
