begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack Foundation'
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
string|'"""Possible vm states for instances.\n\nCompute instance vm states represent the state of an instance as it pertains to\na user or administrator.\n\nvm_state describes a VM\'s current stable (not transition) state. That is, if\nthere is no ongoing compute API calls (running tasks), vm_state should reflect\nwhat the customer expect the VM to be. When combined with task states\n(task_states.py), a better picture can be formed regarding the instance\'s\nhealth and progress.\n\nSee http://wiki.openstack.org/VMState\n"""'
newline|'\n'
nl|'\n'
DECL|variable|ACTIVE
name|'ACTIVE'
op|'='
string|"'active'"
comment|'# VM is running'
newline|'\n'
DECL|variable|BUILDING
name|'BUILDING'
op|'='
string|"'building'"
comment|'# VM only exists in DB'
newline|'\n'
DECL|variable|PAUSED
name|'PAUSED'
op|'='
string|"'paused'"
newline|'\n'
DECL|variable|SUSPENDED
name|'SUSPENDED'
op|'='
string|"'suspended'"
comment|'# VM is suspended to disk.'
newline|'\n'
DECL|variable|STOPPED
name|'STOPPED'
op|'='
string|"'stopped'"
comment|'# VM is powered off, the disk image is still there.'
newline|'\n'
DECL|variable|RESCUED
name|'RESCUED'
op|'='
string|"'rescued'"
comment|'# A rescue image is running with the original VM image'
newline|'\n'
comment|'# attached.'
nl|'\n'
DECL|variable|RESIZED
name|'RESIZED'
op|'='
string|"'resized'"
comment|'# a VM with the new size is active. The user is expected'
newline|'\n'
comment|'# to manually confirm or revert.'
nl|'\n'
nl|'\n'
DECL|variable|SOFT_DELETED
name|'SOFT_DELETED'
op|'='
string|"'soft-delete'"
comment|'# VM is marked as deleted but the disk images are'
newline|'\n'
comment|'# still available to restore.'
nl|'\n'
DECL|variable|DELETED
name|'DELETED'
op|'='
string|"'deleted'"
comment|'# VM is permanently deleted.'
newline|'\n'
nl|'\n'
DECL|variable|ERROR
name|'ERROR'
op|'='
string|"'error'"
newline|'\n'
nl|'\n'
DECL|variable|SHELVED
name|'SHELVED'
op|'='
string|"'shelved'"
comment|'# VM is powered off, resources still on hypervisor'
newline|'\n'
DECL|variable|SHELVED_OFFLOADED
name|'SHELVED_OFFLOADED'
op|'='
string|"'shelved_offloaded'"
comment|'# VM and associated resources are'
newline|'\n'
comment|'# not on hypervisor'
nl|'\n'
endmarker|''
end_unit
