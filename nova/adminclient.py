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
string|'"""\nNova User API client library.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'boto'
newline|'\n'
name|'import'
name|'httplib'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'regioninfo'
name|'import'
name|'RegionInfo'
newline|'\n'
nl|'\n'
DECL|class|ConsoleInfo
name|'class'
name|'ConsoleInfo'
op|'('
name|'object'
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
name|'connection'
op|'='
name|'None'
op|','
name|'endpoint'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection'
newline|'\n'
name|'self'
op|'.'
name|'endpoint'
op|'='
name|'endpoint'
newline|'\n'
nl|'\n'
DECL|member|startElement
dedent|''
name|'def'
name|'startElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'attrs'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|endElement
dedent|''
name|'def'
name|'endElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'url'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'url'
op|'='
name|'str'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'name'
op|'=='
string|"'kind'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'url'
op|'='
name|'str'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
dedent|''
dedent|''
dedent|''
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|DEFAULT_CLC_URL
name|'DEFAULT_CLC_URL'
op|'='
string|"'http://127.0.0.1:8773'"
newline|'\n'
DECL|variable|DEFAULT_REGION
name|'DEFAULT_REGION'
op|'='
string|"'nova'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UserInfo
name|'class'
name|'UserInfo'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Information about a Nova user, as parsed through SAX.\n\n    **Fields Include**\n\n    * username\n    * accesskey\n    * secretkey\n    * file (optional) containing zip of X509 cert & rc file\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|','
name|'username'
op|'='
name|'None'
op|','
name|'endpoint'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection'
newline|'\n'
name|'self'
op|'.'
name|'username'
op|'='
name|'username'
newline|'\n'
name|'self'
op|'.'
name|'endpoint'
op|'='
name|'endpoint'
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
string|"'UserInfo:%s'"
op|'%'
name|'self'
op|'.'
name|'username'
newline|'\n'
nl|'\n'
DECL|member|startElement
dedent|''
name|'def'
name|'startElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'attrs'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|endElement
dedent|''
name|'def'
name|'endElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'username'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'username'
op|'='
name|'str'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'file'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'file'
op|'='
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'str'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'accesskey'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'accesskey'
op|'='
name|'str'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'secretkey'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'secretkey'
op|'='
name|'str'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UserRole
dedent|''
dedent|''
dedent|''
name|'class'
name|'UserRole'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Information about a Nova user\'s role, as parsed through SAX.\n\n    **Fields include**\n\n    * role\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection'
newline|'\n'
name|'self'
op|'.'
name|'role'
op|'='
name|'None'
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
string|"'UserRole:%s'"
op|'%'
name|'self'
op|'.'
name|'role'
newline|'\n'
nl|'\n'
DECL|member|startElement
dedent|''
name|'def'
name|'startElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'attrs'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|endElement
dedent|''
name|'def'
name|'endElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'role'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'role'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'str'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProjectInfo
dedent|''
dedent|''
dedent|''
name|'class'
name|'ProjectInfo'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Information about a Nova project, as parsed through SAX.\n\n    **Fields include**\n\n    * projectname\n    * description\n    * projectManagerId\n    * memberIds\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection'
newline|'\n'
name|'self'
op|'.'
name|'projectname'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'description'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'projectManagerId'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'memberIds'
op|'='
op|'['
op|']'
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
string|"'ProjectInfo:%s'"
op|'%'
name|'self'
op|'.'
name|'projectname'
newline|'\n'
nl|'\n'
DECL|member|startElement
dedent|''
name|'def'
name|'startElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'attrs'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|endElement
dedent|''
name|'def'
name|'endElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'projectname'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'projectname'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'description'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'description'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'projectManagerId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'projectManagerId'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'memberId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'memberIds'
op|'.'
name|'append'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'str'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProjectMember
dedent|''
dedent|''
dedent|''
name|'class'
name|'ProjectMember'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Information about a Nova project member, as parsed through SAX.\n\n    **Fields include**\n\n    * memberId\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection'
newline|'\n'
name|'self'
op|'.'
name|'memberId'
op|'='
name|'None'
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
string|"'ProjectMember:%s'"
op|'%'
name|'self'
op|'.'
name|'memberId'
newline|'\n'
nl|'\n'
DECL|member|startElement
dedent|''
name|'def'
name|'startElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'attrs'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|endElement
dedent|''
name|'def'
name|'endElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'member'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'memberId'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'str'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostInfo
dedent|''
dedent|''
dedent|''
name|'class'
name|'HostInfo'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Information about a Nova Host, as parsed through SAX.\n\n    **Fields Include**\n\n    * Disk stats\n    * Running Instances\n    * Memory stats\n    * CPU stats\n    * Network address info\n    * Firewall info\n    * Bridge and devices\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection'
newline|'\n'
name|'self'
op|'.'
name|'hostname'
op|'='
name|'None'
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
string|"'Host:%s'"
op|'%'
name|'self'
op|'.'
name|'hostname'
newline|'\n'
nl|'\n'
comment|'# this is needed by the sax parser, so ignore the ugly name'
nl|'\n'
DECL|member|startElement
dedent|''
name|'def'
name|'startElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'attrs'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
comment|'# this is needed by the sax parser, so ignore the ugly name'
nl|'\n'
DECL|member|endElement
dedent|''
name|'def'
name|'endElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'setattr'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaAdminClient
dedent|''
dedent|''
name|'class'
name|'NovaAdminClient'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
nl|'\n'
name|'self'
op|','
nl|'\n'
name|'clc_url'
op|'='
name|'DEFAULT_CLC_URL'
op|','
nl|'\n'
name|'region'
op|'='
name|'DEFAULT_REGION'
op|','
nl|'\n'
name|'access_key'
op|'='
name|'FLAGS'
op|'.'
name|'aws_access_key_id'
op|','
nl|'\n'
name|'secret_key'
op|'='
name|'FLAGS'
op|'.'
name|'aws_secret_access_key'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'parts'
op|'='
name|'self'
op|'.'
name|'split_clc_url'
op|'('
name|'clc_url'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'clc_url'
op|'='
name|'clc_url'
newline|'\n'
name|'self'
op|'.'
name|'region'
op|'='
name|'region'
newline|'\n'
name|'self'
op|'.'
name|'access'
op|'='
name|'access_key'
newline|'\n'
name|'self'
op|'.'
name|'secret'
op|'='
name|'secret_key'
newline|'\n'
name|'self'
op|'.'
name|'apiconn'
op|'='
name|'boto'
op|'.'
name|'connect_ec2'
op|'('
name|'aws_access_key_id'
op|'='
name|'access_key'
op|','
nl|'\n'
name|'aws_secret_access_key'
op|'='
name|'secret_key'
op|','
nl|'\n'
name|'is_secure'
op|'='
name|'parts'
op|'['
string|"'is_secure'"
op|']'
op|','
nl|'\n'
name|'region'
op|'='
name|'RegionInfo'
op|'('
name|'None'
op|','
nl|'\n'
name|'region'
op|','
nl|'\n'
name|'parts'
op|'['
string|"'ip'"
op|']'
op|')'
op|','
nl|'\n'
name|'port'
op|'='
name|'parts'
op|'['
string|"'port'"
op|']'
op|','
nl|'\n'
name|'path'
op|'='
string|"'/services/Admin'"
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'APIVersion'
op|'='
string|"'nova'"
newline|'\n'
nl|'\n'
DECL|member|connection_for
dedent|''
name|'def'
name|'connection_for'
op|'('
name|'self'
op|','
name|'username'
op|','
name|'project'
op|','
name|'clc_url'
op|'='
name|'None'
op|','
name|'region'
op|'='
name|'None'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a boto ec2 connection for the given username."""'
newline|'\n'
name|'if'
name|'not'
name|'clc_url'
op|':'
newline|'\n'
indent|'            '
name|'clc_url'
op|'='
name|'self'
op|'.'
name|'clc_url'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'region'
op|':'
newline|'\n'
indent|'            '
name|'region'
op|'='
name|'self'
op|'.'
name|'region'
newline|'\n'
dedent|''
name|'parts'
op|'='
name|'self'
op|'.'
name|'split_clc_url'
op|'('
name|'clc_url'
op|')'
newline|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'get_user'
op|'('
name|'username'
op|')'
newline|'\n'
name|'access_key'
op|'='
string|"'%s:%s'"
op|'%'
op|'('
name|'user'
op|'.'
name|'accesskey'
op|','
name|'project'
op|')'
newline|'\n'
name|'return'
name|'boto'
op|'.'
name|'connect_ec2'
op|'('
name|'aws_access_key_id'
op|'='
name|'access_key'
op|','
nl|'\n'
name|'aws_secret_access_key'
op|'='
name|'user'
op|'.'
name|'secretkey'
op|','
nl|'\n'
name|'is_secure'
op|'='
name|'parts'
op|'['
string|"'is_secure'"
op|']'
op|','
nl|'\n'
name|'region'
op|'='
name|'RegionInfo'
op|'('
name|'None'
op|','
nl|'\n'
name|'self'
op|'.'
name|'region'
op|','
nl|'\n'
name|'parts'
op|'['
string|"'ip'"
op|']'
op|')'
op|','
nl|'\n'
name|'port'
op|'='
name|'parts'
op|'['
string|"'port'"
op|']'
op|','
nl|'\n'
name|'path'
op|'='
string|"'/services/Cloud'"
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|split_clc_url
dedent|''
name|'def'
name|'split_clc_url'
op|'('
name|'self'
op|','
name|'clc_url'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Splits a cloud controller endpoint url."""'
newline|'\n'
name|'parts'
op|'='
name|'httplib'
op|'.'
name|'urlsplit'
op|'('
name|'clc_url'
op|')'
newline|'\n'
name|'is_secure'
op|'='
name|'parts'
op|'.'
name|'scheme'
op|'=='
string|"'https'"
newline|'\n'
name|'ip'
op|','
name|'port'
op|'='
name|'parts'
op|'.'
name|'netloc'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'ip'"
op|':'
name|'ip'
op|','
string|"'port'"
op|':'
name|'int'
op|'('
name|'port'
op|')'
op|','
string|"'is_secure'"
op|':'
name|'is_secure'
op|'}'
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
string|'"""Grabs the list of all users."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_list'
op|'('
string|"'DescribeUsers'"
op|','
op|'{'
op|'}'
op|','
op|'['
op|'('
string|"'item'"
op|','
name|'UserInfo'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_user
dedent|''
name|'def'
name|'get_user'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Grab a single user by name."""'
newline|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_object'
op|'('
string|"'DescribeUser'"
op|','
op|'{'
string|"'Name'"
op|':'
name|'name'
op|'}'
op|','
nl|'\n'
name|'UserInfo'
op|')'
newline|'\n'
name|'if'
name|'user'
op|'.'
name|'username'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'user'
newline|'\n'
nl|'\n'
DECL|member|has_user
dedent|''
dedent|''
name|'def'
name|'has_user'
op|'('
name|'self'
op|','
name|'username'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Determine if user exists."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'get_user'
op|'('
name|'username'
op|')'
op|'!='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|create_user
dedent|''
name|'def'
name|'create_user'
op|'('
name|'self'
op|','
name|'username'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a new user, returning the userinfo object with\n        access/secret."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_object'
op|'('
string|"'RegisterUser'"
op|','
op|'{'
string|"'Name'"
op|':'
name|'username'
op|'}'
op|','
nl|'\n'
name|'UserInfo'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_user
dedent|''
name|'def'
name|'delete_user'
op|'('
name|'self'
op|','
name|'username'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes a user."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_object'
op|'('
string|"'DeregisterUser'"
op|','
op|'{'
string|"'Name'"
op|':'
name|'username'
op|'}'
op|','
nl|'\n'
name|'UserInfo'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_roles
dedent|''
name|'def'
name|'get_roles'
op|'('
name|'self'
op|','
name|'project_roles'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of available roles."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_list'
op|'('
string|"'DescribeRoles'"
op|','
nl|'\n'
op|'{'
string|"'ProjectRoles'"
op|':'
name|'project_roles'
op|'}'
op|','
nl|'\n'
op|'['
op|'('
string|"'item'"
op|','
name|'UserRole'
op|')'
op|']'
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
name|'user'
op|','
name|'project'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of roles for the given user.\n\n        Omitting project will return any global roles that the user has.\n        Specifying project will return only project specific roles.\n\n        """'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'User'"
op|':'
name|'user'
op|'}'
newline|'\n'
name|'if'
name|'project'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'Project'"
op|']'
op|'='
name|'project'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_list'
op|'('
string|"'DescribeUserRoles'"
op|','
nl|'\n'
name|'params'
op|','
nl|'\n'
op|'['
op|'('
string|"'item'"
op|','
name|'UserRole'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_user_role
dedent|''
name|'def'
name|'add_user_role'
op|'('
name|'self'
op|','
name|'user'
op|','
name|'role'
op|','
name|'project'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add a role to a user either globally or for a specific project."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'modify_user_role'
op|'('
name|'user'
op|','
name|'role'
op|','
name|'project'
op|'='
name|'project'
op|','
nl|'\n'
name|'operation'
op|'='
string|"'add'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_user_role
dedent|''
name|'def'
name|'remove_user_role'
op|'('
name|'self'
op|','
name|'user'
op|','
name|'role'
op|','
name|'project'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove a role from a user either globally or for a specific\n        project."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'modify_user_role'
op|'('
name|'user'
op|','
name|'role'
op|','
name|'project'
op|'='
name|'project'
op|','
nl|'\n'
name|'operation'
op|'='
string|"'remove'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|modify_user_role
dedent|''
name|'def'
name|'modify_user_role'
op|'('
name|'self'
op|','
name|'user'
op|','
name|'role'
op|','
name|'project'
op|'='
name|'None'
op|','
name|'operation'
op|'='
string|"'add'"
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add or remove a role for a user and project."""'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'User'"
op|':'
name|'user'
op|','
nl|'\n'
string|"'Role'"
op|':'
name|'role'
op|','
nl|'\n'
string|"'Project'"
op|':'
name|'project'
op|','
nl|'\n'
string|"'Operation'"
op|':'
name|'operation'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_status'
op|'('
string|"'ModifyUserRole'"
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_projects
dedent|''
name|'def'
name|'get_projects'
op|'('
name|'self'
op|','
name|'user'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of all projects."""'
newline|'\n'
name|'if'
name|'user'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
op|'{'
string|"'User'"
op|':'
name|'user'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_list'
op|'('
string|"'DescribeProjects'"
op|','
nl|'\n'
name|'params'
op|','
nl|'\n'
op|'['
op|'('
string|"'item'"
op|','
name|'ProjectInfo'
op|')'
op|']'
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
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a single project with the specified name."""'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_object'
op|'('
string|"'DescribeProject'"
op|','
nl|'\n'
op|'{'
string|"'Name'"
op|':'
name|'name'
op|'}'
op|','
nl|'\n'
name|'ProjectInfo'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'project'
op|'.'
name|'projectname'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'project'
newline|'\n'
nl|'\n'
DECL|member|create_project
dedent|''
dedent|''
name|'def'
name|'create_project'
op|'('
name|'self'
op|','
name|'projectname'
op|','
name|'manager_user'
op|','
name|'description'
op|'='
name|'None'
op|','
nl|'\n'
name|'member_users'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a new project."""'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'Name'"
op|':'
name|'projectname'
op|','
nl|'\n'
string|"'ManagerUser'"
op|':'
name|'manager_user'
op|','
nl|'\n'
string|"'Description'"
op|':'
name|'description'
op|','
nl|'\n'
string|"'MemberUsers'"
op|':'
name|'member_users'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_object'
op|'('
string|"'RegisterProject'"
op|','
name|'params'
op|','
name|'ProjectInfo'
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
name|'projectname'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Permanently deletes the specified project."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_object'
op|'('
string|"'DeregisterProject'"
op|','
nl|'\n'
op|'{'
string|"'Name'"
op|':'
name|'projectname'
op|'}'
op|','
nl|'\n'
name|'ProjectInfo'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_project_members
dedent|''
name|'def'
name|'get_project_members'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of members of a project."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_list'
op|'('
string|"'DescribeProjectMembers'"
op|','
nl|'\n'
op|'{'
string|"'Name'"
op|':'
name|'name'
op|'}'
op|','
nl|'\n'
op|'['
op|'('
string|"'item'"
op|','
name|'ProjectMember'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_project_member
dedent|''
name|'def'
name|'add_project_member'
op|'('
name|'self'
op|','
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adds a user to a project."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'modify_project_member'
op|'('
name|'user'
op|','
name|'project'
op|','
name|'operation'
op|'='
string|"'add'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_project_member
dedent|''
name|'def'
name|'remove_project_member'
op|'('
name|'self'
op|','
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes a user from a project."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'modify_project_member'
op|'('
name|'user'
op|','
name|'project'
op|','
name|'operation'
op|'='
string|"'remove'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|modify_project_member
dedent|''
name|'def'
name|'modify_project_member'
op|'('
name|'self'
op|','
name|'user'
op|','
name|'project'
op|','
name|'operation'
op|'='
string|"'add'"
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adds or removes a user from a project."""'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'User'"
op|':'
name|'user'
op|','
nl|'\n'
string|"'Project'"
op|':'
name|'project'
op|','
nl|'\n'
string|"'Operation'"
op|':'
name|'operation'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_status'
op|'('
string|"'ModifyProjectMember'"
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_zip
dedent|''
name|'def'
name|'get_zip'
op|'('
name|'self'
op|','
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the content of a zip file containing novarc and access\n        credentials."""'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'Name'"
op|':'
name|'user'
op|','
string|"'Project'"
op|':'
name|'project'
op|'}'
newline|'\n'
name|'zip'
op|'='
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_object'
op|'('
string|"'GenerateX509ForUser'"
op|','
name|'params'
op|','
name|'UserInfo'
op|')'
newline|'\n'
name|'return'
name|'zip'
op|'.'
name|'file'
newline|'\n'
nl|'\n'
DECL|member|get_hosts
dedent|''
name|'def'
name|'get_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_list'
op|'('
string|"'DescribeHosts'"
op|','
op|'{'
op|'}'
op|','
op|'['
op|'('
string|"'item'"
op|','
name|'HostInfo'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_console
dedent|''
name|'def'
name|'create_console'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'kind'
op|'='
string|"'ajax'"
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create a console\n        """'
newline|'\n'
name|'console'
op|'='
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_object'
op|'('
string|"'CreateConsole'"
op|','
op|'{'
string|"'Kind'"
op|':'
name|'kind'
op|','
string|"'InstanceId'"
op|':'
name|'instance_id'
op|'}'
op|','
name|'ConsoleInfo'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'console'
op|'.'
name|'url'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'console'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
