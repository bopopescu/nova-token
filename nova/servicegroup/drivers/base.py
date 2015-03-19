begin_unit
comment|'# Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'# you may not use this file except in compliance with the License.'
nl|'\n'
comment|'# You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or'
nl|'\n'
comment|'# implied.'
nl|'\n'
comment|'# See the License for the specific language governing permissions and'
nl|'\n'
comment|'# limitations under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'random'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Driver
name|'class'
name|'Driver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for all ServiceGroup drivers."""'
newline|'\n'
nl|'\n'
DECL|member|join
name|'def'
name|'join'
op|'('
name|'self'
op|','
name|'member'
op|','
name|'group'
op|','
name|'service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add a new member to a service group.\n\n        :param member: the joined member ID/name\n        :param group: the group ID/name, of the joined member\n        :param service: a `nova.service.Service` object\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_up
dedent|''
name|'def'
name|'is_up'
op|'('
name|'self'
op|','
name|'member'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check whether the given member is up."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all
dedent|''
name|'def'
name|'get_all'
op|'('
name|'self'
op|','
name|'group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns ALL members of the given group."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_one
dedent|''
name|'def'
name|'get_one'
op|'('
name|'self'
op|','
name|'group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The default behavior of get_one is to randomly pick one from\n        the result of get_all(). This is likely to be overridden in the\n        actual driver implementation.\n        """'
newline|'\n'
name|'members'
op|'='
name|'self'
op|'.'
name|'get_all'
op|'('
name|'group_id'
op|')'
newline|'\n'
name|'if'
name|'members'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'length'
op|'='
name|'len'
op|'('
name|'members'
op|')'
newline|'\n'
name|'if'
name|'length'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'random'
op|'.'
name|'choice'
op|'('
name|'members'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
