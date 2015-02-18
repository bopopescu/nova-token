begin_unit
comment|'# Copyright (c) 2011 OpenStack Foundation'
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
string|'"""Compute-related Utilities and helpers."""'
newline|'\n'
nl|'\n'
name|'import'
name|'itertools'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
name|'import'
name|'traceback'
newline|'\n'
nl|'\n'
name|'import'
name|'netifaces'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'encodeutils'
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
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_states'
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
op|'.'
name|'network'
name|'import'
name|'model'
name|'as'
name|'network_model'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'notifications'
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
name|'log'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'host'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'log'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|exception_to_dict
name|'def'
name|'exception_to_dict'
op|'('
name|'fault'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Converts exceptions to a dict for use in notifications."""'
newline|'\n'
comment|'# TODO(johngarbutt) move to nova/exception.py to share with wrap_exception'
nl|'\n'
nl|'\n'
name|'code'
op|'='
number|'500'
newline|'\n'
name|'if'
name|'hasattr'
op|'('
name|'fault'
op|','
string|'"kwargs"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'code'
op|'='
name|'fault'
op|'.'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'code'"
op|','
number|'500'
op|')'
newline|'\n'
nl|'\n'
comment|'# get the message from the exception that was thrown'
nl|'\n'
comment|'# if that does not exist, use the name of the exception class itself'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'message'
op|'='
name|'fault'
op|'.'
name|'format_message'
op|'('
op|')'
newline|'\n'
comment|"# These exception handlers are broad so we don't fail to log the fault"
nl|'\n'
comment|'# just because there is an unexpected error retrieving the message'
nl|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'message'
op|'='
name|'unicode'
op|'('
name|'fault'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'message'
op|'='
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'message'
op|':'
newline|'\n'
indent|'        '
name|'message'
op|'='
name|'fault'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
newline|'\n'
comment|'# NOTE(dripton) The message field in the database is limited to 255 chars.'
nl|'\n'
comment|'# MySQL silently truncates overly long messages, but PostgreSQL throws an'
nl|'\n'
comment|"# error if we don't truncate it."
nl|'\n'
dedent|''
name|'b_message'
op|'='
name|'encodeutils'
op|'.'
name|'safe_encode'
op|'('
name|'message'
op|')'
op|'['
op|':'
number|'255'
op|']'
newline|'\n'
nl|'\n'
comment|'# NOTE(chaochin) UTF-8 character byte size varies from 1 to 6. If'
nl|'\n'
comment|'# truncating a long byte string to 255, the last character may be'
nl|'\n'
comment|'# cut in the middle, so that UnicodeDecodeError will occur when'
nl|'\n'
comment|'# converting it back to unicode.'
nl|'\n'
name|'decode_ok'
op|'='
name|'False'
newline|'\n'
name|'while'
name|'not'
name|'decode_ok'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'u_message'
op|'='
name|'encodeutils'
op|'.'
name|'safe_decode'
op|'('
name|'b_message'
op|')'
newline|'\n'
name|'decode_ok'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'UnicodeDecodeError'
op|':'
newline|'\n'
indent|'            '
name|'b_message'
op|'='
name|'b_message'
op|'['
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'fault_dict'
op|'='
name|'dict'
op|'('
name|'exception'
op|'='
name|'fault'
op|')'
newline|'\n'
name|'fault_dict'
op|'['
string|'"message"'
op|']'
op|'='
name|'u_message'
newline|'\n'
name|'fault_dict'
op|'['
string|'"code"'
op|']'
op|'='
name|'code'
newline|'\n'
name|'return'
name|'fault_dict'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_fault_details
dedent|''
name|'def'
name|'_get_fault_details'
op|'('
name|'exc_info'
op|','
name|'error_code'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'details'
op|'='
string|"''"
newline|'\n'
name|'if'
name|'exc_info'
name|'and'
name|'error_code'
op|'=='
number|'500'
op|':'
newline|'\n'
indent|'        '
name|'tb'
op|'='
name|'exc_info'
op|'['
number|'2'
op|']'
newline|'\n'
name|'if'
name|'tb'
op|':'
newline|'\n'
indent|'            '
name|'details'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
name|'traceback'
op|'.'
name|'format_tb'
op|'('
name|'tb'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'unicode'
op|'('
name|'details'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|add_instance_fault_from_exc
dedent|''
name|'def'
name|'add_instance_fault_from_exc'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'fault'
op|','
name|'exc_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Adds the specified fault to the database."""'
newline|'\n'
nl|'\n'
name|'fault_obj'
op|'='
name|'objects'
op|'.'
name|'InstanceFault'
op|'('
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'fault_obj'
op|'.'
name|'host'
op|'='
name|'CONF'
op|'.'
name|'host'
newline|'\n'
name|'fault_obj'
op|'.'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'fault_obj'
op|'.'
name|'update'
op|'('
name|'exception_to_dict'
op|'('
name|'fault'
op|')'
op|')'
newline|'\n'
name|'code'
op|'='
name|'fault_obj'
op|'.'
name|'code'
newline|'\n'
name|'fault_obj'
op|'.'
name|'details'
op|'='
name|'_get_fault_details'
op|'('
name|'exc_info'
op|','
name|'code'
op|')'
newline|'\n'
name|'fault_obj'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_device_name_for_instance
dedent|''
name|'def'
name|'get_device_name_for_instance'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'bdms'
op|','
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Validates (or generates) a device name for instance.\n\n    This method is a wrapper for get_next_device_name that gets the list\n    of used devices and the root device from a block device mapping.\n    """'
newline|'\n'
name|'mappings'
op|'='
name|'block_device'
op|'.'
name|'instance_block_mapping'
op|'('
name|'instance'
op|','
name|'bdms'
op|')'
newline|'\n'
name|'return'
name|'get_next_device_name'
op|'('
name|'instance'
op|','
name|'mappings'
op|'.'
name|'values'
op|'('
op|')'
op|','
nl|'\n'
name|'mappings'
op|'['
string|"'root'"
op|']'
op|','
name|'device'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|default_device_names_for_instance
dedent|''
name|'def'
name|'default_device_names_for_instance'
op|'('
name|'instance'
op|','
name|'root_device_name'
op|','
nl|'\n'
op|'*'
name|'block_device_lists'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generate missing device names for an instance."""'
newline|'\n'
nl|'\n'
name|'dev_list'
op|'='
op|'['
name|'bdm'
op|'.'
name|'device_name'
nl|'\n'
name|'for'
name|'bdm'
name|'in'
name|'itertools'
op|'.'
name|'chain'
op|'('
op|'*'
name|'block_device_lists'
op|')'
nl|'\n'
name|'if'
name|'bdm'
op|'.'
name|'device_name'
op|']'
newline|'\n'
name|'if'
name|'root_device_name'
name|'not'
name|'in'
name|'dev_list'
op|':'
newline|'\n'
indent|'        '
name|'dev_list'
op|'.'
name|'append'
op|'('
name|'root_device_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'bdm'
name|'in'
name|'itertools'
op|'.'
name|'chain'
op|'('
op|'*'
name|'block_device_lists'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev'
op|'='
name|'bdm'
op|'.'
name|'device_name'
newline|'\n'
name|'if'
name|'not'
name|'dev'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'='
name|'get_next_device_name'
op|'('
name|'instance'
op|','
name|'dev_list'
op|','
nl|'\n'
name|'root_device_name'
op|')'
newline|'\n'
name|'bdm'
op|'.'
name|'device_name'
op|'='
name|'dev'
newline|'\n'
name|'bdm'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'dev_list'
op|'.'
name|'append'
op|'('
name|'dev'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_next_device_name
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_next_device_name'
op|'('
name|'instance'
op|','
name|'device_name_list'
op|','
nl|'\n'
name|'root_device_name'
op|'='
name|'None'
op|','
name|'device'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Validates (or generates) a device name for instance.\n\n    If device is not set, it will generate a unique device appropriate\n    for the instance. It uses the root_device_name (if provided) and\n    the list of used devices to find valid device names. If the device\n    name is valid but applicable to a different backend (for example\n    /dev/vdc is specified but the backend uses /dev/xvdc), the device\n    name will be converted to the appropriate format.\n    """'
newline|'\n'
name|'is_xen'
op|'='
name|'driver'
op|'.'
name|'compute_driver_matches'
op|'('
string|"'xenapi.XenAPIDriver'"
op|')'
newline|'\n'
nl|'\n'
name|'req_prefix'
op|'='
name|'None'
newline|'\n'
name|'req_letter'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'if'
name|'device'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'req_prefix'
op|','
name|'req_letter'
op|'='
name|'block_device'
op|'.'
name|'match_device'
op|'('
name|'device'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'AttributeError'
op|','
name|'ValueError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidDevicePath'
op|'('
name|'path'
op|'='
name|'device'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'root_device_name'
op|':'
newline|'\n'
indent|'        '
name|'root_device_name'
op|'='
name|'block_device'
op|'.'
name|'DEFAULT_ROOT_DEV_NAME'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'prefix'
op|'='
name|'block_device'
op|'.'
name|'match_device'
op|'('
nl|'\n'
name|'block_device'
op|'.'
name|'prepend_dev'
op|'('
name|'root_device_name'
op|')'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'AttributeError'
op|','
name|'ValueError'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidDevicePath'
op|'('
name|'path'
op|'='
name|'root_device_name'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(vish): remove this when xenapi is setting default_root_device'
nl|'\n'
dedent|''
name|'if'
name|'is_xen'
op|':'
newline|'\n'
indent|'        '
name|'prefix'
op|'='
string|"'/dev/xvd'"
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'req_prefix'
op|'!='
name|'prefix'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Using %(prefix)s instead of %(req_prefix)s"'
op|','
nl|'\n'
op|'{'
string|"'prefix'"
op|':'
name|'prefix'
op|','
string|"'req_prefix'"
op|':'
name|'req_prefix'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'used_letters'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'for'
name|'device_path'
name|'in'
name|'device_name_list'
op|':'
newline|'\n'
indent|'        '
name|'letter'
op|'='
name|'block_device'
op|'.'
name|'get_device_letter'
op|'('
name|'device_path'
op|')'
newline|'\n'
name|'used_letters'
op|'.'
name|'add'
op|'('
name|'letter'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(vish): remove this when xenapi is properly setting'
nl|'\n'
comment|'#             default_ephemeral_device and default_swap_device'
nl|'\n'
dedent|''
name|'if'
name|'is_xen'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'instance'
op|'.'
name|'get_flavor'
op|'('
op|')'
newline|'\n'
name|'if'
name|'flavor'
op|'.'
name|'ephemeral_gb'
op|':'
newline|'\n'
indent|'            '
name|'used_letters'
op|'.'
name|'add'
op|'('
string|"'b'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'flavor'
op|'.'
name|'swap'
op|':'
newline|'\n'
indent|'            '
name|'used_letters'
op|'.'
name|'add'
op|'('
string|"'c'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'req_letter'
op|':'
newline|'\n'
indent|'        '
name|'req_letter'
op|'='
name|'_get_unused_letter'
op|'('
name|'used_letters'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'req_letter'
name|'in'
name|'used_letters'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'DevicePathInUse'
op|'('
name|'path'
op|'='
name|'device'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'prefix'
op|'+'
name|'req_letter'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_unused_letter
dedent|''
name|'def'
name|'_get_unused_letter'
op|'('
name|'used_letters'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'doubles'
op|'='
op|'['
name|'first'
op|'+'
name|'second'
name|'for'
name|'second'
name|'in'
name|'string'
op|'.'
name|'ascii_lowercase'
nl|'\n'
name|'for'
name|'first'
name|'in'
name|'string'
op|'.'
name|'ascii_lowercase'
op|']'
newline|'\n'
name|'all_letters'
op|'='
name|'set'
op|'('
name|'list'
op|'('
name|'string'
op|'.'
name|'ascii_lowercase'
op|')'
op|'+'
name|'doubles'
op|')'
newline|'\n'
name|'letters'
op|'='
name|'list'
op|'('
name|'all_letters'
op|'-'
name|'used_letters'
op|')'
newline|'\n'
comment|'# NOTE(vish): prepend ` so all shorter sequences sort first'
nl|'\n'
name|'letters'
op|'.'
name|'sort'
op|'('
name|'key'
op|'='
name|'lambda'
name|'x'
op|':'
name|'x'
op|'.'
name|'rjust'
op|'('
number|'2'
op|','
string|"'`'"
op|')'
op|')'
newline|'\n'
name|'return'
name|'letters'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_image_metadata
dedent|''
name|'def'
name|'get_image_metadata'
op|'('
name|'context'
op|','
name|'image_api'
op|','
name|'image_id_or_uri'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'image_system_meta'
op|'='
op|'{'
op|'}'
newline|'\n'
comment|"# In case of boot from volume, image_id_or_uri may be None or ''"
nl|'\n'
name|'if'
name|'image_id_or_uri'
name|'is'
name|'not'
name|'None'
name|'and'
name|'image_id_or_uri'
op|'!='
string|"''"
op|':'
newline|'\n'
comment|'# If the base image is still available, get its metadata'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image'
op|'='
name|'image_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'image_id_or_uri'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'ImageNotAuthorized'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'ImageNotFound'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'Invalid'
op|')'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Can\'t access image %(image_id)s: %(error)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|'"image_id"'
op|':'
name|'image_id_or_uri'
op|','
string|'"error"'
op|':'
name|'e'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'flavor'
op|'='
name|'instance'
op|'.'
name|'get_flavor'
op|'('
op|')'
newline|'\n'
name|'image_system_meta'
op|'='
name|'utils'
op|'.'
name|'get_system_metadata_from_image'
op|'('
name|'image'
op|','
nl|'\n'
name|'flavor'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get the system metadata from the instance'
nl|'\n'
dedent|''
dedent|''
name|'system_meta'
op|'='
name|'utils'
op|'.'
name|'instance_sys_meta'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|"# Merge the metadata from the instance with the image's, if any"
nl|'\n'
name|'system_meta'
op|'.'
name|'update'
op|'('
name|'image_system_meta'
op|')'
newline|'\n'
nl|'\n'
comment|'# Convert the system metadata to image metadata'
nl|'\n'
name|'return'
name|'utils'
op|'.'
name|'get_image_from_system_metadata'
op|'('
name|'system_meta'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_value_from_system_metadata
dedent|''
name|'def'
name|'get_value_from_system_metadata'
op|'('
name|'instance'
op|','
name|'key'
op|','
name|'type'
op|','
name|'default'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get a value of a specified type from image metadata.\n\n    @param instance: The instance object\n    @param key: The name of the property to get\n    @param type: The python type the value is be returned as\n    @param default: The value to return if key is not set or not the right type\n    """'
newline|'\n'
name|'value'
op|'='
name|'instance'
op|'.'
name|'system_metadata'
op|'.'
name|'get'
op|'('
name|'key'
op|','
name|'default'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'type'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Metadata value %(value)s for %(key)s is not of "'
nl|'\n'
string|'"type %(type)s. Using default value %(default)s."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'value'"
op|':'
name|'value'
op|','
string|"'key'"
op|':'
name|'key'
op|','
string|"'type'"
op|':'
name|'type'
op|','
nl|'\n'
string|"'default'"
op|':'
name|'default'
op|'}'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'default'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify_usage_exists
dedent|''
dedent|''
name|'def'
name|'notify_usage_exists'
op|'('
name|'notifier'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'current_period'
op|'='
name|'False'
op|','
nl|'\n'
name|'ignore_missing_network_data'
op|'='
name|'True'
op|','
nl|'\n'
name|'system_metadata'
op|'='
name|'None'
op|','
name|'extra_usage_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generates \'exists\' notification for an instance for usage auditing\n    purposes.\n\n    :param notifier: a messaging.Notifier\n\n    :param current_period: if True, this will generate a usage for the\n        current usage period; if False, this will generate a usage for the\n        previous audit period.\n\n    :param ignore_missing_network_data: if True, log any exceptions generated\n        while getting network info; if False, raise the exception.\n    :param system_metadata: system_metadata DB entries for the instance,\n        if not None.  *NOTE*: Currently unused here in trunk, but needed for\n        potential custom modifications.\n    :param extra_usage_info: Dictionary containing extra values to add or\n        override in the notification if not None.\n    """'
newline|'\n'
nl|'\n'
name|'audit_start'
op|','
name|'audit_end'
op|'='
name|'notifications'
op|'.'
name|'audit_period_bounds'
op|'('
name|'current_period'
op|')'
newline|'\n'
nl|'\n'
name|'bw'
op|'='
name|'notifications'
op|'.'
name|'bandwidth_usage'
op|'('
name|'instance_ref'
op|','
name|'audit_start'
op|','
nl|'\n'
name|'ignore_missing_network_data'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'system_metadata'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'system_metadata'
op|'='
name|'utils'
op|'.'
name|'instance_sys_meta'
op|'('
name|'instance_ref'
op|')'
newline|'\n'
nl|'\n'
comment|'# add image metadata to the notification:'
nl|'\n'
dedent|''
name|'image_meta'
op|'='
name|'notifications'
op|'.'
name|'image_meta'
op|'('
name|'system_metadata'
op|')'
newline|'\n'
nl|'\n'
name|'extra_info'
op|'='
name|'dict'
op|'('
name|'audit_period_beginning'
op|'='
name|'str'
op|'('
name|'audit_start'
op|')'
op|','
nl|'\n'
name|'audit_period_ending'
op|'='
name|'str'
op|'('
name|'audit_end'
op|')'
op|','
nl|'\n'
name|'bandwidth'
op|'='
name|'bw'
op|','
name|'image_meta'
op|'='
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'extra_usage_info'
op|':'
newline|'\n'
indent|'        '
name|'extra_info'
op|'.'
name|'update'
op|'('
name|'extra_usage_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'notify_about_instance_usage'
op|'('
name|'notifier'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
string|"'exists'"
op|','
nl|'\n'
name|'system_metadata'
op|'='
name|'system_metadata'
op|','
name|'extra_usage_info'
op|'='
name|'extra_info'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify_about_instance_usage
dedent|''
name|'def'
name|'notify_about_instance_usage'
op|'('
name|'notifier'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'event_suffix'
op|','
nl|'\n'
name|'network_info'
op|'='
name|'None'
op|','
name|'system_metadata'
op|'='
name|'None'
op|','
nl|'\n'
name|'extra_usage_info'
op|'='
name|'None'
op|','
name|'fault'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Send a notification about an instance.\n\n    :param notifier: a messaging.Notifier\n    :param event_suffix: Event type like "delete.start" or "exists"\n    :param network_info: Networking information, if provided.\n    :param system_metadata: system_metadata DB entries for the instance,\n        if provided.\n    :param extra_usage_info: Dictionary containing extra values to add or\n        override in the notification.\n    """'
newline|'\n'
name|'if'
name|'not'
name|'extra_usage_info'
op|':'
newline|'\n'
indent|'        '
name|'extra_usage_info'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'usage_info'
op|'='
name|'notifications'
op|'.'
name|'info_from_instance'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'network_info'
op|','
name|'system_metadata'
op|','
op|'**'
name|'extra_usage_info'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'fault'
op|':'
newline|'\n'
comment|'# NOTE(johngarbutt) mirrors the format in wrap_exception'
nl|'\n'
indent|'        '
name|'fault_payload'
op|'='
name|'exception_to_dict'
op|'('
name|'fault'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'fault_payload'
op|'['
string|'"message"'
op|']'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'usage_info'
op|'.'
name|'update'
op|'('
name|'fault_payload'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'event_suffix'
op|'.'
name|'endswith'
op|'('
string|'"error"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'method'
op|'='
name|'notifier'
op|'.'
name|'error'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'method'
op|'='
name|'notifier'
op|'.'
name|'info'
newline|'\n'
nl|'\n'
dedent|''
name|'method'
op|'('
name|'context'
op|','
string|"'compute.instance.%s'"
op|'%'
name|'event_suffix'
op|','
name|'usage_info'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify_about_server_group_update
dedent|''
name|'def'
name|'notify_about_server_group_update'
op|'('
name|'context'
op|','
name|'event_suffix'
op|','
name|'sg_payload'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Send a notification about server group update.\n\n    :param event_suffix: Event type like "create.start" or "create.end"\n    :param sg_payload: payload for server group update\n    """'
newline|'\n'
name|'notifier'
op|'='
name|'rpc'
op|'.'
name|'get_notifier'
op|'('
name|'service'
op|'='
string|"'servergroup'"
op|')'
newline|'\n'
nl|'\n'
name|'notifier'
op|'.'
name|'info'
op|'('
name|'context'
op|','
string|"'servergroup.%s'"
op|'%'
name|'event_suffix'
op|','
name|'sg_payload'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify_about_aggregate_update
dedent|''
name|'def'
name|'notify_about_aggregate_update'
op|'('
name|'context'
op|','
name|'event_suffix'
op|','
name|'aggregate_payload'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Send a notification about aggregate update.\n\n    :param event_suffix: Event type like "create.start" or "create.end"\n    :param aggregate_payload: payload for aggregate update\n    """'
newline|'\n'
name|'aggregate_identifier'
op|'='
name|'aggregate_payload'
op|'.'
name|'get'
op|'('
string|"'aggregate_id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'aggregate_identifier'
op|':'
newline|'\n'
indent|'        '
name|'aggregate_identifier'
op|'='
name|'aggregate_payload'
op|'.'
name|'get'
op|'('
string|"'name'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'aggregate_identifier'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"No aggregate id or name specified for this "'
nl|'\n'
string|'"notification and it will be ignored"'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'notifier'
op|'='
name|'rpc'
op|'.'
name|'get_notifier'
op|'('
name|'service'
op|'='
string|"'aggregate'"
op|','
nl|'\n'
name|'host'
op|'='
name|'aggregate_identifier'
op|')'
newline|'\n'
nl|'\n'
name|'notifier'
op|'.'
name|'info'
op|'('
name|'context'
op|','
string|"'aggregate.%s'"
op|'%'
name|'event_suffix'
op|','
name|'aggregate_payload'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify_about_host_update
dedent|''
name|'def'
name|'notify_about_host_update'
op|'('
name|'context'
op|','
name|'event_suffix'
op|','
name|'host_payload'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Send a notification about host update.\n\n    :param event_suffix: Event type like "create.start" or "create.end"\n    :param host_payload: payload for host update. It is a dict and there\n                         should be at least the \'host_name\' key in this\n                         dict.\n    """'
newline|'\n'
name|'host_identifier'
op|'='
name|'host_payload'
op|'.'
name|'get'
op|'('
string|"'host_name'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'host_identifier'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"No host name specified for the notification of "'
nl|'\n'
string|'"HostAPI.%s and it will be ignored"'
op|')'
op|','
name|'event_suffix'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'notifier'
op|'='
name|'rpc'
op|'.'
name|'get_notifier'
op|'('
name|'service'
op|'='
string|"'api'"
op|','
name|'host'
op|'='
name|'host_identifier'
op|')'
newline|'\n'
nl|'\n'
name|'notifier'
op|'.'
name|'info'
op|'('
name|'context'
op|','
string|"'HostAPI.%s'"
op|'%'
name|'event_suffix'
op|','
name|'host_payload'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_nw_info_for_instance
dedent|''
name|'def'
name|'get_nw_info_for_instance'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'isinstance'
op|'('
name|'instance'
op|','
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'instance'
op|'.'
name|'info_cache'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'.'
name|'hydrate'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'instance'
op|'.'
name|'info_cache'
op|'.'
name|'network_info'
newline|'\n'
comment|'# FIXME(comstud): Transitional while we convert to objects.'
nl|'\n'
dedent|''
name|'info_cache'
op|'='
name|'instance'
op|'['
string|"'info_cache'"
op|']'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'nw_info'
op|'='
name|'info_cache'
op|'.'
name|'get'
op|'('
string|"'network_info'"
op|')'
name|'or'
op|'['
op|']'
newline|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'nw_info'
op|','
name|'network_model'
op|'.'
name|'NetworkInfo'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nw_info'
op|'='
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'.'
name|'hydrate'
op|'('
name|'nw_info'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'nw_info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|has_audit_been_run
dedent|''
name|'def'
name|'has_audit_been_run'
op|'('
name|'context'
op|','
name|'conductor'
op|','
name|'host'
op|','
name|'timestamp'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'begin'
op|','
name|'end'
op|'='
name|'utils'
op|'.'
name|'last_completed_audit_period'
op|'('
name|'before'
op|'='
name|'timestamp'
op|')'
newline|'\n'
name|'task_log'
op|'='
name|'conductor'
op|'.'
name|'task_log_get'
op|'('
name|'context'
op|','
string|'"instance_usage_audit"'
op|','
nl|'\n'
name|'begin'
op|','
name|'end'
op|','
name|'host'
op|')'
newline|'\n'
name|'if'
name|'task_log'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|start_instance_usage_audit
dedent|''
dedent|''
name|'def'
name|'start_instance_usage_audit'
op|'('
name|'context'
op|','
name|'conductor'
op|','
name|'begin'
op|','
name|'end'
op|','
name|'host'
op|','
nl|'\n'
name|'num_instances'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conductor'
op|'.'
name|'task_log_begin_task'
op|'('
name|'context'
op|','
string|'"instance_usage_audit"'
op|','
name|'begin'
op|','
nl|'\n'
name|'end'
op|','
name|'host'
op|','
name|'num_instances'
op|','
nl|'\n'
string|'"Instance usage audit started..."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|finish_instance_usage_audit
dedent|''
name|'def'
name|'finish_instance_usage_audit'
op|'('
name|'context'
op|','
name|'conductor'
op|','
name|'begin'
op|','
name|'end'
op|','
name|'host'
op|','
name|'errors'
op|','
nl|'\n'
name|'message'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conductor'
op|'.'
name|'task_log_end_task'
op|'('
name|'context'
op|','
string|'"instance_usage_audit"'
op|','
name|'begin'
op|','
name|'end'
op|','
nl|'\n'
name|'host'
op|','
name|'errors'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|usage_volume_info
dedent|''
name|'def'
name|'usage_volume_info'
op|'('
name|'vol_usage'
op|')'
op|':'
newline|'\n'
DECL|function|null_safe_str
indent|'    '
name|'def'
name|'null_safe_str'
op|'('
name|'s'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'s'
op|')'
name|'if'
name|'s'
name|'else'
string|"''"
newline|'\n'
nl|'\n'
dedent|''
name|'tot_refreshed'
op|'='
name|'vol_usage'
op|'['
string|"'tot_last_refreshed'"
op|']'
newline|'\n'
name|'curr_refreshed'
op|'='
name|'vol_usage'
op|'['
string|"'curr_last_refreshed'"
op|']'
newline|'\n'
name|'if'
name|'tot_refreshed'
name|'and'
name|'curr_refreshed'
op|':'
newline|'\n'
indent|'        '
name|'last_refreshed_time'
op|'='
name|'max'
op|'('
name|'tot_refreshed'
op|','
name|'curr_refreshed'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'tot_refreshed'
op|':'
newline|'\n'
indent|'        '
name|'last_refreshed_time'
op|'='
name|'tot_refreshed'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# curr_refreshed must be set'
nl|'\n'
indent|'        '
name|'last_refreshed_time'
op|'='
name|'curr_refreshed'
newline|'\n'
nl|'\n'
dedent|''
name|'usage_info'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'volume_id'
op|'='
name|'vol_usage'
op|'['
string|"'volume_id'"
op|']'
op|','
nl|'\n'
name|'tenant_id'
op|'='
name|'vol_usage'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'vol_usage'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
name|'availability_zone'
op|'='
name|'vol_usage'
op|'['
string|"'availability_zone'"
op|']'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'vol_usage'
op|'['
string|"'instance_uuid'"
op|']'
op|','
nl|'\n'
name|'last_refreshed'
op|'='
name|'null_safe_str'
op|'('
name|'last_refreshed_time'
op|')'
op|','
nl|'\n'
name|'reads'
op|'='
name|'vol_usage'
op|'['
string|"'tot_reads'"
op|']'
op|'+'
name|'vol_usage'
op|'['
string|"'curr_reads'"
op|']'
op|','
nl|'\n'
name|'read_bytes'
op|'='
name|'vol_usage'
op|'['
string|"'tot_read_bytes'"
op|']'
op|'+'
nl|'\n'
name|'vol_usage'
op|'['
string|"'curr_read_bytes'"
op|']'
op|','
nl|'\n'
name|'writes'
op|'='
name|'vol_usage'
op|'['
string|"'tot_writes'"
op|']'
op|'+'
name|'vol_usage'
op|'['
string|"'curr_writes'"
op|']'
op|','
nl|'\n'
name|'write_bytes'
op|'='
name|'vol_usage'
op|'['
string|"'tot_write_bytes'"
op|']'
op|'+'
nl|'\n'
name|'vol_usage'
op|'['
string|"'curr_write_bytes'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'usage_info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_reboot_type
dedent|''
name|'def'
name|'get_reboot_type'
op|'('
name|'task_state'
op|','
name|'current_power_state'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Checks if the current instance state requires a HARD reboot."""'
newline|'\n'
name|'if'
name|'current_power_state'
op|'!='
name|'power_state'
op|'.'
name|'RUNNING'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'HARD'"
newline|'\n'
dedent|''
name|'soft_types'
op|'='
op|'['
name|'task_states'
op|'.'
name|'REBOOT_STARTED'
op|','
name|'task_states'
op|'.'
name|'REBOOT_PENDING'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'REBOOTING'
op|']'
newline|'\n'
name|'reboot_type'
op|'='
string|"'SOFT'"
name|'if'
name|'task_state'
name|'in'
name|'soft_types'
name|'else'
string|"'HARD'"
newline|'\n'
name|'return'
name|'reboot_type'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_machine_ips
dedent|''
name|'def'
name|'get_machine_ips'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the machine\'s ip addresses\n\n    :returns: list of Strings of ip addresses\n    """'
newline|'\n'
name|'addresses'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'interface'
name|'in'
name|'netifaces'
op|'.'
name|'interfaces'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'iface_data'
op|'='
name|'netifaces'
op|'.'
name|'ifaddresses'
op|'('
name|'interface'
op|')'
newline|'\n'
name|'for'
name|'family'
name|'in'
name|'iface_data'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'family'
name|'not'
name|'in'
op|'('
name|'netifaces'
op|'.'
name|'AF_INET'
op|','
name|'netifaces'
op|'.'
name|'AF_INET6'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'for'
name|'address'
name|'in'
name|'iface_data'
op|'['
name|'family'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'addr'
op|'='
name|'address'
op|'['
string|"'addr'"
op|']'
newline|'\n'
nl|'\n'
comment|'# If we have an ipv6 address remove the'
nl|'\n'
comment|'# %ether_interface at the end'
nl|'\n'
name|'if'
name|'family'
op|'=='
name|'netifaces'
op|'.'
name|'AF_INET6'
op|':'
newline|'\n'
indent|'                        '
name|'addr'
op|'='
name|'addr'
op|'.'
name|'split'
op|'('
string|"'%'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'addresses'
op|'.'
name|'append'
op|'('
name|'addr'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'addresses'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|EventReporter
dedent|''
name|'class'
name|'EventReporter'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Context manager to report instance action events."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'event_name'
op|','
op|'*'
name|'instance_uuids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
newline|'\n'
name|'self'
op|'.'
name|'event_name'
op|'='
name|'event_name'
newline|'\n'
name|'self'
op|'.'
name|'instance_uuids'
op|'='
name|'instance_uuids'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'uuid'
name|'in'
name|'self'
op|'.'
name|'instance_uuids'
op|':'
newline|'\n'
indent|'            '
name|'objects'
op|'.'
name|'InstanceActionEvent'
op|'.'
name|'event_start'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'uuid'
op|','
name|'self'
op|'.'
name|'event_name'
op|','
name|'want_result'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
name|'exc_type'
op|','
name|'exc_val'
op|','
name|'exc_tb'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'uuid'
name|'in'
name|'self'
op|'.'
name|'instance_uuids'
op|':'
newline|'\n'
indent|'            '
name|'objects'
op|'.'
name|'InstanceActionEvent'
op|'.'
name|'event_finish_with_failure'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'uuid'
op|','
name|'self'
op|'.'
name|'event_name'
op|','
name|'exc_val'
op|'='
name|'exc_val'
op|','
nl|'\n'
name|'exc_tb'
op|'='
name|'exc_tb'
op|','
name|'want_result'
op|'='
name|'False'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UnlimitedSemaphore
dedent|''
dedent|''
name|'class'
name|'UnlimitedSemaphore'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__enter__
indent|'    '
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|balance
name|'def'
name|'balance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'0'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
