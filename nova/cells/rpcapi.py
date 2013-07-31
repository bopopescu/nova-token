begin_unit
comment|'# Copyright (c) 2012 Rackspace Hosting'
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
string|'"""\nClient side of nova-cells RPC API (for talking to the nova-cells service\nwithin a cell).\n\nThis is different than communication between child and parent nova-cells\nservices.  That communication is handled by the cells driver via the\nmessging module.\n"""'
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
name|'import'
name|'exception'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
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
op|'.'
name|'rpc'
name|'import'
name|'proxy'
name|'as'
name|'rpc_proxy'
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
string|"'enable'"
op|','
string|"'nova.cells.opts'"
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'topic'"
op|','
string|"'nova.cells.opts'"
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|rpcapi_cap_opt
name|'rpcapi_cap_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cells'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set a version cap for messages sent to local cells services'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opt'
op|'('
name|'rpcapi_cap_opt'
op|','
string|"'upgrade_levels'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellsAPI
name|'class'
name|'CellsAPI'
op|'('
name|'rpc_proxy'
op|'.'
name|'RpcProxy'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Cells client-side RPC API\n\n    API version history:\n\n        1.0 - Initial version.\n        1.1 - Adds get_cell_info_for_neighbors() and sync_instances()\n        1.2 - Adds service_get_all(), service_get_by_compute_host(),\n              and proxy_rpc_to_compute_manager()\n        1.3 - Adds task_log_get_all()\n        1.4 - Adds compute_node_get(), compute_node_get_all(), and\n              compute_node_stats()\n        1.5 - Adds actions_get(), action_get_by_request_id(), and\n              action_events_get()\n        1.6 - Adds consoleauth_delete_tokens() and validate_console_port()\n\n        ... Grizzly supports message version 1.6.  So, any changes to existing\n        methods in 2.x after that point should be done such that they can\n        handle the version_cap being set to 1.6.\n\n        1.7 - Adds service_update()\n        1.8 - Adds build_instances(), deprecates schedule_run_instance()\n        1.9 - Adds get_capacities()\n        1.10 - Adds bdm_update_or_create_at_top(), and bdm_destroy_at_top()\n        1.11 - Adds get_migrations()\n        1.12 - Adds instance_start() and instance_stop()\n        1.13 - Adds cell_create(), cell_update(), cell_delete(), and\n               cell_get()\n        1.14 - Adds reboot_instance()\n        1.15 - Adds suspend_instance() and resume_instance()\n        1.16 - Adds instance_update_from_api()\n        1.17 - Adds get_host_uptime()\n    '''"
newline|'\n'
DECL|variable|BASE_RPC_API_VERSION
name|'BASE_RPC_API_VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|VERSION_ALIASES
name|'VERSION_ALIASES'
op|'='
op|'{'
nl|'\n'
string|"'grizzly'"
op|':'
string|"'1.6'"
nl|'\n'
op|'}'
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
name|'cells'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'cells'
op|')'
newline|'\n'
name|'super'
op|'('
name|'CellsAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'topic'
op|'='
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'topic'
op|','
nl|'\n'
name|'default_version'
op|'='
name|'self'
op|'.'
name|'BASE_RPC_API_VERSION'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'objects_base'
op|'.'
name|'NovaObjectSerializer'
op|'('
op|')'
op|','
nl|'\n'
name|'version_cap'
op|'='
name|'version_cap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|cast_compute_api_method
dedent|''
name|'def'
name|'cast_compute_api_method'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'cell_name'
op|','
name|'method'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make a cast to a compute API method in a certain cell."""'
newline|'\n'
name|'method_info'
op|'='
op|'{'
string|"'method'"
op|':'
name|'method'
op|','
nl|'\n'
string|"'method_args'"
op|':'
name|'args'
op|','
nl|'\n'
string|"'method_kwargs'"
op|':'
name|'kwargs'
op|'}'
newline|'\n'
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
string|"'run_compute_api_method'"
op|','
nl|'\n'
name|'cell_name'
op|'='
name|'cell_name'
op|','
nl|'\n'
name|'method_info'
op|'='
name|'method_info'
op|','
nl|'\n'
name|'call'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|call_compute_api_method
dedent|''
name|'def'
name|'call_compute_api_method'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'cell_name'
op|','
name|'method'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make a call to a compute API method in a certain cell."""'
newline|'\n'
name|'method_info'
op|'='
op|'{'
string|"'method'"
op|':'
name|'method'
op|','
nl|'\n'
string|"'method_args'"
op|':'
name|'args'
op|','
nl|'\n'
string|"'method_kwargs'"
op|':'
name|'kwargs'
op|'}'
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
string|"'run_compute_api_method'"
op|','
nl|'\n'
name|'cell_name'
op|'='
name|'cell_name'
op|','
nl|'\n'
name|'method_info'
op|'='
name|'method_info'
op|','
nl|'\n'
name|'call'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(alaski): Deprecated and should be removed later.'
nl|'\n'
DECL|member|schedule_run_instance
dedent|''
name|'def'
name|'schedule_run_instance'
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
string|'"""Schedule a new instance for creation."""'
newline|'\n'
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
string|"'schedule_run_instance'"
op|','
nl|'\n'
name|'host_sched_kwargs'
op|'='
name|'kwargs'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|build_instances
dedent|''
name|'def'
name|'build_instances'
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
string|'"""Build instances."""'
newline|'\n'
name|'build_inst_kwargs'
op|'='
name|'kwargs'
newline|'\n'
name|'instances'
op|'='
name|'build_inst_kwargs'
op|'['
string|"'instances'"
op|']'
newline|'\n'
name|'instances_p'
op|'='
op|'['
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'inst'
op|')'
name|'for'
name|'inst'
name|'in'
name|'instances'
op|']'
newline|'\n'
name|'build_inst_kwargs'
op|'['
string|"'instances'"
op|']'
op|'='
name|'instances_p'
newline|'\n'
name|'build_inst_kwargs'
op|'['
string|"'image'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
nl|'\n'
name|'build_inst_kwargs'
op|'['
string|"'image'"
op|']'
op|')'
newline|'\n'
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
string|"'build_instances'"
op|','
nl|'\n'
name|'build_inst_kwargs'
op|'='
name|'build_inst_kwargs'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.8'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_update_at_top
dedent|''
name|'def'
name|'instance_update_at_top'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update instance at API level."""'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
comment|'# Make sure we have a dict, not a SQLAlchemy model'
nl|'\n'
dedent|''
name|'instance_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'instance'
op|')'
newline|'\n'
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
string|"'instance_update_at_top'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance_p'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_destroy_at_top
dedent|''
name|'def'
name|'instance_destroy_at_top'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy instance at API level."""'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'instance_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'instance'
op|')'
newline|'\n'
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
string|"'instance_destroy_at_top'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance_p'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_delete_everywhere
dedent|''
name|'def'
name|'instance_delete_everywhere'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'delete_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete instance everywhere.  delete_type may be \'soft\'\n        or \'hard\'.  This is generally only used to resolve races\n        when API cell doesn\'t know to what cell an instance belongs.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'instance_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'instance'
op|')'
newline|'\n'
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
string|"'instance_delete_everywhere'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance_p'
op|','
nl|'\n'
name|'delete_type'
op|'='
name|'delete_type'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_fault_create_at_top
dedent|''
name|'def'
name|'instance_fault_create_at_top'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_fault'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create an instance fault at the top."""'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'instance_fault_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'instance_fault'
op|')'
newline|'\n'
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
string|"'instance_fault_create_at_top'"
op|','
nl|'\n'
name|'instance_fault'
op|'='
name|'instance_fault_p'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|bw_usage_update_at_top
dedent|''
name|'def'
name|'bw_usage_update_at_top'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'uuid'
op|','
name|'mac'
op|','
name|'start_period'
op|','
nl|'\n'
name|'bw_in'
op|','
name|'bw_out'
op|','
name|'last_ctr_in'
op|','
name|'last_ctr_out'
op|','
name|'last_refreshed'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Broadcast upwards that bw_usage was updated."""'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'bw_update_info'
op|'='
op|'{'
string|"'uuid'"
op|':'
name|'uuid'
op|','
nl|'\n'
string|"'mac'"
op|':'
name|'mac'
op|','
nl|'\n'
string|"'start_period'"
op|':'
name|'start_period'
op|','
nl|'\n'
string|"'bw_in'"
op|':'
name|'bw_in'
op|','
nl|'\n'
string|"'bw_out'"
op|':'
name|'bw_out'
op|','
nl|'\n'
string|"'last_ctr_in'"
op|':'
name|'last_ctr_in'
op|','
nl|'\n'
string|"'last_ctr_out'"
op|':'
name|'last_ctr_out'
op|','
nl|'\n'
string|"'last_refreshed'"
op|':'
name|'last_refreshed'
op|'}'
newline|'\n'
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
string|"'bw_usage_update_at_top'"
op|','
nl|'\n'
name|'bw_update_info'
op|'='
name|'bw_update_info'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_info_cache_update_at_top
dedent|''
name|'def'
name|'instance_info_cache_update_at_top'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_info_cache'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Broadcast up that an instance\'s info_cache has changed."""'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'iicache'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'instance_info_cache'
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
name|'iicache'
op|'['
string|"'instance_uuid'"
op|']'
op|','
nl|'\n'
string|"'info_cache'"
op|':'
name|'iicache'
op|'}'
newline|'\n'
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
string|"'instance_update_at_top'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_cell_info_for_neighbors
dedent|''
name|'def'
name|'get_cell_info_for_neighbors'
op|'('
name|'self'
op|','
name|'ctxt'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get information about our neighbor cells from the manager."""'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
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
string|"'get_cell_info_for_neighbors'"
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|sync_instances
dedent|''
name|'def'
name|'sync_instances'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'project_id'
op|'='
name|'None'
op|','
name|'updated_since'
op|'='
name|'None'
op|','
nl|'\n'
name|'deleted'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ask all cells to sync instance data."""'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'return'
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
string|"'sync_instances'"
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'updated_since'
op|'='
name|'updated_since'
op|','
nl|'\n'
name|'deleted'
op|'='
name|'deleted'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_get_all
dedent|''
name|'def'
name|'service_get_all'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'filters'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ask all cells for their list of services."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'service_get_all'"
op|','
nl|'\n'
name|'filters'
op|'='
name|'filters'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_get_by_compute_host
dedent|''
name|'def'
name|'service_get_by_compute_host'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'host_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the service entry for a host in a particular cell.  The\n        cell name should be encoded within the host_name.\n        """'
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
string|"'service_get_by_compute_host'"
op|','
nl|'\n'
name|'host_name'
op|'='
name|'host_name'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_host_uptime
dedent|''
name|'def'
name|'get_host_uptime'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Gets the host uptime in a particular cell. The cell name should\n        be encoded within the host_name\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_host_uptime'"
op|','
nl|'\n'
name|'host_name'
op|'='
name|'host_name'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.17'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_update
dedent|''
name|'def'
name|'service_update'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'host_name'
op|','
name|'binary'
op|','
name|'params_to_update'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Used to enable/disable a service. For compute services, setting to\n        disabled stops new builds arriving on that host.\n\n        :param host_name: the name of the host machine that the service is\n                          running\n        :param binary: The name of the executable that the service runs as\n        :param params_to_update: eg. {\'disabled\': True}\n        """'
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
string|"'service_update'"
op|','
name|'host_name'
op|'='
name|'host_name'
op|','
nl|'\n'
name|'binary'
op|'='
name|'binary'
op|','
name|'params_to_update'
op|'='
name|'params_to_update'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.7'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|proxy_rpc_to_manager
dedent|''
name|'def'
name|'proxy_rpc_to_manager'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'rpc_message'
op|','
name|'topic'
op|','
name|'call'
op|'='
name|'False'
op|','
nl|'\n'
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Proxy RPC to a compute manager.  The host in the topic\n        should be encoded with the target cell name.\n        """'
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
string|"'proxy_rpc_to_manager'"
op|','
nl|'\n'
name|'topic'
op|'='
name|'topic'
op|','
nl|'\n'
name|'rpc_message'
op|'='
name|'rpc_message'
op|','
nl|'\n'
name|'call'
op|'='
name|'call'
op|','
nl|'\n'
name|'timeout'
op|'='
name|'timeout'
op|')'
op|','
nl|'\n'
name|'timeout'
op|'='
name|'timeout'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|task_log_get_all
dedent|''
name|'def'
name|'task_log_get_all'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'task_name'
op|','
name|'period_beginning'
op|','
nl|'\n'
name|'period_ending'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'state'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the task logs from the DB in child cells."""'
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
string|"'task_log_get_all'"
op|','
nl|'\n'
name|'task_name'
op|'='
name|'task_name'
op|','
nl|'\n'
name|'period_beginning'
op|'='
name|'period_beginning'
op|','
nl|'\n'
name|'period_ending'
op|'='
name|'period_ending'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
name|'state'
op|'='
name|'state'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.3'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|compute_node_get
dedent|''
name|'def'
name|'compute_node_get'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'compute_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get a compute node by ID in a specific cell."""'
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
string|"'compute_node_get'"
op|','
nl|'\n'
name|'compute_id'
op|'='
name|'compute_id'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.4'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|compute_node_get_all
dedent|''
name|'def'
name|'compute_node_get_all'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'hypervisor_match'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return list of compute nodes in all cells, optionally\n        filtering by hypervisor host.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'compute_node_get_all'"
op|','
nl|'\n'
name|'hypervisor_match'
op|'='
name|'hypervisor_match'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.4'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|compute_node_stats
dedent|''
name|'def'
name|'compute_node_stats'
op|'('
name|'self'
op|','
name|'ctxt'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return compute node stats from all cells."""'
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
string|"'compute_node_stats'"
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.4'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|actions_get
dedent|''
name|'def'
name|'actions_get'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'instance'
op|'['
string|"'cell_name'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceUnknownCell'
op|'('
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
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
string|"'actions_get'"
op|','
nl|'\n'
name|'cell_name'
op|'='
name|'instance'
op|'['
string|"'cell_name'"
op|']'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.5'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|action_get_by_request_id
dedent|''
name|'def'
name|'action_get_by_request_id'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'request_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'instance'
op|'['
string|"'cell_name'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceUnknownCell'
op|'('
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
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
string|"'action_get_by_request_id'"
op|','
nl|'\n'
name|'cell_name'
op|'='
name|'instance'
op|'['
string|"'cell_name'"
op|']'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'request_id'
op|'='
name|'request_id'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.5'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|action_events_get
dedent|''
name|'def'
name|'action_events_get'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'action_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'instance'
op|'['
string|"'cell_name'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceUnknownCell'
op|'('
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
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
string|"'action_events_get'"
op|','
nl|'\n'
name|'cell_name'
op|'='
name|'instance'
op|'['
string|"'cell_name'"
op|']'
op|','
nl|'\n'
name|'action_id'
op|'='
name|'action_id'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.5'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|consoleauth_delete_tokens
dedent|''
name|'def'
name|'consoleauth_delete_tokens'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete consoleauth tokens for an instance in API cells."""'
newline|'\n'
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
string|"'consoleauth_delete_tokens'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.6'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|validate_console_port
dedent|''
name|'def'
name|'validate_console_port'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_uuid'
op|','
name|'console_port'
op|','
nl|'\n'
name|'console_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Validate console port with child cell compute node."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'validate_console_port'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'console_port'
op|'='
name|'console_port'
op|','
nl|'\n'
name|'console_type'
op|'='
name|'console_type'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.6'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_capacities
dedent|''
name|'def'
name|'get_capacities'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'cell_name'
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
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_capacities'"
op|','
name|'cell_name'
op|'='
name|'cell_name'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.9'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|bdm_update_or_create_at_top
dedent|''
name|'def'
name|'bdm_update_or_create_at_top'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'bdm'
op|','
name|'create'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create or update a block device mapping in API cells.  If\n        create is True, only try to create.  If create is None, try to\n        update but fall back to create.  If create is False, only attempt\n        to update.  This maps to nova-conductor\'s behavior.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
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
string|"'bdm_update_or_create_at_top'"
op|','
nl|'\n'
name|'bdm'
op|'='
name|'bdm'
op|','
name|'create'
op|'='
name|'create'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.10'"
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
name|'exception'
op|'('
name|'_'
op|'('
string|'"Failed to notify cells of BDM update/create."'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|bdm_destroy_at_top
dedent|''
dedent|''
name|'def'
name|'bdm_destroy_at_top'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_uuid'
op|','
name|'device_name'
op|'='
name|'None'
op|','
nl|'\n'
name|'volume_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Broadcast upwards that a block device mapping was destroyed.\n        One of device_name or volume_id should be specified.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
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
string|"'bdm_destroy_at_top'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'device_name'
op|'='
name|'device_name'
op|','
nl|'\n'
name|'volume_id'
op|'='
name|'volume_id'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.10'"
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
name|'exception'
op|'('
name|'_'
op|'('
string|'"Failed to notify cells of BDM destroy."'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_migrations
dedent|''
dedent|''
name|'def'
name|'get_migrations'
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
string|'"""Get all migrations applying the filters."""'
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
string|"'get_migrations'"
op|','
nl|'\n'
name|'filters'
op|'='
name|'filters'
op|')'
op|','
name|'version'
op|'='
string|"'1.11'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_update_from_api
dedent|''
name|'def'
name|'instance_update_from_api'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'expected_vm_state'
op|','
nl|'\n'
name|'expected_task_state'
op|','
name|'admin_state_reset'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update an instance in its cell.\n\n        This method takes a new-world instance object.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'instance_update_from_api'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|','
nl|'\n'
name|'expected_vm_state'
op|'='
name|'expected_vm_state'
op|','
nl|'\n'
name|'expected_task_state'
op|'='
name|'expected_task_state'
op|','
nl|'\n'
name|'admin_state_reset'
op|'='
name|'admin_state_reset'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.16'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|start_instance
dedent|''
name|'def'
name|'start_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start an instance in its cell.\n\n        This method takes a new-world instance object.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'start_instance'"
op|','
name|'instance'
op|'='
name|'instance'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.12'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop_instance
dedent|''
name|'def'
name|'stop_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'do_cast'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stop an instance in its cell.\n\n        This method takes a new-world instance object.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'method'
op|'='
name|'do_cast'
name|'and'
name|'self'
op|'.'
name|'cast'
name|'or'
name|'self'
op|'.'
name|'call'
newline|'\n'
name|'return'
name|'method'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'stop_instance'"
op|','
name|'instance'
op|'='
name|'instance'
op|','
nl|'\n'
name|'do_cast'
op|'='
name|'do_cast'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.12'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|cell_create
dedent|''
name|'def'
name|'cell_create'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'values'
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
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'cell_create'"
op|','
name|'values'
op|'='
name|'values'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.13'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|cell_update
dedent|''
name|'def'
name|'cell_update'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'cell_name'
op|','
name|'values'
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
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'cell_update'"
op|','
nl|'\n'
name|'cell_name'
op|'='
name|'cell_name'
op|','
nl|'\n'
name|'values'
op|'='
name|'values'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.13'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|cell_delete
dedent|''
name|'def'
name|'cell_delete'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'cell_name'
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
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'cell_delete'"
op|','
name|'cell_name'
op|'='
name|'cell_name'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.13'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|cell_get
dedent|''
name|'def'
name|'cell_get'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'cell_name'
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
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'cell_get'"
op|','
name|'cell_name'
op|'='
name|'cell_name'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.13'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|reboot_instance
dedent|''
name|'def'
name|'reboot_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'block_device_info'
op|','
nl|'\n'
name|'reboot_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboot an instance in its cell.\n\n        This method takes a new-world instance object.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'reboot_instance'"
op|','
name|'instance'
op|'='
name|'instance'
op|','
nl|'\n'
name|'reboot_type'
op|'='
name|'reboot_type'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.14'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|suspend_instance
dedent|''
name|'def'
name|'suspend_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Suspend an instance in its cell.\n\n        This method takes a new-world instance object.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'suspend_instance'"
op|','
name|'instance'
op|'='
name|'instance'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.15'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|resume_instance
dedent|''
name|'def'
name|'resume_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Resume an instance in its cell.\n\n        This method takes a new-world instance object.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'enable'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'resume_instance'"
op|','
name|'instance'
op|'='
name|'instance'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.15'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
