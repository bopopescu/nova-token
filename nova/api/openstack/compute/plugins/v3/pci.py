begin_unit
comment|'# Copyright 2013 Intel Corporation'
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
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
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
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-pci'"
newline|'\n'
DECL|variable|instance_authorize
name|'instance_authorize'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
op|'('
nl|'\n'
string|"'compute'"
op|','
string|"'v3:'"
op|'+'
name|'ALIAS'
op|'+'
string|"':pci_servers'"
op|')'
newline|'\n'
nl|'\n'
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
DECL|variable|PCI_ADMIN_KEYS
name|'PCI_ADMIN_KEYS'
op|'='
op|'['
string|"'id'"
op|','
string|"'address'"
op|','
string|"'vendor_id'"
op|','
string|"'product_id'"
op|','
string|"'status'"
op|','
nl|'\n'
string|"'compute_node_id'"
op|']'
newline|'\n'
DECL|variable|PCI_DETAIL_KEYS
name|'PCI_DETAIL_KEYS'
op|'='
op|'['
string|"'dev_type'"
op|','
string|"'label'"
op|','
string|"'instance_uuid'"
op|','
string|"'dev_id'"
op|','
nl|'\n'
string|"'extra_info'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciServerController
name|'class'
name|'PciServerController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|_extend_server
indent|'    '
name|'def'
name|'_extend_server'
op|'('
name|'self'
op|','
name|'server'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_id'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'dev'
name|'in'
name|'instance'
op|'.'
name|'pci_devices'
op|':'
newline|'\n'
indent|'            '
name|'dev_id'
op|'.'
name|'append'
op|'('
op|'{'
string|"'id'"
op|':'
name|'dev'
op|'['
string|"'id'"
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'server'
op|'['
string|"'%s:pci_devices'"
op|'%'
name|'Pci'
op|'.'
name|'alias'
op|']'
op|'='
name|'dev_id'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'if'
name|'instance_authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'instance'
op|'='
name|'req'
op|'.'
name|'get_db_instance'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'server'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'if'
name|'instance_authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'servers'
op|'='
name|'list'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'='
name|'req'
op|'.'
name|'get_db_instance'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'server'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciHypervisorController
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'PciHypervisorController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|_extend_hypervisor
indent|'    '
name|'def'
name|'_extend_hypervisor'
op|'('
name|'self'
op|','
name|'hypervisor'
op|','
name|'compute_node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hypervisor'
op|'['
string|"'%s:pci_stats'"
op|'%'
name|'Pci'
op|'.'
name|'alias'
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
nl|'\n'
name|'compute_node'
op|'['
string|"'pci_stats'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hypervisor'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'hypervisor'"
op|']'
newline|'\n'
name|'compute_node'
op|'='
name|'req'
op|'.'
name|'get_db_compute_node'
op|'('
name|'hypervisor'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_extend_hypervisor'
op|'('
name|'hypervisor'
op|','
name|'compute_node'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hypervisors'
op|'='
name|'list'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'hypervisors'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'hypervisor'
name|'in'
name|'hypervisors'
op|':'
newline|'\n'
indent|'            '
name|'compute_node'
op|'='
name|'req'
op|'.'
name|'get_db_compute_node'
op|'('
name|'hypervisor'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_extend_hypervisor'
op|'('
name|'hypervisor'
op|','
name|'compute_node'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciController
dedent|''
dedent|''
dedent|''
name|'class'
name|'PciController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'host_api'
op|'='
name|'compute'
op|'.'
name|'HostAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_view_pcidevice
dedent|''
name|'def'
name|'_view_pcidevice'
op|'('
name|'self'
op|','
name|'device'
op|','
name|'detail'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'PCI_ADMIN_KEYS'
op|':'
newline|'\n'
indent|'            '
name|'dev_dict'
op|'['
name|'key'
op|']'
op|'='
name|'device'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'detail'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'field'
name|'in'
name|'PCI_DETAIL_KEYS'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'field'
op|'=='
string|"'instance_uuid'"
op|':'
newline|'\n'
indent|'                    '
name|'dev_dict'
op|'['
string|"'server_uuid'"
op|']'
op|'='
name|'device'
op|'['
name|'field'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'dev_dict'
op|'['
name|'field'
op|']'
op|'='
name|'device'
op|'['
name|'field'
op|']'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'dev_dict'
newline|'\n'
nl|'\n'
DECL|member|_get_all_nodes_pci_devices
dedent|''
name|'def'
name|'_get_all_nodes_pci_devices'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'detail'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
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
op|','
name|'action'
op|'='
name|'action'
op|')'
newline|'\n'
name|'compute_nodes'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'compute_node_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'results'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'node'
name|'in'
name|'compute_nodes'
op|':'
newline|'\n'
indent|'            '
name|'pci_devs'
op|'='
name|'objects'
op|'.'
name|'PciDeviceList'
op|'.'
name|'get_by_compute_node'
op|'('
nl|'\n'
name|'context'
op|','
name|'node'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'results'
op|'.'
name|'extend'
op|'('
op|'['
name|'self'
op|'.'
name|'_view_pcidevice'
op|'('
name|'dev'
op|','
name|'detail'
op|')'
nl|'\n'
name|'for'
name|'dev'
name|'in'
name|'pci_devs'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'results'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'results'
op|'='
name|'self'
op|'.'
name|'_get_all_nodes_pci_devices'
op|'('
name|'req'
op|','
name|'True'
op|','
string|"'detail'"
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'pci_devices'
op|'='
name|'results'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
op|')'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
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
op|','
name|'action'
op|'='
string|"'show'"
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'pci_dev'
op|'='
name|'objects'
op|'.'
name|'PciDevice'
op|'.'
name|'get_by_dev_id'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'PciDeviceNotFoundById'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'result'
op|'='
name|'self'
op|'.'
name|'_view_pcidevice'
op|'('
name|'pci_dev'
op|','
name|'True'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'pci_device'
op|'='
name|'result'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
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
name|'results'
op|'='
name|'self'
op|'.'
name|'_get_all_nodes_pci_devices'
op|'('
name|'req'
op|','
name|'False'
op|','
string|"'index'"
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'pci_devices'
op|'='
name|'results'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Pci
dedent|''
dedent|''
name|'class'
name|'Pci'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Pci access support."""'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"PciAccess"'
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
name|'resources'
op|'='
op|'['
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
nl|'\n'
name|'PciController'
op|'('
op|')'
op|','
nl|'\n'
name|'collection_actions'
op|'='
op|'{'
string|"'detail'"
op|':'
string|"'GET'"
op|'}'
op|')'
op|']'
newline|'\n'
name|'return'
name|'resources'
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
name|'server_extension'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
nl|'\n'
name|'self'
op|','
string|"'servers'"
op|','
name|'PciServerController'
op|'('
op|')'
op|')'
newline|'\n'
name|'compute_extension'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
nl|'\n'
name|'self'
op|','
string|"'os-hypervisors'"
op|','
name|'PciHypervisorController'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
op|'['
name|'server_extension'
op|','
name|'compute_extension'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
