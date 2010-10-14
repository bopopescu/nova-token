begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright 2010 Cloud.com, Inc'
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
string|'"""\nTests For Hyper-V driver\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'random'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'hyperv'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'connection_type'
op|'='
string|"'hyperv'"
newline|'\n'
comment|'# Redis is probably not  running on Hyper-V host.'
nl|'\n'
comment|'# Change this to the actual Redis host'
nl|'\n'
name|'FLAGS'
op|'.'
name|'redis_host'
op|'='
string|"'127.0.0.1'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HyperVTestCase
name|'class'
name|'HyperVTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test cases for the Hyper-V driver"""'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
comment|'# pylint: disable-msg=C0103'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|test_create_destroy
dedent|''
name|'def'
name|'test_create_destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a VM and destroy it"""'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|"'internal_id'"
op|':'
name|'random'
op|'.'
name|'randint'
op|'('
number|'1'
op|','
number|'1000000'
op|')'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
string|"'1024'"
op|','
nl|'\n'
string|"'mac_address'"
op|':'
string|"'02:12:34:46:56:67'"
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'instance_type'"
op|':'
string|"'m1.small'"
op|'}'
newline|'\n'
nl|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'None'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'conn'
op|'='
name|'hyperv'
op|'.'
name|'get_connection'
op|'('
name|'False'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'_create_vm'
op|'('
name|'instance_ref'
op|')'
comment|'# pylint: disable-msg=W0212'
newline|'\n'
name|'found'
op|'='
op|'['
name|'n'
name|'for'
name|'n'
name|'in'
name|'conn'
op|'.'
name|'list_instances'
op|'('
op|')'
nl|'\n'
name|'if'
name|'n'
op|'=='
name|'instance_ref'
op|'['
string|"'name'"
op|']'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'found'
op|')'
op|'=='
number|'1'
op|')'
newline|'\n'
name|'info'
op|'='
name|'conn'
op|'.'
name|'get_info'
op|'('
name|'instance_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
comment|'#Unfortunately since the vm is not running at this point,'
nl|'\n'
comment|'#we cannot obtain memory information from get_info'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'info'
op|'['
string|"'num_cpu'"
op|']'
op|','
name|'instance_ref'
op|'['
string|"'vcpus'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'conn'
op|'.'
name|'destroy'
op|'('
name|'instance_ref'
op|')'
newline|'\n'
name|'found'
op|'='
op|'['
name|'n'
name|'for'
name|'n'
name|'in'
name|'conn'
op|'.'
name|'list_instances'
op|'('
op|')'
nl|'\n'
name|'if'
name|'n'
op|'=='
name|'instance_ref'
op|'['
string|"'name'"
op|']'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'found'
op|')'
op|'=='
number|'0'
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
comment|'# pylint: disable-msg=C0103'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
