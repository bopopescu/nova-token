begin_unit
comment|'# Copyright 2011 Andrew Bogott for the Wikimedia Foundation'
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
nl|'\n'
DECL|class|DNSDriver
name|'class'
name|'DNSDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Defines the DNS manager interface.  Does nothing."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|get_domains
dedent|''
name|'def'
name|'get_domains'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_entry
dedent|''
name|'def'
name|'create_entry'
op|'('
name|'self'
op|','
name|'_name'
op|','
name|'_address'
op|','
name|'_type'
op|','
name|'_domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_entry
dedent|''
name|'def'
name|'delete_entry'
op|'('
name|'self'
op|','
name|'_name'
op|','
name|'_domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|modify_address
dedent|''
name|'def'
name|'modify_address'
op|'('
name|'self'
op|','
name|'_name'
op|','
name|'_address'
op|','
name|'_domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_entries_by_address
dedent|''
name|'def'
name|'get_entries_by_address'
op|'('
name|'self'
op|','
name|'_address'
op|','
name|'_domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_entries_by_name
dedent|''
name|'def'
name|'get_entries_by_name'
op|'('
name|'self'
op|','
name|'_name'
op|','
name|'_domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_domain
dedent|''
name|'def'
name|'create_domain'
op|'('
name|'self'
op|','
name|'_fqdomain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_domain
dedent|''
name|'def'
name|'delete_domain'
op|'('
name|'self'
op|','
name|'_fqdomain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
