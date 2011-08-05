begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Isaku Yamahata'
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
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'s3'
newline|'\n'
nl|'\n'
nl|'\n'
name|'ami_manifest_xml'
op|'='
string|'"""<?xml version="1.0" ?>\n<manifest>\n        <version>2011-06-17</version>\n        <bundler>\n                <name>test-s3</name>\n                <version>0</version>\n                <release>0</release>\n        </bundler>\n        <machine_configuration>\n                <architecture>x86_64</architecture>\n                <block_device_mapping>\n                        <mapping>\n                                <virtual>ami</virtual>\n                                <device>sda1</device>\n                        </mapping>\n                        <mapping>\n                                <virtual>root</virtual>\n                                <device>/dev/sda1</device>\n                        </mapping>\n                        <mapping>\n                                <virtual>ephemeral0</virtual>\n                                <device>sda2</device>\n                        </mapping>\n                        <mapping>\n                                <virtual>swap</virtual>\n                                <device>sda3</device>\n                        </mapping>\n                </block_device_mapping>\n        </machine_configuration>\n</manifest>\n"""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestS3ImageService
name|'class'
name|'TestS3ImageService'
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
name|'TestS3ImageService'
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
name|'image_service'
op|'='
string|"'nova.image.fake.FakeImageService'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'='
name|'s3'
op|'.'
name|'S3ImageService'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_assertEqualList
dedent|''
name|'def'
name|'_assertEqualList'
op|'('
name|'self'
op|','
name|'list0'
op|','
name|'list1'
op|','
name|'keys'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'list0'
op|')'
op|','
name|'len'
op|'('
name|'list1'
op|')'
op|')'
newline|'\n'
name|'key'
op|'='
name|'keys'
op|'['
number|'0'
op|']'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'list0'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'x'
op|')'
op|','
name|'len'
op|'('
name|'keys'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'key'
name|'in'
name|'x'
op|')'
newline|'\n'
name|'for'
name|'y'
name|'in'
name|'list1'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'key'
name|'in'
name|'y'
op|')'
newline|'\n'
name|'if'
name|'x'
op|'['
name|'key'
op|']'
op|'=='
name|'y'
op|'['
name|'key'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'for'
name|'k'
name|'in'
name|'keys'
op|':'
newline|'\n'
indent|'                        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'x'
op|'['
name|'k'
op|']'
op|','
name|'y'
op|'['
name|'k'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_s3_create
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_s3_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
op|'{'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'root_device_name'"
op|':'
string|"'/dev/sda1'"
op|','
nl|'\n'
string|"'block_device_mapping'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/sda1'"
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
string|"'snap-12345678'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/sda2'"
op|','
nl|'\n'
string|"'virutal_name'"
op|':'
string|"'ephemeral0'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/sdb0'"
op|','
nl|'\n'
string|"'no_device'"
op|':'
name|'True'
op|'}'
op|']'
op|'}'
op|'}'
newline|'\n'
name|'_manifest'
op|','
name|'image'
op|'='
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'_s3_parse_manifest'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'metadata'
op|','
name|'ami_manifest_xml'
op|')'
newline|'\n'
name|'image_id'
op|'='
name|'image'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
name|'ret_image'
op|'='
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'properties'"
name|'in'
name|'ret_image'
op|')'
newline|'\n'
name|'properties'
op|'='
name|'ret_image'
op|'['
string|"'properties'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'mappings'"
name|'in'
name|'properties'
op|')'
newline|'\n'
name|'mappings'
op|'='
name|'properties'
op|'['
string|"'mappings'"
op|']'
newline|'\n'
name|'expected_mappings'
op|'='
op|'['
nl|'\n'
op|'{'
string|'"device"'
op|':'
string|'"sda1"'
op|','
string|'"virtual"'
op|':'
string|'"ami"'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"device"'
op|':'
string|'"/dev/sda1"'
op|','
string|'"virtual"'
op|':'
string|'"root"'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"device"'
op|':'
string|'"sda2"'
op|','
string|'"virtual"'
op|':'
string|'"ephemeral0"'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"device"'
op|':'
string|'"sda3"'
op|','
string|'"virtual"'
op|':'
string|'"swap"'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_assertEqualList'
op|'('
name|'mappings'
op|','
name|'expected_mappings'
op|','
nl|'\n'
op|'['
string|"'device'"
op|','
string|"'virtual'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'block_device_mapping'"
op|','
name|'properties'
op|')'
newline|'\n'
name|'block_device_mapping'
op|'='
name|'properties'
op|'['
string|"'block_device_mapping'"
op|']'
newline|'\n'
name|'expected_bdm'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/sda1'"
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
string|"'snap-12345678'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/sda2'"
op|','
nl|'\n'
string|"'virutal_name'"
op|':'
string|"'ephemeral0'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/sdb0'"
op|','
nl|'\n'
string|"'no_device'"
op|':'
name|'True'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'block_device_mapping'
op|','
name|'expected_bdm'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
