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
name|'datetime'
newline|'\n'
name|'import'
name|'hashlib'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'compute'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'context'
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
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilder
name|'class'
name|'ViewBuilder'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Model a server response as a python dictionary.\n\n    Public methods: build\n    Abstract methods: _build_image, _build_flavor\n\n    """'
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
string|'"""Return a dict that represenst a server."""'
newline|'\n'
name|'if'
name|'inst'
op|'.'
name|'get'
op|'('
string|"'_is_precooked'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'dict'
op|'('
name|'server'
op|'='
name|'inst'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'is_detail'
op|':'
newline|'\n'
indent|'                '
name|'server'
op|'='
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
indent|'                '
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_simple'
op|'('
name|'inst'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_build_extra'
op|'('
name|'server'
op|'['
string|"'server'"
op|']'
op|','
name|'inst'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'server'
newline|'\n'
nl|'\n'
DECL|member|_build_simple
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
indent|'        '
string|'"""Return a simple model of a server."""'
newline|'\n'
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
string|'"""Returns a detailed model of a server."""'
newline|'\n'
name|'vm_state'
op|'='
name|'inst'
op|'.'
name|'get'
op|'('
string|"'vm_state'"
op|','
name|'vm_states'
op|'.'
name|'BUILDING'
op|')'
newline|'\n'
name|'task_state'
op|'='
name|'inst'
op|'.'
name|'get'
op|'('
string|"'task_state'"
op|')'
newline|'\n'
nl|'\n'
name|'inst_dict'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'inst'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'inst'
op|'['
string|"'display_name'"
op|']'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'common'
op|'.'
name|'status_from_state'
op|'('
name|'vm_state'
op|','
name|'task_state'
op|')'
op|'}'
newline|'\n'
nl|'\n'
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
name|'compute_api'
op|'='
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'compute_api'
op|'.'
name|'has_finished_migration'
op|'('
name|'ctxt'
op|','
name|'inst'
op|'['
string|"'uuid'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'inst_dict'
op|'['
string|"'status'"
op|']'
op|'='
string|"'RESIZE-CONFIRM'"
newline|'\n'
nl|'\n'
comment|'# Return the metadata as a dictionary'
nl|'\n'
dedent|''
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'inst'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|','
op|'['
op|']'
op|')'
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
name|'str'
op|'('
name|'item'
op|'['
string|"'value'"
op|']'
op|')'
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
op|'.'
name|'get'
op|'('
string|"'host'"
op|')'
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
name|'self'
op|'.'
name|'_build_addresses'
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
DECL|member|_build_addresses
dedent|''
name|'def'
name|'_build_addresses'
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
string|'"""Return the addresses sub-resource of a server."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Return the image sub-resource of a server."""'
newline|'\n'
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
string|'"""Return the flavor sub-resource of a server."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_extra
dedent|''
name|'def'
name|'_build_extra'
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
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilderV10
dedent|''
dedent|''
name|'class'
name|'ViewBuilderV10'
op|'('
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Model an Openstack API V1.0 server response."""'
newline|'\n'
nl|'\n'
DECL|member|_build_extra
name|'def'
name|'_build_extra'
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
string|"'uuid'"
op|']'
op|'='
name|'inst'
op|'['
string|"'uuid'"
op|']'
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
name|'if'
name|'inst'
op|'.'
name|'get'
op|'('
string|"'image_ref'"
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image_ref'
op|'='
name|'inst'
op|'['
string|"'image_ref'"
op|']'
newline|'\n'
name|'if'
name|'str'
op|'('
name|'image_ref'
op|')'
op|'.'
name|'startswith'
op|'('
string|"'http'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'ListingImageRefsNotSupported'
op|'('
op|')'
newline|'\n'
dedent|''
name|'response'
op|'['
string|"'imageId'"
op|']'
op|'='
name|'int'
op|'('
name|'image_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_flavor
dedent|''
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
name|'if'
name|'inst'
op|'.'
name|'get'
op|'('
string|"'instance_type'"
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'response'
op|'['
string|"'flavorId'"
op|']'
op|'='
name|'inst'
op|'['
string|"'instance_type'"
op|']'
op|'['
string|"'flavorid'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_build_addresses
dedent|''
dedent|''
name|'def'
name|'_build_addresses'
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
nl|'\n'
DECL|class|ViewBuilderV11
dedent|''
dedent|''
name|'class'
name|'ViewBuilderV11'
op|'('
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Model an Openstack API V1.0 server response."""'
newline|'\n'
DECL|member|__init__
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
op|','
nl|'\n'
name|'base_url'
op|','
name|'project_id'
op|'='
string|'""'
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
name|'self'
op|'.'
name|'base_url'
op|'='
name|'base_url'
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
name|'project_id'
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
name|'response'
op|'='
name|'super'
op|'('
name|'ViewBuilderV11'
op|','
name|'self'
op|')'
op|'.'
name|'_build_detail'
op|'('
name|'inst'
op|')'
newline|'\n'
name|'response'
op|'['
string|"'server'"
op|']'
op|'['
string|"'created'"
op|']'
op|'='
name|'utils'
op|'.'
name|'isotime'
op|'('
name|'inst'
op|'['
string|"'created_at'"
op|']'
op|')'
newline|'\n'
name|'response'
op|'['
string|"'server'"
op|']'
op|'['
string|"'updated'"
op|']'
op|'='
name|'utils'
op|'.'
name|'isotime'
op|'('
name|'inst'
op|'['
string|"'updated_at'"
op|']'
op|')'
newline|'\n'
name|'if'
string|"'status'"
name|'in'
name|'response'
op|'['
string|"'server'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'response'
op|'['
string|"'server'"
op|']'
op|'['
string|"'status'"
op|']'
op|'=='
string|'"ACTIVE"'
op|':'
newline|'\n'
indent|'                '
name|'response'
op|'['
string|"'server'"
op|']'
op|'['
string|"'progress'"
op|']'
op|'='
number|'100'
newline|'\n'
dedent|''
name|'elif'
name|'response'
op|'['
string|"'server'"
op|']'
op|'['
string|"'status'"
op|']'
op|'=='
string|'"BUILD"'
op|':'
newline|'\n'
indent|'                '
name|'response'
op|'['
string|"'server'"
op|']'
op|'['
string|"'progress'"
op|']'
op|'='
number|'0'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'response'
op|'['
string|"'server'"
op|']'
op|'['
string|"'accessIPv4'"
op|']'
op|'='
name|'inst'
op|'.'
name|'get'
op|'('
string|"'access_ip_v4'"
op|')'
name|'or'
string|'""'
newline|'\n'
name|'response'
op|'['
string|"'server'"
op|']'
op|'['
string|"'accessIPv6'"
op|']'
op|'='
name|'inst'
op|'.'
name|'get'
op|'('
string|"'access_ip_v6'"
op|')'
name|'or'
string|'""'
newline|'\n'
nl|'\n'
name|'return'
name|'response'
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
name|'if'
name|'inst'
op|'.'
name|'get'
op|'('
string|'"image_ref"'
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image_href'
op|'='
name|'inst'
op|'['
string|"'image_ref'"
op|']'
newline|'\n'
name|'image_id'
op|'='
name|'str'
op|'('
name|'common'
op|'.'
name|'get_id_from_href'
op|'('
name|'image_href'
op|')'
op|')'
newline|'\n'
name|'_bookmark'
op|'='
name|'self'
op|'.'
name|'image_builder'
op|'.'
name|'generate_bookmark'
op|'('
name|'image_id'
op|')'
newline|'\n'
name|'response'
op|'['
string|"'image'"
op|']'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'image_id'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'_bookmark'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_build_flavor
dedent|''
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
name|'if'
name|'inst'
op|'.'
name|'get'
op|'('
string|'"instance_type"'
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'flavor_id'
op|'='
name|'inst'
op|'['
string|'"instance_type"'
op|']'
op|'['
string|"'flavorid'"
op|']'
newline|'\n'
name|'flavor_ref'
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
name|'flavor_bookmark'
op|'='
name|'self'
op|'.'
name|'flavor_builder'
op|'.'
name|'generate_bookmark'
op|'('
name|'flavor_id'
op|')'
newline|'\n'
name|'response'
op|'['
string|'"flavor"'
op|']'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'str'
op|'('
name|'common'
op|'.'
name|'get_id_from_href'
op|'('
name|'flavor_ref'
op|')'
op|')'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'flavor_bookmark'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_build_addresses
dedent|''
dedent|''
name|'def'
name|'_build_addresses'
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
name|'interfaces'
op|'='
name|'inst'
op|'.'
name|'get'
op|'('
string|"'virtual_interfaces'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'response'
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
name|'interfaces'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_extra
dedent|''
name|'def'
name|'_build_extra'
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
name|'self'
op|'.'
name|'_build_links'
op|'('
name|'response'
op|','
name|'inst'
op|')'
newline|'\n'
name|'response'
op|'['
string|"'uuid'"
op|']'
op|'='
name|'inst'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_build_links
dedent|''
name|'def'
name|'_build_links'
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
name|'href'
op|'='
name|'self'
op|'.'
name|'generate_href'
op|'('
name|'inst'
op|'['
string|'"id"'
op|']'
op|')'
newline|'\n'
name|'bookmark'
op|'='
name|'self'
op|'.'
name|'generate_bookmark'
op|'('
name|'inst'
op|'['
string|'"id"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'links'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'href'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'bookmark'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'response'
op|'['
string|'"links"'
op|']'
op|'='
name|'links'
newline|'\n'
nl|'\n'
DECL|member|generate_href
dedent|''
name|'def'
name|'generate_href'
op|'('
name|'self'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create an url that refers to a specific server id."""'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'base_url'
op|','
name|'self'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|'"servers"'
op|','
name|'str'
op|'('
name|'server_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|generate_bookmark
dedent|''
name|'def'
name|'generate_bookmark'
op|'('
name|'self'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create an url that refers to a specific flavor id."""'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'common'
op|'.'
name|'remove_version_from_href'
op|'('
name|'self'
op|'.'
name|'base_url'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'project_id'
op|','
string|'"servers"'
op|','
name|'str'
op|'('
name|'server_id'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
