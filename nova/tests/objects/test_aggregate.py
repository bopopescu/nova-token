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
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'aggregate'
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
name|'import'
name|'fake_notifier'
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
DECL|variable|fake_aggregate
name|'fake_aggregate'
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
string|"'name'"
op|':'
string|"'fake-aggregate'"
op|','
nl|'\n'
string|"'hosts'"
op|':'
op|'['
string|"'foo'"
op|','
string|"'bar'"
op|']'
op|','
nl|'\n'
string|"'metadetails'"
op|':'
op|'{'
string|"'this'"
op|':'
string|"'that'"
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|SUBS
name|'SUBS'
op|'='
op|'{'
string|"'metadata'"
op|':'
string|"'metadetails'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestAggregateObject
name|'class'
name|'_TestAggregateObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_by_id
indent|'    '
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
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'aggregate_get'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_aggregate'
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
name|'agg'
op|'='
name|'aggregate'
op|'.'
name|'Aggregate'
op|'.'
name|'get_by_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'agg'
op|','
name|'fake_aggregate'
op|','
name|'subs'
op|'='
name|'SUBS'
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
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'aggregate_create'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'name'"
op|':'
string|"'foo'"
op|'}'
op|','
nl|'\n'
name|'metadata'
op|'='
op|'{'
string|"'one'"
op|':'
string|"'two'"
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_aggregate'
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
name|'agg'
op|'='
name|'aggregate'
op|'.'
name|'Aggregate'
op|'('
op|')'
newline|'\n'
name|'agg'
op|'.'
name|'name'
op|'='
string|"'foo'"
newline|'\n'
name|'agg'
op|'.'
name|'metadata'
op|'='
op|'{'
string|"'one'"
op|':'
string|"'two'"
op|'}'
newline|'\n'
name|'agg'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'agg'
op|','
name|'fake_aggregate'
op|','
name|'subs'
op|'='
name|'SUBS'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_recreate_fails
dedent|''
name|'def'
name|'test_recreate_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'aggregate_create'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'name'"
op|':'
string|"'foo'"
op|'}'
op|','
nl|'\n'
name|'metadata'
op|'='
op|'{'
string|"'one'"
op|':'
string|"'two'"
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_aggregate'
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
name|'agg'
op|'='
name|'aggregate'
op|'.'
name|'Aggregate'
op|'('
op|')'
newline|'\n'
name|'agg'
op|'.'
name|'name'
op|'='
string|"'foo'"
newline|'\n'
name|'agg'
op|'.'
name|'metadata'
op|'='
op|'{'
string|"'one'"
op|':'
string|"'two'"
op|'}'
newline|'\n'
name|'agg'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
name|'agg'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
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
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'aggregate_update'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|','
op|'{'
string|"'name'"
op|':'
string|"'baz'"
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'fake_aggregate'
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
name|'agg'
op|'='
name|'aggregate'
op|'.'
name|'Aggregate'
op|'('
op|')'
newline|'\n'
name|'agg'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'agg'
op|'.'
name|'name'
op|'='
string|"'baz'"
newline|'\n'
name|'agg'
op|'.'
name|'save'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'agg'
op|','
name|'fake_aggregate'
op|','
name|'subs'
op|'='
name|'SUBS'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_and_create_no_hosts
dedent|''
name|'def'
name|'test_save_and_create_no_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agg'
op|'='
name|'aggregate'
op|'.'
name|'Aggregate'
op|'('
op|')'
newline|'\n'
name|'agg'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'agg'
op|'.'
name|'hosts'
op|'='
op|'['
string|"'foo'"
op|','
string|"'bar'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
nl|'\n'
name|'agg'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
nl|'\n'
name|'agg'
op|'.'
name|'save'
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_metadata
dedent|''
name|'def'
name|'test_update_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'aggregate_metadata_delete'"
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
string|"'aggregate_metadata_add'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_metadata_delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|','
string|"'todelete'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_metadata_add'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|','
op|'{'
string|"'toadd'"
op|':'
string|"'myval'"
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
name|'fake_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'='
op|'['
op|']'
newline|'\n'
name|'agg'
op|'='
name|'aggregate'
op|'.'
name|'Aggregate'
op|'('
op|')'
newline|'\n'
name|'agg'
op|'.'
name|'_context'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'agg'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'agg'
op|'.'
name|'metadata'
op|'='
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
newline|'\n'
name|'agg'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'agg'
op|'.'
name|'update_metadata'
op|'('
op|'{'
string|"'todelete'"
op|':'
name|'None'
op|','
string|"'toadd'"
op|':'
string|"'myval'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'fake_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'fake_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'aggregate.updatemetadata.start'"
op|','
name|'msg'
op|'.'
name|'event_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'todelete'"
op|':'
name|'None'
op|','
string|"'toadd'"
op|':'
string|"'myval'"
op|'}'
op|','
nl|'\n'
name|'msg'
op|'.'
name|'payload'
op|'['
string|"'meta_data'"
op|']'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'fake_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'aggregate.updatemetadata.end'"
op|','
name|'msg'
op|'.'
name|'event_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'todelete'"
op|':'
name|'None'
op|','
string|"'toadd'"
op|':'
string|"'myval'"
op|'}'
op|','
nl|'\n'
name|'msg'
op|'.'
name|'payload'
op|'['
string|"'meta_data'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'toadd'"
op|':'
string|"'myval'"
op|'}'
op|','
name|'agg'
op|'.'
name|'metadata'
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
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'aggregate_delete'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_delete'
op|'('
name|'self'
op|'.'
name|'context'
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
name|'agg'
op|'='
name|'aggregate'
op|'.'
name|'Aggregate'
op|'('
op|')'
newline|'\n'
name|'agg'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'agg'
op|'.'
name|'destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_host
dedent|''
name|'def'
name|'test_add_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'aggregate_host_add'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_host_add'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|','
string|"'bar'"
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
string|"'host'"
op|':'
string|"'bar'"
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
name|'agg'
op|'='
name|'aggregate'
op|'.'
name|'Aggregate'
op|'('
op|')'
newline|'\n'
name|'agg'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'agg'
op|'.'
name|'hosts'
op|'='
op|'['
string|"'foo'"
op|']'
newline|'\n'
name|'agg'
op|'.'
name|'_context'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'agg'
op|'.'
name|'add_host'
op|'('
string|"'bar'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'agg'
op|'.'
name|'hosts'
op|','
op|'['
string|"'foo'"
op|','
string|"'bar'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_host
dedent|''
name|'def'
name|'test_delete_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'aggregate_host_delete'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_host_delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|','
string|"'foo'"
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
name|'agg'
op|'='
name|'aggregate'
op|'.'
name|'Aggregate'
op|'('
op|')'
newline|'\n'
name|'agg'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'agg'
op|'.'
name|'hosts'
op|'='
op|'['
string|"'foo'"
op|','
string|"'bar'"
op|']'
newline|'\n'
name|'agg'
op|'.'
name|'_context'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'agg'
op|'.'
name|'delete_host'
op|'('
string|"'foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'agg'
op|'.'
name|'hosts'
op|','
op|'['
string|"'bar'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_availability_zone
dedent|''
name|'def'
name|'test_availability_zone'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agg'
op|'='
name|'aggregate'
op|'.'
name|'Aggregate'
op|'('
op|')'
newline|'\n'
name|'agg'
op|'.'
name|'metadata'
op|'='
op|'{'
string|"'availability_zone'"
op|':'
string|"'foo'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'foo'"
op|','
name|'agg'
op|'.'
name|'availability_zone'
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
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'aggregate_get_all'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'fake_aggregate'
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
name|'aggs'
op|'='
name|'aggregate'
op|'.'
name|'AggregateList'
op|'.'
name|'get_all'
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
number|'1'
op|','
name|'len'
op|'('
name|'aggs'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'aggs'
op|'['
number|'0'
op|']'
op|','
name|'fake_aggregate'
op|','
name|'subs'
op|'='
name|'SUBS'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_by_host
dedent|''
name|'def'
name|'test_by_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'aggregate_get_by_host'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_get_by_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-host'"
op|','
name|'key'
op|'='
name|'None'
op|','
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'fake_aggregate'
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
name|'aggs'
op|'='
name|'aggregate'
op|'.'
name|'AggregateList'
op|'.'
name|'get_by_host'
op|'('
name|'self'
op|'.'
name|'context'
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
name|'aggs'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'aggs'
op|'['
number|'0'
op|']'
op|','
name|'fake_aggregate'
op|','
name|'subs'
op|'='
name|'SUBS'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.aggregate_get_by_metadata_key'"
op|')'
newline|'\n'
DECL|member|test_get_by_metadata_key
name|'def'
name|'test_get_by_metadata_key'
op|'('
name|'self'
op|','
name|'get_by_metadata_key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get_by_metadata_key'
op|'.'
name|'return_value'
op|'='
op|'['
name|'fake_aggregate'
op|']'
newline|'\n'
name|'aggs'
op|'='
name|'aggregate'
op|'.'
name|'AggregateList'
op|'.'
name|'get_by_metadata_key'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'this'"
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
name|'aggs'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'aggs'
op|'['
number|'0'
op|']'
op|','
name|'fake_aggregate'
op|','
name|'subs'
op|'='
name|'SUBS'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.aggregate_get_by_metadata_key'"
op|')'
newline|'\n'
DECL|member|test_get_by_metadata_key_and_hosts_no_match
name|'def'
name|'test_get_by_metadata_key_and_hosts_no_match'
op|'('
name|'self'
op|','
name|'get_by_metadata_key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get_by_metadata_key'
op|'.'
name|'return_value'
op|'='
op|'['
name|'fake_aggregate'
op|']'
newline|'\n'
name|'aggs'
op|'='
name|'aggregate'
op|'.'
name|'AggregateList'
op|'.'
name|'get_by_metadata_key'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'this'"
op|','
name|'hosts'
op|'='
op|'['
string|"'baz'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'aggs'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.aggregate_get_by_metadata_key'"
op|')'
newline|'\n'
DECL|member|test_get_by_metadata_key_and_hosts_match
name|'def'
name|'test_get_by_metadata_key_and_hosts_match'
op|'('
name|'self'
op|','
name|'get_by_metadata_key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get_by_metadata_key'
op|'.'
name|'return_value'
op|'='
op|'['
name|'fake_aggregate'
op|']'
newline|'\n'
name|'aggs'
op|'='
name|'aggregate'
op|'.'
name|'AggregateList'
op|'.'
name|'get_by_metadata_key'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'this'"
op|','
name|'hosts'
op|'='
op|'['
string|"'foo'"
op|','
string|"'bar'"
op|']'
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
name|'aggs'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'aggs'
op|'['
number|'0'
op|']'
op|','
name|'fake_aggregate'
op|','
name|'subs'
op|'='
name|'SUBS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestAggregateObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestAggregateObject
name|'_TestAggregateObject'
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
name|'TestRemoteAggregateObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteAggregateObject
name|'_TestAggregateObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
