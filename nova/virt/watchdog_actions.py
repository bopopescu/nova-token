begin_unit
comment|'#    Copyright 2014 Red Hat, Inc'
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
string|'"""Describes and verifies the watchdog device actions."""'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# the values which may be passed to libvirt'
nl|'\n'
DECL|variable|RAW_WATCHDOG_ACTIONS
name|'RAW_WATCHDOG_ACTIONS'
op|'='
op|'['
string|"'poweroff'"
op|','
string|"'reset'"
op|','
string|"'pause'"
op|','
string|"'none'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_valid_watchdog_action
name|'def'
name|'is_valid_watchdog_action'
op|'('
name|'val'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check if the given value is a valid watchdog device parameter."""'
newline|'\n'
name|'return'
name|'val'
name|'in'
name|'RAW_WATCHDOG_ACTIONS'
newline|'\n'
dedent|''
endmarker|''
end_unit
