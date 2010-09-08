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
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'StringIO'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
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
name|'service'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'endpoint'
name|'import'
name|'api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'endpoint'
name|'import'
name|'cloud'
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
nl|'\n'
name|'fake_storage'
op|'='
name|'True'
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
name|'service'
op|'.'
name|'ComputeService'
op|'('
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
name|'injected'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'compute_consumer'
op|'.'
name|'attach_to_twisted'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'create_user'
op|'('
string|"'admin'"
op|','
string|"'admin'"
op|','
string|"'admin'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
name|'admin'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_user'
op|'('
string|"'admin'"
op|')'
newline|'\n'
name|'project'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
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
name|'api'
op|'.'
name|'APIRequestContext'
op|'('
name|'handler'
op|'='
name|'None'
op|','
nl|'\n'
name|'project'
op|'='
name|'project'
op|','
nl|'\n'
name|'user'
op|'='
name|'admin'
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
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'delete_project'
op|'('
string|"'proj'"
op|')'
newline|'\n'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'delete_user'
op|'('
string|"'admin'"
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
name|'instance_id'
op|'='
string|"'foo'"
newline|'\n'
name|'inst'
op|'='
name|'yield'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'instance_id'
op|')'
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
name|'self'
op|'.'
name|'context'
op|','
op|'['
name|'instance_id'
op|']'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'output'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'output'
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
name|'instance_id'
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
name|'node'
op|'.'
name|'Instance'
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
dedent|''
dedent|''
endmarker|''
end_unit
