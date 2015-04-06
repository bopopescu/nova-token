begin_unit
comment|'# Copyright 2015 IBM Corp.'
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
name|'mock'
newline|'\n'
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
name|'v3'
name|'import'
name|'api_sample_base'
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
string|"'nova.api.openstack.compute.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeNode
name|'class'
name|'FakeNode'
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
name|'uuid'
op|'='
string|"'058d27fa-241b-445a-a386-08c04f96db43'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'uuid'
op|'='
name|'uuid'
newline|'\n'
name|'self'
op|'.'
name|'provision_state'
op|'='
string|"'active'"
newline|'\n'
name|'self'
op|'.'
name|'properties'
op|'='
op|'{'
string|"'cpus'"
op|':'
string|"'2'"
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
string|"'1024'"
op|','
nl|'\n'
string|"'local_gb'"
op|':'
string|"'10'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'instance_uuid'
op|'='
string|"'1ea4e53e-149a-4f02-9515-590c9fb2315a'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NodeManager
dedent|''
dedent|''
name|'class'
name|'NodeManager'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|list
indent|'    '
name|'def'
name|'list'
op|'('
name|'self'
op|','
name|'detail'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'FakeNode'
op|'('
op|')'
op|','
name|'FakeNode'
op|'('
string|"'e2025409-f3ce-4d6a-9788-c565cf3b1b1c'"
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FakeNode'
op|'('
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|list_ports
dedent|''
name|'def'
name|'list_ports'
op|'('
name|'self'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|fake_client
dedent|''
dedent|''
name|'class'
name|'fake_client'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|node
indent|'    '
name|'node'
op|'='
name|'NodeManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalNodesSampleJsonTest
dedent|''
name|'class'
name|'BareMetalNodesSampleJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV3'
op|')'
op|':'
newline|'\n'
DECL|variable|ADMIN_API
indent|'    '
name|'ADMIN_API'
op|'='
name|'True'
newline|'\n'
DECL|variable|extension_name
name|'extension_name'
op|'='
string|'"os-baremetal-nodes"'
newline|'\n'
comment|"# TODO(gmann): Overriding '_api_version' till all functional tests"
nl|'\n'
comment|'# are merged between v2 and v2.1. After that base class variable'
nl|'\n'
comment|"# itself can be changed to 'v2'"
nl|'\n'
DECL|variable|_api_version
name|'_api_version'
op|'='
string|"'v2'"
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
name|'BareMetalNodesSampleJsonTest'
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
string|"'nova.api.openstack.compute.'"
nl|'\n'
string|"'contrib.baremetal_nodes.Baremetal_nodes'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|'"nova.api.openstack.compute.plugins.v3.baremetal_nodes"'
nl|'\n'
string|'"._get_ironic_client"'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|'"nova.api.openstack.compute.contrib.baremetal_nodes"'
nl|'\n'
string|'"._get_ironic_client"'
op|')'
newline|'\n'
DECL|member|test_baremetal_nodes_list
name|'def'
name|'test_baremetal_nodes_list'
op|'('
name|'self'
op|','
name|'mock_get_irc'
op|','
name|'v2_1_mock_get_irc'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_irc'
op|'.'
name|'return_value'
op|'='
name|'fake_client'
op|'('
op|')'
newline|'\n'
name|'v2_1_mock_get_irc'
op|'.'
name|'return_value'
op|'='
name|'fake_client'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-baremetal-nodes'"
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
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'baremetal-node-list-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|'"nova.api.openstack.compute.plugins.v3.baremetal_nodes"'
nl|'\n'
string|'"._get_ironic_client"'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|'"nova.api.openstack.compute.contrib.baremetal_nodes"'
nl|'\n'
string|'"._get_ironic_client"'
op|')'
newline|'\n'
DECL|member|test_baremetal_nodes_get
name|'def'
name|'test_baremetal_nodes_get'
op|'('
name|'self'
op|','
name|'mock_get_irc'
op|','
name|'v2_1_mock_get_irc'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_irc'
op|'.'
name|'return_value'
op|'='
name|'fake_client'
op|'('
op|')'
newline|'\n'
name|'v2_1_mock_get_irc'
op|'.'
name|'return_value'
op|'='
name|'fake_client'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-baremetal-nodes/'"
nl|'\n'
string|"'058d27fa-241b-445a-a386-08c04f96db43'"
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
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'baremetal-node-get-resp'"
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
