begin_unit
comment|'# Copyright 2012 OpenStack Foundation  # All Rights Reserved.'
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
string|'"""\nFake Loadable subclasses module #1\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_loadables'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeLoadableSubClass1
name|'class'
name|'FakeLoadableSubClass1'
op|'('
name|'fake_loadables'
op|'.'
name|'FakeLoadable'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeLoadableSubClass2
dedent|''
name|'class'
name|'FakeLoadableSubClass2'
op|'('
name|'fake_loadables'
op|'.'
name|'FakeLoadable'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_FakeLoadableSubClass3
dedent|''
name|'class'
name|'_FakeLoadableSubClass3'
op|'('
name|'fake_loadables'
op|'.'
name|'FakeLoadable'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Classes beginning with \'_\' will be ignored."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeLoadableSubClass4
dedent|''
name|'class'
name|'FakeLoadableSubClass4'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Not a correct subclass."""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_valid_classes
dedent|''
name|'def'
name|'return_valid_classes'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
name|'FakeLoadableSubClass1'
op|','
name|'FakeLoadableSubClass2'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_invalid_classes
dedent|''
name|'def'
name|'return_invalid_classes'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
name|'FakeLoadableSubClass1'
op|','
name|'_FakeLoadableSubClass3'
op|','
nl|'\n'
name|'FakeLoadableSubClass4'
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
