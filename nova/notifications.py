begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 OpenStack, LLC.'
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
string|'"""Functionality related to notifications common to multiple layers of\nthe system.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'network'
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
op|'.'
name|'notifier'
name|'import'
name|'api'
name|'as'
name|'notifier_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
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
DECL|variable|notify_state_opt
name|'notify_state_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'notify_on_state_change'"
op|','
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'If set, send compute.instance.update notifications on instance '"
nl|'\n'
string|"'state changes.  Valid values are None for no notifications, '"
nl|'\n'
string|'\'"vm_state" for notifications on VM state changes, or \''
nl|'\n'
string|'\'"vm_and_task_state" for notifications on VM and task state \''
nl|'\n'
string|"'changes.'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opt'
op|'('
name|'notify_state_opt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|send_update
name|'def'
name|'send_update'
op|'('
name|'context'
op|','
name|'old_instance'
op|','
name|'new_instance'
op|','
name|'service'
op|'='
name|'None'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Send compute.instance.update notification to report changes\n    in vm state and (optionally) task state\n    """'
newline|'\n'
nl|'\n'
name|'send_update_with_states'
op|'('
name|'context'
op|','
name|'new_instance'
op|','
name|'old_instance'
op|'['
string|'"vm_state"'
op|']'
op|','
nl|'\n'
name|'new_instance'
op|'['
string|'"vm_state"'
op|']'
op|','
name|'old_instance'
op|'['
string|'"task_state"'
op|']'
op|','
nl|'\n'
name|'new_instance'
op|'['
string|'"task_state"'
op|']'
op|','
name|'service'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|send_update_with_states
dedent|''
name|'def'
name|'send_update_with_states'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'old_vm_state'
op|','
name|'new_vm_state'
op|','
nl|'\n'
name|'old_task_state'
op|','
name|'new_task_state'
op|','
name|'service'
op|'='
name|'None'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Send compute.instance.update notification to report changes\n    in vm state and (optionally) task state\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'notify_on_state_change'
op|':'
newline|'\n'
comment|'# skip all this if state updates are disabled'
nl|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'fire_update'
op|'='
name|'False'
newline|'\n'
nl|'\n'
name|'if'
name|'old_vm_state'
op|'!='
name|'new_vm_state'
op|':'
newline|'\n'
comment|'# yes, the vm state is changing:'
nl|'\n'
indent|'        '
name|'fire_update'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'FLAGS'
op|'.'
name|'notify_on_state_change'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|'"vm_and_task_state"'
name|'and'
nl|'\n'
name|'old_task_state'
op|'!='
name|'new_task_state'
op|')'
op|':'
newline|'\n'
comment|'# yes, the task state is changing:'
nl|'\n'
indent|'        '
name|'fire_update'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'fire_update'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'_send_instance_update_notification'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'old_vm_state'
op|','
nl|'\n'
name|'old_task_state'
op|','
name|'new_vm_state'
op|','
name|'new_task_state'
op|','
name|'service'
op|','
nl|'\n'
name|'host'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Failed to send state update notification"'
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_send_instance_update_notification
dedent|''
dedent|''
dedent|''
name|'def'
name|'_send_instance_update_notification'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'old_vm_state'
op|','
nl|'\n'
name|'old_task_state'
op|','
name|'new_vm_state'
op|','
name|'new_task_state'
op|','
name|'service'
op|'='
name|'None'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Send \'compute.instance.exists\' notification to inform observers\n    about instance state changes"""'
newline|'\n'
nl|'\n'
name|'payload'
op|'='
name|'usage_from_instance'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'states_payload'
op|'='
op|'{'
nl|'\n'
string|'"old_state"'
op|':'
name|'old_vm_state'
op|','
nl|'\n'
string|'"state"'
op|':'
name|'new_vm_state'
op|','
nl|'\n'
string|'"old_task_state"'
op|':'
name|'old_task_state'
op|','
nl|'\n'
string|'"new_task_state"'
op|':'
name|'new_task_state'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'payload'
op|'.'
name|'update'
op|'('
name|'states_payload'
op|')'
newline|'\n'
nl|'\n'
comment|'# add audit fields:'
nl|'\n'
op|'('
name|'audit_start'
op|','
name|'audit_end'
op|')'
op|'='
name|'audit_period_bounds'
op|'('
name|'current_period'
op|'='
name|'True'
op|')'
newline|'\n'
name|'payload'
op|'['
string|'"audit_period_beginning"'
op|']'
op|'='
name|'audit_start'
newline|'\n'
name|'payload'
op|'['
string|'"audit_period_ending"'
op|']'
op|'='
name|'audit_end'
newline|'\n'
nl|'\n'
comment|'# add bw usage info:'
nl|'\n'
name|'bw'
op|'='
name|'bandwidth_usage'
op|'('
name|'instance'
op|','
name|'audit_start'
op|')'
newline|'\n'
name|'payload'
op|'['
string|'"bandwidth"'
op|']'
op|'='
name|'bw'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'system_metadata'
op|'='
name|'db'
op|'.'
name|'instance_system_metadata_get'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|'.'
name|'uuid'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'        '
name|'system_metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|'# add image metadata'
nl|'\n'
dedent|''
name|'image_meta_props'
op|'='
name|'image_meta'
op|'('
name|'system_metadata'
op|')'
newline|'\n'
name|'payload'
op|'['
string|'"image_meta"'
op|']'
op|'='
name|'image_meta_props'
newline|'\n'
nl|'\n'
comment|'# if the service name (e.g. api/scheduler/compute) is not provided, default'
nl|'\n'
comment|'# to "compute"'
nl|'\n'
name|'if'
name|'not'
name|'service'
op|':'
newline|'\n'
indent|'        '
name|'service'
op|'='
string|'"compute"'
newline|'\n'
nl|'\n'
dedent|''
name|'publisher_id'
op|'='
name|'notifier_api'
op|'.'
name|'publisher_id'
op|'('
name|'service'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
name|'notifier_api'
op|'.'
name|'notify'
op|'('
name|'context'
op|','
name|'publisher_id'
op|','
string|"'compute.instance.update'"
op|','
nl|'\n'
name|'notifier_api'
op|'.'
name|'INFO'
op|','
name|'payload'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|audit_period_bounds
dedent|''
name|'def'
name|'audit_period_bounds'
op|'('
name|'current_period'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the start and end of the relevant audit usage period\n\n    :param current_period: if True, this will generate a usage for the\n        current usage period; if False, this will generate a usage for the\n        previous audit period.\n    """'
newline|'\n'
nl|'\n'
name|'begin'
op|','
name|'end'
op|'='
name|'utils'
op|'.'
name|'last_completed_audit_period'
op|'('
op|')'
newline|'\n'
name|'if'
name|'current_period'
op|':'
newline|'\n'
indent|'        '
name|'audit_start'
op|'='
name|'end'
newline|'\n'
name|'audit_end'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'audit_start'
op|'='
name|'begin'
newline|'\n'
name|'audit_end'
op|'='
name|'end'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
name|'audit_start'
op|','
name|'audit_end'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bandwidth_usage
dedent|''
name|'def'
name|'bandwidth_usage'
op|'('
name|'instance_ref'
op|','
name|'audit_start'
op|','
nl|'\n'
name|'ignore_missing_network_data'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get bandwidth usage information for the instance for the\n    specified audit period.\n    """'
newline|'\n'
nl|'\n'
name|'admin_context'
op|'='
name|'nova'
op|'.'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
name|'read_deleted'
op|'='
string|"'yes'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
op|'('
name|'instance_ref'
op|'.'
name|'get'
op|'('
string|"'info_cache'"
op|')'
name|'and'
nl|'\n'
name|'instance_ref'
op|'['
string|"'info_cache'"
op|']'
op|'.'
name|'get'
op|'('
string|"'network_info'"
op|')'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'cached_info'
op|'='
name|'instance_ref'
op|'['
string|"'info_cache'"
op|']'
op|'['
string|"'network_info'"
op|']'
newline|'\n'
name|'nw_info'
op|'='
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'.'
name|'hydrate'
op|'('
name|'cached_info'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'nw_info'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'get_instance_nw_info'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'instance_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
string|"'Failed to get nw_info'"
op|','
name|'instance'
op|'='
name|'instance_ref'
op|')'
newline|'\n'
name|'if'
name|'ignore_missing_network_data'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'macs'
op|'='
op|'['
name|'vif'
op|'['
string|"'address'"
op|']'
name|'for'
name|'vif'
name|'in'
name|'nw_info'
op|']'
newline|'\n'
name|'uuids'
op|'='
op|'['
name|'instance_ref'
op|'['
string|'"uuid"'
op|']'
op|']'
newline|'\n'
nl|'\n'
name|'bw_usages'
op|'='
name|'db'
op|'.'
name|'bw_usage_get_by_uuids'
op|'('
name|'admin_context'
op|','
name|'uuids'
op|','
name|'audit_start'
op|')'
newline|'\n'
name|'bw_usages'
op|'='
op|'['
name|'b'
name|'for'
name|'b'
name|'in'
name|'bw_usages'
name|'if'
name|'b'
op|'.'
name|'mac'
name|'in'
name|'macs'
op|']'
newline|'\n'
nl|'\n'
name|'bw'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'b'
name|'in'
name|'bw_usages'
op|':'
newline|'\n'
indent|'        '
name|'label'
op|'='
string|"'net-name-not-found-%s'"
op|'%'
name|'b'
op|'['
string|"'mac'"
op|']'
newline|'\n'
name|'for'
name|'vif'
name|'in'
name|'nw_info'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'vif'
op|'['
string|"'address'"
op|']'
op|'=='
name|'b'
op|'['
string|"'mac'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'label'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'label'"
op|']'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'bw'
op|'['
name|'label'
op|']'
op|'='
name|'dict'
op|'('
name|'bw_in'
op|'='
name|'b'
op|'.'
name|'bw_in'
op|','
name|'bw_out'
op|'='
name|'b'
op|'.'
name|'bw_out'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'bw'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|image_meta
dedent|''
name|'def'
name|'image_meta'
op|'('
name|'system_metadata'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Format image metadata for use in notifications from the instance\n    system metadata.\n    """'
newline|'\n'
name|'image_meta'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'md_key'
op|','
name|'md_value'
name|'in'
name|'system_metadata'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'md_key'
op|'.'
name|'startswith'
op|'('
string|"'image_'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|'['
name|'md_key'
op|'['
number|'6'
op|':'
op|']'
op|']'
op|'='
name|'md_value'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'image_meta'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|usage_from_instance
dedent|''
name|'def'
name|'usage_from_instance'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
name|'network_info'
op|','
nl|'\n'
name|'system_metadata'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get usage information for an instance which is common to all\n    notifications.\n\n    :param network_info: network_info provided if not None\n    :param system_metadata: system_metadata DB entries for the instance,\n    if not None.  *NOTE*: Currently unused here in trunk, but needed for\n    potential custom modifications.\n    """'
newline|'\n'
nl|'\n'
DECL|function|null_safe_str
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
name|'image_ref_url'
op|'='
name|'utils'
op|'.'
name|'generate_image_url'
op|'('
name|'instance_ref'
op|'['
string|"'image_ref'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'instance_type_name'
op|'='
name|'instance_ref'
op|'.'
name|'get'
op|'('
string|"'instance_type'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
string|"'name'"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
name|'usage_info'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'tenant_id'
op|'='
name|'instance_ref'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'instance_ref'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_ref'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'instance_type'
op|'='
name|'instance_type_name'
op|','
nl|'\n'
name|'instance_type_id'
op|'='
name|'instance_ref'
op|'['
string|"'instance_type_id'"
op|']'
op|','
nl|'\n'
name|'memory_mb'
op|'='
name|'instance_ref'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
name|'disk_gb'
op|'='
name|'instance_ref'
op|'['
string|"'root_gb'"
op|']'
op|'+'
name|'instance_ref'
op|'['
string|"'ephemeral_gb'"
op|']'
op|','
nl|'\n'
name|'display_name'
op|'='
name|'instance_ref'
op|'['
string|"'display_name'"
op|']'
op|','
nl|'\n'
name|'created_at'
op|'='
name|'str'
op|'('
name|'instance_ref'
op|'['
string|"'created_at'"
op|']'
op|')'
op|','
nl|'\n'
comment|"# Nova's deleted vs terminated instance terminology is confusing,"
nl|'\n'
comment|'# this should be when the instance was deleted (i.e. terminated_at),'
nl|'\n'
comment|'# not when the db record was deleted. (mdragon)'
nl|'\n'
name|'deleted_at'
op|'='
name|'null_safe_str'
op|'('
name|'instance_ref'
op|'.'
name|'get'
op|'('
string|"'terminated_at'"
op|')'
op|')'
op|','
nl|'\n'
name|'launched_at'
op|'='
name|'null_safe_str'
op|'('
name|'instance_ref'
op|'.'
name|'get'
op|'('
string|"'launched_at'"
op|')'
op|')'
op|','
nl|'\n'
name|'image_ref_url'
op|'='
name|'image_ref_url'
op|','
nl|'\n'
name|'state'
op|'='
name|'instance_ref'
op|'['
string|"'vm_state'"
op|']'
op|','
nl|'\n'
name|'state_description'
op|'='
name|'null_safe_str'
op|'('
name|'instance_ref'
op|'.'
name|'get'
op|'('
string|"'task_state'"
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'network_info'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'usage_info'
op|'['
string|"'fixed_ips'"
op|']'
op|'='
name|'network_info'
op|'.'
name|'fixed_ips'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'usage_info'
op|'.'
name|'update'
op|'('
name|'kw'
op|')'
newline|'\n'
name|'return'
name|'usage_info'
newline|'\n'
dedent|''
endmarker|''
end_unit
