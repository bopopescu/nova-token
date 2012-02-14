begin_unit
comment|'#   Copyright 2011 Openstack, LLC.'
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
name|'import'
name|'os'
newline|'\n'
nl|'\n'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
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
name|'vm_states'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
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
name|'log'
name|'as'
name|'logging'
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
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'cloudpipe'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CloudpipeTemplate
name|'class'
name|'CloudpipeTemplate'
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
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'make_flat_dict'
op|'('
string|"'cloudpipe'"
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CloudpipesTemplate
dedent|''
dedent|''
name|'class'
name|'CloudpipesTemplate'
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
string|"'cloudpipes'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'make_flat_dict'
op|'('
string|"'cloudpipe'"
op|','
name|'selector'
op|'='
string|"'cloudpipes'"
op|','
nl|'\n'
name|'subselector'
op|'='
string|"'cloudpipe'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'append'
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
DECL|class|CloudpipeController
dedent|''
dedent|''
name|'class'
name|'CloudpipeController'
op|'('
name|'object'
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
name|'auth_manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
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
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'FLAGS'
op|'.'
name|'keys_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'FLAGS'
op|'.'
name|'keys_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_cloudpipe_for_project
dedent|''
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
comment|'# NOTE(todd): this should probably change to compute_api.get_all'
nl|'\n'
comment|'#             or db.instance_get_project_vpn'
nl|'\n'
name|'for'
name|'instance'
name|'in'
name|'db'
op|'.'
name|'instance_get_all_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'instance'
op|'['
string|"'image_id'"
op|']'
op|'=='
name|'str'
op|'('
name|'FLAGS'
op|'.'
name|'vpn_image_id'
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
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|member|_vpn_dict
dedent|''
dedent|''
dedent|''
name|'def'
name|'_vpn_dict'
op|'('
name|'self'
op|','
name|'project'
op|','
name|'vpn_instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rv'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'project'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'public_ip'"
op|':'
name|'project'
op|'.'
name|'vpn_ip'
op|','
nl|'\n'
string|"'public_port'"
op|':'
name|'project'
op|'.'
name|'vpn_port'
op|'}'
newline|'\n'
name|'if'
name|'vpn_instance'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'vpn_instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'rv'
op|'['
string|"'created_at'"
op|']'
op|'='
name|'utils'
op|'.'
name|'isotime'
op|'('
name|'vpn_instance'
op|'['
string|"'created_at'"
op|']'
op|')'
newline|'\n'
name|'address'
op|'='
name|'vpn_instance'
op|'.'
name|'get'
op|'('
string|"'fixed_ip'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'address'
op|':'
newline|'\n'
indent|'                '
name|'rv'
op|'['
string|"'internal_ip'"
op|']'
op|'='
name|'address'
op|'['
string|"'address'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'project'
op|'.'
name|'vpn_ip'
name|'and'
name|'project'
op|'.'
name|'vpn_port'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'utils'
op|'.'
name|'vpn_ping'
op|'('
name|'project'
op|'.'
name|'vpn_ip'
op|','
name|'project'
op|'.'
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
name|'else'
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
dedent|''
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'CloudpipeTemplate'
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
string|'"""Create a new cloudpipe instance, if none exists.\n\n        Parameters: {cloudpipe: {project_id: XYZ}}\n        """'
newline|'\n'
nl|'\n'
name|'ctxt'
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
name|'ctxt'
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
name|'ctxt'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_get_cloudpipe_for_project'
op|'('
name|'ctxt'
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
name|'proj'
op|'='
name|'self'
op|'.'
name|'auth_manager'
op|'.'
name|'get_project'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'user_id'
op|'='
name|'proj'
op|'.'
name|'project_manager_id'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'cloudpipe'
op|'.'
name|'launch_vpn_instance'
op|'('
name|'project_id'
op|','
name|'user_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'db'
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
name|'exception'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'instance'
op|'='
name|'self'
op|'.'
name|'_get_cloudpipe_for_project'
op|'('
name|'ctxt'
op|','
name|'proj'
op|')'
newline|'\n'
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
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'CloudpipesTemplate'
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
op|']'
newline|'\n'
comment|'# TODO(todd): could use compute_api.get_all with admin context?'
nl|'\n'
name|'for'
name|'project'
name|'in'
name|'self'
op|'.'
name|'auth_manager'
op|'.'
name|'get_projects'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_get_cloudpipe_for_project'
op|'('
name|'context'
op|','
name|'project'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'vpns'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_vpn_dict'
op|'('
name|'project'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'cloudpipes'"
op|':'
name|'vpns'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Cloudpipe
dedent|''
dedent|''
name|'class'
name|'Cloudpipe'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
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
string|'"os-cloudpipe"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/cloudpipe/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-12-16T00:00:00+00:00"'
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
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-cloudpipe'"
op|','
nl|'\n'
name|'CloudpipeController'
op|'('
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
