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
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'faults'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
name|'as'
name|'auth_manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
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
name|'api'
op|'.'
name|'openstack'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_entity_list
name|'def'
name|'_entity_list'
op|'('
name|'entities'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Coerces a list of servers into proper dictionary format """'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'servers'
op|'='
name|'entities'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_entity_detail
dedent|''
name|'def'
name|'_entity_detail'
op|'('
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Maps everything to Rackspace-like attributes for return"""'
newline|'\n'
name|'power_mapping'
op|'='
op|'{'
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
name|'PAUSED'
op|':'
string|"'suspended'"
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
op|'}'
newline|'\n'
name|'inst_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'mapped_keys'
op|'='
name|'dict'
op|'('
name|'status'
op|'='
string|"'state'"
op|','
name|'imageId'
op|'='
string|"'image_id'"
op|','
nl|'\n'
name|'flavorId'
op|'='
string|"'instance_type'"
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
indent|'        '
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
name|'inst_dict'
op|'['
string|"'addresses'"
op|']'
op|'='
name|'dict'
op|'('
name|'public'
op|'='
op|'['
op|']'
op|','
name|'private'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'inst_dict'
op|'['
string|"'metadata'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'inst_dict'
op|'['
string|"'hostId'"
op|']'
op|'='
string|"''"
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
nl|'\n'
DECL|function|_entity_inst
dedent|''
name|'def'
name|'_entity_inst'
op|'('
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Filters all model attributes save for id and name """'
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
nl|'\n'
DECL|class|Controller
dedent|''
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
string|'""" The Server API controller for the OpenStack API """'
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
string|'"server"'
op|':'
op|'['
string|'"id"'
op|','
string|'"imageId"'
op|','
string|'"name"'
op|','
string|'"flavorId"'
op|','
string|'"hostId"'
op|','
nl|'\n'
string|'"status"'
op|','
string|'"progress"'
op|']'
op|'}'
op|'}'
op|'}'
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
name|'compute_api'
op|'.'
name|'ComputeAPI'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'Controller'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
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
string|'""" Returns a list of server names and ids for a given user """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_items'
op|'('
name|'req'
op|','
name|'entity_maker'
op|'='
name|'_entity_inst'
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
string|'""" Returns a list of server details for a given user """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_items'
op|'('
name|'req'
op|','
name|'entity_maker'
op|'='
name|'_entity_detail'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_items
dedent|''
name|'def'
name|'_items'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'entity_maker'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of servers for a given user.\n\n        entity_maker - either _entity_detail or _entity_inst\n        """'
newline|'\n'
name|'user_id'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user_id'
op|','
name|'user_id'
op|')'
newline|'\n'
name|'instance_list'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_instances'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'limited_list'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'limited'
op|'('
name|'instance_list'
op|','
name|'req'
op|')'
newline|'\n'
name|'res'
op|'='
op|'['
name|'entity_maker'
op|'('
name|'inst'
op|')'
op|'['
string|"'server'"
op|']'
name|'for'
name|'inst'
name|'in'
name|'limited_list'
op|']'
newline|'\n'
name|'return'
name|'_entity_list'
op|'('
name|'res'
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
string|'""" Returns server details by server id """'
newline|'\n'
name|'user_id'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user_id'
op|','
name|'user_id'
op|')'
newline|'\n'
name|'inst'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_instance'
op|'('
name|'ctxt'
op|','
name|'int'
op|'('
name|'id'
op|')'
op|')'
newline|'\n'
name|'if'
name|'inst'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'inst'
op|'.'
name|'user_id'
op|'=='
name|'user_id'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'_entity_detail'
op|'('
name|'inst'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
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
string|'""" Destroys a server """'
newline|'\n'
name|'user_id'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user_id'
op|','
name|'user_id'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'delete_instance'
op|'('
name|'ctxt'
op|','
name|'int'
op|'('
name|'id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Creates a new server for a given user """'
newline|'\n'
name|'env'
op|'='
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'req'
op|'.'
name|'body'
op|','
name|'req'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'env'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'user_id'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user_id'
op|','
name|'user_id'
op|')'
newline|'\n'
name|'key_pair'
op|'='
name|'auth_manager'
op|'.'
name|'AuthManager'
op|'.'
name|'get_key_pairs'
op|'('
name|'ctxt'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'instances'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'create_instances'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'get_by_flavor_id'
op|'('
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'flavorId'"
op|']'
op|')'
op|','
nl|'\n'
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'imageId'"
op|']'
op|','
nl|'\n'
name|'display_name'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'description'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'key_name'
op|'='
name|'key_pair'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'key_data'
op|'='
name|'key_pair'
op|'['
string|"'public_key'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'_entity_inst'
op|'('
name|'instances'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
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
string|'""" Updates the server name or password """'
newline|'\n'
name|'user_id'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user_id'
op|','
name|'user_id'
op|')'
newline|'\n'
name|'inst_dict'
op|'='
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'req'
op|'.'
name|'body'
op|','
name|'req'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'inst_dict'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'update_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
string|"'adminPass'"
name|'in'
name|'inst_dict'
op|'['
string|"'server'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'update_dict'
op|'['
string|"'admin_pass'"
op|']'
op|'='
name|'inst_dict'
op|'['
string|"'server'"
op|']'
op|'['
string|"'adminPass'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'name'"
name|'in'
name|'inst_dict'
op|'['
string|"'server'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'update_dict'
op|'['
string|"'display_name'"
op|']'
op|'='
name|'inst_dict'
op|'['
string|"'server'"
op|']'
op|'['
string|"'name'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'update_instance'
op|'('
name|'ctxt'
op|','
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'**'
name|'update_dict'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPNoContent'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|action
dedent|''
name|'def'
name|'action'
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
string|'""" Multi-purpose method used to reboot, rebuild, and\n        resize a server """'
newline|'\n'
name|'user_id'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user_id'
op|','
name|'user_id'
op|')'
newline|'\n'
name|'input_dict'
op|'='
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'req'
op|'.'
name|'body'
op|','
name|'req'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'reboot_type'
op|'='
name|'input_dict'
op|'['
string|"'reboot'"
op|']'
op|'['
string|"'type'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# TODO(gundlach): pass reboot_type, support soft reboot in'
nl|'\n'
comment|'# virt driver'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'reboot'
op|'('
name|'ctxt'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
