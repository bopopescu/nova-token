begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'test_servers'
newline|'\n'
nl|'\n'
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
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsolesSampleJsonTests
name|'class'
name|'ConsolesSampleJsonTests'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|'"os-remote-consoles"'
newline|'\n'
nl|'\n'
DECL|member|_get_flags
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'super'
op|'('
name|'ConsolesSampleJsonTests'
op|','
name|'self'
op|')'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'osapi_compute_extension'
op|'['
op|':'
op|']'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.consoles.Consoles'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'ConsolesSampleJsonTests'
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
name|'enabled'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'vnc'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'enabled'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'spice'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'enabled'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'rdp'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'enabled'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'serial_console'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vnc_console
dedent|''
name|'def'
name|'test_get_vnc_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'uuid'
op|','
nl|'\n'
string|"'get-vnc-console-post-req'"
op|','
nl|'\n'
op|'{'
string|"'action'"
op|':'
string|"'os-getVNCConsole'"
op|'}'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|'"url"'
op|']'
op|'='
string|'"((https?):((//)|(\\\\\\\\))+([\\w\\d:#@%/;$()~_?\\+-=\\\\\\.&](#!)?)*)"'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'get-vnc-console-post-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_spice_console
dedent|''
name|'def'
name|'test_get_spice_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'uuid'
op|','
nl|'\n'
string|"'get-spice-console-post-req'"
op|','
nl|'\n'
op|'{'
string|"'action'"
op|':'
string|"'os-getSPICEConsole'"
op|'}'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|'"url"'
op|']'
op|'='
string|'"((https?):((//)|(\\\\\\\\))+([\\w\\d:#@%/;$()~_?\\+-=\\\\\\.&](#!)?)*)"'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'get-spice-console-post-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_rdp_console
dedent|''
name|'def'
name|'test_get_rdp_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'uuid'
op|','
nl|'\n'
string|"'get-rdp-console-post-req'"
op|','
nl|'\n'
op|'{'
string|"'action'"
op|':'
string|"'os-getRDPConsole'"
op|'}'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|'"url"'
op|']'
op|'='
string|'"((https?):((//)|(\\\\\\\\))+([\\w\\d:#@%/;$()~_?\\+-=\\\\\\.&](#!)?)*)"'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'get-rdp-console-post-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_serial_console
dedent|''
name|'def'
name|'test_get_serial_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'uuid'
op|','
nl|'\n'
string|"'get-serial-console-post-req'"
op|','
nl|'\n'
op|'{'
string|"'action'"
op|':'
string|"'os-getSerialConsole'"
op|'}'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|'"url"'
op|']'
op|'='
string|'"((ws?):((//)|(\\\\\\\\))+([\\w\\d:#@%/;$()~_?\\+-=\\\\\\.&](#!)?)*)"'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'get-serial-console-post-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsolesV26SampleJsonTests
dedent|''
dedent|''
name|'class'
name|'ConsolesV26SampleJsonTests'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|request_api_version
indent|'    '
name|'request_api_version'
op|'='
string|"'2.6'"
newline|'\n'
DECL|variable|extension_name
name|'extension_name'
op|'='
string|'"os-remote-consoles"'
newline|'\n'
comment|'# NOTE(gmann): microversion tests do not need to run for v2 API'
nl|'\n'
comment|'# so defining scenarios only for v2.6 which will run the original tests'
nl|'\n'
comment|"# by appending '(v2_6)' in test_id."
nl|'\n'
DECL|variable|scenarios
name|'scenarios'
op|'='
op|'['
op|'('
string|"'v2_6'"
op|','
op|'{'
string|"'_api_version'"
op|':'
string|"'v2.1'"
op|'}'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'ConsolesV26SampleJsonTests'
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
name|'http_regex'
op|'='
string|'"(https?://)([\\w\\d:#@%/;$()~_?\\+-=\\\\\\.&](#!)?)*"'
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
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'protocol'"
op|':'
string|"'vnc'"
op|','
string|"'type'"
op|':'
string|"'novnc'"
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/remote-consoles'"
op|'%'
name|'uuid'
op|','
nl|'\n'
string|"'create-vnc-console-req'"
op|','
name|'body'
op|','
nl|'\n'
name|'api_version'
op|'='
string|"'2.6'"
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|'"url"'
op|']'
op|'='
name|'self'
op|'.'
name|'http_regex'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'create-vnc-console-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsolesV28SampleJsonTests
dedent|''
dedent|''
name|'class'
name|'ConsolesV28SampleJsonTests'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|'"os-remote-consoles"'
newline|'\n'
DECL|variable|request_api_version
name|'request_api_version'
op|'='
string|"'2.8'"
newline|'\n'
DECL|variable|scenarios
name|'scenarios'
op|'='
op|'['
op|'('
string|"'v2_8'"
op|','
op|'{'
string|"'_api_version'"
op|':'
string|"'v2.1'"
op|'}'
op|')'
op|']'
newline|'\n'
DECL|variable|_api_version
name|'_api_version'
op|'='
string|"'v2'"
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'ConsolesV28SampleJsonTests'
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
name|'http_regex'
op|'='
string|'"(https?://)([\\w\\d:#@%/;$()~_?\\+-=\\\\\\.&](#!)?)*"'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'enabled'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'mks'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_mks_console
dedent|''
name|'def'
name|'test_create_mks_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'protocol'"
op|':'
string|"'mks'"
op|','
string|"'type'"
op|':'
string|"'webmks'"
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/remote-consoles'"
op|'%'
name|'uuid'
op|','
nl|'\n'
string|"'create-mks-console-req'"
op|','
name|'body'
op|','
nl|'\n'
name|'api_version'
op|'='
string|"'2.8'"
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|'"url"'
op|']'
op|'='
name|'self'
op|'.'
name|'http_regex'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'create-mks-console-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
