begin_unit
comment|'# Copyright (c) 2012 OpenStack, LLC.'
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
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|class|ComputeFilter
name|'class'
name|'ComputeFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Filter on active Compute nodes that satisfy the instance properties"""'
newline|'\n'
nl|'\n'
DECL|member|_instance_supported
name|'def'
name|'_instance_supported'
op|'('
name|'self'
op|','
name|'capabilities'
op|','
name|'instance_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if the instance is supported by the hypervisor.\n\n        The instance may specify an architecture, hypervisor, and\n        vm_mode, e.g. (x86_64, kvm, hvm).\n        """'
newline|'\n'
name|'inst_arch'
op|'='
name|'instance_meta'
op|'.'
name|'get'
op|'('
string|"'image_architecture'"
op|','
name|'None'
op|')'
newline|'\n'
name|'inst_h_type'
op|'='
name|'instance_meta'
op|'.'
name|'get'
op|'('
string|"'image_hypervisor_type'"
op|','
name|'None'
op|')'
newline|'\n'
name|'inst_vm_mode'
op|'='
name|'instance_meta'
op|'.'
name|'get'
op|'('
string|"'image_vm_mode'"
op|','
name|'None'
op|')'
newline|'\n'
name|'inst_props_req'
op|'='
op|'('
name|'inst_arch'
op|','
name|'inst_h_type'
op|','
name|'inst_vm_mode'
op|')'
newline|'\n'
nl|'\n'
comment|'# Supported if no compute-related instance properties are specified'
nl|'\n'
name|'if'
name|'not'
name|'any'
op|'('
name|'inst_props_req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'supp_instances'
op|'='
name|'capabilities'
op|'.'
name|'get'
op|'('
string|"'supported_instances'"
op|','
name|'None'
op|')'
newline|'\n'
comment|'# Not supported if an instance property is requested but nothing'
nl|'\n'
comment|'# advertised by the host.'
nl|'\n'
name|'if'
name|'not'
name|'supp_instances'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Instance contains properties %(instance_meta)s, "'
nl|'\n'
string|'"but no corresponding capabilities are advertised "'
nl|'\n'
string|'"by the compute node"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|function|_compare_props
dedent|''
name|'def'
name|'_compare_props'
op|'('
name|'props'
op|','
name|'other_props'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'i'
name|'in'
name|'props'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'i'
name|'and'
name|'i'
name|'not'
name|'in'
name|'other_props'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'supp_inst'
name|'in'
name|'supp_instances'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'_compare_props'
op|'('
name|'inst_props_req'
op|','
name|'supp_inst'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Instance properties %(instance_meta)s "'
nl|'\n'
string|'"are satisfied by compute host capabilities "'
nl|'\n'
string|'"%(capabilities)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Instance contains properties %(instance_meta)s "'
nl|'\n'
string|'"that are not provided by the compute node "'
nl|'\n'
string|'"capabilities %(capabilities)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|host_passes
dedent|''
name|'def'
name|'host_passes'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if host passes instance compute properties.\n\n        Returns True for active compute nodes that satisfy\n        the compute properties specified in the instance.\n        """'
newline|'\n'
name|'spec'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'request_spec'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'instance_props'
op|'='
name|'spec'
op|'.'
name|'get'
op|'('
string|"'instance_properties'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'instance_meta'
op|'='
name|'instance_props'
op|'.'
name|'get'
op|'('
string|"'system_metadata'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'instance_type'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'instance_type'"
op|')'
newline|'\n'
name|'if'
name|'host_state'
op|'.'
name|'topic'
op|'!='
string|"'compute'"
name|'or'
name|'not'
name|'instance_type'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'capabilities'
op|'='
name|'host_state'
op|'.'
name|'capabilities'
newline|'\n'
name|'service'
op|'='
name|'host_state'
op|'.'
name|'service'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'utils'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
name|'or'
name|'service'
op|'['
string|"'disabled'"
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
string|'"%(host_state)s is disabled or has not been "'
nl|'\n'
string|'"heard from in a while"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'capabilities'
op|'.'
name|'get'
op|'('
string|'"enabled"'
op|','
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(host_state)s is disabled via capabilities"'
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'_instance_supported'
op|'('
name|'capabilities'
op|','
name|'instance_meta'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(host_state)s does not support requested "'
nl|'\n'
string|'"instance_properties"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
