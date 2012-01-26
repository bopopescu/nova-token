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
string|'"""Possible states for host aggregates.\n\nAn aggregate may be \'created\', in which case the admin has triggered its\ncreation, but the underlying hypervisor pool has not actually being set up\nyet. An aggregate may be \'changing\', meaning that the underlying hypervisor\npool is being setup. An aggregate may be \'active\', in which case the underlying\nhypervisor pool is up and running. An aggregate may be \'dismissed\' when it has\nno hosts and it has been deleted. An aggregate may be in \'error\' in all other\ncases.\nA \'created\' aggregate becomes \'changing\' during the first request of\nadding a host. During a \'changing\' status no other requests will be accepted;\nthis is to allow the hypervisor layer to instantiate the underlying pool\nwithout any potential race condition that may incur in master/slave-based\nconfigurations. The aggregate goes into the \'active\' state when the underlying\npool has been correctly instantiated.\nAll other operations (e.g. add/remove hosts) that succeed will keep the\naggregate in the \'active\' state. If a number of continuous requests fail,\nan \'active\' aggregate goes into an \'error\' state. To recover from such a state,\nadmin intervention is required. Currently an error state is irreversible,\nthat is, in order to recover from it an aggregate must be deleted.\n"""'
newline|'\n'
nl|'\n'
DECL|variable|CREATED
name|'CREATED'
op|'='
string|"'created'"
newline|'\n'
DECL|variable|CHANGING
name|'CHANGING'
op|'='
string|"'changing'"
newline|'\n'
DECL|variable|ACTIVE
name|'ACTIVE'
op|'='
string|"'active'"
newline|'\n'
DECL|variable|ERROR
name|'ERROR'
op|'='
string|"'error'"
newline|'\n'
DECL|variable|DISMISSED
name|'DISMISSED'
op|'='
string|"'dismissed'"
newline|'\n'
endmarker|''
end_unit
