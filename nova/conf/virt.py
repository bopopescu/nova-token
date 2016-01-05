begin_unit
comment|'# Copyright 2015 Intel Corporation'
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|vcpu_pin_set
name|'vcpu_pin_set'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'vcpu_pin_set'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Defines which pcpus that instance vcpus can use. For example, '"
nl|'\n'
string|'\'"4-12,^8,15"\''
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALL_OPTS
name|'ALL_OPTS'
op|'='
op|'['
name|'vcpu_pin_set'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_opts
name|'def'
name|'register_opts'
op|'('
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'ALL_OPTS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
dedent|''
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# TODO(sfinucan): This should be moved to a virt or hardware group'
nl|'\n'
indent|'    '
name|'return'
op|'('
string|"'DEFAULT'"
op|','
name|'ALL_OPTS'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
