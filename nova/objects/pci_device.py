begin_unit
comment|'# Copyright 2013 Intel Corporation'
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
name|'copy'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'versionutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compare_pci_device_attributes
name|'def'
name|'compare_pci_device_attributes'
op|'('
name|'obj_a'
op|','
name|'obj_b'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pci_ignore_fields'
op|'='
name|'base'
op|'.'
name|'NovaPersistentObject'
op|'.'
name|'fields'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
name|'for'
name|'name'
name|'in'
name|'obj_a'
op|'.'
name|'obj_fields'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
name|'in'
name|'pci_ignore_fields'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'is_set_a'
op|'='
name|'obj_a'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'name'
op|')'
newline|'\n'
name|'is_set_b'
op|'='
name|'obj_b'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'name'
op|')'
newline|'\n'
name|'if'
name|'is_set_a'
op|'!='
name|'is_set_b'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'is_set_a'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'getattr'
op|'('
name|'obj_a'
op|','
name|'name'
op|')'
op|'!='
name|'getattr'
op|'('
name|'obj_b'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|PciDevice
name|'class'
name|'PciDevice'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Object to represent a PCI device on a compute node.\n\n    PCI devices are managed by the compute resource tracker, which discovers\n    the devices from the hardware platform, claims, allocates and frees\n    devices for instances.\n\n    The PCI device information is permanently maintained in a database.\n    This makes it convenient to get PCI device information, like physical\n    function for a VF device, adjacent switch IP address for a NIC,\n    hypervisor identification for a PCI device, etc. It also provides a\n    convenient way to check device allocation information for administrator\n    purposes.\n\n    A device can be in available/claimed/allocated/deleted/removed state.\n\n    A device is available when it is discovered..\n\n    A device is claimed prior to being allocated to an instance. Normally the\n    transition from claimed to allocated is quick. However, during a resize\n    operation the transition can take longer, because devices are claimed in\n    prep_resize and allocated in finish_resize.\n\n    A device becomes removed when hot removed from a node (i.e. not found in\n    the next auto-discover) but not yet synced with the DB. A removed device\n    should not be allocated to any instance, and once deleted from the DB,\n    the device object is changed to deleted state and no longer synced with\n    the DB.\n\n    Filed notes::\n\n        | \'dev_id\':\n        |   Hypervisor\'s identification for the device, the string format\n        |   is hypervisor specific\n        | \'extra_info\':\n        |   Device-specific properties like PF address, switch ip address etc.\n\n    """'
newline|'\n'
nl|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: String attributes updated to support unicode'
nl|'\n'
comment|'# Version 1.2: added request_id field'
nl|'\n'
comment|'# Version 1.3: Added field to represent PCI device NUMA node'
nl|'\n'
comment|'# Version 1.4: Added parent_addr field'
nl|'\n'
DECL|variable|VERSION
name|'VERSION'
op|'='
string|"'1.4'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
comment|'# Note(yjiang5): the compute_node_id may be None because the pci'
nl|'\n'
comment|'# device objects are created before the compute node is created in DB'
nl|'\n'
string|"'compute_node_id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'address'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'product_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'dev_type'"
op|':'
name|'fields'
op|'.'
name|'PciDeviceTypeField'
op|'('
op|')'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'fields'
op|'.'
name|'PciDeviceStatusField'
op|'('
op|')'
op|','
nl|'\n'
string|"'dev_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'label'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'request_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'extra_info'"
op|':'
name|'fields'
op|'.'
name|'DictOfStringsField'
op|'('
op|')'
op|','
nl|'\n'
string|"'numa_node'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'parent_addr'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_migrate_parent_addr
name|'def'
name|'_migrate_parent_addr'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# NOTE(ndipanov): Only migrate parent_addr if all services are up to at'
nl|'\n'
comment|'# least version 4 - this should only ever be called from save()'
nl|'\n'
indent|'        '
name|'services'
op|'='
op|'('
string|"'conductor'"
op|','
string|"'api'"
op|')'
newline|'\n'
name|'min_parent_addr_version'
op|'='
number|'4'
newline|'\n'
nl|'\n'
name|'min_deployed'
op|'='
name|'min'
op|'('
name|'objects'
op|'.'
name|'Service'
op|'.'
name|'get_minimum_version'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
string|"'nova-'"
op|'+'
name|'service'
op|')'
nl|'\n'
name|'for'
name|'service'
name|'in'
name|'services'
op|')'
newline|'\n'
name|'return'
name|'min_deployed'
op|'>='
name|'min_parent_addr_version'
newline|'\n'
nl|'\n'
DECL|member|obj_make_compatible
dedent|''
name|'def'
name|'obj_make_compatible'
op|'('
name|'self'
op|','
name|'primitive'
op|','
name|'target_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'target_version'
op|'='
name|'versionutils'
op|'.'
name|'convert_version_to_tuple'
op|'('
name|'target_version'
op|')'
newline|'\n'
name|'if'
name|'target_version'
op|'<'
op|'('
number|'1'
op|','
number|'2'
op|')'
name|'and'
string|"'request_id'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'primitive'
op|'['
string|"'request_id'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'target_version'
op|'<'
op|'('
number|'1'
op|','
number|'4'
op|')'
name|'and'
string|"'parent_addr'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'primitive'
op|'['
string|"'parent_addr'"
op|']'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'extra_info'
op|'='
name|'primitive'
op|'.'
name|'get'
op|'('
string|"'extra_info'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'extra_info'
op|'['
string|"'phys_function'"
op|']'
op|'='
name|'primitive'
op|'['
string|"'parent_addr'"
op|']'
newline|'\n'
dedent|''
name|'del'
name|'primitive'
op|'['
string|"'parent_addr'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|update_device
dedent|''
dedent|''
name|'def'
name|'update_device'
op|'('
name|'self'
op|','
name|'dev_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sync the content from device dictionary to device object.\n\n        The resource tracker updates the available devices periodically.\n        To avoid meaningless syncs with the database, we update the device\n        object only if a value changed.\n        """'
newline|'\n'
nl|'\n'
comment|'# Note(yjiang5): status/instance_uuid should only be updated by'
nl|'\n'
comment|'# functions like claim/allocate etc. The id is allocated by'
nl|'\n'
comment|'# database. The extra_info is created by the object.'
nl|'\n'
name|'no_changes'
op|'='
op|'('
string|"'status'"
op|','
string|"'instance_uuid'"
op|','
string|"'id'"
op|','
string|"'extra_info'"
op|')'
newline|'\n'
name|'map'
op|'('
name|'lambda'
name|'x'
op|':'
name|'dev_dict'
op|'.'
name|'pop'
op|'('
name|'x'
op|','
name|'None'
op|')'
op|','
nl|'\n'
op|'['
name|'key'
name|'for'
name|'key'
name|'in'
name|'no_changes'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'dev_dict'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'k'
name|'in'
name|'self'
op|'.'
name|'fields'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'setattr'
op|'('
name|'self'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Note (yjiang5) extra_info.update does not update'
nl|'\n'
comment|'# obj_what_changed, set it explicitly'
nl|'\n'
indent|'                '
name|'extra_info'
op|'='
name|'self'
op|'.'
name|'extra_info'
newline|'\n'
name|'extra_info'
op|'.'
name|'update'
op|'('
op|'{'
name|'k'
op|':'
name|'v'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'extra_info'
op|'='
name|'extra_info'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
dedent|''
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'PciDevice'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'extra_info'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__eq__
dedent|''
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'compare_pci_device_attributes'
op|'('
name|'self'
op|','
name|'other'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__ne__
dedent|''
name|'def'
name|'__ne__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'not'
op|'('
name|'self'
op|'=='
name|'other'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'pci_device'
op|','
name|'db_dev'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
name|'pci_device'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
op|'!='
string|"'extra_info'"
op|':'
newline|'\n'
indent|'                '
name|'setattr'
op|'('
name|'pci_device'
op|','
name|'key'
op|','
name|'db_dev'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'extra_info'
op|'='
name|'db_dev'
op|'.'
name|'get'
op|'('
string|'"extra_info"'
op|')'
newline|'\n'
name|'pci_device'
op|'.'
name|'extra_info'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'extra_info'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'pci_device'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'pci_device'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(ndipanov): As long as there is PF data in the old location, we'
nl|'\n'
comment|'# want to load it as it may have be the only place we have it'
nl|'\n'
name|'if'
string|"'phys_function'"
name|'in'
name|'pci_device'
op|'.'
name|'extra_info'
op|':'
newline|'\n'
indent|'            '
name|'pci_device'
op|'.'
name|'parent_addr'
op|'='
name|'pci_device'
op|'.'
name|'extra_info'
op|'['
string|"'phys_function'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'pci_device'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_dev_addr
name|'def'
name|'get_by_dev_addr'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'compute_node_id'
op|','
name|'dev_addr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_dev'
op|'='
name|'db'
op|'.'
name|'pci_device_get_by_addr'
op|'('
nl|'\n'
name|'context'
op|','
name|'compute_node_id'
op|','
name|'dev_addr'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_dev'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_dev_id
name|'def'
name|'get_by_dev_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_dev'
op|'='
name|'db'
op|'.'
name|'pci_device_get_by_id'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_dev'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'cls'
op|','
name|'dev_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a PCI device based on hypervisor information.\n\n        As the device object is just created and is not synced with db yet\n        thus we should not reset changes here for fields from dict.\n        """'
newline|'\n'
name|'pci_device'
op|'='
name|'cls'
op|'('
op|')'
newline|'\n'
name|'pci_device'
op|'.'
name|'update_device'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'pci_device'
op|'.'
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
newline|'\n'
name|'return'
name|'pci_device'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|save
name|'def'
name|'save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'status'
op|'=='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'REMOVED'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'DELETED'
newline|'\n'
name|'db'
op|'.'
name|'pci_device_destroy'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'compute_node_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'address'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'status'
op|'!='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'DELETED'
op|':'
newline|'\n'
indent|'            '
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_migrate_parent_addr'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# NOTE(ndipanov): If we are not migrating data yet, make sure'
nl|'\n'
comment|'# that any changes to parent_addr are also in the old location'
nl|'\n'
comment|'# in extra_info'
nl|'\n'
indent|'                '
name|'if'
string|"'parent_addr'"
name|'in'
name|'updates'
op|':'
newline|'\n'
indent|'                    '
name|'extra_update'
op|'='
name|'updates'
op|'.'
name|'get'
op|'('
string|"'extra_info'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'extra_update'
name|'and'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'extra_info'"
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'extra_update'
op|'='
name|'self'
op|'.'
name|'extra_info'
newline|'\n'
dedent|''
name|'extra_update'
op|'['
string|"'phys_function'"
op|']'
op|'='
name|'updates'
op|'['
string|"'parent_addr'"
op|']'
newline|'\n'
name|'updates'
op|'['
string|"'extra_info'"
op|']'
op|'='
name|'extra_update'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# NOTE(ndipanov): Once we start migrating, meaning all control'
nl|'\n'
comment|'# plane has been upgraded - aggressively migrate on every save'
nl|'\n'
indent|'                '
name|'pf_extra'
op|'='
name|'self'
op|'.'
name|'extra_info'
op|'.'
name|'pop'
op|'('
string|"'phys_function'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'pf_extra'
name|'and'
string|"'parent_addr'"
name|'not'
name|'in'
name|'updates'
op|':'
newline|'\n'
indent|'                    '
name|'updates'
op|'['
string|"'parent_addr'"
op|']'
op|'='
name|'pf_extra'
newline|'\n'
dedent|''
name|'updates'
op|'['
string|"'extra_info'"
op|']'
op|'='
name|'self'
op|'.'
name|'extra_info'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
string|"'extra_info'"
name|'in'
name|'updates'
op|':'
newline|'\n'
indent|'                '
name|'updates'
op|'['
string|"'extra_info'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'updates'
op|'['
string|"'extra_info'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'updates'
op|':'
newline|'\n'
indent|'                '
name|'db_pci'
op|'='
name|'db'
op|'.'
name|'pci_device_update'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'compute_node_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'address'
op|','
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
name|'db_pci'
op|')'
newline|'\n'
nl|'\n'
DECL|member|claim
dedent|''
dedent|''
dedent|''
name|'def'
name|'claim'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'status'
op|'!='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceInvalidStatus'
op|'('
nl|'\n'
name|'compute_node_id'
op|'='
name|'self'
op|'.'
name|'compute_node_id'
op|','
nl|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'address'
op|','
name|'status'
op|'='
name|'self'
op|'.'
name|'status'
op|','
nl|'\n'
name|'hopestatus'
op|'='
op|'['
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'CLAIMED'
newline|'\n'
name|'self'
op|'.'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|allocate
dedent|''
name|'def'
name|'allocate'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ok_statuses'
op|'='
op|'('
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'CLAIMED'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'status'
name|'not'
name|'in'
name|'ok_statuses'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceInvalidStatus'
op|'('
nl|'\n'
name|'compute_node_id'
op|'='
name|'self'
op|'.'
name|'compute_node_id'
op|','
nl|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'address'
op|','
name|'status'
op|'='
name|'self'
op|'.'
name|'status'
op|','
nl|'\n'
name|'hopestatus'
op|'='
name|'ok_statuses'
op|')'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'self'
op|'.'
name|'status'
op|'=='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'CLAIMED'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'instance_uuid'
op|'!='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceInvalidOwner'
op|'('
nl|'\n'
name|'compute_node_id'
op|'='
name|'self'
op|'.'
name|'compute_node_id'
op|','
nl|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'address'
op|','
name|'owner'
op|'='
name|'self'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
name|'hopeowner'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'ALLOCATED'
newline|'\n'
name|'self'
op|'.'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Notes(yjiang5): remove this check when instance object for'
nl|'\n'
comment|'# compute manager is finished'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'instance'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'pci_devices'"
name|'not'
name|'in'
name|'instance'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'['
string|"'pci_devices'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'instance'
op|'['
string|"'pci_devices'"
op|']'
op|'.'
name|'append'
op|'('
name|'copy'
op|'.'
name|'copy'
op|'('
name|'self'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'.'
name|'pci_devices'
op|'.'
name|'objects'
op|'.'
name|'append'
op|'('
name|'copy'
op|'.'
name|'copy'
op|'('
name|'self'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove
dedent|''
dedent|''
name|'def'
name|'remove'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'status'
op|'!='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceInvalidStatus'
op|'('
nl|'\n'
name|'compute_node_id'
op|'='
name|'self'
op|'.'
name|'compute_node_id'
op|','
nl|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'address'
op|','
name|'status'
op|'='
name|'self'
op|'.'
name|'status'
op|','
nl|'\n'
name|'hopestatus'
op|'='
op|'['
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'REMOVED'
newline|'\n'
name|'self'
op|'.'
name|'instance_uuid'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'request_id'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|free
dedent|''
name|'def'
name|'free'
op|'('
name|'self'
op|','
name|'instance'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ok_statuses'
op|'='
op|'('
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'ALLOCATED'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'CLAIMED'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'status'
name|'not'
name|'in'
name|'ok_statuses'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceInvalidStatus'
op|'('
nl|'\n'
name|'compute_node_id'
op|'='
name|'self'
op|'.'
name|'compute_node_id'
op|','
nl|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'address'
op|','
name|'status'
op|'='
name|'self'
op|'.'
name|'status'
op|','
nl|'\n'
name|'hopestatus'
op|'='
name|'ok_statuses'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'instance'
name|'and'
name|'self'
op|'.'
name|'instance_uuid'
op|'!='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceInvalidOwner'
op|'('
nl|'\n'
name|'compute_node_id'
op|'='
name|'self'
op|'.'
name|'compute_node_id'
op|','
nl|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'address'
op|','
name|'owner'
op|'='
name|'self'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
name|'hopeowner'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'old_status'
op|'='
name|'self'
op|'.'
name|'status'
newline|'\n'
name|'self'
op|'.'
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
newline|'\n'
name|'self'
op|'.'
name|'instance_uuid'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'request_id'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'old_status'
op|'=='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'ALLOCATED'
name|'and'
name|'instance'
op|':'
newline|'\n'
comment|'# Notes(yjiang5): remove this check when instance object for'
nl|'\n'
comment|'# compute manager is finished'
nl|'\n'
indent|'            '
name|'existed'
op|'='
name|'next'
op|'('
op|'('
name|'dev'
name|'for'
name|'dev'
name|'in'
name|'instance'
op|'['
string|"'pci_devices'"
op|']'
nl|'\n'
name|'if'
name|'dev'
op|'.'
name|'id'
op|'=='
name|'self'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'instance'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'['
string|"'pci_devices'"
op|']'
op|'.'
name|'remove'
op|'('
name|'existed'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'.'
name|'pci_devices'
op|'.'
name|'objects'
op|'.'
name|'remove'
op|'('
name|'existed'
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_available
dedent|''
dedent|''
dedent|''
name|'def'
name|'is_available'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'status'
op|'=='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|PciDeviceList
name|'class'
name|'PciDeviceList'
op|'('
name|'base'
op|'.'
name|'ObjectListBase'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'#              PciDevice <= 1.1'
nl|'\n'
comment|'# Version 1.1: PciDevice 1.2'
nl|'\n'
comment|'# Version 1.2: PciDevice 1.3'
nl|'\n'
comment|'# Version 1.3: Adds get_by_parent_address'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.3'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'PciDevice'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'PciDeviceList'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'objects'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_compute_node
name|'def'
name|'get_by_compute_node'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'node_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_dev_list'
op|'='
name|'db'
op|'.'
name|'pci_device_get_all_by_node'
op|'('
name|'context'
op|','
name|'node_id'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'PciDevice'
op|','
nl|'\n'
name|'db_dev_list'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_instance_uuid
name|'def'
name|'get_by_instance_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_dev_list'
op|'='
name|'db'
op|'.'
name|'pci_device_get_all_by_instance_uuid'
op|'('
name|'context'
op|','
name|'uuid'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'PciDevice'
op|','
nl|'\n'
name|'db_dev_list'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_parent_address
name|'def'
name|'get_by_parent_address'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'node_id'
op|','
name|'parent_addr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_dev_list'
op|'='
name|'db'
op|'.'
name|'pci_device_get_all_by_parent_addr'
op|'('
name|'context'
op|','
nl|'\n'
name|'node_id'
op|','
nl|'\n'
name|'parent_addr'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'PciDevice'
op|','
nl|'\n'
name|'db_dev_list'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
