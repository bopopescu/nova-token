begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""Greenthread local storage of variables using weak references"""'
newline|'\n'
nl|'\n'
name|'import'
name|'weakref'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'corolocal'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WeakLocal
name|'class'
name|'WeakLocal'
op|'('
name|'corolocal'
op|'.'
name|'local'
op|')'
op|':'
newline|'\n'
DECL|member|__getattribute__
indent|'    '
name|'def'
name|'__getattribute__'
op|'('
name|'self'
op|','
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rval'
op|'='
name|'corolocal'
op|'.'
name|'local'
op|'.'
name|'__getattribute__'
op|'('
name|'self'
op|','
name|'attr'
op|')'
newline|'\n'
name|'if'
name|'rval'
op|':'
newline|'\n'
comment|'# NOTE(mikal): this bit is confusing. What is stored is a weak'
nl|'\n'
comment|'# reference, not the value itself. We therefore need to lookup'
nl|'\n'
comment|'# the weak reference and return the inner value here.'
nl|'\n'
indent|'            '
name|'rval'
op|'='
name|'rval'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'rval'
newline|'\n'
nl|'\n'
DECL|member|__setattr__
dedent|''
name|'def'
name|'__setattr__'
op|'('
name|'self'
op|','
name|'attr'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
name|'weakref'
op|'.'
name|'ref'
op|'('
name|'value'
op|')'
newline|'\n'
name|'return'
name|'corolocal'
op|'.'
name|'local'
op|'.'
name|'__setattr__'
op|'('
name|'self'
op|','
name|'attr'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(mikal): the name "store" should be deprecated in the future'
nl|'\n'
DECL|variable|store
dedent|''
dedent|''
name|'store'
op|'='
name|'WeakLocal'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# A "weak" store uses weak references and allows an object to fall out of scope'
nl|'\n'
comment|'# when it falls out of scope in the code that uses the thread local storage. A'
nl|'\n'
comment|'# "strong" store will hold a reference to the object so that it never falls out'
nl|'\n'
comment|'# of scope.'
nl|'\n'
DECL|variable|weak_store
name|'weak_store'
op|'='
name|'WeakLocal'
op|'('
op|')'
newline|'\n'
DECL|variable|strong_store
name|'strong_store'
op|'='
name|'corolocal'
op|'.'
name|'local'
newline|'\n'
endmarker|''
end_unit
