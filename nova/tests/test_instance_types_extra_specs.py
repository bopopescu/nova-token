begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 University of Southern California'
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
string|'"""\nUnit Tests for instance types extra specs code\n"""'
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
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'session'
name|'import'
name|'get_session'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'models'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceTypeExtraSpecsTestCase
name|'class'
name|'InstanceTypeExtraSpecsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'InstanceTypeExtraSpecsTestCase'
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
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'values'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"cg1.4xlarge"'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'22000'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'8'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'1690'
op|','
nl|'\n'
name|'flavorid'
op|'='
number|'105'
op|')'
newline|'\n'
name|'specs'
op|'='
name|'dict'
op|'('
name|'cpu_arch'
op|'='
string|'"x86_64"'
op|','
nl|'\n'
name|'cpu_model'
op|'='
string|'"Nehalem"'
op|','
nl|'\n'
name|'xpu_arch'
op|'='
string|'"fermi"'
op|','
nl|'\n'
name|'xpus'
op|'='
number|'2'
op|','
nl|'\n'
name|'xpu_model'
op|'='
string|'"Tesla 2050"'
op|')'
newline|'\n'
name|'values'
op|'['
string|"'extra_specs'"
op|']'
op|'='
name|'specs'
newline|'\n'
name|'ref'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance_type_id'
op|'='
name|'ref'
op|'.'
name|'id'
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
comment|'# Remove the instance type from the database'
nl|'\n'
indent|'        '
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_purge'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
string|'"cg1.4xlarge"'
op|')'
newline|'\n'
name|'super'
op|'('
name|'InstanceTypeExtraSpecsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_type_specs_get
dedent|''
name|'def'
name|'test_instance_type_specs_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_specs'
op|'='
name|'dict'
op|'('
name|'cpu_arch'
op|'='
string|'"x86_64"'
op|','
nl|'\n'
name|'cpu_model'
op|'='
string|'"Nehalem"'
op|','
nl|'\n'
name|'xpu_arch'
op|'='
string|'"fermi"'
op|','
nl|'\n'
name|'xpus'
op|'='
string|'"2"'
op|','
nl|'\n'
name|'xpu_model'
op|'='
string|'"Tesla 2050"'
op|')'
newline|'\n'
name|'actual_specs'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_extra_specs_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_type_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'expected_specs'
op|','
name|'actual_specs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_type_extra_specs_delete
dedent|''
name|'def'
name|'test_instance_type_extra_specs_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_specs'
op|'='
name|'dict'
op|'('
name|'cpu_arch'
op|'='
string|'"x86_64"'
op|','
nl|'\n'
name|'cpu_model'
op|'='
string|'"Nehalem"'
op|','
nl|'\n'
name|'xpu_arch'
op|'='
string|'"fermi"'
op|','
nl|'\n'
name|'xpus'
op|'='
string|'"2"'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_extra_specs_delete'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_type_id'
op|','
nl|'\n'
string|'"xpu_model"'
op|')'
newline|'\n'
name|'actual_specs'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_extra_specs_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_type_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'expected_specs'
op|','
name|'actual_specs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_type_extra_specs_update
dedent|''
name|'def'
name|'test_instance_type_extra_specs_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_specs'
op|'='
name|'dict'
op|'('
name|'cpu_arch'
op|'='
string|'"x86_64"'
op|','
nl|'\n'
name|'cpu_model'
op|'='
string|'"Sandy Bridge"'
op|','
nl|'\n'
name|'xpu_arch'
op|'='
string|'"fermi"'
op|','
nl|'\n'
name|'xpus'
op|'='
string|'"2"'
op|','
nl|'\n'
name|'xpu_model'
op|'='
string|'"Tesla 2050"'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_extra_specs_update_or_create'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_type_id'
op|','
nl|'\n'
name|'dict'
op|'('
name|'cpu_model'
op|'='
string|'"Sandy Bridge"'
op|')'
op|')'
newline|'\n'
name|'actual_specs'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_extra_specs_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_type_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'expected_specs'
op|','
name|'actual_specs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_type_extra_specs_create
dedent|''
name|'def'
name|'test_instance_type_extra_specs_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_specs'
op|'='
name|'dict'
op|'('
name|'cpu_arch'
op|'='
string|'"x86_64"'
op|','
nl|'\n'
name|'cpu_model'
op|'='
string|'"Nehalem"'
op|','
nl|'\n'
name|'xpu_arch'
op|'='
string|'"fermi"'
op|','
nl|'\n'
name|'xpus'
op|'='
string|'"2"'
op|','
nl|'\n'
name|'xpu_model'
op|'='
string|'"Tesla 2050"'
op|','
nl|'\n'
name|'net_arch'
op|'='
string|'"ethernet"'
op|','
nl|'\n'
name|'net_mbps'
op|'='
string|'"10000"'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_extra_specs_update_or_create'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_type_id'
op|','
nl|'\n'
name|'dict'
op|'('
name|'net_arch'
op|'='
string|'"ethernet"'
op|','
nl|'\n'
name|'net_mbps'
op|'='
number|'10000'
op|')'
op|')'
newline|'\n'
name|'actual_specs'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_extra_specs_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_type_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'expected_specs'
op|','
name|'actual_specs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_type_get_by_id_with_extra_specs
dedent|''
name|'def'
name|'test_instance_type_get_by_id_with_extra_specs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_type'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_get_by_id'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_type_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'instance_type'
op|'['
string|"'extra_specs'"
op|']'
op|','
nl|'\n'
name|'dict'
op|'('
name|'cpu_arch'
op|'='
string|'"x86_64"'
op|','
nl|'\n'
name|'cpu_model'
op|'='
string|'"Nehalem"'
op|','
nl|'\n'
name|'xpu_arch'
op|'='
string|'"fermi"'
op|','
nl|'\n'
name|'xpus'
op|'='
string|'"2"'
op|','
nl|'\n'
name|'xpu_model'
op|'='
string|'"Tesla 2050"'
op|')'
op|')'
newline|'\n'
name|'instance_type'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_get_by_id'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
number|'5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'instance_type'
op|'['
string|"'extra_specs'"
op|']'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_type_get_by_name_with_extra_specs
dedent|''
name|'def'
name|'test_instance_type_get_by_name_with_extra_specs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_type'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_get_by_name'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
string|'"cg1.4xlarge"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'instance_type'
op|'['
string|"'extra_specs'"
op|']'
op|','
nl|'\n'
name|'dict'
op|'('
name|'cpu_arch'
op|'='
string|'"x86_64"'
op|','
nl|'\n'
name|'cpu_model'
op|'='
string|'"Nehalem"'
op|','
nl|'\n'
name|'xpu_arch'
op|'='
string|'"fermi"'
op|','
nl|'\n'
name|'xpus'
op|'='
string|'"2"'
op|','
nl|'\n'
name|'xpu_model'
op|'='
string|'"Tesla 2050"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'instance_type'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_get_by_name'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
string|'"m1.small"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'instance_type'
op|'['
string|"'extra_specs'"
op|']'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_type_get_by_id_with_extra_specs
dedent|''
name|'def'
name|'test_instance_type_get_by_id_with_extra_specs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_type'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_get_by_flavor_id'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
number|'105'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'instance_type'
op|'['
string|"'extra_specs'"
op|']'
op|','
nl|'\n'
name|'dict'
op|'('
name|'cpu_arch'
op|'='
string|'"x86_64"'
op|','
nl|'\n'
name|'cpu_model'
op|'='
string|'"Nehalem"'
op|','
nl|'\n'
name|'xpu_arch'
op|'='
string|'"fermi"'
op|','
nl|'\n'
name|'xpus'
op|'='
string|'"2"'
op|','
nl|'\n'
name|'xpu_model'
op|'='
string|'"Tesla 2050"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'instance_type'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_get_by_flavor_id'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'instance_type'
op|'['
string|"'extra_specs'"
op|']'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_type_get_all
dedent|''
name|'def'
name|'test_instance_type_get_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'specs'
op|'='
name|'dict'
op|'('
name|'cpu_arch'
op|'='
string|'"x86_64"'
op|','
nl|'\n'
name|'cpu_model'
op|'='
string|'"Nehalem"'
op|','
nl|'\n'
name|'xpu_arch'
op|'='
string|'"fermi"'
op|','
nl|'\n'
name|'xpus'
op|'='
string|"'2'"
op|','
nl|'\n'
name|'xpu_model'
op|'='
string|'"Tesla 2050"'
op|')'
newline|'\n'
nl|'\n'
name|'types'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_get_all'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'types'
op|'['
string|"'cg1.4xlarge'"
op|']'
op|'['
string|"'extra_specs'"
op|']'
op|','
name|'specs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'types'
op|'['
string|"'m1.small'"
op|']'
op|'['
string|"'extra_specs'"
op|']'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
