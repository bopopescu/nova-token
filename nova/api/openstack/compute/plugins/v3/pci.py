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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
DECL|class|Pci
dedent|''
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
string|'"PCIAccess"'
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
name|'return'
op|'['
op|']'
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
