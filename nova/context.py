begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""RequestContext: context for requests that persist through all of nova."""'
newline|'\n'
nl|'\n'
name|'import'
name|'copy'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'local'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'policy'
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
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_request_id
name|'def'
name|'generate_request_id'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"'req-'"
op|'+'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RequestContext
dedent|''
name|'class'
name|'RequestContext'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Security context and request information.\n\n    Represents the user taking a given action within the system.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'user_id'
op|','
name|'project_id'
op|','
name|'is_admin'
op|'='
name|'None'
op|','
name|'read_deleted'
op|'='
string|'"no"'
op|','
nl|'\n'
name|'roles'
op|'='
name|'None'
op|','
name|'remote_address'
op|'='
name|'None'
op|','
name|'timestamp'
op|'='
name|'None'
op|','
nl|'\n'
name|'request_id'
op|'='
name|'None'
op|','
name|'auth_token'
op|'='
name|'None'
op|','
name|'overwrite'
op|'='
name|'True'
op|','
nl|'\n'
name|'quota_class'
op|'='
name|'None'
op|','
name|'user_name'
op|'='
name|'None'
op|','
name|'project_name'
op|'='
name|'None'
op|','
nl|'\n'
name|'service_catalog'
op|'='
op|'['
op|']'
op|','
name|'instance_lock_checked'
op|'='
name|'False'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        :param read_deleted: \'no\' indicates deleted records are hidden, \'yes\'\n            indicates deleted records are visible, \'only\' indicates that\n            *only* deleted records are visible.\n\n        :param overwrite: Set to False to ensure that the greenthread local\n            copy of the index is not overwritten.\n\n        :param kwargs: Extra arguments that might be present, but we ignore\n            because they possibly came in from older rpc messages.\n        """'
newline|'\n'
name|'if'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Arguments dropped when creating context: %s'"
op|')'
op|'%'
nl|'\n'
name|'str'
op|'('
name|'kwargs'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'user_id'
op|'='
name|'user_id'
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
name|'project_id'
newline|'\n'
name|'self'
op|'.'
name|'roles'
op|'='
name|'roles'
name|'or'
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'is_admin'
op|'='
name|'is_admin'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'is_admin'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'is_admin'
op|'='
name|'policy'
op|'.'
name|'check_is_admin'
op|'('
name|'self'
op|'.'
name|'roles'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'read_deleted'
op|'='
name|'read_deleted'
newline|'\n'
name|'self'
op|'.'
name|'remote_address'
op|'='
name|'remote_address'
newline|'\n'
name|'if'
name|'not'
name|'timestamp'
op|':'
newline|'\n'
indent|'            '
name|'timestamp'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'timestamp'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'timestamp'
op|'='
name|'timeutils'
op|'.'
name|'parse_strtime'
op|'('
name|'timestamp'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'timestamp'
op|'='
name|'timestamp'
newline|'\n'
name|'if'
name|'not'
name|'request_id'
op|':'
newline|'\n'
indent|'            '
name|'request_id'
op|'='
name|'generate_request_id'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'request_id'
op|'='
name|'request_id'
newline|'\n'
name|'self'
op|'.'
name|'auth_token'
op|'='
name|'auth_token'
newline|'\n'
comment|'# Only include required parts of service_catalog'
nl|'\n'
name|'self'
op|'.'
name|'service_catalog'
op|'='
op|'['
name|'s'
name|'for'
name|'s'
name|'in'
name|'service_catalog'
nl|'\n'
name|'if'
name|'s'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
name|'in'
op|'('
string|"'volume'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'instance_lock_checked'
op|'='
name|'instance_lock_checked'
newline|'\n'
nl|'\n'
comment|'# NOTE(markmc): this attribute is currently only used by the'
nl|'\n'
comment|'# rs_limits turnstile pre-processor.'
nl|'\n'
comment|'# See https://lists.launchpad.net/openstack/msg12200.html'
nl|'\n'
name|'self'
op|'.'
name|'quota_class'
op|'='
name|'quota_class'
newline|'\n'
name|'self'
op|'.'
name|'user_name'
op|'='
name|'user_name'
newline|'\n'
name|'self'
op|'.'
name|'project_name'
op|'='
name|'project_name'
newline|'\n'
nl|'\n'
name|'if'
name|'overwrite'
name|'or'
name|'not'
name|'hasattr'
op|'('
name|'local'
op|'.'
name|'store'
op|','
string|"'context'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'update_store'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_read_deleted
dedent|''
dedent|''
name|'def'
name|'_get_read_deleted'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_read_deleted'
newline|'\n'
nl|'\n'
DECL|member|_set_read_deleted
dedent|''
name|'def'
name|'_set_read_deleted'
op|'('
name|'self'
op|','
name|'read_deleted'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'read_deleted'
name|'not'
name|'in'
op|'('
string|"'no'"
op|','
string|"'yes'"
op|','
string|"'only'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"read_deleted can only be one of \'no\', "'
nl|'\n'
string|'"\'yes\' or \'only\', not %r"'
op|')'
op|'%'
name|'read_deleted'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_read_deleted'
op|'='
name|'read_deleted'
newline|'\n'
nl|'\n'
DECL|member|_del_read_deleted
dedent|''
name|'def'
name|'_del_read_deleted'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'del'
name|'self'
op|'.'
name|'_read_deleted'
newline|'\n'
nl|'\n'
DECL|variable|read_deleted
dedent|''
name|'read_deleted'
op|'='
name|'property'
op|'('
name|'_get_read_deleted'
op|','
name|'_set_read_deleted'
op|','
nl|'\n'
name|'_del_read_deleted'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_store
name|'def'
name|'update_store'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'local'
op|'.'
name|'store'
op|'.'
name|'context'
op|'='
name|'self'
newline|'\n'
nl|'\n'
DECL|member|to_dict
dedent|''
name|'def'
name|'to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'user_id'"
op|':'
name|'self'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'is_admin'"
op|':'
name|'self'
op|'.'
name|'is_admin'
op|','
nl|'\n'
string|"'read_deleted'"
op|':'
name|'self'
op|'.'
name|'read_deleted'
op|','
nl|'\n'
string|"'roles'"
op|':'
name|'self'
op|'.'
name|'roles'
op|','
nl|'\n'
string|"'remote_address'"
op|':'
name|'self'
op|'.'
name|'remote_address'
op|','
nl|'\n'
string|"'timestamp'"
op|':'
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'self'
op|'.'
name|'timestamp'
op|')'
op|','
nl|'\n'
string|"'request_id'"
op|':'
name|'self'
op|'.'
name|'request_id'
op|','
nl|'\n'
string|"'auth_token'"
op|':'
name|'self'
op|'.'
name|'auth_token'
op|','
nl|'\n'
string|"'quota_class'"
op|':'
name|'self'
op|'.'
name|'quota_class'
op|','
nl|'\n'
string|"'user_name'"
op|':'
name|'self'
op|'.'
name|'user_name'
op|','
nl|'\n'
string|"'service_catalog'"
op|':'
name|'self'
op|'.'
name|'service_catalog'
op|','
nl|'\n'
string|"'project_name'"
op|':'
name|'self'
op|'.'
name|'project_name'
op|','
nl|'\n'
string|"'instance_lock_checked'"
op|':'
name|'self'
op|'.'
name|'instance_lock_checked'
op|','
nl|'\n'
string|"'tenant'"
op|':'
name|'self'
op|'.'
name|'tenant'
op|','
nl|'\n'
string|"'user'"
op|':'
name|'self'
op|'.'
name|'user'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_dict
name|'def'
name|'from_dict'
op|'('
name|'cls'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'('
op|'**'
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|elevated
dedent|''
name|'def'
name|'elevated'
op|'('
name|'self'
op|','
name|'read_deleted'
op|'='
name|'None'
op|','
name|'overwrite'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a version of this context with admin flag set."""'
newline|'\n'
name|'context'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'self'
op|')'
newline|'\n'
name|'context'
op|'.'
name|'is_admin'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'if'
string|"'admin'"
name|'not'
name|'in'
name|'context'
op|'.'
name|'roles'
op|':'
newline|'\n'
indent|'            '
name|'context'
op|'.'
name|'roles'
op|'.'
name|'append'
op|'('
string|"'admin'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'read_deleted'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'context'
op|'.'
name|'read_deleted'
op|'='
name|'read_deleted'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'context'
newline|'\n'
nl|'\n'
comment|'# NOTE(sirp): the openstack/common version of RequestContext uses'
nl|'\n'
comment|'# tenant/user whereas the Nova version uses project_id/user_id. We need'
nl|'\n'
comment|'# this shim in order to use context-aware code from openstack/common, like'
nl|'\n'
comment|"# logging, until we make the switch to using openstack/common's version of"
nl|'\n'
comment|'# RequestContext.'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|tenant
name|'def'
name|'tenant'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'project_id'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|user
name|'def'
name|'user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'user_id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_admin_context
dedent|''
dedent|''
name|'def'
name|'get_admin_context'
op|'('
name|'read_deleted'
op|'='
string|'"no"'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'RequestContext'
op|'('
name|'user_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'True'
op|','
nl|'\n'
name|'read_deleted'
op|'='
name|'read_deleted'
op|','
nl|'\n'
name|'overwrite'
op|'='
name|'False'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
