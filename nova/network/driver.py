begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Red Hat, Inc.'
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
name|'sys'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|driver_opts
name|'driver_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'network_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.network.linux_net'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Driver to use for network creation'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'driver_opts'
op|')'
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
nl|'\n'
DECL|function|load_network_driver
name|'def'
name|'load_network_driver'
op|'('
name|'network_driver'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'network_driver'
op|':'
newline|'\n'
indent|'        '
name|'network_driver'
op|'='
name|'CONF'
op|'.'
name|'network_driver'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'network_driver'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Network driver option required, but not specified"'
op|')'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Loading network driver \'%s\'"'
op|')'
op|'%'
name|'network_driver'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'importutils'
op|'.'
name|'import_module'
op|'('
name|'network_driver'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
