begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 OpenStack Foundation'
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
string|'"""Tests for common notifcations."""'
newline|'\n'
nl|'\n'
name|'import'
name|'copy'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'flavors'
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
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'api'
name|'as'
name|'network_api'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'notifications'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
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
op|'.'
name|'notifier'
name|'import'
name|'test_notifier'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_network'
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
string|"'compute_driver'"
op|','
string|"'nova.virt.driver'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotificationsTestCase
name|'class'
name|'NotificationsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NotificationsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'net_info'
op|'='
name|'fake_network'
op|'.'
name|'fake_get_instance_nw_info'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
number|'1'
op|','
nl|'\n'
number|'1'
op|','
name|'spectacular'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_get_nw_info
name|'def'
name|'fake_get_nw_info'
op|'('
name|'cls'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'ctxt'
op|'.'
name|'is_admin'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'net_info'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network_api'
op|'.'
name|'API'
op|','
string|"'get_instance_nw_info'"
op|','
nl|'\n'
name|'fake_get_nw_info'
op|')'
newline|'\n'
name|'fake_network'
op|'.'
name|'set_stub_network_methods'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
name|'notifier_api'
op|'.'
name|'_reset_drivers'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'notifier_api'
op|'.'
name|'_reset_drivers'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'compute_driver'
op|'='
string|"'nova.virt.fake.FakeDriver'"
op|','
nl|'\n'
name|'notification_driver'
op|'='
op|'['
name|'test_notifier'
op|'.'
name|'__name__'
op|']'
op|','
nl|'\n'
name|'network_manager'
op|'='
string|"'nova.network.manager.FlatManager'"
op|','
nl|'\n'
name|'notify_on_state_change'
op|'='
string|'"vm_and_task_state"'
op|','
nl|'\n'
name|'host'
op|'='
string|"'testhost'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'user_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_wrapped_create'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_wrapped_create
dedent|''
name|'def'
name|'_wrapped_create'
op|'('
name|'self'
op|','
name|'params'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_type'
op|'='
name|'flavors'
op|'.'
name|'get_instance_type_by_name'
op|'('
string|"'m1.tiny'"
op|')'
newline|'\n'
name|'sys_meta'
op|'='
name|'flavors'
op|'.'
name|'save_instance_type_info'
op|'('
op|'{'
op|'}'
op|','
name|'instance_type'
op|')'
newline|'\n'
name|'inst'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'inst'
op|'['
string|"'image_ref'"
op|']'
op|'='
number|'1'
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'user_id'
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'project_id'
newline|'\n'
name|'inst'
op|'['
string|"'instance_type_id'"
op|']'
op|'='
name|'instance_type'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'root_gb'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'['
string|"'ephemeral_gb'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'['
string|"'access_ip_v4'"
op|']'
op|'='
string|"'1.2.3.4'"
newline|'\n'
name|'inst'
op|'['
string|"'access_ip_v6'"
op|']'
op|'='
string|"'feed:5eed'"
newline|'\n'
name|'inst'
op|'['
string|"'display_name'"
op|']'
op|'='
string|"'test_instance'"
newline|'\n'
name|'inst'
op|'['
string|"'hostname'"
op|']'
op|'='
string|"'test_instance_hostname'"
newline|'\n'
name|'inst'
op|'['
string|"'system_metadata'"
op|']'
op|'='
name|'sys_meta'
newline|'\n'
name|'if'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'inst'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_send_api_fault_disabled
dedent|''
name|'def'
name|'test_send_api_fault_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'notify_api_faults'
op|'='
name|'False'
op|')'
newline|'\n'
name|'notifications'
op|'.'
name|'send_api_fault'
op|'('
string|'"http://example.com/foo"'
op|','
number|'500'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_send_api_fault
dedent|''
name|'def'
name|'test_send_api_fault'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'notify_api_faults'
op|'='
name|'True'
op|')'
newline|'\n'
name|'exception'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# Get a real exception with a call stack.'
nl|'\n'
indent|'            '
name|'raise'
name|'test'
op|'.'
name|'TestingException'
op|'('
string|'"junk"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'test'
op|'.'
name|'TestingException'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'exception'
op|'='
name|'e'
newline|'\n'
nl|'\n'
dedent|''
name|'notifications'
op|'.'
name|'send_api_fault'
op|'('
string|'"http://example.com/foo"'
op|','
number|'500'
op|','
name|'exception'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
name|'n'
op|'='
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'n'
op|'['
string|"'priority'"
op|']'
op|','
string|"'ERROR'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'n'
op|'['
string|"'event_type'"
op|']'
op|','
string|"'api.fault'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'n'
op|'['
string|"'payload'"
op|']'
op|'['
string|"'url'"
op|']'
op|','
string|"'http://example.com/foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'n'
op|'['
string|"'payload'"
op|']'
op|'['
string|"'status'"
op|']'
op|','
number|'500'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'n'
op|'['
string|"'payload'"
op|']'
op|'['
string|"'exception'"
op|']'
name|'is'
name|'not'
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_notif_disabled
dedent|''
name|'def'
name|'test_notif_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# test config disable of the notifcations'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'notify_on_state_change'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'notify_on_any_change'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'old'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|'"vm_state"'
op|']'
op|'='
name|'vm_states'
op|'.'
name|'ACTIVE'
newline|'\n'
nl|'\n'
name|'old_vm_state'
op|'='
name|'old'
op|'['
string|"'vm_state'"
op|']'
newline|'\n'
name|'new_vm_state'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"vm_state"'
op|']'
newline|'\n'
name|'old_task_state'
op|'='
name|'old'
op|'['
string|"'task_state'"
op|']'
newline|'\n'
name|'new_task_state'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"task_state"'
op|']'
newline|'\n'
nl|'\n'
name|'notifications'
op|'.'
name|'send_update_with_states'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'old_vm_state'
op|','
name|'new_vm_state'
op|','
name|'old_task_state'
op|','
name|'new_task_state'
op|','
nl|'\n'
name|'verify_states'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'old'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_task_notif
dedent|''
name|'def'
name|'test_task_notif'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# test config disable of just the task state notifications'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'notify_on_state_change'
op|'='
string|'"vm_state"'
op|')'
newline|'\n'
nl|'\n'
comment|'# we should not get a notification on task stgate chagne now'
nl|'\n'
name|'old'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|'"task_state"'
op|']'
op|'='
name|'task_states'
op|'.'
name|'SPAWNING'
newline|'\n'
nl|'\n'
name|'old_vm_state'
op|'='
name|'old'
op|'['
string|"'vm_state'"
op|']'
newline|'\n'
name|'new_vm_state'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"vm_state"'
op|']'
newline|'\n'
name|'old_task_state'
op|'='
name|'old'
op|'['
string|"'task_state'"
op|']'
newline|'\n'
name|'new_task_state'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"task_state"'
op|']'
newline|'\n'
nl|'\n'
name|'notifications'
op|'.'
name|'send_update_with_states'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'old_vm_state'
op|','
name|'new_vm_state'
op|','
name|'old_task_state'
op|','
name|'new_task_state'
op|','
nl|'\n'
name|'verify_states'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# ok now enable task state notifcations and re-try'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'notify_on_state_change'
op|'='
string|'"vm_and_task_state"'
op|')'
newline|'\n'
nl|'\n'
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'old'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_send_no_notif
dedent|''
name|'def'
name|'test_send_no_notif'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# test notification on send no initial vm state:'
nl|'\n'
indent|'        '
name|'old_vm_state'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|"'vm_state'"
op|']'
newline|'\n'
name|'new_vm_state'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|"'vm_state'"
op|']'
newline|'\n'
name|'old_task_state'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|"'task_state'"
op|']'
newline|'\n'
name|'new_task_state'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|"'task_state'"
op|']'
newline|'\n'
nl|'\n'
name|'notifications'
op|'.'
name|'send_update_with_states'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'old_vm_state'
op|','
name|'new_vm_state'
op|','
name|'old_task_state'
op|','
name|'new_task_state'
op|','
nl|'\n'
name|'service'
op|'='
string|'"compute"'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'verify_states'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_send_on_vm_change
dedent|''
name|'def'
name|'test_send_on_vm_change'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# pretend we just transitioned to ACTIVE:'
nl|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|'"vm_state"'
op|':'
name|'vm_states'
op|'.'
name|'ACTIVE'
op|'}'
newline|'\n'
op|'('
name|'old_ref'
op|','
name|'new_ref'
op|')'
op|'='
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'params'
op|')'
newline|'\n'
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'old_ref'
op|','
name|'new_ref'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_send_on_task_change
dedent|''
name|'def'
name|'test_send_on_task_change'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# pretend we just transitioned to task SPAWNING:'
nl|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|'"task_state"'
op|':'
name|'task_states'
op|'.'
name|'SPAWNING'
op|'}'
newline|'\n'
op|'('
name|'old_ref'
op|','
name|'new_ref'
op|')'
op|'='
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'params'
op|')'
newline|'\n'
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'old_ref'
op|','
name|'new_ref'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_update_with_states
dedent|''
name|'def'
name|'test_no_update_with_states'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'notifications'
op|'.'
name|'send_update_with_states'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
name|'verify_states'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vm_update_with_states
dedent|''
name|'def'
name|'test_vm_update_with_states'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'notifications'
op|'.'
name|'send_update_with_states'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'vm_states'
op|'.'
name|'ACTIVE'
op|','
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
name|'verify_states'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
name|'notif'
op|'='
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'0'
op|']'
newline|'\n'
name|'payload'
op|'='
name|'notif'
op|'['
string|'"payload"'
op|']'
newline|'\n'
name|'access_ip_v4'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"access_ip_v4"'
op|']'
newline|'\n'
name|'access_ip_v6'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"access_ip_v6"'
op|']'
newline|'\n'
name|'display_name'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"display_name"'
op|']'
newline|'\n'
name|'hostname'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"hostname"'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'payload'
op|'['
string|'"old_state"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm_states'
op|'.'
name|'ACTIVE'
op|','
name|'payload'
op|'['
string|'"state"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
name|'payload'
op|'['
string|'"old_task_state"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
name|'payload'
op|'['
string|'"new_task_state"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|'"access_ip_v4"'
op|']'
op|','
name|'access_ip_v4'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|'"access_ip_v6"'
op|']'
op|','
name|'access_ip_v6'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|'"display_name"'
op|']'
op|','
name|'display_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|'"hostname"'
op|']'
op|','
name|'hostname'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_task_update_with_states
dedent|''
name|'def'
name|'test_task_update_with_states'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'notify_on_state_change'
op|'='
string|'"vm_and_task_state"'
op|')'
newline|'\n'
nl|'\n'
name|'notifications'
op|'.'
name|'send_update_with_states'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
nl|'\n'
name|'None'
op|','
name|'verify_states'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
name|'notif'
op|'='
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'0'
op|']'
newline|'\n'
name|'payload'
op|'='
name|'notif'
op|'['
string|'"payload"'
op|']'
newline|'\n'
name|'access_ip_v4'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"access_ip_v4"'
op|']'
newline|'\n'
name|'access_ip_v6'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"access_ip_v6"'
op|']'
newline|'\n'
name|'display_name'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"display_name"'
op|']'
newline|'\n'
name|'hostname'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"hostname"'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'payload'
op|'['
string|'"old_state"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'payload'
op|'['
string|'"state"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
name|'payload'
op|'['
string|'"old_task_state"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'None'
op|','
name|'payload'
op|'['
string|'"new_task_state"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|'"access_ip_v4"'
op|']'
op|','
name|'access_ip_v4'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|'"access_ip_v6"'
op|']'
op|','
name|'access_ip_v6'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|'"display_name"'
op|']'
op|','
name|'display_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|'"hostname"'
op|']'
op|','
name|'hostname'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_no_service_name
dedent|''
name|'def'
name|'test_update_no_service_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'notifications'
op|'.'
name|'send_update_with_states'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
nl|'\n'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# service name should default to 'compute'"
nl|'\n'
name|'notif'
op|'='
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'compute.testhost'"
op|','
name|'notif'
op|'['
string|"'publisher_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_with_service_name
dedent|''
name|'def'
name|'test_update_with_service_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'notifications'
op|'.'
name|'send_update_with_states'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
nl|'\n'
name|'None'
op|','
name|'service'
op|'='
string|'"testservice"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# service name should default to 'compute'"
nl|'\n'
name|'notif'
op|'='
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'testservice.testhost'"
op|','
name|'notif'
op|'['
string|"'publisher_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_with_host_name
dedent|''
name|'def'
name|'test_update_with_host_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'notifications'
op|'.'
name|'send_update_with_states'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
nl|'\n'
name|'None'
op|','
name|'host'
op|'='
string|'"someotherhost"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# service name should default to 'compute'"
nl|'\n'
name|'notif'
op|'='
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'compute.someotherhost'"
op|','
name|'notif'
op|'['
string|"'publisher_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_payload_has_fixed_ip_labels
dedent|''
name|'def'
name|'test_payload_has_fixed_ip_labels'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
name|'notifications'
op|'.'
name|'info_from_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'self'
op|'.'
name|'net_info'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"fixed_ips"'
name|'in'
name|'info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'info'
op|'['
string|'"fixed_ips"'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|'"label"'
op|']'
op|','
string|'"test1"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_send_access_ip_update
dedent|''
name|'def'
name|'test_send_access_ip_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
name|'notif'
op|'='
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'0'
op|']'
newline|'\n'
name|'payload'
op|'='
name|'notif'
op|'['
string|'"payload"'
op|']'
newline|'\n'
name|'access_ip_v4'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"access_ip_v4"'
op|']'
newline|'\n'
name|'access_ip_v6'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"access_ip_v6"'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|'"access_ip_v4"'
op|']'
op|','
name|'access_ip_v4'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|'"access_ip_v6"'
op|']'
op|','
name|'access_ip_v6'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_send_name_update
dedent|''
name|'def'
name|'test_send_name_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
name|'notif'
op|'='
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'0'
op|']'
newline|'\n'
name|'payload'
op|'='
name|'notif'
op|'['
string|'"payload"'
op|']'
newline|'\n'
name|'display_name'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|'"display_name"'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|'"display_name"'
op|']'
op|','
name|'display_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_send_no_state_change
dedent|''
name|'def'
name|'test_send_no_state_change'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'called'
op|'='
op|'['
name|'False'
op|']'
newline|'\n'
nl|'\n'
DECL|function|sending_no_state_change
name|'def'
name|'sending_no_state_change'
op|'('
name|'context'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'called'
op|'['
number|'0'
op|']'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'notifications'
op|','
string|"'_send_instance_update_notification'"
op|','
nl|'\n'
name|'sending_no_state_change'
op|')'
newline|'\n'
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'called'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fail_sending_update
dedent|''
name|'def'
name|'test_fail_sending_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fail_sending
indent|'        '
name|'def'
name|'fail_sending'
op|'('
name|'context'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|"'failed to notify'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'notifications'
op|','
string|"'_send_instance_update_notification'"
op|','
nl|'\n'
name|'fail_sending'
op|')'
newline|'\n'
nl|'\n'
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
