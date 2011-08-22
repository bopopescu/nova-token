begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'exception'
name|'import'
name|'ClassNotFound'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_multistring'
op|'('
string|"'list_notifier_drivers'"
op|','
nl|'\n'
op|'['
string|"'nova.notifier.no_op_notifier'"
op|']'
op|','
nl|'\n'
string|"'List of drivers to send notifications'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.notifier.list_notifier'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|drivers
name|'drivers'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_drivers
name|'def'
name|'_get_drivers'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Instantiates and returns drivers based on the flag values."""'
newline|'\n'
name|'global'
name|'drivers'
newline|'\n'
name|'if'
name|'not'
name|'drivers'
op|':'
newline|'\n'
indent|'        '
name|'drivers'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'notification_driver'
name|'in'
name|'FLAGS'
op|'.'
name|'list_notifier_drivers'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'drivers'
op|'.'
name|'append'
op|'('
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'notification_driver'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ClassNotFound'
op|':'
newline|'\n'
indent|'                '
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'drivers'
newline|'\n'
nl|'\n'
DECL|function|notify
dedent|''
name|'def'
name|'notify'
op|'('
name|'message'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Passes notification to mulitple notifiers in a list."""'
newline|'\n'
name|'for'
name|'driver'
name|'in'
name|'_get_drivers'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'driver'
op|'.'
name|'notify'
op|'('
name|'message'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Problem \'%(e)s\' attempting to send to "'
nl|'\n'
string|'"notification driver %(driver)s."'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_reset_drivers
dedent|''
dedent|''
dedent|''
name|'def'
name|'_reset_drivers'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Used by unit tests to reset the drivers."""'
newline|'\n'
name|'global'
name|'drivers'
newline|'\n'
name|'drivers'
op|'='
name|'None'
newline|'\n'
dedent|''
endmarker|''
end_unit
