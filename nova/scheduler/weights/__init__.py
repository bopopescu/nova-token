begin_unit
comment|'# Copyright (c) 2011 OpenStack Foundation'
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
string|'"""\nScheduler host weights\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'weights'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WeighedHost
name|'class'
name|'WeighedHost'
op|'('
name|'weights'
op|'.'
name|'WeighedObject'
op|')'
op|':'
newline|'\n'
DECL|member|to_dict
indent|'    '
name|'def'
name|'to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'x'
op|'='
name|'dict'
op|'('
name|'weight'
op|'='
name|'self'
op|'.'
name|'weight'
op|')'
newline|'\n'
name|'x'
op|'['
string|"'host'"
op|']'
op|'='
name|'self'
op|'.'
name|'obj'
op|'.'
name|'host'
newline|'\n'
name|'return'
name|'x'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"WeighedHost [host: %r, weight: %s]"'
op|'%'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'obj'
op|','
name|'self'
op|'.'
name|'weight'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseHostWeigher
dedent|''
dedent|''
name|'class'
name|'BaseHostWeigher'
op|'('
name|'weights'
op|'.'
name|'BaseWeigher'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for host weights."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostWeightHandler
dedent|''
name|'class'
name|'HostWeightHandler'
op|'('
name|'weights'
op|'.'
name|'BaseWeightHandler'
op|')'
op|':'
newline|'\n'
DECL|variable|object_class
indent|'    '
name|'object_class'
op|'='
name|'WeighedHost'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'HostWeightHandler'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'BaseHostWeigher'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|all_weighers
dedent|''
dedent|''
name|'def'
name|'all_weighers'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a list of weight plugin classes found in this directory."""'
newline|'\n'
name|'return'
name|'HostWeightHandler'
op|'('
op|')'
op|'.'
name|'get_all_classes'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
