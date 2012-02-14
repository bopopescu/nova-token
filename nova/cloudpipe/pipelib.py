begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nCloudPipe - Build a user-data payload zip file, and launch\nan instance with it.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
name|'import'
name|'zipfile'
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
name|'crypto'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
comment|'# TODO(eday): Eventually changes these to something not ec2-specific'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'cloud'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'ec2utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|cloudpipe_opts
name|'cloudpipe_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'boot_script_template'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'cloudpipe/bootscript.template'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Template for cloudpipe instance boot script'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'dmz_net'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'10.0.0.0'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Network to push into openvpn config'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'dmz_mask'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'255.255.255.0'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Netmask to push into openvpn config'"
op|')'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'cloudpipe_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
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
nl|'\n'
nl|'\n'
DECL|class|CloudPipe
name|'class'
name|'CloudPipe'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'controller'
op|'='
name|'cloud'
op|'.'
name|'CloudController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_encoded_zip
dedent|''
name|'def'
name|'get_encoded_zip'
op|'('
name|'self'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
comment|'# Make a payload.zip'
nl|'\n'
indent|'        '
name|'tmpfolder'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
name|'filename'
op|'='
string|'"payload.zip"'
newline|'\n'
name|'zippath'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpfolder'
op|','
name|'filename'
op|')'
newline|'\n'
name|'z'
op|'='
name|'zipfile'
op|'.'
name|'ZipFile'
op|'('
name|'zippath'
op|','
string|'"w"'
op|','
name|'zipfile'
op|'.'
name|'ZIP_DEFLATED'
op|')'
newline|'\n'
name|'shellfile'
op|'='
name|'open'
op|'('
name|'FLAGS'
op|'.'
name|'boot_script_template'
op|','
string|'"r"'
op|')'
newline|'\n'
name|'s'
op|'='
name|'string'
op|'.'
name|'Template'
op|'('
name|'shellfile'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
name|'shellfile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'boot_script'
op|'='
name|'s'
op|'.'
name|'substitute'
op|'('
name|'cc_dmz'
op|'='
name|'FLAGS'
op|'.'
name|'ec2_dmz_host'
op|','
nl|'\n'
name|'cc_port'
op|'='
name|'FLAGS'
op|'.'
name|'ec2_port'
op|','
nl|'\n'
name|'dmz_net'
op|'='
name|'FLAGS'
op|'.'
name|'dmz_net'
op|','
nl|'\n'
name|'dmz_mask'
op|'='
name|'FLAGS'
op|'.'
name|'dmz_mask'
op|','
nl|'\n'
name|'num_vpn'
op|'='
name|'FLAGS'
op|'.'
name|'cnt_vpn_clients'
op|')'
newline|'\n'
comment|'# genvpn, sign csr'
nl|'\n'
name|'crypto'
op|'.'
name|'generate_vpn_files'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'z'
op|'.'
name|'writestr'
op|'('
string|"'autorun.sh'"
op|','
name|'boot_script'
op|')'
newline|'\n'
name|'crl'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'crypto'
op|'.'
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|','
string|"'crl.pem'"
op|')'
newline|'\n'
name|'z'
op|'.'
name|'write'
op|'('
name|'crl'
op|','
string|"'crl.pem'"
op|')'
newline|'\n'
name|'server_key'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'crypto'
op|'.'
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|','
string|"'server.key'"
op|')'
newline|'\n'
name|'z'
op|'.'
name|'write'
op|'('
name|'server_key'
op|','
string|"'server.key'"
op|')'
newline|'\n'
name|'ca_crt'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'crypto'
op|'.'
name|'ca_path'
op|'('
name|'project_id'
op|')'
op|')'
newline|'\n'
name|'z'
op|'.'
name|'write'
op|'('
name|'ca_crt'
op|','
string|"'ca.crt'"
op|')'
newline|'\n'
name|'server_crt'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'crypto'
op|'.'
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|','
string|"'server.crt'"
op|')'
newline|'\n'
name|'z'
op|'.'
name|'write'
op|'('
name|'server_crt'
op|','
string|"'server.crt'"
op|')'
newline|'\n'
name|'z'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'zippy'
op|'='
name|'open'
op|'('
name|'zippath'
op|','
string|'"r"'
op|')'
newline|'\n'
comment|'# NOTE(vish): run instances expects encoded userdata, it is decoded'
nl|'\n'
comment|'# in the get_metadata_call. autorun.sh also decodes the zip file,'
nl|'\n'
comment|'# hence the double encoding.'
nl|'\n'
name|'encoded'
op|'='
name|'zippy'
op|'.'
name|'read'
op|'('
op|')'
op|'.'
name|'encode'
op|'('
string|'"base64"'
op|')'
op|'.'
name|'encode'
op|'('
string|'"base64"'
op|')'
newline|'\n'
name|'zippy'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'return'
name|'encoded'
newline|'\n'
nl|'\n'
DECL|member|launch_vpn_instance
dedent|''
name|'def'
name|'launch_vpn_instance'
op|'('
name|'self'
op|','
name|'project_id'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Launching VPN for %s"'
op|')'
op|'%'
op|'('
name|'project_id'
op|')'
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user_id'
op|'='
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|')'
newline|'\n'
name|'key_name'
op|'='
name|'self'
op|'.'
name|'setup_key_pair'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'group_name'
op|'='
name|'self'
op|'.'
name|'setup_security_group'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
name|'ec2_id'
op|'='
name|'ec2utils'
op|'.'
name|'image_ec2_id'
op|'('
name|'FLAGS'
op|'.'
name|'vpn_image_id'
op|')'
newline|'\n'
name|'reservation'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'run_instances'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'user_data'
op|'='
name|'self'
op|'.'
name|'get_encoded_zip'
op|'('
name|'project_id'
op|')'
op|','
nl|'\n'
name|'max_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'min_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'instance_type'
op|'='
string|"'m1.tiny'"
op|','
nl|'\n'
name|'image_id'
op|'='
name|'ec2_id'
op|','
nl|'\n'
name|'key_name'
op|'='
name|'key_name'
op|','
nl|'\n'
name|'security_group'
op|'='
op|'['
name|'group_name'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_security_group
dedent|''
name|'def'
name|'setup_security_group'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group_name'
op|'='
string|"'%s%s'"
op|'%'
op|'('
name|'context'
op|'.'
name|'project_id'
op|','
name|'FLAGS'
op|'.'
name|'vpn_key_suffix'
op|')'
newline|'\n'
name|'if'
name|'db'
op|'.'
name|'security_group_exists'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'project_id'
op|','
name|'group_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'group_name'
newline|'\n'
dedent|''
name|'group'
op|'='
op|'{'
string|"'user_id'"
op|':'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'group_name'
op|','
nl|'\n'
string|"'description'"
op|':'
string|"'Group for vpn'"
op|'}'
newline|'\n'
name|'group_ref'
op|'='
name|'db'
op|'.'
name|'security_group_create'
op|'('
name|'context'
op|','
name|'group'
op|')'
newline|'\n'
name|'rule'
op|'='
op|'{'
string|"'parent_group_id'"
op|':'
name|'group_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'0.0.0.0/0'"
op|','
nl|'\n'
string|"'protocol'"
op|':'
string|"'udp'"
op|','
nl|'\n'
string|"'from_port'"
op|':'
number|'1194'
op|','
nl|'\n'
string|"'to_port'"
op|':'
number|'1194'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'security_group_rule_create'
op|'('
name|'context'
op|','
name|'rule'
op|')'
newline|'\n'
name|'rule'
op|'='
op|'{'
string|"'parent_group_id'"
op|':'
name|'group_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'0.0.0.0/0'"
op|','
nl|'\n'
string|"'protocol'"
op|':'
string|"'icmp'"
op|','
nl|'\n'
string|"'from_port'"
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
string|"'to_port'"
op|':'
op|'-'
number|'1'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'security_group_rule_create'
op|'('
name|'context'
op|','
name|'rule'
op|')'
newline|'\n'
comment|'# NOTE(vish): No need to trigger the group since the instance'
nl|'\n'
comment|'#             has not been run yet.'
nl|'\n'
name|'return'
name|'group_name'
newline|'\n'
nl|'\n'
DECL|member|setup_key_pair
dedent|''
name|'def'
name|'setup_key_pair'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key_name'
op|'='
string|"'%s%s'"
op|'%'
op|'('
name|'context'
op|'.'
name|'project_id'
op|','
name|'FLAGS'
op|'.'
name|'vpn_key_suffix'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'cloud'
op|'.'
name|'_gen_key'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'user_id'
op|','
name|'key_name'
op|')'
newline|'\n'
name|'private_key'
op|'='
name|'result'
op|'['
string|"'private_key'"
op|']'
newline|'\n'
name|'key_dir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'keys_path'
op|','
name|'context'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'key_dir'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'key_dir'
op|')'
newline|'\n'
dedent|''
name|'key_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'key_dir'
op|','
string|"'%s.pem'"
op|'%'
name|'key_name'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'key_path'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'f'
op|'.'
name|'write'
op|'('
name|'private_key'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'Duplicate'
op|','
name|'os'
op|'.'
name|'error'
op|','
name|'IOError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'return'
name|'key_name'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
