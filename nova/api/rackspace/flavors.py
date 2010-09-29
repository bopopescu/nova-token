begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
DECL|class|Controller
name|'class'
name|'Controller'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Flavor controller for the Rackspace API."""'
newline|'\n'
nl|'\n'
DECL|variable|_serialization_metadata
name|'_serialization_metadata'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
op|'{'
nl|'\n'
string|'"flavor"'
op|':'
op|'['
string|'"id"'
op|','
string|'"name"'
op|','
string|'"ram"'
op|','
string|'"disk"'
op|']'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return all flavors in brief."""'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'flavors'
op|'='
op|'['
name|'dict'
op|'('
name|'id'
op|'='
name|'flavor'
op|'['
string|"'id'"
op|']'
op|','
name|'name'
op|'='
name|'flavor'
op|'['
string|"'name'"
op|']'
op|')'
nl|'\n'
name|'for'
name|'flavor'
name|'in'
name|'self'
op|'.'
name|'detail'
op|'('
name|'req'
op|')'
op|'['
string|"'flavors'"
op|']'
op|']'
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
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return all flavors in detail."""'
newline|'\n'
name|'items'
op|'='
op|'['
name|'self'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'id'
op|')'
op|'['
string|"'flavor'"
op|']'
name|'for'
name|'id'
name|'in'
name|'self'
op|'.'
name|'_all_ids'
op|'('
op|')'
op|']'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'flavors'
op|'='
name|'items'
op|')'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about the given flavor id."""'
newline|'\n'
name|'for'
name|'name'
op|','
name|'val'
name|'in'
name|'instance_types'
op|'.'
name|'INSTANCE_TYPES'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'val'
op|'['
string|"'flavorid'"
op|']'
op|'=='
name|'int'
op|'('
name|'id'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'item'
op|'='
name|'dict'
op|'('
name|'ram'
op|'='
name|'val'
op|'['
string|"'memory_mb'"
op|']'
op|','
name|'disk'
op|'='
name|'val'
op|'['
string|"'local_gb'"
op|']'
op|','
nl|'\n'
name|'id'
op|'='
name|'val'
op|'['
string|"'flavorid'"
op|']'
op|','
name|'name'
op|'='
name|'name'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'flavor'
op|'='
name|'item'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_all_ids
dedent|''
name|'def'
name|'_all_ids'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the list of all flavorids."""'
newline|'\n'
name|'return'
op|'['
name|'i'
op|'['
string|"'flavorid'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instance_types'
op|'.'
name|'INSTANCE_TYPES'
op|'.'
name|'values'
op|'('
op|')'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
