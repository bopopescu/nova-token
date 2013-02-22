begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
string|'"""Custom SQLAlchemy types."""'
newline|'\n'
nl|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'dialects'
name|'import'
name|'postgresql'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'types'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IPAddress
name|'class'
name|'IPAddress'
op|'('
name|'types'
op|'.'
name|'TypeDecorator'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""An SQLAlchemy type representing an IP-address."""'
newline|'\n'
DECL|variable|impl
name|'impl'
op|'='
name|'types'
op|'.'
name|'String'
op|'('
number|'39'
op|')'
op|'.'
name|'with_variant'
op|'('
name|'postgresql'
op|'.'
name|'INET'
op|'('
op|')'
op|','
string|"'postgresql'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|process_bind_param
name|'def'
name|'process_bind_param'
op|'('
name|'self'
op|','
name|'value'
op|','
name|'dialect'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Process/Formats the value before insert it into the db."""'
newline|'\n'
name|'if'
name|'dialect'
op|'.'
name|'name'
op|'=='
string|"'postgresql'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'value'
newline|'\n'
comment|'# NOTE(maurosr): The purpose here is to convert ipv6 to the shortened'
nl|'\n'
comment|'# form, not validate it.'
nl|'\n'
dedent|''
name|'elif'
name|'utils'
op|'.'
name|'is_valid_ipv6'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'utils'
op|'.'
name|'get_shortened_ipv6'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'value'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CIDR
dedent|''
dedent|''
name|'class'
name|'CIDR'
op|'('
name|'types'
op|'.'
name|'TypeDecorator'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""An SQLAlchemy type representing a CIDR definition."""'
newline|'\n'
DECL|variable|impl
name|'impl'
op|'='
name|'types'
op|'.'
name|'String'
op|'('
number|'43'
op|')'
op|'.'
name|'with_variant'
op|'('
name|'postgresql'
op|'.'
name|'INET'
op|'('
op|')'
op|','
string|"'postgresql'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|process_bind_param
name|'def'
name|'process_bind_param'
op|'('
name|'self'
op|','
name|'value'
op|','
name|'dialect'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Process/Formats the value before insert it into the db."""'
newline|'\n'
comment|'# NOTE(sdague): normalize all the inserts'
nl|'\n'
name|'if'
name|'utils'
op|'.'
name|'is_valid_ipv6_cidr'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'utils'
op|'.'
name|'get_shortened_ipv6_cidr'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'value'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
