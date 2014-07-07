begin_unit
comment|'# Copyright 2014 Red Hat, Inc.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'hardware'
name|'as'
name|'hw'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeFlavor
name|'class'
name|'FakeFlavor'
op|'('
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'vcpus'
op|','
name|'extra_specs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'vcpus'
op|'='
name|'vcpus'
newline|'\n'
name|'self'
op|'.'
name|'extra_specs'
op|'='
name|'extra_specs'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CpuSetTestCase
dedent|''
dedent|''
name|'class'
name|'CpuSetTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_vcpu_pin_set
indent|'    '
name|'def'
name|'test_get_vcpu_pin_set'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'vcpu_pin_set'
op|'='
string|'"1-3,5,^2"'
op|')'
newline|'\n'
name|'cpuset_ids'
op|'='
name|'hw'
op|'.'
name|'get_vcpu_pin_set'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
number|'1'
op|','
number|'3'
op|','
number|'5'
op|']'
op|','
name|'cpuset_ids'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_parse_cpu_spec_none_returns_none
dedent|''
name|'def'
name|'test_parse_cpu_spec_none_returns_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'vcpu_pin_set'
op|'='
name|'None'
op|')'
newline|'\n'
name|'cpuset_ids'
op|'='
name|'hw'
op|'.'
name|'get_vcpu_pin_set'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'cpuset_ids'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_parse_cpu_spec_valid_syntax_works
dedent|''
name|'def'
name|'test_parse_cpu_spec_valid_syntax_works'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cpuset_ids'
op|'='
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|'('
string|'"1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|']'
op|')'
op|','
name|'cpuset_ids'
op|')'
newline|'\n'
nl|'\n'
name|'cpuset_ids'
op|'='
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|'('
string|'"1,2"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'cpuset_ids'
op|')'
newline|'\n'
nl|'\n'
name|'cpuset_ids'
op|'='
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|'('
string|'", ,   1 ,  ,,  2,    ,"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'cpuset_ids'
op|')'
newline|'\n'
nl|'\n'
name|'cpuset_ids'
op|'='
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|'('
string|'"1-1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|']'
op|')'
op|','
name|'cpuset_ids'
op|')'
newline|'\n'
nl|'\n'
name|'cpuset_ids'
op|'='
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|'('
string|'" 1 - 1, 1 - 2 , 1 -3"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|')'
op|','
name|'cpuset_ids'
op|')'
newline|'\n'
nl|'\n'
name|'cpuset_ids'
op|'='
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|'('
string|'"1,^2"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|']'
op|')'
op|','
name|'cpuset_ids'
op|')'
newline|'\n'
nl|'\n'
name|'cpuset_ids'
op|'='
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|'('
string|'"1-2, ^1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'2'
op|']'
op|')'
op|','
name|'cpuset_ids'
op|')'
newline|'\n'
nl|'\n'
name|'cpuset_ids'
op|'='
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|'('
string|'"1-3,5,^2"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'3'
op|','
number|'5'
op|']'
op|')'
op|','
name|'cpuset_ids'
op|')'
newline|'\n'
nl|'\n'
name|'cpuset_ids'
op|'='
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|'('
string|'" 1 -    3        ,   ^2,        5"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'3'
op|','
number|'5'
op|']'
op|')'
op|','
name|'cpuset_ids'
op|')'
newline|'\n'
nl|'\n'
name|'cpuset_ids'
op|'='
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|'('
string|'" 1,1, ^1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
op|']'
op|')'
op|','
name|'cpuset_ids'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_parse_cpu_spec_invalid_syntax_raises
dedent|''
name|'def'
name|'test_parse_cpu_spec_invalid_syntax_raises'
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
name|'Invalid'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|','
nl|'\n'
string|'" -1-3,5,^2"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|','
nl|'\n'
string|'"1-3-,5,^2"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|','
nl|'\n'
string|'"-3,5,^2"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|','
nl|'\n'
string|'"1-,5,^2"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|','
nl|'\n'
string|'"1-3,5,^2^"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|','
nl|'\n'
string|'"1-3,5,^2-"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|','
nl|'\n'
string|'"--13,^^5,^2"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|','
nl|'\n'
string|'"a-3,5,^2"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|','
nl|'\n'
string|'"1-a,5,^2"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|','
nl|'\n'
string|'"1-3,b,^2"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|','
nl|'\n'
string|'"1-3,5,^c"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'parse_cpu_spec'
op|','
nl|'\n'
string|'"3 - 1, 5 , ^ 2 "'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VCPUTopologyTest
dedent|''
dedent|''
name|'class'
name|'VCPUTopologyTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_validate_config
indent|'    '
name|'def'
name|'test_validate_config'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'testdata'
op|'='
op|'['
nl|'\n'
op|'{'
comment|'# Flavor sets preferred topology only'
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_sockets"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_cores"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"hw:cpu_threads"'
op|':'
string|'"1"'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'('
nl|'\n'
number|'8'
op|','
number|'2'
op|','
number|'1'
op|','
number|'65536'
op|','
number|'65536'
op|','
number|'65536'
nl|'\n'
op|')'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Image topology overrides flavor'
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_sockets"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_cores"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"hw:cpu_threads"'
op|':'
string|'"1"'
op|','
nl|'\n'
string|'"hw:cpu_max_threads"'
op|':'
string|'"2"'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
nl|'\n'
string|'"hw_cpu_sockets"'
op|':'
string|'"4"'
op|','
nl|'\n'
string|'"hw_cpu_cores"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"hw_cpu_threads"'
op|':'
string|'"2"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'('
nl|'\n'
number|'4'
op|','
number|'2'
op|','
number|'2'
op|','
number|'65536'
op|','
number|'65536'
op|','
number|'2'
op|','
nl|'\n'
op|')'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Partial image topology overrides flavor'
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_sockets"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_cores"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"hw:cpu_threads"'
op|':'
string|'"1"'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
nl|'\n'
string|'"hw_cpu_sockets"'
op|':'
string|'"2"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'('
nl|'\n'
number|'2'
op|','
op|'-'
number|'1'
op|','
op|'-'
number|'1'
op|','
number|'65536'
op|','
number|'65536'
op|','
number|'65536'
op|','
nl|'\n'
op|')'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Restrict use of threads'
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_max_threads"'
op|':'
string|'"2"'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
nl|'\n'
string|'"hw_cpu_max_threads"'
op|':'
string|'"1"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'('
nl|'\n'
op|'-'
number|'1'
op|','
op|'-'
number|'1'
op|','
op|'-'
number|'1'
op|','
number|'65536'
op|','
number|'65536'
op|','
number|'1'
op|','
nl|'\n'
op|')'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Force use of at least two sockets'
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_max_cores"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_max_threads"'
op|':'
string|'"1"'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'('
nl|'\n'
op|'-'
number|'1'
op|','
op|'-'
number|'1'
op|','
op|'-'
number|'1'
op|','
number|'65536'
op|','
number|'8'
op|','
number|'1'
nl|'\n'
op|')'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Image limits reduce flavor'
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_max_cores"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_max_threads"'
op|':'
string|'"1"'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
nl|'\n'
string|'"hw_cpu_max_cores"'
op|':'
string|'"4"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'('
nl|'\n'
op|'-'
number|'1'
op|','
op|'-'
number|'1'
op|','
op|'-'
number|'1'
op|','
number|'65536'
op|','
number|'4'
op|','
number|'1'
nl|'\n'
op|')'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Image limits kill flavor preferred'
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_sockets"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"hw:cpu_cores"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_threads"'
op|':'
string|'"1"'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
nl|'\n'
string|'"hw_cpu_max_cores"'
op|':'
string|'"4"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'('
nl|'\n'
op|'-'
number|'1'
op|','
op|'-'
number|'1'
op|','
op|'-'
number|'1'
op|','
number|'65536'
op|','
number|'4'
op|','
number|'65536'
nl|'\n'
op|')'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Image limits cannot exceed flavor'
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_max_cores"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_max_threads"'
op|':'
string|'"1"'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
nl|'\n'
string|'"hw_cpu_max_cores"'
op|':'
string|'"16"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
name|'exception'
op|'.'
name|'ImageVCPULimitsRangeExceeded'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Image preferred cannot exceed flavor'
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_max_cores"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_max_threads"'
op|':'
string|'"1"'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
nl|'\n'
string|'"hw_cpu_cores"'
op|':'
string|'"16"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
name|'exception'
op|'.'
name|'ImageVCPUTopologyRangeExceeded'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'test'
name|'in'
name|'testdata'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'type'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|')'
op|'=='
name|'tuple'
op|':'
newline|'\n'
indent|'                '
op|'('
name|'preferred'
op|','
nl|'\n'
name|'maximum'
op|')'
op|'='
name|'hw'
op|'.'
name|'VirtCPUTopology'
op|'.'
name|'get_topology_constraints'
op|'('
nl|'\n'
name|'test'
op|'['
string|'"flavor"'
op|']'
op|','
nl|'\n'
name|'test'
op|'['
string|'"image"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|'['
number|'0'
op|']'
op|','
name|'preferred'
op|'.'
name|'sockets'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|'['
number|'1'
op|']'
op|','
name|'preferred'
op|'.'
name|'cores'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|'['
number|'2'
op|']'
op|','
name|'preferred'
op|'.'
name|'threads'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|'['
number|'3'
op|']'
op|','
name|'maximum'
op|'.'
name|'sockets'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|'['
number|'4'
op|']'
op|','
name|'maximum'
op|'.'
name|'cores'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|'['
number|'5'
op|']'
op|','
name|'maximum'
op|'.'
name|'threads'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'VirtCPUTopology'
op|'.'
name|'get_topology_constraints'
op|','
nl|'\n'
name|'test'
op|'['
string|'"flavor"'
op|']'
op|','
nl|'\n'
name|'test'
op|'['
string|'"image"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_possible_configs
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_possible_configs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'testdata'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxsockets"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxcores"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxthreads"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
nl|'\n'
op|'['
number|'8'
op|','
number|'1'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'['
number|'4'
op|','
number|'2'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'['
number|'2'
op|','
number|'4'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'['
number|'1'
op|','
number|'8'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'['
number|'4'
op|','
number|'1'
op|','
number|'2'
op|']'
op|','
nl|'\n'
op|'['
number|'2'
op|','
number|'2'
op|','
number|'2'
op|']'
op|','
nl|'\n'
op|'['
number|'1'
op|','
number|'4'
op|','
number|'2'
op|']'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'False'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxsockets"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxcores"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxthreads"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
nl|'\n'
op|'['
number|'8'
op|','
number|'1'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'['
number|'4'
op|','
number|'2'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'['
number|'2'
op|','
number|'4'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'['
number|'1'
op|','
number|'8'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxsockets"'
op|':'
number|'1024'
op|','
nl|'\n'
string|'"maxcores"'
op|':'
number|'1024'
op|','
nl|'\n'
string|'"maxthreads"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
nl|'\n'
op|'['
number|'8'
op|','
number|'1'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'['
number|'4'
op|','
number|'2'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'['
number|'2'
op|','
number|'4'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'['
number|'1'
op|','
number|'8'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'['
number|'4'
op|','
number|'1'
op|','
number|'2'
op|']'
op|','
nl|'\n'
op|'['
number|'2'
op|','
number|'2'
op|','
number|'2'
op|']'
op|','
nl|'\n'
op|'['
number|'1'
op|','
number|'4'
op|','
number|'2'
op|']'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxsockets"'
op|':'
number|'1024'
op|','
nl|'\n'
string|'"maxcores"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"maxthreads"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
nl|'\n'
op|'['
number|'8'
op|','
number|'1'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'['
number|'4'
op|','
number|'1'
op|','
number|'2'
op|']'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'7'
op|','
nl|'\n'
string|'"maxsockets"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxcores"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxthreads"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
nl|'\n'
op|'['
number|'7'
op|','
number|'1'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'['
number|'1'
op|','
number|'7'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxsockets"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"maxcores"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"maxthreads"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"expect"'
op|':'
name|'exception'
op|'.'
name|'ImageVCPULimitsRangeImpossible'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'False'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxsockets"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"maxcores"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"maxthreads"'
op|':'
number|'4'
op|','
nl|'\n'
string|'"expect"'
op|':'
name|'exception'
op|'.'
name|'ImageVCPULimitsRangeImpossible'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'test'
name|'in'
name|'testdata'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'type'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|')'
op|'=='
name|'list'
op|':'
newline|'\n'
indent|'                '
name|'actual'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'topology'
name|'in'
name|'hw'
op|'.'
name|'VirtCPUTopology'
op|'.'
name|'get_possible_topologies'
op|'('
nl|'\n'
name|'test'
op|'['
string|'"vcpus"'
op|']'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'VirtCPUTopology'
op|'('
name|'test'
op|'['
string|'"maxsockets"'
op|']'
op|','
nl|'\n'
name|'test'
op|'['
string|'"maxcores"'
op|']'
op|','
nl|'\n'
name|'test'
op|'['
string|'"maxthreads"'
op|']'
op|')'
op|','
nl|'\n'
name|'test'
op|'['
string|'"allow_threads"'
op|']'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'actual'
op|'.'
name|'append'
op|'('
op|'['
name|'topology'
op|'.'
name|'sockets'
op|','
nl|'\n'
name|'topology'
op|'.'
name|'cores'
op|','
nl|'\n'
name|'topology'
op|'.'
name|'threads'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|','
name|'actual'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'VirtCPUTopology'
op|'.'
name|'get_possible_topologies'
op|','
nl|'\n'
name|'test'
op|'['
string|'"vcpus"'
op|']'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'VirtCPUTopology'
op|'('
name|'test'
op|'['
string|'"maxsockets"'
op|']'
op|','
nl|'\n'
name|'test'
op|'['
string|'"maxcores"'
op|']'
op|','
nl|'\n'
name|'test'
op|'['
string|'"maxthreads"'
op|']'
op|')'
op|','
nl|'\n'
name|'test'
op|'['
string|'"allow_threads"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_sorting_configs
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_sorting_configs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'testdata'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxsockets"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxcores"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxthreads"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"sockets"'
op|':'
number|'4'
op|','
nl|'\n'
string|'"cores"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"threads"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
nl|'\n'
op|'['
number|'4'
op|','
number|'2'
op|','
number|'1'
op|']'
op|','
comment|'# score = 2'
nl|'\n'
op|'['
number|'8'
op|','
number|'1'
op|','
number|'1'
op|']'
op|','
comment|'# score = 1'
nl|'\n'
op|'['
number|'2'
op|','
number|'4'
op|','
number|'1'
op|']'
op|','
comment|'# score = 1'
nl|'\n'
op|'['
number|'1'
op|','
number|'8'
op|','
number|'1'
op|']'
op|','
comment|'# score = 1'
nl|'\n'
op|'['
number|'4'
op|','
number|'1'
op|','
number|'2'
op|']'
op|','
comment|'# score = 1'
nl|'\n'
op|'['
number|'2'
op|','
number|'2'
op|','
number|'2'
op|']'
op|','
comment|'# score = 1'
nl|'\n'
op|'['
number|'1'
op|','
number|'4'
op|','
number|'2'
op|']'
op|','
comment|'# score = 1'
nl|'\n'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxsockets"'
op|':'
number|'1024'
op|','
nl|'\n'
string|'"maxcores"'
op|':'
number|'1024'
op|','
nl|'\n'
string|'"maxthreads"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"sockets"'
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
string|'"cores"'
op|':'
number|'4'
op|','
nl|'\n'
string|'"threads"'
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
nl|'\n'
op|'['
number|'2'
op|','
number|'4'
op|','
number|'1'
op|']'
op|','
comment|'# score = 1'
nl|'\n'
op|'['
number|'1'
op|','
number|'4'
op|','
number|'2'
op|']'
op|','
comment|'# score = 1'
nl|'\n'
op|'['
number|'8'
op|','
number|'1'
op|','
number|'1'
op|']'
op|','
comment|'# score = 0'
nl|'\n'
op|'['
number|'4'
op|','
number|'2'
op|','
number|'1'
op|']'
op|','
comment|'# score = 0'
nl|'\n'
op|'['
number|'1'
op|','
number|'8'
op|','
number|'1'
op|']'
op|','
comment|'# score = 0'
nl|'\n'
op|'['
number|'4'
op|','
number|'1'
op|','
number|'2'
op|']'
op|','
comment|'# score = 0'
nl|'\n'
op|'['
number|'2'
op|','
number|'2'
op|','
number|'2'
op|']'
op|','
comment|'# score = 0'
nl|'\n'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxsockets"'
op|':'
number|'1024'
op|','
nl|'\n'
string|'"maxcores"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"maxthreads"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"sockets"'
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
string|'"cores"'
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
string|'"threads"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
nl|'\n'
op|'['
number|'4'
op|','
number|'1'
op|','
number|'2'
op|']'
op|','
comment|'# score = 1'
nl|'\n'
op|'['
number|'8'
op|','
number|'1'
op|','
number|'1'
op|']'
op|','
comment|'# score = 0'
nl|'\n'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'False'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'8'
op|','
nl|'\n'
string|'"maxsockets"'
op|':'
number|'1024'
op|','
nl|'\n'
string|'"maxcores"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"maxthreads"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"sockets"'
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
string|'"cores"'
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
string|'"threads"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
nl|'\n'
op|'['
number|'8'
op|','
number|'1'
op|','
number|'1'
op|']'
op|','
comment|'# score = 0'
nl|'\n'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'test'
name|'in'
name|'testdata'
op|':'
newline|'\n'
indent|'            '
name|'actual'
op|'='
op|'['
op|']'
newline|'\n'
name|'possible'
op|'='
name|'hw'
op|'.'
name|'VirtCPUTopology'
op|'.'
name|'get_possible_topologies'
op|'('
nl|'\n'
name|'test'
op|'['
string|'"vcpus"'
op|']'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'VirtCPUTopology'
op|'('
name|'test'
op|'['
string|'"maxsockets"'
op|']'
op|','
nl|'\n'
name|'test'
op|'['
string|'"maxcores"'
op|']'
op|','
nl|'\n'
name|'test'
op|'['
string|'"maxthreads"'
op|']'
op|')'
op|','
nl|'\n'
name|'test'
op|'['
string|'"allow_threads"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'tops'
op|'='
name|'hw'
op|'.'
name|'VirtCPUTopology'
op|'.'
name|'sort_possible_topologies'
op|'('
nl|'\n'
name|'possible'
op|','
nl|'\n'
name|'hw'
op|'.'
name|'VirtCPUTopology'
op|'('
name|'test'
op|'['
string|'"sockets"'
op|']'
op|','
nl|'\n'
name|'test'
op|'['
string|'"cores"'
op|']'
op|','
nl|'\n'
name|'test'
op|'['
string|'"threads"'
op|']'
op|')'
op|')'
newline|'\n'
name|'for'
name|'topology'
name|'in'
name|'tops'
op|':'
newline|'\n'
indent|'                '
name|'actual'
op|'.'
name|'append'
op|'('
op|'['
name|'topology'
op|'.'
name|'sockets'
op|','
nl|'\n'
name|'topology'
op|'.'
name|'cores'
op|','
nl|'\n'
name|'topology'
op|'.'
name|'threads'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|','
name|'actual'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_best_config
dedent|''
dedent|''
name|'def'
name|'test_best_config'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'testdata'
op|'='
op|'['
nl|'\n'
op|'{'
comment|'# Flavor sets preferred topology only'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_sockets"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_cores"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"hw:cpu_threads"'
op|':'
string|'"1"'
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
number|'8'
op|','
number|'2'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Image topology overrides flavor'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_sockets"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_cores"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"hw:cpu_threads"'
op|':'
string|'"1"'
op|','
nl|'\n'
string|'"hw:cpu_maxthreads"'
op|':'
string|'"2"'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
nl|'\n'
string|'"hw_cpu_sockets"'
op|':'
string|'"4"'
op|','
nl|'\n'
string|'"hw_cpu_cores"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"hw_cpu_threads"'
op|':'
string|'"2"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
number|'4'
op|','
number|'2'
op|','
number|'2'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Image topology overrides flavor'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'False'
op|','
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_sockets"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_cores"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"hw:cpu_threads"'
op|':'
string|'"1"'
op|','
nl|'\n'
string|'"hw:cpu_maxthreads"'
op|':'
string|'"2"'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
nl|'\n'
string|'"hw_cpu_sockets"'
op|':'
string|'"4"'
op|','
nl|'\n'
string|'"hw_cpu_cores"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"hw_cpu_threads"'
op|':'
string|'"2"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
number|'8'
op|','
number|'2'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Partial image topology overrides flavor'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_sockets"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_cores"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"hw:cpu_threads"'
op|':'
string|'"1"'
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
nl|'\n'
string|'"hw_cpu_sockets"'
op|':'
string|'"2"'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
number|'2'
op|','
number|'8'
op|','
number|'1'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Restrict use of threads'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_max_threads"'
op|':'
string|'"1"'
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
number|'16'
op|','
number|'1'
op|','
number|'1'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Force use of at least two sockets'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_max_cores"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_max_threads"'
op|':'
string|'"1"'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
number|'16'
op|','
number|'1'
op|','
number|'1'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Image limits reduce flavor'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_max_sockets"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_max_cores"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_max_threads"'
op|':'
string|'"1"'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
nl|'\n'
string|'"hw_cpu_max_sockets"'
op|':'
number|'4'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
number|'4'
op|','
number|'4'
op|','
number|'1'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
comment|'# Image limits kill flavor preferred'
nl|'\n'
string|'"allow_threads"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"flavor"'
op|':'
name|'FakeFlavor'
op|'('
number|'16'
op|','
op|'{'
nl|'\n'
string|'"hw:cpu_sockets"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"hw:cpu_cores"'
op|':'
string|'"8"'
op|','
nl|'\n'
string|'"hw:cpu_threads"'
op|':'
string|'"1"'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"properties"'
op|':'
op|'{'
nl|'\n'
string|'"hw_cpu_max_cores"'
op|':'
number|'4'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"expect"'
op|':'
op|'['
number|'16'
op|','
number|'1'
op|','
number|'1'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'test'
name|'in'
name|'testdata'
op|':'
newline|'\n'
indent|'            '
name|'topology'
op|'='
name|'hw'
op|'.'
name|'VirtCPUTopology'
op|'.'
name|'get_desirable_configs'
op|'('
nl|'\n'
name|'test'
op|'['
string|'"flavor"'
op|']'
op|','
nl|'\n'
name|'test'
op|'['
string|'"image"'
op|']'
op|','
nl|'\n'
name|'test'
op|'['
string|'"allow_threads"'
op|']'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|'['
number|'0'
op|']'
op|','
name|'topology'
op|'.'
name|'sockets'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|'['
number|'1'
op|']'
op|','
name|'topology'
op|'.'
name|'cores'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test'
op|'['
string|'"expect"'
op|']'
op|'['
number|'2'
op|']'
op|','
name|'topology'
op|'.'
name|'threads'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
