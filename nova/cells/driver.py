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
string|'"""\nBase Cells Communication Driver\n"""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseCellsDriver
name|'class'
name|'BaseCellsDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The base class for cells communication.\n\n    One instance of this class will be created for every neighbor cell\n    that we find in the DB and it will be associated with the cell in\n    its CellState.\n\n    One instance is also created by the cells manager for setting up\n    the consumers.\n    """'
newline|'\n'
DECL|member|start_consumers
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
string|'"""Start any consumers the driver may need."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop_consumers
dedent|''
name|'def'
name|'stop_consumers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stop consuming messages."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
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
string|'"""Send a message to a cell."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
