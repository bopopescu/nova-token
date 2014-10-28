begin_unit
comment|'# Copyright 2011 OpenStack Foundation.'
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
string|'"""\nSimple class that stores security context information in the web request.\n\nProjects should subclass this class if they wish to enhance the request\ncontext or provide additional information in their specific WSGI pipeline.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'itertools'
newline|'\n'
name|'import'
name|'uuid'
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
string|"b'req-'"
op|'+'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|'.'
name|'encode'
op|'('
string|"'ascii'"
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
nl|'\n'
indent|'    '
string|'"""Helper class to represent useful information about a request context.\n\n    Stores information about the security context under which the user\n    accesses the system, as well as additional request information.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|user_idt_format
name|'user_idt_format'
op|'='
string|"'{user} {tenant} {domain} {user_domain} {p_domain}'"
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'auth_token'
op|'='
name|'None'
op|','
name|'user'
op|'='
name|'None'
op|','
name|'tenant'
op|'='
name|'None'
op|','
name|'domain'
op|'='
name|'None'
op|','
nl|'\n'
name|'user_domain'
op|'='
name|'None'
op|','
name|'project_domain'
op|'='
name|'None'
op|','
name|'is_admin'
op|'='
name|'False'
op|','
nl|'\n'
name|'read_only'
op|'='
name|'False'
op|','
name|'show_deleted'
op|'='
name|'False'
op|','
name|'request_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'auth_token'
op|'='
name|'auth_token'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'user'
newline|'\n'
name|'self'
op|'.'
name|'tenant'
op|'='
name|'tenant'
newline|'\n'
name|'self'
op|'.'
name|'domain'
op|'='
name|'domain'
newline|'\n'
name|'self'
op|'.'
name|'user_domain'
op|'='
name|'user_domain'
newline|'\n'
name|'self'
op|'.'
name|'project_domain'
op|'='
name|'project_domain'
newline|'\n'
name|'self'
op|'.'
name|'is_admin'
op|'='
name|'is_admin'
newline|'\n'
name|'self'
op|'.'
name|'read_only'
op|'='
name|'read_only'
newline|'\n'
name|'self'
op|'.'
name|'show_deleted'
op|'='
name|'show_deleted'
newline|'\n'
name|'self'
op|'.'
name|'instance_uuid'
op|'='
name|'instance_uuid'
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
name|'user_idt'
op|'='
op|'('
nl|'\n'
name|'self'
op|'.'
name|'user_idt_format'
op|'.'
name|'format'
op|'('
name|'user'
op|'='
name|'self'
op|'.'
name|'user'
name|'or'
string|"'-'"
op|','
nl|'\n'
name|'tenant'
op|'='
name|'self'
op|'.'
name|'tenant'
name|'or'
string|"'-'"
op|','
nl|'\n'
name|'domain'
op|'='
name|'self'
op|'.'
name|'domain'
name|'or'
string|"'-'"
op|','
nl|'\n'
name|'user_domain'
op|'='
name|'self'
op|'.'
name|'user_domain'
name|'or'
string|"'-'"
op|','
nl|'\n'
name|'p_domain'
op|'='
name|'self'
op|'.'
name|'project_domain'
name|'or'
string|"'-'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'user'"
op|':'
name|'self'
op|'.'
name|'user'
op|','
nl|'\n'
string|"'tenant'"
op|':'
name|'self'
op|'.'
name|'tenant'
op|','
nl|'\n'
string|"'domain'"
op|':'
name|'self'
op|'.'
name|'domain'
op|','
nl|'\n'
string|"'user_domain'"
op|':'
name|'self'
op|'.'
name|'user_domain'
op|','
nl|'\n'
string|"'project_domain'"
op|':'
name|'self'
op|'.'
name|'project_domain'
op|','
nl|'\n'
string|"'is_admin'"
op|':'
name|'self'
op|'.'
name|'is_admin'
op|','
nl|'\n'
string|"'read_only'"
op|':'
name|'self'
op|'.'
name|'read_only'
op|','
nl|'\n'
string|"'show_deleted'"
op|':'
name|'self'
op|'.'
name|'show_deleted'
op|','
nl|'\n'
string|"'auth_token'"
op|':'
name|'self'
op|'.'
name|'auth_token'
op|','
nl|'\n'
string|"'request_id'"
op|':'
name|'self'
op|'.'
name|'request_id'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'self'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
string|"'user_identity'"
op|':'
name|'user_idt'
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
name|'ctx'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'('
nl|'\n'
name|'auth_token'
op|'='
name|'ctx'
op|'.'
name|'get'
op|'('
string|'"auth_token"'
op|')'
op|','
nl|'\n'
name|'user'
op|'='
name|'ctx'
op|'.'
name|'get'
op|'('
string|'"user"'
op|')'
op|','
nl|'\n'
name|'tenant'
op|'='
name|'ctx'
op|'.'
name|'get'
op|'('
string|'"tenant"'
op|')'
op|','
nl|'\n'
name|'domain'
op|'='
name|'ctx'
op|'.'
name|'get'
op|'('
string|'"domain"'
op|')'
op|','
nl|'\n'
name|'user_domain'
op|'='
name|'ctx'
op|'.'
name|'get'
op|'('
string|'"user_domain"'
op|')'
op|','
nl|'\n'
name|'project_domain'
op|'='
name|'ctx'
op|'.'
name|'get'
op|'('
string|'"project_domain"'
op|')'
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'ctx'
op|'.'
name|'get'
op|'('
string|'"is_admin"'
op|','
name|'False'
op|')'
op|','
nl|'\n'
name|'read_only'
op|'='
name|'ctx'
op|'.'
name|'get'
op|'('
string|'"read_only"'
op|','
name|'False'
op|')'
op|','
nl|'\n'
name|'show_deleted'
op|'='
name|'ctx'
op|'.'
name|'get'
op|'('
string|'"show_deleted"'
op|','
name|'False'
op|')'
op|','
nl|'\n'
name|'request_id'
op|'='
name|'ctx'
op|'.'
name|'get'
op|'('
string|'"request_id"'
op|')'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'ctx'
op|'.'
name|'get'
op|'('
string|'"instance_uuid"'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_admin_context
dedent|''
dedent|''
name|'def'
name|'get_admin_context'
op|'('
name|'show_deleted'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'context'
op|'='
name|'RequestContext'
op|'('
name|'None'
op|','
nl|'\n'
name|'tenant'
op|'='
name|'None'
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'True'
op|','
nl|'\n'
name|'show_deleted'
op|'='
name|'show_deleted'
op|')'
newline|'\n'
name|'return'
name|'context'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_context_from_function_and_args
dedent|''
name|'def'
name|'get_context_from_function_and_args'
op|'('
name|'function'
op|','
name|'args'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Find an arg of type RequestContext and return it.\n\n       This is useful in a couple of decorators where we don\'t\n       know much about the function we\'re wrapping.\n    """'
newline|'\n'
nl|'\n'
name|'for'
name|'arg'
name|'in'
name|'itertools'
op|'.'
name|'chain'
op|'('
name|'kwargs'
op|'.'
name|'values'
op|'('
op|')'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'arg'
op|','
name|'RequestContext'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'arg'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_user_context
dedent|''
name|'def'
name|'is_user_context'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Indicates if the request context is a normal user."""'
newline|'\n'
name|'if'
name|'not'
name|'context'
name|'or'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'context'
op|'.'
name|'user_id'
name|'and'
name|'context'
op|'.'
name|'project_id'
newline|'\n'
dedent|''
endmarker|''
end_unit
