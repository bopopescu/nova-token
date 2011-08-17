begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
string|'"""Possible vm states for instances"""'
newline|'\n'
nl|'\n'
DECL|variable|ACTIVE
name|'ACTIVE'
op|'='
string|"'active'"
newline|'\n'
DECL|variable|BUILD
name|'BUILD'
op|'='
string|"'build'"
newline|'\n'
DECL|variable|REBUILD
name|'REBUILD'
op|'='
string|"'rebuild'"
newline|'\n'
DECL|variable|REBOOT
name|'REBOOT'
op|'='
string|"'reboot'"
newline|'\n'
DECL|variable|DELETE
name|'DELETE'
op|'='
string|"'delete'"
newline|'\n'
DECL|variable|STOP
name|'STOP'
op|'='
string|"'stop'"
newline|'\n'
DECL|variable|MIGRATE
name|'MIGRATE'
op|'='
string|"'migrate'"
newline|'\n'
DECL|variable|RESIZE
name|'RESIZE'
op|'='
string|"'resize'"
newline|'\n'
DECL|variable|VERIFY_RESIZE
name|'VERIFY_RESIZE'
op|'='
string|"'verify_resize'"
newline|'\n'
DECL|variable|PAUSE
name|'PAUSE'
op|'='
string|"'pause'"
newline|'\n'
DECL|variable|SUSPEND
name|'SUSPEND'
op|'='
string|"'suspend'"
newline|'\n'
DECL|variable|RESCUE
name|'RESCUE'
op|'='
string|"'rescue'"
newline|'\n'
endmarker|''
end_unit
