begin_unit
comment|'# Copyright (c) 2011 OpenStack, LLC.'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
name|'import'
name|'extra_specs_ops'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeCapabilitiesFilter
name|'class'
name|'ComputeCapabilitiesFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""HostFilter hard-coded to work with InstanceType records."""'
newline|'\n'
nl|'\n'
DECL|member|_satisfies_extra_specs
name|'def'
name|'_satisfies_extra_specs'
op|'('
name|'self'
op|','
name|'capabilities'
op|','
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check that the capabilities provided by the compute service\n        satisfy the extra specs associated with the instance type"""'
newline|'\n'
name|'if'
string|"'extra_specs'"
name|'not'
name|'in'
name|'instance_type'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'key'
op|','
name|'req'
name|'in'
name|'instance_type'
op|'['
string|"'extra_specs'"
op|']'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# Either not scope format, or in capabilities scope'
nl|'\n'
indent|'            '
name|'scope'
op|'='
name|'key'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'scope'
op|')'
op|'>'
number|'1'
name|'and'
name|'scope'
op|'['
number|'0'
op|']'
op|'!='
string|'"capabilities"'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'elif'
name|'scope'
op|'['
number|'0'
op|']'
op|'=='
string|'"capabilities"'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'scope'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'cap'
op|'='
name|'capabilities'
newline|'\n'
name|'for'
name|'index'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'scope'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'cap'
op|'='
name|'cap'
op|'.'
name|'get'
op|'('
name|'scope'
op|'['
name|'index'
op|']'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'cap'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'extra_specs_ops'
op|'.'
name|'match'
op|'('
name|'cap'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|host_passes
dedent|''
name|'def'
name|'host_passes'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of hosts that can create instance_type."""'
newline|'\n'
name|'instance_type'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'instance_type'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_satisfies_extra_specs'
op|'('
name|'host_state'
op|'.'
name|'capabilities'
op|','
nl|'\n'
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(host_state)s fails instance_type extra_specs "'
nl|'\n'
string|'"requirements"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
