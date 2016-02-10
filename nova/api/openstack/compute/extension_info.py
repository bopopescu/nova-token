begin_unit
comment|'# Copyright 2013 IBM Corp.'
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
name|'copy'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'six'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LE'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'extensions'"
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
name|'os_compute_authorizer'
op|'('
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(cyeoh): The following mappings are currently incomplete'
nl|'\n'
comment|'# Having a v2.1 extension loaded can imply that several v2 extensions'
nl|'\n'
comment|'# should also appear to be loaded (although they no longer do in v2.1)'
nl|'\n'
DECL|variable|v21_to_v2_extension_list_mapping
name|'v21_to_v2_extension_list_mapping'
op|'='
op|'{'
nl|'\n'
string|"'os-quota-sets'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'UserQuotas'"
op|','
string|"'alias'"
op|':'
string|"'os-user-quotas'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'ExtendedQuotas'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-extended-quotas'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'os-cells'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'CellCapacities'"
op|','
string|"'alias'"
op|':'
string|"'os-cell-capacities'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'os-baremetal-nodes'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'BareMetalExtStatus'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-baremetal-ext-status'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'os-block-device-mapping'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'BlockDeviceMappingV2Boot'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-block-device-mapping-v2-boot'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'os-cloudpipe'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'CloudpipeUpdate'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-cloudpipe-update'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'servers'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'Createserverext'"
op|','
string|"'alias'"
op|':'
string|"'os-create-server-ext'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'ExtendedIpsMac'"
op|','
string|"'alias'"
op|':'
string|"'OS-EXT-IPS-MAC'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'ExtendedIps'"
op|','
string|"'alias'"
op|':'
string|"'OS-EXT-IPS'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'ServerListMultiStatus'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-server-list-multi-status'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'ServerSortKeys'"
op|','
string|"'alias'"
op|':'
string|"'os-server-sort-keys'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'ServerStartStop'"
op|','
string|"'alias'"
op|':'
string|"'os-server-start-stop'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'flavors'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'FlavorDisabled'"
op|','
string|"'alias'"
op|':'
string|"'OS-FLV-DISABLED'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'FlavorExtraData'"
op|','
string|"'alias'"
op|':'
string|"'OS-FLV-EXT-DATA'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'FlavorSwap'"
op|','
string|"'alias'"
op|':'
string|"'os-flavor-swap'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'os-services'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'ExtendedServicesDelete'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-extended-services-delete'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'ExtendedServices'"
op|','
string|"'alias'"
op|':'
nl|'\n'
string|"'os-extended-services'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'os-evacuate'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'ExtendedEvacuateFindHost'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-extended-evacuate-find-host'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'os-floating-ips'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'ExtendedFloatingIps'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-extended-floating-ips'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'os-hypervisors'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'ExtendedHypervisors'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-extended-hypervisors'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'HypervisorStatus'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-hypervisor-status'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'os-networks'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'ExtendedNetworks'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-extended-networks'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'os-rescue'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'ExtendedRescueWithImage'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-extended-rescue-with-image'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'os-extended-status'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'ExtendedStatus'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'OS-EXT-STS'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'os-used-limits'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'UsedLimitsForAdmin'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-used-limits-for-admin'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'os-volumes'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'VolumeAttachmentUpdate'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-volume-attachment-update'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'os-server-groups'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'ServerGroupQuotas'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'os-server-group-quotas'"
op|'}'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|'# v2.1 plugins which should never appear in the v2 extension list'
nl|'\n'
comment|'# This should be the v2.1 alias, not the V2.0 alias'
nl|'\n'
DECL|variable|v2_extension_suppress_list
name|'v2_extension_suppress_list'
op|'='
op|'['
string|"'servers'"
op|','
string|"'images'"
op|','
string|"'versions'"
op|','
string|"'flavors'"
op|','
nl|'\n'
string|"'os-block-device-mapping-v1'"
op|','
string|"'os-consoles'"
op|','
nl|'\n'
string|"'extensions'"
op|','
string|"'image-metadata'"
op|','
string|"'ips'"
op|','
string|"'limits'"
op|','
nl|'\n'
string|"'server-metadata'"
op|','
string|"'server-migrations'"
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
comment|'# v2.1 plugins which should appear under a different name in v2'
nl|'\n'
DECL|variable|v21_to_v2_alias_mapping
name|'v21_to_v2_alias_mapping'
op|'='
op|'{'
nl|'\n'
string|"'image-size'"
op|':'
string|"'OS-EXT-IMG-SIZE'"
op|','
nl|'\n'
string|"'os-remote-consoles'"
op|':'
string|"'os-consoles'"
op|','
nl|'\n'
string|"'os-disk-config'"
op|':'
string|"'OS-DCF'"
op|','
nl|'\n'
string|"'os-extended-availability-zone'"
op|':'
string|"'OS-EXT-AZ'"
op|','
nl|'\n'
string|"'os-extended-server-attributes'"
op|':'
string|"'OS-EXT-SRV-ATTR'"
op|','
nl|'\n'
string|"'os-multinic'"
op|':'
string|"'NMN'"
op|','
nl|'\n'
string|"'os-scheduler-hints'"
op|':'
string|"'OS-SCH-HNT'"
op|','
nl|'\n'
string|"'os-server-usage'"
op|':'
string|"'OS-SRV-USG'"
op|','
nl|'\n'
string|"'os-instance-usage-audit-log'"
op|':'
string|"'os-instance_usage_audit_log'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|'# V2.1 does not support XML but we need to keep an entry in the'
nl|'\n'
comment|'# /extensions information returned to the user for backwards'
nl|'\n'
comment|'# compatibility'
nl|'\n'
DECL|variable|FAKE_XML_URL
name|'FAKE_XML_URL'
op|'='
string|'"http://docs.openstack.org/compute/ext/fake_xml"'
newline|'\n'
DECL|variable|FAKE_UPDATED_DATE
name|'FAKE_UPDATED_DATE'
op|'='
string|'"2014-12-03T00:00:00Z"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeExtension
name|'class'
name|'FakeExtension'
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
name|'name'
op|','
name|'alias'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'alias'
op|'='
name|'alias'
newline|'\n'
name|'self'
op|'.'
name|'__doc__'
op|'='
string|'""'
newline|'\n'
name|'self'
op|'.'
name|'version'
op|'='
op|'-'
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionInfoController
dedent|''
dedent|''
name|'class'
name|'ExtensionInfoController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
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
op|','
name|'extension_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'extension_info'
op|'='
name|'extension_info'
newline|'\n'
nl|'\n'
DECL|member|_translate
dedent|''
name|'def'
name|'_translate'
op|'('
name|'self'
op|','
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext_data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'ext_data'
op|'['
string|'"name"'
op|']'
op|'='
name|'ext'
op|'.'
name|'name'
newline|'\n'
name|'ext_data'
op|'['
string|'"alias"'
op|']'
op|'='
name|'ext'
op|'.'
name|'alias'
newline|'\n'
name|'ext_data'
op|'['
string|'"description"'
op|']'
op|'='
name|'ext'
op|'.'
name|'__doc__'
newline|'\n'
name|'ext_data'
op|'['
string|'"namespace"'
op|']'
op|'='
name|'FAKE_XML_URL'
newline|'\n'
name|'ext_data'
op|'['
string|'"updated"'
op|']'
op|'='
name|'FAKE_UPDATED_DATE'
newline|'\n'
name|'ext_data'
op|'['
string|'"links"'
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'return'
name|'ext_data'
newline|'\n'
nl|'\n'
DECL|member|_create_fake_ext
dedent|''
name|'def'
name|'_create_fake_ext'
op|'('
name|'self'
op|','
name|'alias'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FakeExtension'
op|'('
name|'alias'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_add_vif_extension
dedent|''
name|'def'
name|'_add_vif_extension'
op|'('
name|'self'
op|','
name|'discoverable_extensions'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vif_extension'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vif_extension_info'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'ExtendedVIFNet'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'OS-EXT-VIF-NET'"
op|'}'
newline|'\n'
name|'vif_extension'
op|'['
name|'vif_extension_info'
op|'['
string|'"alias"'
op|']'
op|']'
op|'='
name|'self'
op|'.'
name|'_create_fake_ext'
op|'('
nl|'\n'
name|'vif_extension_info'
op|'['
string|'"name"'
op|']'
op|','
name|'vif_extension_info'
op|'['
string|'"alias"'
op|']'
op|')'
newline|'\n'
name|'discoverable_extensions'
op|'.'
name|'update'
op|'('
name|'vif_extension'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_extensions
dedent|''
name|'def'
name|'_get_extensions'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Filter extensions list based on policy."""'
newline|'\n'
nl|'\n'
name|'discoverable_extensions'
op|'='
name|'dict'
op|'('
op|')'
newline|'\n'
name|'for'
name|'alias'
op|','
name|'ext'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'self'
op|'.'
name|'extension_info'
op|'.'
name|'get_extensions'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'os_compute_soft_authorizer'
op|'('
name|'alias'
op|')'
newline|'\n'
name|'if'
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'discoverable'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'discoverable_extensions'
op|'['
name|'alias'
op|']'
op|'='
name|'ext'
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
string|'"Filter out extension %s from discover list"'
op|','
nl|'\n'
name|'alias'
op|')'
newline|'\n'
nl|'\n'
comment|'# Add fake v2 extensions to list'
nl|'\n'
dedent|''
dedent|''
name|'extra_exts'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'alias'
name|'in'
name|'discoverable_extensions'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'alias'
name|'in'
name|'v21_to_v2_extension_list_mapping'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'extra_ext'
name|'in'
name|'v21_to_v2_extension_list_mapping'
op|'['
name|'alias'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'extra_exts'
op|'['
name|'extra_ext'
op|'['
string|'"alias"'
op|']'
op|']'
op|'='
name|'self'
op|'.'
name|'_create_fake_ext'
op|'('
nl|'\n'
name|'extra_ext'
op|'['
string|'"name"'
op|']'
op|','
name|'extra_ext'
op|'['
string|'"alias"'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'discoverable_extensions'
op|'.'
name|'update'
op|'('
name|'extra_exts'
op|')'
newline|'\n'
nl|'\n'
comment|"# Suppress extensions which we don't want to see in v2"
nl|'\n'
name|'for'
name|'suppress_ext'
name|'in'
name|'v2_extension_suppress_list'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'discoverable_extensions'
op|'['
name|'suppress_ext'
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
comment|'# v2.1 to v2 extension name mapping'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'rename_ext'
name|'in'
name|'v21_to_v2_alias_mapping'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'rename_ext'
name|'in'
name|'discoverable_extensions'
op|':'
newline|'\n'
indent|'                '
name|'new_name'
op|'='
name|'v21_to_v2_alias_mapping'
op|'['
name|'rename_ext'
op|']'
newline|'\n'
name|'mod_ext'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
nl|'\n'
name|'discoverable_extensions'
op|'.'
name|'pop'
op|'('
name|'rename_ext'
op|')'
op|')'
newline|'\n'
name|'mod_ext'
op|'.'
name|'alias'
op|'='
name|'new_name'
newline|'\n'
name|'discoverable_extensions'
op|'['
name|'new_name'
op|']'
op|'='
name|'mod_ext'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'discoverable_extensions'
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
name|'discoverable_extensions'
op|'='
name|'self'
op|'.'
name|'_get_extensions'
op|'('
name|'context'
op|')'
newline|'\n'
comment|'# NOTE(gmann): This is for v2.1 compatible mode where'
nl|'\n'
comment|'# extension list should show all extensions as shown by v2.'
nl|'\n'
comment|'# Here we add VIF extension which has been removed from v2.1 list.'
nl|'\n'
name|'if'
name|'req'
op|'.'
name|'is_legacy_v2'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_add_vif_extension'
op|'('
name|'discoverable_extensions'
op|')'
newline|'\n'
dedent|''
name|'sorted_ext_list'
op|'='
name|'sorted'
op|'('
nl|'\n'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'discoverable_extensions'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'extensions'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'_alias'
op|','
name|'ext'
name|'in'
name|'sorted_ext_list'
op|':'
newline|'\n'
indent|'            '
name|'extensions'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_translate'
op|'('
name|'ext'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'extensions'
op|'='
name|'extensions'
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
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|"# NOTE(dprince): the extensions alias is used as the 'id' for show"
nl|'\n'
indent|'            '
name|'ext'
op|'='
name|'self'
op|'.'
name|'_get_extensions'
op|'('
name|'context'
op|')'
op|'['
name|'id'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
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
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'extension'
op|'='
name|'self'
op|'.'
name|'_translate'
op|'('
name|'ext'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionInfo
dedent|''
dedent|''
name|'class'
name|'ExtensionInfo'
op|'('
name|'extensions'
op|'.'
name|'V21APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extension information."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Extensions"'
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
nl|'\n'
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
name|'ALIAS'
op|','
name|'ExtensionInfoController'
op|'('
name|'self'
op|'.'
name|'extension_info'
op|')'
op|','
nl|'\n'
name|'member_name'
op|'='
string|"'extension'"
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
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LoadedExtensionInfo
dedent|''
dedent|''
name|'class'
name|'LoadedExtensionInfo'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Keep track of all loaded API extensions."""'
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
name|'extensions'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|register_extension
dedent|''
name|'def'
name|'register_extension'
op|'('
name|'self'
op|','
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_check_extension'
op|'('
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'alias'
op|'='
name|'ext'
op|'.'
name|'alias'
newline|'\n'
nl|'\n'
name|'if'
name|'alias'
name|'in'
name|'self'
op|'.'
name|'extensions'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
string|'"Found duplicate extension: %s"'
nl|'\n'
op|'%'
name|'alias'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'extensions'
op|'['
name|'alias'
op|']'
op|'='
name|'ext'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_check_extension
dedent|''
name|'def'
name|'_check_extension'
op|'('
name|'self'
op|','
name|'extension'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Checks for required methods in extension objects."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'extension'
op|'.'
name|'is_valid'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"Exception loading extension"'
op|')'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|get_extensions
dedent|''
name|'def'
name|'get_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'extensions'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
