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
string|"'''Cells client-side RPC API\n\n    API version history:\n\n        1.0 - Initial version.\n        1.1 - Adds get_cell_info_for_neighbors() and sync_instances()\n    '''"
newline|'\n'
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
op|')'
op|':'
newline|'\n'
indent|'        '
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
dedent|''
dedent|''
endmarker|''
end_unit
