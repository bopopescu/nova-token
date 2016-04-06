begin_unit
comment|'# Copyright 2016 OpenStack Foundation'
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
name|'itertools'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|vmware_group
name|'vmware_group'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
string|"'vmware'"
op|','
name|'title'
op|'='
string|"'VMWare Options'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|vmwareapi_vif_opts
name|'vmwareapi_vif_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vlan_interface'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'vmnic0'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Physical ethernet adapter name for vlan networking'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'integration_bridge'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'This option should be configured only when using the '"
nl|'\n'
string|"'NSX-MH Neutron plugin. This is the name of the '"
nl|'\n'
string|"'integration bridge on the ESXi. This should not be set '"
nl|'\n'
string|"'for any other Neutron plugin. Hence the default value '"
nl|'\n'
string|"'is not set.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|vmware_utils_opts
name|'vmware_utils_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'console_delay_seconds'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set this value if affected by an increased network '"
nl|'\n'
string|"'latency causing repeated characters when typing in '"
nl|'\n'
string|"'a remote console.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'serial_port_service_uri'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Identifies the remote system that serial port traffic '"
nl|'\n'
string|"'will be sent to. If this is not set, no serial ports '"
nl|'\n'
string|"'will be added to the created VMs.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'serial_port_proxy_uri'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Identifies a proxy service that provides network access '"
nl|'\n'
string|"'to the serial_port_service_uri. This option is ignored '"
nl|'\n'
string|"'if serial_port_service_uri is not specified.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|vmwareapi_opts
name|'vmwareapi_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'host_ip'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Hostname or IP address for connection to VMware '"
nl|'\n'
string|"'vCenter host.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'PortOpt'
op|'('
string|"'host_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'443'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Port for connection to VMware vCenter host.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'host_username'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Username for connection to VMware vCenter host.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'host_password'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Password for connection to VMware vCenter host.'"
op|','
nl|'\n'
DECL|variable|secret
name|'secret'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ca_file'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Specify a CA bundle file to use in verifying the '"
nl|'\n'
string|"'vCenter server certificate.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'insecure'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'If true, the vCenter server certificate is not '"
nl|'\n'
string|"'verified. If false, then the default CA truststore is '"
nl|'\n'
string|"'used for verification. This option is ignored if '"
nl|'\n'
string|'\'"ca_file" is set.\''
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cluster_name'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Name of a VMware Cluster ComputeResource.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'datastore_regex'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Regex to match the name of a datastore.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'task_poll_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0.5'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The interval used for polling of remote tasks.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'api_retry_count'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The number of times we retry on failures, e.g., '"
nl|'\n'
string|"'socket error, etc.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'PortOpt'
op|'('
string|"'vnc_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'5900'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'VNC starting port'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'vnc_port_total'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10000'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Total number of VNC ports'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_linked_clone'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Whether to use linked clone'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'wsdl_location'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Optional VIM Service WSDL Location '"
nl|'\n'
string|"'e.g http://<server>/vimService.wsdl. '"
nl|'\n'
string|"'Optional over-ride to default location for bug '"
nl|'\n'
string|"'work-arounds'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|spbm_opts
name|'spbm_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'pbm_enabled'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The PBM status.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'pbm_wsdl_location'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'PBM service WSDL file location URL. '"
nl|'\n'
string|"'e.g. file:///opt/SDK/spbm/wsdl/pbmService.wsdl '"
nl|'\n'
string|"'Not setting this will disable storage policy based '"
nl|'\n'
string|"'placement of instances.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'pbm_default_policy'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The PBM default policy. If pbm_wsdl_location is set and '"
nl|'\n'
string|"'there is no defined storage policy for the specific '"
nl|'\n'
string|"'request then this policy will be used.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|vimutil_opts
name|'vimutil_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'maximum_objects'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'100'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The maximum number of ObjectContent data '"
nl|'\n'
string|"'objects that should be returned in a single '"
nl|'\n'
string|"'result. A positive value will cause the '"
nl|'\n'
string|"'operation to suspend the retrieval when the '"
nl|'\n'
string|"'count of objects reaches the specified '"
nl|'\n'
string|"'maximum. The server may still limit the count '"
nl|'\n'
string|"'to something less than the configured value. '"
nl|'\n'
string|"'Any remaining objects may be retrieved with '"
nl|'\n'
string|"'additional requests.'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|vmops_opts
name|'vmops_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cache_prefix'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The prefix for where cached images are stored. This is '"
nl|'\n'
string|"'NOT the full path - just a folder prefix. '"
nl|'\n'
string|"'This should only be used when a datastore cache should '"
nl|'\n'
string|"'be shared between compute nodes. Note: this should only '"
nl|'\n'
string|"'be used when the compute nodes have a shared file '"
nl|'\n'
string|"'system.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|ALL_VMWARE_OPTS
name|'ALL_VMWARE_OPTS'
op|'='
name|'list'
op|'('
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
name|'vmwareapi_vif_opts'
op|','
nl|'\n'
name|'vmware_utils_opts'
op|','
nl|'\n'
name|'vmwareapi_opts'
op|','
nl|'\n'
name|'spbm_opts'
op|','
nl|'\n'
name|'vimutil_opts'
op|','
nl|'\n'
name|'vmops_opts'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_opts
name|'def'
name|'register_opts'
op|'('
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conf'
op|'.'
name|'register_group'
op|'('
name|'vmware_group'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'ALL_VMWARE_OPTS'
op|','
name|'group'
op|'='
name|'vmware_group'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
dedent|''
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
name|'vmware_group'
op|':'
name|'ALL_VMWARE_OPTS'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit
