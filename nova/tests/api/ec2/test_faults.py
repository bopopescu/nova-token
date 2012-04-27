begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
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
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'faults'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestFaults
name|'class'
name|'TestFaults'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tests covering ec2 Fault class."""'
newline|'\n'
nl|'\n'
DECL|member|test_fault_exception
name|'def'
name|'test_fault_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure the status_int is set correctly on faults"""'
newline|'\n'
name|'fault'
op|'='
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
nl|'\n'
name|'explanation'
op|'='
string|"'test'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'fault'
op|'.'
name|'wrapped_exc'
op|','
nl|'\n'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fault_exception_status_int
dedent|''
name|'def'
name|'test_fault_exception_status_int'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure the status_int is set correctly on faults"""'
newline|'\n'
name|'fault'
op|'='
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
string|"'test'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'fault'
op|'.'
name|'wrapped_exc'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
