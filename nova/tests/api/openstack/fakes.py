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
name|'webob'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
name|'from'
name|'paste'
name|'import'
name|'urlmap'
newline|'\n'
nl|'\n'
name|'from'
name|'glance'
name|'import'
name|'client'
name|'as'
name|'glance_client'
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
name|'as'
name|'exc'
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
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'auth'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'openstack'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'auth'
name|'as'
name|'api_auth'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'auth'
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
name|'versions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'limits'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
name|'import'
name|'User'
op|','
name|'Project'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'glance'
name|'import'
name|'stubs'
name|'as'
name|'glance_stubs'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Context
name|'class'
name|'Context'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRouter
dedent|''
name|'class'
name|'FakeRouter'
op|'('
name|'wsgi'
op|'.'
name|'Router'
op|')'
op|':'
newline|'\n'
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
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'res'
op|'='
name|'webob'
op|'.'
name|'Response'
op|'('
op|')'
newline|'\n'
name|'res'
op|'.'
name|'status'
op|'='
string|"'200'"
newline|'\n'
name|'res'
op|'.'
name|'headers'
op|'['
string|"'X-Test-Success'"
op|']'
op|'='
string|"'True'"
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_auth_init
dedent|''
dedent|''
name|'def'
name|'fake_auth_init'
op|'('
name|'self'
op|','
name|'application'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'self'
op|'.'
name|'db'
op|'='
name|'FakeAuthDatabase'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'Context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'auth'
op|'='
name|'FakeAuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'application'
op|'='
name|'application'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|fake_wsgi
name|'def'
name|'fake_wsgi'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wsgi_app
dedent|''
name|'def'
name|'wsgi_app'
op|'('
name|'inner_app10'
op|'='
name|'None'
op|','
name|'inner_app11'
op|'='
name|'None'
op|','
name|'fake_auth'
op|'='
name|'True'
op|','
nl|'\n'
name|'fake_auth_context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'inner_app10'
op|':'
newline|'\n'
indent|'        '
name|'inner_app10'
op|'='
name|'openstack'
op|'.'
name|'APIRouterV10'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'inner_app11'
op|':'
newline|'\n'
indent|'        '
name|'inner_app11'
op|'='
name|'openstack'
op|'.'
name|'APIRouterV11'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'fake_auth'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'fake_auth_context'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'ctxt'
op|'='
name|'fake_auth_context'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'auth_token'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'api10'
op|'='
name|'openstack'
op|'.'
name|'FaultWrapper'
op|'('
name|'api_auth'
op|'.'
name|'InjectContext'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'limits'
op|'.'
name|'RateLimitingMiddleware'
op|'('
name|'inner_app10'
op|')'
op|')'
op|')'
newline|'\n'
name|'api11'
op|'='
name|'openstack'
op|'.'
name|'FaultWrapper'
op|'('
name|'api_auth'
op|'.'
name|'InjectContext'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'limits'
op|'.'
name|'RateLimitingMiddleware'
op|'('
nl|'\n'
name|'extensions'
op|'.'
name|'ExtensionMiddleware'
op|'('
name|'inner_app11'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'api10'
op|'='
name|'openstack'
op|'.'
name|'FaultWrapper'
op|'('
name|'auth'
op|'.'
name|'AuthMiddleware'
op|'('
nl|'\n'
name|'limits'
op|'.'
name|'RateLimitingMiddleware'
op|'('
name|'inner_app10'
op|')'
op|')'
op|')'
newline|'\n'
name|'api11'
op|'='
name|'openstack'
op|'.'
name|'FaultWrapper'
op|'('
name|'auth'
op|'.'
name|'AuthMiddleware'
op|'('
nl|'\n'
name|'limits'
op|'.'
name|'RateLimitingMiddleware'
op|'('
nl|'\n'
name|'extensions'
op|'.'
name|'ExtensionMiddleware'
op|'('
name|'inner_app11'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
name|'Auth'
op|'='
name|'auth'
newline|'\n'
dedent|''
name|'mapper'
op|'='
name|'urlmap'
op|'.'
name|'URLMap'
op|'('
op|')'
newline|'\n'
name|'mapper'
op|'['
string|"'/v1.0'"
op|']'
op|'='
name|'api10'
newline|'\n'
name|'mapper'
op|'['
string|"'/v1.1'"
op|']'
op|'='
name|'api11'
newline|'\n'
name|'mapper'
op|'['
string|"'/'"
op|']'
op|'='
name|'openstack'
op|'.'
name|'FaultWrapper'
op|'('
name|'versions'
op|'.'
name|'Versions'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'mapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_key_pair_funcs
dedent|''
name|'def'
name|'stub_out_key_pair_funcs'
op|'('
name|'stubs'
op|','
name|'have_key_pair'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
DECL|function|key_pair
indent|'    '
name|'def'
name|'key_pair'
op|'('
name|'context'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'dict'
op|'('
name|'name'
op|'='
string|"'key'"
op|','
name|'public_key'
op|'='
string|"'public_key'"
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|function|one_key_pair
dedent|''
name|'def'
name|'one_key_pair'
op|'('
name|'context'
op|','
name|'user_id'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'key'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'dict'
op|'('
name|'name'
op|'='
string|"'key'"
op|','
name|'public_key'
op|'='
string|"'public_key'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'KeypairNotFound'
op|'('
name|'user_id'
op|'='
name|'user_id'
op|','
name|'name'
op|'='
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|function|no_key_pair
dedent|''
dedent|''
name|'def'
name|'no_key_pair'
op|'('
name|'context'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'have_key_pair'
op|':'
newline|'\n'
indent|'        '
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'key_pair_get_all_by_user'"
op|','
name|'key_pair'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'key_pair_get'"
op|','
name|'one_key_pair'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'key_pair_get_all_by_user'"
op|','
name|'no_key_pair'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_image_service
dedent|''
dedent|''
name|'def'
name|'stub_out_image_service'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_image_service
indent|'    '
name|'def'
name|'fake_get_image_service'
op|'('
name|'context'
op|','
name|'image_href'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'nova'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'FakeImageService'
op|'('
op|')'
op|','
name|'image_href'
op|')'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|','
string|"'get_image_service'"
op|','
name|'fake_get_image_service'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|','
string|"'get_default_image_service'"
op|','
nl|'\n'
name|'lambda'
op|':'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'FakeImageService'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_auth
dedent|''
name|'def'
name|'stub_out_auth'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_auth_init
indent|'    '
name|'def'
name|'fake_auth_init'
op|'('
name|'self'
op|','
name|'app'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'application'
op|'='
name|'app'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'auth'
op|'.'
name|'AuthMiddleware'
op|','
nl|'\n'
string|"'__init__'"
op|','
name|'fake_auth_init'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'auth'
op|'.'
name|'AuthMiddleware'
op|','
nl|'\n'
string|"'__call__'"
op|','
name|'fake_wsgi'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_rate_limiting
dedent|''
name|'def'
name|'stub_out_rate_limiting'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_rate_init
indent|'    '
name|'def'
name|'fake_rate_init'
op|'('
name|'self'
op|','
name|'app'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'limits'
op|'.'
name|'RateLimitingMiddleware'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'application'
op|'='
name|'app'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'limits'
op|'.'
name|'RateLimitingMiddleware'
op|','
nl|'\n'
string|"'__init__'"
op|','
name|'fake_rate_init'
op|')'
newline|'\n'
nl|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'limits'
op|'.'
name|'RateLimitingMiddleware'
op|','
nl|'\n'
string|"'__call__'"
op|','
name|'fake_wsgi'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_networking
dedent|''
name|'def'
name|'stub_out_networking'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|get_my_ip
indent|'    '
name|'def'
name|'get_my_ip'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'127.0.0.1'"
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'flags'
op|','
string|"'_get_my_ip'"
op|','
name|'get_my_ip'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_compute_api_snapshot
dedent|''
name|'def'
name|'stub_out_compute_api_snapshot'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|snapshot
indent|'    '
name|'def'
name|'snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'name'
op|','
name|'extra_properties'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'props'
op|'='
name|'dict'
op|'('
name|'instance_id'
op|'='
name|'instance_id'
op|','
name|'instance_ref'
op|'='
name|'instance_id'
op|')'
newline|'\n'
name|'props'
op|'.'
name|'update'
op|'('
name|'extra_properties'
name|'or'
op|'{'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
string|"'123'"
op|','
name|'status'
op|'='
string|"'ACTIVE'"
op|','
name|'name'
op|'='
name|'name'
op|','
name|'properties'
op|'='
name|'props'
op|')'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'API'
op|','
string|"'snapshot'"
op|','
name|'snapshot'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_compute_api_backup
dedent|''
name|'def'
name|'stub_out_compute_api_backup'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|backup
indent|'    '
name|'def'
name|'backup'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'name'
op|','
name|'backup_type'
op|','
name|'rotation'
op|','
nl|'\n'
name|'extra_properties'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'props'
op|'='
name|'dict'
op|'('
name|'instance_id'
op|'='
name|'instance_id'
op|','
name|'instance_ref'
op|'='
name|'instance_id'
op|','
nl|'\n'
name|'backup_type'
op|'='
name|'backup_type'
op|','
name|'rotation'
op|'='
name|'rotation'
op|')'
newline|'\n'
name|'props'
op|'.'
name|'update'
op|'('
name|'extra_properties'
name|'or'
op|'{'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
string|"'123'"
op|','
name|'status'
op|'='
string|"'ACTIVE'"
op|','
name|'name'
op|'='
name|'name'
op|','
name|'properties'
op|'='
name|'props'
op|')'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'API'
op|','
string|"'backup'"
op|','
name|'backup'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_nw_api_get_instance_nw_info
dedent|''
name|'def'
name|'stub_out_nw_api_get_instance_nw_info'
op|'('
name|'stubs'
op|','
name|'func'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
DECL|function|get_instance_nw_info
indent|'    '
name|'def'
name|'get_instance_nw_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|'('
name|'None'
op|','
op|'{'
string|"'label'"
op|':'
string|"'public'"
op|','
nl|'\n'
string|"'ips'"
op|':'
op|'['
op|'{'
string|"'ip'"
op|':'
string|"'192.168.0.3'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'ip6s'"
op|':'
op|'['
op|']'
op|'}'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'func'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'func'
op|'='
name|'get_instance_nw_info'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'network'
op|'.'
name|'API'
op|','
string|"'get_instance_nw_info'"
op|','
name|'func'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_nw_api_get_floating_ips_by_fixed_address
dedent|''
name|'def'
name|'stub_out_nw_api_get_floating_ips_by_fixed_address'
op|'('
name|'stubs'
op|','
name|'func'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
DECL|function|get_floating_ips_by_fixed_address
indent|'    '
name|'def'
name|'get_floating_ips_by_fixed_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'fixed_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
string|"'1.2.3.4'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'func'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'func'
op|'='
name|'get_floating_ips_by_fixed_address'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'network'
op|'.'
name|'API'
op|','
string|"'get_floating_ips_by_fixed_address'"
op|','
name|'func'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_nw_api
dedent|''
name|'def'
name|'stub_out_nw_api'
op|'('
name|'stubs'
op|','
name|'cls'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
DECL|class|Fake
indent|'    '
name|'class'
name|'Fake'
op|':'
newline|'\n'
DECL|member|get_instance_nw_info
indent|'        '
name|'def'
name|'get_instance_nw_info'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ips_by_fixed_address
dedent|''
name|'def'
name|'get_floating_ips_by_fixed_address'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'cls'
name|'is'
name|'None'
op|':'
newline|'\n'
DECL|variable|cls
indent|'        '
name|'cls'
op|'='
name|'Fake'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'network'
op|','
string|"'API'"
op|','
name|'cls'
op|')'
newline|'\n'
name|'stub_out_nw_api_get_floating_ips_by_fixed_address'
op|'('
name|'stubs'
op|')'
newline|'\n'
name|'stub_out_nw_api_get_instance_nw_info'
op|'('
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_make_image_fixtures
dedent|''
name|'def'
name|'_make_image_fixtures'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'NOW_GLANCE_FORMAT'
op|'='
string|'"2010-10-11T10:30:22"'
newline|'\n'
nl|'\n'
name|'image_id'
op|'='
number|'123'
newline|'\n'
name|'base_attrs'
op|'='
op|'{'
string|"'deleted'"
op|':'
name|'False'
op|'}'
newline|'\n'
nl|'\n'
name|'fixtures'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|add_fixture
name|'def'
name|'add_fixture'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'.'
name|'update'
op|'('
name|'base_attrs'
op|')'
newline|'\n'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|'# Public image'
nl|'\n'
dedent|''
name|'add_fixture'
op|'('
name|'id'
op|'='
name|'image_id'
op|','
name|'name'
op|'='
string|"'public image'"
op|','
name|'is_public'
op|'='
name|'True'
op|','
nl|'\n'
name|'status'
op|'='
string|"'active'"
op|','
name|'properties'
op|'='
op|'{'
string|"'key1'"
op|':'
string|"'value1'"
op|'}'
op|','
nl|'\n'
name|'min_ram'
op|'='
string|'"128"'
op|','
name|'min_disk'
op|'='
string|'"10"'
op|')'
newline|'\n'
name|'image_id'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
comment|'# Snapshot for User 1'
nl|'\n'
name|'server_ref'
op|'='
string|"'http://localhost/v1.1/servers/42'"
newline|'\n'
name|'snapshot_properties'
op|'='
op|'{'
string|"'instance_ref'"
op|':'
name|'server_ref'
op|','
string|"'user_id'"
op|':'
string|"'fake'"
op|'}'
newline|'\n'
name|'for'
name|'status'
name|'in'
op|'('
string|"'queued'"
op|','
string|"'saving'"
op|','
string|"'active'"
op|','
string|"'killed'"
op|','
nl|'\n'
string|"'deleted'"
op|','
string|"'pending_delete'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'add_fixture'
op|'('
name|'id'
op|'='
name|'image_id'
op|','
name|'name'
op|'='
string|"'%s snapshot'"
op|'%'
name|'status'
op|','
nl|'\n'
name|'is_public'
op|'='
name|'False'
op|','
name|'status'
op|'='
name|'status'
op|','
nl|'\n'
name|'properties'
op|'='
name|'snapshot_properties'
op|')'
newline|'\n'
name|'image_id'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
comment|'# Image without a name'
nl|'\n'
dedent|''
name|'add_fixture'
op|'('
name|'id'
op|'='
name|'image_id'
op|','
name|'is_public'
op|'='
name|'True'
op|','
name|'status'
op|'='
string|"'active'"
op|','
name|'properties'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'fixtures'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_glance_add_image
dedent|''
name|'def'
name|'stub_out_glance_add_image'
op|'('
name|'stubs'
op|','
name|'sent_to_glance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    We return the metadata sent to glance by modifying the sent_to_glance dict\n    in place.\n    """'
newline|'\n'
name|'orig_add_image'
op|'='
name|'glance_client'
op|'.'
name|'Client'
op|'.'
name|'add_image'
newline|'\n'
nl|'\n'
DECL|function|fake_add_image
name|'def'
name|'fake_add_image'
op|'('
name|'context'
op|','
name|'metadata'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sent_to_glance'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'metadata'
newline|'\n'
name|'sent_to_glance'
op|'['
string|"'data'"
op|']'
op|'='
name|'data'
newline|'\n'
name|'return'
name|'orig_add_image'
op|'('
name|'metadata'
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'glance_client'
op|'.'
name|'Client'
op|','
string|"'add_image'"
op|','
name|'fake_add_image'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_glance
dedent|''
name|'def'
name|'stub_out_glance'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_image_service
indent|'    '
name|'def'
name|'fake_get_image_service'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'client'
op|'='
name|'glance_stubs'
op|'.'
name|'StubGlanceClient'
op|'('
name|'_make_image_fixtures'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
op|'.'
name|'GlanceImageService'
op|'('
name|'client'
op|')'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|','
string|"'get_default_image_service'"
op|','
name|'fake_get_image_service'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeToken
dedent|''
name|'class'
name|'FakeToken'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
comment|"# FIXME(sirp): let's not use id here"
nl|'\n'
DECL|variable|id
indent|'    '
name|'id'
op|'='
number|'0'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'getattr'
op|'('
name|'self'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FakeToken'
op|'.'
name|'id'
op|'+='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'id'
op|'='
name|'FakeToken'
op|'.'
name|'id'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'kwargs'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequestContext
dedent|''
dedent|''
dedent|''
name|'class'
name|'FakeRequestContext'
op|'('
name|'object'
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
name|'user'
op|','
name|'project'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'user_id'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeAuthDatabase
dedent|''
dedent|''
name|'class'
name|'FakeAuthDatabase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|data
indent|'    '
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|auth_token_get
name|'def'
name|'auth_token_get'
op|'('
name|'context'
op|','
name|'token_hash'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'.'
name|'get'
op|'('
name|'token_hash'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|auth_token_create
name|'def'
name|'auth_token_create'
op|'('
name|'context'
op|','
name|'token'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_token'
op|'='
name|'FakeToken'
op|'('
name|'created_at'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
op|'**'
name|'token'
op|')'
newline|'\n'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'['
name|'fake_token'
op|'.'
name|'token_hash'
op|']'
op|'='
name|'fake_token'
newline|'\n'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'['
string|"'id_%i'"
op|'%'
name|'fake_token'
op|'.'
name|'id'
op|']'
op|'='
name|'fake_token'
newline|'\n'
name|'return'
name|'fake_token'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|auth_token_destroy
name|'def'
name|'auth_token_destroy'
op|'('
name|'context'
op|','
name|'token_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'token'
op|'='
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'.'
name|'get'
op|'('
string|"'id_%i'"
op|'%'
name|'token_id'
op|')'
newline|'\n'
name|'if'
name|'token'
name|'and'
name|'token'
op|'.'
name|'token_hash'
name|'in'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'['
name|'token'
op|'.'
name|'token_hash'
op|']'
newline|'\n'
name|'del'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'['
string|"'id_%i'"
op|'%'
name|'token_id'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeAuthManager
dedent|''
dedent|''
dedent|''
name|'class'
name|'FakeAuthManager'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
comment|'#NOTE(justinsb): Accessing static variables through instances is FUBAR'
nl|'\n'
comment|'#NOTE(justinsb): This should also be private!'
nl|'\n'
DECL|variable|auth_data
indent|'    '
name|'auth_data'
op|'='
op|'['
op|']'
newline|'\n'
DECL|variable|projects
name|'projects'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|clear_fakes
name|'def'
name|'clear_fakes'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cls'
op|'.'
name|'auth_data'
op|'='
op|'['
op|']'
newline|'\n'
name|'cls'
op|'.'
name|'projects'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|reset_fake_data
name|'def'
name|'reset_fake_data'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'u1'
op|'='
name|'User'
op|'('
string|"'id1'"
op|','
string|"'guy1'"
op|','
string|"'acc1'"
op|','
string|"'secret1'"
op|','
name|'False'
op|')'
newline|'\n'
name|'cls'
op|'.'
name|'auth_data'
op|'='
op|'['
name|'u1'
op|']'
newline|'\n'
name|'cls'
op|'.'
name|'projects'
op|'='
name|'dict'
op|'('
name|'testacct'
op|'='
name|'Project'
op|'('
string|"'testacct'"
op|','
nl|'\n'
string|"'testacct'"
op|','
nl|'\n'
string|"'id1'"
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
op|'['
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_user
dedent|''
name|'def'
name|'add_user'
op|'('
name|'self'
op|','
name|'user'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FakeAuthManager'
op|'.'
name|'auth_data'
op|'.'
name|'append'
op|'('
name|'user'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_users
dedent|''
name|'def'
name|'get_users'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FakeAuthManager'
op|'.'
name|'auth_data'
newline|'\n'
nl|'\n'
DECL|member|get_user
dedent|''
name|'def'
name|'get_user'
op|'('
name|'self'
op|','
name|'uid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'user'
name|'in'
name|'FakeAuthManager'
op|'.'
name|'auth_data'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'user'
op|'.'
name|'id'
op|'=='
name|'uid'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'user'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|get_user_from_access_key
dedent|''
name|'def'
name|'get_user_from_access_key'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'user'
name|'in'
name|'FakeAuthManager'
op|'.'
name|'auth_data'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'user'
op|'.'
name|'access'
op|'=='
name|'key'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'user'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|delete_user
dedent|''
name|'def'
name|'delete_user'
op|'('
name|'self'
op|','
name|'uid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'user'
name|'in'
name|'FakeAuthManager'
op|'.'
name|'auth_data'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'user'
op|'.'
name|'id'
op|'=='
name|'uid'
op|':'
newline|'\n'
indent|'                '
name|'FakeAuthManager'
op|'.'
name|'auth_data'
op|'.'
name|'remove'
op|'('
name|'user'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|create_user
dedent|''
name|'def'
name|'create_user'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'access'
op|'='
name|'None'
op|','
name|'secret'
op|'='
name|'None'
op|','
name|'admin'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'u'
op|'='
name|'User'
op|'('
name|'name'
op|','
name|'name'
op|','
name|'access'
op|','
name|'secret'
op|','
name|'admin'
op|')'
newline|'\n'
name|'FakeAuthManager'
op|'.'
name|'auth_data'
op|'.'
name|'append'
op|'('
name|'u'
op|')'
newline|'\n'
name|'return'
name|'u'
newline|'\n'
nl|'\n'
DECL|member|modify_user
dedent|''
name|'def'
name|'modify_user'
op|'('
name|'self'
op|','
name|'user_id'
op|','
name|'access'
op|'='
name|'None'
op|','
name|'secret'
op|'='
name|'None'
op|','
name|'admin'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'user'
op|'='
name|'self'
op|'.'
name|'get_user'
op|'('
name|'user_id'
op|')'
newline|'\n'
name|'if'
name|'user'
op|':'
newline|'\n'
indent|'            '
name|'user'
op|'.'
name|'access'
op|'='
name|'access'
newline|'\n'
name|'user'
op|'.'
name|'secret'
op|'='
name|'secret'
newline|'\n'
name|'if'
name|'admin'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'user'
op|'.'
name|'admin'
op|'='
name|'admin'
newline|'\n'
nl|'\n'
DECL|member|is_admin
dedent|''
dedent|''
dedent|''
name|'def'
name|'is_admin'
op|'('
name|'self'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'user'
op|'='
name|'self'
op|'.'
name|'get_user'
op|'('
name|'user_id'
op|')'
newline|'\n'
name|'return'
name|'user'
op|'.'
name|'admin'
newline|'\n'
nl|'\n'
DECL|member|is_project_member
dedent|''
name|'def'
name|'is_project_member'
op|'('
name|'self'
op|','
name|'user_id'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'project'
op|','
name|'Project'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'project'
op|'='
name|'self'
op|'.'
name|'get_project'
op|'('
name|'project'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exc'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnauthorized'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
op|'('
op|'('
name|'user_id'
name|'in'
name|'project'
op|'.'
name|'member_ids'
op|')'
name|'or'
nl|'\n'
op|'('
name|'user_id'
op|'=='
name|'project'
op|'.'
name|'project_manager_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_project
dedent|''
name|'def'
name|'create_project'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'manager_user'
op|','
name|'description'
op|'='
name|'None'
op|','
nl|'\n'
name|'member_users'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'member_ids'
op|'='
op|'['
name|'User'
op|'.'
name|'safe_id'
op|'('
name|'m'
op|')'
name|'for'
name|'m'
name|'in'
name|'member_users'
op|']'
name|'if'
name|'member_users'
name|'else'
op|'['
op|']'
newline|'\n'
name|'p'
op|'='
name|'Project'
op|'('
name|'name'
op|','
name|'name'
op|','
name|'User'
op|'.'
name|'safe_id'
op|'('
name|'manager_user'
op|')'
op|','
nl|'\n'
name|'description'
op|','
name|'member_ids'
op|')'
newline|'\n'
name|'FakeAuthManager'
op|'.'
name|'projects'
op|'['
name|'name'
op|']'
op|'='
name|'p'
newline|'\n'
name|'return'
name|'p'
newline|'\n'
nl|'\n'
DECL|member|delete_project
dedent|''
name|'def'
name|'delete_project'
op|'('
name|'self'
op|','
name|'pid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'pid'
name|'in'
name|'FakeAuthManager'
op|'.'
name|'projects'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'FakeAuthManager'
op|'.'
name|'projects'
op|'['
name|'pid'
op|']'
newline|'\n'
nl|'\n'
DECL|member|modify_project
dedent|''
dedent|''
name|'def'
name|'modify_project'
op|'('
name|'self'
op|','
name|'project'
op|','
name|'manager_user'
op|'='
name|'None'
op|','
name|'description'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'p'
op|'='
name|'FakeAuthManager'
op|'.'
name|'projects'
op|'.'
name|'get'
op|'('
name|'project'
op|')'
newline|'\n'
name|'p'
op|'.'
name|'project_manager_id'
op|'='
name|'User'
op|'.'
name|'safe_id'
op|'('
name|'manager_user'
op|')'
newline|'\n'
name|'p'
op|'.'
name|'description'
op|'='
name|'description'
newline|'\n'
nl|'\n'
DECL|member|get_project
dedent|''
name|'def'
name|'get_project'
op|'('
name|'self'
op|','
name|'pid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'p'
op|'='
name|'FakeAuthManager'
op|'.'
name|'projects'
op|'.'
name|'get'
op|'('
name|'pid'
op|')'
newline|'\n'
name|'if'
name|'p'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'p'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
DECL|member|get_projects
dedent|''
dedent|''
name|'def'
name|'get_projects'
op|'('
name|'self'
op|','
name|'user_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'user_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'FakeAuthManager'
op|'.'
name|'projects'
op|'.'
name|'values'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'p'
name|'for'
name|'p'
name|'in'
name|'FakeAuthManager'
op|'.'
name|'projects'
op|'.'
name|'values'
op|'('
op|')'
nl|'\n'
name|'if'
op|'('
name|'user_id'
name|'in'
name|'p'
op|'.'
name|'member_ids'
op|')'
name|'or'
nl|'\n'
op|'('
name|'user_id'
op|'=='
name|'p'
op|'.'
name|'project_manager_id'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRateLimiter
dedent|''
dedent|''
dedent|''
name|'class'
name|'FakeRateLimiter'
op|'('
name|'object'
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
name|'application'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'application'
op|'='
name|'application'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
