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
name|'hashlib'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
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
name|'views'
name|'import'
name|'addresses'
name|'as'
name|'addresses_view'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
name|'import'
name|'flavors'
name|'as'
name|'flavors_view'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
name|'import'
name|'images'
name|'as'
name|'images_view'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_view_builder
name|'def'
name|'get_view_builder'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''\n    A factory method that returns the correct builder based on the version of\n    the api requested.\n    '''"
newline|'\n'
name|'version'
op|'='
name|'common'
op|'.'
name|'get_api_version'
op|'('
name|'req'
op|')'
newline|'\n'
name|'addresses_builder'
op|'='
name|'addresses_view'
op|'.'
name|'get_view_builder'
op|'('
name|'req'
op|')'
newline|'\n'
name|'if'
name|'version'
op|'=='
string|"'1.1'"
op|':'
newline|'\n'
indent|'        '
name|'flavor_builder'
op|'='
name|'flavors_view'
op|'.'
name|'get_view_builder'
op|'('
name|'req'
op|')'
newline|'\n'
name|'image_builder'
op|'='
name|'images_view'
op|'.'
name|'get_view_builder'
op|'('
name|'req'
op|')'
newline|'\n'
name|'return'
name|'ViewBuilder_1_1'
op|'('
name|'addresses_builder'
op|','
name|'flavor_builder'
op|','
nl|'\n'
name|'image_builder'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'ViewBuilder_1_0'
op|'('
name|'addresses_builder'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilder
dedent|''
dedent|''
name|'class'
name|'ViewBuilder'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''\n    Models a server response as a python dictionary.\n    Abstract methods: _build_image, _build_flavor\n    '''"
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'addresses_builder'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'addresses_builder'
op|'='
name|'addresses_builder'
newline|'\n'
nl|'\n'
DECL|member|build
dedent|''
name|'def'
name|'build'
op|'('
name|'self'
op|','
name|'inst'
op|','
name|'is_detail'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Coerces into dictionary format, mapping everything to\n        Rackspace-like attributes for return\n        """'
newline|'\n'
name|'if'
name|'is_detail'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'_build_detail'
op|'('
name|'inst'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'_build_simple'
op|'('
name|'inst'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_simple
dedent|''
dedent|''
name|'def'
name|'_build_simple'
op|'('
name|'self'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'dict'
op|'('
name|'server'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
name|'inst'
op|'['
string|"'id'"
op|']'
op|','
name|'name'
op|'='
name|'inst'
op|'['
string|"'display_name'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_detail
dedent|''
name|'def'
name|'_build_detail'
op|'('
name|'self'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'power_mapping'
op|'='
op|'{'
nl|'\n'
name|'None'
op|':'
string|"'build'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'NOSTATE'
op|':'
string|"'build'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'RUNNING'
op|':'
string|"'active'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'BLOCKED'
op|':'
string|"'active'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'SUSPENDED'
op|':'
string|"'suspended'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'PAUSED'
op|':'
string|"'paused'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|':'
string|"'active'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'SHUTOFF'
op|':'
string|"'active'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'CRASHED'
op|':'
string|"'error'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'FAILED'
op|':'
string|"'error'"
op|'}'
newline|'\n'
name|'inst_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|"#mapped_keys = dict(status='state', imageId='image_id',"
nl|'\n'
comment|"#    flavorId='instance_type', name='display_name', id='id')"
nl|'\n'
nl|'\n'
name|'mapped_keys'
op|'='
name|'dict'
op|'('
name|'status'
op|'='
string|"'state'"
op|','
name|'name'
op|'='
string|"'display_name'"
op|','
name|'id'
op|'='
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'mapped_keys'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'inst_dict'
op|'['
name|'k'
op|']'
op|'='
name|'inst'
op|'['
name|'v'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'inst_dict'
op|'['
string|"'status'"
op|']'
op|'='
name|'power_mapping'
op|'['
name|'inst_dict'
op|'['
string|"'status'"
op|']'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ctxt'
op|'='
name|'nova'
op|'.'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'migration'
op|'='
name|'db'
op|'.'
name|'migration_get_by_instance_and_status'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'inst'
op|'['
string|"'id'"
op|']'
op|','
string|"'finished'"
op|')'
newline|'\n'
name|'inst_dict'
op|'['
string|"'status'"
op|']'
op|'='
string|"'resize-confirm'"
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'inst_dict'
op|'['
string|"'addresses'"
op|']'
op|'='
name|'self'
op|'.'
name|'addresses_builder'
op|'.'
name|'build'
op|'('
name|'inst'
op|')'
newline|'\n'
nl|'\n'
comment|'# Return the metadata as a dictionary'
nl|'\n'
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'inst'
op|'['
string|"'metadata'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'['
name|'item'
op|'['
string|"'key'"
op|']'
op|']'
op|'='
name|'item'
op|'['
string|"'value'"
op|']'
newline|'\n'
dedent|''
name|'inst_dict'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'metadata'
newline|'\n'
nl|'\n'
name|'inst_dict'
op|'['
string|"'hostId'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'if'
name|'inst'
op|'['
string|"'host'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'inst_dict'
op|'['
string|"'hostId'"
op|']'
op|'='
name|'hashlib'
op|'.'
name|'sha224'
op|'('
name|'inst'
op|'['
string|"'host'"
op|']'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_build_image'
op|'('
name|'inst_dict'
op|','
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_build_flavor'
op|'('
name|'inst_dict'
op|','
name|'inst'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'dict'
op|'('
name|'server'
op|'='
name|'inst_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_image
dedent|''
name|'def'
name|'_build_image'
op|'('
name|'self'
op|','
name|'response'
op|','
name|'inst'
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
DECL|member|_build_flavor
dedent|''
name|'def'
name|'_build_flavor'
op|'('
name|'self'
op|','
name|'response'
op|','
name|'inst'
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
nl|'\n'
DECL|class|ViewBuilder_1_0
dedent|''
dedent|''
name|'class'
name|'ViewBuilder_1_0'
op|'('
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|_build_image
indent|'    '
name|'def'
name|'_build_image'
op|'('
name|'self'
op|','
name|'response'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'['
string|'"imageId"'
op|']'
op|'='
name|'inst'
op|'['
string|'"image_id"'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_build_flavor
dedent|''
name|'def'
name|'_build_flavor'
op|'('
name|'self'
op|','
name|'response'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'['
string|'"flavorId"'
op|']'
op|'='
name|'inst'
op|'['
string|'"instance_type"'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilder_1_1
dedent|''
dedent|''
name|'class'
name|'ViewBuilder_1_1'
op|'('
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'addresses_builder'
op|','
name|'flavor_builder'
op|','
name|'image_builder'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ViewBuilder'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'addresses_builder'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flavor_builder'
op|'='
name|'flavor_builder'
newline|'\n'
name|'self'
op|'.'
name|'image_builder'
op|'='
name|'image_builder'
newline|'\n'
nl|'\n'
DECL|member|_build_image
dedent|''
name|'def'
name|'_build_image'
op|'('
name|'self'
op|','
name|'response'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
name|'inst'
op|'['
string|'"image_id"'
op|']'
newline|'\n'
name|'response'
op|'['
string|'"imageRef"'
op|']'
op|'='
name|'self'
op|'.'
name|'image_builder'
op|'.'
name|'generate_href'
op|'('
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_flavor
dedent|''
name|'def'
name|'_build_flavor'
op|'('
name|'self'
op|','
name|'response'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor_id'
op|'='
name|'inst'
op|'['
string|'"instance_type"'
op|']'
newline|'\n'
name|'response'
op|'['
string|'"flavorRef"'
op|']'
op|'='
name|'self'
op|'.'
name|'flavor_builder'
op|'.'
name|'generate_href'
op|'('
name|'flavor_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
