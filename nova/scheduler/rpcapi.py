begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012, Red Hat, Inc.'
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
string|'"""\nClient side of the scheduler manager RPC API.\n"""'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rpc'
op|'.'
name|'proxy'
newline|'\n'
nl|'\n'
DECL|variable|rpcapi_opts
name|'rpcapi_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'scheduler_topic'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'scheduler'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the topic scheduler nodes listen on'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'rpcapi_opts'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|rpcapi_cap_opt
name|'rpcapi_cap_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'scheduler'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set a version cap for messages sent to scheduler services'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opt'
op|'('
name|'rpcapi_cap_opt'
op|','
string|"'upgrade_levels'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SchedulerAPI
name|'class'
name|'SchedulerAPI'
op|'('
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rpc'
op|'.'
name|'proxy'
op|'.'
name|'RpcProxy'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Client side of the scheduler rpc API.\n\n    API version history:\n\n        1.0 - Initial version.\n        1.1 - Changes to prep_resize():\n                - remove instance_uuid, add instance\n                - remove instance_type_id, add instance_type\n                - remove topic, it was unused\n        1.2 - Remove topic from run_instance, it was unused\n        1.3 - Remove instance_id, add instance to live_migration\n        1.4 - Remove update_db from prep_resize\n        1.5 - Add reservations argument to prep_resize()\n        1.6 - Remove reservations argument to run_instance()\n        1.7 - Add create_volume() method, remove topic from live_migration()\n\n        2.0 - Remove 1.x backwards compat\n        2.1 - Add image_id to create_volume()\n        2.2 - Remove reservations argument to create_volume()\n        2.3 - Remove create_volume()\n        2.4 - Change update_service_capabilities()\n                - accepts a list of capabilities\n        2.5 - Add get_backdoor_port()\n        2.6 - Add select_hosts()\n\n        ... Grizzly supports message version 2.6.  So, any changes to existing\n        methods in 2.x after that point should be done such that they can\n        handle the version_cap being set to 2.6.\n\n        2.7 - Add select_destinations()\n    '''"
newline|'\n'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# NOTE(russellb): This is the default minimum version that the server'
nl|'\n'
comment|'# (manager) side must implement unless otherwise specified using a version'
nl|'\n'
comment|'# argument to self.call()/cast()/etc. here.  It should be left as X.0 where'
nl|'\n'
comment|'# X is the current major API version (1.0, 2.0, ...).  For more information'
nl|'\n'
comment|'# about rpc API versioning, see the docs in'
nl|'\n'
comment|'# openstack/common/rpc/dispatcher.py.'
nl|'\n'
comment|'#'
nl|'\n'
DECL|variable|BASE_RPC_API_VERSION
name|'BASE_RPC_API_VERSION'
op|'='
string|"'2.0'"
newline|'\n'
nl|'\n'
DECL|variable|VERSION_ALIASES
name|'VERSION_ALIASES'
op|'='
op|'{'
nl|'\n'
string|"'grizzly'"
op|':'
string|"'2.6'"
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'version_cap'
op|'='
name|'self'
op|'.'
name|'VERSION_ALIASES'
op|'.'
name|'get'
op|'('
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'scheduler'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'scheduler'
op|')'
newline|'\n'
name|'super'
op|'('
name|'SchedulerAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'topic'
op|'='
name|'CONF'
op|'.'
name|'scheduler_topic'
op|','
nl|'\n'
name|'default_version'
op|'='
name|'self'
op|'.'
name|'BASE_RPC_API_VERSION'
op|','
nl|'\n'
name|'version_cap'
op|'='
name|'version_cap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|select_destinations
dedent|''
name|'def'
name|'select_destinations'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'select_destinations'"
op|','
nl|'\n'
name|'request_spec'
op|'='
name|'request_spec'
op|','
name|'filter_properties'
op|'='
name|'filter_properties'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'2.7'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|run_instance
dedent|''
name|'def'
name|'run_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'request_spec'
op|','
name|'admin_password'
op|','
nl|'\n'
name|'injected_files'
op|','
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
name|'return'
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'run_instance'"
op|','
nl|'\n'
name|'request_spec'
op|'='
name|'request_spec'
op|','
name|'admin_password'
op|'='
name|'admin_password'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'injected_files'
op|','
nl|'\n'
name|'requested_networks'
op|'='
name|'requested_networks'
op|','
nl|'\n'
name|'is_first_time'
op|'='
name|'is_first_time'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|prep_resize
dedent|''
name|'def'
name|'prep_resize'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'instance_type'
op|','
name|'image'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'filter_properties'
op|','
name|'reservations'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'instance_type_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'instance_type'
op|')'
newline|'\n'
name|'reservations_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'reservations'
op|')'
newline|'\n'
name|'image_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'image'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'prep_resize'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance_p'
op|','
name|'instance_type'
op|'='
name|'instance_type_p'
op|','
nl|'\n'
name|'image'
op|'='
name|'image_p'
op|','
name|'request_spec'
op|'='
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|','
nl|'\n'
name|'reservations'
op|'='
name|'reservations_p'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|live_migration
dedent|''
name|'def'
name|'live_migration'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'block_migration'
op|','
name|'disk_over_commit'
op|','
nl|'\n'
name|'instance'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(comstud): Call vs cast so we can get exceptions back, otherwise'
nl|'\n'
comment|"# this call in the scheduler driver doesn't return anything."
nl|'\n'
indent|'        '
name|'instance_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'live_migration'"
op|','
nl|'\n'
name|'block_migration'
op|'='
name|'block_migration'
op|','
nl|'\n'
name|'disk_over_commit'
op|'='
name|'disk_over_commit'
op|','
name|'instance'
op|'='
name|'instance_p'
op|','
nl|'\n'
name|'dest'
op|'='
name|'dest'
op|')'
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
name|'ctxt'
op|','
name|'service_name'
op|','
name|'host'
op|','
nl|'\n'
name|'capabilities'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'fanout_cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'update_service_capabilities'"
op|','
nl|'\n'
name|'service_name'
op|'='
name|'service_name'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'capabilities'
op|'='
name|'capabilities'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'2.4'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|select_hosts
dedent|''
name|'def'
name|'select_hosts'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'select_hosts'"
op|','
nl|'\n'
name|'request_spec'
op|'='
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'2.6'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
