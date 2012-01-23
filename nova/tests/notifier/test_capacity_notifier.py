begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'import'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'notifier'
name|'import'
name|'capacity_notifier'
name|'as'
name|'cn'
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
nl|'\n'
nl|'\n'
DECL|class|CapacityNotifierTestCase
name|'class'
name|'CapacityNotifierTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for the Capacity updating notifier."""'
newline|'\n'
nl|'\n'
DECL|member|_make_msg
name|'def'
name|'_make_msg'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'event'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'usage_info'
op|'='
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'123'
op|','
name|'disk_gb'
op|'='
number|'456'
op|')'
newline|'\n'
name|'payload'
op|'='
name|'utils'
op|'.'
name|'to_primitive'
op|'('
name|'usage_info'
op|','
name|'convert_instances'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
nl|'\n'
name|'publisher_id'
op|'='
string|'"compute.%s"'
op|'%'
name|'host'
op|','
nl|'\n'
name|'event_type'
op|'='
string|'"compute.instance.%s"'
op|'%'
name|'event'
op|','
nl|'\n'
name|'payload'
op|'='
name|'payload'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_event_type
dedent|''
name|'def'
name|'test_event_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'self'
op|'.'
name|'_make_msg'
op|'('
string|'"myhost"'
op|','
string|'"mymethod"'
op|')'
newline|'\n'
name|'msg'
op|'['
string|"'event_type'"
op|']'
op|'='
string|"'random'"
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'cn'
op|'.'
name|'notify'
op|'('
name|'msg'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_event_suffix
dedent|''
name|'def'
name|'test_bad_event_suffix'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'self'
op|'.'
name|'_make_msg'
op|'('
string|'"myhost"'
op|','
string|'"mymethod.badsuffix"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'cn'
op|'.'
name|'notify'
op|'('
name|'msg'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_publisher_id
dedent|''
name|'def'
name|'test_bad_publisher_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'self'
op|'.'
name|'_make_msg'
op|'('
string|'"myhost"'
op|','
string|'"mymethod.start"'
op|')'
newline|'\n'
name|'msg'
op|'['
string|"'publisher_id'"
op|']'
op|'='
string|"'badpublisher'"
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'cn'
op|'.'
name|'notify'
op|'('
name|'msg'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_called
dedent|''
name|'def'
name|'test_update_called'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|_verify_called
indent|'        '
name|'def'
name|'_verify_called'
op|'('
name|'host'
op|','
name|'context'
op|','
name|'free_ram_mb_delta'
op|','
nl|'\n'
name|'free_disk_gb_delta'
op|','
name|'work_delta'
op|','
name|'vm_delta'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'free_ram_mb_delta'
op|','
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'free_disk_gb_delta'
op|','
number|'456'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm_delta'
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'work_delta'
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|'"compute_node_utilization_update"'
op|','
nl|'\n'
name|'_verify_called'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'self'
op|'.'
name|'_make_msg'
op|'('
string|'"myhost"'
op|','
string|'"delete.end"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'cn'
op|'.'
name|'notify'
op|'('
name|'msg'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
