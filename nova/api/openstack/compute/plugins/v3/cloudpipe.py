begin_unit
comment|'#   Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#   not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#   a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#       http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#   License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#   under the License.'
nl|'\n'
nl|'\n'
string|'"""Connect your vlan to the world."""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'schemas'
op|'.'
name|'v3'
name|'import'
name|'cloudpipe'
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
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'validation'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cloudpipe'
name|'import'
name|'pipelib'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
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
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'fileutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
string|"'keys_path'"
op|','
string|"'nova.crypto'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-cloudpipe'"
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'v3:'"
op|'+'
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CloudpipeController
name|'class'
name|'CloudpipeController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Handle creating and listing cloudpipe instances."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloudpipe'
op|'='
name|'pipelib'
op|'.'
name|'CloudPipe'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup
dedent|''
name|'def'
name|'setup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure the keychains and folders exist."""'
newline|'\n'
comment|'# NOTE(vish): One of the drawbacks of doing this in the api is'
nl|'\n'
comment|'#             the keys will only be on the api node that launched'
nl|'\n'
comment|'#             the cloudpipe.'
nl|'\n'
name|'fileutils'
op|'.'
name|'ensure_tree'
op|'('
name|'CONF'
op|'.'
name|'keys_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_all_cloudpipes
dedent|''
name|'def'
name|'_get_all_cloudpipes'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get all cloudpipes."""'
newline|'\n'
name|'instances'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_all'
op|'('
name|'context'
op|','
nl|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'deleted'"
op|':'
name|'False'
op|'}'
op|')'
newline|'\n'
name|'return'
op|'['
name|'instance'
name|'for'
name|'instance'
name|'in'
name|'instances'
nl|'\n'
name|'if'
name|'pipelib'
op|'.'
name|'is_vpn_image'
op|'('
name|'instance'
op|'['
string|"'image_ref'"
op|']'
op|')'
nl|'\n'
name|'and'
name|'instance'
op|'['
string|"'vm_state'"
op|']'
op|'!='
name|'vm_states'
op|'.'
name|'DELETED'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_cloudpipe_for_project
dedent|''
name|'def'
name|'_get_cloudpipe_for_project'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the cloudpipe instance for a project ID."""'
newline|'\n'
name|'cloudpipes'
op|'='
name|'self'
op|'.'
name|'_get_all_cloudpipes'
op|'('
name|'context'
op|')'
name|'or'
op|'['
name|'None'
op|']'
newline|'\n'
name|'return'
name|'cloudpipes'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_ip_and_port
dedent|''
name|'def'
name|'_get_ip_and_port'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_vpn_dict
dedent|''
name|'def'
name|'_vpn_dict'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'elevated'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'rv'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'project_id'
op|'}'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'['
string|"'state'"
op|']'
op|'='
string|"'pending'"
newline|'\n'
name|'return'
name|'rv'
newline|'\n'
dedent|''
name|'rv'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'rv'
op|'['
string|"'created_at'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'instance'
op|'['
string|"'created_at'"
op|']'
op|')'
newline|'\n'
name|'nw_info'
op|'='
name|'compute_utils'
op|'.'
name|'get_nw_info_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'nw_info'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'rv'
newline|'\n'
dedent|''
name|'vif'
op|'='
name|'nw_info'
op|'['
number|'0'
op|']'
newline|'\n'
name|'ips'
op|'='
op|'['
name|'ip'
name|'for'
name|'ip'
name|'in'
name|'vif'
op|'.'
name|'fixed_ips'
op|'('
op|')'
name|'if'
name|'ip'
op|'['
string|"'version'"
op|']'
op|'=='
number|'4'
op|']'
newline|'\n'
name|'if'
name|'ips'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'['
string|"'internal_ip'"
op|']'
op|'='
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
comment|'# NOTE(vish): Currently network_api.get does an owner check on'
nl|'\n'
comment|'#             project_id. This is probably no longer necessary'
nl|'\n'
comment|'#             but rather than risk changes in the db layer,'
nl|'\n'
comment|'#             we are working around it here by changing the'
nl|'\n'
comment|'#             project_id in the context. This can be removed'
nl|'\n'
comment|'#             if we remove the project_id check in the db.'
nl|'\n'
dedent|''
name|'elevated'
op|'.'
name|'project_id'
op|'='
name|'project_id'
newline|'\n'
name|'network'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get'
op|'('
name|'elevated'
op|','
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'network'
op|':'
newline|'\n'
indent|'            '
name|'vpn_ip'
op|'='
name|'network'
op|'['
string|"'vpn_public_address'"
op|']'
newline|'\n'
name|'vpn_port'
op|'='
name|'network'
op|'['
string|"'vpn_public_port'"
op|']'
newline|'\n'
name|'rv'
op|'['
string|"'public_ip'"
op|']'
op|'='
name|'vpn_ip'
newline|'\n'
name|'rv'
op|'['
string|"'public_port'"
op|']'
op|'='
name|'vpn_port'
newline|'\n'
name|'if'
name|'vpn_ip'
name|'and'
name|'vpn_port'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'utils'
op|'.'
name|'vpn_ping'
op|'('
name|'vpn_ip'
op|','
name|'vpn_port'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'rv'
op|'['
string|"'state'"
op|']'
op|'='
string|"'running'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'rv'
op|'['
string|"'state'"
op|']'
op|'='
string|"'down'"
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'rv'
op|'['
string|"'state'"
op|']'
op|'='
string|"'invalid'"
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'403'
op|')'
op|')'
newline|'\n'
DECL|member|create
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
string|'"""Create a new cloudpipe instance, if none exists.\n\n        Parameters: {cloudpipe: {\'project_id\': \'\'}}\n        """'
newline|'\n'
nl|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'params'
op|'='
name|'body'
op|'.'
name|'get'
op|'('
string|"'cloudpipe'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'project_id'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'project_id'"
op|','
name|'context'
op|'.'
name|'project_id'
op|')'
newline|'\n'
comment|'# NOTE(vish): downgrade to project context. Note that we keep'
nl|'\n'
comment|'#             the same token so we can still talk to glance'
nl|'\n'
name|'context'
op|'.'
name|'project_id'
op|'='
name|'project_id'
newline|'\n'
name|'context'
op|'.'
name|'user_id'
op|'='
string|"'project-vpn'"
newline|'\n'
name|'context'
op|'.'
name|'is_admin'
op|'='
name|'False'
newline|'\n'
name|'context'
op|'.'
name|'roles'
op|'='
op|'['
op|']'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_get_cloudpipe_for_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'self'
op|'.'
name|'cloudpipe'
op|'.'
name|'launch_vpn_instance'
op|'('
name|'context'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'result'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NoMoreNetworks'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Unable to claim IP for VPN instances, ensure it "'
nl|'\n'
string|'"isn\'t running, and try again in a few minutes"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
op|'{'
string|"'instance_id'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'403'
op|','
number|'404'
op|')'
op|')'
newline|'\n'
DECL|member|index
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
string|'"""List running cloudpipe instances."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'vpns'
op|'='
op|'['
name|'self'
op|'.'
name|'_vpn_dict'
op|'('
name|'context'
op|','
name|'x'
op|'['
string|"'project_id'"
op|']'
op|','
name|'x'
op|')'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'_get_all_cloudpipes'
op|'('
name|'context'
op|')'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'cloudpipes'"
op|':'
name|'vpns'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'400'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'cloudpipe'
op|'.'
name|'update'
op|')'
newline|'\n'
DECL|member|update
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
string|'"""Configure cloudpipe parameters for the project."""'
newline|'\n'
nl|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'id'
op|'!='
string|'"configure-project"'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Unknown action %s"'
op|')'
op|'%'
name|'id'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
name|'networks'
op|'='
name|'objects'
op|'.'
name|'NetworkList'
op|'.'
name|'get_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
name|'params'
op|'='
name|'body'
op|'['
string|"'configure_project'"
op|']'
newline|'\n'
name|'vpn_ip'
op|'='
name|'params'
op|'['
string|"'vpn_ip'"
op|']'
newline|'\n'
name|'vpn_port'
op|'='
name|'params'
op|'['
string|"'vpn_port'"
op|']'
newline|'\n'
name|'for'
name|'nw'
name|'in'
name|'networks'
op|':'
newline|'\n'
indent|'            '
name|'nw'
op|'.'
name|'vpn_public_address'
op|'='
name|'vpn_ip'
newline|'\n'
name|'nw'
op|'.'
name|'vpn_public_port'
op|'='
name|'vpn_port'
newline|'\n'
name|'nw'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Cloudpipe
dedent|''
dedent|''
dedent|''
name|'class'
name|'Cloudpipe'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Adds actions to create cloudpipe instances.\n\n    When running with the Vlan network mode, you need a mechanism to route\n    from the public Internet to your vlans.  This mechanism is known as a\n    cloudpipe.\n\n    At the time of creating this class, only OpenVPN is supported.  Support for\n    a SSH Bastion host is forthcoming.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Cloudpipe"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resource'
op|'='
op|'['
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
nl|'\n'
name|'CloudpipeController'
op|'('
op|')'
op|')'
op|']'
newline|'\n'
name|'return'
name|'resource'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""It\'s an abstract function V3APIExtensionBase and the extension\n        will not be loaded without it.\n        """'
newline|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
