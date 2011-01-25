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
string|'"""\nAuth driver using the DB as its backend.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
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
name|'db'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DbDriver
name|'class'
name|'DbDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""DB Auth driver\n\n    Defines enter and exit and therefore supports the with/as syntax.\n    """'
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
string|'"""Imports the LDAP module"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
name|'exc_type'
op|','
name|'exc_value'
op|','
name|'traceback'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|get_user
dedent|''
name|'def'
name|'get_user'
op|'('
name|'self'
op|','
name|'uid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieve user by id"""'
newline|'\n'
name|'user'
op|'='
name|'db'
op|'.'
name|'user_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'uid'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_db_user_to_auth_user'
op|'('
name|'user'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_user_from_access_key
dedent|''
name|'def'
name|'get_user_from_access_key'
op|'('
name|'self'
op|','
name|'access'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieve user by access key"""'
newline|'\n'
name|'user'
op|'='
name|'db'
op|'.'
name|'user_get_by_access_key'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'access'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_db_user_to_auth_user'
op|'('
name|'user'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_project
dedent|''
name|'def'
name|'get_project'
op|'('
name|'self'
op|','
name|'pid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieve project by id"""'
newline|'\n'
name|'project'
op|'='
name|'db'
op|'.'
name|'project_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'pid'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_db_project_to_auth_projectuser'
op|'('
name|'project'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_users
dedent|''
name|'def'
name|'get_users'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieve list of users"""'
newline|'\n'
name|'return'
op|'['
name|'self'
op|'.'
name|'_db_user_to_auth_user'
op|'('
name|'user'
op|')'
nl|'\n'
name|'for'
name|'user'
name|'in'
name|'db'
op|'.'
name|'user_get_all'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_projects
dedent|''
name|'def'
name|'get_projects'
op|'('
name|'self'
op|','
name|'uid'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieve list of projects"""'
newline|'\n'
name|'if'
name|'uid'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'db'
op|'.'
name|'project_get_by_user'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'uid'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'db'
op|'.'
name|'project_get_all'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'['
name|'self'
op|'.'
name|'_db_project_to_auth_projectuser'
op|'('
name|'proj'
op|')'
name|'for'
name|'proj'
name|'in'
name|'result'
op|']'
newline|'\n'
nl|'\n'
DECL|member|create_user
dedent|''
name|'def'
name|'create_user'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'access_key'
op|','
name|'secret_key'
op|','
name|'is_admin'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a user"""'
newline|'\n'
name|'values'
op|'='
op|'{'
string|"'id'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'access_key'"
op|':'
name|'access_key'
op|','
nl|'\n'
string|"'secret_key'"
op|':'
name|'secret_key'
op|','
nl|'\n'
string|"'is_admin'"
op|':'
name|'is_admin'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'user_ref'
op|'='
name|'db'
op|'.'
name|'user_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'values'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_db_user_to_auth_user'
op|'('
name|'user_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Duplicate'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Duplicate'
op|'('
name|'_'
op|'('
string|"'User %s already exists'"
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_db_user_to_auth_user
dedent|''
dedent|''
name|'def'
name|'_db_user_to_auth_user'
op|'('
name|'self'
op|','
name|'user_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'id'"
op|':'
name|'user_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'user_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'access'"
op|':'
name|'user_ref'
op|'['
string|"'access_key'"
op|']'
op|','
nl|'\n'
string|"'secret'"
op|':'
name|'user_ref'
op|'['
string|"'secret_key'"
op|']'
op|','
nl|'\n'
string|"'admin'"
op|':'
name|'user_ref'
op|'['
string|"'is_admin'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_db_project_to_auth_projectuser
dedent|''
name|'def'
name|'_db_project_to_auth_projectuser'
op|'('
name|'self'
op|','
name|'project_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'member_ids'
op|'='
op|'['
name|'member'
op|'['
string|"'id'"
op|']'
name|'for'
name|'member'
name|'in'
name|'project_ref'
op|'['
string|"'members'"
op|']'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'id'"
op|':'
name|'project_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'project_ref'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'project_manager_id'"
op|':'
name|'project_ref'
op|'['
string|"'project_manager'"
op|']'
op|','
nl|'\n'
string|"'description'"
op|':'
name|'project_ref'
op|'['
string|"'description'"
op|']'
op|','
nl|'\n'
string|"'member_ids'"
op|':'
name|'member_ids'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|create_project
dedent|''
name|'def'
name|'create_project'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'manager_uid'
op|','
nl|'\n'
name|'description'
op|'='
name|'None'
op|','
name|'member_uids'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a project"""'
newline|'\n'
name|'manager'
op|'='
name|'db'
op|'.'
name|'user_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'manager_uid'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'manager'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|'"Project can\'t be created because "'
nl|'\n'
string|'"manager %s doesn\'t exist"'
op|')'
nl|'\n'
op|'%'
name|'manager_uid'
op|')'
newline|'\n'
nl|'\n'
comment|'# description is a required attribute'
nl|'\n'
dedent|''
name|'if'
name|'description'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'description'
op|'='
name|'name'
newline|'\n'
nl|'\n'
comment|'# First, we ensure that all the given users exist before we go'
nl|'\n'
comment|"# on to create the project. This way we won't have to destroy"
nl|'\n'
comment|'# the project again because a user turns out to be invalid.'
nl|'\n'
dedent|''
name|'members'
op|'='
name|'set'
op|'('
op|'['
name|'manager'
op|']'
op|')'
newline|'\n'
name|'if'
name|'member_uids'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'member_uid'
name|'in'
name|'member_uids'
op|':'
newline|'\n'
indent|'                '
name|'member'
op|'='
name|'db'
op|'.'
name|'user_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'member_uid'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'member'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|'"Project can\'t be created "'
nl|'\n'
string|'"because user %s doesn\'t exist"'
op|')'
nl|'\n'
op|'%'
name|'member_uid'
op|')'
newline|'\n'
dedent|''
name|'members'
op|'.'
name|'add'
op|'('
name|'member'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'values'
op|'='
op|'{'
string|"'id'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'project_manager'"
op|':'
name|'manager'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'description'"
op|':'
name|'description'
op|'}'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'project'
op|'='
name|'db'
op|'.'
name|'project_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'values'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Duplicate'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Duplicate'
op|'('
name|'_'
op|'('
string|'"Project can\'t be created because "'
nl|'\n'
string|'"project %s already exists"'
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'member'
name|'in'
name|'members'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'project_add_member'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'project'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'member'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# This looks silly, but ensures that the members element has been'
nl|'\n'
comment|'# correctly populated'
nl|'\n'
dedent|''
name|'project_ref'
op|'='
name|'db'
op|'.'
name|'project_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'project'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_db_project_to_auth_projectuser'
op|'('
name|'project_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|modify_project
dedent|''
name|'def'
name|'modify_project'
op|'('
name|'self'
op|','
name|'project_id'
op|','
name|'manager_uid'
op|'='
name|'None'
op|','
name|'description'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Modify an existing project"""'
newline|'\n'
name|'if'
name|'not'
name|'manager_uid'
name|'and'
name|'not'
name|'description'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'values'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'manager_uid'
op|':'
newline|'\n'
indent|'            '
name|'manager'
op|'='
name|'db'
op|'.'
name|'user_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'manager_uid'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'manager'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|'"Project can\'t be modified because "'
nl|'\n'
string|'"manager %s doesn\'t exist"'
op|')'
op|'%'
nl|'\n'
name|'manager_uid'
op|')'
newline|'\n'
dedent|''
name|'values'
op|'['
string|"'project_manager'"
op|']'
op|'='
name|'manager'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'description'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'['
string|"'description'"
op|']'
op|'='
name|'description'
newline|'\n'
nl|'\n'
dedent|''
name|'db'
op|'.'
name|'project_update'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'project_id'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_to_project
dedent|''
name|'def'
name|'add_to_project'
op|'('
name|'self'
op|','
name|'uid'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add user to project"""'
newline|'\n'
name|'user'
op|','
name|'project'
op|'='
name|'self'
op|'.'
name|'_validate_user_and_project'
op|'('
name|'uid'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'project_add_member'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'project'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'user'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_from_project
dedent|''
name|'def'
name|'remove_from_project'
op|'('
name|'self'
op|','
name|'uid'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove user from project"""'
newline|'\n'
name|'user'
op|','
name|'project'
op|'='
name|'self'
op|'.'
name|'_validate_user_and_project'
op|'('
name|'uid'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'project_remove_member'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'project'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'user'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_in_project
dedent|''
name|'def'
name|'is_in_project'
op|'('
name|'self'
op|','
name|'uid'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if user is in project"""'
newline|'\n'
name|'user'
op|','
name|'project'
op|'='
name|'self'
op|'.'
name|'_validate_user_and_project'
op|'('
name|'uid'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'return'
name|'user'
name|'in'
name|'project'
op|'.'
name|'members'
newline|'\n'
nl|'\n'
DECL|member|has_role
dedent|''
name|'def'
name|'has_role'
op|'('
name|'self'
op|','
name|'uid'
op|','
name|'role'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if user has role\n\n        If project is specified, it checks for local role, otherwise it\n        checks for global role\n        """'
newline|'\n'
nl|'\n'
name|'return'
name|'role'
name|'in'
name|'self'
op|'.'
name|'get_user_roles'
op|'('
name|'uid'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_role
dedent|''
name|'def'
name|'add_role'
op|'('
name|'self'
op|','
name|'uid'
op|','
name|'role'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add role for user (or user and project)"""'
newline|'\n'
name|'if'
name|'not'
name|'project_id'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'user_add_role'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'uid'
op|','
name|'role'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'user_add_project_role'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'uid'
op|','
name|'project_id'
op|','
name|'role'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_role
dedent|''
name|'def'
name|'remove_role'
op|'('
name|'self'
op|','
name|'uid'
op|','
name|'role'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove role for user (or user and project)"""'
newline|'\n'
name|'if'
name|'not'
name|'project_id'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'user_remove_role'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'uid'
op|','
name|'role'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'user_remove_project_role'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'uid'
op|','
name|'project_id'
op|','
name|'role'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_user_roles
dedent|''
name|'def'
name|'get_user_roles'
op|'('
name|'self'
op|','
name|'uid'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieve list of roles for user (or user and project)"""'
newline|'\n'
name|'if'
name|'project_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'roles'
op|'='
name|'db'
op|'.'
name|'user_get_roles'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'uid'
op|')'
newline|'\n'
name|'return'
name|'roles'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'roles'
op|'='
name|'db'
op|'.'
name|'user_get_roles_for_project'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'uid'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'return'
name|'roles'
newline|'\n'
nl|'\n'
DECL|member|delete_user
dedent|''
dedent|''
name|'def'
name|'delete_user'
op|'('
name|'self'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete a user"""'
newline|'\n'
name|'user'
op|'='
name|'db'
op|'.'
name|'user_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'user_delete'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'user'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_project
dedent|''
name|'def'
name|'delete_project'
op|'('
name|'self'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete a project"""'
newline|'\n'
name|'db'
op|'.'
name|'project_delete'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|modify_user
dedent|''
name|'def'
name|'modify_user'
op|'('
name|'self'
op|','
name|'uid'
op|','
name|'access_key'
op|'='
name|'None'
op|','
name|'secret_key'
op|'='
name|'None'
op|','
name|'admin'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Modify an existing user"""'
newline|'\n'
name|'if'
name|'not'
name|'access_key'
name|'and'
name|'not'
name|'secret_key'
name|'and'
name|'admin'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'values'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'access_key'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'['
string|"'access_key'"
op|']'
op|'='
name|'access_key'
newline|'\n'
dedent|''
name|'if'
name|'secret_key'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'['
string|"'secret_key'"
op|']'
op|'='
name|'secret_key'
newline|'\n'
dedent|''
name|'if'
name|'admin'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'['
string|"'is_admin'"
op|']'
op|'='
name|'admin'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'user_update'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'uid'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_validate_user_and_project
dedent|''
name|'def'
name|'_validate_user_and_project'
op|'('
name|'self'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'user'
op|'='
name|'db'
op|'.'
name|'user_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'user_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'user'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|'\'User "%s" not found\''
op|')'
op|'%'
name|'user_id'
op|')'
newline|'\n'
dedent|''
name|'project'
op|'='
name|'db'
op|'.'
name|'project_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'project'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|'\'Project "%s" not found\''
op|')'
op|'%'
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'user'
op|','
name|'project'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
