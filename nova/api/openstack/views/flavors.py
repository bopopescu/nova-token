begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010-2011 OpenStack LLC.'
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
name|'os'
op|'.'
name|'path'
newline|'\n'
nl|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilder
name|'class'
name|'ViewBuilder'
op|'('
name|'common'
op|'.'
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|_collection_name
indent|'    '
name|'_collection_name'
op|'='
string|'"flavors"'
newline|'\n'
nl|'\n'
DECL|member|basic
name|'def'
name|'basic'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|'"flavor"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'flavor'
op|'['
string|'"flavorid"'
op|']'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'flavor'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
string|'"links"'
op|':'
name|'self'
op|'.'
name|'_get_links'
op|'('
name|'request'
op|','
name|'flavor'
op|'['
string|'"flavorid"'
op|']'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|'"flavor"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'flavor'
op|'['
string|'"flavorid"'
op|']'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'flavor'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
string|'"ram"'
op|':'
name|'flavor'
op|'['
string|'"memory_mb"'
op|']'
op|','
nl|'\n'
string|'"disk"'
op|':'
name|'flavor'
op|'['
string|'"local_gb"'
op|']'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
name|'flavor'
op|'.'
name|'get'
op|'('
string|'"vcpus"'
op|')'
name|'or'
string|'""'
op|','
nl|'\n'
string|'"swap"'
op|':'
name|'flavor'
op|'.'
name|'get'
op|'('
string|'"swap"'
op|')'
name|'or'
string|'""'
op|','
nl|'\n'
string|'"rxtx_quota"'
op|':'
name|'flavor'
op|'.'
name|'get'
op|'('
string|'"rxtx_quota"'
op|')'
name|'or'
string|'""'
op|','
nl|'\n'
string|'"rxtx_cap"'
op|':'
name|'flavor'
op|'.'
name|'get'
op|'('
string|'"rxtx_cap"'
op|')'
name|'or'
string|'""'
op|','
nl|'\n'
string|'"links"'
op|':'
name|'self'
op|'.'
name|'_get_links'
op|'('
name|'request'
op|','
name|'flavor'
op|'['
string|'"flavorid"'
op|']'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'flavors'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the \'index\' view of flavors."""'
newline|'\n'
DECL|function|_get_flavors
name|'def'
name|'_get_flavors'
op|'('
name|'request'
op|','
name|'flavors'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'_'
op|','
name|'flavor'
name|'in'
name|'flavors'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'self'
op|'.'
name|'basic'
op|'('
name|'request'
op|','
name|'flavor'
op|')'
op|'['
string|'"flavor"'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'dict'
op|'('
name|'flavors'
op|'='
name|'list'
op|'('
name|'_get_flavors'
op|'('
name|'request'
op|','
name|'flavors'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detail
dedent|''
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'flavors'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the \'detail\' view of flavors."""'
newline|'\n'
DECL|function|_get_flavors
name|'def'
name|'_get_flavors'
op|'('
name|'request'
op|','
name|'flavors'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'_'
op|','
name|'flavor'
name|'in'
name|'flavors'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'self'
op|'.'
name|'show'
op|'('
name|'request'
op|','
name|'flavor'
op|')'
op|'['
string|'"flavor"'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'dict'
op|'('
name|'flavors'
op|'='
name|'list'
op|'('
name|'_get_flavors'
op|'('
name|'request'
op|','
name|'flavors'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
