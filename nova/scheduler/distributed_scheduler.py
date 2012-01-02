begin_unit
comment|'# Copyright (c) 2011 Openstack, LLC.'
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
string|'"""\nThe DistributedScheduler is for creating instances locally or across zones.\nYou can customize this scheduler by specifying your own Host Filters and\nWeighing Functions.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'operator'
newline|'\n'
nl|'\n'
name|'import'
name|'M2Crypto'
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
name|'novaclient'
name|'import'
name|'v1_1'
name|'as'
name|'novaclient'
newline|'\n'
name|'from'
name|'novaclient'
name|'import'
name|'exceptions'
name|'as'
name|'novaclient_exceptions'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'crypto'
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
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'least_cost'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'scheduler_options'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_list'
op|'('
string|"'default_host_filters'"
op|','
op|'['
string|"'InstanceTypeFilter'"
op|']'
op|','
nl|'\n'
string|"'Which filters to use for filtering hosts when not specified '"
nl|'\n'
string|"'in the request.'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.scheduler.distributed_scheduler'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidBlob
name|'class'
name|'InvalidBlob'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Ill-formed or incorrectly routed \'blob\' data sent "'
nl|'\n'
string|'"to instance create request."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DistributedScheduler
dedent|''
name|'class'
name|'DistributedScheduler'
op|'('
name|'driver'
op|'.'
name|'Scheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Scheduler that can work across any nova deployment, from simple\n    deployments to multiple nested zones.\n    """'
newline|'\n'
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
name|'DistributedScheduler'
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
name|'cost_function_cache'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'options'
op|'='
name|'scheduler_options'
op|'.'
name|'SchedulerOptions'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule
dedent|''
name|'def'
name|'schedule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|','
name|'method'
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
string|'"""The schedule() contract requires we return the one\n        best-suited host for this request.\n\n        NOTE: We\'re only focused on compute instances right now,\n        so this method will always raise NoValidHost()."""'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"No host selection for %s defined."'
op|'%'
name|'topic'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
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
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is called from nova.compute.api to provision\n        an instance. However we need to look at the parameters being\n        passed in to see if this is a request to:\n        1. Create build plan (a list of WeightedHosts) and then provision, or\n        2. Use the WeightedHost information in the request parameters\n           to simply create the instance (either in this zone or\n           a child zone).\n\n        returns a list of the instances created.\n        """'
newline|'\n'
nl|'\n'
name|'elevated'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'num_instances'"
op|','
number|'1'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Attempting to build %(num_instances)d instance(s)"'
op|')'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'weighted_hosts'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|"# Having a 'blob' hint means we've already provided a build plan."
nl|'\n'
comment|'# We need to turn this back into a WeightedHost object.'
nl|'\n'
name|'blob'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'blob'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'blob'
op|':'
newline|'\n'
indent|'            '
name|'weighted_hosts'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_make_weighted_host_from_blob'
op|'('
name|'blob'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# No plan ... better make one.'
nl|'\n'
indent|'            '
name|'weighted_hosts'
op|'='
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'elevated'
op|','
string|'"compute"'
op|','
name|'request_spec'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'weighted_hosts'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
name|'_'
op|'('
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'instances'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'num'
name|'in'
name|'xrange'
op|'('
name|'num_instances'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'weighted_hosts'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'weighted_host'
op|'='
name|'weighted_hosts'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'weighted_host'
op|'.'
name|'host'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_provision_resource_locally'
op|'('
name|'elevated'
op|','
nl|'\n'
name|'weighted_host'
op|','
name|'request_spec'
op|','
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_ask_child_zone_to_create_instance'
op|'('
name|'elevated'
op|','
nl|'\n'
name|'weighted_host'
op|','
name|'request_spec'
op|','
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'instance'
op|':'
newline|'\n'
indent|'                '
name|'instances'
op|'.'
name|'append'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'instances'
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
name|'request_spec'
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
string|'"""Select a target for resize.\n\n        Selects a target host for the instance, post-resize, and casts\n        the prep_resize operation to it.\n        """'
newline|'\n'
nl|'\n'
comment|'# We need the new instance type ID...'
nl|'\n'
name|'instance_type_id'
op|'='
name|'kwargs'
op|'['
string|"'instance_type_id'"
op|']'
newline|'\n'
nl|'\n'
name|'elevated'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Attempting to determine target host for resize to "'
nl|'\n'
string|'"instance type %(instance_type_id)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Convert it to an actual instance type'
nl|'\n'
name|'instance_type'
op|'='
name|'db'
op|'.'
name|'instance_type_get'
op|'('
name|'elevated'
op|','
name|'instance_type_id'
op|')'
newline|'\n'
nl|'\n'
comment|"# Now let's grab a possibility"
nl|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'elevated'
op|','
string|"'compute'"
op|','
name|'request_spec'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'hosts'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
name|'_'
op|'('
string|'""'
op|')'
op|')'
newline|'\n'
dedent|''
name|'host'
op|'='
name|'hosts'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
comment|'# Forward off to the host'
nl|'\n'
name|'driver'
op|'.'
name|'cast_to_host'
op|'('
name|'context'
op|','
string|"'compute'"
op|','
name|'host'
op|'.'
name|'host'
op|','
string|"'prep_resize'"
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|select
dedent|''
name|'def'
name|'select'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
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
string|'"""Select returns a list of weights and zone/host information\n        corresponding to the best hosts to service the request. Any\n        internal zone information will be encrypted so as not to reveal\n        anything about our inner layout.\n        """'
newline|'\n'
name|'elevated'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'weighted_hosts'
op|'='
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'elevated'
op|','
string|'"compute"'
op|','
name|'request_spec'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
op|'['
name|'weighted_host'
op|'.'
name|'to_dict'
op|'('
op|')'
name|'for'
name|'weighted_host'
name|'in'
name|'weighted_hosts'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_call_zone_method
dedent|''
name|'def'
name|'_call_zone_method'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'method'
op|','
name|'specs'
op|','
name|'zones'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call novaclient zone method. Broken out for testing."""'
newline|'\n'
name|'return'
name|'api'
op|'.'
name|'call_zone_method'
op|'('
name|'context'
op|','
name|'method'
op|','
name|'specs'
op|'='
name|'specs'
op|','
name|'zones'
op|'='
name|'zones'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_provision_resource_locally
dedent|''
name|'def'
name|'_provision_resource_locally'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'weighted_host'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create the requested resource in this Zone."""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_instance_db_entry'
op|'('
name|'context'
op|','
name|'request_spec'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'cast_to_compute_host'
op|'('
name|'context'
op|','
name|'weighted_host'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'run_instance'"
op|','
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'inst'
op|'='
name|'driver'
op|'.'
name|'encode_instance'
op|'('
name|'instance'
op|','
name|'local'
op|'='
name|'True'
op|')'
newline|'\n'
comment|'# So if another instance is created, create_instance_db_entry will'
nl|'\n'
comment|"# actually create a new entry, instead of assume it's been created"
nl|'\n'
comment|'# already'
nl|'\n'
name|'del'
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'return'
name|'inst'
newline|'\n'
nl|'\n'
DECL|member|_make_weighted_host_from_blob
dedent|''
name|'def'
name|'_make_weighted_host_from_blob'
op|'('
name|'self'
op|','
name|'blob'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the decrypted blob as a WeightedHost object\n        or None if invalid. Broken out for testing.\n        """'
newline|'\n'
name|'decryptor'
op|'='
name|'crypto'
op|'.'
name|'decryptor'
op|'('
name|'FLAGS'
op|'.'
name|'build_plan_encryption_key'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'json_entry'
op|'='
name|'decryptor'
op|'('
name|'blob'
op|')'
newline|'\n'
comment|'# Extract our WeightedHost values'
nl|'\n'
name|'wh_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'json_entry'
op|')'
newline|'\n'
name|'host'
op|'='
name|'wh_dict'
op|'.'
name|'get'
op|'('
string|"'host'"
op|','
name|'None'
op|')'
newline|'\n'
name|'blob'
op|'='
name|'wh_dict'
op|'.'
name|'get'
op|'('
string|"'blob'"
op|','
name|'None'
op|')'
newline|'\n'
name|'zone'
op|'='
name|'wh_dict'
op|'.'
name|'get'
op|'('
string|"'zone'"
op|','
name|'None'
op|')'
newline|'\n'
name|'return'
name|'least_cost'
op|'.'
name|'WeightedHost'
op|'('
name|'wh_dict'
op|'['
string|"'weight'"
op|']'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
name|'blob'
op|'='
name|'blob'
op|','
name|'zone'
op|'='
name|'zone'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'M2Crypto'
op|'.'
name|'EVP'
op|'.'
name|'EVPError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidBlob'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_ask_child_zone_to_create_instance
dedent|''
dedent|''
name|'def'
name|'_ask_child_zone_to_create_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'weighted_host'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Once we have determined that the request should go to one\n        of our children, we need to fabricate a new POST /servers/\n        call with the same parameters that were passed into us.\n        This request is always for a single instance.\n\n        Note that we have to reverse engineer from our args to get back the\n        image, flavor, ipgroup, etc. since the original call could have\n        come in from EC2 (which doesn\'t use these things).\n        """'
newline|'\n'
name|'instance_type'
op|'='
name|'request_spec'
op|'['
string|"'instance_type'"
op|']'
newline|'\n'
name|'instance_properties'
op|'='
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
newline|'\n'
nl|'\n'
name|'name'
op|'='
name|'instance_properties'
op|'['
string|"'display_name'"
op|']'
newline|'\n'
name|'image_ref'
op|'='
name|'instance_properties'
op|'['
string|"'image_ref'"
op|']'
newline|'\n'
name|'meta'
op|'='
name|'instance_properties'
op|'['
string|"'metadata'"
op|']'
newline|'\n'
name|'flavor_id'
op|'='
name|'instance_type'
op|'['
string|"'flavorid'"
op|']'
newline|'\n'
name|'reservation_id'
op|'='
name|'instance_properties'
op|'['
string|"'reservation_id'"
op|']'
newline|'\n'
name|'files'
op|'='
name|'kwargs'
op|'['
string|"'injected_files'"
op|']'
newline|'\n'
nl|'\n'
name|'zone'
op|'='
name|'db'
op|'.'
name|'zone_get'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
name|'weighted_host'
op|'.'
name|'zone'
op|')'
newline|'\n'
name|'zone_name'
op|'='
name|'zone'
op|'.'
name|'name'
newline|'\n'
name|'url'
op|'='
name|'zone'
op|'.'
name|'api_url'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Forwarding instance create call to zone \'%(zone_name)s\'. "'
nl|'\n'
string|'"ReservationID=%(reservation_id)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'nova'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# This operation is done as the caller, not the zone admin.'
nl|'\n'
indent|'            '
name|'nova'
op|'='
name|'novaclient'
op|'.'
name|'Client'
op|'('
name|'zone'
op|'.'
name|'username'
op|','
name|'zone'
op|'.'
name|'password'
op|','
name|'None'
op|','
name|'url'
op|','
nl|'\n'
name|'token'
op|'='
name|'context'
op|'.'
name|'auth_token'
op|','
nl|'\n'
name|'region_name'
op|'='
name|'zone_name'
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'authenticate'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'novaclient_exceptions'
op|'.'
name|'BadRequest'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
name|'_'
op|'('
string|'"Bad credentials attempting "'
nl|'\n'
string|'"to talk to zone at %(url)s."'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
comment|'# NOTE(Vek): Novaclient has two different calling conventions'
nl|'\n'
comment|"#            for this call, depending on whether you're using"
nl|'\n'
comment|"#            1.0 or 1.1 API: in 1.0, there's an ipgroups"
nl|'\n'
comment|"#            argument after flavor_id which isn't present in"
nl|'\n'
comment|'#            1.1.  To work around this, all the extra'
nl|'\n'
comment|'#            arguments are passed as keyword arguments'
nl|'\n'
comment|"#            (there's a reasonable default for ipgroups in the"
nl|'\n'
comment|'#            novaclient call).'
nl|'\n'
dedent|''
name|'instance'
op|'='
name|'nova'
op|'.'
name|'servers'
op|'.'
name|'create'
op|'('
name|'name'
op|','
name|'image_ref'
op|','
name|'flavor_id'
op|','
nl|'\n'
name|'meta'
op|'='
name|'meta'
op|','
name|'files'
op|'='
name|'files'
op|','
nl|'\n'
name|'zone_blob'
op|'='
name|'weighted_host'
op|'.'
name|'blob'
op|','
nl|'\n'
name|'reservation_id'
op|'='
name|'reservation_id'
op|')'
newline|'\n'
name|'return'
name|'driver'
op|'.'
name|'encode_instance'
op|'('
name|'instance'
op|'.'
name|'_info'
op|','
name|'local'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_adjust_child_weights
dedent|''
name|'def'
name|'_adjust_child_weights'
op|'('
name|'self'
op|','
name|'child_results'
op|','
name|'zones'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Apply the Scale and Offset values from the Zone definition\n        to adjust the weights returned from the child zones. Returns\n        a list of WeightedHost objects: [WeightedHost(), ...]\n        """'
newline|'\n'
name|'weighted_hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'zone_id'
op|','
name|'result'
name|'in'
name|'child_results'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'zone_rec'
name|'in'
name|'zones'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'zone_rec'
op|'['
string|"'id'"
op|']'
op|'!='
name|'zone_id'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'for'
name|'item'
name|'in'
name|'result'
op|':'
newline|'\n'
indent|'                    '
name|'try'
op|':'
newline|'\n'
indent|'                        '
name|'offset'
op|'='
name|'zone_rec'
op|'['
string|"'weight_offset'"
op|']'
newline|'\n'
name|'scale'
op|'='
name|'zone_rec'
op|'['
string|"'weight_scale'"
op|']'
newline|'\n'
name|'raw_weight'
op|'='
name|'item'
op|'['
string|"'weight'"
op|']'
newline|'\n'
name|'cooked_weight'
op|'='
name|'offset'
op|'+'
name|'scale'
op|'*'
name|'raw_weight'
newline|'\n'
nl|'\n'
name|'weighted_hosts'
op|'.'
name|'append'
op|'('
name|'least_cost'
op|'.'
name|'WeightedHost'
op|'('
nl|'\n'
name|'host'
op|'='
name|'None'
op|','
name|'weight'
op|'='
name|'cooked_weight'
op|','
nl|'\n'
name|'zone'
op|'='
name|'zone_id'
op|','
name|'blob'
op|'='
name|'item'
op|'['
string|"'blob'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'                        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Bad child zone scaling values "'
nl|'\n'
string|'"for Zone: %(zone_id)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'return'
name|'weighted_hosts'
newline|'\n'
nl|'\n'
DECL|member|_zone_get_all
dedent|''
name|'def'
name|'_zone_get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Broken out for testing."""'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'zone_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_configuration_options
dedent|''
name|'def'
name|'_get_configuration_options'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Fetch options dictionary. Broken out for testing."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'options'
op|'.'
name|'get_configuration'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_schedule
dedent|''
name|'def'
name|'_schedule'
op|'('
name|'self'
op|','
name|'elevated'
op|','
name|'topic'
op|','
name|'request_spec'
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
string|'"""Returns a list of hosts that meet the required specs,\n        ordered by their fitness.\n        """'
newline|'\n'
name|'if'
name|'topic'
op|'!='
string|'"compute"'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Scheduler only understands Compute nodes (for now)"'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'instance_type'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|'"instance_type"'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance_type'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Scheduler only understands InstanceType-based"'
string|'"provisioning."'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cost_functions'
op|'='
name|'self'
op|'.'
name|'get_cost_functions'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'ram_requirement_mb'
op|'='
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'disk_requirement_bg'
op|'='
name|'instance_type'
op|'['
string|"'local_gb'"
op|']'
newline|'\n'
nl|'\n'
name|'options'
op|'='
name|'self'
op|'.'
name|'_get_configuration_options'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Find our local list of acceptable hosts by repeatedly'
nl|'\n'
comment|'# filtering and weighing our options. Each time we choose a'
nl|'\n'
comment|'# host, we virtually consume resources on it so subsequent'
nl|'\n'
comment|'# selections can adjust accordingly.'
nl|'\n'
nl|'\n'
comment|'# unfiltered_hosts_dict is {host : ZoneManager.HostInfo()}'
nl|'\n'
name|'unfiltered_hosts_dict'
op|'='
name|'self'
op|'.'
name|'zone_manager'
op|'.'
name|'get_all_host_data'
op|'('
name|'elevated'
op|')'
newline|'\n'
name|'unfiltered_hosts'
op|'='
name|'unfiltered_hosts_dict'
op|'.'
name|'items'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'num_instances'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'num_instances'"
op|','
number|'1'
op|')'
newline|'\n'
name|'selected_hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'num'
name|'in'
name|'xrange'
op|'('
name|'num_instances'
op|')'
op|':'
newline|'\n'
comment|'# Filter local hosts based on requirements ...'
nl|'\n'
indent|'            '
name|'filtered_hosts'
op|'='
name|'self'
op|'.'
name|'_filter_hosts'
op|'('
name|'topic'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'unfiltered_hosts'
op|','
name|'options'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'filtered_hosts'
op|':'
newline|'\n'
comment|"# Can't get any more locally."
nl|'\n'
indent|'                '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Filtered %(filtered_hosts)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# weighted_host = WeightedHost() ... the best'
nl|'\n'
comment|'# host for the job.'
nl|'\n'
name|'weighted_host'
op|'='
name|'least_cost'
op|'.'
name|'weighted_sum'
op|'('
name|'cost_functions'
op|','
nl|'\n'
name|'filtered_hosts'
op|','
name|'options'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Weighted %(weighted_host)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'selected_hosts'
op|'.'
name|'append'
op|'('
name|'weighted_host'
op|')'
newline|'\n'
nl|'\n'
comment|'# Now consume the resources so the filter/weights'
nl|'\n'
comment|'# will change for the next instance.'
nl|'\n'
name|'weighted_host'
op|'.'
name|'hostinfo'
op|'.'
name|'consume_resources'
op|'('
name|'disk_requirement_bg'
op|','
nl|'\n'
name|'ram_requirement_mb'
op|')'
newline|'\n'
nl|'\n'
comment|'# Next, tack on the host weights from the child zones'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'local_zone'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'json_spec'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'request_spec'
op|')'
newline|'\n'
name|'all_zones'
op|'='
name|'self'
op|'.'
name|'_zone_get_all'
op|'('
name|'elevated'
op|')'
newline|'\n'
name|'child_results'
op|'='
name|'self'
op|'.'
name|'_call_zone_method'
op|'('
name|'elevated'
op|','
string|'"select"'
op|','
nl|'\n'
name|'specs'
op|'='
name|'json_spec'
op|','
name|'zones'
op|'='
name|'all_zones'
op|')'
newline|'\n'
name|'selected_hosts'
op|'.'
name|'extend'
op|'('
name|'self'
op|'.'
name|'_adjust_child_weights'
op|'('
nl|'\n'
name|'child_results'
op|','
name|'all_zones'
op|')'
op|')'
newline|'\n'
dedent|''
name|'selected_hosts'
op|'.'
name|'sort'
op|'('
name|'key'
op|'='
name|'operator'
op|'.'
name|'attrgetter'
op|'('
string|"'weight'"
op|')'
op|')'
newline|'\n'
name|'return'
name|'selected_hosts'
op|'['
op|':'
name|'num_instances'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_filter_classes
dedent|''
name|'def'
name|'_get_filter_classes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Imported here to avoid circular imports'
nl|'\n'
indent|'        '
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
nl|'\n'
DECL|function|get_itm
name|'def'
name|'get_itm'
op|'('
name|'nm'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'getattr'
op|'('
name|'filters'
op|','
name|'nm'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'['
name|'get_itm'
op|'('
name|'itm'
op|')'
name|'for'
name|'itm'
name|'in'
name|'dir'
op|'('
name|'filters'
op|')'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'get_itm'
op|'('
name|'itm'
op|')'
op|','
name|'type'
op|')'
nl|'\n'
name|'and'
name|'issubclass'
op|'('
name|'get_itm'
op|'('
name|'itm'
op|')'
op|','
name|'filters'
op|'.'
name|'AbstractHostFilter'
op|')'
nl|'\n'
name|'and'
name|'get_itm'
op|'('
name|'itm'
op|')'
name|'is'
name|'not'
name|'filters'
op|'.'
name|'AbstractHostFilter'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_choose_host_filters
dedent|''
name|'def'
name|'_choose_host_filters'
op|'('
name|'self'
op|','
name|'filters'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Since the caller may specify which filters to use we need\n        to have an authoritative list of what is permissible. This\n        function checks the filter names against a predefined set\n        of acceptable filters.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'filters'
op|':'
newline|'\n'
indent|'            '
name|'filters'
op|'='
name|'FLAGS'
op|'.'
name|'default_host_filters'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'filters'
op|','
op|'('
name|'list'
op|','
name|'tuple'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'filters'
op|'='
op|'['
name|'filters'
op|']'
newline|'\n'
dedent|''
name|'good_filters'
op|'='
op|'['
op|']'
newline|'\n'
name|'bad_filters'
op|'='
op|'['
op|']'
newline|'\n'
name|'filter_classes'
op|'='
name|'self'
op|'.'
name|'_get_filter_classes'
op|'('
op|')'
newline|'\n'
name|'for'
name|'filter_name'
name|'in'
name|'filters'
op|':'
newline|'\n'
indent|'            '
name|'found_class'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'cls'
name|'in'
name|'filter_classes'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'cls'
op|'.'
name|'__name__'
op|'=='
name|'filter_name'
op|':'
newline|'\n'
indent|'                    '
name|'good_filters'
op|'.'
name|'append'
op|'('
name|'cls'
op|'('
op|')'
op|')'
newline|'\n'
name|'found_class'
op|'='
name|'True'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'found_class'
op|':'
newline|'\n'
indent|'                '
name|'bad_filters'
op|'.'
name|'append'
op|'('
name|'filter_name'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'bad_filters'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
string|'", "'
op|'.'
name|'join'
op|'('
name|'bad_filters'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'SchedulerHostFilterNotFound'
op|'('
name|'filter_name'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'good_filters'
newline|'\n'
nl|'\n'
DECL|member|_filter_hosts
dedent|''
name|'def'
name|'_filter_hosts'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'request_spec'
op|','
name|'hosts'
op|','
name|'options'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Filter the full host list. hosts = [(host, HostInfo()), ...].\n        This method returns a subset of hosts, in the same format."""'
newline|'\n'
name|'selected_filters'
op|'='
name|'self'
op|'.'
name|'_choose_host_filters'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Filter out original host'
nl|'\n'
name|'if'
op|'('
string|"'original_host'"
name|'in'
name|'request_spec'
name|'and'
nl|'\n'
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'avoid_original_host'"
op|','
name|'True'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'hosts'
op|'='
op|'['
op|'('
name|'h'
op|','
name|'hi'
op|')'
name|'for'
name|'h'
op|','
name|'hi'
name|'in'
name|'hosts'
nl|'\n'
name|'if'
name|'h'
op|'!='
name|'request_spec'
op|'['
string|"'original_host'"
op|']'
op|']'
newline|'\n'
nl|'\n'
comment|"# TODO(sandy): We're only using InstanceType-based specs"
nl|'\n'
comment|"# currently. Later we'll need to snoop for more detailed"
nl|'\n'
comment|'# host filter requests.'
nl|'\n'
dedent|''
name|'instance_type'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|'"instance_type"'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'instance_type'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# No way to select; return the specified hosts.'
nl|'\n'
indent|'            '
name|'return'
name|'hosts'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'selected_filter'
name|'in'
name|'selected_filters'
op|':'
newline|'\n'
indent|'            '
name|'query'
op|'='
name|'selected_filter'
op|'.'
name|'instance_type_to_filter'
op|'('
name|'instance_type'
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'selected_filter'
op|'.'
name|'filter_hosts'
op|'('
name|'hosts'
op|','
name|'query'
op|','
name|'options'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'hosts'
newline|'\n'
nl|'\n'
DECL|member|get_cost_functions
dedent|''
name|'def'
name|'get_cost_functions'
op|'('
name|'self'
op|','
name|'topic'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of tuples containing weights and cost functions to\n        use for weighing hosts\n        """'
newline|'\n'
name|'if'
name|'topic'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# Schedulers only support compute right now.'
nl|'\n'
indent|'            '
name|'topic'
op|'='
string|'"compute"'
newline|'\n'
dedent|''
name|'if'
name|'topic'
name|'in'
name|'self'
op|'.'
name|'cost_function_cache'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'cost_function_cache'
op|'['
name|'topic'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'cost_fns'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'cost_fn_str'
name|'in'
name|'FLAGS'
op|'.'
name|'least_cost_functions'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'.'"
name|'in'
name|'cost_fn_str'
op|':'
newline|'\n'
indent|'                '
name|'short_name'
op|'='
name|'cost_fn_str'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'short_name'
op|'='
name|'cost_fn_str'
newline|'\n'
name|'cost_fn_str'
op|'='
string|'"%s.%s.%s"'
op|'%'
op|'('
nl|'\n'
name|'__name__'
op|','
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|','
name|'short_name'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
op|'('
name|'short_name'
op|'.'
name|'startswith'
op|'('
string|"'%s_'"
op|'%'
name|'topic'
op|')'
name|'or'
nl|'\n'
name|'short_name'
op|'.'
name|'startswith'
op|'('
string|"'noop'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# NOTE: import_class is somewhat misnamed since'
nl|'\n'
comment|'# the weighing function can be any non-class callable'
nl|'\n'
comment|"# (i.e., no 'self')"
nl|'\n'
indent|'                '
name|'cost_fn'
op|'='
name|'utils'
op|'.'
name|'import_class'
op|'('
name|'cost_fn_str'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ClassNotFound'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'SchedulerCostFunctionNotFound'
op|'('
nl|'\n'
name|'cost_fn_str'
op|'='
name|'cost_fn_str'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'flag_name'
op|'='
string|'"%s_weight"'
op|'%'
name|'cost_fn'
op|'.'
name|'__name__'
newline|'\n'
name|'weight'
op|'='
name|'getattr'
op|'('
name|'FLAGS'
op|','
name|'flag_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'SchedulerWeightFlagNotFound'
op|'('
nl|'\n'
name|'flag_name'
op|'='
name|'flag_name'
op|')'
newline|'\n'
dedent|''
name|'cost_fns'
op|'.'
name|'append'
op|'('
op|'('
name|'weight'
op|','
name|'cost_fn'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'cost_function_cache'
op|'['
name|'topic'
op|']'
op|'='
name|'cost_fns'
newline|'\n'
name|'return'
name|'cost_fns'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
