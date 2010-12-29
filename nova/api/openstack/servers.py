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
name|'logging'
newline|'\n'
name|'import'
name|'traceback'
newline|'\n'
name|'import'
name|'functools'
newline|'\n'
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
name|'common'
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
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'server'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|checks_lock
name|'def'
name|'checks_lock'
op|'('
name|'function'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    decorator used for preventing action against locked instances\n    unless, of course, you happen to be admin\n\n    """'
newline|'\n'
nl|'\n'
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'function'
op|')'
newline|'\n'
DECL|function|decorated_function
name|'def'
name|'decorated_function'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# grab args to function'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'req'"
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'                '
name|'req'
op|'='
name|'kwargs'
op|'['
string|"'req'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'req'
op|'='
name|'args'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'id'"
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'                '
name|'_id'
op|'='
name|'kwargs'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'req'
op|'='
name|'args'
op|'['
number|'2'
op|']'
newline|'\n'
dedent|''
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"CheckLock: argument error: |%s|, |%s|"'
op|')'
op|','
name|'args'
op|','
nl|'\n'
name|'kwargs'
op|')'
newline|'\n'
comment|'# if admin or unlocked call function, otherwise 404'
nl|'\n'
dedent|''
name|'locked'
op|'='
name|'compute_api'
op|'.'
name|'ComputeAPI'
op|'('
op|')'
op|'.'
name|'get_lock'
op|'('
name|'context'
op|','
name|'_id'
op|')'
newline|'\n'
name|'admin'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'.'
name|'is_admin'
newline|'\n'
name|'if'
op|'('
name|'admin'
name|'or'
name|'not'
name|'locked'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'function'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
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
dedent|''
name|'return'
name|'decorated_function'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_detail_keys
dedent|''
name|'def'
name|'_translate_detail_keys'
op|'('
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Coerces into dictionary format, mapping everything to Rackspace-like\n    attributes for return"""'
newline|'\n'
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
string|"'error'"
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
string|"'internal_id'"
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
DECL|function|_translate_keys
dedent|''
name|'def'
name|'_translate_keys'
op|'('
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Coerces into dictionary format, excluding all model attributes\n    save for id and name """'
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
string|"'internal_id'"
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
name|'_translate_keys'
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
name|'_translate_detail_keys'
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
string|'"""Returns a list of servers for a given user.\n\n        entity_maker - either _translate_detail_keys or _translate_keys\n        """'
newline|'\n'
name|'instance_list'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_instances'
op|'('
nl|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'limited_list'
op|'='
name|'common'
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
name|'dict'
op|'('
name|'servers'
op|'='
name|'res'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'checks_lock'
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
string|'""" Returns server details by server id """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_instance'
op|'('
nl|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'int'
op|'('
name|'id'
op|')'
op|')'
newline|'\n'
name|'return'
name|'_translate_detail_keys'
op|'('
name|'instance'
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
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'checks_lock'
newline|'\n'
DECL|member|delete
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
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
nl|'\n'
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
name|'key_pair'
op|'='
name|'auth_manager'
op|'.'
name|'AuthManager'
op|'.'
name|'get_key_pairs'
op|'('
nl|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
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
nl|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
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
name|'_translate_keys'
op|'('
name|'instances'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'checks_lock'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Updates the server name or password """'
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
name|'ctxt'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'update_instance'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'id'
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
dedent|''
op|'@'
name|'checks_lock'
newline|'\n'
DECL|member|action
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
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
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
nl|'\n'
DECL|member|lock
dedent|''
name|'def'
name|'lock'
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
string|'"""\n        lock the instance with id\n        admin only operation\n\n        """'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'lock'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Compute.api::lock %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
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
nl|'\n'
DECL|member|unlock
dedent|''
name|'def'
name|'unlock'
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
string|'"""\n        unlock the instance with id\n        admin only operation\n\n        """'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'unlock'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Compute.api::unlock %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
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
nl|'\n'
DECL|member|get_lock
dedent|''
name|'def'
name|'get_lock'
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
string|'"""\n        return the boolean state of (instance with id)\'s lock\n\n        """'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_lock'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Compute.api::get_lock %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
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
nl|'\n'
dedent|''
op|'@'
name|'checks_lock'
newline|'\n'
DECL|member|pause
name|'def'
name|'pause'
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
string|'""" Permit Admins to Pause the server. """'
newline|'\n'
name|'ctxt'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'pause'
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
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Compute.api::pause %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
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
nl|'\n'
dedent|''
op|'@'
name|'checks_lock'
newline|'\n'
DECL|member|unpause
name|'def'
name|'unpause'
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
string|'""" Permit Admins to Unpause the server. """'
newline|'\n'
name|'ctxt'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'unpause'
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
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Compute.api::unpause %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
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
nl|'\n'
dedent|''
op|'@'
name|'checks_lock'
newline|'\n'
DECL|member|suspend
name|'def'
name|'suspend'
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
string|'"""permit admins to suspend the server"""'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'suspend'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"compute.api::suspend %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
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
nl|'\n'
dedent|''
op|'@'
name|'checks_lock'
newline|'\n'
DECL|member|resume
name|'def'
name|'resume'
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
string|'"""permit admins to resume the server from suspend"""'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'resume'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"compute.api::resume %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
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
