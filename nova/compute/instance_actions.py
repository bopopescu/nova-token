begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 OpenStack Foundation'
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
string|'"""Possible actions on an instance.\n\nActions should probably match a user intention at the API level.  Because they\ncan be user visible that should help to avoid confusion.  For that reason they\ntend to maintain the casing sent to the API.\n\nMaintaining a list of actions here should protect against inconsistencies when\nthey are used.\n"""'
newline|'\n'
nl|'\n'
DECL|variable|CREATE
name|'CREATE'
op|'='
string|"'create'"
newline|'\n'
DECL|variable|DELETE
name|'DELETE'
op|'='
string|"'delete'"
newline|'\n'
DECL|variable|EVACUATE
name|'EVACUATE'
op|'='
string|"'evacuate'"
newline|'\n'
DECL|variable|RESTORE
name|'RESTORE'
op|'='
string|"'restore'"
newline|'\n'
DECL|variable|STOP
name|'STOP'
op|'='
string|"'stop'"
newline|'\n'
DECL|variable|START
name|'START'
op|'='
string|"'start'"
newline|'\n'
DECL|variable|REBOOT
name|'REBOOT'
op|'='
string|"'reboot'"
newline|'\n'
DECL|variable|REBUILD
name|'REBUILD'
op|'='
string|"'rebuild'"
newline|'\n'
DECL|variable|REVERT_RESIZE
name|'REVERT_RESIZE'
op|'='
string|"'revertResize'"
newline|'\n'
DECL|variable|CONFIRM_RESIZE
name|'CONFIRM_RESIZE'
op|'='
string|"'confirmResize'"
newline|'\n'
DECL|variable|RESIZE
name|'RESIZE'
op|'='
string|"'resize'"
newline|'\n'
DECL|variable|PAUSE
name|'PAUSE'
op|'='
string|"'pause'"
newline|'\n'
DECL|variable|UNPAUSE
name|'UNPAUSE'
op|'='
string|"'unpause'"
newline|'\n'
DECL|variable|SUSPEND
name|'SUSPEND'
op|'='
string|"'suspend'"
newline|'\n'
DECL|variable|RESUME
name|'RESUME'
op|'='
string|"'resume'"
newline|'\n'
DECL|variable|RESCUE
name|'RESCUE'
op|'='
string|"'rescue'"
newline|'\n'
DECL|variable|UNRESCUE
name|'UNRESCUE'
op|'='
string|"'unrescue'"
newline|'\n'
DECL|variable|CHANGE_PASSWORD
name|'CHANGE_PASSWORD'
op|'='
string|"'changePassword'"
newline|'\n'
DECL|variable|SHELVE
name|'SHELVE'
op|'='
string|"'shelve'"
newline|'\n'
DECL|variable|UNSHELVE
name|'UNSHELVE'
op|'='
string|"'unshelve'"
newline|'\n'
endmarker|''
end_unit
