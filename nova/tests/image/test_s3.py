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
name|'import'
name|'binascii'
newline|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'import'
name|'mox'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'s3'
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
op|'.'
name|'image'
name|'import'
name|'fake'
newline|'\n'
nl|'\n'
nl|'\n'
name|'ami_manifest_xml'
op|'='
string|'"""<?xml version="1.0" ?>\n<manifest>\n        <version>2011-06-17</version>\n        <bundler>\n                <name>test-s3</name>\n                <version>0</version>\n                <release>0</release>\n        </bundler>\n        <machine_configuration>\n                <architecture>x86_64</architecture>\n                <block_device_mapping>\n                        <mapping>\n                                <virtual>ami</virtual>\n                                <device>sda1</device>\n                        </mapping>\n                        <mapping>\n                                <virtual>root</virtual>\n                                <device>/dev/sda1</device>\n                        </mapping>\n                        <mapping>\n                                <virtual>ephemeral0</virtual>\n                                <device>sda2</device>\n                        </mapping>\n                        <mapping>\n                                <virtual>swap</virtual>\n                                <device>sda3</device>\n                        </mapping>\n                </block_device_mapping>\n                <kernel_id>aki-00000001</kernel_id>\n                <ramdisk_id>ari-00000001</ramdisk_id>\n        </machine_configuration>\n</manifest>\n"""'
newline|'\n'
nl|'\n'
name|'file_manifest_xml'
op|'='
string|'"""<?xml version="1.0" ?>\n<manifest>\n        <image>\n                <ec2_encrypted_key>foo</ec2_encrypted_key>\n                <user_encrypted_key>foo</user_encrypted_key>\n                <ec2_encrypted_iv>foo</ec2_encrypted_iv>\n                <parts count="1">\n                        <part index="0">\n                               <filename>foo</filename>\n                        </part>\n                </parts>\n        </image>\n</manifest>\n"""'
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
comment|"# set up one fixture to test shows, should have id '1'"
nl|'\n'
name|'nova'
op|'.'
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
string|"'155d900f-4e14-4e4c-a73d-069cbf4541e6'"
op|')'
newline|'\n'
nl|'\n'
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
name|'image_service'
op|'='
name|'s3'
op|'.'
name|'S3ImageService'
op|'('
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
name|'TestS3ImageService'
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
DECL|member|test_show_cannot_use_uuid
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_show_cannot_use_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ImageNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'show'
op|','
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'155d900f-4e14-4e4c-a73d-069cbf4541e6'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_translates_correctly
dedent|''
name|'def'
name|'test_show_translates_correctly'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail
dedent|''
name|'def'
name|'test_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_s3_create
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
op|','
name|'image_uuid'
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
name|'image'
op|'['
string|"'id'"
op|']'
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
nl|'\n'
DECL|member|test_s3_create_is_public
dedent|''
name|'def'
name|'test_s3_create_is_public'
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
string|"'image_location'"
op|':'
string|"'mybucket/my.img.manifest.xml'"
op|'}'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'mybucket/my.img'"
op|'}'
newline|'\n'
name|'handle'
op|','
name|'tempf'
op|'='
name|'tempfile'
op|'.'
name|'mkstemp'
op|'('
name|'dir'
op|'='
string|"'/tmp'"
op|')'
newline|'\n'
nl|'\n'
name|'ignore'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
newline|'\n'
name|'mockobj'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'image_service'
op|','
string|"'_conn'"
op|','
name|'mockobj'
op|')'
newline|'\n'
name|'mockobj'
op|'('
name|'ignore'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'mockobj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'mockobj'
op|','
string|"'get_bucket'"
op|','
name|'mockobj'
op|')'
newline|'\n'
name|'mockobj'
op|'('
name|'ignore'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'mockobj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'mockobj'
op|','
string|"'get_key'"
op|','
name|'mockobj'
op|')'
newline|'\n'
name|'mockobj'
op|'('
name|'ignore'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'mockobj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'mockobj'
op|','
string|"'get_contents_as_string'"
op|','
name|'mockobj'
op|')'
newline|'\n'
name|'mockobj'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'file_manifest_xml'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'image_service'
op|','
string|"'_download_file'"
op|','
name|'mockobj'
op|')'
newline|'\n'
name|'mockobj'
op|'('
name|'ignore'
op|','
name|'ignore'
op|','
name|'ignore'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'tempf'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'binascii'
op|','
string|"'a2b_hex'"
op|','
name|'mockobj'
op|')'
newline|'\n'
name|'mockobj'
op|'('
name|'ignore'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'foo'"
op|')'
newline|'\n'
name|'mockobj'
op|'('
name|'ignore'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'image_service'
op|','
string|"'_decrypt_image'"
op|','
name|'mockobj'
op|')'
newline|'\n'
name|'mockobj'
op|'('
name|'ignore'
op|','
name|'ignore'
op|','
name|'ignore'
op|','
name|'ignore'
op|','
name|'ignore'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'mockobj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'image_service'
op|','
string|"'_untarzip_image'"
op|','
name|'mockobj'
op|')'
newline|'\n'
name|'mockobj'
op|'('
name|'ignore'
op|','
name|'ignore'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'tempf'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'img'
op|'='
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'_s3_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'metadata'
op|')'
newline|'\n'
name|'eventlet'
op|'.'
name|'sleep'
op|'('
op|')'
newline|'\n'
name|'translated'
op|'='
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'_translate_id_to_uuid'
op|'('
name|'context'
op|','
name|'img'
op|')'
newline|'\n'
name|'uuid'
op|'='
name|'translated'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'image_service'
op|'='
name|'fake'
op|'.'
name|'FakeImageService'
op|'('
op|')'
newline|'\n'
name|'updated_image'
op|'='
name|'image_service'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'uuid'
op|','
nl|'\n'
op|'{'
string|"'is_public'"
op|':'
name|'True'
op|'}'
op|','
name|'None'
op|','
nl|'\n'
op|'{'
string|"'x-glance-registry-purge-props'"
op|':'
name|'False'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'updated_image'
op|'['
string|"'is_public'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'updated_image'
op|'['
string|"'status'"
op|']'
op|','
string|"'active'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'updated_image'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'image_state'"
op|']'
op|','
nl|'\n'
string|"'available'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_s3_malicious_tarballs
dedent|''
name|'def'
name|'test_s3_malicious_tarballs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'_test_for_malicious_tarball'
op|','
nl|'\n'
string|'"/unused"'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
string|"'abs.tar.gz'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'_test_for_malicious_tarball'
op|','
nl|'\n'
string|'"/unused"'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
string|"'rel.tar.gz'"
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
