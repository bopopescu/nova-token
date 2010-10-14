begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
name|'from'
name|'base64'
name|'import'
name|'b64decode'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'from'
name|'M2Crypto'
name|'import'
name|'BIO'
newline|'\n'
name|'from'
name|'M2Crypto'
name|'import'
name|'RSA'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'StringIO'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'etree'
name|'import'
name|'ElementTree'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
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
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'cloud'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objectstore'
name|'import'
name|'image'
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
nl|'\n'
nl|'\n'
comment|'# Temp dirs for working with image attributes through the cloud controller'
nl|'\n'
comment|'# (stole this from objectstore_unittest.py)'
nl|'\n'
DECL|variable|OSS_TEMPDIR
name|'OSS_TEMPDIR'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
name|'prefix'
op|'='
string|"'test_oss-'"
op|')'
newline|'\n'
DECL|variable|IMAGES_PATH
name|'IMAGES_PATH'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'OSS_TEMPDIR'
op|','
string|"'images'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'IMAGES_PATH'
op|')'
newline|'\n'
nl|'\n'
DECL|class|CloudTestCase
name|'class'
name|'CloudTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
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
name|'CloudTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'connection_type'
op|'='
string|"'fake'"
op|','
name|'images_path'
op|'='
name|'IMAGES_PATH'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'rpc'
op|'.'
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
comment|'# set up our cloud'
nl|'\n'
name|'self'
op|'.'
name|'cloud'
op|'='
name|'cloud'
op|'.'
name|'CloudController'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# set up a service'
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_consumer'
op|'='
name|'rpc'
op|'.'
name|'AdapterConsumer'
op|'('
name|'connection'
op|'='
name|'self'
op|'.'
name|'conn'
op|','
nl|'\n'
name|'topic'
op|'='
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
nl|'\n'
name|'proxy'
op|'='
name|'self'
op|'.'
name|'compute'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_consumer'
op|'.'
name|'attach_to_eventlet'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'network_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_consumer'
op|'='
name|'rpc'
op|'.'
name|'AdapterConsumer'
op|'('
name|'connection'
op|'='
name|'self'
op|'.'
name|'conn'
op|','
nl|'\n'
name|'topic'
op|'='
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
nl|'\n'
name|'proxy'
op|'='
name|'self'
op|'.'
name|'network'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_consumer'
op|'.'
name|'attach_to_eventlet'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'admin'"
op|','
string|"'admin'"
op|','
string|"'admin'"
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'proj'"
op|','
string|"'admin'"
op|','
string|"'proj'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'APIRequestContext'
op|'('
name|'user'
op|'='
name|'self'
op|'.'
name|'user'
op|','
nl|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'super'
op|'('
name|'CloudTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_key
dedent|''
name|'def'
name|'_create_key'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): create depends on pool, so just call helper directly'
nl|'\n'
indent|'        '
name|'return'
name|'cloud'
op|'.'
name|'_gen_key'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'.'
name|'id'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_console_output
dedent|''
name|'def'
name|'test_console_output'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
name|'FLAGS'
op|'.'
name|'default_image'
newline|'\n'
name|'instance_type'
op|'='
name|'FLAGS'
op|'.'
name|'default_instance_type'
newline|'\n'
name|'max_count'
op|'='
number|'1'
newline|'\n'
name|'kwargs'
op|'='
op|'{'
string|"'image_id'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'instance_type'
op|','
nl|'\n'
string|"'max_count'"
op|':'
name|'max_count'
op|'}'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'run_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'instance_id'
op|'='
name|'rv'
op|'['
string|"'instancesSet'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'instanceId'"
op|']'
newline|'\n'
name|'output'
op|'='
name|'yield'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'get_console_output'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|'='
op|'['
name|'instance_id'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'b64decode'
op|'('
name|'output'
op|'['
string|"'output'"
op|']'
op|')'
op|','
string|"'FAKE CONSOLE OUTPUT'"
op|')'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'terminate_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'['
name|'instance_id'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_key_generation
dedent|''
name|'def'
name|'test_key_generation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'_create_key'
op|'('
string|"'test'"
op|')'
newline|'\n'
name|'private_key'
op|'='
name|'result'
op|'['
string|"'private_key'"
op|']'
newline|'\n'
name|'key'
op|'='
name|'RSA'
op|'.'
name|'load_key_string'
op|'('
name|'private_key'
op|','
name|'callback'
op|'='
name|'lambda'
op|':'
name|'None'
op|')'
newline|'\n'
name|'bio'
op|'='
name|'BIO'
op|'.'
name|'MemoryBuffer'
op|'('
op|')'
newline|'\n'
name|'public_key'
op|'='
name|'db'
op|'.'
name|'key_pair_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'test'"
op|')'
op|'['
string|"'public_key'"
op|']'
newline|'\n'
name|'key'
op|'.'
name|'save_pub_key_bio'
op|'('
name|'bio'
op|')'
newline|'\n'
name|'converted'
op|'='
name|'crypto'
op|'.'
name|'ssl_pub_to_ssh_pub'
op|'('
name|'bio'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
comment|'# assert key fields are equal'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'public_key'
op|'.'
name|'split'
op|'('
string|'" "'
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|','
nl|'\n'
name|'converted'
op|'.'
name|'split'
op|'('
string|'" "'
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_describe_key_pairs
dedent|''
name|'def'
name|'test_describe_key_pairs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_key'
op|'('
string|"'test1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_key'
op|'('
string|"'test2'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'describe_key_pairs'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'keys'
op|'='
name|'result'
op|'['
string|'"keypairsSet"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filter'
op|'('
name|'lambda'
name|'k'
op|':'
name|'k'
op|'['
string|"'keyName'"
op|']'
op|'=='
string|"'test1'"
op|','
name|'keys'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filter'
op|'('
name|'lambda'
name|'k'
op|':'
name|'k'
op|'['
string|"'keyName'"
op|']'
op|'=='
string|"'test2'"
op|','
name|'keys'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_key_pair
dedent|''
name|'def'
name|'test_delete_key_pair'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_key'
op|'('
string|"'test'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'delete_key_pair'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'test'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_instances
dedent|''
name|'def'
name|'test_run_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'FLAGS'
op|'.'
name|'connection_type'
op|'=='
string|"'fake'"
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Can\'t test instances without a real virtual env."'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'image_id'
op|'='
name|'FLAGS'
op|'.'
name|'default_image'
newline|'\n'
name|'instance_type'
op|'='
name|'FLAGS'
op|'.'
name|'default_instance_type'
newline|'\n'
name|'max_count'
op|'='
number|'1'
newline|'\n'
name|'kwargs'
op|'='
op|'{'
string|"'image_id'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'instance_type'
op|','
nl|'\n'
string|"'max_count'"
op|':'
name|'max_count'
op|'}'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'run_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
comment|'# TODO: check for proper response'
nl|'\n'
name|'instance'
op|'='
name|'rv'
op|'['
string|"'reservationSet'"
op|']'
op|'['
number|'0'
op|']'
op|'['
name|'rv'
op|'['
string|"'reservationSet'"
op|']'
op|'['
number|'0'
op|']'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Need to watch instance %s until it\'s running..."'
op|'%'
name|'instance'
op|'['
string|"'instance_id'"
op|']'
op|')'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'='
name|'yield'
name|'defer'
op|'.'
name|'succeed'
op|'('
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'_get_instance'
op|'('
name|'instance'
op|'['
string|"'instance_id'"
op|']'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'info'
op|'['
string|"'state'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'info'
op|'['
string|"'state'"
op|']'
op|'=='
name|'power_state'
op|'.'
name|'RUNNING'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assert_'
op|'('
name|'rv'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'connection_type'
op|'!='
string|"'fake'"
op|':'
newline|'\n'
indent|'            '
name|'time'
op|'.'
name|'sleep'
op|'('
number|'45'
op|')'
comment|'# Should use boto for polling here'
newline|'\n'
dedent|''
name|'for'
name|'reservations'
name|'in'
name|'rv'
op|'['
string|"'reservationSet'"
op|']'
op|':'
newline|'\n'
comment|'# for res_id in reservations.keys():'
nl|'\n'
comment|'#  logging.debug(reservations[res_id])'
nl|'\n'
comment|'# for instance in reservations[res_id]:'
nl|'\n'
indent|'           '
name|'for'
name|'instance'
name|'in'
name|'reservations'
op|'['
name|'reservations'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|']'
op|':'
newline|'\n'
indent|'               '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Terminating instance %s"'
op|'%'
name|'instance'
op|'['
string|"'instance_id'"
op|']'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'instance'
op|'['
string|"'instance_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_update_state
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_instance_update_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|instance
indent|'        '
name|'def'
name|'instance'
op|'('
name|'num'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
nl|'\n'
string|"'reservation_id'"
op|':'
string|"'r-1'"
op|','
nl|'\n'
string|"'instance_id'"
op|':'
string|"'i-%s'"
op|'%'
name|'num'
op|','
nl|'\n'
string|"'image_id'"
op|':'
string|"'ami-%s'"
op|'%'
name|'num'
op|','
nl|'\n'
string|"'private_dns_name'"
op|':'
string|"'10.0.0.%s'"
op|'%'
name|'num'
op|','
nl|'\n'
string|"'dns_name'"
op|':'
string|"'10.0.0%s'"
op|'%'
name|'num'
op|','
nl|'\n'
string|"'ami_launch_index'"
op|':'
name|'str'
op|'('
name|'num'
op|')'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'key_name'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'groups'"
op|':'
op|'['
string|"'default'"
op|']'
op|','
nl|'\n'
string|"'product_codes'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'state'"
op|':'
number|'0x01'
op|','
nl|'\n'
string|"'user_data'"
op|':'
string|"''"
nl|'\n'
op|'}'
newline|'\n'
dedent|''
name|'rv'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'_format_describe_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'len'
op|'('
name|'rv'
op|'['
string|"'reservationSet'"
op|']'
op|')'
op|'=='
number|'0'
op|')'
newline|'\n'
nl|'\n'
comment|'# simulate launch of 5 instances'
nl|'\n'
comment|"# self.cloud.instances['pending'] = {}"
nl|'\n'
comment|'#for i in xrange(5):'
nl|'\n'
comment|'#    inst = instance(i)'
nl|'\n'
comment|"#    self.cloud.instances['pending'][inst['instance_id']] = inst"
nl|'\n'
nl|'\n'
comment|'#rv = self.cloud._format_instances(self.admin)'
nl|'\n'
comment|"#self.assert_(len(rv['reservationSet']) == 1)"
nl|'\n'
comment|"#self.assert_(len(rv['reservationSet'][0]['instances_set']) == 5)"
nl|'\n'
comment|'# report 4 nodes each having 1 of the instances'
nl|'\n'
comment|'#for i in xrange(4):'
nl|'\n'
comment|"#    self.cloud.update_state('instances', {('node-%s' % i): {('i-%s' % i): instance(i)}})"
nl|'\n'
nl|'\n'
comment|'# one instance should be pending still'
nl|'\n'
comment|"#self.assert_(len(self.cloud.instances['pending'].keys()) == 1)"
nl|'\n'
nl|'\n'
comment|'# check that the reservations collapse'
nl|'\n'
comment|'#rv = self.cloud._format_instances(self.admin)'
nl|'\n'
comment|"#self.assert_(len(rv['reservationSet']) == 1)"
nl|'\n'
comment|"#self.assert_(len(rv['reservationSet'][0]['instances_set']) == 5)"
nl|'\n'
nl|'\n'
comment|'# check that we can get metadata for each instance'
nl|'\n'
comment|'#for i in xrange(4):'
nl|'\n'
comment|"#    data = self.cloud.get_metadata(instance(i)['private_dns_name'])"
nl|'\n'
comment|"#    self.assert_(data['meta-data']['ami-id'] == 'ami-%s' % i)"
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_fake_set_image_description
name|'def'
name|'_fake_set_image_description'
op|'('
name|'ctxt'
op|','
name|'image_id'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'from'
name|'nova'
op|'.'
name|'objectstore'
name|'import'
name|'handler'
newline|'\n'
DECL|class|req
name|'class'
name|'req'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'request'
op|'='
name|'req'
op|'('
op|')'
newline|'\n'
name|'request'
op|'.'
name|'context'
op|'='
name|'ctxt'
newline|'\n'
name|'request'
op|'.'
name|'args'
op|'='
op|'{'
string|"'image_id'"
op|':'
op|'['
name|'image_id'
op|']'
op|','
nl|'\n'
string|"'description'"
op|':'
op|'['
name|'description'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'resource'
op|'='
name|'handler'
op|'.'
name|'ImagesResource'
op|'('
op|')'
newline|'\n'
name|'resource'
op|'.'
name|'render_POST'
op|'('
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_user_editable_image_endpoint
dedent|''
name|'def'
name|'test_user_editable_image_endpoint'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pathdir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'images_path'
op|','
string|"'ami-testing'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'mkdir'
op|'('
name|'pathdir'
op|')'
newline|'\n'
name|'info'
op|'='
op|'{'
string|"'isPublic'"
op|':'
name|'False'
op|'}'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'pathdir'
op|','
string|"'info.json'"
op|')'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'json'
op|'.'
name|'dump'
op|'('
name|'info'
op|','
name|'f'
op|')'
newline|'\n'
dedent|''
name|'img'
op|'='
name|'image'
op|'.'
name|'Image'
op|'('
string|"'ami-testing'"
op|')'
newline|'\n'
comment|"# self.cloud.set_image_description(self.context, 'ami-testing',"
nl|'\n'
comment|"#                                  'Foo Img')"
nl|'\n'
comment|"# NOTE(vish): Above won't work unless we start objectstore or create"
nl|'\n'
comment|'#             a fake version of api/ec2/images.py conn that can'
nl|'\n'
comment|'#             call methods directly instead of going through boto.'
nl|'\n'
comment|'#             for now, just cheat and call the method directly'
nl|'\n'
name|'self'
op|'.'
name|'_fake_set_image_description'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'ami-testing'"
op|','
nl|'\n'
string|"'Foo Img'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'Foo Img'"
op|','
name|'img'
op|'.'
name|'metadata'
op|'['
string|"'description'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_fake_set_image_description'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'ami-testing'"
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'img'
op|'.'
name|'metadata'
op|'['
string|"'description'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_of_instance_display_fields
dedent|''
name|'def'
name|'test_update_of_instance_display_fields'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
op|'{'
op|'}'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'ec2_id'
op|'='
name|'cloud'
op|'.'
name|'internal_id_to_ec2_id'
op|'('
name|'inst'
op|'['
string|"'internal_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'update_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'ec2_id'
op|','
nl|'\n'
name|'display_name'
op|'='
string|"'c00l 1m4g3'"
op|')'
newline|'\n'
name|'inst'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
op|'{'
op|'}'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'c00l 1m4g3'"
op|','
name|'inst'
op|'['
string|"'display_name'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
op|'{'
op|'}'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_of_instance_wont_update_private_fields
dedent|''
name|'def'
name|'test_update_of_instance_wont_update_private_fields'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
op|'{'
op|'}'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'update_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'mac_address'
op|'='
string|"'DE:AD:BE:EF'"
op|')'
newline|'\n'
name|'inst'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
op|'{'
op|'}'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'None'
op|','
name|'inst'
op|'['
string|"'mac_address'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
op|'{'
op|'}'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_of_volume_display_fields
dedent|''
name|'def'
name|'test_update_of_volume_display_fields'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vol'
op|'='
name|'db'
op|'.'
name|'volume_create'
op|'('
op|'{'
op|'}'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'update_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'display_name'
op|'='
string|"'c00l v0lum3'"
op|')'
newline|'\n'
name|'vol'
op|'='
name|'db'
op|'.'
name|'volume_get'
op|'('
op|'{'
op|'}'
op|','
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'c00l v0lum3'"
op|','
name|'vol'
op|'['
string|"'display_name'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
op|'{'
op|'}'
op|','
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_of_volume_wont_update_private_fields
dedent|''
name|'def'
name|'test_update_of_volume_wont_update_private_fields'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vol'
op|'='
name|'db'
op|'.'
name|'volume_create'
op|'('
op|'{'
op|'}'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'update_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'mountpoint'
op|'='
string|"'/not/here'"
op|')'
newline|'\n'
name|'vol'
op|'='
name|'db'
op|'.'
name|'volume_get'
op|'('
op|'{'
op|'}'
op|','
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'None'
op|','
name|'vol'
op|'['
string|"'mountpoint'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
op|'{'
op|'}'
op|','
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
