begin_unit
comment|'#    Copyright 2010 OpenStack Foundation'
nl|'\n'
comment|'#    Copyright 2012 University Of Minho'
nl|'\n'
comment|'#    Copyright 2014-2015 Red Hat, Inc'
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
name|'mock'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'encodeutils'
newline|'\n'
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
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'fakelibvirt'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'guest'
name|'as'
name|'libvirt_guest'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'host'
newline|'\n'
nl|'\n'
nl|'\n'
name|'host'
op|'.'
name|'libvirt'
op|'='
name|'fakelibvirt'
newline|'\n'
name|'libvirt_guest'
op|'.'
name|'libvirt'
op|'='
name|'fakelibvirt'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GuestTestCase
name|'class'
name|'GuestTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'GuestTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fakelibvirt'
op|'.'
name|'FakeLibvirtFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
name|'host'
op|'.'
name|'Host'
op|'('
string|'"qemu:///system"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_repr
dedent|''
name|'def'
name|'test_repr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'domain'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'spec'
op|'='
name|'fakelibvirt'
op|'.'
name|'virDomain'
op|')'
newline|'\n'
name|'domain'
op|'.'
name|'ID'
op|'.'
name|'return_value'
op|'='
number|'99'
newline|'\n'
name|'domain'
op|'.'
name|'UUIDString'
op|'.'
name|'return_value'
op|'='
string|'"UUID"'
newline|'\n'
name|'domain'
op|'.'
name|'name'
op|'.'
name|'return_value'
op|'='
string|'"foo"'
newline|'\n'
nl|'\n'
name|'guest'
op|'='
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'('
name|'domain'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"<Guest 99 foo UUID>"'
op|','
name|'repr'
op|'('
name|'guest'
op|')'
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
name|'fakelibvirt'
op|'.'
name|'Connection'
op|','
string|"'defineXML'"
op|')'
newline|'\n'
DECL|member|test_create
name|'def'
name|'test_create'
op|'('
name|'self'
op|','
name|'mock_define'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'.'
name|'create'
op|'('
string|'"xml"'
op|','
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'mock_define'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"xml"'
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
name|'fakelibvirt'
op|'.'
name|'Connection'
op|','
string|"'defineXML'"
op|')'
newline|'\n'
DECL|member|test_create_exception
name|'def'
name|'test_create_exception'
op|'('
name|'self'
op|','
name|'mock_define'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_define'
op|'.'
name|'side_effect'
op|'='
name|'test'
op|'.'
name|'TestingException'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'test'
op|'.'
name|'TestingException'
op|','
nl|'\n'
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'.'
name|'create'
op|','
nl|'\n'
string|'"foo"'
op|','
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_launch
dedent|''
name|'def'
name|'test_launch'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'domain'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'spec'
op|'='
name|'fakelibvirt'
op|'.'
name|'virDomain'
op|')'
newline|'\n'
nl|'\n'
name|'guest'
op|'='
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'('
name|'domain'
op|')'
newline|'\n'
name|'guest'
op|'.'
name|'launch'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'domain'
op|'.'
name|'createWithFlags'
op|'.'
name|'assert_called_once_with'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_launch_and_pause
dedent|''
name|'def'
name|'test_launch_and_pause'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'domain'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'spec'
op|'='
name|'fakelibvirt'
op|'.'
name|'virDomain'
op|')'
newline|'\n'
nl|'\n'
name|'guest'
op|'='
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'('
name|'domain'
op|')'
newline|'\n'
name|'guest'
op|'.'
name|'launch'
op|'('
name|'pause'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'domain'
op|'.'
name|'createWithFlags'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'fakelibvirt'
op|'.'
name|'VIR_DOMAIN_START_PAUSED'
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
name|'encodeutils'
op|','
string|"'safe_decode'"
op|')'
newline|'\n'
DECL|member|test_launch_exception
name|'def'
name|'test_launch_exception'
op|'('
name|'self'
op|','
name|'mock_safe_decode'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'domain'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'spec'
op|'='
name|'fakelibvirt'
op|'.'
name|'virDomain'
op|')'
newline|'\n'
name|'domain'
op|'.'
name|'createWithFlags'
op|'.'
name|'side_effect'
op|'='
name|'test'
op|'.'
name|'TestingException'
newline|'\n'
name|'mock_safe_decode'
op|'.'
name|'return_value'
op|'='
string|'"</xml>"'
newline|'\n'
nl|'\n'
name|'guest'
op|'='
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'('
name|'domain'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'test'
op|'.'
name|'TestingException'
op|','
name|'guest'
op|'.'
name|'launch'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'mock_safe_decode'
op|'.'
name|'called'
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
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'libvirt_guest'
op|'.'
name|'Guest'
op|','
string|"'get_interfaces'"
op|')'
newline|'\n'
DECL|member|test_enable_hairpin
name|'def'
name|'test_enable_hairpin'
op|'('
name|'self'
op|','
name|'mock_get_interfaces'
op|','
name|'mock_execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_interfaces'
op|'.'
name|'return_value'
op|'='
op|'['
string|'"vnet0"'
op|','
string|'"vnet1"'
op|']'
newline|'\n'
nl|'\n'
name|'guest'
op|'='
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'('
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
op|')'
newline|'\n'
name|'guest'
op|'.'
name|'enable_hairpin'
op|'('
op|')'
newline|'\n'
name|'mock_execute'
op|'.'
name|'assert_has_calls'
op|'('
op|'['
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
nl|'\n'
string|"'tee'"
op|','
string|"'/sys/class/net/vnet0/brport/hairpin_mode'"
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
name|'process_input'
op|'='
string|"'1'"
op|','
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|','
number|'1'
op|']'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
nl|'\n'
string|"'tee'"
op|','
string|"'/sys/class/net/vnet1/brport/hairpin_mode'"
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
name|'process_input'
op|'='
string|"'1'"
op|','
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|','
number|'1'
op|']'
op|')'
op|']'
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
name|'encodeutils'
op|','
string|"'safe_decode'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'libvirt_guest'
op|'.'
name|'Guest'
op|','
string|"'get_interfaces'"
op|')'
newline|'\n'
DECL|member|test_enable_hairpin_exception
name|'def'
name|'test_enable_hairpin_exception'
op|'('
name|'self'
op|','
name|'mock_get_interfaces'
op|','
nl|'\n'
name|'mock_execute'
op|','
name|'mock_safe_decode'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_interfaces'
op|'.'
name|'return_value'
op|'='
op|'['
string|'"foo"'
op|']'
newline|'\n'
name|'mock_execute'
op|'.'
name|'side_effect'
op|'='
name|'test'
op|'.'
name|'TestingException'
op|'('
string|"'oops'"
op|')'
newline|'\n'
nl|'\n'
name|'guest'
op|'='
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'('
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'test'
op|'.'
name|'TestingException'
op|','
name|'guest'
op|'.'
name|'enable_hairpin'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'mock_safe_decode'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_interfaces
dedent|''
name|'def'
name|'test_get_interfaces'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dom'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'spec'
op|'='
name|'fakelibvirt'
op|'.'
name|'virDomain'
op|')'
newline|'\n'
name|'dom'
op|'.'
name|'XMLDesc'
op|'.'
name|'return_value'
op|'='
string|'"""\n<domain>\n  <devices>\n    <interface type="network">\n      <target dev="vnet0"/>\n    </interface>\n    <interface type="network">\n      <target dev="vnet1"/>\n    </interface>\n  </devices>\n</domain>"""'
newline|'\n'
name|'guest'
op|'='
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'('
name|'dom'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|'"vnet0"'
op|','
string|'"vnet1"'
op|']'
op|','
name|'guest'
op|'.'
name|'get_interfaces'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_interfaces_exception
dedent|''
name|'def'
name|'test_get_interfaces_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dom'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'spec'
op|'='
name|'fakelibvirt'
op|'.'
name|'virDomain'
op|')'
newline|'\n'
name|'dom'
op|'.'
name|'XMLDesc'
op|'.'
name|'return_value'
op|'='
string|'"<bad xml>"'
newline|'\n'
name|'guest'
op|'='
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'('
name|'dom'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'guest'
op|'.'
name|'get_interfaces'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_poweroff
dedent|''
name|'def'
name|'test_poweroff'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'domain'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'spec'
op|'='
name|'fakelibvirt'
op|'.'
name|'virDomain'
op|')'
newline|'\n'
nl|'\n'
name|'guest'
op|'='
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'('
name|'domain'
op|')'
newline|'\n'
name|'guest'
op|'.'
name|'poweroff'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'domain'
op|'.'
name|'destroy'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_resume
dedent|''
name|'def'
name|'test_resume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'domain'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'spec'
op|'='
name|'fakelibvirt'
op|'.'
name|'virDomain'
op|')'
newline|'\n'
nl|'\n'
name|'guest'
op|'='
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'('
name|'domain'
op|')'
newline|'\n'
name|'guest'
op|'.'
name|'resume'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'domain'
op|'.'
name|'resume'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vcpus_info
dedent|''
name|'def'
name|'test_get_vcpus_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'domain'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'spec'
op|'='
name|'fakelibvirt'
op|'.'
name|'virDomain'
op|')'
newline|'\n'
name|'domain'
op|'.'
name|'vcpus'
op|'.'
name|'return_value'
op|'='
op|'('
op|'['
op|'('
number|'0'
op|','
number|'1'
op|','
number|'10290000000L'
op|','
number|'2'
op|')'
op|']'
op|','
nl|'\n'
op|'['
op|'('
name|'True'
op|','
name|'True'
op|')'
op|']'
op|')'
newline|'\n'
name|'guest'
op|'='
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'('
name|'domain'
op|')'
newline|'\n'
name|'vcpus'
op|'='
name|'list'
op|'('
name|'guest'
op|'.'
name|'get_vcpus_info'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'vcpus'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'vcpus'
op|'['
number|'0'
op|']'
op|'.'
name|'cpu'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'vcpus'
op|'['
number|'0'
op|']'
op|'.'
name|'state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'10290000000L'
op|','
name|'vcpus'
op|'['
number|'0'
op|']'
op|'.'
name|'time'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_configuration
dedent|''
name|'def'
name|'test_delete_configuration'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'domain'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'spec'
op|'='
name|'fakelibvirt'
op|'.'
name|'virDomain'
op|')'
newline|'\n'
nl|'\n'
name|'guest'
op|'='
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'('
name|'domain'
op|')'
newline|'\n'
name|'guest'
op|'.'
name|'delete_configuration'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'domain'
op|'.'
name|'undefineFlags'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'fakelibvirt'
op|'.'
name|'VIR_DOMAIN_UNDEFINE_MANAGED_SAVE'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_configuration_exception
dedent|''
name|'def'
name|'test_delete_configuration_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'domain'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'spec'
op|'='
name|'fakelibvirt'
op|'.'
name|'virDomain'
op|')'
newline|'\n'
name|'domain'
op|'.'
name|'undefineFlags'
op|'.'
name|'side_effect'
op|'='
name|'fakelibvirt'
op|'.'
name|'libvirtError'
op|'('
string|"'oops'"
op|')'
newline|'\n'
name|'domain'
op|'.'
name|'ID'
op|'.'
name|'return_value'
op|'='
number|'1'
newline|'\n'
nl|'\n'
name|'guest'
op|'='
name|'libvirt_guest'
op|'.'
name|'Guest'
op|'('
name|'domain'
op|')'
newline|'\n'
name|'guest'
op|'.'
name|'delete_configuration'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'domain'
op|'.'
name|'undefine'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
