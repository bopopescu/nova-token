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
string|'"""\nAuth driver for ldap.  Includes FakeLdapDriver.\n\nIt should be easy to create a replacement for this driver supporting\nother backends by creating another class that exposes the same\npublic methods.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
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
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ldap_url'"
op|','
string|"'ldap://localhost'"
op|','
nl|'\n'
string|"'Point this at your ldap server'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ldap_password'"
op|','
string|"'changeme'"
op|','
string|"'LDAP password'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ldap_user_dn'"
op|','
string|"'cn=Manager,dc=example,dc=com'"
op|','
nl|'\n'
string|"'DN of admin user'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ldap_user_unit'"
op|','
string|"'Users'"
op|','
string|"'OID for Users'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ldap_user_subtree'"
op|','
string|"'ou=Users,dc=example,dc=com'"
op|','
nl|'\n'
string|"'OU for Users'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ldap_project_subtree'"
op|','
string|"'ou=Groups,dc=example,dc=com'"
op|','
nl|'\n'
string|"'OU for Projects'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'role_project_subtree'"
op|','
string|"'ou=Groups,dc=example,dc=com'"
op|','
nl|'\n'
string|"'OU for Roles'"
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(vish): mapping with these flags is necessary because we're going"
nl|'\n'
comment|'#             to tie in to an existing ldap schema'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ldap_cloudadmin'"
op|','
nl|'\n'
string|"'cn=cloudadmins,ou=Groups,dc=example,dc=com'"
op|','
string|"'cn for Cloud Admins'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ldap_itsec'"
op|','
nl|'\n'
string|"'cn=itsec,ou=Groups,dc=example,dc=com'"
op|','
string|"'cn for ItSec'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ldap_sysadmin'"
op|','
nl|'\n'
string|"'cn=sysadmins,ou=Groups,dc=example,dc=com'"
op|','
string|"'cn for Sysadmins'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ldap_netadmin'"
op|','
nl|'\n'
string|"'cn=netadmins,ou=Groups,dc=example,dc=com'"
op|','
string|"'cn for NetAdmins'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ldap_developer'"
op|','
nl|'\n'
string|"'cn=developers,ou=Groups,dc=example,dc=com'"
op|','
string|"'cn for Developers'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(vish): make an abstract base class with the same public methods'
nl|'\n'
comment|"#             to define a set interface for AuthDrivers. I'm delaying"
nl|'\n'
comment|"#             creating this now because I'm expecting an auth refactor"
nl|'\n'
comment|'#             in which we may want to change the interface a bit more.'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|LdapDriver
name|'class'
name|'LdapDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ldap Auth driver\n\n    Defines enter and exit and therefore supports the with/as syntax.\n    """'
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
name|'self'
op|'.'
name|'ldap'
op|'='
name|'__import__'
op|'('
string|"'ldap'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'None'
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
string|'"""Creates the connection to LDAP"""'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'self'
op|'.'
name|'ldap'
op|'.'
name|'initialize'
op|'('
name|'FLAGS'
op|'.'
name|'ldap_url'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'simple_bind_s'
op|'('
name|'FLAGS'
op|'.'
name|'ldap_user_dn'
op|','
name|'FLAGS'
op|'.'
name|'ldap_password'
op|')'
newline|'\n'
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
string|'"""Destroys the connection to LDAP"""'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'unbind_s'
op|'('
op|')'
newline|'\n'
name|'return'
name|'False'
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
name|'attr'
op|'='
name|'self'
op|'.'
name|'__find_object'
op|'('
name|'self'
op|'.'
name|'__uid_to_dn'
op|'('
name|'uid'
op|')'
op|','
nl|'\n'
string|"'(objectclass=novaUser)'"
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'__to_user'
op|'('
name|'attr'
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
name|'query'
op|'='
string|"'(accessKey=%s)'"
op|'%'
name|'access'
newline|'\n'
name|'dn'
op|'='
name|'FLAGS'
op|'.'
name|'ldap_user_subtree'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'__to_user'
op|'('
name|'self'
op|'.'
name|'__find_object'
op|'('
name|'dn'
op|','
name|'query'
op|')'
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
name|'dn'
op|'='
string|"'cn=%s,%s'"
op|'%'
op|'('
name|'pid'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'ldap_project_subtree'
op|')'
newline|'\n'
name|'attr'
op|'='
name|'self'
op|'.'
name|'__find_object'
op|'('
name|'dn'
op|','
string|"'(objectclass=novaProject)'"
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'__to_project'
op|'('
name|'attr'
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
name|'attrs'
op|'='
name|'self'
op|'.'
name|'__find_objects'
op|'('
name|'FLAGS'
op|'.'
name|'ldap_user_subtree'
op|','
nl|'\n'
string|"'(objectclass=novaUser)'"
op|')'
newline|'\n'
name|'return'
op|'['
name|'self'
op|'.'
name|'__to_user'
op|'('
name|'attr'
op|')'
name|'for'
name|'attr'
name|'in'
name|'attrs'
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
name|'pattern'
op|'='
string|"'(objectclass=novaProject)'"
newline|'\n'
name|'if'
name|'uid'
op|':'
newline|'\n'
indent|'            '
name|'pattern'
op|'='
string|'"(&%s(member=%s))"'
op|'%'
op|'('
name|'pattern'
op|','
name|'self'
op|'.'
name|'__uid_to_dn'
op|'('
name|'uid'
op|')'
op|')'
newline|'\n'
dedent|''
name|'attrs'
op|'='
name|'self'
op|'.'
name|'__find_objects'
op|'('
name|'FLAGS'
op|'.'
name|'ldap_project_subtree'
op|','
nl|'\n'
name|'pattern'
op|')'
newline|'\n'
name|'return'
op|'['
name|'self'
op|'.'
name|'__to_project'
op|'('
name|'attr'
op|')'
name|'for'
name|'attr'
name|'in'
name|'attrs'
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
name|'if'
name|'self'
op|'.'
name|'__user_exists'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Duplicate'
op|'('
string|'"LDAP user %s already exists"'
op|'%'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'attr'
op|'='
op|'['
nl|'\n'
op|'('
string|"'objectclass'"
op|','
op|'['
string|"'person'"
op|','
nl|'\n'
string|"'organizationalPerson'"
op|','
nl|'\n'
string|"'inetOrgPerson'"
op|','
nl|'\n'
string|"'novaUser'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'ou'"
op|','
op|'['
name|'FLAGS'
op|'.'
name|'ldap_user_unit'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'uid'"
op|','
op|'['
name|'name'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'sn'"
op|','
op|'['
name|'name'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'cn'"
op|','
op|'['
name|'name'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'secretKey'"
op|','
op|'['
name|'secret_key'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'accessKey'"
op|','
op|'['
name|'access_key'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'isAdmin'"
op|','
op|'['
name|'str'
op|'('
name|'is_admin'
op|')'
op|'.'
name|'upper'
op|'('
op|')'
op|']'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'add_s'
op|'('
name|'self'
op|'.'
name|'__uid_to_dn'
op|'('
name|'name'
op|')'
op|','
name|'attr'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'__to_user'
op|'('
name|'dict'
op|'('
name|'attr'
op|')'
op|')'
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
name|'if'
name|'self'
op|'.'
name|'__project_exists'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Duplicate'
op|'('
string|'"Project can\'t be created because "'
nl|'\n'
string|'"project %s already exists"'
op|'%'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'__user_exists'
op|'('
name|'manager_uid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"Project can\'t be created because "'
nl|'\n'
string|'"manager %s doesn\'t exist"'
op|'%'
name|'manager_uid'
op|')'
newline|'\n'
dedent|''
name|'manager_dn'
op|'='
name|'self'
op|'.'
name|'__uid_to_dn'
op|'('
name|'manager_uid'
op|')'
newline|'\n'
comment|'# description is a required attribute'
nl|'\n'
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
dedent|''
name|'members'
op|'='
op|'['
op|']'
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
name|'if'
name|'not'
name|'self'
op|'.'
name|'__user_exists'
op|'('
name|'member_uid'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"Project can\'t be created "'
nl|'\n'
string|'"because user %s doesn\'t exist"'
nl|'\n'
op|'%'
name|'member_uid'
op|')'
newline|'\n'
dedent|''
name|'members'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'__uid_to_dn'
op|'('
name|'member_uid'
op|')'
op|')'
newline|'\n'
comment|'# always add the manager as a member because members is required'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'manager_dn'
name|'in'
name|'members'
op|':'
newline|'\n'
indent|'            '
name|'members'
op|'.'
name|'append'
op|'('
name|'manager_dn'
op|')'
newline|'\n'
dedent|''
name|'attr'
op|'='
op|'['
nl|'\n'
op|'('
string|"'objectclass'"
op|','
op|'['
string|"'novaProject'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'cn'"
op|','
op|'['
name|'name'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'description'"
op|','
op|'['
name|'description'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'projectManager'"
op|','
op|'['
name|'manager_dn'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'member'"
op|','
name|'members'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'add_s'
op|'('
string|"'cn=%s,%s'"
op|'%'
op|'('
name|'name'
op|','
name|'FLAGS'
op|'.'
name|'ldap_project_subtree'
op|')'
op|','
name|'attr'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'__to_project'
op|'('
name|'dict'
op|'('
name|'attr'
op|')'
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
name|'dn'
op|'='
string|"'cn=%s,%s'"
op|'%'
op|'('
name|'project_id'
op|','
name|'FLAGS'
op|'.'
name|'ldap_project_subtree'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'__add_to_group'
op|'('
name|'uid'
op|','
name|'dn'
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
name|'dn'
op|'='
string|"'cn=%s,%s'"
op|'%'
op|'('
name|'project_id'
op|','
name|'FLAGS'
op|'.'
name|'ldap_project_subtree'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'__remove_from_group'
op|'('
name|'uid'
op|','
name|'dn'
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
name|'dn'
op|'='
string|"'cn=%s,%s'"
op|'%'
op|'('
name|'project_id'
op|','
name|'FLAGS'
op|'.'
name|'ldap_project_subtree'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'__is_in_group'
op|'('
name|'uid'
op|','
name|'dn'
op|')'
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
name|'role_dn'
op|'='
name|'self'
op|'.'
name|'__role_to_dn'
op|'('
name|'role'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'__is_in_group'
op|'('
name|'uid'
op|','
name|'role_dn'
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
name|'role_dn'
op|'='
name|'self'
op|'.'
name|'__role_to_dn'
op|'('
name|'role'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'__group_exists'
op|'('
name|'role_dn'
op|')'
op|':'
newline|'\n'
comment|"# create the role if it doesn't exist"
nl|'\n'
indent|'            '
name|'description'
op|'='
string|"'%s role for %s'"
op|'%'
op|'('
name|'role'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'__create_group'
op|'('
name|'role_dn'
op|','
name|'role'
op|','
name|'uid'
op|','
name|'description'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'__add_to_group'
op|'('
name|'uid'
op|','
name|'role_dn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_role
dedent|''
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
name|'role_dn'
op|'='
name|'self'
op|'.'
name|'__role_to_dn'
op|'('
name|'role'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'__remove_from_group'
op|'('
name|'uid'
op|','
name|'role_dn'
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
comment|"# NOTE(vish): This is unneccesarily slow, but since we can't"
nl|'\n'
comment|'#             guarantee that the global roles are located'
nl|'\n'
comment|"#             together in the ldap tree, we're doing this version."
nl|'\n'
indent|'            '
name|'roles'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'role'
name|'in'
name|'FLAGS'
op|'.'
name|'allowed_roles'
op|':'
newline|'\n'
indent|'                '
name|'role_dn'
op|'='
name|'self'
op|'.'
name|'__role_to_dn'
op|'('
name|'role'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'__is_in_group'
op|'('
name|'uid'
op|','
name|'role_dn'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'roles'
op|'.'
name|'append'
op|'('
name|'role'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'roles'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'project_dn'
op|'='
string|"'cn=%s,%s'"
op|'%'
op|'('
name|'project_id'
op|','
name|'FLAGS'
op|'.'
name|'ldap_project_subtree'
op|')'
newline|'\n'
name|'roles'
op|'='
name|'self'
op|'.'
name|'__find_objects'
op|'('
name|'project_dn'
op|','
nl|'\n'
string|"'(&(&(objectclass=groupOfNames)'"
nl|'\n'
string|"'(!(objectclass=novaProject)))'"
nl|'\n'
string|"'(member=%s))'"
op|'%'
name|'self'
op|'.'
name|'__uid_to_dn'
op|'('
name|'uid'
op|')'
op|')'
newline|'\n'
name|'return'
op|'['
name|'role'
op|'['
string|"'cn'"
op|']'
op|'['
number|'0'
op|']'
name|'for'
name|'role'
name|'in'
name|'roles'
op|']'
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
name|'uid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete a user"""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'__user_exists'
op|'('
name|'uid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"User %s doesn\'t exist"'
op|'%'
name|'uid'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'__remove_from_all'
op|'('
name|'uid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'delete_s'
op|'('
string|"'uid=%s,%s'"
op|'%'
op|'('
name|'uid'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'ldap_user_subtree'
op|')'
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
name|'project_dn'
op|'='
string|"'cn=%s,%s'"
op|'%'
op|'('
name|'project_id'
op|','
name|'FLAGS'
op|'.'
name|'ldap_project_subtree'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'__delete_roles'
op|'('
name|'project_dn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'__delete_group'
op|'('
name|'project_dn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__user_exists
dedent|''
name|'def'
name|'__user_exists'
op|'('
name|'self'
op|','
name|'uid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if user exists"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'get_user'
op|'('
name|'uid'
op|')'
op|'!='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__project_exists
dedent|''
name|'def'
name|'__project_exists'
op|'('
name|'self'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if project exists"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'get_project'
op|'('
name|'project_id'
op|')'
op|'!='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__find_object
dedent|''
name|'def'
name|'__find_object'
op|'('
name|'self'
op|','
name|'dn'
op|','
name|'query'
op|'='
name|'None'
op|','
name|'scope'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find an object by dn and query"""'
newline|'\n'
name|'objects'
op|'='
name|'self'
op|'.'
name|'__find_objects'
op|'('
name|'dn'
op|','
name|'query'
op|','
name|'scope'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'objects'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'objects'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__find_dns
dedent|''
name|'def'
name|'__find_dns'
op|'('
name|'self'
op|','
name|'dn'
op|','
name|'query'
op|'='
name|'None'
op|','
name|'scope'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find dns by query"""'
newline|'\n'
name|'if'
name|'scope'
name|'is'
name|'None'
op|':'
comment|'# one of the flags is 0!!'
newline|'\n'
indent|'            '
name|'scope'
op|'='
name|'self'
op|'.'
name|'ldap'
op|'.'
name|'SCOPE_SUBTREE'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'res'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'search_s'
op|'('
name|'dn'
op|','
name|'scope'
op|','
name|'query'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'ldap'
op|'.'
name|'NO_SUCH_OBJECT'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
comment|'# just return the DNs'
nl|'\n'
dedent|''
name|'return'
op|'['
name|'dn'
name|'for'
name|'dn'
op|','
name|'_attributes'
name|'in'
name|'res'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__find_objects
dedent|''
name|'def'
name|'__find_objects'
op|'('
name|'self'
op|','
name|'dn'
op|','
name|'query'
op|'='
name|'None'
op|','
name|'scope'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find objects by query"""'
newline|'\n'
name|'if'
name|'scope'
name|'is'
name|'None'
op|':'
comment|'# one of the flags is 0!!'
newline|'\n'
indent|'            '
name|'scope'
op|'='
name|'self'
op|'.'
name|'ldap'
op|'.'
name|'SCOPE_SUBTREE'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'res'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'search_s'
op|'('
name|'dn'
op|','
name|'scope'
op|','
name|'query'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'ldap'
op|'.'
name|'NO_SUCH_OBJECT'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
comment|'# just return the attributes'
nl|'\n'
dedent|''
name|'return'
op|'['
name|'attributes'
name|'for'
name|'dn'
op|','
name|'attributes'
name|'in'
name|'res'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__find_role_dns
dedent|''
name|'def'
name|'__find_role_dns'
op|'('
name|'self'
op|','
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find dns of role objects in given tree"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'__find_dns'
op|'('
name|'tree'
op|','
nl|'\n'
string|"'(&(objectclass=groupOfNames)(!(objectclass=novaProject)))'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|__find_group_dns_with_member
dedent|''
name|'def'
name|'__find_group_dns_with_member'
op|'('
name|'self'
op|','
name|'tree'
op|','
name|'uid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find dns of group objects in a given tree that contain member"""'
newline|'\n'
name|'dns'
op|'='
name|'self'
op|'.'
name|'__find_dns'
op|'('
name|'tree'
op|','
nl|'\n'
string|"'(&(objectclass=groupOfNames)(member=%s))'"
op|'%'
nl|'\n'
name|'self'
op|'.'
name|'__uid_to_dn'
op|'('
name|'uid'
op|')'
op|')'
newline|'\n'
name|'return'
name|'dns'
newline|'\n'
nl|'\n'
DECL|member|__group_exists
dedent|''
name|'def'
name|'__group_exists'
op|'('
name|'self'
op|','
name|'dn'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if group exists"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'__find_object'
op|'('
name|'dn'
op|','
string|"'(objectclass=groupOfNames)'"
op|')'
op|'!='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|__role_to_dn
name|'def'
name|'__role_to_dn'
op|'('
name|'role'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert role to corresponding dn"""'
newline|'\n'
name|'if'
name|'project_id'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'FLAGS'
op|'.'
name|'__getitem__'
op|'('
string|'"ldap_%s"'
op|'%'
name|'role'
op|')'
op|'.'
name|'value'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'cn=%s,cn=%s,%s'"
op|'%'
op|'('
name|'role'
op|','
nl|'\n'
name|'project_id'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'ldap_project_subtree'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__create_group
dedent|''
dedent|''
name|'def'
name|'__create_group'
op|'('
name|'self'
op|','
name|'group_dn'
op|','
name|'name'
op|','
name|'uid'
op|','
nl|'\n'
name|'description'
op|','
name|'member_uids'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a group"""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'__group_exists'
op|'('
name|'group_dn'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Duplicate'
op|'('
string|'"Group can\'t be created because "'
nl|'\n'
string|'"group %s already exists"'
op|'%'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'members'
op|'='
op|'['
op|']'
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
name|'if'
name|'not'
name|'self'
op|'.'
name|'__user_exists'
op|'('
name|'member_uid'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"Group can\'t be created "'
nl|'\n'
string|'"because user %s doesn\'t exist"'
op|'%'
name|'member_uid'
op|')'
newline|'\n'
dedent|''
name|'members'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'__uid_to_dn'
op|'('
name|'member_uid'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'dn'
op|'='
name|'self'
op|'.'
name|'__uid_to_dn'
op|'('
name|'uid'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'dn'
name|'in'
name|'members'
op|':'
newline|'\n'
indent|'            '
name|'members'
op|'.'
name|'append'
op|'('
name|'dn'
op|')'
newline|'\n'
dedent|''
name|'attr'
op|'='
op|'['
nl|'\n'
op|'('
string|"'objectclass'"
op|','
op|'['
string|"'groupOfNames'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'cn'"
op|','
op|'['
name|'name'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'description'"
op|','
op|'['
name|'description'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'member'"
op|','
name|'members'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'add_s'
op|'('
name|'group_dn'
op|','
name|'attr'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__is_in_group
dedent|''
name|'def'
name|'__is_in_group'
op|'('
name|'self'
op|','
name|'uid'
op|','
name|'group_dn'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if user is in group"""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'__user_exists'
op|'('
name|'uid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"User %s can\'t be searched in group "'
nl|'\n'
string|'"becuase the user doesn\'t exist"'
op|'%'
op|'('
name|'uid'
op|','
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'__group_exists'
op|'('
name|'group_dn'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'res'
op|'='
name|'self'
op|'.'
name|'__find_object'
op|'('
name|'group_dn'
op|','
nl|'\n'
string|"'(member=%s)'"
op|'%'
name|'self'
op|'.'
name|'__uid_to_dn'
op|'('
name|'uid'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'ldap'
op|'.'
name|'SCOPE_BASE'
op|')'
newline|'\n'
name|'return'
name|'res'
op|'!='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__add_to_group
dedent|''
name|'def'
name|'__add_to_group'
op|'('
name|'self'
op|','
name|'uid'
op|','
name|'group_dn'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add user to group"""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'__user_exists'
op|'('
name|'uid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"User %s can\'t be added to the group "'
nl|'\n'
string|'"becuase the user doesn\'t exist"'
op|'%'
op|'('
name|'uid'
op|','
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'__group_exists'
op|'('
name|'group_dn'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"The group at dn %s doesn\'t exist"'
op|'%'
nl|'\n'
op|'('
name|'group_dn'
op|','
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'__is_in_group'
op|'('
name|'uid'
op|','
name|'group_dn'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Duplicate'
op|'('
string|'"User %s is already a member of "'
nl|'\n'
string|'"the group %s"'
op|'%'
op|'('
name|'uid'
op|','
name|'group_dn'
op|')'
op|')'
newline|'\n'
dedent|''
name|'attr'
op|'='
op|'['
op|'('
name|'self'
op|'.'
name|'ldap'
op|'.'
name|'MOD_ADD'
op|','
string|"'member'"
op|','
name|'self'
op|'.'
name|'__uid_to_dn'
op|'('
name|'uid'
op|')'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'modify_s'
op|'('
name|'group_dn'
op|','
name|'attr'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__remove_from_group
dedent|''
name|'def'
name|'__remove_from_group'
op|'('
name|'self'
op|','
name|'uid'
op|','
name|'group_dn'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove user from group"""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'__group_exists'
op|'('
name|'group_dn'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"The group at dn %s doesn\'t exist"'
op|'%'
nl|'\n'
op|'('
name|'group_dn'
op|','
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'__user_exists'
op|'('
name|'uid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"User %s can\'t be removed from the "'
nl|'\n'
string|'"group because the user doesn\'t exist"'
op|'%'
op|'('
name|'uid'
op|','
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'__is_in_group'
op|'('
name|'uid'
op|','
name|'group_dn'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"User %s is not a member of the group"'
op|'%'
nl|'\n'
op|'('
name|'uid'
op|','
op|')'
op|')'
newline|'\n'
comment|'# NOTE(vish): remove user from group and any sub_groups'
nl|'\n'
dedent|''
name|'sub_dns'
op|'='
name|'self'
op|'.'
name|'__find_group_dns_with_member'
op|'('
nl|'\n'
name|'group_dn'
op|','
name|'uid'
op|')'
newline|'\n'
name|'for'
name|'sub_dn'
name|'in'
name|'sub_dns'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'__safe_remove_from_group'
op|'('
name|'uid'
op|','
name|'sub_dn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__safe_remove_from_group
dedent|''
dedent|''
name|'def'
name|'__safe_remove_from_group'
op|'('
name|'self'
op|','
name|'uid'
op|','
name|'group_dn'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove user from group, deleting group if user is last member"""'
newline|'\n'
comment|'# FIXME(vish): what if deleted user is a project manager?'
nl|'\n'
name|'attr'
op|'='
op|'['
op|'('
name|'self'
op|'.'
name|'ldap'
op|'.'
name|'MOD_DELETE'
op|','
string|"'member'"
op|','
name|'self'
op|'.'
name|'__uid_to_dn'
op|'('
name|'uid'
op|')'
op|')'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'modify_s'
op|'('
name|'group_dn'
op|','
name|'attr'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'ldap'
op|'.'
name|'OBJECT_CLASS_VIOLATION'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Attempted to remove the last member of a group. "'
nl|'\n'
string|'"Deleting the group at %s instead."'
op|','
name|'group_dn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'__delete_group'
op|'('
name|'group_dn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__remove_from_all
dedent|''
dedent|''
name|'def'
name|'__remove_from_all'
op|'('
name|'self'
op|','
name|'uid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove user from all roles and projects"""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'__user_exists'
op|'('
name|'uid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"User %s can\'t be removed from all "'
nl|'\n'
string|'"because the user doesn\'t exist"'
op|'%'
op|'('
name|'uid'
op|','
op|')'
op|')'
newline|'\n'
dedent|''
name|'role_dns'
op|'='
name|'self'
op|'.'
name|'__find_group_dns_with_member'
op|'('
nl|'\n'
name|'FLAGS'
op|'.'
name|'role_project_subtree'
op|','
name|'uid'
op|')'
newline|'\n'
name|'for'
name|'role_dn'
name|'in'
name|'role_dns'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'__safe_remove_from_group'
op|'('
name|'uid'
op|','
name|'role_dn'
op|')'
newline|'\n'
dedent|''
name|'project_dns'
op|'='
name|'self'
op|'.'
name|'__find_group_dns_with_member'
op|'('
nl|'\n'
name|'FLAGS'
op|'.'
name|'ldap_project_subtree'
op|','
name|'uid'
op|')'
newline|'\n'
name|'for'
name|'project_dn'
name|'in'
name|'project_dns'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'__safe_remove_from_group'
op|'('
name|'uid'
op|','
name|'project_dn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__delete_group
dedent|''
dedent|''
name|'def'
name|'__delete_group'
op|'('
name|'self'
op|','
name|'group_dn'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete Group"""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'__group_exists'
op|'('
name|'group_dn'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"Group at dn %s doesn\'t exist"'
op|'%'
name|'group_dn'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'conn'
op|'.'
name|'delete_s'
op|'('
name|'group_dn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__delete_roles
dedent|''
name|'def'
name|'__delete_roles'
op|'('
name|'self'
op|','
name|'project_dn'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete all roles for project"""'
newline|'\n'
name|'for'
name|'role_dn'
name|'in'
name|'self'
op|'.'
name|'__find_role_dns'
op|'('
name|'project_dn'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'__delete_group'
op|'('
name|'role_dn'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|__to_user
name|'def'
name|'__to_user'
op|'('
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert ldap attributes to User object"""'
newline|'\n'
name|'if'
name|'attr'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'attr'
op|'['
string|"'uid'"
op|']'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'attr'
op|'['
string|"'cn'"
op|']'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'access'"
op|':'
name|'attr'
op|'['
string|"'accessKey'"
op|']'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'secret'"
op|':'
name|'attr'
op|'['
string|"'secretKey'"
op|']'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'admin'"
op|':'
op|'('
name|'attr'
op|'['
string|"'isAdmin'"
op|']'
op|'['
number|'0'
op|']'
op|'=='
string|"'TRUE'"
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__to_project
dedent|''
name|'def'
name|'__to_project'
op|'('
name|'self'
op|','
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert ldap attributes to Project object"""'
newline|'\n'
name|'if'
name|'attr'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'member_dns'
op|'='
name|'attr'
op|'.'
name|'get'
op|'('
string|"'member'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'attr'
op|'['
string|"'cn'"
op|']'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'attr'
op|'['
string|"'cn'"
op|']'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'project_manager_id'"
op|':'
name|'self'
op|'.'
name|'__dn_to_uid'
op|'('
name|'attr'
op|'['
string|"'projectManager'"
op|']'
op|'['
number|'0'
op|']'
op|')'
op|','
nl|'\n'
string|"'description'"
op|':'
name|'attr'
op|'.'
name|'get'
op|'('
string|"'description'"
op|','
op|'['
name|'None'
op|']'
op|')'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'member_ids'"
op|':'
op|'['
name|'self'
op|'.'
name|'__dn_to_uid'
op|'('
name|'x'
op|')'
name|'for'
name|'x'
name|'in'
name|'member_dns'
op|']'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|__dn_to_uid
name|'def'
name|'__dn_to_uid'
op|'('
name|'dn'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert user dn to uid"""'
newline|'\n'
name|'return'
name|'dn'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'split'
op|'('
string|"'='"
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|__uid_to_dn
name|'def'
name|'__uid_to_dn'
op|'('
name|'dn'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert uid to dn"""'
newline|'\n'
name|'return'
string|"'uid=%s,%s'"
op|'%'
op|'('
name|'dn'
op|','
name|'FLAGS'
op|'.'
name|'ldap_user_subtree'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeLdapDriver
dedent|''
dedent|''
name|'class'
name|'FakeLdapDriver'
op|'('
name|'LdapDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fake Ldap Auth driver"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
comment|'# pylint: disable-msg=W0231'
newline|'\n'
indent|'        '
name|'__import__'
op|'('
string|"'nova.auth.fakeldap'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ldap'
op|'='
name|'sys'
op|'.'
name|'modules'
op|'['
string|"'nova.auth.fakeldap'"
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
