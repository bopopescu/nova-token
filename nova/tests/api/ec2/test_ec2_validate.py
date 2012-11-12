begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Cloudscaling, Inc.'
nl|'\n'
comment|'# Author: Joe Gordon <jogo@cloudscaling.com>'
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
name|'datetime'
newline|'\n'
nl|'\n'
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
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'ec2utils'
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
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_network'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
name|'import'
name|'fake'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'config'
op|'.'
name|'CONF'
newline|'\n'
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
DECL|class|EC2ValidateTestCase
name|'class'
name|'EC2ValidateTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'EC2ValidateTestCase'
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
name|'compute_driver'
op|'='
string|"'nova.virt.fake.FakeDriver'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|dumb
name|'def'
name|'dumb'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_utils'
op|','
string|"'notify_about_instance_usage'"
op|','
name|'dumb'
op|')'
newline|'\n'
name|'fake_network'
op|'.'
name|'set_stub_network_methods'
op|'('
name|'self'
op|'.'
name|'stubs'
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
comment|'# set up services'
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'compute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'scheduter'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'scheduler'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'network'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'='
name|'fake'
op|'.'
name|'FakeImageService'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'user_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'EC2_MALFORMED_IDS'
op|'='
op|'['
string|"'foobar'"
op|','
string|"''"
op|','
number|'123'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'EC2_VALID__IDS'
op|'='
op|'['
string|"'i-284f3a41'"
op|','
string|"'i-001'"
op|','
string|"'i-deadbeef'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ec2_id_exception_map'
op|'='
op|'['
op|'('
name|'x'
op|','
name|'exception'
op|'.'
name|'InvalidInstanceIDMalformed'
op|')'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'EC2_MALFORMED_IDS'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'ec2_id_exception_map'
op|'.'
name|'extend'
op|'('
op|'['
op|'('
name|'x'
op|','
name|'exception'
op|'.'
name|'InstanceNotFound'
op|')'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'EC2_VALID__IDS'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_id_exception_map'
op|'='
op|'['
op|'('
name|'x'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InvalidInstanceIDMalformed'
op|')'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'EC2_MALFORMED_IDS'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'volume_id_exception_map'
op|'.'
name|'extend'
op|'('
op|'['
op|'('
name|'x'
op|','
name|'exception'
op|'.'
name|'VolumeNotFound'
op|')'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'EC2_VALID__IDS'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_show
name|'def'
name|'fake_show'
op|'('
name|'meh'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'id'"
op|':'
name|'id'
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'ami'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'kernel_id'"
op|':'
string|"'cedef40a-ed67-4d10-800e-17455edce175'"
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
string|"'cedef40a-ed67-4d10-800e-17455edce175'"
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'machine'"
op|','
nl|'\n'
string|"'image_state'"
op|':'
string|"'available'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_detail
dedent|''
name|'def'
name|'fake_detail'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image'
op|'='
name|'fake_show'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'None'
op|')'
newline|'\n'
name|'image'
op|'['
string|"'name'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'return'
op|'['
name|'image'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'fake'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'fake'
op|'.'
name|'_FakeImageService'
op|','
string|"'show'"
op|','
name|'fake_show'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'fake'
op|'.'
name|'_FakeImageService'
op|','
string|"'detail'"
op|','
name|'fake_detail'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(comstud): Make 'cast' behave like a 'call' which will"
nl|'\n'
comment|'# ensure that operations complete'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'rpc'
op|','
string|"'cast'"
op|','
name|'rpc'
op|'.'
name|'call'
op|')'
newline|'\n'
nl|'\n'
comment|'# make sure we can map ami-00000001/2 to a uuid in FakeImageService'
nl|'\n'
name|'db'
op|'.'
name|'api'
op|'.'
name|'s3_image_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'cedef40a-ed67-4d10-800e-17455edce175'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'api'
op|'.'
name|'s3_image_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
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
name|'EC2ValidateTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'fake'
op|'.'
name|'FakeImageService_reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'#EC2_API tests (InvalidInstanceID.Malformed)'
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
name|'for'
name|'ec2_id'
op|','
name|'e'
name|'in'
name|'self'
op|'.'
name|'ec2_id_exception_map'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'e'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'get_console_output'
op|','
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|'='
op|'['
name|'ec2_id'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_describe_instance_attribute
dedent|''
dedent|''
name|'def'
name|'test_describe_instance_attribute'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'ec2_id'
op|','
name|'e'
name|'in'
name|'self'
op|'.'
name|'ec2_id_exception_map'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'e'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'describe_instance_attribute'
op|','
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'ec2_id'
op|','
nl|'\n'
name|'attribute'
op|'='
string|"'kernel'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_lifecycle
dedent|''
dedent|''
name|'def'
name|'test_instance_lifecycle'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'lifecycle'
op|'='
op|'['
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'terminate_instances'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'reboot_instances'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'stop_instances'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'start_instances'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'for'
name|'cmd'
name|'in'
name|'lifecycle'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'ec2_id'
op|','
name|'e'
name|'in'
name|'self'
op|'.'
name|'ec2_id_exception_map'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'e'
op|','
nl|'\n'
name|'cmd'
op|','
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|'='
op|'['
name|'ec2_id'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_image
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_create_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'ec2_id'
op|','
name|'e'
name|'in'
name|'self'
op|'.'
name|'ec2_id_exception_map'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'e'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'create_image'
op|','
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'ec2_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_snapshot
dedent|''
dedent|''
name|'def'
name|'test_create_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'ec2_id'
op|','
name|'e'
name|'in'
name|'self'
op|'.'
name|'volume_id_exception_map'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'e'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'create_snapshot'
op|','
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|'='
name|'ec2_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_describe_volumes
dedent|''
dedent|''
name|'def'
name|'test_describe_volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'ec2_id'
op|','
name|'e'
name|'in'
name|'self'
op|'.'
name|'volume_id_exception_map'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'e'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'describe_volumes'
op|','
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|'='
op|'['
name|'ec2_id'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_volume
dedent|''
dedent|''
name|'def'
name|'test_delete_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'ec2_id'
op|','
name|'e'
name|'in'
name|'self'
op|'.'
name|'volume_id_exception_map'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'e'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'delete_volume'
op|','
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|'='
name|'ec2_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_volume
dedent|''
dedent|''
name|'def'
name|'test_detach_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'ec2_id'
op|','
name|'e'
name|'in'
name|'self'
op|'.'
name|'volume_id_exception_map'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'e'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'detach_volume'
op|','
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|'='
name|'ec2_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|EC2TimestampValidationTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'EC2TimestampValidationTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for EC2 request timestamp validation"""'
newline|'\n'
nl|'\n'
DECL|member|test_validate_ec2_timestamp_valid
name|'def'
name|'test_validate_ec2_timestamp_valid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|"'Timestamp'"
op|':'
string|"'2011-04-22T11:29:49Z'"
op|'}'
newline|'\n'
name|'expired'
op|'='
name|'ec2utils'
op|'.'
name|'is_ec2_timestamp_expired'
op|'('
name|'params'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'expired'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate_ec2_timestamp_old_format
dedent|''
name|'def'
name|'test_validate_ec2_timestamp_old_format'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|"'Timestamp'"
op|':'
string|"'2011-04-22T11:29:49'"
op|'}'
newline|'\n'
name|'expired'
op|'='
name|'ec2utils'
op|'.'
name|'is_ec2_timestamp_expired'
op|'('
name|'params'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'expired'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate_ec2_timestamp_not_set
dedent|''
name|'def'
name|'test_validate_ec2_timestamp_not_set'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'expired'
op|'='
name|'ec2utils'
op|'.'
name|'is_ec2_timestamp_expired'
op|'('
name|'params'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'expired'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate_ec2_timestamp_invalid_format
dedent|''
name|'def'
name|'test_validate_ec2_timestamp_invalid_format'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|"'Timestamp'"
op|':'
string|"'2011-04-22T11:29:49.000P'"
op|'}'
newline|'\n'
name|'expired'
op|'='
name|'ec2utils'
op|'.'
name|'is_ec2_timestamp_expired'
op|'('
name|'params'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'expired'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate_ec2_timestamp_advanced_time
dedent|''
name|'def'
name|'test_validate_ec2_timestamp_advanced_time'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'#EC2 request with Timestamp in advanced time'
nl|'\n'
indent|'        '
name|'timestamp'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'+'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
number|'250'
op|')'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'Timestamp'"
op|':'
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'timestamp'
op|','
nl|'\n'
string|'"%Y-%m-%dT%H:%M:%SZ"'
op|')'
op|'}'
newline|'\n'
name|'expired'
op|'='
name|'ec2utils'
op|'.'
name|'is_ec2_timestamp_expired'
op|'('
name|'params'
op|','
name|'expires'
op|'='
number|'300'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'expired'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate_ec2_timestamp_advanced_time_expired
dedent|''
name|'def'
name|'test_validate_ec2_timestamp_advanced_time_expired'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'timestamp'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'+'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
number|'350'
op|')'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'Timestamp'"
op|':'
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'timestamp'
op|','
nl|'\n'
string|'"%Y-%m-%dT%H:%M:%SZ"'
op|')'
op|'}'
newline|'\n'
name|'expired'
op|'='
name|'ec2utils'
op|'.'
name|'is_ec2_timestamp_expired'
op|'('
name|'params'
op|','
name|'expires'
op|'='
number|'300'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'expired'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate_ec2_req_timestamp_not_expired
dedent|''
name|'def'
name|'test_validate_ec2_req_timestamp_not_expired'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|"'Timestamp'"
op|':'
name|'timeutils'
op|'.'
name|'isotime'
op|'('
op|')'
op|'}'
newline|'\n'
name|'expired'
op|'='
name|'ec2utils'
op|'.'
name|'is_ec2_timestamp_expired'
op|'('
name|'params'
op|','
name|'expires'
op|'='
number|'15'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'expired'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate_ec2_req_timestamp_expired
dedent|''
name|'def'
name|'test_validate_ec2_req_timestamp_expired'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|"'Timestamp'"
op|':'
string|"'2011-04-22T12:00:00Z'"
op|'}'
newline|'\n'
name|'compare'
op|'='
name|'ec2utils'
op|'.'
name|'is_ec2_timestamp_expired'
op|'('
name|'params'
op|','
name|'expires'
op|'='
number|'300'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'compare'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate_ec2_req_expired
dedent|''
name|'def'
name|'test_validate_ec2_req_expired'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|"'Expires'"
op|':'
name|'timeutils'
op|'.'
name|'isotime'
op|'('
op|')'
op|'}'
newline|'\n'
name|'expired'
op|'='
name|'ec2utils'
op|'.'
name|'is_ec2_timestamp_expired'
op|'('
name|'params'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'expired'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate_ec2_req_not_expired
dedent|''
name|'def'
name|'test_validate_ec2_req_not_expired'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expire'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'+'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
number|'350'
op|')'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'Expires'"
op|':'
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'expire'
op|','
string|'"%Y-%m-%dT%H:%M:%SZ"'
op|')'
op|'}'
newline|'\n'
name|'expired'
op|'='
name|'ec2utils'
op|'.'
name|'is_ec2_timestamp_expired'
op|'('
name|'params'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'expired'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate_Expires_timestamp_invalid_format
dedent|''
name|'def'
name|'test_validate_Expires_timestamp_invalid_format'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'#EC2 request with invalid Expires'
nl|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|"'Expires'"
op|':'
string|"'2011-04-22T11:29:49'"
op|'}'
newline|'\n'
name|'expired'
op|'='
name|'ec2utils'
op|'.'
name|'is_ec2_timestamp_expired'
op|'('
name|'params'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'expired'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate_ec2_req_timestamp_Expires
dedent|''
name|'def'
name|'test_validate_ec2_req_timestamp_Expires'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'#EC2 request with both Timestamp and Expires'
nl|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|"'Timestamp'"
op|':'
string|"'2011-04-22T11:29:49Z'"
op|','
nl|'\n'
string|"'Expires'"
op|':'
name|'timeutils'
op|'.'
name|'isotime'
op|'('
op|')'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidRequest'
op|','
nl|'\n'
name|'ec2utils'
op|'.'
name|'is_ec2_timestamp_expired'
op|','
nl|'\n'
name|'params'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
