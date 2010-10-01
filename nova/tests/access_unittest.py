begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
name|'import'
name|'unittest'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'webob'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'ec2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|class|Context
name|'class'
name|'Context'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|AccessTestCase
dedent|''
name|'class'
name|'AccessTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
op|')'
op|':'
newline|'\n'
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
name|'AccessTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'um'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
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
comment|'# Make test users'
nl|'\n'
name|'self'
op|'.'
name|'testadmin'
op|'='
name|'um'
op|'.'
name|'create_user'
op|'('
string|"'testadmin'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'testpmsys'
op|'='
name|'um'
op|'.'
name|'create_user'
op|'('
string|"'testpmsys'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'testnet'
op|'='
name|'um'
op|'.'
name|'create_user'
op|'('
string|"'testnet'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'testsys'
op|'='
name|'um'
op|'.'
name|'create_user'
op|'('
string|"'testsys'"
op|')'
newline|'\n'
comment|'# Assign some rules'
nl|'\n'
name|'um'
op|'.'
name|'add_role'
op|'('
string|"'testadmin'"
op|','
string|"'cloudadmin'"
op|')'
newline|'\n'
name|'um'
op|'.'
name|'add_role'
op|'('
string|"'testpmsys'"
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
name|'um'
op|'.'
name|'add_role'
op|'('
string|"'testnet'"
op|','
string|"'netadmin'"
op|')'
newline|'\n'
name|'um'
op|'.'
name|'add_role'
op|'('
string|"'testsys'"
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Make a test project'
nl|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'um'
op|'.'
name|'create_project'
op|'('
string|"'testproj'"
op|','
nl|'\n'
string|"'testpmsys'"
op|','
nl|'\n'
string|"'a test project'"
op|','
nl|'\n'
op|'['
string|"'testpmsys'"
op|','
string|"'testnet'"
op|','
string|"'testsys'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'.'
name|'add_role'
op|'('
name|'self'
op|'.'
name|'testnet'
op|','
string|"'netadmin'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'.'
name|'add_role'
op|'('
name|'self'
op|'.'
name|'testsys'
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
comment|'#user is set in each test'
nl|'\n'
DECL|function|noopWSGIApp
name|'def'
name|'noopWSGIApp'
op|'('
name|'environ'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'start_response'
op|'('
string|"'200 OK'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'return'
op|'['
string|"''"
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mw'
op|'='
name|'ec2'
op|'.'
name|'Authorizer'
op|'('
name|'noopWSGIApp'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mw'
op|'.'
name|'action_roles'
op|'='
op|'{'
string|"'str'"
op|':'
op|'{'
nl|'\n'
string|"'_allow_all'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'_allow_none'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'_allow_project_manager'"
op|':'
op|'['
string|"'projectmanager'"
op|']'
op|','
nl|'\n'
string|"'_allow_sys_and_net'"
op|':'
op|'['
string|"'sysadmin'"
op|','
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'_allow_sysadmin'"
op|':'
op|'['
string|"'sysadmin'"
op|']'
op|'}'
op|'}'
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
indent|'        '
name|'um'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
comment|'# Delete the test project'
nl|'\n'
name|'um'
op|'.'
name|'delete_project'
op|'('
string|"'testproj'"
op|')'
newline|'\n'
comment|'# Delete the test user'
nl|'\n'
name|'um'
op|'.'
name|'delete_user'
op|'('
string|"'testadmin'"
op|')'
newline|'\n'
name|'um'
op|'.'
name|'delete_user'
op|'('
string|"'testpmsys'"
op|')'
newline|'\n'
name|'um'
op|'.'
name|'delete_user'
op|'('
string|"'testnet'"
op|')'
newline|'\n'
name|'um'
op|'.'
name|'delete_user'
op|'('
string|"'testsys'"
op|')'
newline|'\n'
name|'super'
op|'('
name|'AccessTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|response_status
dedent|''
name|'def'
name|'response_status'
op|'('
name|'self'
op|','
name|'user'
op|','
name|'methodName'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user'
op|','
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'environ'
op|'='
op|'{'
string|"'ec2.context'"
op|':'
name|'ctxt'
op|','
nl|'\n'
string|"'ec2.controller'"
op|':'
string|"'some string'"
op|','
nl|'\n'
string|"'ec2.action'"
op|':'
name|'methodName'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|','
name|'environ'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'mw'
op|')'
newline|'\n'
name|'return'
name|'resp'
op|'.'
name|'status_int'
newline|'\n'
nl|'\n'
DECL|member|shouldAllow
dedent|''
name|'def'
name|'shouldAllow'
op|'('
name|'self'
op|','
name|'user'
op|','
name|'methodName'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'self'
op|'.'
name|'response_status'
op|'('
name|'user'
op|','
name|'methodName'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|shouldDeny
dedent|''
name|'def'
name|'shouldDeny'
op|'('
name|'self'
op|','
name|'user'
op|','
name|'methodName'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'401'
op|','
name|'self'
op|'.'
name|'response_status'
op|'('
name|'user'
op|','
name|'methodName'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_001_allow_all
dedent|''
name|'def'
name|'test_001_allow_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'users'
op|'='
op|'['
name|'self'
op|'.'
name|'testadmin'
op|','
name|'self'
op|'.'
name|'testpmsys'
op|','
name|'self'
op|'.'
name|'testnet'
op|','
name|'self'
op|'.'
name|'testsys'
op|']'
newline|'\n'
name|'for'
name|'user'
name|'in'
name|'users'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'shouldAllow'
op|'('
name|'user'
op|','
string|"'_allow_all'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_002_allow_none
dedent|''
dedent|''
name|'def'
name|'test_002_allow_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'shouldAllow'
op|'('
name|'self'
op|'.'
name|'testadmin'
op|','
string|"'_allow_none'"
op|')'
newline|'\n'
name|'users'
op|'='
op|'['
name|'self'
op|'.'
name|'testpmsys'
op|','
name|'self'
op|'.'
name|'testnet'
op|','
name|'self'
op|'.'
name|'testsys'
op|']'
newline|'\n'
name|'for'
name|'user'
name|'in'
name|'users'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'shouldDeny'
op|'('
name|'user'
op|','
string|"'_allow_none'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_003_allow_project_manager
dedent|''
dedent|''
name|'def'
name|'test_003_allow_project_manager'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'user'
name|'in'
op|'['
name|'self'
op|'.'
name|'testadmin'
op|','
name|'self'
op|'.'
name|'testpmsys'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'shouldAllow'
op|'('
name|'user'
op|','
string|"'_allow_project_manager'"
op|')'
newline|'\n'
dedent|''
name|'for'
name|'user'
name|'in'
op|'['
name|'self'
op|'.'
name|'testnet'
op|','
name|'self'
op|'.'
name|'testsys'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'shouldDeny'
op|'('
name|'user'
op|','
string|"'_allow_project_manager'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_004_allow_sys_and_net
dedent|''
dedent|''
name|'def'
name|'test_004_allow_sys_and_net'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'user'
name|'in'
op|'['
name|'self'
op|'.'
name|'testadmin'
op|','
name|'self'
op|'.'
name|'testnet'
op|','
name|'self'
op|'.'
name|'testsys'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'shouldAllow'
op|'('
name|'user'
op|','
string|"'_allow_sys_and_net'"
op|')'
newline|'\n'
comment|"# denied because it doesn't have the per project sysadmin"
nl|'\n'
dedent|''
name|'for'
name|'user'
name|'in'
op|'['
name|'self'
op|'.'
name|'testpmsys'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'shouldDeny'
op|'('
name|'user'
op|','
string|"'_allow_sys_and_net'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
comment|'# TODO: Implement use_fake as an option'
nl|'\n'
indent|'    '
name|'unittest'
op|'.'
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
