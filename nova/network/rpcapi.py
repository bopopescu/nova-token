begin_unit
comment|'# Copyright 2013, Red Hat, Inc.'
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
string|'"""\nClient side of the network RPC API.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'oslo_messaging'
name|'as'
name|'messaging'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'objects_base'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkAPI
name|'class'
name|'NetworkAPI'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Client side of the network rpc API.\n\n    API version history:\n\n        * 1.0 - Initial version.\n        * 1.1 - Adds migrate_instance_[start|finish]\n        * 1.2 - Make migrate_instance_[start|finish] a little more flexible\n        * 1.3 - Adds fanout cast update_dns for multi_host networks\n        * 1.4 - Add get_backdoor_port()\n        * 1.5 - Adds associate\n        * 1.6 - Adds instance_uuid to _{dis,}associate_floating_ip\n        * 1.7 - Adds method get_floating_ip_pools to replace get_floating_pools\n        * 1.8 - Adds macs to allocate_for_instance\n        * 1.9 - Adds rxtx_factor to [add|remove]_fixed_ip, removes\n                instance_uuid from allocate_for_instance and\n                instance_get_nw_info\n\n        ... Grizzly supports message version 1.9.  So, any changes to existing\n        methods in 1.x after that point should be done such that they can\n        handle the version_cap being set to 1.9.\n\n        * 1.10- Adds (optional) requested_networks to deallocate_for_instance\n\n        ... Havana supports message version 1.10.  So, any changes to existing\n        methods in 1.x after that point should be done such that they can\n        handle the version_cap being set to 1.10.\n\n        * NOTE: remove unused method get_vifs_by_instance()\n        * NOTE: remove unused method get_vif_by_mac_address()\n        * NOTE: remove unused method get_network()\n        * NOTE: remove unused method get_all_networks()\n        * 1.11 - Add instance to deallocate_for_instance().\n                 Remove instance_id, project_id, and host.\n        * 1.12 - Add instance to deallocate_fixed_ip()\n\n        ... Icehouse supports message version 1.12.  So, any changes to\n        existing methods in 1.x after that point should be done such that they\n        can handle the version_cap being set to 1.12.\n\n        * 1.13 - Convert allocate_for_instance()\n                 to use NetworkRequestList objects\n\n        ... Juno and Kilo supports message version 1.13.  So, any changes to\n        existing methods in 1.x after that point should be done such that they\n        can handle the version_cap being set to 1.13.\n\n        * NOTE: remove unused method get_floating_ips_by_fixed_address()\n        * NOTE: remove unused method get_instance_uuids_by_ip_filter()\n        * NOTE: remove unused method disassociate_network()\n        * NOTE: remove unused method get_fixed_ip()\n        * NOTE: remove unused method get_fixed_ip_by_address()\n        * NOTE: remove unused method get_floating_ip()\n        * NOTE: remove unused method get_floating_ip_pools()\n        * NOTE: remove unused method get_floating_ip_by_address()\n        * NOTE: remove unused method get_floating_ips_by_project()\n        * NOTE: remove unused method get_instance_id_by_floating_address()\n        * NOTE: remove unused method allocate_floating_ip()\n        * NOTE: remove unused method deallocate_floating_ip()\n        * NOTE: remove unused method associate_floating_ip()\n        * NOTE: remove unused method disassociate_floating_ip()\n        * NOTE: remove unused method associate()\n\n        * 1.14 - Add mac parameter to release_fixed_ip().\n        * 1.15 - Convert set_network_host() to use Network objects.\n\n        ... Liberty supports message version 1.15.  So, any changes to\n        existing methods in 1.x after that point should be done such that they\n        can handle the version_cap being set to 1.15.\n\n        * 1.16 - Transfer instance in addition to instance_id in\n                 setup_networks_on_host\n\n        ... Liberty supports message version 1.16.  So, any changes to\n        existing methods in 1.x after that point should be done such that they\n        can handle the version_cap being set to 1.16.\n    '''"
newline|'\n'
nl|'\n'
DECL|variable|VERSION_ALIASES
name|'VERSION_ALIASES'
op|'='
op|'{'
nl|'\n'
string|"'grizzly'"
op|':'
string|"'1.9'"
op|','
nl|'\n'
string|"'havana'"
op|':'
string|"'1.10'"
op|','
nl|'\n'
string|"'icehouse'"
op|':'
string|"'1.12'"
op|','
nl|'\n'
string|"'juno'"
op|':'
string|"'1.13'"
op|','
nl|'\n'
string|"'kilo'"
op|':'
string|"'1.13'"
op|','
nl|'\n'
string|"'liberty'"
op|':'
string|"'1.15'"
op|','
nl|'\n'
string|"'mitaka'"
op|':'
string|"'1.16'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'topic'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NetworkAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'topic'
op|'='
name|'topic'
name|'or'
name|'CONF'
op|'.'
name|'network_topic'
newline|'\n'
name|'target'
op|'='
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'topic'
op|'='
name|'topic'
op|','
name|'version'
op|'='
string|"'1.0'"
op|')'
newline|'\n'
name|'version_cap'
op|'='
name|'self'
op|'.'
name|'VERSION_ALIASES'
op|'.'
name|'get'
op|'('
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'network'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'network'
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'objects_base'
op|'.'
name|'NovaObjectSerializer'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'rpc'
op|'.'
name|'get_client'
op|'('
name|'target'
op|','
name|'version_cap'
op|','
name|'serializer'
op|')'
newline|'\n'
nl|'\n'
comment|"# TODO(russellb): Convert this to named arguments.  It's a pretty large"
nl|'\n'
comment|"# list, so unwinding it all is probably best done in its own patch so it's"
nl|'\n'
comment|'# easier to review.'
nl|'\n'
DECL|member|create_networks
dedent|''
name|'def'
name|'create_networks'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'client'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'create_networks'"
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_network
dedent|''
name|'def'
name|'delete_network'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'uuid'
op|','
name|'fixed_range'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'client'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'delete_network'"
op|','
nl|'\n'
name|'uuid'
op|'='
name|'uuid'
op|','
name|'fixed_range'
op|'='
name|'fixed_range'
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_for_instance
dedent|''
name|'def'
name|'allocate_for_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_id'
op|','
name|'project_id'
op|','
name|'host'
op|','
nl|'\n'
name|'rxtx_factor'
op|','
name|'vpn'
op|','
name|'requested_networks'
op|','
name|'macs'
op|'='
name|'None'
op|','
nl|'\n'
name|'dhcp_options'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'version'
op|'='
string|"'1.13'"
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
string|"'1.9'"
newline|'\n'
name|'if'
name|'requested_networks'
op|':'
newline|'\n'
indent|'                '
name|'requested_networks'
op|'='
name|'requested_networks'
op|'.'
name|'as_tuples'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'multi_host'
op|':'
newline|'\n'
indent|'            '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
op|','
name|'server'
op|'='
name|'host'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'allocate_for_instance'"
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|','
name|'project_id'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
name|'rxtx_factor'
op|'='
name|'rxtx_factor'
op|','
name|'vpn'
op|'='
name|'vpn'
op|','
nl|'\n'
name|'requested_networks'
op|'='
name|'requested_networks'
op|','
nl|'\n'
name|'macs'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'macs'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deallocate_for_instance
dedent|''
name|'def'
name|'deallocate_for_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'requested_networks'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
newline|'\n'
name|'kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
string|"'1.11'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
string|"'1.11'"
newline|'\n'
name|'kwargs'
op|'['
string|"'instance'"
op|']'
op|'='
name|'instance'
newline|'\n'
name|'kwargs'
op|'['
string|"'requested_networks'"
op|']'
op|'='
name|'requested_networks'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
string|"'1.10'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'version'
op|'='
string|"'1.10'"
newline|'\n'
name|'kwargs'
op|'['
string|"'requested_networks'"
op|']'
op|'='
name|'requested_networks'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'version'
op|'='
string|"'1.0'"
newline|'\n'
dedent|''
name|'kwargs'
op|'['
string|"'host'"
op|']'
op|'='
name|'instance'
op|'.'
name|'host'
newline|'\n'
name|'kwargs'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'instance'
op|'.'
name|'uuid'
newline|'\n'
name|'kwargs'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'instance'
op|'.'
name|'project_id'
newline|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'multi_host'
op|':'
newline|'\n'
indent|'            '
name|'cctxt'
op|'='
name|'cctxt'
op|'.'
name|'prepare'
op|'('
name|'server'
op|'='
name|'instance'
op|'.'
name|'host'
op|','
name|'version'
op|'='
name|'version'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'deallocate_for_instance'"
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_fixed_ip_to_instance
dedent|''
name|'def'
name|'add_fixed_ip_to_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_id'
op|','
name|'rxtx_factor'
op|','
nl|'\n'
name|'host'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
string|"'1.9'"
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'add_fixed_ip_to_instance'"
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|','
name|'rxtx_factor'
op|'='
name|'rxtx_factor'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
name|'network_id'
op|'='
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_fixed_ip_from_instance
dedent|''
name|'def'
name|'remove_fixed_ip_from_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_id'
op|','
name|'rxtx_factor'
op|','
nl|'\n'
name|'host'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
string|"'1.9'"
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'remove_fixed_ip_from_instance'"
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|','
name|'rxtx_factor'
op|'='
name|'rxtx_factor'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
name|'address'
op|'='
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_network_to_project
dedent|''
name|'def'
name|'add_network_to_project'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'project_id'
op|','
name|'network_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'client'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'add_network_to_project'"
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'network_uuid'
op|'='
name|'network_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instance_nw_info
dedent|''
name|'def'
name|'get_instance_nw_info'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_id'
op|','
name|'rxtx_factor'
op|','
name|'host'
op|','
nl|'\n'
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
string|"'1.9'"
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'get_instance_nw_info'"
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|','
name|'rxtx_factor'
op|'='
name|'rxtx_factor'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
name|'project_id'
op|'='
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|validate_networks
dedent|''
name|'def'
name|'validate_networks'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'networks'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'client'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'validate_networks'"
op|','
name|'networks'
op|'='
name|'networks'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_dns_domains
dedent|''
name|'def'
name|'get_dns_domains'
op|'('
name|'self'
op|','
name|'ctxt'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'client'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'get_dns_domains'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_dns_entry
dedent|''
name|'def'
name|'add_dns_entry'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'address'
op|','
name|'name'
op|','
name|'dns_type'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'client'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'add_dns_entry'"
op|','
nl|'\n'
name|'address'
op|'='
name|'address'
op|','
name|'name'
op|'='
name|'name'
op|','
nl|'\n'
name|'dns_type'
op|'='
name|'dns_type'
op|','
name|'domain'
op|'='
name|'domain'
op|')'
newline|'\n'
nl|'\n'
DECL|member|modify_dns_entry
dedent|''
name|'def'
name|'modify_dns_entry'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'address'
op|','
name|'name'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'client'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'modify_dns_entry'"
op|','
nl|'\n'
name|'address'
op|'='
name|'address'
op|','
name|'name'
op|'='
name|'name'
op|','
name|'domain'
op|'='
name|'domain'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_dns_entry
dedent|''
name|'def'
name|'delete_dns_entry'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'name'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'client'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'delete_dns_entry'"
op|','
nl|'\n'
name|'name'
op|'='
name|'name'
op|','
name|'domain'
op|'='
name|'domain'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_dns_domain
dedent|''
name|'def'
name|'delete_dns_domain'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'client'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'delete_dns_domain'"
op|','
name|'domain'
op|'='
name|'domain'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_dns_entries_by_address
dedent|''
name|'def'
name|'get_dns_entries_by_address'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'address'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'client'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'get_dns_entries_by_address'"
op|','
nl|'\n'
name|'address'
op|'='
name|'address'
op|','
name|'domain'
op|'='
name|'domain'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_dns_entries_by_name
dedent|''
name|'def'
name|'get_dns_entries_by_name'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'name'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'client'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'get_dns_entries_by_name'"
op|','
nl|'\n'
name|'name'
op|'='
name|'name'
op|','
name|'domain'
op|'='
name|'domain'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_private_dns_domain
dedent|''
name|'def'
name|'create_private_dns_domain'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'domain'
op|','
name|'av_zone'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'client'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'create_private_dns_domain'"
op|','
nl|'\n'
name|'domain'
op|'='
name|'domain'
op|','
name|'av_zone'
op|'='
name|'av_zone'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_public_dns_domain
dedent|''
name|'def'
name|'create_public_dns_domain'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'domain'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'client'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'create_public_dns_domain'"
op|','
nl|'\n'
name|'domain'
op|'='
name|'domain'
op|','
name|'project'
op|'='
name|'project'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_networks_on_host
dedent|''
name|'def'
name|'setup_networks_on_host'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_id'
op|','
name|'host'
op|','
name|'teardown'
op|','
nl|'\n'
name|'instance'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(tr3buchet): the call is just to wait for completion'
nl|'\n'
indent|'        '
name|'version'
op|'='
string|"'1.16'"
newline|'\n'
name|'kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
string|"'1.0'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'['
string|"'instance'"
op|']'
op|'='
name|'instance'
newline|'\n'
dedent|''
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'setup_networks_on_host'"
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'teardown'
op|'='
name|'teardown'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_network_host
dedent|''
name|'def'
name|'set_network_host'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'network_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'version'
op|'='
string|"'1.15'"
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
string|"'1.0'"
newline|'\n'
name|'network_ref'
op|'='
name|'objects_base'
op|'.'
name|'obj_to_primitive'
op|'('
name|'network_ref'
op|')'
newline|'\n'
dedent|''
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'set_network_host'"
op|','
name|'network_ref'
op|'='
name|'network_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|rpc_setup_network_on_host
dedent|''
name|'def'
name|'rpc_setup_network_on_host'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'network_id'
op|','
name|'teardown'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(tr3buchet): the call is just to wait for completion'
nl|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'server'
op|'='
name|'host'
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'rpc_setup_network_on_host'"
op|','
nl|'\n'
name|'network_id'
op|'='
name|'network_id'
op|','
name|'teardown'
op|'='
name|'teardown'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(russellb): Ideally this would not have a prefix of '_' since it is"
nl|'\n'
comment|'# a part of the rpc API. However, this is how it was being called when the'
nl|'\n'
comment|'# 1.0 API was being documented using this client proxy class.  It should be'
nl|'\n'
comment|'# changed if there was ever a 2.0.'
nl|'\n'
DECL|member|_rpc_allocate_fixed_ip
dedent|''
name|'def'
name|'_rpc_allocate_fixed_ip'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_id'
op|','
name|'network_id'
op|','
name|'address'
op|','
nl|'\n'
name|'vpn'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'server'
op|'='
name|'host'
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'_rpc_allocate_fixed_ip'"
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|','
name|'network_id'
op|'='
name|'network_id'
op|','
nl|'\n'
name|'address'
op|'='
name|'address'
op|','
name|'vpn'
op|'='
name|'vpn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deallocate_fixed_ip
dedent|''
name|'def'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'address'
op|','
name|'host'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
string|"'1.12'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
string|"'1.12'"
newline|'\n'
name|'kwargs'
op|'['
string|"'instance'"
op|']'
op|'='
name|'instance'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
string|"'1.0'"
newline|'\n'
dedent|''
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'server'
op|'='
name|'host'
op|','
name|'version'
op|'='
name|'version'
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'deallocate_fixed_ip'"
op|','
nl|'\n'
name|'address'
op|'='
name|'address'
op|','
name|'host'
op|'='
name|'host'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_dns
dedent|''
name|'def'
name|'update_dns'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'network_ids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'fanout'
op|'='
name|'True'
op|','
name|'version'
op|'='
string|"'1.3'"
op|')'
newline|'\n'
name|'cctxt'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
string|"'update_dns'"
op|','
name|'network_ids'
op|'='
name|'network_ids'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(russellb): Ideally this would not have a prefix of '_' since it is"
nl|'\n'
comment|'# a part of the rpc API. However, this is how it was being called when the'
nl|'\n'
comment|'# 1.0 API was being documented using this client proxy class.  It should be'
nl|'\n'
comment|'# changed if there was ever a 2.0.'
nl|'\n'
DECL|member|_associate_floating_ip
dedent|''
name|'def'
name|'_associate_floating_ip'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'floating_address'
op|','
name|'fixed_address'
op|','
nl|'\n'
name|'interface'
op|','
name|'host'
op|','
name|'instance_uuid'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'server'
op|'='
name|'host'
op|','
name|'version'
op|'='
string|"'1.6'"
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'_associate_floating_ip'"
op|','
nl|'\n'
name|'floating_address'
op|'='
name|'floating_address'
op|','
nl|'\n'
name|'fixed_address'
op|'='
name|'fixed_address'
op|','
nl|'\n'
name|'interface'
op|'='
name|'interface'
op|','
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(russellb): Ideally this would not have a prefix of '_' since it is"
nl|'\n'
comment|'# a part of the rpc API. However, this is how it was being called when the'
nl|'\n'
comment|'# 1.0 API was being documented using this client proxy class.  It should be'
nl|'\n'
comment|'# changed if there was ever a 2.0.'
nl|'\n'
DECL|member|_disassociate_floating_ip
dedent|''
name|'def'
name|'_disassociate_floating_ip'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'address'
op|','
name|'interface'
op|','
name|'host'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'server'
op|'='
name|'host'
op|','
name|'version'
op|'='
string|"'1.6'"
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'_disassociate_floating_ip'"
op|','
nl|'\n'
name|'address'
op|'='
name|'address'
op|','
name|'interface'
op|'='
name|'interface'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lease_fixed_ip
dedent|''
name|'def'
name|'lease_fixed_ip'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'address'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'server'
op|'='
name|'host'
op|')'
newline|'\n'
name|'cctxt'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
string|"'lease_fixed_ip'"
op|','
name|'address'
op|'='
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|release_fixed_ip
dedent|''
name|'def'
name|'release_fixed_ip'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'address'
op|','
name|'host'
op|','
name|'mac'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
string|"'1.14'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
string|"'1.14'"
newline|'\n'
name|'kwargs'
op|'['
string|"'mac'"
op|']'
op|'='
name|'mac'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
string|"'1.0'"
newline|'\n'
dedent|''
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'server'
op|'='
name|'host'
op|','
name|'version'
op|'='
name|'version'
op|')'
newline|'\n'
name|'cctxt'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
string|"'release_fixed_ip'"
op|','
name|'address'
op|'='
name|'address'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|migrate_instance_start
dedent|''
name|'def'
name|'migrate_instance_start'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_uuid'
op|','
name|'rxtx_factor'
op|','
nl|'\n'
name|'project_id'
op|','
name|'source_compute'
op|','
name|'dest_compute'
op|','
nl|'\n'
name|'floating_addresses'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'server'
op|'='
name|'host'
op|','
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'migrate_instance_start'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'rxtx_factor'
op|'='
name|'rxtx_factor'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'source'
op|'='
name|'source_compute'
op|','
nl|'\n'
name|'dest'
op|'='
name|'dest_compute'
op|','
nl|'\n'
name|'floating_addresses'
op|'='
name|'floating_addresses'
op|')'
newline|'\n'
nl|'\n'
DECL|member|migrate_instance_finish
dedent|''
name|'def'
name|'migrate_instance_finish'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_uuid'
op|','
name|'rxtx_factor'
op|','
nl|'\n'
name|'project_id'
op|','
name|'source_compute'
op|','
name|'dest_compute'
op|','
nl|'\n'
name|'floating_addresses'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'server'
op|'='
name|'host'
op|','
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'migrate_instance_finish'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'rxtx_factor'
op|'='
name|'rxtx_factor'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'source'
op|'='
name|'source_compute'
op|','
nl|'\n'
name|'dest'
op|'='
name|'dest_compute'
op|','
nl|'\n'
name|'floating_addresses'
op|'='
name|'floating_addresses'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
