begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 University of Southern California'
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
name|'compute'
name|'import'
name|'power_state'
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
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'nodes'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
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
DECL|function|read_domains
name|'def'
name|'read_domains'
op|'('
name|'fname'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'open'
op|'('
name|'fname'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'json'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'f'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'domains'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'json'
op|')'
newline|'\n'
name|'return'
name|'domains'
newline|'\n'
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|write_domains
dedent|''
dedent|''
name|'def'
name|'write_domains'
op|'('
name|'fname'
op|','
name|'domains'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'json'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'domains'
op|')'
newline|'\n'
name|'f'
op|'='
name|'open'
op|'('
name|'fname'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'f'
op|'.'
name|'write'
op|'('
name|'json'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalDom
dedent|''
name|'class'
name|'BareMetalDom'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    BareMetalDom class handles fake domain for bare metal back ends.\n\n    This implements the singleton pattern.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|_instance
name|'_instance'
op|'='
name|'None'
newline|'\n'
DECL|variable|_is_init
name|'_is_init'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|__new__
name|'def'
name|'__new__'
op|'('
name|'cls'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Returns the BareMetalDom singleton.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'cls'
op|'.'
name|'_instance'
name|'or'
op|'('
string|"'new'"
name|'in'
name|'kwargs'
name|'and'
name|'kwargs'
op|'['
string|"'new'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_instance'
op|'='
name|'super'
op|'('
name|'BareMetalDom'
op|','
name|'cls'
op|')'
op|'.'
name|'__new__'
op|'('
name|'cls'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_instance'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
nl|'\n'
name|'fake_dom_file'
op|'='
string|'"/tftpboot/test_fake_dom_file"'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Only call __init__ the first time object is instantiated.\n\n        Sets and Opens domain file: /tftpboot/test_fake_dom_file. Even though\n        nova-compute service is rebooted, this file should retain the\n        existing domains.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_is_init'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_is_init'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'fake_dom_file'
op|'='
name|'fake_dom_file'
newline|'\n'
name|'self'
op|'.'
name|'domains'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'fake_dom_nums'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'baremetal_nodes'
op|'='
name|'nodes'
op|'.'
name|'get_baremetal_nodes'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_read_domain_from_file'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_read_domain_from_file
dedent|''
name|'def'
name|'_read_domain_from_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Reads the domains from a file.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'domains'
op|'='
name|'read_domains'
op|'('
name|'self'
op|'.'
name|'fake_dom_file'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'            '
name|'dom'
op|'='
op|'['
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"No domains exist."'
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'msg'
op|'='
name|'_'
op|'('
string|'"============= initial domains =========== : %s"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|'%'
op|'('
name|'self'
op|'.'
name|'domains'
op|')'
op|')'
newline|'\n'
name|'for'
name|'dom'
name|'in'
name|'self'
op|'.'
name|'domains'
op|'['
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'dom'
op|'['
string|"'status'"
op|']'
op|'=='
name|'power_state'
op|'.'
name|'BUILDING'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Building domain: to be removed"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'destroy_domain'
op|'('
name|'dom'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'elif'
name|'dom'
op|'['
string|"'status'"
op|']'
op|'!='
name|'power_state'
op|'.'
name|'RUNNING'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Not running domain: remove"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'domains'
op|'.'
name|'remove'
op|'('
name|'dom'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'res'
op|'='
name|'self'
op|'.'
name|'baremetal_nodes'
op|'.'
name|'set_status'
op|'('
name|'dom'
op|'['
string|"'node_id'"
op|']'
op|','
nl|'\n'
name|'dom'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'res'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fake_dom_nums'
op|'='
name|'self'
op|'.'
name|'fake_dom_nums'
op|'+'
number|'1'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"domain running on an unknown node: discarded"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'domains'
op|'.'
name|'remove'
op|'('
name|'dom'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'self'
op|'.'
name|'domains'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'store_domain'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|reboot_domain
dedent|''
name|'def'
name|'reboot_domain'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Finds domain and deactivates (power down) bare-metal node.\n\n        Activates the node again. In case of fail,\n        destroys the domain from domains list.\n        """'
newline|'\n'
name|'fd'
op|'='
name|'self'
op|'.'
name|'find_domain'
op|'('
name|'name'
op|')'
newline|'\n'
name|'if'
name|'fd'
op|'=='
op|'['
op|']'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"No such domain (%s)"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'msg'
op|'%'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'node_ip'
op|'='
name|'self'
op|'.'
name|'baremetal_nodes'
op|'.'
name|'get_ip_by_id'
op|'('
name|'fd'
op|'['
string|"'node_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'baremetal_nodes'
op|'.'
name|'deactivate_node'
op|'('
name|'fd'
op|'['
string|"'node_id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Failed power down Bare-metal node %s"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'msg'
op|'%'
name|'fd'
op|'['
string|"'node_id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'change_domain_state'
op|'('
name|'name'
op|','
name|'power_state'
op|'.'
name|'BUILDING'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'state'
op|'='
name|'self'
op|'.'
name|'baremetal_nodes'
op|'.'
name|'activate_node'
op|'('
name|'fd'
op|'['
string|"'node_id'"
op|']'
op|','
nl|'\n'
name|'node_ip'
op|','
name|'name'
op|','
name|'fd'
op|'['
string|"'mac_address'"
op|']'
op|','
name|'fd'
op|'['
string|"'ip_address'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'change_domain_state'
op|'('
name|'name'
op|','
name|'state'
op|')'
newline|'\n'
name|'return'
name|'state'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"deactivate -> activate fails"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'destroy_domain'
op|'('
name|'name'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|destroy_domain
dedent|''
dedent|''
name|'def'
name|'destroy_domain'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Removes domain from domains list and deactivates node.\n        """'
newline|'\n'
name|'fd'
op|'='
name|'self'
op|'.'
name|'find_domain'
op|'('
name|'name'
op|')'
newline|'\n'
name|'if'
name|'fd'
op|'=='
op|'['
op|']'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"destroy_domain: no such domain"'
op|')'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"No such domain %s"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'msg'
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'baremetal_nodes'
op|'.'
name|'deactivate_node'
op|'('
name|'fd'
op|'['
string|"'node_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'domains'
op|'.'
name|'remove'
op|'('
name|'fd'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Domains: %s"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|'%'
op|'('
name|'self'
op|'.'
name|'domains'
op|')'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Nodes: %s"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|'%'
op|'('
name|'self'
op|'.'
name|'baremetal_nodes'
op|'.'
name|'nodes'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'store_domain'
op|'('
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"After storing domains: %s"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|'%'
op|'('
name|'self'
op|'.'
name|'domains'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"deactivation/removing domain failed"'
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|create_domain
dedent|''
dedent|''
name|'def'
name|'create_domain'
op|'('
name|'self'
op|','
name|'xml_dict'
op|','
name|'bpath'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Adds a domain to domains list and activates an idle bare-metal node.\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"===== Domain is being created ====="'
op|')'
op|')'
newline|'\n'
name|'fd'
op|'='
name|'self'
op|'.'
name|'find_domain'
op|'('
name|'xml_dict'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'fd'
op|'!='
op|'['
op|']'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Same domain name already exists"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"create_domain: before get_idle_node"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'node_id'
op|'='
name|'self'
op|'.'
name|'baremetal_nodes'
op|'.'
name|'get_idle_node'
op|'('
op|')'
newline|'\n'
name|'node_ip'
op|'='
name|'self'
op|'.'
name|'baremetal_nodes'
op|'.'
name|'get_ip_by_id'
op|'('
name|'node_id'
op|')'
newline|'\n'
nl|'\n'
name|'new_dom'
op|'='
op|'{'
string|"'node_id'"
op|':'
name|'node_id'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'xml_dict'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'memory_kb'"
op|':'
name|'xml_dict'
op|'['
string|"'memory_kb'"
op|']'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'xml_dict'
op|'['
string|"'vcpus'"
op|']'
op|','
nl|'\n'
string|"'mac_address'"
op|':'
name|'xml_dict'
op|'['
string|"'mac_address'"
op|']'
op|','
nl|'\n'
string|"'user_data'"
op|':'
name|'xml_dict'
op|'['
string|"'user_data'"
op|']'
op|','
nl|'\n'
string|"'ip_address'"
op|':'
name|'xml_dict'
op|'['
string|"'ip_address'"
op|']'
op|','
nl|'\n'
string|"'image_id'"
op|':'
name|'xml_dict'
op|'['
string|"'image_id'"
op|']'
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
name|'xml_dict'
op|'['
string|"'kernel_id'"
op|']'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'xml_dict'
op|'['
string|"'ramdisk_id'"
op|']'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'power_state'
op|'.'
name|'BUILDING'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'domains'
op|'.'
name|'append'
op|'('
name|'new_dom'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Created new domain: %s"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|'%'
op|'('
name|'new_dom'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'change_domain_state'
op|'('
name|'new_dom'
op|'['
string|"'name'"
op|']'
op|','
name|'power_state'
op|'.'
name|'BUILDING'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'baremetal_nodes'
op|'.'
name|'set_image'
op|'('
name|'bpath'
op|','
name|'node_id'
op|')'
newline|'\n'
nl|'\n'
name|'state'
op|'='
name|'power_state'
op|'.'
name|'NOSTATE'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'state'
op|'='
name|'self'
op|'.'
name|'baremetal_nodes'
op|'.'
name|'activate_node'
op|'('
name|'node_id'
op|','
nl|'\n'
name|'node_ip'
op|','
name|'new_dom'
op|'['
string|"'name'"
op|']'
op|','
name|'new_dom'
op|'['
string|"'mac_address'"
op|']'
op|','
nl|'\n'
name|'new_dom'
op|'['
string|"'ip_address'"
op|']'
op|','
name|'new_dom'
op|'['
string|"'user_data'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'change_domain_state'
op|'('
name|'new_dom'
op|'['
string|"'name'"
op|']'
op|','
name|'state'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'domains'
op|'.'
name|'remove'
op|'('
name|'new_dom'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'baremetal_nodes'
op|'.'
name|'free_node'
op|'('
name|'node_id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Failed to boot Bare-metal node %s"'
op|')'
op|','
name|'node_id'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'state'
newline|'\n'
nl|'\n'
DECL|member|change_domain_state
dedent|''
name|'def'
name|'change_domain_state'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'state'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Changes domain state by the given state and updates domain file.\n        """'
newline|'\n'
name|'l'
op|'='
name|'self'
op|'.'
name|'find_domain'
op|'('
name|'name'
op|')'
newline|'\n'
name|'if'
name|'l'
op|'=='
op|'['
op|']'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"No such domain exists"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'i'
op|'='
name|'self'
op|'.'
name|'domains'
op|'.'
name|'index'
op|'('
name|'l'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'domains'
op|'['
name|'i'
op|']'
op|'['
string|"'status'"
op|']'
op|'='
name|'state'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"change_domain_state: to new state %s"'
op|')'
op|','
name|'str'
op|'('
name|'state'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'store_domain'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|store_domain
dedent|''
name|'def'
name|'store_domain'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Stores fake domains to the file.\n        """'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Stored fake domains to the file: %s"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|'%'
op|'('
name|'self'
op|'.'
name|'domains'
op|')'
op|')'
newline|'\n'
name|'write_domains'
op|'('
name|'self'
op|'.'
name|'fake_dom_file'
op|','
name|'self'
op|'.'
name|'domains'
op|')'
newline|'\n'
nl|'\n'
DECL|member|find_domain
dedent|''
name|'def'
name|'find_domain'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Finds domain by the given name and returns the domain.\n        """'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'self'
op|'.'
name|'domains'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'item'
op|'['
string|"'name'"
op|']'
op|'=='
name|'name'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'item'
newline|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"domain does not exist"'
op|')'
op|')'
newline|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|list_domains
dedent|''
name|'def'
name|'list_domains'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Returns the instance name from domains list.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'domains'
op|'=='
op|'['
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
name|'return'
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
name|'domains'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_domain_info
dedent|''
name|'def'
name|'get_domain_info'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Finds domain by the given instance_name and returns informaiton.\n\n        For example, status, memory_kb, vcpus, etc.\n        """'
newline|'\n'
name|'domain'
op|'='
name|'self'
op|'.'
name|'find_domain'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'domain'
op|'!='
op|'['
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'domain'
op|'['
string|"'status'"
op|']'
op|','
name|'domain'
op|'['
string|"'memory_kb'"
op|']'
op|','
nl|'\n'
name|'domain'
op|'['
string|"'memory_kb'"
op|']'
op|','
nl|'\n'
name|'domain'
op|'['
string|"'vcpus'"
op|']'
op|','
nl|'\n'
number|'100'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'power_state'
op|'.'
name|'NOSTATE'
op|','
string|"''"
op|','
string|"''"
op|','
string|"''"
op|','
string|"''"
op|']'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
