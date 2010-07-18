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
DECL|class|UserInfo
name|'class'
name|'UserInfo'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Information about a Nova user, as parsed through SAX\n    fields include:\n        username\n        accesskey\n        secretkey\n\n    and an optional field containing a zip with X509 cert & rc\n        file\n    """'
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
string|'"""\n    Information about a Nova Host, as parsed through SAX:\n        Disk stats\n        Running Instances\n        Memory stats\n        CPU stats\n        Network address info\n        Firewall info\n        Bridge and devices\n    """'
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
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'clc_ip'
op|'='
string|"'127.0.0.1'"
op|','
name|'region'
op|'='
string|"'nova'"
op|','
name|'access_key'
op|'='
string|"'admin'"
op|','
nl|'\n'
name|'secret_key'
op|'='
string|"'admin'"
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'clc_ip'
op|'='
name|'clc_ip'
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
name|'False'
op|','
nl|'\n'
name|'region'
op|'='
name|'RegionInfo'
op|'('
name|'None'
op|','
name|'region'
op|','
name|'clc_ip'
op|')'
op|','
nl|'\n'
name|'port'
op|'='
number|'8773'
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
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Returns a boto ec2 connection for the given username.\n        """'
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
name|'return'
name|'boto'
op|'.'
name|'connect_ec2'
op|'('
nl|'\n'
name|'aws_access_key_id'
op|'='
name|'user'
op|'.'
name|'accesskey'
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
name|'False'
op|','
nl|'\n'
name|'region'
op|'='
name|'RegionInfo'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'region'
op|','
name|'self'
op|'.'
name|'clc_ip'
op|')'
op|','
nl|'\n'
name|'port'
op|'='
number|'8773'
op|','
nl|'\n'
name|'path'
op|'='
string|"'/services/Cloud'"
op|','
nl|'\n'
op|'**'
name|'kwargs'
nl|'\n'
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
string|'""" grabs the list of all users """'
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
string|'""" grab a single user by name """'
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
name|'UserInfo'
op|')'
newline|'\n'
nl|'\n'
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
string|'""" determine if user exists """'
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
string|'""" creates a new user, returning the userinfo object with access/secret """'
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
string|'""" deletes a user """'
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
name|'UserInfo'
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
name|'username'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" returns the content of a zip file containing novarc and access credentials. """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'apiconn'
op|'.'
name|'get_object'
op|'('
string|"'GenerateX509ForUser'"
op|','
op|'{'
string|"'Name'"
op|':'
name|'username'
op|'}'
op|','
name|'UserInfo'
op|')'
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
dedent|''
dedent|''
endmarker|''
end_unit
