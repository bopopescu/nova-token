begin_unit
comment|'# Copyright (c) 2011-2012 OpenStack Foundation'
nl|'\n'
comment|'# Copyright (c) 2012 Canonical Ltd'
nl|'\n'
comment|'# Copyright (c) 2012 SUSE LINUX Products GmbH'
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
name|'from'
name|'distutils'
name|'import'
name|'versionpredicate'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'versionutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'arch'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'hv_type'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_mode'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
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
DECL|class|ImagePropertiesFilter
name|'class'
name|'ImagePropertiesFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Filter compute nodes that satisfy instance image properties.\n\n    The ImagePropertiesFilter filters compute nodes that satisfy\n    any architecture, hypervisor type, or virtual machine mode properties\n    specified on the instance\'s image properties.  Image properties are\n    contained in the image dictionary in the request_spec.\n    """'
newline|'\n'
nl|'\n'
comment|'# Image Properties and Compute Capabilities do not change within'
nl|'\n'
comment|'# a request'
nl|'\n'
DECL|variable|run_filter_once_per_request
name|'run_filter_once_per_request'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_instance_supported
name|'def'
name|'_instance_supported'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'image_props'
op|','
nl|'\n'
name|'hypervisor_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'img_arch'
op|'='
name|'image_props'
op|'.'
name|'get'
op|'('
string|"'hw_architecture'"
op|')'
newline|'\n'
name|'img_h_type'
op|'='
name|'image_props'
op|'.'
name|'get'
op|'('
string|"'img_hv_type'"
op|')'
newline|'\n'
name|'img_vm_mode'
op|'='
name|'image_props'
op|'.'
name|'get'
op|'('
string|"'hw_vm_mode'"
op|')'
newline|'\n'
name|'checked_img_props'
op|'='
op|'('
nl|'\n'
name|'arch'
op|'.'
name|'canonicalize'
op|'('
name|'img_arch'
op|')'
op|','
nl|'\n'
name|'hv_type'
op|'.'
name|'canonicalize'
op|'('
name|'img_h_type'
op|')'
op|','
nl|'\n'
name|'vm_mode'
op|'.'
name|'canonicalize'
op|'('
name|'img_vm_mode'
op|')'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
comment|'# Supported if no compute-related instance properties are specified'
nl|'\n'
name|'if'
name|'not'
name|'any'
op|'('
name|'checked_img_props'
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
name|'host_state'
op|'.'
name|'supported_instances'
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
string|'"Instance contains properties %(image_props)s, "'
nl|'\n'
string|'"but no corresponding supported_instances are "'
nl|'\n'
string|'"advertised by the compute node"'
op|','
nl|'\n'
op|'{'
string|"'image_props'"
op|':'
name|'image_props'
op|'}'
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
DECL|function|_compare_product_version
dedent|''
name|'def'
name|'_compare_product_version'
op|'('
name|'hyper_version'
op|','
name|'image_props'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'version_required'
op|'='
name|'image_props'
op|'.'
name|'get'
op|'('
string|"'img_hv_requested_version'"
op|')'
newline|'\n'
name|'if'
name|'not'
op|'('
name|'hypervisor_version'
name|'and'
name|'version_required'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'img_prop_predicate'
op|'='
name|'versionpredicate'
op|'.'
name|'VersionPredicate'
op|'('
nl|'\n'
string|"'image_prop (%s)'"
op|'%'
name|'version_required'
op|')'
newline|'\n'
name|'hyper_ver_str'
op|'='
name|'versionutils'
op|'.'
name|'convert_version_to_str'
op|'('
name|'hyper_version'
op|')'
newline|'\n'
name|'return'
name|'img_prop_predicate'
op|'.'
name|'satisfied_by'
op|'('
name|'hyper_ver_str'
op|')'
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
name|'checked_img_props'
op|','
name|'supp_inst'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'_compare_product_version'
op|'('
name|'hypervisor_version'
op|','
name|'image_props'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Instance contains properties %(image_props)s "'
nl|'\n'
string|'"that are not provided by the compute node "'
nl|'\n'
string|'"supported_instances %(supp_instances)s or "'
nl|'\n'
string|'"hypervisor version %(hypervisor_version)s do not match"'
op|','
nl|'\n'
op|'{'
string|"'image_props'"
op|':'
name|'image_props'
op|','
nl|'\n'
string|"'supp_instances'"
op|':'
name|'supp_instances'
op|','
nl|'\n'
string|"'hypervisor_version'"
op|':'
name|'hypervisor_version'
op|'}'
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
name|'spec_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if host passes specified image properties.\n\n        Returns True for compute nodes that satisfy image properties\n        contained in the request_spec.\n        """'
newline|'\n'
name|'image_props'
op|'='
name|'spec_obj'
op|'.'
name|'image'
op|'.'
name|'properties'
name|'if'
name|'spec_obj'
op|'.'
name|'image'
name|'else'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_instance_supported'
op|'('
name|'host_state'
op|','
name|'image_props'
op|','
nl|'\n'
name|'host_state'
op|'.'
name|'hypervisor_version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"%(host_state)s does not support requested "'
nl|'\n'
string|'"instance_properties"'
op|','
op|'{'
string|"'host_state'"
op|':'
name|'host_state'
op|'}'
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
