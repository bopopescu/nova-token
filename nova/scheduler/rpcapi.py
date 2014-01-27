begin_unit
comment|'# Copyright 2013, Red Hat, Inc.'
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
name|'from'
name|'oslo'
name|'import'
name|'messaging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'objects_base'
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
name|'import'
name|'rpc'
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
string|"'The topic scheduler nodes listen on'"
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
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Client side of the scheduler rpc API.\n\n    API version history:\n\n        1.0 - Initial version.\n        1.1 - Changes to prep_resize():\n                - remove instance_uuid, add instance\n                - remove instance_type_id, add instance_type\n                - remove topic, it was unused\n        1.2 - Remove topic from run_instance, it was unused\n        1.3 - Remove instance_id, add instance to live_migration\n        1.4 - Remove update_db from prep_resize\n        1.5 - Add reservations argument to prep_resize()\n        1.6 - Remove reservations argument to run_instance()\n        1.7 - Add create_volume() method, remove topic from live_migration()\n\n        2.0 - Remove 1.x backwards compat\n        2.1 - Add image_id to create_volume()\n        2.2 - Remove reservations argument to create_volume()\n        2.3 - Remove create_volume()\n        2.4 - Change update_service_capabilities()\n                - accepts a list of capabilities\n        2.5 - Add get_backdoor_port()\n        2.6 - Add select_hosts()\n\n        ... Grizzly supports message version 2.6.  So, any changes to existing\n        methods in 2.x after that point should be done such that they can\n        handle the version_cap being set to 2.6.\n\n        2.7 - Add select_destinations()\n        2.8 - Deprecate prep_resize() -- JUST KIDDING.  It is still used\n              by the compute manager for retries.\n        2.9 - Added the legacy_bdm_in_spec parameter to run_instance()\n\n        ... Havana supports message version 2.9.  So, any changes to existing\n        methods in 2.x after that point should be done such that they can\n        handle the version_cap being set to 2.9.\n\n        ... - Deprecated live_migration() call, moved to conductor\n        ... - Deprecated select_hosts()\n    '''"
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
string|"'havana'"
op|':'
string|"'2.9'"
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
name|'super'
op|'('
name|'SchedulerAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'target'
op|'='
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'topic'
op|'='
name|'CONF'
op|'.'
name|'scheduler_topic'
op|','
name|'version'
op|'='
string|"'2.0'"
op|')'
newline|'\n'
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
name|'serializer'
op|'='
name|'objects_base'
op|'.'
name|'NovaObjectSerializer'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'rpc'
op|'.'
name|'get_client'
op|'('
name|'target'
op|','
name|'version_cap'
op|'='
name|'version_cap'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'serializer'
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
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
string|"'2.7'"
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
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
op|','
name|'legacy_bdm_in_spec'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'version'
op|'='
string|"'2.0'"
newline|'\n'
name|'msg_kwargs'
op|'='
op|'{'
string|"'request_spec'"
op|':'
name|'request_spec'
op|','
nl|'\n'
string|"'admin_password'"
op|':'
name|'admin_password'
op|','
nl|'\n'
string|"'injected_files'"
op|':'
name|'injected_files'
op|','
nl|'\n'
string|"'requested_networks'"
op|':'
name|'requested_networks'
op|','
nl|'\n'
string|"'is_first_time'"
op|':'
name|'is_first_time'
op|','
nl|'\n'
string|"'filter_properties'"
op|':'
name|'filter_properties'
op|'}'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
string|"'2.9'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
string|"'2.9'"
newline|'\n'
name|'msg_kwargs'
op|'['
string|"'legacy_bdm_in_spec'"
op|']'
op|'='
name|'legacy_bdm_in_spec'
newline|'\n'
dedent|''
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
string|"'run_instance'"
op|','
op|'**'
name|'msg_kwargs'
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
name|'client'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
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
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
