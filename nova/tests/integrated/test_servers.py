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
name|'time'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
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
op|'.'
name|'api'
name|'import'
name|'client'
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
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'fake'
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
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersTest
name|'class'
name|'ServersTest'
op|'('
name|'integrated_helpers'
op|'.'
name|'_IntegratedTestBase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_wait_for_state_change
indent|'    '
name|'def'
name|'_wait_for_state_change'
op|'('
name|'self'
op|','
name|'server'
op|','
name|'from_status'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'0'
op|','
number|'50'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'server'
op|'['
string|"'status'"
op|']'
op|'!='
name|'from_status'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'.1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'server'
newline|'\n'
nl|'\n'
DECL|member|_restart_compute_service
dedent|''
name|'def'
name|'_restart_compute_service'
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
string|'"""restart compute service. NOTE: fake driver forgets all instances."""'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'compute'"
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_servers
dedent|''
name|'def'
name|'test_get_servers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Simple check that listing servers works."""'
newline|'\n'
name|'servers'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_servers'
op|'('
op|')'
newline|'\n'
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"server: %s"'
op|'%'
name|'server'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_with_error
dedent|''
dedent|''
name|'def'
name|'test_create_server_with_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a server which will enter error state."""'
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
DECL|function|throw_error
name|'def'
name|'throw_error'
op|'('
op|'*'
name|'_'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'fake'
op|'.'
name|'FakeDriver'
op|','
string|"'spawn'"
op|','
name|'throw_error'
op|')'
newline|'\n'
nl|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
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
op|'{'
string|'"server"'
op|':'
name|'server'
op|'}'
op|')'
newline|'\n'
name|'created_server_id'
op|'='
name|'created_server'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'created_server_id'
op|','
name|'found_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'_wait_for_state_change'
op|'('
name|'found_server'
op|','
string|"'BUILD'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'ERROR'"
op|','
name|'found_server'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_delete_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_delete_server
dedent|''
name|'def'
name|'test_create_and_delete_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates and deletes a server."""'
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
comment|'# Build the server data gradually, checking errors along the way'
nl|'\n'
name|'server'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'good_server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'post'
op|'='
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Without an imageRef, this throws 500.'
nl|'\n'
comment|'# TODO(justinsb): Check whatever the spec says should be thrown here'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|','
name|'post'
op|')'
newline|'\n'
nl|'\n'
comment|'# With an invalid imageRef, this throws 500.'
nl|'\n'
name|'server'
op|'['
string|"'imageRef'"
op|']'
op|'='
name|'self'
op|'.'
name|'get_invalid_image'
op|'('
op|')'
newline|'\n'
comment|'# TODO(justinsb): Check whatever the spec says should be thrown here'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|','
name|'post'
op|')'
newline|'\n'
nl|'\n'
comment|'# Add a valid imageRef'
nl|'\n'
name|'server'
op|'['
string|"'imageRef'"
op|']'
op|'='
name|'good_server'
op|'.'
name|'get'
op|'('
string|"'imageRef'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Without flavorRef, this throws 500'
nl|'\n'
comment|'# TODO(justinsb): Check whatever the spec says should be thrown here'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|','
name|'post'
op|')'
newline|'\n'
nl|'\n'
name|'server'
op|'['
string|"'flavorRef'"
op|']'
op|'='
name|'good_server'
op|'.'
name|'get'
op|'('
string|"'flavorRef'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Without a name, this throws 500'
nl|'\n'
comment|'# TODO(justinsb): Check whatever the spec says should be thrown here'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|','
name|'post'
op|')'
newline|'\n'
nl|'\n'
comment|'# Set a valid server name'
nl|'\n'
name|'server'
op|'['
string|"'name'"
op|']'
op|'='
name|'good_server'
op|'['
string|"'name'"
op|']'
newline|'\n'
nl|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
name|'post'
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
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_server_id'
op|'='
name|'created_server'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|"# Check it's there"
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'created_server_id'
op|','
name|'found_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# It should also be in the all-servers list'
nl|'\n'
name|'servers'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_servers'
op|'('
op|')'
newline|'\n'
name|'server_ids'
op|'='
op|'['
name|'server'
op|'['
string|"'id'"
op|']'
name|'for'
name|'server'
name|'in'
name|'servers'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server_id'
name|'in'
name|'server_ids'
op|')'
newline|'\n'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'_wait_for_state_change'
op|'('
name|'found_server'
op|','
string|"'BUILD'"
op|')'
newline|'\n'
comment|'# It should be available...'
nl|'\n'
comment|"# TODO(justinsb): Mock doesn't yet do this..."
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'ACTIVE'"
op|','
name|'found_server'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
name|'servers'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_servers'
op|'('
name|'detail'
op|'='
name|'True'
op|')'
newline|'\n'
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"image"'
name|'in'
name|'server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"flavor"'
name|'in'
name|'server'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_delete_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deferred_delete
dedent|''
name|'def'
name|'test_deferred_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates, deletes and waits for server to be reclaimed."""'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'stub_network'
op|'='
name|'True'
op|','
name|'reclaim_instance_interval'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
comment|'# enforce periodic tasks run in short time to avoid wait for 60s.'
nl|'\n'
name|'self'
op|'.'
name|'_restart_compute_service'
op|'('
nl|'\n'
name|'periodic_interval'
op|'='
number|'0.3'
op|','
name|'periodic_fuzzy_delay'
op|'='
number|'0'
op|')'
newline|'\n'
nl|'\n'
comment|'# Create server'
nl|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
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
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_server_id'
op|'='
name|'created_server'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Wait for it to finish being created'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'_wait_for_state_change'
op|'('
name|'created_server'
op|','
string|"'BUILD'"
op|')'
newline|'\n'
nl|'\n'
comment|'# It should be available...'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'ACTIVE'"
op|','
name|'found_server'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Cannot restore unless instance is deleted'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server_action'
op|','
name|'created_server_id'
op|','
nl|'\n'
op|'{'
string|"'restore'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# Cannot forceDelete unless instance is deleted'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server_action'
op|','
name|'created_server_id'
op|','
nl|'\n'
op|'{'
string|"'forceDelete'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete the server'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'delete_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Wait for queued deletion'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'_wait_for_state_change'
op|'('
name|'found_server'
op|','
string|"'ACTIVE'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'DELETED'"
op|','
name|'found_server'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Wait for real deletion'
nl|'\n'
name|'self'
op|'.'
name|'_wait_for_deletion'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deferred_delete_restore
dedent|''
name|'def'
name|'test_deferred_delete_restore'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates, deletes and restores a server."""'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'stub_network'
op|'='
name|'True'
op|','
name|'reclaim_instance_interval'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
comment|'# Create server'
nl|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
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
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_server_id'
op|'='
name|'created_server'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Wait for it to finish being created'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'_wait_for_state_change'
op|'('
name|'created_server'
op|','
string|"'BUILD'"
op|')'
newline|'\n'
nl|'\n'
comment|'# It should be available...'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'ACTIVE'"
op|','
name|'found_server'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete the server'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'delete_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Wait for queued deletion'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'_wait_for_state_change'
op|'('
name|'found_server'
op|','
string|"'ACTIVE'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'DELETED'"
op|','
name|'found_server'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Restore server'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server_action'
op|'('
name|'created_server_id'
op|','
op|'{'
string|"'restore'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# Wait for server to become active again'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'_wait_for_state_change'
op|'('
name|'found_server'
op|','
string|"'DELETED'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'ACTIVE'"
op|','
name|'found_server'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deferred_delete_force
dedent|''
name|'def'
name|'test_deferred_delete_force'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates, deletes and force deletes a server."""'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'stub_network'
op|'='
name|'True'
op|','
name|'reclaim_instance_interval'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
comment|'# Create server'
nl|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
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
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_server_id'
op|'='
name|'created_server'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Wait for it to finish being created'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'_wait_for_state_change'
op|'('
name|'created_server'
op|','
string|"'BUILD'"
op|')'
newline|'\n'
nl|'\n'
comment|'# It should be available...'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'ACTIVE'"
op|','
name|'found_server'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete the server'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'delete_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Wait for queued deletion'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'_wait_for_state_change'
op|'('
name|'found_server'
op|','
string|"'ACTIVE'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'DELETED'"
op|','
name|'found_server'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Force delete server'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server_action'
op|'('
name|'created_server_id'
op|','
op|'{'
string|"'forceDelete'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# Wait for real deletion'
nl|'\n'
name|'self'
op|'.'
name|'_wait_for_deletion'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_wait_for_deletion
dedent|''
name|'def'
name|'_wait_for_deletion'
op|'('
name|'self'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
comment|'# Wait (briefly) for deletion'
nl|'\n'
indent|'        '
name|'for'
name|'_retries'
name|'in'
name|'range'
op|'('
number|'50'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'found_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'server_id'
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
name|'found_server'
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
string|'"Found_server=%s"'
op|'%'
name|'found_server'
op|')'
newline|'\n'
nl|'\n'
comment|"# TODO(justinsb): Mock doesn't yet do accurate state changes"
nl|'\n'
comment|"#if found_server['status'] != 'deleting':"
nl|'\n'
comment|'#    break'
nl|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'.1'
op|')'
newline|'\n'
nl|'\n'
comment|'# Should be gone'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'found_server'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_delete_server
dedent|''
name|'def'
name|'_delete_server'
op|'('
name|'self'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
comment|'# Delete the server'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'api'
op|'.'
name|'delete_server'
op|'('
name|'server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_wait_for_deletion'
op|'('
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_with_metadata
dedent|''
name|'def'
name|'test_create_server_with_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a server with metadata."""'
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
comment|'# Build the server data gradually, checking errors along the way'
nl|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'30'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'['
string|"'key_%s'"
op|'%'
name|'i'
op|']'
op|'='
string|"'value_%s'"
op|'%'
name|'i'
newline|'\n'
nl|'\n'
dedent|''
name|'server'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'metadata'
newline|'\n'
nl|'\n'
name|'post'
op|'='
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
newline|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
name|'post'
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
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_server_id'
op|'='
name|'created_server'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'created_server_id'
op|','
name|'found_server'
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
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# The server should also be in the all-servers details list'
nl|'\n'
name|'servers'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_servers'
op|'('
name|'detail'
op|'='
name|'True'
op|')'
newline|'\n'
name|'server_map'
op|'='
name|'dict'
op|'('
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|','
name|'server'
op|')'
name|'for'
name|'server'
name|'in'
name|'servers'
op|')'
newline|'\n'
name|'found_server'
op|'='
name|'server_map'
op|'.'
name|'get'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'found_server'
op|')'
newline|'\n'
comment|'# Details do include metadata'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'metadata'
op|','
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# The server should also be in the all-servers summary list'
nl|'\n'
name|'servers'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_servers'
op|'('
name|'detail'
op|'='
name|'False'
op|')'
newline|'\n'
name|'server_map'
op|'='
name|'dict'
op|'('
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|','
name|'server'
op|')'
name|'for'
name|'server'
name|'in'
name|'servers'
op|')'
newline|'\n'
name|'found_server'
op|'='
name|'server_map'
op|'.'
name|'get'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'found_server'
op|')'
newline|'\n'
comment|'# Summary should not include metadata'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Cleanup'
nl|'\n'
name|'self'
op|'.'
name|'_delete_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_rebuild_server
dedent|''
name|'def'
name|'test_create_and_rebuild_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Rebuild a server with metadata."""'
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
comment|'# create a server with initially has no metadata'
nl|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
name|'server_post'
op|'='
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
newline|'\n'
nl|'\n'
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'30'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'['
string|"'key_%s'"
op|'%'
name|'i'
op|']'
op|'='
string|"'value_%s'"
op|'%'
name|'i'
newline|'\n'
nl|'\n'
dedent|''
name|'server_post'
op|'['
string|"'server'"
op|']'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'metadata'
newline|'\n'
nl|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
name|'server_post'
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
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_server_id'
op|'='
name|'created_server'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'_wait_for_state_change'
op|'('
name|'created_server'
op|','
string|"'BUILD'"
op|')'
newline|'\n'
nl|'\n'
comment|'# rebuild the server with metadata and other server attributes'
nl|'\n'
name|'post'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'post'
op|'['
string|"'rebuild'"
op|']'
op|'='
op|'{'
nl|'\n'
string|'"imageRef"'
op|':'
string|'"76fa36fc-c930-4bf3-8c8a-ea2a2420deb6"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"blah"'
op|','
nl|'\n'
string|'"accessIPv4"'
op|':'
string|'"172.19.0.2"'
op|','
nl|'\n'
string|'"accessIPv6"'
op|':'
string|'"fe80::2"'
op|','
nl|'\n'
string|'"metadata"'
op|':'
op|'{'
string|"'some'"
op|':'
string|"'thing'"
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server_action'
op|'('
name|'created_server_id'
op|','
name|'post'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"rebuilt server: %s"'
op|'%'
name|'created_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'created_server_id'
op|','
name|'found_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'some'"
op|':'
string|"'thing'"
op|'}'
op|','
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'blah'"
op|','
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'post'
op|'['
string|"'rebuild'"
op|']'
op|'['
string|"'imageRef'"
op|']'
op|','
nl|'\n'
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'image'"
op|')'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'172.19.0.2'"
op|','
name|'found_server'
op|'['
string|"'accessIPv4'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fe80::2'"
op|','
name|'found_server'
op|'['
string|"'accessIPv6'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# rebuild the server with empty metadata and nothing else'
nl|'\n'
name|'post'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'post'
op|'['
string|"'rebuild'"
op|']'
op|'='
op|'{'
nl|'\n'
string|'"imageRef"'
op|':'
string|'"76fa36fc-c930-4bf3-8c8a-ea2a2420deb6"'
op|','
nl|'\n'
string|'"metadata"'
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server_action'
op|'('
name|'created_server_id'
op|','
name|'post'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"rebuilt server: %s"'
op|'%'
name|'created_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'created_server_id'
op|','
name|'found_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
op|'}'
op|','
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'blah'"
op|','
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'post'
op|'['
string|"'rebuild'"
op|']'
op|'['
string|"'imageRef'"
op|']'
op|','
nl|'\n'
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'image'"
op|')'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'172.19.0.2'"
op|','
name|'found_server'
op|'['
string|"'accessIPv4'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fe80::2'"
op|','
name|'found_server'
op|'['
string|"'accessIPv6'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Cleanup'
nl|'\n'
name|'self'
op|'.'
name|'_delete_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rename_server
dedent|''
name|'def'
name|'test_rename_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test building and renaming a server."""'
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
comment|'# Create a server'
nl|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
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
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
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
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
comment|"# Rename the server to 'new-name'"
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'put_server'
op|'('
name|'server_id'
op|','
op|'{'
string|"'server'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'new-name'"
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check the name of the server'
nl|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'created_server'
op|'['
string|"'name'"
op|']'
op|','
string|"'new-name'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Cleanup'
nl|'\n'
name|'self'
op|'.'
name|'_delete_server'
op|'('
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_multiple_servers
dedent|''
name|'def'
name|'test_create_multiple_servers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates multiple servers and checks for reservation_id"""'
newline|'\n'
nl|'\n'
comment|"# Create 2 servers, setting 'return_reservation_id, which should"
nl|'\n'
comment|'# return a reservation_id'
nl|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
name|'server'
op|'['
string|"'min_count'"
op|']'
op|'='
number|'2'
newline|'\n'
name|'server'
op|'['
string|"'return_reservation_id'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'post'
op|'='
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
name|'post'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'reservation_id'"
op|','
name|'response'
op|')'
newline|'\n'
name|'reservation_id'
op|'='
name|'response'
op|'['
string|"'reservation_id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
name|'reservation_id'
op|','
op|'['
string|"''"
op|','
name|'None'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Create 1 more server, which should not return a reservation_id'
nl|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
name|'post'
op|'='
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
newline|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
name|'post'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_server_id'
op|'='
name|'created_server'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'# lookup servers created by the first request.'
nl|'\n'
name|'servers'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_servers'
op|'('
name|'detail'
op|'='
name|'True'
op|','
nl|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'reservation_id'"
op|':'
name|'reservation_id'
op|'}'
op|')'
newline|'\n'
name|'server_map'
op|'='
name|'dict'
op|'('
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|','
name|'server'
op|')'
name|'for'
name|'server'
name|'in'
name|'servers'
op|')'
newline|'\n'
name|'found_server'
op|'='
name|'server_map'
op|'.'
name|'get'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
comment|'# The server from the 2nd request should not be there.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'found_server'
op|','
name|'None'
op|')'
newline|'\n'
comment|'# Should have found 2 servers.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'server_map'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
comment|'# Cleanup'
nl|'\n'
name|'self'
op|'.'
name|'_delete_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'for'
name|'server_id'
name|'in'
name|'server_map'
op|'.'
name|'iterkeys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_delete_server'
op|'('
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
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
