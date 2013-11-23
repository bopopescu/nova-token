begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'integrated'
op|'.'
name|'v3'
name|'import'
name|'api_sample_base'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersSampleBase
name|'class'
name|'ServersSampleBase'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV3'
op|')'
op|':'
newline|'\n'
DECL|member|_post_server
indent|'    '
name|'def'
name|'_post_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'image_id'"
op|':'
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'_get_host'
op|'('
op|')'
op|','
nl|'\n'
string|"'glance_host'"
op|':'
name|'self'
op|'.'
name|'_get_glance_host'
op|'('
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers'"
op|','
string|"'server-post-req'"
op|','
name|'subs'
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
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-post-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'202'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersSampleJsonTest
dedent|''
dedent|''
name|'class'
name|'ServersSampleJsonTest'
op|'('
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|sample_dir
indent|'    '
name|'sample_dir'
op|'='
string|"'servers'"
newline|'\n'
nl|'\n'
DECL|member|test_servers_post
name|'def'
name|'test_servers_post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_get
dedent|''
name|'def'
name|'test_servers_get'
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
name|'test_servers_post'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s'"
op|'%'
name|'uuid'
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
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'id'"
op|']'
op|'='
name|'uuid'
newline|'\n'
name|'subs'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|'='
string|"r'[\\w\\.\\-]+'"
newline|'\n'
name|'subs'
op|'['
string|"'mac_addr'"
op|']'
op|'='
string|"'(?:[a-f0-9]{2}:){5}[a-f0-9]{2}'"
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_list
dedent|''
name|'def'
name|'test_servers_list'
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
name|'_do_get'
op|'('
string|"'servers'"
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
string|"'id'"
op|']'
op|'='
name|'uuid'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'servers-list-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_details
dedent|''
name|'def'
name|'test_servers_details'
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
name|'_do_get'
op|'('
string|"'servers/detail'"
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
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'id'"
op|']'
op|'='
name|'uuid'
newline|'\n'
name|'subs'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|'='
string|"r'[\\w\\.\\-]+'"
newline|'\n'
name|'subs'
op|'['
string|"'mac_addr'"
op|']'
op|'='
string|"'(?:[a-f0-9]{2}:){5}[a-f0-9]{2}'"
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'servers-details-resp'"
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
DECL|class|ServersSampleXmlTest
dedent|''
dedent|''
name|'class'
name|'ServersSampleXmlTest'
op|'('
name|'ServersSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|ctype
indent|'    '
name|'ctype'
op|'='
string|"'xml'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersSampleAllExtensionJsonTest
dedent|''
name|'class'
name|'ServersSampleAllExtensionJsonTest'
op|'('
name|'ServersSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|all_extensions
indent|'    '
name|'all_extensions'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersSampleAllExtensionXmlTest
dedent|''
name|'class'
name|'ServersSampleAllExtensionXmlTest'
op|'('
name|'ServersSampleXmlTest'
op|')'
op|':'
newline|'\n'
DECL|variable|all_extensions
indent|'    '
name|'all_extensions'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersActionsJsonTest
dedent|''
name|'class'
name|'ServersActionsJsonTest'
op|'('
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|sample_dir
indent|'    '
name|'sample_dir'
op|'='
string|"'servers'"
newline|'\n'
nl|'\n'
DECL|member|_test_server_action
name|'def'
name|'_test_server_action'
op|'('
name|'self'
op|','
name|'uuid'
op|','
name|'action'
op|','
nl|'\n'
name|'subs'
op|'='
op|'{'
op|'}'
op|','
name|'resp_tpl'
op|'='
name|'None'
op|','
name|'code'
op|'='
number|'202'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'.'
name|'update'
op|'('
op|'{'
string|"'action'"
op|':'
name|'action'
op|','
nl|'\n'
string|"'glance_host'"
op|':'
name|'self'
op|'.'
name|'_get_glance_host'
op|'('
op|')'
op|'}'
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
string|"'server-action-%s'"
op|'%'
name|'action'
op|'.'
name|'replace'
op|'('
string|"'_'"
op|','
nl|'\n'
string|"'-'"
op|')'
op|','
nl|'\n'
name|'subs'
op|')'
newline|'\n'
name|'if'
name|'resp_tpl'
op|':'
newline|'\n'
indent|'            '
name|'subs'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
name|'resp_tpl'
op|','
name|'subs'
op|','
name|'response'
op|','
name|'code'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status'
op|','
name|'code'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'read'
op|'('
op|')'
op|','
string|'""'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_reboot_hard
dedent|''
dedent|''
name|'def'
name|'test_server_reboot_hard'
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
name|'self'
op|'.'
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|'"reboot"'
op|','
nl|'\n'
op|'{'
string|'"type"'
op|':'
string|'"HARD"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_reboot_soft
dedent|''
name|'def'
name|'test_server_reboot_soft'
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
name|'self'
op|'.'
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|'"reboot"'
op|','
nl|'\n'
op|'{'
string|'"type"'
op|':'
string|'"SOFT"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_rebuild
dedent|''
name|'def'
name|'test_server_rebuild'
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
name|'image'
op|'='
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'_get_host'
op|'('
op|')'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'image'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'foobar'"
op|','
nl|'\n'
string|"'pass'"
op|':'
string|"'seekr3t'"
op|','
nl|'\n'
string|"'hostid'"
op|':'
string|"'[a-f0-9]+'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|"'rebuild'"
op|','
name|'subs'
op|','
nl|'\n'
string|"'server-action-rebuild-resp'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_resize
dedent|''
name|'def'
name|'test_server_resize'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'allow_resize_to_same_host'
op|'='
name|'True'
op|')'
newline|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|'"resize"'
op|','
nl|'\n'
op|'{'
string|'"id"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"host"'
op|':'
name|'self'
op|'.'
name|'_get_host'
op|'('
op|')'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'uuid'
newline|'\n'
nl|'\n'
DECL|member|test_server_revert_resize
dedent|''
name|'def'
name|'test_server_revert_resize'
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
name|'test_server_resize'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|'"revert_resize"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_confirm_resize
dedent|''
name|'def'
name|'test_server_confirm_resize'
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
name|'test_server_resize'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|'"confirm_resize"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_create_image
dedent|''
name|'def'
name|'test_server_create_image'
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
name|'self'
op|'.'
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|"'create_image'"
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'foo-image'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersActionsXmlTest
dedent|''
dedent|''
name|'class'
name|'ServersActionsXmlTest'
op|'('
name|'ServersActionsJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|ctype
indent|'    '
name|'ctype'
op|'='
string|"'xml'"
newline|'\n'
dedent|''
endmarker|''
end_unit
