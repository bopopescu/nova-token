begin_unit
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
name|'functools'
newline|'\n'
name|'import'
name|'operator'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'block_device'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
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
name|'as'
name|'obj_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'excutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
name|'volume'
name|'import'
name|'encryptors'
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
DECL|class|_NotTransformable
name|'class'
name|'_NotTransformable'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_InvalidType
dedent|''
name|'class'
name|'_InvalidType'
op|'('
name|'_NotTransformable'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_NoLegacy
dedent|''
name|'class'
name|'_NoLegacy'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|update_db
dedent|''
name|'def'
name|'update_db'
op|'('
name|'method'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'method'
op|')'
newline|'\n'
DECL|function|wrapped
name|'def'
name|'wrapped'
op|'('
name|'obj'
op|','
name|'context'
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
name|'ret_val'
op|'='
name|'method'
op|'('
name|'obj'
op|','
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'save'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
name|'ret_val'
newline|'\n'
dedent|''
name|'return'
name|'wrapped'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DriverBlockDevice
dedent|''
name|'class'
name|'DriverBlockDevice'
op|'('
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A dict subclass that represents block devices used by the virt layer.\n\n    Uses block device objects internally to do the database access.\n\n    _fields and _legacy_fields class attributes present a set of fields that\n    are expected on a certain DriverBlockDevice type. We may have more legacy\n    versions in the future.\n\n    If an attribute access is attempted for a name that is found in the\n    _proxy_as_attr set, it will be proxied to the underlying object. This\n    allows us to access stuff that is not part of the data model that all\n    drivers understand.\n\n    The save() method allows us to update the database using the underlying\n    object. _update_on_save class attribute dictionary keeps the following\n    mapping:\n\n        {\'object field name\': \'driver dict field name (or None if same)\'}\n\n    These fields will be updated on the internal object, from the values in the\n    dict, before the actual database update is done.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|_fields
name|'_fields'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
DECL|variable|_legacy_fields
name|'_legacy_fields'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_proxy_as_attr
name|'_proxy_as_attr'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
DECL|variable|_update_on_save
name|'_update_on_save'
op|'='
op|'{'
string|"'disk_bus'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'device_name'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'device_type'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'bdm'
op|')'
op|':'
newline|'\n'
comment|'# TODO(ndipanov): Remove this check when we have all the rpc methods'
nl|'\n'
comment|'# use objects for block devices.'
nl|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'bdm'
op|','
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'_bdm_obj'"
op|']'
op|'='
name|'bdm'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'_bdm_obj'"
op|']'
op|'='
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'update'
op|'('
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|'('
name|'bdm'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'no_device'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'_NotTransformable'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'update'
op|'('
name|'dict'
op|'('
op|'('
name|'field'
op|','
name|'None'
op|')'
nl|'\n'
name|'for'
name|'field'
name|'in'
name|'self'
op|'.'
name|'_fields'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_transform'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
name|'in'
name|'self'
op|'.'
name|'_proxy_as_attr'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'_bdm_obj'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'super'
op|'('
name|'DriverBlockDevice'
op|','
name|'self'
op|')'
op|'.'
name|'__getattr__'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__setattr__
dedent|''
dedent|''
name|'def'
name|'__setattr__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
name|'in'
name|'self'
op|'.'
name|'_proxy_as_attr'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'setattr'
op|'('
name|'self'
op|'.'
name|'_bdm_obj'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'super'
op|'('
name|'DriverBlockDevice'
op|','
name|'self'
op|')'
op|'.'
name|'__setattr__'
op|'('
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_transform
dedent|''
dedent|''
name|'def'
name|'_transform'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Transform bdm to the format that is passed to drivers."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|legacy
dedent|''
name|'def'
name|'legacy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Basic legacy transformation.\n\n        Basic method will just drop the fields that are not in\n        _legacy_fields set. Override this in subclass if needed.\n        """'
newline|'\n'
name|'return'
name|'dict'
op|'('
op|'('
name|'key'
op|','
name|'self'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|')'
name|'for'
name|'key'
name|'in'
name|'self'
op|'.'
name|'_legacy_fields'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach
dedent|''
name|'def'
name|'attach'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make the device available to be used by VMs.\n\n        To be overridden in subclasses with the connecting logic for\n        the type of device the subclass represents.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
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
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'attr_name'
op|','
name|'key_name'
name|'in'
name|'self'
op|'.'
name|'_update_on_save'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|'.'
name|'_bdm_obj'
op|','
name|'attr_name'
op|','
name|'self'
op|'['
name|'key_name'
name|'or'
name|'attr_name'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'context'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'save'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DriverSwapBlockDevice
dedent|''
dedent|''
dedent|''
name|'class'
name|'DriverSwapBlockDevice'
op|'('
name|'DriverBlockDevice'
op|')'
op|':'
newline|'\n'
DECL|variable|_fields
indent|'    '
name|'_fields'
op|'='
name|'set'
op|'('
op|'['
string|"'device_name'"
op|','
string|"'swap_size'"
op|','
string|"'disk_bus'"
op|']'
op|')'
newline|'\n'
DECL|variable|_legacy_fields
name|'_legacy_fields'
op|'='
name|'_fields'
op|'-'
name|'set'
op|'('
op|'['
string|"'disk_bus'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_update_on_save
name|'_update_on_save'
op|'='
op|'{'
string|"'disk_bus'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'device_name'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_transform
name|'def'
name|'_transform'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'block_device'
op|'.'
name|'new_format_is_swap'
op|'('
name|'self'
op|'.'
name|'_bdm_obj'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'_InvalidType'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'update'
op|'('
op|'{'
nl|'\n'
string|"'device_name'"
op|':'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'device_name'
op|','
nl|'\n'
string|"'swap_size'"
op|':'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'volume_size'
name|'or'
number|'0'
op|','
nl|'\n'
string|"'disk_bus'"
op|':'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'disk_bus'
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DriverEphemeralBlockDevice
dedent|''
dedent|''
name|'class'
name|'DriverEphemeralBlockDevice'
op|'('
name|'DriverBlockDevice'
op|')'
op|':'
newline|'\n'
DECL|variable|_new_only_fields
indent|'    '
name|'_new_only_fields'
op|'='
name|'set'
op|'('
op|'['
string|"'disk_bus'"
op|','
string|"'device_type'"
op|','
string|"'guest_format'"
op|']'
op|')'
newline|'\n'
DECL|variable|_fields
name|'_fields'
op|'='
name|'set'
op|'('
op|'['
string|"'device_name'"
op|','
string|"'size'"
op|']'
op|')'
op|'|'
name|'_new_only_fields'
newline|'\n'
DECL|variable|_legacy_fields
name|'_legacy_fields'
op|'='
op|'('
name|'_fields'
op|'-'
name|'_new_only_fields'
op|'|'
nl|'\n'
name|'set'
op|'('
op|'['
string|"'num'"
op|','
string|"'virtual_name'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_transform
name|'def'
name|'_transform'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'block_device'
op|'.'
name|'new_format_is_ephemeral'
op|'('
name|'self'
op|'.'
name|'_bdm_obj'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'_InvalidType'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'update'
op|'('
op|'{'
nl|'\n'
string|"'device_name'"
op|':'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'device_name'
op|','
nl|'\n'
string|"'size'"
op|':'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'volume_size'
name|'or'
number|'0'
op|','
nl|'\n'
string|"'disk_bus'"
op|':'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'disk_bus'
op|','
nl|'\n'
string|"'device_type'"
op|':'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'device_type'
op|','
nl|'\n'
string|"'guest_format'"
op|':'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'guest_format'
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|legacy
dedent|''
name|'def'
name|'legacy'
op|'('
name|'self'
op|','
name|'num'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'legacy_bdm'
op|'='
name|'super'
op|'('
name|'DriverEphemeralBlockDevice'
op|','
name|'self'
op|')'
op|'.'
name|'legacy'
op|'('
op|')'
newline|'\n'
name|'legacy_bdm'
op|'['
string|"'num'"
op|']'
op|'='
name|'num'
newline|'\n'
name|'legacy_bdm'
op|'['
string|"'virtual_name'"
op|']'
op|'='
string|"'ephemeral'"
op|'+'
name|'str'
op|'('
name|'num'
op|')'
newline|'\n'
name|'return'
name|'legacy_bdm'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DriverVolumeBlockDevice
dedent|''
dedent|''
name|'class'
name|'DriverVolumeBlockDevice'
op|'('
name|'DriverBlockDevice'
op|')'
op|':'
newline|'\n'
DECL|variable|_legacy_fields
indent|'    '
name|'_legacy_fields'
op|'='
name|'set'
op|'('
op|'['
string|"'connection_info'"
op|','
string|"'mount_device'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|']'
op|')'
newline|'\n'
DECL|variable|_new_fields
name|'_new_fields'
op|'='
name|'set'
op|'('
op|'['
string|"'guest_format'"
op|','
string|"'device_type'"
op|','
nl|'\n'
string|"'disk_bus'"
op|','
string|"'boot_index'"
op|']'
op|')'
newline|'\n'
DECL|variable|_fields
name|'_fields'
op|'='
name|'_legacy_fields'
op|'|'
name|'_new_fields'
newline|'\n'
nl|'\n'
DECL|variable|_valid_source
name|'_valid_source'
op|'='
string|"'volume'"
newline|'\n'
DECL|variable|_valid_destination
name|'_valid_destination'
op|'='
string|"'volume'"
newline|'\n'
nl|'\n'
DECL|variable|_proxy_as_attr
name|'_proxy_as_attr'
op|'='
name|'set'
op|'('
op|'['
string|"'volume_size'"
op|','
string|"'volume_id'"
op|']'
op|')'
newline|'\n'
DECL|variable|_update_on_save
name|'_update_on_save'
op|'='
op|'{'
string|"'disk_bus'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'mount_device'"
op|','
nl|'\n'
string|"'device_type'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_transform
name|'def'
name|'_transform'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
op|'('
name|'not'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'source_type'
op|'=='
name|'self'
op|'.'
name|'_valid_source'
nl|'\n'
name|'or'
name|'not'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'destination_type'
op|'=='
nl|'\n'
name|'self'
op|'.'
name|'_valid_destination'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'_InvalidType'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'update'
op|'('
nl|'\n'
name|'dict'
op|'('
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'iteritems'
op|'('
op|')'
nl|'\n'
name|'if'
name|'k'
name|'in'
name|'self'
op|'.'
name|'_new_fields'
op|'|'
name|'set'
op|'('
op|'['
string|"'delete_on_termination'"
op|']'
op|')'
op|')'
nl|'\n'
op|')'
newline|'\n'
name|'self'
op|'['
string|"'mount_device'"
op|']'
op|'='
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'device_name'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'connection_info'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'connection_info'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'connection_info'"
op|']'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'update_db'
newline|'\n'
DECL|member|attach
name|'def'
name|'attach'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'volume_api'
op|','
name|'virt_driver'
op|','
nl|'\n'
name|'do_check_attach'
op|'='
name|'True'
op|','
name|'do_driver_attach'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
name|'volume_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'volume_id'
op|')'
newline|'\n'
name|'if'
name|'do_check_attach'
op|':'
newline|'\n'
indent|'            '
name|'volume_api'
op|'.'
name|'check_attach'
op|'('
name|'context'
op|','
name|'volume'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'volume_id'
op|'='
name|'volume'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'connector'
op|'='
name|'virt_driver'
op|'.'
name|'get_volume_connector'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'connection_info'
op|'='
name|'volume_api'
op|'.'
name|'initialize_connection'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|','
nl|'\n'
name|'connector'
op|')'
newline|'\n'
name|'if'
string|"'serial'"
name|'not'
name|'in'
name|'connection_info'
op|':'
newline|'\n'
indent|'            '
name|'connection_info'
op|'['
string|"'serial'"
op|']'
op|'='
name|'self'
op|'.'
name|'volume_id'
newline|'\n'
nl|'\n'
comment|'# If do_driver_attach is False, we will attach a volume to an instance'
nl|'\n'
comment|'# at boot time. So actual attach is done by instance creation code.'
nl|'\n'
dedent|''
name|'if'
name|'do_driver_attach'
op|':'
newline|'\n'
indent|'            '
name|'encryption'
op|'='
name|'encryptors'
op|'.'
name|'get_encryption_metadata'
op|'('
nl|'\n'
name|'context'
op|','
name|'volume_api'
op|','
name|'volume_id'
op|','
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'virt_driver'
op|'.'
name|'attach_volume'
op|'('
nl|'\n'
name|'context'
op|','
name|'connection_info'
op|','
name|'instance'
op|','
nl|'\n'
name|'self'
op|'['
string|"'mount_device'"
op|']'
op|','
name|'disk_bus'
op|'='
name|'self'
op|'['
string|"'disk_bus'"
op|']'
op|','
nl|'\n'
name|'device_type'
op|'='
name|'self'
op|'['
string|"'device_type'"
op|']'
op|','
name|'encryption'
op|'='
name|'encryption'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
comment|'# pylint: disable=W0702'
newline|'\n'
indent|'                '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Driver failed to attach volume "'
nl|'\n'
string|'"%(volume_id)s at %(mountpoint)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'volume_id'"
op|':'
name|'volume_id'
op|','
nl|'\n'
string|"'mountpoint'"
op|':'
name|'self'
op|'['
string|"'mount_device'"
op|']'
op|'}'
op|','
nl|'\n'
name|'context'
op|'='
name|'context'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'volume_api'
op|'.'
name|'terminate_connection'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
nl|'\n'
name|'connector'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'self'
op|'['
string|"'connection_info'"
op|']'
op|'='
name|'connection_info'
newline|'\n'
nl|'\n'
name|'mode'
op|'='
string|"'rw'"
newline|'\n'
name|'if'
string|"'data'"
name|'in'
name|'connection_info'
op|':'
newline|'\n'
indent|'            '
name|'mode'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'.'
name|'get'
op|'('
string|"'access_mode'"
op|','
string|"'rw'"
op|')'
newline|'\n'
dedent|''
name|'volume_api'
op|'.'
name|'attach'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'self'
op|'['
string|"'mount_device'"
op|']'
op|','
name|'mode'
op|'='
name|'mode'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'update_db'
newline|'\n'
DECL|member|refresh_connection_info
name|'def'
name|'refresh_connection_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'volume_api'
op|','
name|'virt_driver'
op|')'
op|':'
newline|'\n'
comment|'# NOTE (ndipanov): A no-op if there is no connection info already'
nl|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'['
string|"'connection_info'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'connector'
op|'='
name|'virt_driver'
op|'.'
name|'get_volume_connector'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'connection_info'
op|'='
name|'volume_api'
op|'.'
name|'initialize_connection'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume_id'
op|','
nl|'\n'
name|'connector'
op|')'
newline|'\n'
name|'if'
string|"'serial'"
name|'not'
name|'in'
name|'connection_info'
op|':'
newline|'\n'
indent|'            '
name|'connection_info'
op|'['
string|"'serial'"
op|']'
op|'='
name|'self'
op|'.'
name|'volume_id'
newline|'\n'
dedent|''
name|'self'
op|'['
string|"'connection_info'"
op|']'
op|'='
name|'connection_info'
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
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(ndipanov): we might want to generalize this by adding it to the'
nl|'\n'
comment|'# _update_on_save and adding a transformation function.'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_bdm_obj'
op|'.'
name|'connection_info'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'get'
op|'('
string|"'connection_info'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'DriverVolumeBlockDevice'
op|','
name|'self'
op|')'
op|'.'
name|'save'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DriverSnapshotBlockDevice
dedent|''
dedent|''
name|'class'
name|'DriverSnapshotBlockDevice'
op|'('
name|'DriverVolumeBlockDevice'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|_valid_source
indent|'    '
name|'_valid_source'
op|'='
string|"'snapshot'"
newline|'\n'
DECL|variable|_proxy_as_attr
name|'_proxy_as_attr'
op|'='
name|'set'
op|'('
op|'['
string|"'volume_size'"
op|','
string|"'volume_id'"
op|','
string|"'snapshot_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach
name|'def'
name|'attach'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'volume_api'
op|','
nl|'\n'
name|'virt_driver'
op|','
name|'wait_func'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'volume_id'
op|':'
newline|'\n'
indent|'            '
name|'snapshot'
op|'='
name|'volume_api'
op|'.'
name|'get_snapshot'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'snapshot_id'
op|')'
newline|'\n'
name|'vol'
op|'='
name|'volume_api'
op|'.'
name|'create'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'volume_size'
op|','
nl|'\n'
string|"''"
op|','
string|"''"
op|','
name|'snapshot'
op|')'
newline|'\n'
name|'if'
name|'wait_func'
op|':'
newline|'\n'
indent|'                '
name|'wait_func'
op|'('
name|'context'
op|','
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'volume_id'
op|'='
name|'vol'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Call the volume attach now'
nl|'\n'
dedent|''
name|'super'
op|'('
name|'DriverSnapshotBlockDevice'
op|','
name|'self'
op|')'
op|'.'
name|'attach'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'volume_api'
op|','
name|'virt_driver'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DriverImageBlockDevice
dedent|''
dedent|''
name|'class'
name|'DriverImageBlockDevice'
op|'('
name|'DriverVolumeBlockDevice'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|_valid_source
indent|'    '
name|'_valid_source'
op|'='
string|"'image'"
newline|'\n'
DECL|variable|_proxy_as_attr
name|'_proxy_as_attr'
op|'='
name|'set'
op|'('
op|'['
string|"'volume_size'"
op|','
string|"'volume_id'"
op|','
string|"'image_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach
name|'def'
name|'attach'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'volume_api'
op|','
nl|'\n'
name|'virt_driver'
op|','
name|'wait_func'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'volume_id'
op|':'
newline|'\n'
indent|'            '
name|'vol'
op|'='
name|'volume_api'
op|'.'
name|'create'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'volume_size'
op|','
nl|'\n'
string|"''"
op|','
string|"''"
op|','
name|'image_id'
op|'='
name|'self'
op|'.'
name|'image_id'
op|')'
newline|'\n'
name|'if'
name|'wait_func'
op|':'
newline|'\n'
indent|'                '
name|'wait_func'
op|'('
name|'context'
op|','
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'volume_id'
op|'='
name|'vol'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'super'
op|'('
name|'DriverImageBlockDevice'
op|','
name|'self'
op|')'
op|'.'
name|'attach'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'volume_api'
op|','
name|'virt_driver'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_convert_block_devices
dedent|''
dedent|''
name|'def'
name|'_convert_block_devices'
op|'('
name|'device_type'
op|','
name|'block_device_mapping'
op|')'
op|':'
newline|'\n'
DECL|function|_is_transformable
indent|'    '
name|'def'
name|'_is_transformable'
op|'('
name|'bdm'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'device_type'
op|'('
name|'bdm'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'_NotTransformable'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'['
name|'device_type'
op|'('
name|'bdm'
op|')'
nl|'\n'
name|'for'
name|'bdm'
name|'in'
name|'block_device_mapping'
nl|'\n'
name|'if'
name|'_is_transformable'
op|'('
name|'bdm'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|convert_swap
dedent|''
name|'convert_swap'
op|'='
name|'functools'
op|'.'
name|'partial'
op|'('
name|'_convert_block_devices'
op|','
nl|'\n'
name|'DriverSwapBlockDevice'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|convert_ephemerals
name|'convert_ephemerals'
op|'='
name|'functools'
op|'.'
name|'partial'
op|'('
name|'_convert_block_devices'
op|','
nl|'\n'
name|'DriverEphemeralBlockDevice'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|convert_volumes
name|'convert_volumes'
op|'='
name|'functools'
op|'.'
name|'partial'
op|'('
name|'_convert_block_devices'
op|','
nl|'\n'
name|'DriverVolumeBlockDevice'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|convert_snapshots
name|'convert_snapshots'
op|'='
name|'functools'
op|'.'
name|'partial'
op|'('
name|'_convert_block_devices'
op|','
nl|'\n'
name|'DriverSnapshotBlockDevice'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|convert_images
name|'convert_images'
op|'='
name|'functools'
op|'.'
name|'partial'
op|'('
name|'_convert_block_devices'
op|','
nl|'\n'
name|'DriverImageBlockDevice'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|attach_block_devices
name|'def'
name|'attach_block_devices'
op|'('
name|'block_device_mapping'
op|','
op|'*'
name|'attach_args'
op|','
op|'**'
name|'attach_kwargs'
op|')'
op|':'
newline|'\n'
DECL|function|_log_and_attach
indent|'    '
name|'def'
name|'_log_and_attach'
op|'('
name|'bdm'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'attach_args'
op|'['
number|'0'
op|']'
newline|'\n'
name|'instance'
op|'='
name|'attach_args'
op|'['
number|'1'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'Booting with volume %(volume_id)s at %(mountpoint)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'volume_id'"
op|':'
name|'bdm'
op|'.'
name|'volume_id'
op|','
nl|'\n'
string|"'mountpoint'"
op|':'
name|'bdm'
op|'['
string|"'mount_device'"
op|']'
op|'}'
op|','
nl|'\n'
name|'context'
op|'='
name|'context'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'bdm'
op|'.'
name|'attach'
op|'('
op|'*'
name|'attach_args'
op|','
op|'**'
name|'attach_kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'map'
op|'('
name|'_log_and_attach'
op|','
name|'block_device_mapping'
op|')'
newline|'\n'
name|'return'
name|'block_device_mapping'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|refresh_conn_infos
dedent|''
name|'def'
name|'refresh_conn_infos'
op|'('
name|'block_device_mapping'
op|','
op|'*'
name|'refresh_args'
op|','
op|'**'
name|'refresh_kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'map'
op|'('
name|'operator'
op|'.'
name|'methodcaller'
op|'('
string|"'refresh_connection_info'"
op|','
nl|'\n'
op|'*'
name|'refresh_args'
op|','
op|'**'
name|'refresh_kwargs'
op|')'
op|','
nl|'\n'
name|'block_device_mapping'
op|')'
newline|'\n'
name|'return'
name|'block_device_mapping'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|legacy_block_devices
dedent|''
name|'def'
name|'legacy_block_devices'
op|'('
name|'block_device_mapping'
op|')'
op|':'
newline|'\n'
DECL|function|_has_legacy
indent|'    '
name|'def'
name|'_has_legacy'
op|'('
name|'bdm'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'bdm'
op|'.'
name|'legacy'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'_NoLegacy'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'bdms'
op|'='
op|'['
name|'bdm'
op|'.'
name|'legacy'
op|'('
op|')'
nl|'\n'
name|'for'
name|'bdm'
name|'in'
name|'block_device_mapping'
nl|'\n'
name|'if'
name|'_has_legacy'
op|'('
name|'bdm'
op|')'
op|']'
newline|'\n'
nl|'\n'
comment|'# Re-enumerate ephemeral devices'
nl|'\n'
name|'if'
name|'all'
op|'('
name|'isinstance'
op|'('
name|'bdm'
op|','
name|'DriverEphemeralBlockDevice'
op|')'
nl|'\n'
name|'for'
name|'bdm'
name|'in'
name|'block_device_mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'i'
op|','
name|'dev'
name|'in'
name|'enumerate'
op|'('
name|'bdms'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'['
string|"'virtual_name'"
op|']'
op|'='
name|'dev'
op|'['
string|"'virtual_name'"
op|']'
op|'['
op|':'
op|'-'
number|'1'
op|']'
op|'+'
name|'str'
op|'('
name|'i'
op|')'
newline|'\n'
name|'dev'
op|'['
string|"'num'"
op|']'
op|'='
name|'i'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'bdms'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_swap
dedent|''
name|'def'
name|'get_swap'
op|'('
name|'transformed_list'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the swap device out of the list context.\n\n    The block_device_info needs swap to be a single device,\n    not a list - otherwise this is a no-op.\n    """'
newline|'\n'
name|'if'
name|'not'
name|'all'
op|'('
name|'isinstance'
op|'('
name|'device'
op|','
name|'DriverSwapBlockDevice'
op|')'
name|'or'
nl|'\n'
string|"'swap_size'"
name|'in'
name|'device'
nl|'\n'
name|'for'
name|'device'
name|'in'
name|'transformed_list'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'transformed_list'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'transformed_list'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IndexError'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_IMPLEMENTED_CLASSES
dedent|''
dedent|''
name|'_IMPLEMENTED_CLASSES'
op|'='
op|'('
name|'DriverSwapBlockDevice'
op|','
name|'DriverEphemeralBlockDevice'
op|','
nl|'\n'
name|'DriverVolumeBlockDevice'
op|','
name|'DriverSnapshotBlockDevice'
op|','
nl|'\n'
name|'DriverImageBlockDevice'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_implemented
name|'def'
name|'is_implemented'
op|'('
name|'bdm'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'cls'
name|'in'
name|'_IMPLEMENTED_CLASSES'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'('
name|'bdm'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'_NotTransformable'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
dedent|''
endmarker|''
end_unit
