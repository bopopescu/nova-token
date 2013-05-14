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
string|'"""\nCells Service Manager\n"""'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'time'
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
op|'.'
name|'cells'
name|'import'
name|'messaging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'state'
name|'as'
name|'cells_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'utils'
name|'as'
name|'cells_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'periodic_task'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
DECL|variable|cell_manager_opts
name|'cell_manager_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.cells.rpc_driver.CellsRPCDriver'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Cells communication driver to use'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"instance_updated_at_threshold"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Number of seconds after an instance was updated "'
nl|'\n'
string|'"or deleted to continue to update cells"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"instance_update_num_instances"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Number of instances to update per periodic task run"'
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
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
name|'register_opts'
op|'('
name|'cell_manager_opts'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellsManager
name|'class'
name|'CellsManager'
op|'('
name|'manager'
op|'.'
name|'Manager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The nova-cells manager class.  This class defines RPC\n    methods that the local cell may call.  This class is NOT used for\n    messages coming from other cells.  That communication is\n    driver-specific.\n\n    Communication to other cells happens via the messaging module.  The\n    MessageRunner from that module will handle routing the message to\n    the correct cell via the communications driver.  Most methods below\n    create \'targeted\' (where we want to route a message to a specific cell)\n    or \'broadcast\' (where we want a message to go to multiple cells)\n    messages.\n\n    Scheduling requests get passed to the scheduler class.\n    """'
newline|'\n'
DECL|variable|RPC_API_VERSION
name|'RPC_API_VERSION'
op|'='
string|"'1.8'"
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|'# Mostly for tests.'
nl|'\n'
indent|'        '
name|'cell_state_manager'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'cell_state_manager'"
op|','
name|'None'
op|')'
newline|'\n'
name|'super'
op|'('
name|'CellsManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'service_name'
op|'='
string|"'cells'"
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'if'
name|'cell_state_manager'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'cell_state_manager'
op|'='
name|'cells_state'
op|'.'
name|'CellStateManager'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'state_manager'
op|'='
name|'cell_state_manager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'='
name|'messaging'
op|'.'
name|'MessageRunner'
op|'('
name|'self'
op|'.'
name|'state_manager'
op|')'
newline|'\n'
name|'cells_driver_cls'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'driver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'='
name|'cells_driver_cls'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instances_to_heal'
op|'='
name|'iter'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|post_start_hook
dedent|''
name|'def'
name|'post_start_hook'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Have the driver start its consumers for inter-cell communication.\n        Also ask our child cells for their capacities and capabilities so\n        we get them more quickly than just waiting for the next periodic\n        update.  Receiving the updates from the children will cause us to\n        update our parents.  If we don\'t have any children, just update\n        our parents immediately.\n        """'
newline|'\n'
comment|"# FIXME(comstud): There's currently no hooks when services are"
nl|'\n'
comment|'# stopping, so we have no way to stop consumers cleanly.'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'start_consumers'
op|'('
name|'self'
op|'.'
name|'msg_runner'
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'state_manager'
op|'.'
name|'get_child_cells'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'ask_children_for_capabilities'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'ask_children_for_capacities'
op|'('
name|'ctxt'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_update_our_parents'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'periodic_task'
op|'.'
name|'periodic_task'
newline|'\n'
DECL|member|_update_our_parents
name|'def'
name|'_update_our_parents'
op|'('
name|'self'
op|','
name|'ctxt'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update our parent cells with our capabilities and capacity\n        if we\'re at the bottom of the tree.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'tell_parents_our_capabilities'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'tell_parents_our_capacities'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'periodic_task'
op|'.'
name|'periodic_task'
newline|'\n'
DECL|member|_heal_instances
name|'def'
name|'_heal_instances'
op|'('
name|'self'
op|','
name|'ctxt'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Periodic task to send updates for a number of instances to\n        parent cells.\n\n        On every run of the periodic task, we will attempt to sync\n        \'CONF.cells.instance_update_num_instances\' number of instances.\n        When we get the list of instances, we shuffle them so that multiple\n        nova-cells services aren\'t attempting to sync the same instances\n        in lockstep.\n\n        If CONF.cells.instance_update_at_threshold is set, only attempt\n        to sync instances that have been updated recently.  The CONF\n        setting defines the maximum number of seconds old the updated_at\n        can be.  Ie, a threshold of 3600 means to only update instances\n        that have modified in the last hour.\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'state_manager'
op|'.'
name|'get_parent_cells'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# No need to sync up if we have no parents.'
nl|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'info'
op|'='
op|'{'
string|"'updated_list'"
op|':'
name|'False'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|_next_instance
name|'def'
name|'_next_instance'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'='
name|'self'
op|'.'
name|'instances_to_heal'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'StopIteration'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'info'
op|'['
string|"'updated_list'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'return'
newline|'\n'
dedent|''
name|'threshold'
op|'='
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'instance_updated_at_threshold'
newline|'\n'
name|'updated_since'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'threshold'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                    '
name|'updated_since'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'-'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
nl|'\n'
name|'seconds'
op|'='
name|'threshold'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'instances_to_heal'
op|'='
name|'cells_utils'
op|'.'
name|'get_instances_to_sync'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'updated_since'
op|'='
name|'updated_since'
op|','
name|'shuffle'
op|'='
name|'True'
op|','
nl|'\n'
name|'uuids_only'
op|'='
name|'True'
op|')'
newline|'\n'
name|'info'
op|'['
string|"'updated_list'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'instance'
op|'='
name|'self'
op|'.'
name|'instances_to_heal'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'StopIteration'
op|':'
newline|'\n'
indent|'                    '
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
dedent|''
name|'rd_context'
op|'='
name|'ctxt'
op|'.'
name|'elevated'
op|'('
name|'read_deleted'
op|'='
string|"'yes'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'instance_update_num_instances'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'while'
name|'True'
op|':'
newline|'\n'
comment|'# Yield to other greenthreads'
nl|'\n'
indent|'                '
name|'time'
op|'.'
name|'sleep'
op|'('
number|'0'
op|')'
newline|'\n'
name|'instance_uuid'
op|'='
name|'_next_instance'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance_uuid'
op|':'
newline|'\n'
indent|'                    '
name|'return'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'instance'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'rd_context'
op|','
nl|'\n'
name|'instance_uuid'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_sync_instance'
op|'('
name|'ctxt'
op|','
name|'instance'
op|')'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
DECL|member|_sync_instance
dedent|''
dedent|''
dedent|''
name|'def'
name|'_sync_instance'
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
string|'"""Broadcast an instance_update or instance_destroy message up to\n        parent cells.\n        """'
newline|'\n'
name|'if'
name|'instance'
op|'['
string|"'deleted'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'instance_destroy_at_top'
op|'('
name|'ctxt'
op|','
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'instance_update_at_top'
op|'('
name|'ctxt'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_run_instance
dedent|''
dedent|''
name|'def'
name|'schedule_run_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'host_sched_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Pick a cell (possibly ourselves) to build new instance(s)\n        and forward the request accordingly.\n        """'
newline|'\n'
comment|'# Target is ourselves first.'
nl|'\n'
name|'our_cell'
op|'='
name|'self'
op|'.'
name|'state_manager'
op|'.'
name|'get_my_state'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'schedule_run_instance'
op|'('
name|'ctxt'
op|','
name|'our_cell'
op|','
nl|'\n'
name|'host_sched_kwargs'
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
name|'build_inst_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Pick a cell (possibly ourselves) to build new instance(s) and\n        forward the request accordingly.\n        """'
newline|'\n'
comment|'# Target is ourselves first.'
nl|'\n'
name|'our_cell'
op|'='
name|'self'
op|'.'
name|'state_manager'
op|'.'
name|'get_my_state'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'build_instances'
op|'('
name|'ctxt'
op|','
name|'our_cell'
op|','
name|'build_inst_kwargs'
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
name|'_ctxt'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return cell information for our neighbor cells."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'state_manager'
op|'.'
name|'get_cell_info_for_neighbors'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|run_compute_api_method
dedent|''
name|'def'
name|'run_compute_api_method'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'cell_name'
op|','
name|'method_info'
op|','
name|'call'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call a compute API method in a specific cell."""'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'run_compute_api_method'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'cell_name'
op|','
nl|'\n'
name|'method_info'
op|','
nl|'\n'
name|'call'
op|')'
newline|'\n'
name|'if'
name|'call'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'response'
op|'.'
name|'value_or_raise'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_update_at_top
dedent|''
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
string|'"""Update an instance at the top level cell."""'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'instance_update_at_top'
op|'('
name|'ctxt'
op|','
name|'instance'
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
string|'"""Destroy an instance at the top level cell."""'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'instance_destroy_at_top'
op|'('
name|'ctxt'
op|','
name|'instance'
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
string|'"""This is used by API cell when it didn\'t know what cell\n        an instance was in, but the instance was requested to be\n        deleted or soft_deleted.  So, we\'ll broadcast this everywhere.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'instance_delete_everywhere'
op|'('
name|'ctxt'
op|','
name|'instance'
op|','
nl|'\n'
name|'delete_type'
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
string|'"""Create an instance fault at the top level cell."""'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'instance_fault_create_at_top'
op|'('
name|'ctxt'
op|','
name|'instance_fault'
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
name|'bw_update_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update bandwidth usage at top level cell."""'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'bw_usage_update_at_top'
op|'('
name|'ctxt'
op|','
name|'bw_update_info'
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
op|','
name|'updated_since'
op|','
name|'deleted'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Force a sync of all instances, potentially by project_id,\n        and potentially since a certain date/time.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'sync_instances'
op|'('
name|'ctxt'
op|','
name|'project_id'
op|','
name|'updated_since'
op|','
nl|'\n'
name|'deleted'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return services in this cell and in all child cells."""'
newline|'\n'
name|'responses'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'service_get_all'
op|'('
name|'ctxt'
op|','
name|'filters'
op|')'
newline|'\n'
name|'ret_services'
op|'='
op|'['
op|']'
newline|'\n'
comment|'# 1 response per cell.  Each response is a list of services.'
nl|'\n'
name|'for'
name|'response'
name|'in'
name|'responses'
op|':'
newline|'\n'
indent|'            '
name|'services'
op|'='
name|'response'
op|'.'
name|'value_or_raise'
op|'('
op|')'
newline|'\n'
name|'for'
name|'service'
name|'in'
name|'services'
op|':'
newline|'\n'
indent|'                '
name|'cells_utils'
op|'.'
name|'add_cell_to_service'
op|'('
name|'service'
op|','
name|'response'
op|'.'
name|'cell_name'
op|')'
newline|'\n'
name|'ret_services'
op|'.'
name|'append'
op|'('
name|'service'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'ret_services'
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
string|'"""Return a service entry for a compute host in a certain cell."""'
newline|'\n'
name|'cell_name'
op|','
name|'host_name'
op|'='
name|'cells_utils'
op|'.'
name|'split_cell_and_item'
op|'('
name|'host_name'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'cell_name'
op|','
nl|'\n'
name|'host_name'
op|')'
newline|'\n'
name|'service'
op|'='
name|'response'
op|'.'
name|'value_or_raise'
op|'('
op|')'
newline|'\n'
name|'cells_utils'
op|'.'
name|'add_cell_to_service'
op|'('
name|'service'
op|','
name|'response'
op|'.'
name|'cell_name'
op|')'
newline|'\n'
name|'return'
name|'service'
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
string|'"""\n        Used to enable/disable a service. For compute services, setting to\n        disabled stops new builds arriving on that host.\n\n        :param host_name: the name of the host machine that the service is\n                          running\n        :param binary: The name of the executable that the service runs as\n        :param params_to_update: eg. {\'disabled\': True}\n        :returns: the service reference\n        """'
newline|'\n'
name|'cell_name'
op|','
name|'host_name'
op|'='
name|'cells_utils'
op|'.'
name|'split_cell_and_item'
op|'('
name|'host_name'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'service_update'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'cell_name'
op|','
name|'host_name'
op|','
name|'binary'
op|','
name|'params_to_update'
op|')'
newline|'\n'
name|'service'
op|'='
name|'response'
op|'.'
name|'value_or_raise'
op|'('
op|')'
newline|'\n'
name|'cells_utils'
op|'.'
name|'add_cell_to_service'
op|'('
name|'service'
op|','
name|'response'
op|'.'
name|'cell_name'
op|')'
newline|'\n'
name|'return'
name|'service'
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
name|'topic'
op|','
name|'rpc_message'
op|','
name|'call'
op|','
name|'timeout'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Proxy an RPC message as-is to a manager."""'
newline|'\n'
name|'compute_topic'
op|'='
name|'CONF'
op|'.'
name|'compute_topic'
newline|'\n'
name|'cell_and_host'
op|'='
name|'topic'
op|'['
name|'len'
op|'('
name|'compute_topic'
op|')'
op|'+'
number|'1'
op|':'
op|']'
newline|'\n'
name|'cell_name'
op|','
name|'host_name'
op|'='
name|'cells_utils'
op|'.'
name|'split_cell_and_item'
op|'('
name|'cell_and_host'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'proxy_rpc_to_manager'
op|'('
name|'ctxt'
op|','
name|'cell_name'
op|','
nl|'\n'
name|'host_name'
op|','
name|'topic'
op|','
name|'rpc_message'
op|','
name|'call'
op|','
name|'timeout'
op|')'
newline|'\n'
name|'return'
name|'response'
op|'.'
name|'value_or_raise'
op|'('
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
string|'"""Get task logs from the DB from all cells or a particular\n        cell.\n\n        If \'host\' is not None, host will be of the format \'cell!name@host\',\n        with \'@host\' being optional.  The query will be directed to the\n        appropriate cell and return all task logs, or task logs matching\n        the host if specified.\n\n        \'state\' also may be None.  If it\'s not, filter by the state as well.\n        """'
newline|'\n'
name|'if'
name|'host'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'cell_name'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'cell_name'
op|','
name|'host'
op|'='
name|'cells_utils'
op|'.'
name|'split_cell_and_item'
op|'('
name|'host'
op|')'
newline|'\n'
comment|'# If no cell name was given, assume that the host name is the'
nl|'\n'
comment|'# cell_name and that the target is all hosts'
nl|'\n'
name|'if'
name|'cell_name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'cell_name'
op|','
name|'host'
op|'='
name|'host'
op|','
name|'cell_name'
newline|'\n'
dedent|''
dedent|''
name|'responses'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'task_log_get_all'
op|'('
name|'ctxt'
op|','
name|'cell_name'
op|','
nl|'\n'
name|'task_name'
op|','
name|'period_beginning'
op|','
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
newline|'\n'
comment|'# 1 response per cell.  Each response is a list of task log'
nl|'\n'
comment|'# entries.'
nl|'\n'
name|'ret_task_logs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'response'
name|'in'
name|'responses'
op|':'
newline|'\n'
indent|'            '
name|'task_logs'
op|'='
name|'response'
op|'.'
name|'value_or_raise'
op|'('
op|')'
newline|'\n'
name|'for'
name|'task_log'
name|'in'
name|'task_logs'
op|':'
newline|'\n'
indent|'                '
name|'cells_utils'
op|'.'
name|'add_cell_to_task_log'
op|'('
name|'task_log'
op|','
nl|'\n'
name|'response'
op|'.'
name|'cell_name'
op|')'
newline|'\n'
name|'ret_task_logs'
op|'.'
name|'append'
op|'('
name|'task_log'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'ret_task_logs'
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
name|'cell_name'
op|','
name|'compute_id'
op|'='
name|'cells_utils'
op|'.'
name|'split_cell_and_item'
op|'('
nl|'\n'
name|'compute_id'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'compute_node_get'
op|'('
name|'ctxt'
op|','
name|'cell_name'
op|','
nl|'\n'
name|'compute_id'
op|')'
newline|'\n'
name|'node'
op|'='
name|'response'
op|'.'
name|'value_or_raise'
op|'('
op|')'
newline|'\n'
name|'cells_utils'
op|'.'
name|'add_cell_to_compute_node'
op|'('
name|'node'
op|','
name|'cell_name'
op|')'
newline|'\n'
name|'return'
name|'node'
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
string|'"""Return list of compute nodes in all cells."""'
newline|'\n'
name|'responses'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'compute_node_get_all'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'hypervisor_match'
op|'='
name|'hypervisor_match'
op|')'
newline|'\n'
comment|'# 1 response per cell.  Each response is a list of compute_node'
nl|'\n'
comment|'# entries.'
nl|'\n'
name|'ret_nodes'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'response'
name|'in'
name|'responses'
op|':'
newline|'\n'
indent|'            '
name|'nodes'
op|'='
name|'response'
op|'.'
name|'value_or_raise'
op|'('
op|')'
newline|'\n'
name|'for'
name|'node'
name|'in'
name|'nodes'
op|':'
newline|'\n'
indent|'                '
name|'cells_utils'
op|'.'
name|'add_cell_to_compute_node'
op|'('
name|'node'
op|','
nl|'\n'
name|'response'
op|'.'
name|'cell_name'
op|')'
newline|'\n'
name|'ret_nodes'
op|'.'
name|'append'
op|'('
name|'node'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'ret_nodes'
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
string|'"""Return compute node stats totals from all cells."""'
newline|'\n'
name|'responses'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'compute_node_stats'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'totals'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'response'
name|'in'
name|'responses'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'='
name|'response'
op|'.'
name|'value_or_raise'
op|'('
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'val'
name|'in'
name|'data'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'totals'
op|'.'
name|'setdefault'
op|'('
name|'key'
op|','
number|'0'
op|')'
newline|'\n'
name|'totals'
op|'['
name|'key'
op|']'
op|'+='
name|'val'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'totals'
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
name|'cell_name'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'actions_get'
op|'('
name|'ctxt'
op|','
name|'cell_name'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
name|'return'
name|'response'
op|'.'
name|'value_or_raise'
op|'('
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
name|'cell_name'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'request_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'action_get_by_request_id'
op|'('
name|'ctxt'
op|','
name|'cell_name'
op|','
nl|'\n'
name|'instance_uuid'
op|','
nl|'\n'
name|'request_id'
op|')'
newline|'\n'
name|'return'
name|'response'
op|'.'
name|'value_or_raise'
op|'('
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
name|'cell_name'
op|','
name|'action_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'action_events_get'
op|'('
name|'ctxt'
op|','
name|'cell_name'
op|','
nl|'\n'
name|'action_id'
op|')'
newline|'\n'
name|'return'
name|'response'
op|'.'
name|'value_or_raise'
op|'('
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
name|'msg_runner'
op|'.'
name|'consoleauth_delete_tokens'
op|'('
name|'ctxt'
op|','
name|'instance_uuid'
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
name|'instance'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
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
name|'instance_uuid'
op|')'
newline|'\n'
dedent|''
name|'response'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'validate_console_port'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'cell_name'"
op|']'
op|','
name|'instance_uuid'
op|','
name|'console_port'
op|','
nl|'\n'
name|'console_type'
op|')'
newline|'\n'
name|'return'
name|'response'
op|'.'
name|'value_or_raise'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
