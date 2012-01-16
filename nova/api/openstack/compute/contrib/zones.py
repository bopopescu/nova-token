begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
string|'"""The zones extension."""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
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
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'crypto'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'api'
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
string|'"nova.api.openstack.compute.contrib.zones"'
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CapabilitySelector
name|'class'
name|'CapabilitySelector'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__call__
indent|'    '
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'obj'
op|','
name|'do_raise'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'obj'
op|'.'
name|'items'
op|'('
op|')'
nl|'\n'
name|'if'
name|'k'
name|'not'
name|'in'
op|'('
string|"'id'"
op|','
string|"'api_url'"
op|','
string|"'name'"
op|','
string|"'capabilities'"
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_zone
dedent|''
dedent|''
name|'def'
name|'make_zone'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'elem'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'api_url'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'capabilities'"
op|')'
newline|'\n'
nl|'\n'
name|'cap'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'elem'
op|','
name|'xmlutil'
op|'.'
name|'Selector'
op|'('
number|'0'
op|')'
op|','
nl|'\n'
name|'selector'
op|'='
name|'CapabilitySelector'
op|'('
op|')'
op|')'
newline|'\n'
name|'cap'
op|'.'
name|'text'
op|'='
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|zone_nsmap
dedent|''
name|'zone_nsmap'
op|'='
op|'{'
name|'None'
op|':'
name|'wsgi'
op|'.'
name|'XMLNS_V10'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ZoneTemplate
name|'class'
name|'ZoneTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'zone'"
op|','
name|'selector'
op|'='
string|"'zone'"
op|')'
newline|'\n'
name|'make_zone'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
name|'zone_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ZonesTemplate
dedent|''
dedent|''
name|'class'
name|'ZonesTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'zones'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'zone'"
op|','
name|'selector'
op|'='
string|"'zones'"
op|')'
newline|'\n'
name|'make_zone'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
name|'zone_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WeightsTemplate
dedent|''
dedent|''
name|'class'
name|'WeightsTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'weights'"
op|')'
newline|'\n'
name|'weight'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'weight'"
op|','
name|'selector'
op|'='
string|"'weights'"
op|')'
newline|'\n'
name|'blob'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'weight'
op|','
string|"'blob'"
op|')'
newline|'\n'
name|'blob'
op|'.'
name|'text'
op|'='
string|"'blob'"
newline|'\n'
name|'inner_weight'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'weight'
op|','
string|"'weight'"
op|')'
newline|'\n'
name|'inner_weight'
op|'.'
name|'text'
op|'='
string|"'weight'"
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
name|'zone_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_filter_keys
dedent|''
dedent|''
name|'def'
name|'_filter_keys'
op|'('
name|'item'
op|','
name|'keys'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Filters all model attributes except for keys\n    item is a dict\n\n    """'
newline|'\n'
name|'return'
name|'dict'
op|'('
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'item'
op|'.'
name|'iteritems'
op|'('
op|')'
name|'if'
name|'k'
name|'in'
name|'keys'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_exclude_keys
dedent|''
name|'def'
name|'_exclude_keys'
op|'('
name|'item'
op|','
name|'keys'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'dict'
op|'('
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'item'
op|'.'
name|'iteritems'
op|'('
op|')'
name|'if'
name|'k'
name|'and'
op|'('
name|'k'
name|'not'
name|'in'
name|'keys'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_scrub_zone
dedent|''
name|'def'
name|'_scrub_zone'
op|'('
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_exclude_keys'
op|'('
name|'zone'
op|','
op|'('
string|"'username'"
op|','
string|"'password'"
op|','
string|"'created_at'"
op|','
nl|'\n'
string|"'deleted'"
op|','
string|"'deleted_at'"
op|','
string|"'updated_at'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_encryption_key
dedent|''
name|'def'
name|'check_encryption_key'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
DECL|function|wrapped
indent|'    '
name|'def'
name|'wrapped'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'build_plan_encryption_key'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"--build_plan_encryption_key not set"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'func'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'wrapped'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
dedent|''
name|'class'
name|'Controller'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Controller for Zone resources."""'
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
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ZonesTemplate'
op|')'
newline|'\n'
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
string|'"""Return all zones in brief"""'
newline|'\n'
comment|'# Ask the ZoneManager in the Scheduler for most recent data,'
nl|'\n'
comment|'# or fall-back to the database ...'
nl|'\n'
name|'items'
op|'='
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'api'
op|'.'
name|'get_zone_list'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'items'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'items'
op|','
name|'req'
op|')'
newline|'\n'
name|'items'
op|'='
op|'['
name|'_scrub_zone'
op|'('
name|'item'
op|')'
name|'for'
name|'item'
name|'in'
name|'items'
op|']'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'zones'
op|'='
name|'items'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ZonesTemplate'
op|')'
newline|'\n'
DECL|member|detail
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
string|'"""Return all zones in detail"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ZoneTemplate'
op|')'
newline|'\n'
DECL|member|info
name|'def'
name|'info'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return name and capabilities for this zone."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'zone_capabs'
op|'='
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'api'
op|'.'
name|'get_zone_capabilities'
op|'('
name|'context'
op|')'
newline|'\n'
comment|'# NOTE(comstud): This should probably return, instead:'
nl|'\n'
comment|"# {'zone': {'name': FLAGS.zone_name,"
nl|'\n'
comment|"#           'capabilities': zone_capabs}}"
nl|'\n'
name|'zone_capabs'
op|'['
string|"'name'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'zone_name'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'zone'
op|'='
name|'zone_capabs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ZoneTemplate'
op|')'
newline|'\n'
DECL|member|show
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
string|'"""Return data about the given zone id"""'
newline|'\n'
name|'zone_id'
op|'='
name|'int'
op|'('
name|'id'
op|')'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'zone'
op|'='
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'api'
op|'.'
name|'zone_get'
op|'('
name|'context'
op|','
name|'zone_id'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'zone'
op|'='
name|'_scrub_zone'
op|'('
name|'zone'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
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
string|'"""Delete a child zone entry."""'
newline|'\n'
name|'zone_id'
op|'='
name|'int'
op|'('
name|'id'
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'api'
op|'.'
name|'zone_delete'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'zone_id'
op|')'
newline|'\n'
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ZoneTemplate'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'deserializers'
op|'('
name|'xml'
op|'='
name|'servers'
op|'.'
name|'CreateDeserializer'
op|')'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a child zone entry."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'zone'
op|'='
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'api'
op|'.'
name|'zone_create'
op|'('
name|'context'
op|','
name|'body'
op|'['
string|'"zone"'
op|']'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'zone'
op|'='
name|'_scrub_zone'
op|'('
name|'zone'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ZoneTemplate'
op|')'
newline|'\n'
DECL|member|update
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update a child zone entry."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'zone_id'
op|'='
name|'int'
op|'('
name|'id'
op|')'
newline|'\n'
name|'zone'
op|'='
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'api'
op|'.'
name|'zone_update'
op|'('
name|'context'
op|','
name|'zone_id'
op|','
name|'body'
op|'['
string|'"zone"'
op|']'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'zone'
op|'='
name|'_scrub_zone'
op|'('
name|'zone'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'WeightsTemplate'
op|')'
newline|'\n'
op|'@'
name|'check_encryption_key'
newline|'\n'
DECL|member|select
name|'def'
name|'select'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a weighted list of costs to create instances\n           of desired capabilities."""'
newline|'\n'
name|'ctx'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'specs'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'body'
op|')'
newline|'\n'
name|'build_plan'
op|'='
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'api'
op|'.'
name|'select'
op|'('
name|'ctx'
op|','
name|'specs'
op|'='
name|'specs'
op|')'
newline|'\n'
name|'cooked'
op|'='
name|'self'
op|'.'
name|'_scrub_build_plan'
op|'('
name|'build_plan'
op|')'
newline|'\n'
name|'return'
op|'{'
string|'"weights"'
op|':'
name|'cooked'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_scrub_build_plan
dedent|''
name|'def'
name|'_scrub_build_plan'
op|'('
name|'self'
op|','
name|'build_plan'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove all the confidential data and return a sanitized\n        version of the build plan. Include an encrypted full version\n        of the weighting entry so we can get back to it later."""'
newline|'\n'
name|'encryptor'
op|'='
name|'crypto'
op|'.'
name|'encryptor'
op|'('
name|'FLAGS'
op|'.'
name|'build_plan_encryption_key'
op|')'
newline|'\n'
name|'cooked'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'entry'
name|'in'
name|'build_plan'
op|':'
newline|'\n'
indent|'            '
name|'json_entry'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'entry'
op|')'
newline|'\n'
name|'cipher_text'
op|'='
name|'encryptor'
op|'('
name|'json_entry'
op|')'
newline|'\n'
name|'cooked'
op|'.'
name|'append'
op|'('
name|'dict'
op|'('
name|'weight'
op|'='
name|'entry'
op|'['
string|"'weight'"
op|']'
op|','
nl|'\n'
name|'blob'
op|'='
name|'cipher_text'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cooked'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ZonesXMLSerializer
dedent|''
dedent|''
name|'class'
name|'ZonesXMLSerializer'
op|'('
name|'xmlutil'
op|'.'
name|'XMLTemplateSerializer'
op|')'
op|':'
newline|'\n'
DECL|member|index
indent|'    '
name|'def'
name|'index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'ZonesTemplate'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|detail
dedent|''
name|'def'
name|'detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'ZonesTemplate'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|select
dedent|''
name|'def'
name|'select'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'WeightsTemplate'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|default
dedent|''
name|'def'
name|'default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'ZoneTemplate'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Zones
dedent|''
dedent|''
name|'class'
name|'Zones'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Enables zones-related functionality such as adding child zones,\n    listing child zones, getting the capabilities of the local zone,\n    and returning build plans to parent zones\' schedulers\n    """'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Zones"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-zones"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/zones/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-09-21T00:00:00+00:00"'
newline|'\n'
DECL|variable|admin_only
name|'admin_only'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"#NOTE(bcwaldon): This resource should be prefixed with 'os-'"
nl|'\n'
indent|'        '
name|'coll_actions'
op|'='
op|'{'
nl|'\n'
string|"'detail'"
op|':'
string|"'GET'"
op|','
nl|'\n'
string|"'info'"
op|':'
string|"'GET'"
op|','
nl|'\n'
string|"'select'"
op|':'
string|"'POST'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'zones'"
op|','
nl|'\n'
name|'Controller'
op|'('
op|')'
op|','
nl|'\n'
name|'collection_actions'
op|'='
name|'coll_actions'
op|')'
newline|'\n'
name|'return'
op|'['
name|'res'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
