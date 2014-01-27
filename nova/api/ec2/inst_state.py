begin_unit
comment|'# Copyright 2011 Isaku Yamahata <yamahata at valinux co jp>'
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
DECL|variable|PENDING_CODE
name|'PENDING_CODE'
op|'='
number|'0'
newline|'\n'
DECL|variable|RUNNING_CODE
name|'RUNNING_CODE'
op|'='
number|'16'
newline|'\n'
DECL|variable|SHUTTING_DOWN_CODE
name|'SHUTTING_DOWN_CODE'
op|'='
number|'32'
newline|'\n'
DECL|variable|TERMINATED_CODE
name|'TERMINATED_CODE'
op|'='
number|'48'
newline|'\n'
DECL|variable|STOPPING_CODE
name|'STOPPING_CODE'
op|'='
number|'64'
newline|'\n'
DECL|variable|STOPPED_CODE
name|'STOPPED_CODE'
op|'='
number|'80'
newline|'\n'
nl|'\n'
DECL|variable|PENDING
name|'PENDING'
op|'='
string|"'pending'"
newline|'\n'
DECL|variable|RUNNING
name|'RUNNING'
op|'='
string|"'running'"
newline|'\n'
DECL|variable|SHUTTING_DOWN
name|'SHUTTING_DOWN'
op|'='
string|"'shutting-down'"
newline|'\n'
DECL|variable|TERMINATED
name|'TERMINATED'
op|'='
string|"'terminated'"
newline|'\n'
DECL|variable|STOPPING
name|'STOPPING'
op|'='
string|"'stopping'"
newline|'\n'
DECL|variable|STOPPED
name|'STOPPED'
op|'='
string|"'stopped'"
newline|'\n'
nl|'\n'
comment|'# non-ec2 value'
nl|'\n'
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
nl|'\n'
comment|'# EC2 API instance status code'
nl|'\n'
DECL|variable|_NAME_TO_CODE
name|'_NAME_TO_CODE'
op|'='
op|'{'
nl|'\n'
name|'PENDING'
op|':'
name|'PENDING_CODE'
op|','
nl|'\n'
name|'RUNNING'
op|':'
name|'RUNNING_CODE'
op|','
nl|'\n'
name|'SHUTTING_DOWN'
op|':'
name|'SHUTTING_DOWN_CODE'
op|','
nl|'\n'
name|'TERMINATED'
op|':'
name|'TERMINATED_CODE'
op|','
nl|'\n'
name|'STOPPING'
op|':'
name|'STOPPING_CODE'
op|','
nl|'\n'
name|'STOPPED'
op|':'
name|'STOPPED_CODE'
op|','
nl|'\n'
nl|'\n'
comment|'# approximation'
nl|'\n'
name|'MIGRATE'
op|':'
name|'RUNNING_CODE'
op|','
nl|'\n'
name|'RESIZE'
op|':'
name|'RUNNING_CODE'
op|','
nl|'\n'
name|'PAUSE'
op|':'
name|'STOPPED_CODE'
op|','
nl|'\n'
name|'SUSPEND'
op|':'
name|'STOPPED_CODE'
op|','
nl|'\n'
name|'RESCUE'
op|':'
name|'RUNNING_CODE'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|name_to_code
name|'def'
name|'name_to_code'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_NAME_TO_CODE'
op|'.'
name|'get'
op|'('
name|'name'
op|','
name|'PENDING_CODE'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
