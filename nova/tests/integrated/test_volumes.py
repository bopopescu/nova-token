begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
name|'unittest'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'log'
name|'import'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'integrated'
name|'import'
name|'integrated_helpers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'integrated'
op|'.'
name|'api'
name|'import'
name|'client'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.integrated'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumesTest
name|'class'
name|'VolumesTest'
op|'('
name|'integrated_helpers'
op|'.'
name|'_IntegratedTestBase'
op|')'
op|':'
newline|'\n'
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
name|'VolumesTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'LoggingVolumeDriver'
op|'.'
name|'clear_logs'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_flags
dedent|''
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'super'
op|'('
name|'VolumesTest'
op|','
name|'self'
op|')'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'f'
op|'['
string|"'use_local_volumes'"
op|']'
op|'='
name|'False'
comment|'# Avoids calling local_path'
newline|'\n'
name|'f'
op|'['
string|"'volume_driver'"
op|']'
op|'='
string|"'nova.volume.driver.LoggingVolumeDriver'"
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|test_get_volumes_summary
dedent|''
name|'def'
name|'test_get_volumes_summary'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Simple check that listing volumes works."""'
newline|'\n'
name|'volumes'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_volumes'
op|'('
name|'False'
op|')'
newline|'\n'
name|'for'
name|'volume'
name|'in'
name|'volumes'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"volume: %s"'
op|'%'
name|'volume'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_volumes
dedent|''
dedent|''
name|'def'
name|'test_get_volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Simple check that listing volumes works."""'
newline|'\n'
name|'volumes'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_volumes'
op|'('
op|')'
newline|'\n'
name|'for'
name|'volume'
name|'in'
name|'volumes'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"volume: %s"'
op|'%'
name|'volume'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_poll_while
dedent|''
dedent|''
name|'def'
name|'_poll_while'
op|'('
name|'self'
op|','
name|'volume_id'
op|','
name|'continue_states'
op|','
name|'max_retries'
op|'='
number|'5'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Poll (briefly) while the state is in continue_states."""'
newline|'\n'
name|'retries'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'found_volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_volume'
op|'('
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'client'
op|'.'
name|'OpenStackApiNotFoundException'
op|':'
newline|'\n'
indent|'                '
name|'found_volume'
op|'='
name|'None'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Got 404, proceeding"'
op|')'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Found %s"'
op|'%'
name|'found_volume'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_id'
op|','
name|'found_volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'found_volume'
op|'['
string|"'status'"
op|']'
name|'in'
name|'continue_states'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
name|'retries'
op|'='
name|'retries'
op|'+'
number|'1'
newline|'\n'
name|'if'
name|'retries'
op|'>'
name|'max_retries'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'found_volume'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_delete_volume
dedent|''
name|'def'
name|'test_create_and_delete_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates and deletes a volume."""'
newline|'\n'
nl|'\n'
comment|'# Create volume'
nl|'\n'
name|'created_volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_volume'
op|'('
op|'{'
string|"'volume'"
op|':'
op|'{'
string|"'size'"
op|':'
number|'1'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"created_volume: %s"'
op|'%'
name|'created_volume'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_volume_id'
op|'='
name|'created_volume'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|"# Check it's there"
nl|'\n'
name|'found_volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_volume'
op|'('
name|'created_volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'created_volume_id'
op|','
name|'found_volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# It should also be in the all-volume list'
nl|'\n'
name|'volumes'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_volumes'
op|'('
op|')'
newline|'\n'
name|'volume_names'
op|'='
op|'['
name|'volume'
op|'['
string|"'id'"
op|']'
name|'for'
name|'volume'
name|'in'
name|'volumes'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_volume_id'
name|'in'
name|'volume_names'
op|')'
newline|'\n'
nl|'\n'
comment|"# Wait (briefly) for creation. Delay is due to the 'message queue'"
nl|'\n'
name|'found_volume'
op|'='
name|'self'
op|'.'
name|'_poll_while'
op|'('
name|'created_volume_id'
op|','
op|'['
string|"'creating'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# It should be available...'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'available'"
op|','
name|'found_volume'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete the volume'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'delete_volume'
op|'('
name|'created_volume_id'
op|')'
newline|'\n'
nl|'\n'
comment|"# Wait (briefly) for deletion. Delay is due to the 'message queue'"
nl|'\n'
name|'found_volume'
op|'='
name|'self'
op|'.'
name|'_poll_while'
op|'('
name|'created_volume_id'
op|','
op|'['
string|"'deleting'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Should be gone'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'found_volume'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Logs: %s"'
op|'%'
name|'driver'
op|'.'
name|'LoggingVolumeDriver'
op|'.'
name|'all_logs'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'create_actions'
op|'='
name|'driver'
op|'.'
name|'LoggingVolumeDriver'
op|'.'
name|'logs_like'
op|'('
nl|'\n'
string|"'create_volume'"
op|','
nl|'\n'
name|'id'
op|'='
name|'created_volume_id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Create_Actions: %s"'
op|'%'
name|'create_actions'
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
name|'create_actions'
op|')'
op|')'
newline|'\n'
name|'create_action'
op|'='
name|'create_actions'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'create_action'
op|'['
string|"'id'"
op|']'
op|','
name|'created_volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'create_action'
op|'['
string|"'availability_zone'"
op|']'
op|','
string|"'nova'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'create_action'
op|'['
string|"'size'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'export_actions'
op|'='
name|'driver'
op|'.'
name|'LoggingVolumeDriver'
op|'.'
name|'logs_like'
op|'('
nl|'\n'
string|"'create_export'"
op|','
nl|'\n'
name|'id'
op|'='
name|'created_volume_id'
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
name|'export_actions'
op|')'
op|')'
newline|'\n'
name|'export_action'
op|'='
name|'export_actions'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'export_action'
op|'['
string|"'id'"
op|']'
op|','
name|'created_volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'export_action'
op|'['
string|"'availability_zone'"
op|']'
op|','
string|"'nova'"
op|')'
newline|'\n'
nl|'\n'
name|'delete_actions'
op|'='
name|'driver'
op|'.'
name|'LoggingVolumeDriver'
op|'.'
name|'logs_like'
op|'('
nl|'\n'
string|"'delete_volume'"
op|','
nl|'\n'
name|'id'
op|'='
name|'created_volume_id'
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
name|'delete_actions'
op|')'
op|')'
newline|'\n'
name|'delete_action'
op|'='
name|'export_actions'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'delete_action'
op|'['
string|"'id'"
op|']'
op|','
name|'created_volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_and_detach_volume
dedent|''
name|'def'
name|'test_attach_and_detach_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates, attaches, detaches and deletes a volume."""'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'stub_network'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# Create server'
nl|'\n'
name|'server_req'
op|'='
op|'{'
string|"'server'"
op|':'
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
op|'}'
newline|'\n'
comment|'# NOTE(justinsb): Create an extra server so that server_id != volume_id'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
name|'server_req'
op|')'
newline|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
name|'server_req'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"created_server: %s"'
op|'%'
name|'created_server'
op|')'
newline|'\n'
name|'server_id'
op|'='
name|'created_server'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Create volume'
nl|'\n'
name|'created_volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_volume'
op|'('
op|'{'
string|"'volume'"
op|':'
op|'{'
string|"'size'"
op|':'
number|'1'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"created_volume: %s"'
op|'%'
name|'created_volume'
op|')'
newline|'\n'
name|'volume_id'
op|'='
name|'created_volume'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_poll_while'
op|'('
name|'volume_id'
op|','
op|'['
string|"'creating'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|"# Check we've got different IDs"
nl|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'server_id'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# List current server attachments - should be none'
nl|'\n'
name|'attachments'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server_volumes'
op|'('
name|'server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'attachments'
op|')'
newline|'\n'
nl|'\n'
comment|'# Template attach request'
nl|'\n'
name|'device'
op|'='
string|"'/dev/sdc'"
newline|'\n'
name|'attach_req'
op|'='
op|'{'
string|"'device'"
op|':'
name|'device'
op|'}'
newline|'\n'
name|'post_req'
op|'='
op|'{'
string|"'volumeAttachment'"
op|':'
name|'attach_req'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Try to attach to a non-existent volume; should fail'
nl|'\n'
name|'attach_req'
op|'['
string|"'volumeId'"
op|']'
op|'='
number|'3405691582'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiNotFoundException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server_volume'
op|','
name|'server_id'
op|','
name|'post_req'
op|')'
newline|'\n'
nl|'\n'
comment|'# Try to attach to a non-existent server; should fail'
nl|'\n'
name|'attach_req'
op|'['
string|"'volumeId'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiNotFoundException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server_volume'
op|','
number|'3405691582'
op|','
name|'post_req'
op|')'
newline|'\n'
nl|'\n'
comment|'# Should still be no attachments...'
nl|'\n'
name|'attachments'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server_volumes'
op|'('
name|'server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'attachments'
op|')'
newline|'\n'
nl|'\n'
comment|'# Do a real attach'
nl|'\n'
name|'attach_req'
op|'['
string|"'volumeId'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
name|'attach_result'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server_volume'
op|'('
name|'server_id'
op|','
name|'post_req'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Attachment = %s"'
op|')'
op|'%'
name|'attach_result'
op|')'
newline|'\n'
nl|'\n'
name|'attachment_id'
op|'='
name|'attach_result'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'volume_id'
op|','
name|'attach_result'
op|'['
string|"'volumeId'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|"# These fields aren't set because it's async"
nl|'\n'
comment|"#self.assertEquals(server_id, attach_result['serverId'])"
nl|'\n'
comment|"#self.assertEquals(device, attach_result['device'])"
nl|'\n'
nl|'\n'
comment|"# This is just an implementation detail, but let's check it..."
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'volume_id'
op|','
name|'attachment_id'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(justinsb): There's an issue with the attach code, in that"
nl|'\n'
comment|"# it's currently asynchronous and not recorded until the attach"
nl|'\n'
comment|"# completes.  So the caller must be 'smart', like this..."
nl|'\n'
name|'attach_done'
op|'='
name|'None'
newline|'\n'
name|'retries'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'attach_done'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server_volume'
op|'('
name|'server_id'
op|','
nl|'\n'
name|'attachment_id'
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
name|'except'
name|'client'
op|'.'
name|'OpenStackApiNotFoundException'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Got 404, waiting"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
name|'retries'
op|'='
name|'retries'
op|'+'
number|'1'
newline|'\n'
name|'if'
name|'retries'
op|'>'
number|'10'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'expect_attach'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'expect_attach'
op|'['
string|"'id'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
name|'expect_attach'
op|'['
string|"'volumeId'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
name|'expect_attach'
op|'['
string|"'serverId'"
op|']'
op|'='
name|'server_id'
newline|'\n'
name|'expect_attach'
op|'['
string|"'device'"
op|']'
op|'='
name|'device'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expect_attach'
op|','
name|'attach_done'
op|')'
newline|'\n'
nl|'\n'
comment|'# Should be one attachemnt'
nl|'\n'
name|'attachments'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server_volumes'
op|'('
name|'server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
name|'expect_attach'
op|']'
op|','
name|'attachments'
op|')'
newline|'\n'
nl|'\n'
comment|'# Should be able to get details'
nl|'\n'
name|'attachment_info'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server_volume'
op|'('
name|'server_id'
op|','
name|'attachment_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'expect_attach'
op|','
name|'attachment_info'
op|')'
newline|'\n'
nl|'\n'
comment|'# Getting details on a different id should fail'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiNotFoundException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server_volume'
op|','
name|'server_id'
op|','
number|'3405691582'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiNotFoundException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server_volume'
op|','
nl|'\n'
number|'3405691582'
op|','
name|'attachment_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Trying to detach a different id should fail'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiNotFoundException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'delete_server_volume'
op|','
name|'server_id'
op|','
number|'3405691582'
op|')'
newline|'\n'
nl|'\n'
comment|'# Detach should work'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'delete_server_volume'
op|'('
name|'server_id'
op|','
name|'attachment_id'
op|')'
newline|'\n'
nl|'\n'
comment|"# Again, it's async, so wait..."
nl|'\n'
name|'retries'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'attachment'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server_volume'
op|'('
name|'server_id'
op|','
nl|'\n'
name|'attachment_id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Attachment still there: %s"'
op|'%'
name|'attachment'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'client'
op|'.'
name|'OpenStackApiNotFoundException'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Got 404, delete done"'
op|')'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
name|'retries'
op|'='
name|'retries'
op|'+'
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'retries'
op|'<'
number|'10'
op|')'
newline|'\n'
nl|'\n'
comment|'# Should be no attachments again'
nl|'\n'
dedent|''
name|'attachments'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server_volumes'
op|'('
name|'server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'attachments'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Logs: %s"'
op|'%'
name|'driver'
op|'.'
name|'LoggingVolumeDriver'
op|'.'
name|'all_logs'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# prepare_attach and prepare_detach are called from compute'
nl|'\n'
comment|'#  on attach/detach'
nl|'\n'
nl|'\n'
name|'disco_moves'
op|'='
name|'driver'
op|'.'
name|'LoggingVolumeDriver'
op|'.'
name|'logs_like'
op|'('
nl|'\n'
string|"'initialize_connection'"
op|','
nl|'\n'
name|'id'
op|'='
name|'volume_id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"initialize_connection actions: %s"'
op|'%'
name|'disco_moves'
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
name|'disco_moves'
op|')'
op|')'
newline|'\n'
name|'disco_move'
op|'='
name|'disco_moves'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'disco_move'
op|'['
string|"'id'"
op|']'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
name|'last_days_of_disco_moves'
op|'='
name|'driver'
op|'.'
name|'LoggingVolumeDriver'
op|'.'
name|'logs_like'
op|'('
nl|'\n'
string|"'terminate_connection'"
op|','
nl|'\n'
name|'id'
op|'='
name|'volume_id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"terminate_connection actions: %s"'
op|'%'
nl|'\n'
name|'last_days_of_disco_moves'
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
name|'last_days_of_disco_moves'
op|')'
op|')'
newline|'\n'
name|'undisco_move'
op|'='
name|'last_days_of_disco_moves'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'undisco_move'
op|'['
string|"'id'"
op|']'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'undisco_move'
op|'['
string|"'mountpoint'"
op|']'
op|','
name|'device'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'undisco_move'
op|'['
string|"'instance_id'"
op|']'
op|','
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_volume_with_metadata
dedent|''
name|'def'
name|'test_create_volume_with_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates and deletes a volume."""'
newline|'\n'
nl|'\n'
comment|'# Create volume'
nl|'\n'
name|'metadata'
op|'='
op|'{'
string|"'key1'"
op|':'
string|"'value1'"
op|','
nl|'\n'
string|"'key2'"
op|':'
string|"'value2'"
op|'}'
newline|'\n'
name|'created_volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_volume'
op|'('
nl|'\n'
op|'{'
string|"'volume'"
op|':'
op|'{'
string|"'size'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'metadata'"
op|':'
name|'metadata'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"created_volume: %s"'
op|'%'
name|'created_volume'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_volume_id'
op|'='
name|'created_volume'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|"# Check it's there and metadata present"
nl|'\n'
name|'found_volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_volume'
op|'('
name|'created_volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'created_volume_id'
op|','
name|'found_volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'metadata'
op|','
name|'found_volume'
op|'['
string|"'metadata'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'unittest'
op|'.'
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
