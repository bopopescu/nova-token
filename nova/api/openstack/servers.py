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
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
name|'import'
name|'cloud'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'context'
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
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'service'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|function|_filter_params
name|'def'
name|'_filter_params'
op|'('
name|'inst_dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Extracts all updatable parameters for a server update request """'
newline|'\n'
name|'keys'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'name'"
op|','
name|'admin_pass'
op|'='
string|"'adminPass'"
op|')'
newline|'\n'
name|'new_attrs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'keys'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'inst_dict'
op|'.'
name|'has_key'
op|'('
name|'v'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'new_attrs'
op|'['
name|'k'
op|']'
op|'='
name|'inst_dict'
op|'['
name|'v'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'new_attrs'
newline|'\n'
nl|'\n'
DECL|function|_entity_list
dedent|''
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
string|'""" Maps everything to valid attributes for return"""'
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
nl|'\n'
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
string|"'server_name'"
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
string|"'server_name'"
op|']'
op|')'
op|')'
newline|'\n'
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
op|','
string|'"progress"'
op|']'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'db_driver'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'db_driver'
op|':'
newline|'\n'
indent|'            '
name|'db_driver'
op|'='
name|'FLAGS'
op|'.'
name|'db_driver'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'db_driver'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'db_driver'
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
name|'instance_list'
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_get_all_by_user'
op|'('
name|'None'
op|','
name|'user_id'
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
name|'inst'
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_get_by_internal_id'
op|'('
name|'None'
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
name|'instance'
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_get_by_internal_id'
op|'('
name|'None'
op|','
name|'int'
op|'('
name|'id'
op|')'
op|')'
newline|'\n'
name|'if'
name|'instance'
name|'and'
name|'instance'
op|'['
string|"'user_id'"
op|']'
op|'=='
name|'user_id'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_destroy'
op|'('
name|'None'
op|','
name|'id'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
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
nl|'\n'
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
comment|'#try:'
nl|'\n'
dedent|''
name|'inst'
op|'='
name|'self'
op|'.'
name|'_build_server_instance'
op|'('
name|'req'
op|','
name|'env'
op|')'
newline|'\n'
comment|'#except Exception, e:'
nl|'\n'
comment|'#    return faults.Fault(exc.HTTPUnprocessableEntity())'
nl|'\n'
nl|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
op|'{'
nl|'\n'
string|'"method"'
op|':'
string|'"run_instance"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"instance_id"'
op|':'
name|'inst'
op|'['
string|"'id'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'_entity_inst'
op|'('
name|'inst'
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
nl|'\n'
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
nl|'\n'
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
name|'instance'
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_get_by_internal_id'
op|'('
name|'None'
op|','
name|'int'
op|'('
name|'id'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance'
name|'or'
name|'instance'
op|'.'
name|'user_id'
op|'!='
name|'user_id'
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
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_update'
op|'('
name|'None'
op|','
name|'int'
op|'('
name|'id'
op|')'
op|','
nl|'\n'
name|'_filter_params'
op|'('
name|'inst_dict'
op|'['
string|"'server'"
op|']'
op|')'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNoContent'
op|'('
op|')'
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
string|'""" multi-purpose method used to reboot, rebuild, and \n        resize a server """'
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
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'inst_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_by_internal_id'
op|'('
name|'None'
op|','
name|'int'
op|'('
name|'id'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'inst_ref'
name|'or'
op|'('
name|'inst_ref'
name|'and'
name|'not'
name|'inst_ref'
op|'.'
name|'user_id'
op|'=='
name|'user_id'
op|')'
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
name|'cloud'
op|'.'
name|'reboot'
op|'('
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_server_instance
dedent|''
name|'def'
name|'_build_server_instance'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'env'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Build instance data structure and save it to the data store."""'
newline|'\n'
name|'ltime'
op|'='
name|'time'
op|'.'
name|'strftime'
op|'('
string|"'%Y-%m-%dT%H:%M:%SZ'"
op|','
name|'time'
op|'.'
name|'gmtime'
op|'('
op|')'
op|')'
newline|'\n'
name|'inst'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
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
nl|'\n'
name|'flavor_id'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'flavorId'"
op|']'
newline|'\n'
nl|'\n'
name|'instance_type'
op|','
name|'flavor'
op|'='
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
nl|'\n'
name|'instance_types'
op|'.'
name|'INSTANCE_TYPES'
op|'.'
name|'iteritems'
op|'('
op|')'
nl|'\n'
name|'if'
name|'v'
op|'['
string|"'flavorid'"
op|']'
op|'=='
name|'flavor_id'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'image_id'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'imageId'"
op|']'
newline|'\n'
nl|'\n'
name|'img_service'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'image_service'
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'img_service'
op|'.'
name|'show'
op|'('
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'image'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|','
string|'"Image not found"'
newline|'\n'
nl|'\n'
dedent|''
name|'inst'
op|'['
string|"'server_name'"
op|']'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'image_id'"
op|']'
op|'='
name|'image_id'
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'user_id'
newline|'\n'
name|'inst'
op|'['
string|"'launch_time'"
op|']'
op|'='
name|'ltime'
newline|'\n'
name|'inst'
op|'['
string|"'mac_address'"
op|']'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'user_id'
newline|'\n'
nl|'\n'
name|'inst'
op|'['
string|"'state_description'"
op|']'
op|'='
string|"'scheduling'"
newline|'\n'
name|'inst'
op|'['
string|"'kernel_id'"
op|']'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'kernelId'"
op|','
name|'FLAGS'
op|'.'
name|'default_kernel'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'ramdisk_id'"
op|']'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'ramdiskId'"
op|','
name|'FLAGS'
op|'.'
name|'default_ramdisk'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'r'"
op|')'
newline|'\n'
nl|'\n'
name|'inst'
op|'['
string|"'display_name'"
op|']'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'display_description'"
op|']'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'name'"
op|']'
newline|'\n'
nl|'\n'
comment|'#TODO(dietz) this may be ill advised'
nl|'\n'
name|'key_pair_ref'
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'key_pair_get_all_by_user'
op|'('
nl|'\n'
name|'None'
op|','
name|'user_id'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'inst'
op|'['
string|"'key_data'"
op|']'
op|'='
name|'key_pair_ref'
op|'['
string|"'public_key'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'key_name'"
op|']'
op|'='
name|'key_pair_ref'
op|'['
string|"'name'"
op|']'
newline|'\n'
nl|'\n'
comment|'#TODO(dietz) stolen from ec2 api, see TODO there'
nl|'\n'
name|'inst'
op|'['
string|"'security_group'"
op|']'
op|'='
string|"'default'"
newline|'\n'
nl|'\n'
comment|'# Flavor related attributes'
nl|'\n'
name|'inst'
op|'['
string|"'instance_type'"
op|']'
op|'='
name|'instance_type'
newline|'\n'
name|'inst'
op|'['
string|"'memory_mb'"
op|']'
op|'='
name|'flavor'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'vcpus'"
op|']'
op|'='
name|'flavor'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'local_gb'"
op|']'
op|'='
name|'flavor'
op|'['
string|"'local_gb'"
op|']'
newline|'\n'
nl|'\n'
name|'ref'
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_create'
op|'('
name|'None'
op|','
name|'inst'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'id'"
op|']'
op|'='
name|'ref'
op|'.'
name|'internal_id'
newline|'\n'
nl|'\n'
comment|"# TODO(dietz): this isn't explicitly necessary, but the networking"
nl|'\n'
comment|'# calls depend on an object with a project_id property, and therefore'
nl|'\n'
comment|'# should be cleaned up later'
nl|'\n'
name|'api_context'
op|'='
name|'context'
op|'.'
name|'APIRequestContext'
op|'('
name|'user_id'
op|')'
newline|'\n'
nl|'\n'
name|'inst'
op|'['
string|"'mac_address'"
op|']'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'#TODO(dietz) is this necessary? '
nl|'\n'
name|'inst'
op|'['
string|"'launch_index'"
op|']'
op|'='
number|'0'
newline|'\n'
nl|'\n'
name|'inst'
op|'['
string|"'hostname'"
op|']'
op|'='
name|'str'
op|'('
name|'ref'
op|'.'
name|'internal_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_update'
op|'('
name|'None'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|','
name|'inst'
op|')'
newline|'\n'
nl|'\n'
name|'network_manager'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'network_manager'
op|')'
newline|'\n'
name|'address'
op|'='
name|'network_manager'
op|'.'
name|'allocate_fixed_ip'
op|'('
name|'api_context'
op|','
nl|'\n'
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(vish): This probably should be done in the scheduler'
nl|'\n'
comment|'#             network is setup when host is assigned'
nl|'\n'
name|'network_topic'
op|'='
name|'self'
op|'.'
name|'_get_network_topic'
op|'('
name|'user_id'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'network_topic'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"setup_fixed_ip"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"context"'
op|':'
name|'None'
op|','
nl|'\n'
string|'"address"'
op|':'
name|'address'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'inst'
newline|'\n'
nl|'\n'
DECL|member|_get_network_topic
dedent|''
name|'def'
name|'_get_network_topic'
op|'('
name|'self'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieves the network host for a project"""'
newline|'\n'
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'project_get_network'
op|'('
name|'None'
op|','
nl|'\n'
name|'user_id'
op|')'
newline|'\n'
name|'host'
op|'='
name|'network_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'rpc'
op|'.'
name|'call'
op|'('
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"set_network_host"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"context"'
op|':'
name|'None'
op|','
nl|'\n'
string|'"project_id"'
op|':'
name|'user_id'
op|'}'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'queue_get_for'
op|'('
name|'None'
op|','
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
name|'host'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
