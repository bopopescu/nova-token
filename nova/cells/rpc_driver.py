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
string|'"""\nCells RPC Communication Driver\n"""'
newline|'\n'
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
name|'driver'
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
name|'dispatcher'
name|'as'
name|'rpc_dispatcher'
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
DECL|variable|cell_rpc_driver_opts
name|'cell_rpc_driver_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'rpc_driver_queue_base'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'cells.intercell'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Base queue name to use when communicating between "'
nl|'\n'
string|'"cells.  Various topics by message type will be "'
nl|'\n'
string|'"appended to this."'
op|')'
op|']'
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
name|'register_opts'
op|'('
name|'cell_rpc_driver_opts'
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
string|"'call_timeout'"
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
string|"'intercell'"
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
string|"'Set a version cap for messages sent between cells services'"
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
DECL|variable|_CELL_TO_CELL_RPC_API_VERSION
name|'_CELL_TO_CELL_RPC_API_VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellsRPCDriver
name|'class'
name|'CellsRPCDriver'
op|'('
name|'driver'
op|'.'
name|'BaseCellsDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Driver for cell<->cell communication via RPC.  This is used to\n    setup the RPC consumers as well as to send a message to another cell.\n\n    One instance of this class will be created for every neighbor cell\n    that we find in the DB and it will be associated with the cell in\n    its CellState.\n\n    One instance is also created by the cells manager for setting up\n    the consumers.\n    """'
newline|'\n'
DECL|variable|BASE_RPC_API_VERSION
name|'BASE_RPC_API_VERSION'
op|'='
name|'_CELL_TO_CELL_RPC_API_VERSION'
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
indent|'        '
name|'super'
op|'('
name|'CellsRPCDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rpc_connections'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'intercell_rpcapi'
op|'='
name|'InterCellRPCAPI'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'BASE_RPC_API_VERSION'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_start_consumer
dedent|''
name|'def'
name|'_start_consumer'
op|'('
name|'self'
op|','
name|'dispatcher'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start an RPC consumer."""'
newline|'\n'
name|'conn'
op|'='
name|'rpc'
op|'.'
name|'create_connection'
op|'('
name|'new'
op|'='
name|'True'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'create_consumer'
op|'('
name|'topic'
op|','
name|'dispatcher'
op|','
name|'fanout'
op|'='
name|'False'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'create_consumer'
op|'('
name|'topic'
op|','
name|'dispatcher'
op|','
name|'fanout'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rpc_connections'
op|'.'
name|'append'
op|'('
name|'conn'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'consume_in_thread'
op|'('
op|')'
newline|'\n'
name|'return'
name|'conn'
newline|'\n'
nl|'\n'
DECL|member|start_consumers
dedent|''
name|'def'
name|'start_consumers'
op|'('
name|'self'
op|','
name|'msg_runner'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start RPC consumers.\n\n        Start up 2 separate consumers for handling inter-cell\n        communication via RPC.  Both handle the same types of\n        messages, but requests/replies are separated to solve\n        potential deadlocks. (If we used the same queue for both,\n        it\'s possible to exhaust the RPC thread pool while we wait\n        for replies.. such that we\'d never consume a reply.)\n        """'
newline|'\n'
name|'topic_base'
op|'='
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'rpc_driver_queue_base'
newline|'\n'
name|'proxy_manager'
op|'='
name|'InterCellRPCDispatcher'
op|'('
name|'msg_runner'
op|')'
newline|'\n'
name|'dispatcher'
op|'='
name|'rpc_dispatcher'
op|'.'
name|'RpcDispatcher'
op|'('
op|'['
name|'proxy_manager'
op|']'
op|')'
newline|'\n'
name|'for'
name|'msg_type'
name|'in'
name|'msg_runner'
op|'.'
name|'get_message_types'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'topic'
op|'='
string|"'%s.%s'"
op|'%'
op|'('
name|'topic_base'
op|','
name|'msg_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_start_consumer'
op|'('
name|'dispatcher'
op|','
name|'topic'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop_consumers
dedent|''
dedent|''
name|'def'
name|'stop_consumers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stop RPC consumers.\n\n        NOTE: Currently there\'s no hooks when stopping services\n        to have managers cleanup, so this is not currently called.\n        """'
newline|'\n'
name|'for'
name|'conn'
name|'in'
name|'self'
op|'.'
name|'rpc_connections'
op|':'
newline|'\n'
indent|'            '
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|send_message_to_cell
dedent|''
dedent|''
name|'def'
name|'send_message_to_cell'
op|'('
name|'self'
op|','
name|'cell_state'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Use the IntercellRPCAPI to send a message to a cell."""'
newline|'\n'
name|'self'
op|'.'
name|'intercell_rpcapi'
op|'.'
name|'send_message_to_cell'
op|'('
name|'cell_state'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InterCellRPCAPI
dedent|''
dedent|''
name|'class'
name|'InterCellRPCAPI'
op|'('
name|'rpc_proxy'
op|'.'
name|'RpcProxy'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Client side of the Cell<->Cell RPC API.\n\n    The CellsRPCDriver uses this to make calls to another cell.\n\n    API version history:\n        1.0 - Initial version.\n\n        ... Grizzly supports message version 1.0.  So, any changes to existing\n        methods in 2.x after that point should be done such that they can\n        handle the version_cap being set to 1.0.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|VERSION_ALIASES
name|'VERSION_ALIASES'
op|'='
op|'{'
nl|'\n'
string|"'grizzly'"
op|':'
string|"'1.0'"
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
name|'default_version'
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
name|'intercell'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'intercell'
op|')'
newline|'\n'
name|'super'
op|'('
name|'InterCellRPCAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'None'
op|','
name|'default_version'
op|','
nl|'\n'
name|'version_cap'
op|'='
name|'version_cap'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_server_params_for_cell
name|'def'
name|'_get_server_params_for_cell'
op|'('
name|'next_hop'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Turn the DB information for a cell into the parameters\n        needed for the RPC call.\n        """'
newline|'\n'
name|'param_map'
op|'='
op|'{'
string|"'username'"
op|':'
string|"'username'"
op|','
nl|'\n'
string|"'password'"
op|':'
string|"'password'"
op|','
nl|'\n'
string|"'rpc_host'"
op|':'
string|"'hostname'"
op|','
nl|'\n'
string|"'rpc_port'"
op|':'
string|"'port'"
op|','
nl|'\n'
string|"'rpc_virtual_host'"
op|':'
string|"'virtual_host'"
op|'}'
newline|'\n'
name|'server_params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'source'
op|','
name|'target'
name|'in'
name|'param_map'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'next_hop'
op|'.'
name|'db_info'
op|'['
name|'source'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'server_params'
op|'['
name|'target'
op|']'
op|'='
name|'next_hop'
op|'.'
name|'db_info'
op|'['
name|'source'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'server_params'
newline|'\n'
nl|'\n'
DECL|member|send_message_to_cell
dedent|''
name|'def'
name|'send_message_to_cell'
op|'('
name|'self'
op|','
name|'cell_state'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Send a message to another cell by JSON-ifying the message and\n        making an RPC cast to \'process_message\'.  If the message says to\n        fanout, do it.  The topic that is used will be\n        \'CONF.rpc_driver_queue_base.<message_type>\'.\n        """'
newline|'\n'
name|'ctxt'
op|'='
name|'message'
op|'.'
name|'ctxt'
newline|'\n'
name|'json_message'
op|'='
name|'message'
op|'.'
name|'to_json'
op|'('
op|')'
newline|'\n'
name|'rpc_message'
op|'='
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'process_message'"
op|','
name|'message'
op|'='
name|'json_message'
op|')'
newline|'\n'
name|'topic_base'
op|'='
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'rpc_driver_queue_base'
newline|'\n'
name|'topic'
op|'='
string|"'%s.%s'"
op|'%'
op|'('
name|'topic_base'
op|','
name|'message'
op|'.'
name|'message_type'
op|')'
newline|'\n'
name|'server_params'
op|'='
name|'self'
op|'.'
name|'_get_server_params_for_cell'
op|'('
name|'cell_state'
op|')'
newline|'\n'
name|'if'
name|'message'
op|'.'
name|'fanout'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fanout_cast_to_server'
op|'('
name|'ctxt'
op|','
name|'server_params'
op|','
nl|'\n'
name|'rpc_message'
op|','
name|'topic'
op|'='
name|'topic'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'cast_to_server'
op|'('
name|'ctxt'
op|','
name|'server_params'
op|','
nl|'\n'
name|'rpc_message'
op|','
name|'topic'
op|'='
name|'topic'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InterCellRPCDispatcher
dedent|''
dedent|''
dedent|''
name|'class'
name|'InterCellRPCDispatcher'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""RPC Dispatcher to handle messages received from other cells.\n\n    All messages received here have come from a sibling cell.  Depending\n    on the ultimate target and type of message, we may process the message\n    in this cell, relay the message to another sibling cell, or both.  This\n    logic is defined by the message class in the messaging module.\n    """'
newline|'\n'
DECL|variable|BASE_RPC_API_VERSION
name|'BASE_RPC_API_VERSION'
op|'='
name|'_CELL_TO_CELL_RPC_API_VERSION'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'msg_runner'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Init the Intercell RPC Dispatcher."""'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'='
name|'msg_runner'
newline|'\n'
nl|'\n'
DECL|member|process_message
dedent|''
name|'def'
name|'process_message'
op|'('
name|'self'
op|','
name|'_ctxt'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""We received a message from another cell.  Use the MessageRunner\n        to turn this from JSON back into an instance of the correct\n        Message class.  Then process it!\n        """'
newline|'\n'
name|'message'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'message_from_json'
op|'('
name|'message'
op|')'
newline|'\n'
name|'message'
op|'.'
name|'process'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
