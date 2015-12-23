begin_unit
comment|'# Copyright (c) 2012 Rackspace Hosting'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright 2013 Red Hat, Inc.'
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
name|'import'
name|'oslo_messaging'
name|'as'
name|'messaging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'driver'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
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
name|'rpc_servers'
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
op|')'
newline|'\n'
nl|'\n'
DECL|member|start_servers
dedent|''
name|'def'
name|'start_servers'
op|'('
name|'self'
op|','
name|'msg_runner'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start RPC servers.\n\n        Start up 2 separate servers for handling inter-cell\n        communication via RPC.  Both handle the same types of\n        messages, but requests/replies are separated to solve\n        potential deadlocks. (If we used the same queue for both,\n        it\'s possible to exhaust the RPC thread pool while we wait\n        for replies.. such that we\'d never consume a reply.)\n        """'
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
name|'target'
op|'='
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'topic'
op|'='
string|"'%s.%s'"
op|'%'
op|'('
name|'topic_base'
op|','
name|'msg_type'
op|')'
op|','
nl|'\n'
name|'server'
op|'='
name|'CONF'
op|'.'
name|'host'
op|')'
newline|'\n'
comment|'# NOTE(comstud): We do not need to use the object serializer'
nl|'\n'
comment|'# on this because object serialization is taken care for us in'
nl|'\n'
comment|'# the nova.cells.messaging module.'
nl|'\n'
name|'server'
op|'='
name|'rpc'
op|'.'
name|'get_server'
op|'('
name|'target'
op|','
name|'endpoints'
op|'='
op|'['
name|'proxy_manager'
op|']'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rpc_servers'
op|'.'
name|'append'
op|'('
name|'server'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop_servers
dedent|''
dedent|''
name|'def'
name|'stop_servers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stop RPC servers.\n\n        NOTE: Currently there\'s no hooks when stopping services\n        to have managers cleanup, so this is not currently called.\n        """'
newline|'\n'
name|'for'
name|'server'
name|'in'
name|'self'
op|'.'
name|'rpc_servers'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'.'
name|'stop'
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
name|'object'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'InterCellRPCAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'version_cap'
op|'='
op|'('
nl|'\n'
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'transports'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_client
dedent|''
name|'def'
name|'_get_client'
op|'('
name|'self'
op|','
name|'next_hop'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Turn the DB information for a cell into a messaging.RPCClient."""'
newline|'\n'
name|'transport'
op|'='
name|'self'
op|'.'
name|'_get_transport'
op|'('
name|'next_hop'
op|')'
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
name|'serializer'
op|'='
name|'rpc'
op|'.'
name|'RequestContextSerializer'
op|'('
name|'None'
op|')'
newline|'\n'
name|'return'
name|'messaging'
op|'.'
name|'RPCClient'
op|'('
name|'transport'
op|','
nl|'\n'
name|'target'
op|','
nl|'\n'
name|'version_cap'
op|'='
name|'self'
op|'.'
name|'version_cap'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'serializer'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_transport
dedent|''
name|'def'
name|'_get_transport'
op|'('
name|'self'
op|','
name|'next_hop'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""NOTE(belliott) Each Transport object contains connection pool\n        state.  Maintain references to them to avoid continual reconnects\n        to the message broker.\n        """'
newline|'\n'
name|'transport_url'
op|'='
name|'next_hop'
op|'.'
name|'db_info'
op|'['
string|"'transport_url'"
op|']'
newline|'\n'
name|'if'
name|'transport_url'
name|'not'
name|'in'
name|'self'
op|'.'
name|'transports'
op|':'
newline|'\n'
indent|'            '
name|'transport'
op|'='
name|'messaging'
op|'.'
name|'get_transport'
op|'('
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
op|','
name|'transport_url'
op|','
nl|'\n'
name|'rpc'
op|'.'
name|'TRANSPORT_ALIASES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'transports'
op|'['
name|'transport_url'
op|']'
op|'='
name|'transport'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'transport'
op|'='
name|'self'
op|'.'
name|'transports'
op|'['
name|'transport_url'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'transport'
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
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'_get_client'
op|'('
name|'cell_state'
op|','
name|'topic'
op|')'
newline|'\n'
name|'if'
name|'message'
op|'.'
name|'fanout'
op|':'
newline|'\n'
indent|'            '
name|'cctxt'
op|'='
name|'cctxt'
op|'.'
name|'prepare'
op|'('
name|'fanout'
op|'='
name|'message'
op|'.'
name|'fanout'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cctxt'
op|'.'
name|'cast'
op|'('
name|'message'
op|'.'
name|'ctxt'
op|','
string|"'process_message'"
op|','
nl|'\n'
name|'message'
op|'='
name|'message'
op|'.'
name|'to_json'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InterCellRPCDispatcher
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
string|'"""RPC Dispatcher to handle messages received from other cells.\n\n    All messages received here have come from a sibling cell.  Depending\n    on the ultimate target and type of message, we may process the message\n    in this cell, relay the message to another sibling cell, or both.  This\n    logic is defined by the message class in the nova.cells.messaging module.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|target
name|'target'
op|'='
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'version'
op|'='
string|"'1.0'"
op|')'
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
