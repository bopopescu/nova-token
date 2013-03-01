begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 IBM Corp.'
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
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
nl|'\n'
DECL|variable|POWERVM_NOSTATE
name|'POWERVM_NOSTATE'
op|'='
string|"''"
newline|'\n'
DECL|variable|POWERVM_RUNNING
name|'POWERVM_RUNNING'
op|'='
string|"'Running'"
newline|'\n'
DECL|variable|POWERVM_STARTING
name|'POWERVM_STARTING'
op|'='
string|"'Starting'"
newline|'\n'
DECL|variable|POWERVM_SHUTDOWN
name|'POWERVM_SHUTDOWN'
op|'='
string|"'Not Activated'"
newline|'\n'
DECL|variable|POWERVM_POWER_STATE
name|'POWERVM_POWER_STATE'
op|'='
op|'{'
nl|'\n'
name|'POWERVM_NOSTATE'
op|':'
name|'power_state'
op|'.'
name|'NOSTATE'
op|','
nl|'\n'
name|'POWERVM_RUNNING'
op|':'
name|'power_state'
op|'.'
name|'RUNNING'
op|','
nl|'\n'
name|'POWERVM_SHUTDOWN'
op|':'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|','
nl|'\n'
name|'POWERVM_STARTING'
op|':'
name|'power_state'
op|'.'
name|'RUNNING'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|POWERVM_CPU_INFO
name|'POWERVM_CPU_INFO'
op|'='
op|'('
string|"'ppc64'"
op|','
string|"'powervm'"
op|','
string|"'3940'"
op|')'
newline|'\n'
DECL|variable|POWERVM_HYPERVISOR_TYPE
name|'POWERVM_HYPERVISOR_TYPE'
op|'='
string|"'powervm'"
newline|'\n'
DECL|variable|POWERVM_HYPERVISOR_VERSION
name|'POWERVM_HYPERVISOR_VERSION'
op|'='
string|"'7.1'"
newline|'\n'
nl|'\n'
DECL|variable|POWERVM_MIN_ROOT_GB
name|'POWERVM_MIN_ROOT_GB'
op|'='
number|'10'
newline|'\n'
nl|'\n'
DECL|variable|POWERVM_MIN_MEM
name|'POWERVM_MIN_MEM'
op|'='
number|'512'
newline|'\n'
DECL|variable|POWERVM_MAX_MEM
name|'POWERVM_MAX_MEM'
op|'='
number|'1024'
newline|'\n'
DECL|variable|POWERVM_MAX_CPUS
name|'POWERVM_MAX_CPUS'
op|'='
number|'1'
newline|'\n'
DECL|variable|POWERVM_MIN_CPUS
name|'POWERVM_MIN_CPUS'
op|'='
number|'1'
newline|'\n'
endmarker|''
end_unit
