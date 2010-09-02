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
name|'base64'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
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
name|'utils'
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
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'context'
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
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'boot_script_template'"
op|','
nl|'\n'
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'cloudpipe/bootscript.sh'"
op|')'
op|','
nl|'\n'
string|"'Template for script to run on cloudpipe instance boot'"
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
op|','
name|'cloud_controller'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'controller'
op|'='
name|'cloud_controller'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Launching VPN for %s"'
op|'%'
op|'('
name|'project_id'
op|')'
op|')'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_project'
op|'('
name|'project_id'
op|')'
newline|'\n'
comment|'# Make a payload.zip'
nl|'\n'
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
nl|'\n'
name|'z'
op|'.'
name|'write'
op|'('
name|'FLAGS'
op|'.'
name|'boot_script_template'
op|','
string|"'autorun.sh'"
op|')'
newline|'\n'
name|'z'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'key_name'
op|'='
name|'self'
op|'.'
name|'setup_keypair'
op|'('
name|'project'
op|'.'
name|'project_manager_id'
op|','
name|'project_id'
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
name|'context'
op|'='
name|'context'
op|'.'
name|'APIRequestContext'
op|'('
name|'user'
op|'='
name|'project'
op|'.'
name|'project_manager'
op|','
name|'project'
op|'='
name|'project'
op|')'
newline|'\n'
nl|'\n'
name|'reservation'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'run_instances'
op|'('
name|'context'
op|','
nl|'\n'
comment|'# run instances expects encoded userdata, it is decoded in the get_metadata_call'
nl|'\n'
comment|'# autorun.sh also decodes the zip file, hence the double encoding'
nl|'\n'
name|'user_data'
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
name|'FLAGS'
op|'.'
name|'vpn_image_id'
op|','
nl|'\n'
name|'key_name'
op|'='
name|'key_name'
op|','
nl|'\n'
name|'security_groups'
op|'='
op|'['
string|'"vpn-secgroup"'
op|']'
op|')'
newline|'\n'
name|'zippy'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_keypair
dedent|''
name|'def'
name|'setup_keypair'
op|'('
name|'self'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key_name'
op|'='
string|"'%s%s'"
op|'%'
op|'('
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
name|'private_key'
op|','
name|'fingerprint'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'generate_key_pair'
op|'('
name|'user_id'
op|','
name|'key_name'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
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
indent|'                    '
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'key_dir'
op|')'
newline|'\n'
dedent|''
name|'with'
name|'open'
op|'('
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
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                    '
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
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Duplicate'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'return'
name|'key_name'
newline|'\n'
nl|'\n'
comment|'# def setup_secgroups(self, username):'
nl|'\n'
comment|'#     conn = self.euca.connection_for(username)'
nl|'\n'
comment|'#     try:'
nl|'\n'
comment|'#         secgroup = conn.create_security_group("vpn-secgroup", "vpn-secgroup")'
nl|'\n'
comment|'#         secgroup.authorize(ip_protocol = "udp", from_port = "1194", to_port = "1194", cidr_ip = "0.0.0.0/0")'
nl|'\n'
comment|'#         secgroup.authorize(ip_protocol = "tcp", from_port = "80", to_port = "80", cidr_ip = "0.0.0.0/0")'
nl|'\n'
comment|'#         secgroup.authorize(ip_protocol = "tcp", from_port = "22", to_port = "22", cidr_ip = "0.0.0.0/0")'
nl|'\n'
comment|'#     except:'
nl|'\n'
comment|'#         pass'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
