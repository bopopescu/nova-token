begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
string|'"""\nProvides common functionality for integrated unit tests\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'log'
name|'import'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_crypto'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'tests'
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
name|'integrated'
op|'.'
name|'api'
name|'import'
name|'client'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'manager'"
op|','
string|"'nova.cells.opts'"
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_random_alphanumeric
name|'def'
name|'generate_random_alphanumeric'
op|'('
name|'length'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates a random alphanumeric string of specified length."""'
newline|'\n'
name|'return'
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
name|'ascii_uppercase'
op|'+'
name|'string'
op|'.'
name|'digits'
op|')'
nl|'\n'
name|'for'
name|'_x'
name|'in'
name|'range'
op|'('
name|'length'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_random_numeric
dedent|''
name|'def'
name|'generate_random_numeric'
op|'('
name|'length'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates a random numeric string of specified length."""'
newline|'\n'
name|'return'
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
name|'digits'
op|')'
nl|'\n'
name|'for'
name|'_x'
name|'in'
name|'range'
op|'('
name|'length'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_new_element
dedent|''
name|'def'
name|'generate_new_element'
op|'('
name|'items'
op|','
name|'prefix'
op|','
name|'numeric'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates a random string with prefix, that is not in \'items\' list."""'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'numeric'
op|':'
newline|'\n'
indent|'            '
name|'candidate'
op|'='
name|'prefix'
op|'+'
name|'generate_random_numeric'
op|'('
number|'8'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'candidate'
op|'='
name|'prefix'
op|'+'
name|'generate_random_alphanumeric'
op|'('
number|'8'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'candidate'
name|'not'
name|'in'
name|'items'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'candidate'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Random collision on %s"'
op|'%'
name|'candidate'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_IntegratedTestBase
dedent|''
dedent|''
name|'class'
name|'_IntegratedTestBase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'_IntegratedTestBase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'f'
op|'='
name|'self'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
op|'**'
name|'f'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'verbose'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'test'
op|'.'
name|'ReplaceModule'
op|'('
string|"'crypto'"
op|','
name|'fake_crypto'
op|')'
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'scheduler_driver'
op|'='
string|"'nova.scheduler.'"
nl|'\n'
string|"'chance.ChanceScheduler'"
op|')'
newline|'\n'
nl|'\n'
comment|'# set up services'
nl|'\n'
name|'self'
op|'.'
name|'conductor'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'conductor'"
op|','
nl|'\n'
name|'manager'
op|'='
name|'CONF'
op|'.'
name|'conductor'
op|'.'
name|'manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'compute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'scheduler'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'cert'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'network'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'scheduler'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'scheduler'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cells'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'cells'"
op|','
name|'manager'
op|'='
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'manager'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_start_api_service'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'='
name|'client'
op|'.'
name|'TestOpenStackClient'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'self'
op|'.'
name|'auth_url'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'osapi'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'FakeImageService_reset'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'_IntegratedTestBase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_start_api_service
dedent|''
name|'def'
name|'_start_api_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'osapi'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|'"osapi_compute"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'osapi'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'auth_url'
op|'='
string|"'http://%s:%s/v2'"
op|'%'
op|'('
name|'self'
op|'.'
name|'osapi'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'osapi'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'self'
op|'.'
name|'auth_url'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_flags
dedent|''
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""An opportunity to setup flags, before the services are started."""'
newline|'\n'
name|'f'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Ensure tests only listen on localhost'
nl|'\n'
name|'f'
op|'['
string|"'ec2_listen'"
op|']'
op|'='
string|"'127.0.0.1'"
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_listen'"
op|']'
op|'='
string|"'127.0.0.1'"
newline|'\n'
name|'f'
op|'['
string|"'metadata_listen'"
op|']'
op|'='
string|"'127.0.0.1'"
newline|'\n'
nl|'\n'
comment|'# Auto-assign ports to allow concurrent tests'
nl|'\n'
name|'f'
op|'['
string|"'ec2_listen_port'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_listen_port'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'f'
op|'['
string|"'metadata_listen_port'"
op|']'
op|'='
number|'0'
newline|'\n'
nl|'\n'
name|'f'
op|'['
string|"'fake_network'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|get_unused_server_name
dedent|''
name|'def'
name|'get_unused_server_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'servers'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_servers'
op|'('
op|')'
newline|'\n'
name|'server_names'
op|'='
op|'['
name|'server'
op|'['
string|"'name'"
op|']'
name|'for'
name|'server'
name|'in'
name|'servers'
op|']'
newline|'\n'
name|'return'
name|'generate_new_element'
op|'('
name|'server_names'
op|','
string|"'server'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_invalid_image
dedent|''
name|'def'
name|'get_invalid_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
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
DECL|member|_build_minimal_create_server_request
dedent|''
name|'def'
name|'_build_minimal_create_server_request'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_images'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Image: %s"'
op|'%'
name|'image'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'imageRef'"
name|'in'
name|'image'
op|':'
newline|'\n'
indent|'            '
name|'image_href'
op|'='
name|'image'
op|'['
string|"'imageRef'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'image_href'
op|'='
name|'image'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'image_href'
op|'='
string|"'http://fake.server/%s'"
op|'%'
name|'image_href'
newline|'\n'
nl|'\n'
comment|'# We now have a valid imageId'
nl|'\n'
dedent|''
name|'server'
op|'['
string|"'imageRef'"
op|']'
op|'='
name|'image_href'
newline|'\n'
nl|'\n'
comment|'# Set a valid flavorId'
nl|'\n'
name|'flavor'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_flavors'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Using flavor: %s"'
op|'%'
name|'flavor'
op|')'
newline|'\n'
name|'server'
op|'['
string|"'flavorRef'"
op|']'
op|'='
string|"'http://fake.server/%s'"
op|'%'
name|'flavor'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Set a valid server name'
nl|'\n'
name|'server_name'
op|'='
name|'self'
op|'.'
name|'get_unused_server_name'
op|'('
op|')'
newline|'\n'
name|'server'
op|'['
string|"'name'"
op|']'
op|'='
name|'server_name'
newline|'\n'
name|'return'
name|'server'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
