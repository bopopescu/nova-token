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
string|'"""\nClient side of the console RPC API.\n"""'
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
name|'import'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rpc'
op|'.'
name|'proxy'
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
string|"'console_topic'"
op|','
string|"'nova.config'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleAPI
name|'class'
name|'ConsoleAPI'
op|'('
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rpc'
op|'.'
name|'proxy'
op|'.'
name|'RpcProxy'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Client side of the console rpc API.\n\n    API version history:\n\n        1.0 - Initial version.\n        1.1 - Added get_backdoor_port()\n    '''"
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
name|'console_topic'
newline|'\n'
name|'super'
op|'('
name|'ConsoleAPI'
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
DECL|member|add_console
dedent|''
name|'def'
name|'add_console'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_id'
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
string|"'add_console'"
op|','
name|'instance_id'
op|'='
name|'instance_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_console
dedent|''
name|'def'
name|'remove_console'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'console_id'
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
string|"'remove_console'"
op|','
name|'console_id'
op|'='
name|'console_id'
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
name|'version'
op|'='
string|"'1.1'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
