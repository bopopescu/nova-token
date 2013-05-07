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
string|'"""Instance Metadata information."""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'posixpath'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'ec2utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'metadata'
name|'import'
name|'password'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'block_device'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'conductor'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'netutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|metadata_opts
name|'metadata_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'config_drive_skip_versions'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'('
string|"'1.0 2007-01-19 2007-03-01 2007-08-29 2007-10-10 '"
nl|'\n'
string|"'2007-12-15 2008-02-01 2008-09-01'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
op|'('
string|"'List of metadata versions to skip placing into the '"
nl|'\n'
string|"'config drive'"
op|')'
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'metadata_opts'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'dhcp_domain'"
op|','
string|"'nova.network.manager'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|VERSIONS
name|'VERSIONS'
op|'='
op|'['
nl|'\n'
string|"'1.0'"
op|','
nl|'\n'
string|"'2007-01-19'"
op|','
nl|'\n'
string|"'2007-03-01'"
op|','
nl|'\n'
string|"'2007-08-29'"
op|','
nl|'\n'
string|"'2007-10-10'"
op|','
nl|'\n'
string|"'2007-12-15'"
op|','
nl|'\n'
string|"'2008-02-01'"
op|','
nl|'\n'
string|"'2008-09-01'"
op|','
nl|'\n'
string|"'2009-04-04'"
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FOLSOM
name|'FOLSOM'
op|'='
string|"'2012-08-10'"
newline|'\n'
DECL|variable|GRIZZLY
name|'GRIZZLY'
op|'='
string|"'2013-04-04'"
newline|'\n'
DECL|variable|OPENSTACK_VERSIONS
name|'OPENSTACK_VERSIONS'
op|'='
op|'['
nl|'\n'
name|'FOLSOM'
op|','
nl|'\n'
name|'GRIZZLY'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONTENT_DIR
name|'CONTENT_DIR'
op|'='
string|'"content"'
newline|'\n'
DECL|variable|MD_JSON_NAME
name|'MD_JSON_NAME'
op|'='
string|'"meta_data.json"'
newline|'\n'
DECL|variable|UD_NAME
name|'UD_NAME'
op|'='
string|'"user_data"'
newline|'\n'
DECL|variable|PASS_NAME
name|'PASS_NAME'
op|'='
string|'"password"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidMetadataVersion
name|'class'
name|'InvalidMetadataVersion'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidMetadataPath
dedent|''
name|'class'
name|'InvalidMetadataPath'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceMetadata
dedent|''
name|'class'
name|'InstanceMetadata'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Instance metadata."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'address'
op|'='
name|'None'
op|','
name|'content'
op|'='
name|'None'
op|','
name|'extra_md'
op|'='
name|'None'
op|','
nl|'\n'
name|'conductor_api'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creation of this object should basically cover all time consuming\n        collection.  Methods after that should not cause time delays due to\n        network operations or lengthy cpu operations.\n\n        The user should then get a single instance and make multiple method\n        calls on it.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'content'
op|':'
newline|'\n'
indent|'            '
name|'content'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'instance'
op|'='
name|'instance'
newline|'\n'
name|'self'
op|'.'
name|'extra_md'
op|'='
name|'extra_md'
newline|'\n'
nl|'\n'
name|'if'
name|'conductor_api'
op|':'
newline|'\n'
indent|'            '
name|'capi'
op|'='
name|'conductor_api'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'capi'
op|'='
name|'conductor'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'availability_zone'
op|'='
name|'ec2utils'
op|'.'
name|'get_availability_zone_by_host'
op|'('
nl|'\n'
name|'instance'
op|'['
string|"'host'"
op|']'
op|','
name|'capi'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ip_info'
op|'='
name|'ec2utils'
op|'.'
name|'get_ip_info_for_instance'
op|'('
name|'ctxt'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'security_groups'
op|'='
name|'capi'
op|'.'
name|'security_group_get_by_instance'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mappings'
op|'='
name|'_format_instance_mapping'
op|'('
name|'capi'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'instance'
op|'.'
name|'get'
op|'('
string|"'user_data'"
op|','
name|'None'
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'userdata_raw'
op|'='
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'instance'
op|'['
string|"'user_data'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'userdata_raw'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'ec2_ids'
op|'='
name|'capi'
op|'.'
name|'get_ec2_ids'
op|'('
name|'ctxt'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'address'
op|'='
name|'address'
newline|'\n'
nl|'\n'
comment|'# expose instance metadata.'
nl|'\n'
name|'self'
op|'.'
name|'launch_metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'instance'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|','
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'launch_metadata'
op|'['
name|'item'
op|'['
string|"'key'"
op|']'
op|']'
op|'='
name|'item'
op|'['
string|"'value'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'password'
op|'='
name|'password'
op|'.'
name|'extract_password'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'uuid'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'content'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'files'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|'# get network info, and the rendered network template'
nl|'\n'
name|'network_info'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'get_instance_nw_info'
op|'('
name|'ctxt'
op|','
name|'instance'
op|','
nl|'\n'
name|'conductor_api'
op|'='
name|'capi'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'network_config'
op|'='
name|'None'
newline|'\n'
name|'cfg'
op|'='
name|'netutils'
op|'.'
name|'get_injected_network_template'
op|'('
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'cfg'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|'='
string|'"%04i"'
op|'%'
name|'len'
op|'('
name|'self'
op|'.'
name|'content'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'content'
op|'['
name|'key'
op|']'
op|'='
name|'cfg'
newline|'\n'
name|'self'
op|'.'
name|'network_config'
op|'='
op|'{'
string|'"name"'
op|':'
string|'"network_config"'
op|','
nl|'\n'
string|"'content_path'"
op|':'
string|'"/%s/%s"'
op|'%'
op|'('
name|'CONTENT_DIR'
op|','
name|'key'
op|')'
op|'}'
newline|'\n'
nl|'\n'
comment|"# 'content' is passed in from the configdrive code in"
nl|'\n'
comment|'# nova/virt/libvirt/driver.py.  Thats how we get the injected files'
nl|'\n'
comment|"# (personalities) in. AFAIK they're not stored in the db at all,"
nl|'\n'
comment|'# so are not available later (web service metadata time).'
nl|'\n'
dedent|''
name|'for'
op|'('
name|'path'
op|','
name|'contents'
op|')'
name|'in'
name|'content'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|'='
string|'"%04i"'
op|'%'
name|'len'
op|'('
name|'self'
op|'.'
name|'content'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'files'
op|'.'
name|'append'
op|'('
op|'{'
string|"'path'"
op|':'
name|'path'
op|','
nl|'\n'
string|"'content_path'"
op|':'
string|'"/%s/%s"'
op|'%'
op|'('
name|'CONTENT_DIR'
op|','
name|'key'
op|')'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'content'
op|'['
name|'key'
op|']'
op|'='
name|'contents'
newline|'\n'
nl|'\n'
DECL|member|get_ec2_metadata
dedent|''
dedent|''
name|'def'
name|'get_ec2_metadata'
op|'('
name|'self'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'version'
op|'=='
string|'"latest"'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
name|'VERSIONS'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'version'
name|'not'
name|'in'
name|'VERSIONS'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidMetadataVersion'
op|'('
name|'version'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'hostname'
op|'='
name|'self'
op|'.'
name|'_get_hostname'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'floating_ips'
op|'='
name|'self'
op|'.'
name|'ip_info'
op|'['
string|"'floating_ips'"
op|']'
newline|'\n'
name|'floating_ip'
op|'='
name|'floating_ips'
name|'and'
name|'floating_ips'
op|'['
number|'0'
op|']'
name|'or'
string|"''"
newline|'\n'
nl|'\n'
name|'fmt_sgroups'
op|'='
op|'['
name|'x'
op|'['
string|"'name'"
op|']'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'security_groups'
op|']'
newline|'\n'
nl|'\n'
name|'meta_data'
op|'='
op|'{'
nl|'\n'
string|"'ami-id'"
op|':'
name|'self'
op|'.'
name|'ec2_ids'
op|'['
string|"'ami-id'"
op|']'
op|','
nl|'\n'
string|"'ami-launch-index'"
op|':'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'launch_index'"
op|']'
op|','
nl|'\n'
string|"'ami-manifest-path'"
op|':'
string|"'FIXME'"
op|','
nl|'\n'
string|"'instance-id'"
op|':'
name|'self'
op|'.'
name|'ec2_ids'
op|'['
string|"'instance-id'"
op|']'
op|','
nl|'\n'
string|"'hostname'"
op|':'
name|'hostname'
op|','
nl|'\n'
string|"'local-ipv4'"
op|':'
name|'self'
op|'.'
name|'address'
op|','
nl|'\n'
string|"'reservation-id'"
op|':'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'reservation_id'"
op|']'
op|','
nl|'\n'
string|"'security-groups'"
op|':'
name|'fmt_sgroups'
op|'}'
newline|'\n'
nl|'\n'
comment|'# public keys are strangely rendered in ec2 metadata service'
nl|'\n'
comment|"#  meta-data/public-keys/ returns '0=keyname' (with no trailing /)"
nl|'\n'
comment|'# and only if there is a public key given.'
nl|'\n'
comment|"# '0=keyname' means there is a normally rendered dict at"
nl|'\n'
comment|'#  meta-data/public-keys/0'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# meta-data/public-keys/ : '0=%s' % keyname"
nl|'\n'
comment|"# meta-data/public-keys/0/ : 'openssh-key'"
nl|'\n'
comment|"# meta-data/public-keys/0/openssh-key : '%s' % publickey"
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'key_name'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'meta_data'
op|'['
string|"'public-keys'"
op|']'
op|'='
op|'{'
nl|'\n'
string|"'0'"
op|':'
op|'{'
string|"'_name'"
op|':'
string|'"0="'
op|'+'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'key_name'"
op|']'
op|','
nl|'\n'
string|"'openssh-key'"
op|':'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'key_data'"
op|']'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_check_version'
op|'('
string|"'2007-01-19'"
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'meta_data'
op|'['
string|"'local-hostname'"
op|']'
op|'='
name|'hostname'
newline|'\n'
name|'meta_data'
op|'['
string|"'public-hostname'"
op|']'
op|'='
name|'hostname'
newline|'\n'
name|'meta_data'
op|'['
string|"'public-ipv4'"
op|']'
op|'='
name|'floating_ip'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'False'
name|'and'
name|'self'
op|'.'
name|'_check_version'
op|'('
string|"'2007-03-01'"
op|','
name|'version'
op|')'
op|':'
newline|'\n'
comment|'# TODO(vish): store product codes'
nl|'\n'
indent|'            '
name|'meta_data'
op|'['
string|"'product-codes'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_check_version'
op|'('
string|"'2007-08-29'"
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance_type'
op|'='
name|'flavors'
op|'.'
name|'extract_instance_type'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'meta_data'
op|'['
string|"'instance-type'"
op|']'
op|'='
name|'instance_type'
op|'['
string|"'name'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'False'
name|'and'
name|'self'
op|'.'
name|'_check_version'
op|'('
string|"'2007-10-10'"
op|','
name|'version'
op|')'
op|':'
newline|'\n'
comment|'# TODO(vish): store ancestor ids'
nl|'\n'
indent|'            '
name|'meta_data'
op|'['
string|"'ancestor-ami-ids'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_check_version'
op|'('
string|"'2007-12-15'"
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'meta_data'
op|'['
string|"'block-device-mapping'"
op|']'
op|'='
name|'self'
op|'.'
name|'mappings'
newline|'\n'
name|'if'
string|"'kernel-id'"
name|'in'
name|'self'
op|'.'
name|'ec2_ids'
op|':'
newline|'\n'
indent|'                '
name|'meta_data'
op|'['
string|"'kernel-id'"
op|']'
op|'='
name|'self'
op|'.'
name|'ec2_ids'
op|'['
string|"'kernel-id'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'ramdisk-id'"
name|'in'
name|'self'
op|'.'
name|'ec2_ids'
op|':'
newline|'\n'
indent|'                '
name|'meta_data'
op|'['
string|"'ramdisk-id'"
op|']'
op|'='
name|'self'
op|'.'
name|'ec2_ids'
op|'['
string|"'ramdisk-id'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'self'
op|'.'
name|'_check_version'
op|'('
string|"'2008-02-01'"
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'meta_data'
op|'['
string|"'placement'"
op|']'
op|'='
op|'{'
string|"'availability-zone'"
op|':'
nl|'\n'
name|'self'
op|'.'
name|'availability_zone'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_check_version'
op|'('
string|"'2008-09-01'"
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'meta_data'
op|'['
string|"'instance-action'"
op|']'
op|'='
string|"'none'"
newline|'\n'
nl|'\n'
dedent|''
name|'data'
op|'='
op|'{'
string|"'meta-data'"
op|':'
name|'meta_data'
op|'}'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'userdata_raw'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'['
string|"'user-data'"
op|']'
op|'='
name|'self'
op|'.'
name|'userdata_raw'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'data'
newline|'\n'
nl|'\n'
DECL|member|get_ec2_item
dedent|''
name|'def'
name|'get_ec2_item'
op|'('
name|'self'
op|','
name|'path_tokens'
op|')'
op|':'
newline|'\n'
comment|'# get_ec2_metadata returns dict without top level version'
nl|'\n'
indent|'        '
name|'data'
op|'='
name|'self'
op|'.'
name|'get_ec2_metadata'
op|'('
name|'path_tokens'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'return'
name|'find_path_in_tree'
op|'('
name|'data'
op|','
name|'path_tokens'
op|'['
number|'1'
op|':'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_openstack_item
dedent|''
name|'def'
name|'get_openstack_item'
op|'('
name|'self'
op|','
name|'path_tokens'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'path_tokens'
op|'['
number|'0'
op|']'
op|'=='
name|'CONTENT_DIR'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'len'
op|'('
name|'path_tokens'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'KeyError'
op|'('
string|'"no listing for %s"'
op|'%'
string|'"/"'
op|'.'
name|'join'
op|'('
name|'path_tokens'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'path_tokens'
op|')'
op|'!='
number|'2'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'KeyError'
op|'('
string|'"Too many tokens for /%s"'
op|'%'
name|'CONTENT_DIR'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'content'
op|'['
name|'path_tokens'
op|'['
number|'1'
op|']'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'version'
op|'='
name|'path_tokens'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'version'
op|'=='
string|'"latest"'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
name|'OPENSTACK_VERSIONS'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'version'
name|'not'
name|'in'
name|'OPENSTACK_VERSIONS'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidMetadataVersion'
op|'('
name|'version'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'path'
op|'='
string|"'/'"
op|'.'
name|'join'
op|'('
name|'path_tokens'
op|'['
number|'1'
op|':'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'path_tokens'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
comment|'# request for /version, give a list of what is available'
nl|'\n'
indent|'            '
name|'ret'
op|'='
op|'['
name|'MD_JSON_NAME'
op|']'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'userdata_raw'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'ret'
op|'.'
name|'append'
op|'('
name|'UD_NAME'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_check_os_version'
op|'('
name|'GRIZZLY'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'ret'
op|'.'
name|'append'
op|'('
name|'PASS_NAME'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'path'
op|'=='
name|'UD_NAME'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'userdata_raw'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'KeyError'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'userdata_raw'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'path'
op|'=='
name|'PASS_NAME'
name|'and'
name|'self'
op|'.'
name|'_check_os_version'
op|'('
name|'GRIZZLY'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'password'
op|'.'
name|'handle_password'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'path'
op|'!='
name|'MD_JSON_NAME'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'KeyError'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
comment|'# right now, the only valid path is metadata.json'
nl|'\n'
dedent|''
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'metadata'
op|'['
string|"'uuid'"
op|']'
op|'='
name|'self'
op|'.'
name|'uuid'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'launch_metadata'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'['
string|"'meta'"
op|']'
op|'='
name|'self'
op|'.'
name|'launch_metadata'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'['
string|"'files'"
op|']'
op|'='
name|'self'
op|'.'
name|'files'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'extra_md'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'extra_md'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'launch_metadata'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'['
string|"'meta'"
op|']'
op|'='
name|'self'
op|'.'
name|'launch_metadata'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'network_config'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'['
string|"'network_config'"
op|']'
op|'='
name|'self'
op|'.'
name|'network_config'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'key_name'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'['
string|"'public_keys'"
op|']'
op|'='
op|'{'
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'key_name'"
op|']'
op|':'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'key_data'"
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'metadata'
op|'['
string|"'hostname'"
op|']'
op|'='
name|'self'
op|'.'
name|'_get_hostname'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'metadata'
op|'['
string|"'name'"
op|']'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|"'display_name'"
op|']'
newline|'\n'
name|'metadata'
op|'['
string|"'launch_index'"
op|']'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|"'launch_index'"
op|']'
newline|'\n'
name|'metadata'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'self'
op|'.'
name|'availability_zone'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_check_os_version'
op|'('
name|'GRIZZLY'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'['
string|"'random_seed'"
op|']'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'os'
op|'.'
name|'urandom'
op|'('
number|'512'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'data'
op|'='
op|'{'
nl|'\n'
name|'MD_JSON_NAME'
op|':'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'metadata'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'return'
name|'data'
op|'['
name|'path'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_check_version
dedent|''
name|'def'
name|'_check_version'
op|'('
name|'self'
op|','
name|'required'
op|','
name|'requested'
op|','
name|'versions'
op|'='
name|'VERSIONS'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'versions'
op|'.'
name|'index'
op|'('
name|'requested'
op|')'
op|'>='
name|'versions'
op|'.'
name|'index'
op|'('
name|'required'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_os_version
dedent|''
name|'def'
name|'_check_os_version'
op|'('
name|'self'
op|','
name|'required'
op|','
name|'requested'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_check_version'
op|'('
name|'required'
op|','
name|'requested'
op|','
name|'OPENSTACK_VERSIONS'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_hostname
dedent|''
name|'def'
name|'_get_hostname'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"%s%s%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'instance'
op|'['
string|"'hostname'"
op|']'
op|','
nl|'\n'
string|"'.'"
name|'if'
name|'CONF'
op|'.'
name|'dhcp_domain'
name|'else'
string|"''"
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'dhcp_domain'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookup
dedent|''
name|'def'
name|'lookup'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'path'
op|'=='
string|'""'
name|'or'
name|'path'
op|'['
number|'0'
op|']'
op|'!='
string|'"/"'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'posixpath'
op|'.'
name|'normpath'
op|'('
string|'"/"'
op|'+'
name|'path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'posixpath'
op|'.'
name|'normpath'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
comment|'# fix up requests, prepending /ec2 to anything that does not match'
nl|'\n'
dedent|''
name|'path_tokens'
op|'='
name|'path'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
name|'if'
name|'path_tokens'
op|'['
number|'0'
op|']'
name|'not'
name|'in'
op|'('
string|'"ec2"'
op|','
string|'"openstack"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'path_tokens'
op|'['
number|'0'
op|']'
op|'=='
string|'""'
op|':'
newline|'\n'
comment|'# request for /'
nl|'\n'
indent|'                '
name|'path_tokens'
op|'='
op|'['
string|'"ec2"'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'path_tokens'
op|'='
op|'['
string|'"ec2"'
op|']'
op|'+'
name|'path_tokens'
newline|'\n'
dedent|''
name|'path'
op|'='
string|'"/"'
op|'+'
string|'"/"'
op|'.'
name|'join'
op|'('
name|'path_tokens'
op|')'
newline|'\n'
nl|'\n'
comment|"# all values of 'path' input starts with '/' and have no trailing /"
nl|'\n'
nl|'\n'
comment|'# specifically handle the top level request'
nl|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'path_tokens'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'path_tokens'
op|'['
number|'0'
op|']'
op|'=='
string|'"openstack"'
op|':'
newline|'\n'
comment|"# NOTE(vish): don't show versions that are in the future"
nl|'\n'
indent|'                '
name|'today'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'strftime'
op|'('
string|'"%Y-%m-%d"'
op|')'
newline|'\n'
name|'versions'
op|'='
op|'['
name|'v'
name|'for'
name|'v'
name|'in'
name|'OPENSTACK_VERSIONS'
name|'if'
name|'v'
op|'<='
name|'today'
op|']'
newline|'\n'
name|'versions'
op|'+='
op|'['
string|'"latest"'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'versions'
op|'='
name|'VERSIONS'
op|'+'
op|'['
string|'"latest"'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'versions'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'path_tokens'
op|'['
number|'0'
op|']'
op|'=='
string|'"openstack"'
op|':'
newline|'\n'
indent|'                '
name|'data'
op|'='
name|'self'
op|'.'
name|'get_openstack_item'
op|'('
name|'path_tokens'
op|'['
number|'1'
op|':'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'data'
op|'='
name|'self'
op|'.'
name|'get_ec2_item'
op|'('
name|'path_tokens'
op|'['
number|'1'
op|':'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|'('
name|'InvalidMetadataVersion'
op|','
name|'KeyError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidMetadataPath'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'data'
newline|'\n'
nl|'\n'
DECL|member|metadata_for_config_drive
dedent|''
name|'def'
name|'metadata_for_config_drive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Yields (path, value) tuples for metadata elements."""'
newline|'\n'
comment|'# EC2 style metadata'
nl|'\n'
name|'for'
name|'version'
name|'in'
name|'VERSIONS'
op|'+'
op|'['
string|'"latest"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'version'
name|'in'
name|'CONF'
op|'.'
name|'config_drive_skip_versions'
op|'.'
name|'split'
op|'('
string|"' '"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'data'
op|'='
name|'self'
op|'.'
name|'get_ec2_metadata'
op|'('
name|'version'
op|')'
newline|'\n'
name|'if'
string|"'user-data'"
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                '
name|'filepath'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'ec2'"
op|','
name|'version'
op|','
string|"'user-data'"
op|')'
newline|'\n'
name|'yield'
op|'('
name|'filepath'
op|','
name|'data'
op|'['
string|"'user-data'"
op|']'
op|')'
newline|'\n'
name|'del'
name|'data'
op|'['
string|"'user-data'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'data'
op|'['
string|"'public-keys'"
op|']'
op|'['
string|"'0'"
op|']'
op|'['
string|"'_name'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'filepath'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'ec2'"
op|','
name|'version'
op|','
string|"'meta-data.json'"
op|')'
newline|'\n'
name|'yield'
op|'('
name|'filepath'
op|','
name|'json'
op|'.'
name|'dumps'
op|'('
name|'data'
op|'['
string|"'meta-data'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'version'
name|'in'
name|'OPENSTACK_VERSIONS'
op|'+'
op|'['
string|'"latest"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
string|"'openstack/%s/%s'"
op|'%'
op|'('
name|'version'
op|','
name|'MD_JSON_NAME'
op|')'
newline|'\n'
name|'yield'
op|'('
name|'path'
op|','
name|'self'
op|'.'
name|'lookup'
op|'('
name|'path'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'path'
op|'='
string|"'openstack/%s/%s'"
op|'%'
op|'('
name|'version'
op|','
name|'UD_NAME'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'userdata_raw'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'yield'
op|'('
name|'path'
op|','
name|'self'
op|'.'
name|'lookup'
op|'('
name|'path'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'for'
op|'('
name|'cid'
op|','
name|'content'
op|')'
name|'in'
name|'self'
op|'.'
name|'content'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
op|'('
string|"'%s/%s/%s'"
op|'%'
op|'('
string|'"openstack"'
op|','
name|'CONTENT_DIR'
op|','
name|'cid'
op|')'
op|','
name|'content'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_metadata_by_address
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_metadata_by_address'
op|'('
name|'conductor_api'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fixed_ip'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'get_fixed_ip_by_address'
op|'('
name|'ctxt'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'get_metadata_by_instance_id'
op|'('
name|'conductor_api'
op|','
nl|'\n'
name|'fixed_ip'
op|'['
string|"'instance_uuid'"
op|']'
op|','
nl|'\n'
name|'address'
op|','
nl|'\n'
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_metadata_by_instance_id
dedent|''
name|'def'
name|'get_metadata_by_instance_id'
op|'('
name|'conductor_api'
op|','
name|'instance_id'
op|','
name|'address'
op|','
nl|'\n'
name|'ctxt'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ctxt'
op|'='
name|'ctxt'
name|'or'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'='
name|'conductor_api'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'return'
name|'InstanceMetadata'
op|'('
name|'instance'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_format_instance_mapping
dedent|''
name|'def'
name|'_format_instance_mapping'
op|'('
name|'conductor_api'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'bdms'
op|'='
name|'conductor_api'
op|'.'
name|'block_device_mapping_get_all_by_instance'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'block_device'
op|'.'
name|'instance_block_mapping'
op|'('
name|'instance'
op|','
name|'bdms'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ec2_md_print
dedent|''
name|'def'
name|'ec2_md_print'
op|'('
name|'data'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'isinstance'
op|'('
name|'data'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'output'
op|'='
string|"''"
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'sorted'
op|'('
name|'data'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
op|'=='
string|"'_name'"
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'data'
op|'['
name|'key'
op|']'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
string|"'_name'"
name|'in'
name|'data'
op|'['
name|'key'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'output'
op|'+='
name|'str'
op|'('
name|'data'
op|'['
name|'key'
op|']'
op|'['
string|"'_name'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'output'
op|'+='
name|'key'
op|'+'
string|"'/'"
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'output'
op|'+='
name|'key'
newline|'\n'
nl|'\n'
dedent|''
name|'output'
op|'+='
string|"'\\n'"
newline|'\n'
dedent|''
name|'return'
name|'output'
op|'['
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'data'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_path_in_tree
dedent|''
dedent|''
name|'def'
name|'find_path_in_tree'
op|'('
name|'data'
op|','
name|'path_tokens'
op|')'
op|':'
newline|'\n'
comment|'# given a dict/list tree, and a path in that tree, return data found there.'
nl|'\n'
indent|'    '
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'path_tokens'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'data'
op|','
name|'dict'
op|')'
name|'or'
name|'isinstance'
op|'('
name|'data'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'path_tokens'
op|'['
name|'i'
op|']'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                '
name|'data'
op|'='
name|'data'
op|'['
name|'path_tokens'
op|'['
name|'i'
op|']'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'KeyError'
op|'('
string|'"/"'
op|'.'
name|'join'
op|'('
name|'path_tokens'
op|'['
number|'0'
op|':'
name|'i'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'i'
op|'!='
name|'len'
op|'('
name|'path_tokens'
op|')'
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'KeyError'
op|'('
string|'"/"'
op|'.'
name|'join'
op|'('
name|'path_tokens'
op|'['
number|'0'
op|':'
name|'i'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'data'
op|'='
name|'data'
op|'['
name|'path_tokens'
op|'['
name|'i'
op|']'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'data'
newline|'\n'
dedent|''
endmarker|''
end_unit
