begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 IBM'
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
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
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
name|'log'
name|'as'
name|'logging'
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
DECL|variable|deprecate_opts
name|'deprecate_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'fatal_deprecations'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'make deprecations fatal'"
op|')'
nl|'\n'
op|']'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'deprecate_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|warn
name|'def'
name|'warn'
op|'('
name|'msg'
op|'='
string|'""'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Warn of a deprecated config option that an operator has specified.\n    This should be added in the code where we\'ve made a change in how\n    we use some operator changeable parameter to indicate that it will\n    go away in a future version of OpenStack.\n    """'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Deprecated Config: %s"'
op|')'
op|'%'
name|'msg'
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fatal_deprecations'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'DeprecatedConfig'
op|'('
name|'msg'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
