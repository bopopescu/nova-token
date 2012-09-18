begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 OpenStack, LLC.'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nScheduler base class that all Schedulers should inherit from\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
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
name|'rpcapi'
name|'as'
name|'compute_rpcapi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
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
name|'notifications'
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
name|'importutils'
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
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'notifier'
name|'import'
name|'api'
name|'as'
name|'notifier'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'rpc'
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
DECL|variable|scheduler_driver_opts
name|'scheduler_driver_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'scheduler_host_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.scheduler.host_manager.HostManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The scheduler host manager class to use'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'scheduler_max_attempts'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Maximum number of attempts to schedule an instance'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'scheduler_driver_opts'
op|')'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'instances_path'"
op|','
string|"'nova.compute.manager'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'libvirt_type'"
op|','
string|"'nova.virt.libvirt.driver'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|handle_schedule_error
name|'def'
name|'handle_schedule_error'
op|'('
name|'context'
op|','
name|'ex'
op|','
name|'instance_uuid'
op|','
name|'request_spec'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'ex'
op|','
name|'exception'
op|'.'
name|'NoValidHost'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Exception during scheduler.run_instance"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'compute_utils'
op|'.'
name|'add_instance_fault_from_exc'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_uuid'
op|','
name|'ex'
op|','
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|')'
newline|'\n'
name|'state'
op|'='
name|'vm_states'
op|'.'
name|'ERROR'
op|'.'
name|'upper'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Setting instance to %(state)s state.'"
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|','
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
comment|'# update instance state and notify on the transition'
nl|'\n'
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
name|'context'
op|','
nl|'\n'
name|'instance_uuid'
op|','
op|'{'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'ERROR'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'context'
op|','
name|'old_ref'
op|','
name|'new_ref'
op|','
nl|'\n'
name|'service'
op|'='
string|'"scheduler"'
op|')'
newline|'\n'
nl|'\n'
name|'properties'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'instance_properties'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'payload'
op|'='
name|'dict'
op|'('
name|'request_spec'
op|'='
name|'request_spec'
op|','
nl|'\n'
name|'instance_properties'
op|'='
name|'properties'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'state'
op|'='
name|'vm_states'
op|'.'
name|'ERROR'
op|','
nl|'\n'
name|'method'
op|'='
string|"'run_instance'"
op|','
nl|'\n'
name|'reason'
op|'='
name|'ex'
op|')'
newline|'\n'
nl|'\n'
name|'notifier'
op|'.'
name|'notify'
op|'('
name|'context'
op|','
name|'notifier'
op|'.'
name|'publisher_id'
op|'('
string|'"scheduler"'
op|')'
op|','
nl|'\n'
string|"'scheduler.run_instance'"
op|','
name|'notifier'
op|'.'
name|'ERROR'
op|','
name|'payload'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cast_to_volume_host
dedent|''
name|'def'
name|'cast_to_volume_host'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'method'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Cast request to a volume host queue"""'
newline|'\n'
nl|'\n'
name|'volume_id'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'volume_id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'volume_id'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
string|"'scheduled_at'"
op|':'
name|'now'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
string|"'volume'"
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
name|'method'
op|','
string|'"args"'
op|':'
name|'kwargs'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Casted \'%(method)s\' to volume \'%(host)s\'"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_update_db
dedent|''
name|'def'
name|'instance_update_db'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Set the host and scheduled_at fields of an Instance.\n\n    :returns: An Instance with the updated fields set properly.\n    '''"
newline|'\n'
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'values'
op|'='
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
string|"'scheduled_at'"
op|':'
name|'now'
op|'}'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cast_to_compute_host
dedent|''
name|'def'
name|'cast_to_compute_host'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'method'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Cast request to a compute host queue"""'
newline|'\n'
nl|'\n'
name|'instance_uuid'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'instance_uuid'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'instance_uuid'
op|':'
newline|'\n'
indent|'        '
name|'instance_update_db'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
string|"'compute'"
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
name|'method'
op|','
string|'"args"'
op|':'
name|'kwargs'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Casted \'%(method)s\' to compute \'%(host)s\'"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cast_to_network_host
dedent|''
name|'def'
name|'cast_to_network_host'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'method'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Cast request to a network host queue"""'
newline|'\n'
nl|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
string|"'network'"
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
name|'method'
op|','
string|'"args"'
op|':'
name|'kwargs'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Casted \'%(method)s\' to network \'%(host)s\'"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cast_to_host
dedent|''
name|'def'
name|'cast_to_host'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'host'
op|','
name|'method'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generic cast to host"""'
newline|'\n'
nl|'\n'
name|'topic_mapping'
op|'='
op|'{'
nl|'\n'
string|'"compute"'
op|':'
name|'cast_to_compute_host'
op|','
nl|'\n'
string|'"volume"'
op|':'
name|'cast_to_volume_host'
op|','
nl|'\n'
string|"'network'"
op|':'
name|'cast_to_network_host'
op|'}'
newline|'\n'
nl|'\n'
name|'func'
op|'='
name|'topic_mapping'
op|'.'
name|'get'
op|'('
name|'topic'
op|')'
newline|'\n'
name|'if'
name|'func'
op|':'
newline|'\n'
indent|'        '
name|'func'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'method'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
name|'method'
op|','
string|'"args"'
op|':'
name|'kwargs'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Casted \'%(method)s\' to %(topic)s \'%(host)s\'"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|encode_instance
dedent|''
dedent|''
name|'def'
name|'encode_instance'
op|'('
name|'instance'
op|','
name|'local'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Encode locally created instance for return via RPC"""'
newline|'\n'
comment|'# TODO(comstud): I would love to be able to return the full'
nl|'\n'
comment|"# instance information here, but we'll need some modifications"
nl|'\n'
comment|'# to the RPC code to handle datetime conversions with the'
nl|'\n'
comment|'# json encoding/decoding.  We should be able to set a default'
nl|'\n'
comment|'# json handler somehow to do it.'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# For now, I'll just return the instance ID and let the caller"
nl|'\n'
comment|'# do a DB lookup :-/'
nl|'\n'
name|'if'
name|'local'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
name|'_is_precooked'
op|'='
name|'False'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'dict'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'_is_precooked'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'return'
name|'inst'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Scheduler
dedent|''
dedent|''
name|'class'
name|'Scheduler'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The base class that all Scheduler classes should inherit from."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'host_manager'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
nl|'\n'
name|'FLAGS'
op|'.'
name|'scheduler_host_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_rpcapi'
op|'='
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_service_capabilities
dedent|''
name|'def'
name|'update_service_capabilities'
op|'('
name|'self'
op|','
name|'service_name'
op|','
name|'host'
op|','
name|'capabilities'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Process a capability update from a service node."""'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'update_service_capabilities'
op|'('
name|'service_name'
op|','
nl|'\n'
name|'host'
op|','
name|'capabilities'
op|')'
newline|'\n'
nl|'\n'
DECL|member|hosts_up
dedent|''
name|'def'
name|'hosts_up'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the list of hosts that have a running service for topic."""'
newline|'\n'
nl|'\n'
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_topic'
op|'('
name|'context'
op|','
name|'topic'
op|')'
newline|'\n'
name|'return'
op|'['
name|'service'
op|'['
string|"'host'"
op|']'
nl|'\n'
name|'for'
name|'service'
name|'in'
name|'services'
nl|'\n'
name|'if'
name|'utils'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|schedule_prep_resize
dedent|''
name|'def'
name|'schedule_prep_resize'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|','
name|'instance'
op|','
name|'instance_type'
op|','
nl|'\n'
name|'reservations'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Must override schedule_prep_resize method for scheduler to work."""'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Driver must implement schedule_prep_resize"'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_run_instance
dedent|''
name|'def'
name|'schedule_run_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'admin_password'
op|','
name|'injected_files'
op|','
nl|'\n'
name|'requested_networks'
op|','
name|'is_first_time'
op|','
nl|'\n'
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Must override schedule_run_instance method for scheduler to work."""'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Driver must implement schedule_run_instance"'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_create_volume
dedent|''
name|'def'
name|'schedule_create_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'snapshot_id'
op|','
nl|'\n'
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Driver must implement schedule_create_volune"'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_live_migration
dedent|''
name|'def'
name|'schedule_live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'dest'
op|','
nl|'\n'
name|'block_migration'
op|','
name|'disk_over_commit'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Live migration scheduling method.\n\n        :param context:\n        :param instance: instance dict\n        :param dest: destination host\n        :param block_migration: if true, block_migration.\n        :param disk_over_commit: if True, consider real(not virtual)\n                                 disk size.\n\n        :return:\n            The host where instance is running currently.\n            Then scheduler send request that host.\n        """'
newline|'\n'
comment|'# Check we can do live migration'
nl|'\n'
name|'self'
op|'.'
name|'_live_migration_src_check'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_live_migration_dest_check'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'dest'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_live_migration_common_check'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'dest'
op|')'
newline|'\n'
name|'migrate_data'
op|'='
name|'self'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'check_can_live_migrate_destination'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|','
name|'dest'
op|','
name|'block_migration'
op|','
name|'disk_over_commit'
op|')'
newline|'\n'
nl|'\n'
comment|'# Perform migration'
nl|'\n'
name|'src'
op|'='
name|'instance'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'live_migration'
op|'('
name|'context'
op|','
name|'host'
op|'='
name|'src'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|','
name|'dest'
op|'='
name|'dest'
op|','
nl|'\n'
name|'block_migration'
op|'='
name|'block_migration'
op|','
nl|'\n'
name|'migrate_data'
op|'='
name|'migrate_data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_live_migration_src_check
dedent|''
name|'def'
name|'_live_migration_src_check'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Live migration check routine (for src host).\n\n        :param context: security context\n        :param instance_ref: nova.db.sqlalchemy.models.Instance object\n\n        """'
newline|'\n'
comment|'# TODO(johngar) why is this not in the API layer?'
nl|'\n'
comment|'# Checking instance is running.'
nl|'\n'
name|'if'
name|'instance_ref'
op|'['
string|"'power_state'"
op|']'
op|'!='
name|'power_state'
op|'.'
name|'RUNNING'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotRunning'
op|'('
nl|'\n'
name|'instance_id'
op|'='
name|'instance_ref'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking src host exists and compute node'
nl|'\n'
dedent|''
name|'src'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all_compute_by_host'
op|'('
name|'context'
op|','
name|'src'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
op|'('
name|'host'
op|'='
name|'src'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking src host is alive.'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'utils'
op|'.'
name|'service_is_up'
op|'('
name|'services'
op|'['
number|'0'
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
op|'('
name|'host'
op|'='
name|'src'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_live_migration_dest_check
dedent|''
dedent|''
name|'def'
name|'_live_migration_dest_check'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Live migration check routine (for destination host).\n\n        :param context: security context\n        :param instance_ref: nova.db.sqlalchemy.models.Instance object\n        :param dest: destination host\n        """'
newline|'\n'
nl|'\n'
comment|'# Checking dest exists and compute node.'
nl|'\n'
name|'dservice_refs'
op|'='
name|'db'
op|'.'
name|'service_get_all_compute_by_host'
op|'('
name|'context'
op|','
name|'dest'
op|')'
newline|'\n'
name|'dservice_ref'
op|'='
name|'dservice_refs'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'# Checking dest host is alive.'
nl|'\n'
name|'if'
name|'not'
name|'utils'
op|'.'
name|'service_is_up'
op|'('
name|'dservice_ref'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
op|'('
name|'host'
op|'='
name|'dest'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking whether The host where instance is running'
nl|'\n'
comment|'# and dest is not same.'
nl|'\n'
dedent|''
name|'src'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'if'
name|'dest'
op|'=='
name|'src'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'UnableToMigrateToSelf'
op|'('
nl|'\n'
name|'instance_id'
op|'='
name|'instance_ref'
op|'['
string|"'uuid'"
op|']'
op|','
name|'host'
op|'='
name|'dest'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check memory requirements'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_assert_compute_node_has_enough_memory'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_ref'
op|','
name|'dest'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_live_migration_common_check
dedent|''
name|'def'
name|'_live_migration_common_check'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Live migration common check routine.\n\n        The following checks are based on\n        http://wiki.libvirt.org/page/TodoPreMigrationChecks\n\n        :param context: security context\n        :param instance_ref: nova.db.sqlalchemy.models.Instance object\n        :param dest: destination host\n        """'
newline|'\n'
name|'dservice_ref'
op|'='
name|'self'
op|'.'
name|'_get_compute_info'
op|'('
name|'context'
op|','
name|'dest'
op|')'
newline|'\n'
name|'src'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'oservice_ref'
op|'='
name|'self'
op|'.'
name|'_get_compute_info'
op|'('
name|'context'
op|','
name|'src'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking hypervisor is same.'
nl|'\n'
name|'orig_hypervisor'
op|'='
name|'oservice_ref'
op|'['
string|"'hypervisor_type'"
op|']'
newline|'\n'
name|'dest_hypervisor'
op|'='
name|'dservice_ref'
op|'['
string|"'hypervisor_type'"
op|']'
newline|'\n'
name|'if'
name|'orig_hypervisor'
op|'!='
name|'dest_hypervisor'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidHypervisorType'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking hypervisor version.'
nl|'\n'
dedent|''
name|'orig_hypervisor'
op|'='
name|'oservice_ref'
op|'['
string|"'hypervisor_version'"
op|']'
newline|'\n'
name|'dest_hypervisor'
op|'='
name|'dservice_ref'
op|'['
string|"'hypervisor_version'"
op|']'
newline|'\n'
name|'if'
name|'orig_hypervisor'
op|'>'
name|'dest_hypervisor'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'DestinationHypervisorTooOld'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_assert_compute_node_has_enough_memory
dedent|''
dedent|''
name|'def'
name|'_assert_compute_node_has_enough_memory'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'instance_ref'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Checks if destination host has enough memory for live migration.\n\n\n        :param context: security context\n        :param instance_ref: nova.db.sqlalchemy.models.Instance object\n        :param dest: destination host\n\n        """'
newline|'\n'
comment|'# Getting total available memory of host'
nl|'\n'
name|'avail'
op|'='
name|'self'
op|'.'
name|'_get_compute_info'
op|'('
name|'context'
op|','
name|'dest'
op|')'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Getting total used memory and disk of host'
nl|'\n'
comment|'# It should be sum of memories that are assigned as max value,'
nl|'\n'
comment|'# because overcommitting is risky.'
nl|'\n'
name|'instance_refs'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'context'
op|','
name|'dest'
op|')'
newline|'\n'
name|'used'
op|'='
name|'sum'
op|'('
op|'['
name|'i'
op|'['
string|"'memory_mb'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instance_refs'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'mem_inst'
op|'='
name|'instance_ref'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'avail'
op|'='
name|'avail'
op|'-'
name|'used'
newline|'\n'
name|'if'
name|'avail'
op|'<='
name|'mem_inst'
op|':'
newline|'\n'
indent|'            '
name|'instance_uuid'
op|'='
name|'instance_ref'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"Unable to migrate %(instance_uuid)s to %(dest)s: "'
nl|'\n'
string|'"Lack of memory(host:%(avail)s <= "'
nl|'\n'
string|'"instance:%(mem_inst)s)"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'MigrationError'
op|'('
name|'reason'
op|'='
name|'reason'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_compute_info
dedent|''
dedent|''
name|'def'
name|'_get_compute_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""get compute node\'s information specified by key\n\n        :param context: security context\n        :param host: hostname(must be compute node)\n        :param key: column name of compute_nodes\n        :return: value specified by key\n\n        """'
newline|'\n'
name|'compute_node_ref'
op|'='
name|'db'
op|'.'
name|'service_get_all_compute_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'compute_node_ref'
op|'['
number|'0'
op|']'
op|'['
string|"'compute_node'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
