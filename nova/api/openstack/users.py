begin_unit
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
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
name|'wsgi'
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
name|'auth'
name|'import'
name|'manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.api.openstack'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_keys
name|'def'
name|'_translate_keys'
op|'('
name|'user'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
name|'user'
op|'.'
name|'id'
op|','
nl|'\n'
name|'name'
op|'='
name|'user'
op|'.'
name|'name'
op|','
nl|'\n'
name|'access'
op|'='
name|'user'
op|'.'
name|'access'
op|','
nl|'\n'
name|'secret'
op|'='
name|'user'
op|'.'
name|'secret'
op|','
nl|'\n'
name|'admin'
op|'='
name|'user'
op|'.'
name|'admin'
op|')'
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
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_admin
dedent|''
name|'def'
name|'_check_admin'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""We cannot depend on the db layer to check for admin access\n           for the auth manager, so we do it here"""'
newline|'\n'
name|'if'
name|'not'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'AdminRequired'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
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
string|'"""Return all users in brief"""'
newline|'\n'
name|'users'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_users'
op|'('
op|')'
newline|'\n'
name|'users'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'users'
op|','
name|'req'
op|')'
newline|'\n'
name|'users'
op|'='
op|'['
name|'_translate_keys'
op|'('
name|'user'
op|')'
name|'for'
name|'user'
name|'in'
name|'users'
op|']'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'users'
op|'='
name|'users'
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
string|'"""Return all users in detail"""'
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
string|'"""Return data about the given user id"""'
newline|'\n'
nl|'\n'
comment|'#NOTE(justinsb): The drivers are a little inconsistent in how they'
nl|'\n'
comment|'#  deal with "NotFound" - some throw, some return None.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_user'
op|'('
name|'id'
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
name|'user'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'user'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'user'
op|'='
name|'_translate_keys'
op|'('
name|'user'
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
name|'self'
op|'.'
name|'_check_admin'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'id'
op|')'
newline|'\n'
name|'return'
op|'{'
op|'}'
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
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_check_admin'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'is_admin'
op|'='
name|'body'
op|'['
string|"'user'"
op|']'
op|'.'
name|'get'
op|'('
string|"'admin'"
op|')'
name|'in'
op|'('
string|"'T'"
op|','
string|"'True'"
op|','
name|'True'
op|')'
newline|'\n'
name|'name'
op|'='
name|'body'
op|'['
string|"'user'"
op|']'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'access'
op|'='
name|'body'
op|'['
string|"'user'"
op|']'
op|'.'
name|'get'
op|'('
string|"'access'"
op|')'
newline|'\n'
name|'secret'
op|'='
name|'body'
op|'['
string|"'user'"
op|']'
op|'.'
name|'get'
op|'('
string|"'secret'"
op|')'
newline|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
name|'name'
op|','
name|'access'
op|','
name|'secret'
op|','
name|'is_admin'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'user'
op|'='
name|'_translate_keys'
op|'('
name|'user'
op|')'
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
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_check_admin'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'is_admin'
op|'='
name|'body'
op|'['
string|"'user'"
op|']'
op|'.'
name|'get'
op|'('
string|"'admin'"
op|')'
newline|'\n'
name|'if'
name|'is_admin'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'is_admin'
op|'='
name|'is_admin'
name|'in'
op|'('
string|"'T'"
op|','
string|"'True'"
op|','
name|'True'
op|')'
newline|'\n'
dedent|''
name|'access'
op|'='
name|'body'
op|'['
string|"'user'"
op|']'
op|'.'
name|'get'
op|'('
string|"'access'"
op|')'
newline|'\n'
name|'secret'
op|'='
name|'body'
op|'['
string|"'user'"
op|']'
op|'.'
name|'get'
op|'('
string|"'secret'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'modify_user'
op|'('
name|'id'
op|','
name|'access'
op|','
name|'secret'
op|','
name|'is_admin'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'user'
op|'='
name|'_translate_keys'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_user'
op|'('
name|'id'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_user
dedent|''
dedent|''
name|'def'
name|'make_user'
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
string|"'name'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'access'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'secret'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'admin'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UserTemplate
dedent|''
name|'class'
name|'UserTemplate'
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
string|"'user'"
op|','
name|'selector'
op|'='
string|"'user'"
op|')'
newline|'\n'
name|'make_user'
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
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UsersTemplate
dedent|''
dedent|''
name|'class'
name|'UsersTemplate'
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
string|"'users'"
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
string|"'user'"
op|','
name|'selector'
op|'='
string|"'users'"
op|')'
newline|'\n'
name|'make_user'
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
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UserXMLSerializer
dedent|''
dedent|''
name|'class'
name|'UserXMLSerializer'
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
name|'UsersTemplate'
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
name|'UserTemplate'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_resource
dedent|''
dedent|''
name|'def'
name|'create_resource'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'body_serializers'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
name|'UserXMLSerializer'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'ResponseSerializer'
op|'('
name|'body_serializers'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'Controller'
op|'('
op|')'
op|','
name|'serializer'
op|'='
name|'serializer'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
