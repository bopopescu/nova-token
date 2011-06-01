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
name|'copy'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
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
name|'from'
name|'glance'
op|'.'
name|'common'
name|'import'
name|'exception'
name|'as'
name|'glance_exc'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
name|'image'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'local'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'wsgi'
name|'import'
name|'Router'
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
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
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
dedent|''
name|'mapper'
op|'='
name|'urlmap'
op|'.'
name|'URLMap'
op|'('
op|')'
newline|'\n'
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
name|'inner_app11'
op|')'
op|')'
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
DECL|function|no_key_pair
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
op|','
string|"'key_pair_get_all_by_user'"
op|','
name|'key_pair'
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
name|'image_href'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
name|'int'
op|'('
name|'str'
op|'('
name|'image_href'
op|')'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
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
name|'image_id'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'123'
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
op|','
name|'initial_fixtures'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|class|FakeGlanceClient
indent|'    '
name|'class'
name|'FakeGlanceClient'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'        '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'initial_fixtures'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fixtures'
op|'='
name|'initial_fixtures'
name|'or'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|fake_get_images
dedent|''
name|'def'
name|'fake_get_images'
op|'('
name|'self'
op|','
name|'filters'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'dict'
op|'('
name|'id'
op|'='
name|'f'
op|'['
string|"'id'"
op|']'
op|','
name|'name'
op|'='
name|'f'
op|'['
string|"'name'"
op|']'
op|')'
nl|'\n'
name|'for'
name|'f'
name|'in'
name|'self'
op|'.'
name|'fixtures'
op|']'
newline|'\n'
nl|'\n'
DECL|member|fake_get_images_detailed
dedent|''
name|'def'
name|'fake_get_images_detailed'
op|'('
name|'self'
op|','
name|'filters'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'fixtures'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fake_get_image_meta
dedent|''
name|'def'
name|'fake_get_image_meta'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image'
op|'='
name|'self'
op|'.'
name|'_find_image'
op|'('
name|'image_id'
op|')'
newline|'\n'
name|'if'
name|'image'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'image'
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'glance_exc'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
DECL|member|fake_add_image
dedent|''
name|'def'
name|'fake_add_image'
op|'('
name|'self'
op|','
name|'image_meta'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'image_id'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
name|'random'
op|'.'
name|'choice'
op|'('
name|'string'
op|'.'
name|'letters'
op|')'
nl|'\n'
name|'for'
name|'_'
name|'in'
name|'range'
op|'('
number|'20'
op|')'
op|')'
newline|'\n'
name|'image_meta'
op|'['
string|"'id'"
op|']'
op|'='
name|'image_id'
newline|'\n'
name|'self'
op|'.'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'return'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fake_update_image
dedent|''
name|'def'
name|'fake_update_image'
op|'('
name|'self'
op|','
name|'image_id'
op|','
name|'image_meta'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'attr'
name|'in'
op|'('
string|"'created_at'"
op|','
string|"'updated_at'"
op|','
string|"'deleted_at'"
op|','
string|"'deleted'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'attr'
name|'in'
name|'image_meta'
op|':'
newline|'\n'
indent|'                    '
name|'del'
name|'image_meta'
op|'['
name|'attr'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'f'
op|'='
name|'self'
op|'.'
name|'_find_image'
op|'('
name|'image_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'glance_exc'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
dedent|''
name|'f'
op|'.'
name|'update'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'return'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'f'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fake_delete_image
dedent|''
name|'def'
name|'fake_delete_image'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'='
name|'self'
op|'.'
name|'_find_image'
op|'('
name|'image_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'glance_exc'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'fixtures'
op|'.'
name|'remove'
op|'('
name|'f'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_find_image
dedent|''
name|'def'
name|'_find_image'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'f'
name|'in'
name|'self'
op|'.'
name|'fixtures'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'f'
op|'['
string|"'id'"
op|']'
op|'=='
name|'image_id'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'f'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'GlanceClient'
op|'='
name|'glance_client'
op|'.'
name|'Client'
newline|'\n'
name|'fake'
op|'='
name|'FakeGlanceClient'
op|'('
name|'initial_fixtures'
op|')'
newline|'\n'
nl|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'GlanceClient'
op|','
string|"'get_images'"
op|','
name|'fake'
op|'.'
name|'fake_get_images'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'GlanceClient'
op|','
string|"'get_images_detailed'"
op|','
nl|'\n'
name|'fake'
op|'.'
name|'fake_get_images_detailed'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'GlanceClient'
op|','
string|"'get_image_meta'"
op|','
name|'fake'
op|'.'
name|'fake_get_image_meta'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'GlanceClient'
op|','
string|"'add_image'"
op|','
name|'fake'
op|'.'
name|'fake_add_image'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'GlanceClient'
op|','
string|"'update_image'"
op|','
name|'fake'
op|'.'
name|'fake_update_image'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'GlanceClient'
op|','
string|"'delete_image'"
op|','
name|'fake'
op|'.'
name|'fake_delete_image'
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
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'now'
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
name|'user'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
op|'('
name|'user'
op|'.'
name|'id'
name|'in'
name|'project'
op|'.'
name|'member_ids'
op|')'
name|'or'
nl|'\n'
op|'('
name|'user'
op|'.'
name|'id'
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
name|'user'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'user'
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
name|'user'
op|'.'
name|'id'
name|'in'
name|'p'
op|'.'
name|'member_ids'
op|')'
name|'or'
nl|'\n'
op|'('
name|'user'
op|'.'
name|'id'
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
