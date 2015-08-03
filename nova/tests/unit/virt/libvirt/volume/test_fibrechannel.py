begin_unit
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
name|'platform'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'os_brick'
op|'.'
name|'initiator'
name|'import'
name|'connector'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'arch'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
name|'import'
name|'test_volume'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
name|'import'
name|'fibrechannel'
newline|'\n'
nl|'\n'
nl|'\n'
name|'class'
name|'LibvirtFibreChannelVolumeDriverTestCase'
op|'('
nl|'\n'
DECL|class|LibvirtFibreChannelVolumeDriverTestCase
name|'test_volume'
op|'.'
name|'LibvirtVolumeBaseTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_fibrechan_driver
indent|'    '
name|'def'
name|'test_libvirt_fibrechan_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'fibrechannel'
op|'.'
name|'LibvirtFibreChannelVolumeDriver'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'libvirt_driver'
op|'.'
name|'connector'
op|','
nl|'\n'
name|'connector'
op|'.'
name|'FibreChannelConnector'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_libvirt_fibrechan_driver_s390
dedent|''
name|'def'
name|'_test_libvirt_fibrechan_driver_s390'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'fibrechannel'
op|'.'
name|'LibvirtFibreChannelVolumeDriver'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'libvirt_driver'
op|'.'
name|'connector'
op|','
nl|'\n'
name|'connector'
op|'.'
name|'FibreChannelConnectorS390X'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'platform'
op|','
string|"'machine'"
op|','
name|'return_value'
op|'='
name|'arch'
op|'.'
name|'S390'
op|')'
newline|'\n'
DECL|member|test_libvirt_fibrechan_driver_s390
name|'def'
name|'test_libvirt_fibrechan_driver_s390'
op|'('
name|'self'
op|','
name|'mock_machine'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_libvirt_fibrechan_driver_s390'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'platform'
op|','
string|"'machine'"
op|','
name|'return_value'
op|'='
name|'arch'
op|'.'
name|'S390X'
op|')'
newline|'\n'
DECL|member|test_libvirt_fibrechan_driver_s390x
name|'def'
name|'test_libvirt_fibrechan_driver_s390x'
op|'('
name|'self'
op|','
name|'mock_machine'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_libvirt_fibrechan_driver_s390'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
