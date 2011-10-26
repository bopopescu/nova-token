begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010-2011 OpenStack LLC.'
nl|'\n'
comment|'# Copyright 2011 Piston Cloud Computing, Inc.'
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
name|'json'
newline|'\n'
nl|'\n'
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'consoles'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'console'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
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
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
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
name|'tests'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|variable|FAKE_UUID
name|'FAKE_UUID'
op|'='
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_server_by_id
name|'def'
name|'return_server_by_id'
op|'('
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'print'
string|'"GOT HERE"'
newline|'\n'
name|'return'
name|'stub_instance'
op|'('
name|'id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_instance
dedent|''
name|'def'
name|'stub_instance'
op|'('
name|'id'
op|','
name|'user_id'
op|'='
string|"'fake'"
op|','
name|'project_id'
op|'='
string|"'fake'"
op|','
name|'host'
op|'='
name|'None'
op|','
nl|'\n'
name|'vm_state'
op|'='
name|'None'
op|','
name|'task_state'
op|'='
name|'None'
op|','
nl|'\n'
name|'reservation_id'
op|'='
string|'""'
op|','
name|'uuid'
op|'='
name|'FAKE_UUID'
op|','
name|'image_ref'
op|'='
string|'"10"'
op|','
nl|'\n'
name|'flavor_id'
op|'='
string|'"1"'
op|','
name|'name'
op|'='
name|'None'
op|','
name|'key_name'
op|'='
string|"''"
op|','
nl|'\n'
name|'access_ipv4'
op|'='
name|'None'
op|','
name|'access_ipv6'
op|'='
name|'None'
op|','
name|'progress'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
name|'if'
name|'host'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'str'
op|'('
name|'host'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'key_name'
op|':'
newline|'\n'
indent|'        '
name|'key_data'
op|'='
string|"'FAKE'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'key_data'
op|'='
string|"''"
newline|'\n'
nl|'\n'
comment|"# ReservationID isn't sent back, hack it in there."
nl|'\n'
dedent|''
name|'server_name'
op|'='
name|'name'
name|'or'
string|'"server%s"'
op|'%'
name|'id'
newline|'\n'
name|'if'
name|'reservation_id'
op|'!='
string|'""'
op|':'
newline|'\n'
indent|'        '
name|'server_name'
op|'='
string|'"reservation_%s"'
op|'%'
op|'('
name|'reservation_id'
op|','
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'instance'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'int'
op|'('
name|'id'
op|')'
op|','
nl|'\n'
string|'"uuid"'
op|':'
name|'FAKE_UUID'
op|','
nl|'\n'
string|'"created_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'10'
op|','
number|'10'
op|','
number|'12'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"updated_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'11'
op|','
number|'11'
op|','
number|'11'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"admin_pass"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"user_id"'
op|':'
name|'user_id'
op|','
nl|'\n'
string|'"project_id"'
op|':'
name|'project_id'
op|','
nl|'\n'
string|'"image_ref"'
op|':'
name|'image_ref'
op|','
nl|'\n'
string|'"kernel_id"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"ramdisk_id"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"launch_index"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"key_name"'
op|':'
name|'key_name'
op|','
nl|'\n'
string|'"key_data"'
op|':'
name|'key_data'
op|','
nl|'\n'
string|'"vm_state"'
op|':'
name|'vm_state'
name|'or'
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
nl|'\n'
string|'"task_state"'
op|':'
name|'task_state'
op|','
nl|'\n'
string|'"memory_mb"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"local_gb"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"hostname"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"host"'
op|':'
name|'host'
op|','
nl|'\n'
string|'"instance_type"'
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|'"user_data"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"reservation_id"'
op|':'
name|'reservation_id'
op|','
nl|'\n'
string|'"mac_address"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"scheduled_at"'
op|':'
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
string|'"launched_at"'
op|':'
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
string|'"terminated_at"'
op|':'
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
string|'"availability_zone"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"display_name"'
op|':'
name|'server_name'
op|','
nl|'\n'
string|'"display_description"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"locked"'
op|':'
name|'False'
op|','
nl|'\n'
string|'"metadata"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"access_ip_v4"'
op|':'
name|'access_ipv4'
op|','
nl|'\n'
string|'"access_ip_v6"'
op|':'
name|'access_ipv6'
op|','
nl|'\n'
string|'"uuid"'
op|':'
name|'uuid'
op|','
nl|'\n'
string|'"progress"'
op|':'
name|'progress'
op|'}'
newline|'\n'
nl|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsolesTest
dedent|''
name|'class'
name|'ConsolesTest'
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
name|'ConsolesTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server_by_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'webreq'
op|'='
name|'common'
op|'.'
name|'webob_factory'
op|'('
string|"'/v1.1/fake/servers'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_console
dedent|''
name|'def'
name|'test_create_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_create_console
indent|'        '
name|'def'
name|'fake_create_console'
op|'('
name|'cons_self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'instance_id'
op|','
number|'10'
op|')'
newline|'\n'
name|'return'
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'console'
op|'.'
name|'API'
op|','
string|"'create_console'"
op|','
name|'fake_create_console'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/fake/servers/10/consoles'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_console
dedent|''
name|'def'
name|'test_show_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_console
indent|'        '
name|'def'
name|'fake_get_console'
op|'('
name|'cons_self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'console_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance_id'
op|','
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'console_id'
op|','
number|'20'
op|')'
newline|'\n'
name|'pool'
op|'='
name|'dict'
op|'('
name|'console_type'
op|'='
string|"'fake_type'"
op|','
nl|'\n'
name|'public_hostname'
op|'='
string|"'fake_hostname'"
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
name|'console_id'
op|','
name|'password'
op|'='
string|"'fake_password'"
op|','
nl|'\n'
name|'port'
op|'='
string|"'fake_port'"
op|','
name|'pool'
op|'='
name|'pool'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'expected'
op|'='
op|'{'
string|"'console'"
op|':'
op|'{'
string|"'id'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'port'"
op|':'
string|"'fake_port'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fake_hostname'"
op|','
nl|'\n'
string|"'password'"
op|':'
string|"'fake_password'"
op|','
nl|'\n'
string|"'console_type'"
op|':'
string|"'fake_type'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'console'
op|'.'
name|'API'
op|','
string|"'get_console'"
op|','
name|'fake_get_console'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/fake/servers/10/consoles/20'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'res_dict'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_console_xml
dedent|''
name|'def'
name|'test_show_console_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_console
indent|'        '
name|'def'
name|'fake_get_console'
op|'('
name|'cons_self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'console_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance_id'
op|','
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'console_id'
op|','
number|'20'
op|')'
newline|'\n'
name|'pool'
op|'='
name|'dict'
op|'('
name|'console_type'
op|'='
string|"'fake_type'"
op|','
nl|'\n'
name|'public_hostname'
op|'='
string|"'fake_hostname'"
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
name|'console_id'
op|','
name|'password'
op|'='
string|"'fake_password'"
op|','
nl|'\n'
name|'port'
op|'='
string|"'fake_port'"
op|','
name|'pool'
op|'='
name|'pool'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'console'
op|'.'
name|'API'
op|','
string|"'get_console'"
op|','
name|'fake_get_console'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/fake/servers/10/consoles/20.xml'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
name|'res_tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'.'
name|'tag'
op|','
string|"'console'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'.'
name|'xpath'
op|'('
string|"'id'"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'text'
op|','
string|"'20'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'.'
name|'xpath'
op|'('
string|"'port'"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'text'
op|','
string|"'fake_port'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'.'
name|'xpath'
op|'('
string|"'host'"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'text'
op|','
string|"'fake_hostname'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'.'
name|'xpath'
op|'('
string|"'password'"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'text'
op|','
string|"'fake_password'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'.'
name|'xpath'
op|'('
string|"'console_type'"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'text'
op|','
nl|'\n'
string|"'fake_type'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_console_unknown_console
dedent|''
name|'def'
name|'test_show_console_unknown_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_console
indent|'        '
name|'def'
name|'fake_get_console'
op|'('
name|'cons_self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'console_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ConsoleNotFound'
op|'('
name|'console_id'
op|'='
name|'console_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'console'
op|'.'
name|'API'
op|','
string|"'get_console'"
op|','
name|'fake_get_console'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/fake/servers/10/consoles/20'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_console_unknown_instance
dedent|''
name|'def'
name|'test_show_console_unknown_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_console
indent|'        '
name|'def'
name|'fake_get_console'
op|'('
name|'cons_self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'console_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'console'
op|'.'
name|'API'
op|','
string|"'get_console'"
op|','
name|'fake_get_console'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/fake/servers/10/consoles/20'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_consoles
dedent|''
name|'def'
name|'test_list_consoles'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_consoles
indent|'        '
name|'def'
name|'fake_get_consoles'
op|'('
name|'cons_self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance_id'
op|','
number|'10'
op|')'
newline|'\n'
nl|'\n'
name|'pool1'
op|'='
name|'dict'
op|'('
name|'console_type'
op|'='
string|"'fake_type'"
op|','
nl|'\n'
name|'public_hostname'
op|'='
string|"'fake_hostname'"
op|')'
newline|'\n'
name|'cons1'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
number|'10'
op|','
name|'password'
op|'='
string|"'fake_password'"
op|','
nl|'\n'
name|'port'
op|'='
string|"'fake_port'"
op|','
name|'pool'
op|'='
name|'pool1'
op|')'
newline|'\n'
name|'pool2'
op|'='
name|'dict'
op|'('
name|'console_type'
op|'='
string|"'fake_type2'"
op|','
nl|'\n'
name|'public_hostname'
op|'='
string|"'fake_hostname2'"
op|')'
newline|'\n'
name|'cons2'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
number|'11'
op|','
name|'password'
op|'='
string|"'fake_password2'"
op|','
nl|'\n'
name|'port'
op|'='
string|"'fake_port2'"
op|','
name|'pool'
op|'='
name|'pool2'
op|')'
newline|'\n'
name|'return'
op|'['
name|'cons1'
op|','
name|'cons2'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'expected'
op|'='
op|'{'
string|"'consoles'"
op|':'
nl|'\n'
op|'['
op|'{'
string|"'console'"
op|':'
op|'{'
string|"'id'"
op|':'
number|'10'
op|','
string|"'console_type'"
op|':'
string|"'fake_type'"
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'console'"
op|':'
op|'{'
string|"'id'"
op|':'
number|'11'
op|','
string|"'console_type'"
op|':'
string|"'fake_type2'"
op|'}'
op|'}'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'console'
op|'.'
name|'API'
op|','
string|"'get_consoles'"
op|','
name|'fake_get_consoles'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/fake/servers/10/consoles'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'res_dict'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_consoles_xml
dedent|''
name|'def'
name|'test_list_consoles_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_consoles
indent|'        '
name|'def'
name|'fake_get_consoles'
op|'('
name|'cons_self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance_id'
op|','
number|'10'
op|')'
newline|'\n'
nl|'\n'
name|'pool1'
op|'='
name|'dict'
op|'('
name|'console_type'
op|'='
string|"'fake_type'"
op|','
nl|'\n'
name|'public_hostname'
op|'='
string|"'fake_hostname'"
op|')'
newline|'\n'
name|'cons1'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
number|'10'
op|','
name|'password'
op|'='
string|"'fake_password'"
op|','
nl|'\n'
name|'port'
op|'='
string|"'fake_port'"
op|','
name|'pool'
op|'='
name|'pool1'
op|')'
newline|'\n'
name|'pool2'
op|'='
name|'dict'
op|'('
name|'console_type'
op|'='
string|"'fake_type2'"
op|','
nl|'\n'
name|'public_hostname'
op|'='
string|"'fake_hostname2'"
op|')'
newline|'\n'
name|'cons2'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
number|'11'
op|','
name|'password'
op|'='
string|"'fake_password2'"
op|','
nl|'\n'
name|'port'
op|'='
string|"'fake_port2'"
op|','
name|'pool'
op|'='
name|'pool2'
op|')'
newline|'\n'
name|'return'
op|'['
name|'cons1'
op|','
name|'cons2'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'expected'
op|'='
op|'{'
string|"'consoles'"
op|':'
nl|'\n'
op|'['
op|'{'
string|"'console'"
op|':'
op|'{'
string|"'id'"
op|':'
number|'10'
op|','
string|"'console_type'"
op|':'
string|"'fake_type'"
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'console'"
op|':'
op|'{'
string|"'id'"
op|':'
number|'11'
op|','
string|"'console_type'"
op|':'
string|"'fake_type2'"
op|'}'
op|'}'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'console'
op|'.'
name|'API'
op|','
string|"'get_consoles'"
op|','
name|'fake_get_consoles'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/fake/servers/10/consoles.xml'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
name|'res_tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'.'
name|'tag'
op|','
string|"'consoles'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'res_tree'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'['
number|'0'
op|']'
op|'.'
name|'tag'
op|','
string|"'console'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'['
number|'1'
op|']'
op|'.'
name|'tag'
op|','
string|"'console'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'res_tree'
op|'['
number|'0'
op|']'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|'.'
name|'tag'
op|','
string|"'console'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'res_tree'
op|'['
number|'1'
op|']'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'['
number|'1'
op|']'
op|'['
number|'0'
op|']'
op|'.'
name|'tag'
op|','
string|"'console'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|'.'
name|'xpath'
op|'('
string|"'id'"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'text'
op|','
string|"'10'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'['
number|'1'
op|']'
op|'['
number|'0'
op|']'
op|'.'
name|'xpath'
op|'('
string|"'id'"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'text'
op|','
string|"'11'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|'.'
name|'xpath'
op|'('
string|"'console_type'"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'text'
op|','
nl|'\n'
string|"'fake_type'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_tree'
op|'['
number|'1'
op|']'
op|'['
number|'0'
op|']'
op|'.'
name|'xpath'
op|'('
string|"'console_type'"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'text'
op|','
nl|'\n'
string|"'fake_type2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_console
dedent|''
name|'def'
name|'test_delete_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_console
indent|'        '
name|'def'
name|'fake_get_console'
op|'('
name|'cons_self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'console_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance_id'
op|','
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'console_id'
op|','
number|'20'
op|')'
newline|'\n'
name|'pool'
op|'='
name|'dict'
op|'('
name|'console_type'
op|'='
string|"'fake_type'"
op|','
nl|'\n'
name|'public_hostname'
op|'='
string|"'fake_hostname'"
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
name|'console_id'
op|','
name|'password'
op|'='
string|"'fake_password'"
op|','
nl|'\n'
name|'port'
op|'='
string|"'fake_port'"
op|','
name|'pool'
op|'='
name|'pool'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_delete_console
dedent|''
name|'def'
name|'fake_delete_console'
op|'('
name|'cons_self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'console_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance_id'
op|','
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'console_id'
op|','
number|'20'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'console'
op|'.'
name|'API'
op|','
string|"'get_console'"
op|','
name|'fake_get_console'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'console'
op|'.'
name|'API'
op|','
string|"'delete_console'"
op|','
name|'fake_delete_console'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/fake/servers/10/consoles/20'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"DELETE"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_console_unknown_console
dedent|''
name|'def'
name|'test_show_console_unknown_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_delete_console
indent|'        '
name|'def'
name|'fake_delete_console'
op|'('
name|'cons_self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'console_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ConsoleNotFound'
op|'('
name|'console_id'
op|'='
name|'console_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'console'
op|'.'
name|'API'
op|','
string|"'delete_console'"
op|','
name|'fake_delete_console'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/fake/servers/10/consoles/20'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"DELETE"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_console_unknown_instance
dedent|''
name|'def'
name|'test_show_console_unknown_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_delete_console
indent|'        '
name|'def'
name|'fake_delete_console'
op|'('
name|'cons_self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'console_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'console'
op|'.'
name|'API'
op|','
string|"'delete_console'"
op|','
name|'fake_delete_console'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/fake/servers/10/consoles/20'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"DELETE"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
