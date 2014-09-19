begin_unit
comment|'# Copyright (c) 2013 Intel, Inc.'
nl|'\n'
comment|'# Copyright (c) 2013 OpenStack Foundation'
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
name|'collections'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LW'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
name|'from'
name|'nova'
op|'.'
name|'pci'
name|'import'
name|'device'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'pci'
name|'import'
name|'stats'
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
nl|'\n'
DECL|class|PciDevTracker
name|'class'
name|'PciDevTracker'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Manage pci devices in a compute node.\n\n    This class fetches pci passthrough information from hypervisor\n    and trackes the usage of these devices.\n\n    It\'s called by compute node resource tracker to allocate and free\n    devices to/from instances, and to update the available pci passthrough\n    devices information from hypervisor periodically. The devices\n    information is updated to DB when devices information is changed.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'node_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a pci device tracker.\n\n        If a node_id is passed in, it will fetch pci devices information\n        from database, otherwise, it will create an empty devices list\n        and the resource tracker will update the node_id information later.\n        """'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'PciDevTracker'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stale'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'node_id'
op|'='
name|'node_id'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'='
name|'stats'
op|'.'
name|'PciDeviceStats'
op|'('
op|')'
newline|'\n'
name|'if'
name|'node_id'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'pci_devs'
op|'='
name|'list'
op|'('
nl|'\n'
name|'objects'
op|'.'
name|'PciDeviceList'
op|'.'
name|'get_by_compute_node'
op|'('
name|'context'
op|','
name|'node_id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'pci_devs'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_initial_instance_usage'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_initial_instance_usage
dedent|''
name|'def'
name|'_initial_instance_usage'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'allocations'
op|'='
name|'collections'
op|'.'
name|'defaultdict'
op|'('
name|'list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'claims'
op|'='
name|'collections'
op|'.'
name|'defaultdict'
op|'('
name|'list'
op|')'
newline|'\n'
name|'for'
name|'dev'
name|'in'
name|'self'
op|'.'
name|'pci_devs'
op|':'
newline|'\n'
indent|'            '
name|'uuid'
op|'='
name|'dev'
op|'['
string|"'instance_uuid'"
op|']'
newline|'\n'
name|'if'
name|'dev'
op|'['
string|"'status'"
op|']'
op|'=='
string|"'claimed'"
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'claims'
op|'['
name|'uuid'
op|']'
op|'.'
name|'append'
op|'('
name|'dev'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'dev'
op|'['
string|"'status'"
op|']'
op|'=='
string|"'allocated'"
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'allocations'
op|'['
name|'uuid'
op|']'
op|'.'
name|'append'
op|'('
name|'dev'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'dev'
op|'['
string|"'status'"
op|']'
op|'=='
string|"'available'"
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'stats'
op|'.'
name|'add_device'
op|'('
name|'dev'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|all_devs
name|'def'
name|'all_devs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'pci_devs'
newline|'\n'
nl|'\n'
DECL|member|save
dedent|''
name|'def'
name|'save'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'dev'
name|'in'
name|'self'
op|'.'
name|'pci_devs'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'dev'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'dev'
op|'.'
name|'save'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'pci_devs'
op|'='
op|'['
name|'dev'
name|'for'
name|'dev'
name|'in'
name|'self'
op|'.'
name|'pci_devs'
nl|'\n'
name|'if'
name|'dev'
op|'['
string|"'status'"
op|']'
op|'!='
string|"'deleted'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|pci_stats
name|'def'
name|'pci_stats'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'stats'
newline|'\n'
nl|'\n'
DECL|member|set_hvdevs
dedent|''
name|'def'
name|'set_hvdevs'
op|'('
name|'self'
op|','
name|'devices'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sync the pci device tracker with hypervisor information.\n\n        To support pci device hot plug, we sync with the hypervisor\n        periodically, fetching all devices information from hypervisor,\n        update the tracker and sync the DB information.\n\n        Devices should not be hot-plugged when assigned to a guest,\n        but possibly the hypervisor has no such guarantee. The best\n        we can do is to give a warning if a device is changed\n        or removed while assigned.\n        """'
newline|'\n'
nl|'\n'
name|'exist_addrs'
op|'='
name|'set'
op|'('
op|'['
name|'dev'
op|'['
string|"'address'"
op|']'
name|'for'
name|'dev'
name|'in'
name|'self'
op|'.'
name|'pci_devs'
op|']'
op|')'
newline|'\n'
name|'new_addrs'
op|'='
name|'set'
op|'('
op|'['
name|'dev'
op|'['
string|"'address'"
op|']'
name|'for'
name|'dev'
name|'in'
name|'devices'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'existed'
name|'in'
name|'self'
op|'.'
name|'pci_devs'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'existed'
op|'['
string|"'address'"
op|']'
name|'in'
name|'exist_addrs'
op|'-'
name|'new_addrs'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'device'
op|'.'
name|'remove'
op|'('
name|'existed'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'PciDeviceInvalidStatus'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Trying to remove device with %(status)s "'
nl|'\n'
string|'"ownership %(instance_uuid)s because of "'
nl|'\n'
string|'"%(pci_exception)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'status'"
op|':'
name|'existed'
op|'.'
name|'status'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'existed'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
string|"'pci_exception'"
op|':'
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|'}'
op|')'
newline|'\n'
comment|'# Note(yjiang5): remove the device by force so that'
nl|'\n'
comment|'# db entry is cleaned in next sync.'
nl|'\n'
name|'existed'
op|'.'
name|'status'
op|'='
string|"'removed'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Note(yjiang5): no need to update stats if an assigned'
nl|'\n'
comment|'# device is hot removed.'
nl|'\n'
indent|'                    '
name|'self'
op|'.'
name|'stats'
op|'.'
name|'remove_device'
op|'('
name|'existed'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'new_value'
op|'='
name|'next'
op|'('
op|'('
name|'dev'
name|'for'
name|'dev'
name|'in'
name|'devices'
name|'if'
nl|'\n'
name|'dev'
op|'['
string|"'address'"
op|']'
op|'=='
name|'existed'
op|'['
string|"'address'"
op|']'
op|')'
op|')'
newline|'\n'
name|'new_value'
op|'['
string|"'compute_node_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'node_id'
newline|'\n'
name|'if'
name|'existed'
op|'['
string|"'status'"
op|']'
name|'in'
op|'('
string|"'claimed'"
op|','
string|"'allocated'"
op|')'
op|':'
newline|'\n'
comment|'# Pci properties may change while assigned because of'
nl|'\n'
comment|'# hotplug or config changes. Although normally this should'
nl|'\n'
comment|'# not happen.'
nl|'\n'
nl|'\n'
comment|'# As the devices have been assigned to a instance, we defer'
nl|'\n'
comment|'# the change till the instance is destroyed. We will'
nl|'\n'
comment|'# not sync the new properties with database before that.'
nl|'\n'
nl|'\n'
comment|'# TODO(yjiang5): Not sure if this is a right policy, but'
nl|'\n'
comment|'# at least it avoids some confusion and, if needed,'
nl|'\n'
comment|'# we can add more action like killing the instance'
nl|'\n'
comment|'# by force in future.'
nl|'\n'
indent|'                    '
name|'self'
op|'.'
name|'stale'
op|'['
name|'new_value'
op|'['
string|"'address'"
op|']'
op|']'
op|'='
name|'new_value'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'device'
op|'.'
name|'update_device'
op|'('
name|'existed'
op|','
name|'new_value'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'for'
name|'dev'
name|'in'
op|'['
name|'dev'
name|'for'
name|'dev'
name|'in'
name|'devices'
name|'if'
nl|'\n'
name|'dev'
op|'['
string|"'address'"
op|']'
name|'in'
name|'new_addrs'
op|'-'
name|'exist_addrs'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'['
string|"'compute_node_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'node_id'
newline|'\n'
name|'dev_obj'
op|'='
name|'objects'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_devs'
op|'.'
name|'append'
op|'('
name|'dev_obj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'add_device'
op|'('
name|'dev_obj'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_claim_instance
dedent|''
dedent|''
name|'def'
name|'_claim_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'prefix'
op|'='
string|"''"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_requests'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequests'
op|'.'
name|'get_by_instance'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'pci_requests'
op|'.'
name|'requests'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'devs'
op|'='
name|'self'
op|'.'
name|'stats'
op|'.'
name|'consume_requests'
op|'('
name|'pci_requests'
op|'.'
name|'requests'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'devs'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceRequestFailed'
op|'('
name|'pci_requests'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'dev'
name|'in'
name|'devs'
op|':'
newline|'\n'
indent|'            '
name|'device'
op|'.'
name|'claim'
op|'('
name|'dev'
op|','
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'devs'
newline|'\n'
nl|'\n'
DECL|member|_allocate_instance
dedent|''
name|'def'
name|'_allocate_instance'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'devs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'dev'
name|'in'
name|'devs'
op|':'
newline|'\n'
indent|'            '
name|'device'
op|'.'
name|'allocate'
op|'('
name|'dev'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_free_device
dedent|''
dedent|''
name|'def'
name|'_free_device'
op|'('
name|'self'
op|','
name|'dev'
op|','
name|'instance'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'device'
op|'.'
name|'free'
op|'('
name|'dev'
op|','
name|'instance'
op|')'
newline|'\n'
name|'stale'
op|'='
name|'self'
op|'.'
name|'stale'
op|'.'
name|'pop'
op|'('
name|'dev'
op|'['
string|"'address'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'stale'
op|':'
newline|'\n'
indent|'            '
name|'device'
op|'.'
name|'update_device'
op|'('
name|'dev'
op|','
name|'stale'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stats'
op|'.'
name|'add_device'
op|'('
name|'dev'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_free_instance
dedent|''
name|'def'
name|'_free_instance'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
comment|'# Note(yjiang5): When a instance is resized, the devices in the'
nl|'\n'
comment|'# destination node are claimed to the instance in prep_resize stage.'
nl|'\n'
comment|'# However, the instance contains only allocated devices'
nl|'\n'
comment|"# information, not the claimed one. So we can't use"
nl|'\n'
comment|"# instance['pci_devices'] to check the devices to be freed."
nl|'\n'
indent|'        '
name|'for'
name|'dev'
name|'in'
name|'self'
op|'.'
name|'pci_devs'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'dev'
op|'['
string|"'status'"
op|']'
name|'in'
op|'('
string|"'claimed'"
op|','
string|"'allocated'"
op|')'
name|'and'
nl|'\n'
name|'dev'
op|'['
string|"'instance_uuid'"
op|']'
op|'=='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_free_device'
op|'('
name|'dev'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_pci_for_instance
dedent|''
dedent|''
dedent|''
name|'def'
name|'update_pci_for_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update instance\'s pci usage information.\n\n        The caller should hold the COMPUTE_RESOURCE_SEMAPHORE lock\n        """'
newline|'\n'
nl|'\n'
name|'uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'vm_state'
op|'='
name|'instance'
op|'['
string|"'vm_state'"
op|']'
newline|'\n'
name|'task_state'
op|'='
name|'instance'
op|'['
string|"'task_state'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'vm_state'
op|'=='
name|'vm_states'
op|'.'
name|'DELETED'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'allocations'
op|'.'
name|'pop'
op|'('
name|'uuid'
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_free_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'claims'
op|'.'
name|'pop'
op|'('
name|'uuid'
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_free_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'task_state'
op|'=='
name|'task_states'
op|'.'
name|'RESIZE_MIGRATED'
op|':'
newline|'\n'
indent|'            '
name|'devs'
op|'='
name|'self'
op|'.'
name|'allocations'
op|'.'
name|'pop'
op|'('
name|'uuid'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'devs'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_free_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'task_state'
op|'=='
name|'task_states'
op|'.'
name|'RESIZE_FINISH'
op|':'
newline|'\n'
indent|'            '
name|'devs'
op|'='
name|'self'
op|'.'
name|'claims'
op|'.'
name|'pop'
op|'('
name|'uuid'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'devs'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_allocate_instance'
op|'('
name|'instance'
op|','
name|'devs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'allocations'
op|'['
name|'uuid'
op|']'
op|'='
name|'devs'
newline|'\n'
dedent|''
dedent|''
name|'elif'
op|'('
name|'uuid'
name|'not'
name|'in'
name|'self'
op|'.'
name|'allocations'
name|'and'
nl|'\n'
name|'uuid'
name|'not'
name|'in'
name|'self'
op|'.'
name|'claims'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'devs'
op|'='
name|'self'
op|'.'
name|'_claim_instance'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'devs'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_allocate_instance'
op|'('
name|'instance'
op|','
name|'devs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'allocations'
op|'['
name|'uuid'
op|']'
op|'='
name|'devs'
newline|'\n'
nl|'\n'
DECL|member|update_pci_for_migration
dedent|''
dedent|''
dedent|''
name|'def'
name|'update_pci_for_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'sign'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update instance\'s pci usage information when it is migrated.\n\n        The caller should hold the COMPUTE_RESOURCE_SEMAPHORE lock.\n\n        :param sign: claim devices for instance when sign is 1, remove\n                     the claims when sign is -1\n        """'
newline|'\n'
name|'uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'if'
name|'sign'
op|'=='
number|'1'
name|'and'
name|'uuid'
name|'not'
name|'in'
name|'self'
op|'.'
name|'claims'
op|':'
newline|'\n'
indent|'            '
name|'devs'
op|'='
name|'self'
op|'.'
name|'_claim_instance'
op|'('
name|'context'
op|','
name|'instance'
op|','
string|"'new_'"
op|')'
newline|'\n'
name|'if'
name|'devs'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'claims'
op|'['
name|'uuid'
op|']'
op|'='
name|'devs'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'sign'
op|'=='
op|'-'
number|'1'
name|'and'
name|'uuid'
name|'in'
name|'self'
op|'.'
name|'claims'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_free_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|clean_usage
dedent|''
dedent|''
name|'def'
name|'clean_usage'
op|'('
name|'self'
op|','
name|'instances'
op|','
name|'migrations'
op|','
name|'orphans'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove all usages for instances not passed in the parameter.\n\n        The caller should hold the COMPUTE_RESOURCE_SEMAPHORE lock\n        """'
newline|'\n'
name|'existed'
op|'='
op|'['
name|'inst'
op|'['
string|"'uuid'"
op|']'
name|'for'
name|'inst'
name|'in'
name|'instances'
op|']'
newline|'\n'
name|'existed'
op|'+='
op|'['
name|'mig'
op|'['
string|"'instance_uuid'"
op|']'
name|'for'
name|'mig'
name|'in'
name|'migrations'
op|']'
newline|'\n'
name|'existed'
op|'+='
op|'['
name|'inst'
op|'['
string|"'uuid'"
op|']'
name|'for'
name|'inst'
name|'in'
name|'orphans'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'uuid'
name|'in'
name|'self'
op|'.'
name|'claims'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'uuid'
name|'not'
name|'in'
name|'existed'
op|':'
newline|'\n'
indent|'                '
name|'devs'
op|'='
name|'self'
op|'.'
name|'claims'
op|'.'
name|'pop'
op|'('
name|'uuid'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'for'
name|'dev'
name|'in'
name|'devs'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_free_device'
op|'('
name|'dev'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'for'
name|'uuid'
name|'in'
name|'self'
op|'.'
name|'allocations'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'uuid'
name|'not'
name|'in'
name|'existed'
op|':'
newline|'\n'
indent|'                '
name|'devs'
op|'='
name|'self'
op|'.'
name|'allocations'
op|'.'
name|'pop'
op|'('
name|'uuid'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'for'
name|'dev'
name|'in'
name|'devs'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_free_device'
op|'('
name|'dev'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_compute_node_id
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'set_compute_node_id'
op|'('
name|'self'
op|','
name|'node_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Set the compute node id that this object is tracking for.\n\n        In current resource tracker implementation, the\n        compute_node entry is created in the last step of\n        update_available_resoruces, thus we have to lazily set the\n        compute_node_id at that time.\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'node_id'
name|'and'
name|'self'
op|'.'
name|'node_id'
op|'!='
name|'node_id'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PciTrackerInvalidNodeId'
op|'('
name|'node_id'
op|'='
name|'self'
op|'.'
name|'node_id'
op|','
nl|'\n'
name|'new_node_id'
op|'='
name|'node_id'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'node_id'
op|'='
name|'node_id'
newline|'\n'
name|'for'
name|'dev'
name|'in'
name|'self'
op|'.'
name|'pci_devs'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'compute_node_id'
op|'='
name|'node_id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instance_pci_devs
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_instance_pci_devs'
op|'('
name|'inst'
op|','
name|'request_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the devices allocated to one or all requests for an instance.\n\n    - For generic PCI request, the request id is None.\n    - For sr-iov networking, the request id is a valid uuid\n    - There are a couple of cases where all the PCI devices allocated to an\n      instance need to be returned. Refer to libvirt driver that handles\n      soft_reboot and hard_boot of \'xen\' instances.\n    """'
newline|'\n'
name|'pci_devices'
op|'='
name|'inst'
op|'.'
name|'pci_devices'
newline|'\n'
name|'return'
op|'['
name|'device'
name|'for'
name|'device'
name|'in'
name|'pci_devices'
name|'if'
nl|'\n'
name|'device'
op|'.'
name|'request_id'
op|'=='
name|'request_id'
name|'or'
name|'request_id'
op|'=='
string|"'all'"
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
