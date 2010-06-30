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
comment|'# Copyright 2010 Anso Labs, LLC'
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
name|'time'
newline|'\n'
nl|'\n'
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
name|'vendor'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
nl|'\n'
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
name|'compute'
name|'import'
name|'model'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'node'
newline|'\n'
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
DECL|class|InstanceXmlTestCase
name|'class'
name|'InstanceXmlTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
op|')'
op|':'
newline|'\n'
comment|'# @defer.inlineCallbacks'
nl|'\n'
DECL|member|test_serialization
indent|'    '
name|'def'
name|'test_serialization'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# TODO: Reimplement this, it doesn't make sense in redis-land"
nl|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
comment|"# instance_id = 'foo'"
nl|'\n'
comment|'# first_node = node.Node()'
nl|'\n'
comment|'# inst = yield first_node.run_instance(instance_id)'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# # force the state so that we can verify that it changes'
nl|'\n'
comment|"# inst._s['state'] = node.Instance.NOSTATE"
nl|'\n'
comment|'# xml = inst.toXml()'
nl|'\n'
comment|'# self.assert_(ElementTree.parse(StringIO.StringIO(xml)))'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# second_node = node.Node()'
nl|'\n'
comment|'# new_inst = node.Instance.fromXml(second_node._conn, pool=second_node._pool, xml=xml)'
nl|'\n'
comment|'# self.assertEqual(new_inst.state, node.Instance.RUNNING)'
nl|'\n'
comment|'# rv = yield first_node.terminate_instance(instance_id)'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|NodeConnectionTestCase
dedent|''
dedent|''
name|'class'
name|'NodeConnectionTestCase'
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
name|'super'
op|'('
name|'NodeConnectionTestCase'
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
name|'fake_libvirt'
op|'='
name|'True'
op|','
nl|'\n'
name|'fake_storage'
op|'='
name|'True'
op|','
nl|'\n'
name|'fake_users'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'node'
op|'='
name|'node'
op|'.'
name|'Node'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_instance
dedent|''
name|'def'
name|'create_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instdir'
op|'='
name|'model'
op|'.'
name|'InstanceDirectory'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'='
name|'instdir'
op|'.'
name|'new'
op|'('
op|')'
newline|'\n'
comment|'# TODO(ja): add ami, ari, aki, user_data'
nl|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
string|"'r-fakeres'"
newline|'\n'
name|'inst'
op|'['
string|"'launch_time'"
op|']'
op|'='
string|"'10'"
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'inst'
op|'['
string|"'instance_type'"
op|']'
op|'='
string|"'m1.tiny'"
newline|'\n'
name|'inst'
op|'['
string|"'node_name'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'node_name'
newline|'\n'
name|'inst'
op|'['
string|"'mac_address'"
op|']'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'ami_launch_index'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'inst'
op|'['
string|"'instance_id'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|test_run_describe_terminate
name|'def'
name|'test_run_describe_terminate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'create_instance'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'run_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'describe_instances'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|'"Running instances: %s"'
op|','
name|'rv'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rv'
op|'['
name|'instance_id'
op|']'
op|'.'
name|'name'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'terminate_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'describe_instances'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|'"After terminating instances: %s"'
op|','
name|'rv'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rv'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|test_reboot
name|'def'
name|'test_reboot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'create_instance'
op|'('
op|')'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'run_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'describe_instances'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rv'
op|'['
name|'instance_id'
op|']'
op|'.'
name|'name'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'reboot_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'describe_instances'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rv'
op|'['
name|'instance_id'
op|']'
op|'.'
name|'name'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'terminate_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|test_console_output
name|'def'
name|'test_console_output'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'create_instance'
op|'('
op|')'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'run_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'console'
op|'='
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'get_console_output'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'console'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'terminate_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|test_run_instance_existing
name|'def'
name|'test_run_instance_existing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'create_instance'
op|'('
op|')'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'run_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'describe_instances'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rv'
op|'['
name|'instance_id'
op|']'
op|'.'
name|'name'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
name|'self'
op|'.'
name|'node'
op|'.'
name|'run_instance'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'self'
op|'.'
name|'node'
op|'.'
name|'terminate_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
