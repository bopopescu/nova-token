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
string|'"""\nCellState Manager\n"""'
newline|'\n'
name|'import'
name|'copy'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'functools'
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
name|'rpc_driver'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'fileutils'
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
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|cell_state_manager_opts
name|'cell_state_manager_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'db_check_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Seconds between getting fresh cell info from db.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cells_config'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Configuration file from which to read cells '"
nl|'\n'
string|"'configuration.  If given, overrides reading cells '"
nl|'\n'
string|"'from the database.'"
op|')'
op|','
nl|'\n'
op|']'
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
string|"'name'"
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
string|"'reserve_percent'"
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
string|"'mute_child_interval'"
op|','
string|"'nova.cells.opts'"
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
comment|"#CONF.import_opt('capabilities', 'nova.cells.opts', group='cells')"
nl|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'cell_state_manager_opts'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellState
name|'class'
name|'CellState'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Holds information for a particular cell."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'cell_name'
op|','
name|'is_me'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'name'
op|'='
name|'cell_name'
newline|'\n'
name|'self'
op|'.'
name|'is_me'
op|'='
name|'is_me'
newline|'\n'
name|'self'
op|'.'
name|'last_seen'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'min'
newline|'\n'
name|'self'
op|'.'
name|'capabilities'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'capacities'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'db_info'
op|'='
op|'{'
op|'}'
newline|'\n'
comment|'# TODO(comstud): The DB will specify the driver to use to talk'
nl|'\n'
comment|"# to this cell, but there's no column for this yet.  The only"
nl|'\n'
comment|'# available driver is the rpc driver.'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'='
name|'rpc_driver'
op|'.'
name|'CellsRPCDriver'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_db_info
dedent|''
name|'def'
name|'update_db_info'
op|'('
name|'self'
op|','
name|'cell_db_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update cell credentials from db."""'
newline|'\n'
name|'self'
op|'.'
name|'db_info'
op|'='
name|'dict'
op|'('
nl|'\n'
op|'['
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'cell_db_info'
op|'.'
name|'iteritems'
op|'('
op|')'
nl|'\n'
name|'if'
name|'k'
op|'!='
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_capabilities
dedent|''
name|'def'
name|'update_capabilities'
op|'('
name|'self'
op|','
name|'cell_metadata'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update cell capabilities for a cell."""'
newline|'\n'
name|'self'
op|'.'
name|'last_seen'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'capabilities'
op|'='
name|'cell_metadata'
newline|'\n'
nl|'\n'
DECL|member|update_capacities
dedent|''
name|'def'
name|'update_capacities'
op|'('
name|'self'
op|','
name|'capacities'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update capacity information for a cell."""'
newline|'\n'
name|'self'
op|'.'
name|'last_seen'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'capacities'
op|'='
name|'capacities'
newline|'\n'
nl|'\n'
DECL|member|get_cell_info
dedent|''
name|'def'
name|'get_cell_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return subset of cell information for OS API use."""'
newline|'\n'
name|'db_fields_to_return'
op|'='
op|'['
string|"'is_parent'"
op|','
string|"'weight_scale'"
op|','
string|"'weight_offset'"
op|']'
newline|'\n'
name|'url_fields_to_return'
op|'='
op|'{'
nl|'\n'
string|"'username'"
op|':'
string|"'username'"
op|','
nl|'\n'
string|"'hostname'"
op|':'
string|"'rpc_host'"
op|','
nl|'\n'
string|"'port'"
op|':'
string|"'rpc_port'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'cell_info'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
name|'self'
op|'.'
name|'name'
op|','
name|'capabilities'
op|'='
name|'self'
op|'.'
name|'capabilities'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'db_info'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'field'
name|'in'
name|'db_fields_to_return'
op|':'
newline|'\n'
indent|'                '
name|'cell_info'
op|'['
name|'field'
op|']'
op|'='
name|'self'
op|'.'
name|'db_info'
op|'['
name|'field'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'url_info'
op|'='
name|'rpc_driver'
op|'.'
name|'parse_transport_url'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'db_info'
op|'['
string|"'transport_url'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'field'
op|','
name|'canonical'
name|'in'
name|'url_fields_to_return'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'cell_info'
op|'['
name|'canonical'
op|']'
op|'='
name|'url_info'
op|'['
name|'field'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'cell_info'
newline|'\n'
nl|'\n'
DECL|member|send_message
dedent|''
name|'def'
name|'send_message'
op|'('
name|'self'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Send a message to a cell.  Just forward this to the driver,\n        passing ourselves and the message as arguments.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'send_message_to_cell'
op|'('
name|'self'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'me'
op|'='
string|'"me"'
name|'if'
name|'self'
op|'.'
name|'is_me'
name|'else'
string|'"not_me"'
newline|'\n'
name|'return'
string|'"Cell \'%s\' (%s)"'
op|'%'
op|'('
name|'self'
op|'.'
name|'name'
op|','
name|'me'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|sync_before
dedent|''
dedent|''
name|'def'
name|'sync_before'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Use as a decorator to wrap methods that use cell information to\n    make sure they sync the latest information from the DB periodically.\n    """'
newline|'\n'
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'f'
op|')'
newline|'\n'
DECL|function|wrapper
name|'def'
name|'wrapper'
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
name|'self'
op|'.'
name|'_cell_data_sync'
op|'('
op|')'
newline|'\n'
name|'return'
name|'f'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|sync_after
dedent|''
name|'def'
name|'sync_after'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Use as a decorator to wrap methods that update cell information\n    in the database to make sure the data is synchronized immediately.\n    """'
newline|'\n'
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'f'
op|')'
newline|'\n'
DECL|function|wrapper
name|'def'
name|'wrapper'
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
name|'result'
op|'='
name|'f'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_cell_data_sync'
op|'('
name|'force'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_unset
dedent|''
name|'_unset'
op|'='
name|'object'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellStateManager
name|'class'
name|'CellStateManager'
op|'('
name|'base'
op|'.'
name|'Base'
op|')'
op|':'
newline|'\n'
DECL|member|__new__
indent|'    '
name|'def'
name|'__new__'
op|'('
name|'cls'
op|','
name|'cell_state_cls'
op|'='
name|'None'
op|','
name|'cells_config'
op|'='
name|'_unset'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'cls'
name|'is'
name|'not'
name|'CellStateManager'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'super'
op|'('
name|'CellStateManager'
op|','
name|'cls'
op|')'
op|'.'
name|'__new__'
op|'('
name|'cls'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'cells_config'
name|'is'
name|'_unset'
op|':'
newline|'\n'
indent|'            '
name|'cells_config'
op|'='
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'cells_config'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'cells_config'
op|':'
newline|'\n'
indent|'            '
name|'config_path'
op|'='
name|'CONF'
op|'.'
name|'find_file'
op|'('
name|'cells_config'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'config_path'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'cfg'
op|'.'
name|'ConfigFilesNotFoundError'
op|'('
name|'config_files'
op|'='
op|'['
name|'cells_config'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'CellStateManagerFile'
op|'('
name|'cell_state_cls'
op|','
name|'config_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'CellStateManagerDB'
op|'('
name|'cell_state_cls'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'cell_state_cls'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'CellStateManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'cell_state_cls'
op|':'
newline|'\n'
indent|'            '
name|'cell_state_cls'
op|'='
name|'CellState'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'cell_state_cls'
op|'='
name|'cell_state_cls'
newline|'\n'
name|'self'
op|'.'
name|'my_cell_state'
op|'='
name|'cell_state_cls'
op|'('
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'name'
op|','
name|'is_me'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'parent_cells'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'child_cells'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'last_cell_db_check'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'min'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_cell_data_sync'
op|'('
name|'force'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'my_cell_capabs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'cap'
name|'in'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'capabilities'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|','
name|'value'
op|'='
name|'cap'
op|'.'
name|'split'
op|'('
string|"'='"
op|','
number|'1'
op|')'
newline|'\n'
name|'if'
string|"';'"
name|'in'
name|'value'
op|':'
newline|'\n'
indent|'                '
name|'values'
op|'='
name|'set'
op|'('
name|'value'
op|'.'
name|'split'
op|'('
string|"';'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'values'
op|'='
name|'set'
op|'('
op|'['
name|'value'
op|']'
op|')'
newline|'\n'
dedent|''
name|'my_cell_capabs'
op|'['
name|'name'
op|']'
op|'='
name|'values'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'my_cell_state'
op|'.'
name|'update_capabilities'
op|'('
name|'my_cell_capabs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_refresh_cells_from_dict
dedent|''
name|'def'
name|'_refresh_cells_from_dict'
op|'('
name|'self'
op|','
name|'db_cells_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make our cell info map match the db."""'
newline|'\n'
nl|'\n'
comment|'# Update current cells.  Delete ones that disappeared'
nl|'\n'
name|'for'
name|'cells_dict'
name|'in'
op|'('
name|'self'
op|'.'
name|'parent_cells'
op|','
name|'self'
op|'.'
name|'child_cells'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'cell_name'
op|','
name|'cell_info'
name|'in'
name|'cells_dict'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'is_parent'
op|'='
name|'cell_info'
op|'.'
name|'db_info'
op|'['
string|"'is_parent'"
op|']'
newline|'\n'
name|'db_dict'
op|'='
name|'db_cells_dict'
op|'.'
name|'get'
op|'('
name|'cell_name'
op|')'
newline|'\n'
name|'if'
name|'db_dict'
name|'and'
name|'is_parent'
op|'=='
name|'db_dict'
op|'['
string|"'is_parent'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'cell_info'
op|'.'
name|'update_db_info'
op|'('
name|'db_dict'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'del'
name|'cells_dict'
op|'['
name|'cell_name'
op|']'
newline|'\n'
nl|'\n'
comment|'# Add new cells'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'for'
name|'cell_name'
op|','
name|'db_info'
name|'in'
name|'db_cells_dict'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'db_info'
op|'['
string|"'is_parent'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'cells_dict'
op|'='
name|'self'
op|'.'
name|'parent_cells'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'cells_dict'
op|'='
name|'self'
op|'.'
name|'child_cells'
newline|'\n'
dedent|''
name|'if'
name|'cell_name'
name|'not'
name|'in'
name|'cells_dict'
op|':'
newline|'\n'
indent|'                '
name|'cells_dict'
op|'['
name|'cell_name'
op|']'
op|'='
name|'self'
op|'.'
name|'cell_state_cls'
op|'('
name|'cell_name'
op|')'
newline|'\n'
name|'cells_dict'
op|'['
name|'cell_name'
op|']'
op|'.'
name|'update_db_info'
op|'('
name|'db_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_time_to_sync
dedent|''
dedent|''
dedent|''
name|'def'
name|'_time_to_sync'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Is it time to sync the DB against our memory cache?"""'
newline|'\n'
name|'diff'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'-'
name|'self'
op|'.'
name|'last_cell_db_check'
newline|'\n'
name|'return'
name|'diff'
op|'.'
name|'seconds'
op|'>='
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'db_check_interval'
newline|'\n'
nl|'\n'
DECL|member|_update_our_capacity
dedent|''
name|'def'
name|'_update_our_capacity'
op|'('
name|'self'
op|','
name|'ctxt'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update our capacity in the self.my_cell_state CellState.\n\n        This will add/update 2 entries in our CellState.capacities,\n        \'ram_free\' and \'disk_free\'.\n\n        The values of these are both dictionaries with the following\n        format:\n\n        {\'total_mb\': <total_memory_free_in_the_cell>,\n         \'units_by_mb: <units_dictionary>}\n\n        <units_dictionary> contains the number of units that we can\n        build for every instance_type that we have.  This number is\n        computed by looking at room available on every compute_node.\n\n        Take the following instance_types as an example:\n\n        [{\'memory_mb\': 1024, \'root_gb\': 10, \'ephemeral_gb\': 100},\n         {\'memory_mb\': 2048, \'root_gb\': 20, \'ephemeral_gb\': 200}]\n\n        capacities[\'ram_free\'][\'units_by_mb\'] would contain the following:\n\n        {\'1024\': <number_of_instances_that_will_fit>,\n         \'2048\': <number_of_instances_that_will_fit>}\n\n        capacities[\'disk_free\'][\'units_by_mb\'] would contain the following:\n\n        {\'122880\': <number_of_instances_that_will_fit>,\n         \'225280\': <number_of_instances_that_will_fit>}\n\n        Units are in MB, so 122880 = (10 + 100) * 1024.\n\n        NOTE(comstud): Perhaps we should only report a single number\n        available per instance_type.\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'ctxt'
op|':'
newline|'\n'
indent|'            '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'reserve_level'
op|'='
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'reserve_percent'
op|'/'
number|'100.0'
newline|'\n'
name|'compute_hosts'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|_get_compute_hosts
name|'def'
name|'_get_compute_hosts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'compute_nodes'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'compute_node_get_all'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'for'
name|'compute'
name|'in'
name|'compute_nodes'
op|':'
newline|'\n'
indent|'                '
name|'service'
op|'='
name|'compute'
op|'['
string|"'service'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'service'
name|'or'
name|'service'
op|'['
string|"'disabled'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'host'
op|'='
name|'service'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'compute_hosts'
op|'['
name|'host'
op|']'
op|'='
op|'{'
nl|'\n'
string|"'free_ram_mb'"
op|':'
name|'compute'
op|'['
string|"'free_ram_mb'"
op|']'
op|','
nl|'\n'
string|"'free_disk_mb'"
op|':'
name|'compute'
op|'['
string|"'free_disk_gb'"
op|']'
op|'*'
number|'1024'
op|','
nl|'\n'
string|"'total_ram_mb'"
op|':'
name|'compute'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'total_disk_mb'"
op|':'
name|'compute'
op|'['
string|"'local_gb'"
op|']'
op|'*'
number|'1024'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'_get_compute_hosts'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'compute_hosts'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'my_cell_state'
op|'.'
name|'update_capacities'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'ram_mb_free_units'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'disk_mb_free_units'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'total_ram_mb_free'
op|'='
number|'0'
newline|'\n'
name|'total_disk_mb_free'
op|'='
number|'0'
newline|'\n'
nl|'\n'
DECL|function|_free_units
name|'def'
name|'_free_units'
op|'('
name|'total'
op|','
name|'free'
op|','
name|'per_inst'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'per_inst'
op|':'
newline|'\n'
indent|'                '
name|'min_free'
op|'='
name|'total'
op|'*'
name|'reserve_level'
newline|'\n'
name|'free'
op|'='
name|'max'
op|'('
number|'0'
op|','
name|'free'
op|'-'
name|'min_free'
op|')'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'free'
op|'/'
name|'per_inst'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
number|'0'
newline|'\n'
nl|'\n'
DECL|function|_update_from_values
dedent|''
dedent|''
name|'def'
name|'_update_from_values'
op|'('
name|'values'
op|','
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'memory_mb'
op|'='
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'disk_mb'
op|'='
op|'('
name|'instance_type'
op|'['
string|"'root_gb'"
op|']'
op|'+'
nl|'\n'
name|'instance_type'
op|'['
string|"'ephemeral_gb'"
op|']'
op|')'
op|'*'
number|'1024'
newline|'\n'
name|'ram_mb_free_units'
op|'.'
name|'setdefault'
op|'('
name|'str'
op|'('
name|'memory_mb'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
name|'disk_mb_free_units'
op|'.'
name|'setdefault'
op|'('
name|'str'
op|'('
name|'disk_mb'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
name|'ram_free_units'
op|'='
name|'_free_units'
op|'('
name|'compute_values'
op|'['
string|"'total_ram_mb'"
op|']'
op|','
nl|'\n'
name|'compute_values'
op|'['
string|"'free_ram_mb'"
op|']'
op|','
name|'memory_mb'
op|')'
newline|'\n'
name|'disk_free_units'
op|'='
name|'_free_units'
op|'('
name|'compute_values'
op|'['
string|"'total_disk_mb'"
op|']'
op|','
nl|'\n'
name|'compute_values'
op|'['
string|"'free_disk_mb'"
op|']'
op|','
name|'disk_mb'
op|')'
newline|'\n'
name|'ram_mb_free_units'
op|'['
name|'str'
op|'('
name|'memory_mb'
op|')'
op|']'
op|'+='
name|'ram_free_units'
newline|'\n'
name|'disk_mb_free_units'
op|'['
name|'str'
op|'('
name|'disk_mb'
op|')'
op|']'
op|'+='
name|'disk_free_units'
newline|'\n'
nl|'\n'
dedent|''
name|'instance_types'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'flavor_get_all'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'compute_values'
name|'in'
name|'compute_hosts'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'total_ram_mb_free'
op|'+='
name|'compute_values'
op|'['
string|"'free_ram_mb'"
op|']'
newline|'\n'
name|'total_disk_mb_free'
op|'+='
name|'compute_values'
op|'['
string|"'free_disk_mb'"
op|']'
newline|'\n'
name|'for'
name|'instance_type'
name|'in'
name|'instance_types'
op|':'
newline|'\n'
indent|'                '
name|'_update_from_values'
op|'('
name|'compute_values'
op|','
name|'instance_type'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'capacities'
op|'='
op|'{'
string|"'ram_free'"
op|':'
op|'{'
string|"'total_mb'"
op|':'
name|'total_ram_mb_free'
op|','
nl|'\n'
string|"'units_by_mb'"
op|':'
name|'ram_mb_free_units'
op|'}'
op|','
nl|'\n'
string|"'disk_free'"
op|':'
op|'{'
string|"'total_mb'"
op|':'
name|'total_disk_mb_free'
op|','
nl|'\n'
string|"'units_by_mb'"
op|':'
name|'disk_mb_free_units'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'my_cell_state'
op|'.'
name|'update_capacities'
op|'('
name|'capacities'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sync_before'
newline|'\n'
DECL|member|get_cell_info_for_neighbors
name|'def'
name|'get_cell_info_for_neighbors'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return cell information for all neighbor cells."""'
newline|'\n'
name|'cell_list'
op|'='
op|'['
name|'cell'
op|'.'
name|'get_cell_info'
op|'('
op|')'
nl|'\n'
name|'for'
name|'cell'
name|'in'
name|'self'
op|'.'
name|'child_cells'
op|'.'
name|'itervalues'
op|'('
op|')'
op|']'
newline|'\n'
name|'cell_list'
op|'.'
name|'extend'
op|'('
op|'['
name|'cell'
op|'.'
name|'get_cell_info'
op|'('
op|')'
nl|'\n'
name|'for'
name|'cell'
name|'in'
name|'self'
op|'.'
name|'parent_cells'
op|'.'
name|'itervalues'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
name|'cell_list'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sync_before'
newline|'\n'
DECL|member|get_my_state
name|'def'
name|'get_my_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return information for my (this) cell."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'my_cell_state'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sync_before'
newline|'\n'
DECL|member|get_child_cells
name|'def'
name|'get_child_cells'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return list of child cell_infos."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'child_cells'
op|'.'
name|'values'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sync_before'
newline|'\n'
DECL|member|get_parent_cells
name|'def'
name|'get_parent_cells'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return list of parent cell_infos."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'parent_cells'
op|'.'
name|'values'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sync_before'
newline|'\n'
DECL|member|get_parent_cell
name|'def'
name|'get_parent_cell'
op|'('
name|'self'
op|','
name|'cell_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'parent_cells'
op|'.'
name|'get'
op|'('
name|'cell_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sync_before'
newline|'\n'
DECL|member|get_child_cell
name|'def'
name|'get_child_cell'
op|'('
name|'self'
op|','
name|'cell_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'child_cells'
op|'.'
name|'get'
op|'('
name|'cell_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sync_before'
newline|'\n'
DECL|member|update_cell_capabilities
name|'def'
name|'update_cell_capabilities'
op|'('
name|'self'
op|','
name|'cell_name'
op|','
name|'capabilities'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update capabilities for a cell."""'
newline|'\n'
name|'cell'
op|'='
op|'('
name|'self'
op|'.'
name|'child_cells'
op|'.'
name|'get'
op|'('
name|'cell_name'
op|')'
name|'or'
nl|'\n'
name|'self'
op|'.'
name|'parent_cells'
op|'.'
name|'get'
op|'('
name|'cell_name'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'cell'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Unknown cell \'%(cell_name)s\' when trying to "'
nl|'\n'
string|'"update capabilities"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'cell_name'"
op|':'
name|'cell_name'
op|'}'
op|')'
newline|'\n'
name|'return'
newline|'\n'
comment|'# Make sure capabilities are sets.'
nl|'\n'
dedent|''
name|'for'
name|'capab_name'
op|','
name|'values'
name|'in'
name|'capabilities'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'capabilities'
op|'['
name|'capab_name'
op|']'
op|'='
name|'set'
op|'('
name|'values'
op|')'
newline|'\n'
dedent|''
name|'cell'
op|'.'
name|'update_capabilities'
op|'('
name|'capabilities'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sync_before'
newline|'\n'
DECL|member|update_cell_capacities
name|'def'
name|'update_cell_capacities'
op|'('
name|'self'
op|','
name|'cell_name'
op|','
name|'capacities'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update capacities for a cell."""'
newline|'\n'
name|'cell'
op|'='
op|'('
name|'self'
op|'.'
name|'child_cells'
op|'.'
name|'get'
op|'('
name|'cell_name'
op|')'
name|'or'
nl|'\n'
name|'self'
op|'.'
name|'parent_cells'
op|'.'
name|'get'
op|'('
name|'cell_name'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'cell'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Unknown cell \'%(cell_name)s\' when trying to "'
nl|'\n'
string|'"update capacities"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'cell_name'"
op|':'
name|'cell_name'
op|'}'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'cell'
op|'.'
name|'update_capacities'
op|'('
name|'capacities'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sync_before'
newline|'\n'
DECL|member|get_our_capabilities
name|'def'
name|'get_our_capabilities'
op|'('
name|'self'
op|','
name|'include_children'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'capabs'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'my_cell_state'
op|'.'
name|'capabilities'
op|')'
newline|'\n'
name|'if'
name|'include_children'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'cell'
name|'in'
name|'self'
op|'.'
name|'child_cells'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'timeutils'
op|'.'
name|'is_older_than'
op|'('
name|'cell'
op|'.'
name|'last_seen'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'mute_child_interval'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'for'
name|'capab_name'
op|','
name|'values'
name|'in'
name|'cell'
op|'.'
name|'capabilities'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'capab_name'
name|'not'
name|'in'
name|'capabs'
op|':'
newline|'\n'
indent|'                        '
name|'capabs'
op|'['
name|'capab_name'
op|']'
op|'='
name|'set'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
dedent|''
name|'capabs'
op|'['
name|'capab_name'
op|']'
op|'|='
name|'values'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'capabs'
newline|'\n'
nl|'\n'
DECL|member|_add_to_dict
dedent|''
name|'def'
name|'_add_to_dict'
op|'('
name|'self'
op|','
name|'target'
op|','
name|'src'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'src'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'target'
op|'.'
name|'setdefault'
op|'('
name|'key'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_to_dict'
op|'('
name|'target'
op|'['
name|'key'
op|']'
op|','
name|'value'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'target'
op|'.'
name|'setdefault'
op|'('
name|'key'
op|','
number|'0'
op|')'
newline|'\n'
name|'target'
op|'['
name|'key'
op|']'
op|'+='
name|'value'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'sync_before'
newline|'\n'
DECL|member|get_our_capacities
name|'def'
name|'get_our_capacities'
op|'('
name|'self'
op|','
name|'include_children'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'capacities'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'my_cell_state'
op|'.'
name|'capacities'
op|')'
newline|'\n'
name|'if'
name|'include_children'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'cell'
name|'in'
name|'self'
op|'.'
name|'child_cells'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_add_to_dict'
op|'('
name|'capacities'
op|','
name|'cell'
op|'.'
name|'capacities'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'capacities'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sync_before'
newline|'\n'
DECL|member|get_capacities
name|'def'
name|'get_capacities'
op|'('
name|'self'
op|','
name|'cell_name'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'cell_name'
name|'or'
name|'cell_name'
op|'=='
name|'self'
op|'.'
name|'my_cell_state'
op|'.'
name|'name'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'get_our_capacities'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'cell_name'
name|'in'
name|'self'
op|'.'
name|'child_cells'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'child_cells'
op|'['
name|'cell_name'
op|']'
op|'.'
name|'capacities'
newline|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'CellNotFound'
op|'('
name|'cell_name'
op|'='
name|'cell_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sync_before'
newline|'\n'
DECL|member|cell_get
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
name|'for'
name|'cells_dict'
name|'in'
op|'('
name|'self'
op|'.'
name|'parent_cells'
op|','
name|'self'
op|'.'
name|'child_cells'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'cell_name'
name|'in'
name|'cells_dict'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'cells_dict'
op|'['
name|'cell_name'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'CellNotFound'
op|'('
name|'cell_name'
op|'='
name|'cell_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellStateManagerDB
dedent|''
dedent|''
name|'class'
name|'CellStateManagerDB'
op|'('
name|'CellStateManager'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'cell-db-sync'"
op|')'
newline|'\n'
DECL|member|_cell_data_sync
name|'def'
name|'_cell_data_sync'
op|'('
name|'self'
op|','
name|'force'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Update cell status for all cells from the backing data store\n        when necessary.\n\n        :param force: If True, cell status will be updated regardless\n                      of whether it\'s time to do so.\n        """'
newline|'\n'
name|'if'
name|'force'
name|'or'
name|'self'
op|'.'
name|'_time_to_sync'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Updating cell cache from db."'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'last_cell_db_check'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
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
name|'db_cells'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'cell_get_all'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'db_cells_dict'
op|'='
name|'dict'
op|'('
op|'('
name|'cell'
op|'['
string|"'name'"
op|']'
op|','
name|'cell'
op|')'
name|'for'
name|'cell'
name|'in'
name|'db_cells'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_refresh_cells_from_dict'
op|'('
name|'db_cells_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_update_our_capacity'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'sync_after'
newline|'\n'
DECL|member|cell_create
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
name|'db'
op|'.'
name|'cell_create'
op|'('
name|'ctxt'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sync_after'
newline|'\n'
DECL|member|cell_update
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
name|'db'
op|'.'
name|'cell_update'
op|'('
name|'ctxt'
op|','
name|'cell_name'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'sync_after'
newline|'\n'
DECL|member|cell_delete
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
name|'db'
op|'.'
name|'cell_delete'
op|'('
name|'ctxt'
op|','
name|'cell_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellStateManagerFile
dedent|''
dedent|''
name|'class'
name|'CellStateManagerFile'
op|'('
name|'CellStateManager'
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
name|'cell_state_cls'
op|','
name|'cells_config_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cells_config_path'
op|'='
name|'cells_config_path'
newline|'\n'
name|'super'
op|'('
name|'CellStateManagerFile'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'cell_state_cls'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_cell_data_sync
dedent|''
name|'def'
name|'_cell_data_sync'
op|'('
name|'self'
op|','
name|'force'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Update cell status for all cells from the backing data store\n        when necessary.\n\n        :param force: If True, cell status will be updated regardless\n                      of whether it\'s time to do so.\n        """'
newline|'\n'
name|'reloaded'
op|','
name|'data'
op|'='
name|'fileutils'
op|'.'
name|'read_cached_file'
op|'('
name|'self'
op|'.'
name|'cells_config_path'
op|','
nl|'\n'
name|'force_reload'
op|'='
name|'force'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'reloaded'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Updating cell cache from config file."'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cells_config_data'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_refresh_cells_from_dict'
op|'('
name|'self'
op|'.'
name|'cells_config_data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'force'
name|'or'
name|'self'
op|'.'
name|'_time_to_sync'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'last_cell_db_check'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_update_our_capacity'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|cell_create
dedent|''
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
name|'raise'
name|'exception'
op|'.'
name|'CellsUpdateProhibited'
op|'('
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
name|'raise'
name|'exception'
op|'.'
name|'CellsUpdateProhibited'
op|'('
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
name|'raise'
name|'exception'
op|'.'
name|'CellsUpdateProhibited'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
