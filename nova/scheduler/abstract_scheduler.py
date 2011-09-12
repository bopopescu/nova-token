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
string|'"""\nThe AbsractScheduler is an abstract class Scheduler for creating instances\nlocally or across zones. Two methods should be overridden in order to\ncustomize the behavior: filter_hosts() and weigh_hosts(). The default\nbehavior is to simply select all hosts and weight them the same.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'operator'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
nl|'\n'
name|'import'
name|'M2Crypto'
newline|'\n'
nl|'\n'
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
nl|'\n'
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
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.scheduler.abstract_scheduler'"
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
DECL|class|AbstractScheduler
dedent|''
name|'class'
name|'AbstractScheduler'
op|'('
name|'driver'
op|'.'
name|'Scheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for creating Schedulers that can work across any nova\n    deployment, from simple designs to multiply-nested zones.\n    """'
newline|'\n'
DECL|member|_call_zone_method
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
name|'build_plan_item'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create the requested resource in this Zone."""'
newline|'\n'
name|'host'
op|'='
name|'build_plan_item'
op|'['
string|"'hostname'"
op|']'
newline|'\n'
name|'base_options'
op|'='
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
newline|'\n'
name|'image'
op|'='
name|'request_spec'
op|'['
string|"'image'"
op|']'
newline|'\n'
name|'instance_type'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'instance_type'"
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(sandy): I guess someone needs to add block_device_mapping'
nl|'\n'
comment|'# support at some point? Also, OS API has no concept of security'
nl|'\n'
comment|'# groups.'
nl|'\n'
name|'instance'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'create_db_entry_for_new_instance'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_type'
op|','
name|'image'
op|','
name|'base_options'
op|','
name|'None'
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'kwargs'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'instance_id'
newline|'\n'
nl|'\n'
name|'queue'
op|'='
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
string|'"compute"'
op|','
name|'host'
op|')'
newline|'\n'
name|'params'
op|'='
op|'{'
string|'"method"'
op|':'
string|'"run_instance"'
op|','
string|'"args"'
op|':'
name|'kwargs'
op|'}'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
name|'queue'
op|','
name|'params'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Provisioning locally via compute node %(host)s"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_decrypt_blob
dedent|''
name|'def'
name|'_decrypt_blob'
op|'('
name|'self'
op|','
name|'blob'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the decrypted blob or None if invalid. Broken out\n        for testing.\n        """'
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
name|'return'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'json_entry'
op|')'
newline|'\n'
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
name|'pass'
newline|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_ask_child_zone_to_create_instance
dedent|''
name|'def'
name|'_ask_child_zone_to_create_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'zone_info'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Once we have determined that the request should go to one\n        of our children, we need to fabricate a new POST /servers/\n        call with the same parameters that were passed into us.\n\n        Note that we have to reverse engineer from our args to get back the\n        image, flavor, ipgroup, etc. since the original call could have\n        come in from EC2 (which doesn\'t use these things).\n        """'
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
name|'child_zone'
op|'='
name|'zone_info'
op|'['
string|"'child_zone'"
op|']'
newline|'\n'
name|'child_blob'
op|'='
name|'zone_info'
op|'['
string|"'child_blob'"
op|']'
newline|'\n'
name|'zone'
op|'='
name|'db'
op|'.'
name|'zone_get'
op|'('
name|'context'
op|','
name|'child_zone'
op|')'
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
string|'"Forwarding instance create call to child zone %(url)s"'
nl|'\n'
string|'". ReservationID=%(reservation_id)s"'
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
name|'zone_blob'
op|'='
name|'child_blob'
op|','
nl|'\n'
name|'reservation_id'
op|'='
name|'reservation_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_provision_resource_from_blob
dedent|''
name|'def'
name|'_provision_resource_from_blob'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'build_plan_item'
op|','
nl|'\n'
name|'instance_id'
op|','
name|'request_spec'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create the requested resource locally or in a child zone\n           based on what is stored in the zone blob info.\n\n           Attempt to decrypt the blob to see if this request is:\n           1. valid, and\n           2. intended for this zone or a child zone.\n\n           Note: If we have "blob" that means the request was passed\n           into us from a parent zone. If we have "child_blob" that\n           means we gathered the info from one of our children.\n           It\'s possible that, when we decrypt the \'blob\' field, it\n           contains "child_blob" data. In which case we forward the\n           request.\n           """'
newline|'\n'
name|'host_info'
op|'='
name|'None'
newline|'\n'
name|'if'
string|'"blob"'
name|'in'
name|'build_plan_item'
op|':'
newline|'\n'
comment|'# Request was passed in from above. Is it for us?'
nl|'\n'
indent|'            '
name|'host_info'
op|'='
name|'self'
op|'.'
name|'_decrypt_blob'
op|'('
name|'build_plan_item'
op|'['
string|"'blob'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'elif'
string|'"child_blob"'
name|'in'
name|'build_plan_item'
op|':'
newline|'\n'
comment|'# Our immediate child zone provided this info ...'
nl|'\n'
indent|'            '
name|'host_info'
op|'='
name|'build_plan_item'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'host_info'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidBlob'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Valid data ... is it for us?'
nl|'\n'
dedent|''
name|'if'
string|"'child_zone'"
name|'in'
name|'host_info'
name|'and'
string|"'child_blob'"
name|'in'
name|'host_info'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_ask_child_zone_to_create_instance'
op|'('
name|'context'
op|','
name|'host_info'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_provision_resource_locally'
op|'('
name|'context'
op|','
name|'host_info'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_provision_resource
dedent|''
dedent|''
name|'def'
name|'_provision_resource'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'build_plan_item'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create the requested resource in this Zone or a child zone."""'
newline|'\n'
name|'if'
string|'"hostname"'
name|'in'
name|'build_plan_item'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_provision_resource_locally'
op|'('
name|'context'
op|','
name|'build_plan_item'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_provision_resource_from_blob'
op|'('
name|'context'
op|','
name|'build_plan_item'
op|','
nl|'\n'
name|'instance_id'
op|','
name|'request_spec'
op|','
name|'kwargs'
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
string|'"""Apply the Scale and Offset values from the Zone definition\n        to adjust the weights returned from the child zones. Alters\n        child_results in place.\n        """'
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
name|'item'
op|'['
string|"'weight'"
op|']'
op|'='
name|'cooked_weight'
newline|'\n'
name|'item'
op|'['
string|"'raw_weight'"
op|']'
op|'='
name|'raw_weight'
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
nl|'\n'
DECL|member|schedule_run_instance
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'schedule_run_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
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
op|':'
newline|'\n'
indent|'        '
string|'"""This method is called from nova.compute.api to provision\n        an instance. However we need to look at the parameters being\n        passed in to see if this is a request to:\n        1. Create a Build Plan and then provision, or\n        2. Use the Build Plan information in the request parameters\n           to simply create the instance (either in this zone or\n           a child zone).\n        """'
newline|'\n'
comment|"# TODO(sandy): We'll have to look for richer specs at some point."
nl|'\n'
name|'blob'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'blob'"
op|')'
newline|'\n'
name|'if'
name|'blob'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_provision_resource'
op|'('
name|'context'
op|','
name|'request_spec'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
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
comment|'# Create build plan and provision ...'
nl|'\n'
name|'build_plan'
op|'='
name|'self'
op|'.'
name|'select'
op|'('
name|'context'
op|','
name|'request_spec'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'build_plan'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'driver'
op|'.'
name|'NoValidHost'
op|'('
name|'_'
op|'('
string|"'No hosts were available'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'build_plan'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'build_plan_item'
op|'='
name|'build_plan'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_provision_resource'
op|'('
name|'context'
op|','
name|'build_plan_item'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|'# Returning None short-circuits the routing to Compute (since'
nl|'\n'
comment|"# we've already done it here)"
nl|'\n'
dedent|''
name|'return'
name|'None'
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
string|'"""Select returns a list of weights and zone/host information\n        corresponding to the best hosts to service the request. Any\n        child zone information has been encrypted so as not to reveal\n        anything about the children.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
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
string|'"""The schedule() contract requires we return the one\n        best-suited host for this request.\n        """'
newline|'\n'
comment|"# TODO(sandy): We're only focused on compute instances right now,"
nl|'\n'
comment|'# so we don\'t implement the default "schedule()" method required'
nl|'\n'
comment|'# of Schedulers.'
nl|'\n'
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
name|'driver'
op|'.'
name|'NoValidHost'
op|'('
name|'msg'
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
name|'context'
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
comment|'# Get all available hosts.'
nl|'\n'
dedent|''
name|'all_hosts'
op|'='
name|'self'
op|'.'
name|'zone_manager'
op|'.'
name|'service_states'
op|'.'
name|'iteritems'
op|'('
op|')'
newline|'\n'
name|'unfiltered_hosts'
op|'='
op|'['
op|'('
name|'host'
op|','
name|'services'
op|'['
name|'topic'
op|']'
op|')'
nl|'\n'
name|'for'
name|'host'
op|','
name|'services'
name|'in'
name|'all_hosts'
nl|'\n'
name|'if'
name|'topic'
name|'in'
name|'services'
op|']'
newline|'\n'
nl|'\n'
comment|'# Filter local hosts based on requirements ...'
nl|'\n'
name|'filtered_hosts'
op|'='
name|'self'
op|'.'
name|'filter_hosts'
op|'('
name|'topic'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'unfiltered_hosts'
op|')'
newline|'\n'
nl|'\n'
comment|'# weigh the selected hosts.'
nl|'\n'
comment|'# weighted_hosts = [{weight=weight, hostname=hostname,'
nl|'\n'
comment|'#         capabilities=capabs}, ...]'
nl|'\n'
name|'weighted_hosts'
op|'='
name|'self'
op|'.'
name|'weigh_hosts'
op|'('
name|'topic'
op|','
name|'request_spec'
op|','
name|'filtered_hosts'
op|')'
newline|'\n'
comment|'# Next, tack on the host weights from the child zones'
nl|'\n'
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
name|'db'
op|'.'
name|'zone_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'child_results'
op|'='
name|'self'
op|'.'
name|'_call_zone_method'
op|'('
name|'context'
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
name|'self'
op|'.'
name|'_adjust_child_weights'
op|'('
name|'child_results'
op|','
name|'all_zones'
op|')'
newline|'\n'
name|'for'
name|'child_zone'
op|','
name|'result'
name|'in'
name|'child_results'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'weighting'
name|'in'
name|'result'
op|':'
newline|'\n'
comment|'# Remember the child_zone so we can get back to'
nl|'\n'
comment|'# it later if needed. This implicitly builds a zone'
nl|'\n'
comment|'# path structure.'
nl|'\n'
indent|'                '
name|'host_dict'
op|'='
op|'{'
string|'"weight"'
op|':'
name|'weighting'
op|'['
string|'"weight"'
op|']'
op|','
nl|'\n'
string|'"child_zone"'
op|':'
name|'child_zone'
op|','
nl|'\n'
string|'"child_blob"'
op|':'
name|'weighting'
op|'['
string|'"blob"'
op|']'
op|'}'
newline|'\n'
name|'weighted_hosts'
op|'.'
name|'append'
op|'('
name|'host_dict'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'weighted_hosts'
op|'.'
name|'sort'
op|'('
name|'key'
op|'='
name|'operator'
op|'.'
name|'itemgetter'
op|'('
string|"'weight'"
op|')'
op|')'
newline|'\n'
name|'return'
name|'weighted_hosts'
newline|'\n'
nl|'\n'
DECL|member|filter_hosts
dedent|''
name|'def'
name|'filter_hosts'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'request_spec'
op|','
name|'host_list'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Filter the full host list returned from the ZoneManager. By default,\n        this method only applies the basic_ram_filter(), meaning all hosts\n        with at least enough RAM for the requested instance are returned.\n\n        Override in subclasses to provide greater selectivity.\n        """'
newline|'\n'
DECL|function|basic_ram_filter
name|'def'
name|'basic_ram_filter'
op|'('
name|'hostname'
op|','
name|'capabilities'
op|','
name|'request_spec'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Only return hosts with sufficient available RAM."""'
newline|'\n'
name|'instance_type'
op|'='
name|'request_spec'
op|'['
string|"'instance_type'"
op|']'
newline|'\n'
name|'requested_mem'
op|'='
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
op|'*'
number|'1024'
op|'*'
number|'1024'
newline|'\n'
name|'return'
name|'capabilities'
op|'['
string|"'host_memory_free'"
op|']'
op|'>='
name|'requested_mem'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'['
op|'('
name|'host'
op|','
name|'services'
op|')'
name|'for'
name|'host'
op|','
name|'services'
name|'in'
name|'host_list'
nl|'\n'
name|'if'
name|'basic_ram_filter'
op|'('
name|'host'
op|','
name|'services'
op|','
name|'request_spec'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|weigh_hosts
dedent|''
name|'def'
name|'weigh_hosts'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'request_spec'
op|','
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This version assigns a weight of 1 to all hosts, making selection\n        of any host basically a random event. Override this method in your\n        subclass to add logic to prefer one potential host over another.\n        """'
newline|'\n'
name|'return'
op|'['
name|'dict'
op|'('
name|'weight'
op|'='
number|'1'
op|','
name|'hostname'
op|'='
name|'hostname'
op|','
name|'capabilities'
op|'='
name|'capabilities'
op|')'
nl|'\n'
name|'for'
name|'hostname'
op|','
name|'capabilities'
name|'in'
name|'hosts'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
