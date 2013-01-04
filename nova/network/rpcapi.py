begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012, Red Hat, Inc.'
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
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rpc'
name|'import'
name|'proxy'
name|'as'
name|'rpc_proxy'
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
name|'import_opt'
op|'('
string|"'network_topic'"
op|','
string|"'nova.config'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkAPI
name|'class'
name|'NetworkAPI'
op|'('
name|'rpc_proxy'
op|'.'
name|'RpcProxy'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Client side of the network rpc API.\n\n    API version history:\n\n        1.0 - Initial version.\n        1.1 - Adds migrate_instance_[start|finish]\n        1.2 - Make migrate_instance_[start|finish] a little more flexible\n        1.3 - Adds fanout cast update_dns for multi_host networks\n        1.4 - Add get_backdoor_port()\n        1.5 - Adds associate\n        1.6 - Adds instance_uuid to _{dis,}associate_floating_ip\n    '''"
newline|'\n'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# NOTE(russellb): This is the default minimum version that the server'
nl|'\n'
comment|'# (manager) side must implement unless otherwise specified using a version'
nl|'\n'
comment|'# argument to self.call()/cast()/etc. here.  It should be left as X.0 where'
nl|'\n'
comment|'# X is the current major API version (1.0, 2.0, ...).  For more information'
nl|'\n'
comment|'# about rpc API versioning, see the docs in'
nl|'\n'
comment|'# openstack/common/rpc/dispatcher.py.'
nl|'\n'
comment|'#'
nl|'\n'
DECL|variable|BASE_RPC_API_VERSION
name|'BASE_RPC_API_VERSION'
op|'='
string|"'1.0'"
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
name|'topic'
op|'='
name|'topic'
name|'if'
name|'topic'
name|'else'
name|'CONF'
op|'.'
name|'network_topic'
newline|'\n'
name|'super'
op|'('
name|'NetworkAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
nl|'\n'
name|'topic'
op|'='
name|'topic'
op|','
nl|'\n'
name|'default_version'
op|'='
name|'self'
op|'.'
name|'BASE_RPC_API_VERSION'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all_networks
dedent|''
name|'def'
name|'get_all_networks'
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_all_networks'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_network
dedent|''
name|'def'
name|'get_network'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'network_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_network'"
op|','
nl|'\n'
name|'network_uuid'
op|'='
name|'network_uuid'
op|')'
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'create_networks'"
op|','
op|'**'
name|'kwargs'
op|')'
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
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
op|')'
newline|'\n'
nl|'\n'
DECL|member|disassociate_network
dedent|''
name|'def'
name|'disassociate_network'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'network_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'disassociate_network'"
op|','
nl|'\n'
name|'network_uuid'
op|'='
name|'network_uuid'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_fixed_ip
dedent|''
name|'def'
name|'get_fixed_ip'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_fixed_ip'"
op|','
name|'id'
op|'='
name|'id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_fixed_ip_by_address
dedent|''
name|'def'
name|'get_fixed_ip_by_address'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_fixed_ip_by_address'"
op|','
nl|'\n'
name|'address'
op|'='
name|'address'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ip
dedent|''
name|'def'
name|'get_floating_ip'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_floating_ip'"
op|','
name|'id'
op|'='
name|'id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_pools
dedent|''
name|'def'
name|'get_floating_pools'
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_floating_pools'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ip_by_address
dedent|''
name|'def'
name|'get_floating_ip_by_address'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_floating_ip_by_address'"
op|','
nl|'\n'
name|'address'
op|'='
name|'address'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ips_by_project
dedent|''
name|'def'
name|'get_floating_ips_by_project'
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_floating_ips_by_project'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ips_by_fixed_address
dedent|''
name|'def'
name|'get_floating_ips_by_fixed_address'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'fixed_address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
nl|'\n'
string|"'get_floating_ips_by_fixed_address'"
op|','
nl|'\n'
name|'fixed_address'
op|'='
name|'fixed_address'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instance_id_by_floating_address
dedent|''
name|'def'
name|'get_instance_id_by_floating_address'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
nl|'\n'
string|"'get_instance_id_by_floating_address'"
op|','
nl|'\n'
name|'address'
op|'='
name|'address'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_backdoor_port
dedent|''
name|'def'
name|'get_backdoor_port'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_backdoor_port'"
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.4'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_vifs_by_instance
dedent|''
name|'def'
name|'get_vifs_by_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): When the db calls are converted to store network'
nl|'\n'
comment|'#             data by instance_uuid, this should pass uuid instead.'
nl|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_vifs_by_instance'"
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_vif_by_mac_address
dedent|''
name|'def'
name|'get_vif_by_mac_address'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'mac_address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_vif_by_mac_address'"
op|','
nl|'\n'
name|'mac_address'
op|'='
name|'mac_address'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_floating_ip
dedent|''
name|'def'
name|'allocate_floating_ip'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'project_id'
op|','
name|'pool'
op|','
name|'auto_assigned'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'allocate_floating_ip'"
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|','
name|'pool'
op|'='
name|'pool'
op|','
name|'auto_assigned'
op|'='
name|'auto_assigned'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deallocate_floating_ip
dedent|''
name|'def'
name|'deallocate_floating_ip'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'address'
op|','
name|'affect_auto_assigned'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'deallocate_floating_ip'"
op|','
nl|'\n'
name|'address'
op|'='
name|'address'
op|','
name|'affect_auto_assigned'
op|'='
name|'affect_auto_assigned'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|associate_floating_ip
dedent|''
name|'def'
name|'associate_floating_ip'
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
name|'affect_auto_assigned'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'associate_floating_ip'"
op|','
nl|'\n'
name|'floating_address'
op|'='
name|'floating_address'
op|','
name|'fixed_address'
op|'='
name|'fixed_address'
op|','
nl|'\n'
name|'affect_auto_assigned'
op|'='
name|'affect_auto_assigned'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|disassociate_floating_ip
dedent|''
name|'def'
name|'disassociate_floating_ip'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'address'
op|','
name|'affect_auto_assigned'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'disassociate_floating_ip'"
op|','
nl|'\n'
name|'address'
op|'='
name|'address'
op|','
name|'affect_auto_assigned'
op|'='
name|'affect_auto_assigned'
op|')'
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
name|'instance_uuid'
op|','
nl|'\n'
name|'project_id'
op|','
name|'host'
op|','
name|'rxtx_factor'
op|','
name|'vpn'
op|','
nl|'\n'
name|'requested_networks'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'allocate_for_instance'"
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|','
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|','
name|'host'
op|'='
name|'host'
op|','
name|'rxtx_factor'
op|'='
name|'rxtx_factor'
op|','
nl|'\n'
name|'vpn'
op|'='
name|'vpn'
op|','
name|'requested_networks'
op|'='
name|'requested_networks'
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
name|'instance_id'
op|','
name|'project_id'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'deallocate_for_instance'"
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
name|'host'
op|'='
name|'host'
op|')'
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
name|'host'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'add_fixed_ip_to_instance'"
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
name|'network_id'
op|'='
name|'network_id'
op|')'
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
name|'host'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'remove_fixed_ip_from_instance'"
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
name|'address'
op|'='
name|'address'
op|')'
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'add_network_to_project'"
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|','
name|'network_uuid'
op|'='
name|'network_uuid'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|associate
dedent|''
name|'def'
name|'associate'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'network_uuid'
op|','
name|'associations'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'associate'"
op|','
nl|'\n'
name|'network_uuid'
op|'='
name|'network_uuid'
op|','
name|'associations'
op|'='
name|'associations'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'topic'
op|','
name|'version'
op|'='
string|'"1.5"'
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
name|'instance_uuid'
op|','
nl|'\n'
name|'rxtx_factor'
op|','
name|'host'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_instance_nw_info'"
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|','
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'rxtx_factor'
op|'='
name|'rxtx_factor'
op|','
name|'host'
op|'='
name|'host'
op|','
name|'project_id'
op|'='
name|'project_id'
op|')'
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'validate_networks'"
op|','
nl|'\n'
name|'networks'
op|'='
name|'networks'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instance_uuids_by_ip_filter
dedent|''
name|'def'
name|'get_instance_uuids_by_ip_filter'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'filters'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_instance_uuids_by_ip_filter'"
op|','
nl|'\n'
name|'filters'
op|'='
name|'filters'
op|')'
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_dns_domains'"
op|')'
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'add_dns_entry'"
op|','
name|'address'
op|'='
name|'address'
op|','
nl|'\n'
name|'name'
op|'='
name|'name'
op|','
name|'dns_type'
op|'='
name|'dns_type'
op|','
name|'domain'
op|'='
name|'domain'
op|')'
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'delete_dns_domain'"
op|','
nl|'\n'
name|'domain'
op|'='
name|'domain'
op|')'
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
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
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
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
op|')'
op|':'
newline|'\n'
comment|'# NOTE(tr3buchet): the call is just to wait for completion'
nl|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
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
name|'teardown'
op|'='
name|'teardown'
op|')'
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
name|'network_ref_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'network_ref'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'set_network_host'"
op|','
nl|'\n'
name|'network_ref'
op|'='
name|'network_ref_p'
op|')'
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
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
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
op|','
nl|'\n'
name|'topic'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'topic'
op|','
name|'host'
op|')'
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
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
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
op|','
nl|'\n'
name|'topic'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'topic'
op|','
name|'host'
op|')'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
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
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'topic'
op|','
name|'host'
op|')'
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
name|'return'
name|'self'
op|'.'
name|'fanout_cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'update_dns'"
op|','
nl|'\n'
name|'network_ids'
op|'='
name|'network_ids'
op|')'
op|','
name|'version'
op|'='
string|"'1.3'"
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
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'_associate_floating_ip'"
op|','
nl|'\n'
name|'floating_address'
op|'='
name|'floating_address'
op|','
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
op|','
nl|'\n'
name|'topic'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.6'"
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
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
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
op|','
nl|'\n'
name|'topic'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.6'"
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
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'lease_fixed_ip'"
op|','
name|'address'
op|'='
name|'address'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'topic'
op|','
name|'host'
op|')'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'release_fixed_ip'"
op|','
name|'address'
op|'='
name|'address'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'topic'
op|','
name|'host'
op|')'
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
name|'topic'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'topic'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
nl|'\n'
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
op|','
nl|'\n'
name|'topic'
op|'='
name|'topic'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.2'"
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
name|'topic'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'topic'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
nl|'\n'
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
op|','
nl|'\n'
name|'topic'
op|'='
name|'topic'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
