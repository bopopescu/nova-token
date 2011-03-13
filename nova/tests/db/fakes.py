begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack, LLC'
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
string|'"""Stubouts, mocks and fixtures for the test suite"""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
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
nl|'\n'
nl|'\n'
DECL|function|stub_out_db_instance_api
name|'def'
name|'stub_out_db_instance_api'
op|'('
name|'stubs'
op|','
name|'injected'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Stubs out the db API for creating Instances """'
newline|'\n'
nl|'\n'
name|'INSTANCE_TYPES'
op|'='
op|'{'
nl|'\n'
string|"'m1.tiny'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'512'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'0'
op|','
name|'flavorid'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
string|"'m1.small'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'2048'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'20'
op|','
name|'flavorid'
op|'='
number|'2'
op|')'
op|','
nl|'\n'
string|"'m1.medium'"
op|':'
nl|'\n'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'4096'
op|','
name|'vcpus'
op|'='
number|'2'
op|','
name|'local_gb'
op|'='
number|'40'
op|','
name|'flavorid'
op|'='
number|'3'
op|')'
op|','
nl|'\n'
string|"'m1.large'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'8192'
op|','
name|'vcpus'
op|'='
number|'4'
op|','
name|'local_gb'
op|'='
number|'80'
op|','
name|'flavorid'
op|'='
number|'4'
op|')'
op|','
nl|'\n'
string|"'m1.xlarge'"
op|':'
nl|'\n'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'16384'
op|','
name|'vcpus'
op|'='
number|'8'
op|','
name|'local_gb'
op|'='
number|'160'
op|','
name|'flavorid'
op|'='
number|'5'
op|')'
op|'}'
newline|'\n'
nl|'\n'
name|'network_fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
string|"'test'"
op|','
nl|'\n'
string|"'bridge'"
op|':'
string|"'xenbr0'"
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'test_network'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'10.0.0.1'"
op|','
nl|'\n'
string|"'broadcast'"
op|':'
string|"'10.0.0.255'"
op|','
nl|'\n'
string|"'dns'"
op|':'
string|"'10.0.0.2'"
op|','
nl|'\n'
string|"'ra_server'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'injected'"
op|':'
name|'injected'
op|'}'
newline|'\n'
nl|'\n'
name|'fixed_ip_fields'
op|'='
op|'{'
nl|'\n'
string|"'address'"
op|':'
string|"'10.0.0.3'"
op|','
nl|'\n'
string|"'addressV6'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'netmaskV6'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'gatewayV6'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'network_id'"
op|':'
string|"'test'"
op|'}'
newline|'\n'
nl|'\n'
DECL|class|FakeModel
name|'class'
name|'FakeModel'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Stubs out for model """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'values'
op|'='
name|'values'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'values'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'in'
name|'self'
op|'.'
name|'values'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'values'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_type_get_all
dedent|''
dedent|''
dedent|''
name|'def'
name|'fake_instance_type_get_all'
op|'('
name|'context'
op|','
name|'inactive'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'INSTANCE_TYPES'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_type_get_by_name
dedent|''
name|'def'
name|'fake_instance_type_get_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'INSTANCE_TYPES'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_network_get_by_instance
dedent|''
name|'def'
name|'fake_network_get_by_instance'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FakeModel'
op|'('
name|'network_fields'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_network_get_all_by_instance
dedent|''
name|'def'
name|'fake_network_get_all_by_instance'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'l'
op|'='
op|'['
op|']'
newline|'\n'
name|'l'
op|'.'
name|'append'
op|'('
name|'FakeModel'
op|'('
name|'network_fields'
op|')'
op|')'
newline|'\n'
name|'return'
name|'l'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_get_fixed_address
dedent|''
name|'def'
name|'fake_instance_get_fixed_address'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FakeModel'
op|'('
name|'fixed_ip_fields'
op|')'
op|'.'
name|'address'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_get_all_by_instance
dedent|''
name|'def'
name|'fake_fixed_ip_get_all_by_instance'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'l'
op|'='
op|'['
op|']'
newline|'\n'
name|'l'
op|'.'
name|'append'
op|'('
name|'FakeModel'
op|'('
name|'fixed_ip_fields'
op|')'
op|')'
newline|'\n'
name|'return'
name|'l'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'network_get_by_instance'"
op|','
name|'fake_network_get_by_instance'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_type_get_all'"
op|','
name|'fake_instance_type_get_all'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_type_get_by_name'"
op|','
name|'fake_instance_type_get_by_name'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_fixed_address'"
op|','
nl|'\n'
name|'fake_instance_get_fixed_address'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'network_get_all_by_instance'"
op|','
nl|'\n'
name|'fake_network_get_all_by_instance'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'fixed_ip_get_all_by_instance'"
op|','
nl|'\n'
name|'fake_fixed_ip_get_all_by_instance'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
