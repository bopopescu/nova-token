begin_unit
comment|'# Copyright 2016 IBM Corp.'
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
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
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
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fixtures'
name|'as'
name|'nova_fixtures'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'policy_fixture'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestAggregateCreation
name|'class'
name|'TestAggregateCreation'
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
name|'TestAggregateCreation'
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
name|'useFixture'
op|'('
name|'policy_fixture'
op|'.'
name|'RealPolicyFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'api_fixture'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'nova_fixtures'
op|'.'
name|'OSAPIFixture'
op|'('
nl|'\n'
name|'api_version'
op|'='
string|"'v2.1'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'='
name|'api_fixture'
op|'.'
name|'admin_api'
newline|'\n'
nl|'\n'
DECL|member|test_name_validation
dedent|''
name|'def'
name|'test_name_validation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Regression test for bug #1552888.\n\n        The current aggregate accepts a null param for availablitliy zone,\n        change to the validation might affect some command like\n        \'nova aggregate create foo\'\n        This test ensure those kind of change won\'t affect validation\n        """'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"aggregate"'
op|':'
op|'{'
string|'"name"'
op|':'
string|'"foo"'
op|','
string|'"availability_zone"'
op|':'
name|'None'
op|'}'
op|'}'
newline|'\n'
comment|'# This should success'
nl|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'api_post'
op|'('
string|"'/os-aggregates'"
op|','
name|'body'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit