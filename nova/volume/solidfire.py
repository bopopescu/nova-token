begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
string|'"""\nDrivers for san-stored volumes.\n\nThe unique thing about a SAN is that we don\'t expect that we can run the volume\ncontroller on the SAN hardware.  We expect to access it over SSH or some API.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'httplib'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
name|'import'
name|'uuid'
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
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
op|'.'
name|'san'
name|'import'
name|'SanISCSIDriver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|sf_opts
name|'sf_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'sf_emulate_512'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set 512 byte emulation on volume creation; '"
op|')'
op|','
nl|'\n'
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'sf_mvip'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'IP address of SolidFire MVIP'"
op|')'
op|','
nl|'\n'
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'sf_login'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'admin'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Username for SF Cluster Admin'"
op|')'
op|','
nl|'\n'
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'sf_password'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Password for SF Cluster Admin'"
op|')'
op|','
nl|'\n'
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'sf_allow_tenant_qos'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Allow tenants to specify QOS on create'"
op|')'
op|','
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'sf_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SolidFire
name|'class'
name|'SolidFire'
op|'('
name|'SanISCSIDriver'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|sf_qos_dict
indent|'    '
name|'sf_qos_dict'
op|'='
op|'{'
string|"'slow'"
op|':'
op|'{'
string|"'minIOPS'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'maxIOPS'"
op|':'
number|'200'
op|','
nl|'\n'
string|"'burstIOPS'"
op|':'
number|'200'
op|'}'
op|','
nl|'\n'
string|"'medium'"
op|':'
op|'{'
string|"'minIOPS'"
op|':'
number|'200'
op|','
nl|'\n'
string|"'maxIOPS'"
op|':'
number|'400'
op|','
nl|'\n'
string|"'burstIOPS'"
op|':'
number|'400'
op|'}'
op|','
nl|'\n'
string|"'fast'"
op|':'
op|'{'
string|"'minIOPS'"
op|':'
number|'500'
op|','
nl|'\n'
string|"'maxIOPS'"
op|':'
number|'1000'
op|','
nl|'\n'
string|"'burstIOPS'"
op|':'
number|'1000'
op|'}'
op|','
nl|'\n'
string|"'performant'"
op|':'
op|'{'
string|"'minIOPS'"
op|':'
number|'2000'
op|','
nl|'\n'
string|"'maxIOPS'"
op|':'
number|'4000'
op|','
nl|'\n'
string|"'burstIOPS'"
op|':'
number|'4000'
op|'}'
op|','
nl|'\n'
string|"'off'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'super'
op|'('
name|'SolidFire'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_issue_api_request
dedent|''
name|'def'
name|'_issue_api_request'
op|'('
name|'self'
op|','
name|'method_name'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""All API requests to SolidFire device go through this method\n\n        Simple json-rpc web based API calls.\n        each call takes a set of paramaters (dict)\n        and returns results in a dict as well.\n        """'
newline|'\n'
nl|'\n'
name|'host'
op|'='
name|'FLAGS'
op|'.'
name|'san_ip'
newline|'\n'
comment|'# For now 443 is the only port our server accepts requests on'
nl|'\n'
name|'port'
op|'='
number|'443'
newline|'\n'
nl|'\n'
comment|"# NOTE(john-griffith): Probably don't need this, but the idea is"
nl|'\n'
comment|'# we provide a request_id so we can correlate'
nl|'\n'
comment|'# responses with requests'
nl|'\n'
name|'request_id'
op|'='
name|'int'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
comment|'# just generate a random number'
newline|'\n'
nl|'\n'
name|'cluster_admin'
op|'='
name|'FLAGS'
op|'.'
name|'san_login'
newline|'\n'
name|'cluster_password'
op|'='
name|'FLAGS'
op|'.'
name|'san_password'
newline|'\n'
nl|'\n'
name|'command'
op|'='
op|'{'
string|"'method'"
op|':'
name|'method_name'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'request_id'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'params'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'command'
op|'['
string|"'params'"
op|']'
op|'='
name|'params'
newline|'\n'
nl|'\n'
dedent|''
name|'payload'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'command'
op|','
name|'ensure_ascii'
op|'='
name|'False'
op|')'
newline|'\n'
name|'payload'
op|'.'
name|'encode'
op|'('
string|"'utf-8'"
op|')'
newline|'\n'
comment|'# we use json-rpc, webserver needs to see json-rpc in header'
nl|'\n'
name|'header'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json-rpc; charset=utf-8'"
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'cluster_password'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
comment|'# base64.encodestring includes a newline character'
nl|'\n'
comment|'# in the result, make sure we strip it off'
nl|'\n'
indent|'            '
name|'auth_key'
op|'='
name|'base64'
op|'.'
name|'encodestring'
op|'('
string|"'%s:%s'"
op|'%'
op|'('
name|'cluster_admin'
op|','
nl|'\n'
name|'cluster_password'
op|')'
op|')'
op|'['
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
name|'header'
op|'['
string|"'Authorization'"
op|']'
op|'='
string|"'Basic %s'"
op|'%'
name|'auth_key'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Payload for SolidFire API call: %s"'
op|')'
op|','
name|'payload'
op|')'
newline|'\n'
name|'connection'
op|'='
name|'httplib'
op|'.'
name|'HTTPSConnection'
op|'('
name|'host'
op|','
name|'port'
op|')'
newline|'\n'
name|'connection'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/json-rpc/1.0'"
op|','
name|'payload'
op|','
name|'header'
op|')'
newline|'\n'
name|'response'
op|'='
name|'connection'
op|'.'
name|'getresponse'
op|'('
op|')'
newline|'\n'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'response'
op|'.'
name|'status'
op|'!='
number|'200'
op|':'
newline|'\n'
indent|'            '
name|'connection'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'SolidFireAPIException'
op|'('
name|'status'
op|'='
name|'response'
op|'.'
name|'status'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'='
name|'response'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'data'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'ValueError'
op|')'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'connection'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Call to json.loads() raised an exception: %s"'
op|')'
op|'%'
name|'exc'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'SfJsonEncodeFailure'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'connection'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Results of SolidFire API call: %s"'
op|')'
op|','
name|'data'
op|')'
newline|'\n'
name|'return'
name|'data'
newline|'\n'
nl|'\n'
DECL|member|_get_volumes_by_sfaccount
dedent|''
name|'def'
name|'_get_volumes_by_sfaccount'
op|'('
name|'self'
op|','
name|'account_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|"'accountID'"
op|':'
name|'account_id'
op|'}'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_issue_api_request'
op|'('
string|"'ListVolumesForAccount'"
op|','
name|'params'
op|')'
newline|'\n'
name|'if'
string|"'result'"
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'data'
op|'['
string|"'result'"
op|']'
op|'['
string|"'volumes'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_sfaccount_by_name
dedent|''
dedent|''
name|'def'
name|'_get_sfaccount_by_name'
op|'('
name|'self'
op|','
name|'sf_account_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sfaccount'
op|'='
name|'None'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'username'"
op|':'
name|'sf_account_name'
op|'}'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_issue_api_request'
op|'('
string|"'GetAccountByName'"
op|','
name|'params'
op|')'
newline|'\n'
name|'if'
string|"'result'"
name|'in'
name|'data'
name|'and'
string|"'account'"
name|'in'
name|'data'
op|'['
string|"'result'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Found solidfire account: %s'"
op|')'
op|','
name|'sf_account_name'
op|')'
newline|'\n'
name|'sfaccount'
op|'='
name|'data'
op|'['
string|"'result'"
op|']'
op|'['
string|"'account'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'sfaccount'
newline|'\n'
nl|'\n'
DECL|member|_create_sfaccount
dedent|''
name|'def'
name|'_create_sfaccount'
op|'('
name|'self'
op|','
name|'nova_project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create account on SolidFire device if it doesn\'t already exist.\n\n        We\'re first going to check if the account already exits, if it does\n        just return it.  If not, then create it.\n        """'
newline|'\n'
nl|'\n'
name|'sf_account_name'
op|'='
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|'+'
string|"'-'"
op|'+'
name|'nova_project_id'
newline|'\n'
name|'sfaccount'
op|'='
name|'self'
op|'.'
name|'_get_sfaccount_by_name'
op|'('
name|'sf_account_name'
op|')'
newline|'\n'
name|'if'
name|'sfaccount'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'solidfire account: %s does not exist, create it...'"
op|')'
op|','
nl|'\n'
name|'sf_account_name'
op|')'
newline|'\n'
name|'chap_secret'
op|'='
name|'self'
op|'.'
name|'_generate_random_string'
op|'('
number|'12'
op|')'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'username'"
op|':'
name|'sf_account_name'
op|','
nl|'\n'
string|"'initiatorSecret'"
op|':'
name|'chap_secret'
op|','
nl|'\n'
string|"'targetSecret'"
op|':'
name|'chap_secret'
op|','
nl|'\n'
string|"'attributes'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_issue_api_request'
op|'('
string|"'AddAccount'"
op|','
name|'params'
op|')'
newline|'\n'
name|'if'
string|"'result'"
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                '
name|'sfaccount'
op|'='
name|'self'
op|'.'
name|'_get_sfaccount_by_name'
op|'('
name|'sf_account_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'sfaccount'
newline|'\n'
nl|'\n'
DECL|member|_get_cluster_info
dedent|''
name|'def'
name|'_get_cluster_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_issue_api_request'
op|'('
string|"'GetClusterInfo'"
op|','
name|'params'
op|')'
newline|'\n'
name|'if'
string|"'result'"
name|'not'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'SolidFireAPIDataException'
op|'('
name|'data'
op|'='
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'data'
op|'['
string|"'result'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_do_export
dedent|''
name|'def'
name|'_do_export'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Gets the associated account, retrieves CHAP info and updates."""'
newline|'\n'
nl|'\n'
name|'sfaccount_name'
op|'='
string|"'%s-%s'"
op|'%'
op|'('
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|','
name|'volume'
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
name|'sfaccount'
op|'='
name|'self'
op|'.'
name|'_get_sfaccount_by_name'
op|'('
name|'sfaccount_name'
op|')'
newline|'\n'
nl|'\n'
name|'model_update'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'model_update'
op|'['
string|"'provider_auth'"
op|']'
op|'='
op|'('
string|"'CHAP %s %s'"
nl|'\n'
op|'%'
op|'('
name|'sfaccount'
op|'['
string|"'username'"
op|']'
op|','
nl|'\n'
name|'sfaccount'
op|'['
string|"'targetSecret'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'model_update'
newline|'\n'
nl|'\n'
DECL|member|_generate_random_string
dedent|''
name|'def'
name|'_generate_random_string'
op|'('
name|'self'
op|','
name|'length'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Generates random_string to use for CHAP password."""'
newline|'\n'
nl|'\n'
name|'char_set'
op|'='
name|'string'
op|'.'
name|'ascii_uppercase'
op|'+'
name|'string'
op|'.'
name|'digits'
newline|'\n'
name|'return'
string|"''"
op|'.'
name|'join'
op|'('
name|'random'
op|'.'
name|'sample'
op|'('
name|'char_set'
op|','
name|'length'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_volume_create
dedent|''
name|'def'
name|'_do_volume_create'
op|'('
name|'self'
op|','
name|'project_id'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cluster_info'
op|'='
name|'self'
op|'.'
name|'_get_cluster_info'
op|'('
op|')'
newline|'\n'
name|'iscsi_portal'
op|'='
name|'cluster_info'
op|'['
string|"'clusterInfo'"
op|']'
op|'['
string|"'svip'"
op|']'
op|'+'
string|"':3260'"
newline|'\n'
name|'sfaccount'
op|'='
name|'self'
op|'.'
name|'_create_sfaccount'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'chap_secret'
op|'='
name|'sfaccount'
op|'['
string|"'targetSecret'"
op|']'
newline|'\n'
nl|'\n'
name|'params'
op|'['
string|"'accountID'"
op|']'
op|'='
name|'sfaccount'
op|'['
string|"'accountID'"
op|']'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_issue_api_request'
op|'('
string|"'CreateVolume'"
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'result'"
name|'not'
name|'in'
name|'data'
name|'or'
string|"'volumeID'"
name|'not'
name|'in'
name|'data'
op|'['
string|"'result'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'SolidFireAPIDataException'
op|'('
name|'data'
op|'='
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'volume_id'
op|'='
name|'data'
op|'['
string|"'result'"
op|']'
op|'['
string|"'volumeID'"
op|']'
newline|'\n'
nl|'\n'
name|'volume_list'
op|'='
name|'self'
op|'.'
name|'_get_volumes_by_sfaccount'
op|'('
name|'sfaccount'
op|'['
string|"'accountID'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'iqn'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'v'
name|'in'
name|'volume_list'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'v'
op|'['
string|"'volumeID'"
op|']'
op|'=='
name|'volume_id'
op|':'
newline|'\n'
indent|'                '
name|'iqn'
op|'='
name|'v'
op|'['
string|"'iqn'"
op|']'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'model_update'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|'# NOTE(john-griffith): SF volumes are always at lun 0'
nl|'\n'
name|'model_update'
op|'['
string|"'provider_location'"
op|']'
op|'='
op|'('
string|"'%s %s %s'"
nl|'\n'
op|'%'
op|'('
name|'iscsi_portal'
op|','
name|'iqn'
op|','
number|'0'
op|')'
op|')'
newline|'\n'
name|'model_update'
op|'['
string|"'provider_auth'"
op|']'
op|'='
op|'('
string|"'CHAP %s %s'"
nl|'\n'
op|'%'
op|'('
name|'sfaccount'
op|'['
string|"'username'"
op|']'
op|','
nl|'\n'
name|'chap_secret'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'model_update'
newline|'\n'
nl|'\n'
DECL|member|create_volume
dedent|''
name|'def'
name|'create_volume'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create volume on SolidFire device.\n\n        The account is where CHAP settings are derived from, volume is\n        created and exported.  Note that the new volume is immediately ready\n        for use.\n\n        One caveat here is that an existing user account must be specified\n        in the API call to create a new volume.  We use a set algorithm to\n        determine account info based on passed in nova volume object.  First\n        we check to see if the account already exists (and use it), or if it\n        does not already exist, we\'ll go ahead and create it.\n\n        For now, we\'re just using very basic settings, QOS is\n        turned off, 512 byte emulation is off etc.  Will be\n        looking at extensions for these things later, or\n        this module can be hacked to suit needs.\n        """'
newline|'\n'
name|'GB'
op|'='
number|'1048576'
op|'*'
number|'1024'
newline|'\n'
name|'slice_count'
op|'='
number|'1'
newline|'\n'
name|'attributes'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'qos'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'qos_keys'
op|'='
op|'['
string|"'minIOPS'"
op|','
string|"'maxIOPS'"
op|','
string|"'burstIOPS'"
op|']'
newline|'\n'
name|'valid_presets'
op|'='
name|'self'
op|'.'
name|'sf_qos_dict'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'sf_allow_tenant_qos'
name|'and'
name|'volume'
op|'.'
name|'get'
op|'('
string|"'volume_metadata'"
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
nl|'\n'
comment|'#First look to see if they included a preset'
nl|'\n'
indent|'            '
name|'presets'
op|'='
op|'['
name|'i'
op|'.'
name|'value'
name|'for'
name|'i'
name|'in'
name|'volume'
op|'.'
name|'get'
op|'('
string|"'volume_metadata'"
op|')'
nl|'\n'
name|'if'
name|'i'
op|'.'
name|'key'
op|'=='
string|"'sf-qos'"
name|'and'
name|'i'
op|'.'
name|'value'
name|'in'
name|'valid_presets'
op|']'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'presets'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'len'
op|'('
name|'presets'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'More than one valid preset was '"
nl|'\n'
string|"'detected, using %s'"
op|')'
op|'%'
name|'presets'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'qos'
op|'='
name|'self'
op|'.'
name|'sf_qos_dict'
op|'['
name|'presets'
op|'['
number|'0'
op|']'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'#if there was no preset, look for explicit settings'
nl|'\n'
indent|'                '
name|'for'
name|'i'
name|'in'
name|'volume'
op|'.'
name|'get'
op|'('
string|"'volume_metadata'"
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'i'
op|'.'
name|'key'
name|'in'
name|'qos_keys'
op|':'
newline|'\n'
indent|'                        '
name|'qos'
op|'['
name|'i'
op|'.'
name|'key'
op|']'
op|'='
name|'int'
op|'('
name|'i'
op|'.'
name|'value'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'params'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'OS-VOLID-%s'"
op|'%'
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'accountID'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'sliceCount'"
op|':'
name|'slice_count'
op|','
nl|'\n'
string|"'totalSize'"
op|':'
name|'volume'
op|'['
string|"'size'"
op|']'
op|'*'
name|'GB'
op|','
nl|'\n'
string|"'enable512e'"
op|':'
name|'FLAGS'
op|'.'
name|'sf_emulate_512'
op|','
nl|'\n'
string|"'attributes'"
op|':'
name|'attributes'
op|','
nl|'\n'
string|"'qos'"
op|':'
name|'qos'
op|'}'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_do_volume_create'
op|'('
name|'volume'
op|'['
string|"'project_id'"
op|']'
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_volume
dedent|''
name|'def'
name|'delete_volume'
op|'('
name|'self'
op|','
name|'volume'
op|','
name|'is_snapshot'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete SolidFire Volume from device.\n\n        SolidFire allows multipe volumes with same name,\n        volumeID is what\'s guaranteed unique.\n\n        """'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Enter SolidFire delete_volume..."'
op|')'
op|')'
newline|'\n'
name|'sf_account_name'
op|'='
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|'+'
string|"'-'"
op|'+'
name|'volume'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
name|'sfaccount'
op|'='
name|'self'
op|'.'
name|'_get_sfaccount_by_name'
op|'('
name|'sf_account_name'
op|')'
newline|'\n'
name|'if'
name|'sfaccount'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'SfAccountNotFound'
op|'('
name|'account_name'
op|'='
name|'sf_account_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'params'
op|'='
op|'{'
string|"'accountID'"
op|':'
name|'sfaccount'
op|'['
string|"'accountID'"
op|']'
op|'}'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_issue_api_request'
op|'('
string|"'ListVolumesForAccount'"
op|','
name|'params'
op|')'
newline|'\n'
name|'if'
string|"'result'"
name|'not'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'SolidFireAPIDataException'
op|'('
name|'data'
op|'='
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'is_snapshot'
op|':'
newline|'\n'
indent|'            '
name|'seek'
op|'='
string|"'OS-SNAPID-%s'"
op|'%'
op|'('
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'seek'
op|'='
string|"'OS-VOLID-%s'"
op|'%'
name|'volume'
op|'['
string|"'id'"
op|']'
newline|'\n'
comment|"#params = {'name': 'OS-VOLID-:%s' % volume['id'],"
nl|'\n'
nl|'\n'
dedent|''
name|'found_count'
op|'='
number|'0'
newline|'\n'
name|'volid'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'for'
name|'v'
name|'in'
name|'data'
op|'['
string|"'result'"
op|']'
op|'['
string|"'volumes'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'v'
op|'['
string|"'name'"
op|']'
op|'=='
name|'seek'
op|':'
newline|'\n'
indent|'                '
name|'found_count'
op|'+='
number|'1'
newline|'\n'
name|'volid'
op|'='
name|'v'
op|'['
string|"'volumeID'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'found_count'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'VolumeNotFound'
op|'('
name|'volume_id'
op|'='
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'found_count'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Deleting volumeID: %s"'
op|')'
op|','
name|'volid'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'DuplicateSfVolumeNames'
op|'('
name|'vol_name'
op|'='
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'params'
op|'='
op|'{'
string|"'volumeID'"
op|':'
name|'volid'
op|'}'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_issue_api_request'
op|'('
string|"'DeleteVolume'"
op|','
name|'params'
op|')'
newline|'\n'
name|'if'
string|"'result'"
name|'not'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'SolidFireAPIDataException'
op|'('
name|'data'
op|'='
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Leaving SolidFire delete_volume"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|ensure_export
dedent|''
name|'def'
name|'ensure_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Executing SolidFire ensure_export..."'
op|')'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_do_export'
op|'('
name|'volume'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_export
dedent|''
name|'def'
name|'create_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Executing SolidFire create_export..."'
op|')'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_do_export'
op|'('
name|'volume'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_create_snapshot
dedent|''
name|'def'
name|'_do_create_snapshot'
op|'('
name|'self'
op|','
name|'snapshot'
op|','
name|'snapshot_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a snapshot."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Enter SolidFire create_snapshot..."'
op|')'
op|')'
newline|'\n'
name|'sf_account_name'
op|'='
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|'+'
string|"'-'"
op|'+'
name|'snapshot'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
name|'sfaccount'
op|'='
name|'self'
op|'.'
name|'_get_sfaccount_by_name'
op|'('
name|'sf_account_name'
op|')'
newline|'\n'
name|'if'
name|'sfaccount'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'SfAccountNotFound'
op|'('
name|'account_name'
op|'='
name|'sf_account_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'params'
op|'='
op|'{'
string|"'accountID'"
op|':'
name|'sfaccount'
op|'['
string|"'accountID'"
op|']'
op|'}'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_issue_api_request'
op|'('
string|"'ListVolumesForAccount'"
op|','
name|'params'
op|')'
newline|'\n'
name|'if'
string|"'result'"
name|'not'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'SolidFireAPIDataException'
op|'('
name|'data'
op|'='
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'found_count'
op|'='
number|'0'
newline|'\n'
name|'volid'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'for'
name|'v'
name|'in'
name|'data'
op|'['
string|"'result'"
op|']'
op|'['
string|"'volumes'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'v'
op|'['
string|"'name'"
op|']'
op|'=='
string|"'OS-VOLID-%s'"
op|'%'
name|'snapshot'
op|'['
string|"'volume_id'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'found_count'
op|'+='
number|'1'
newline|'\n'
name|'volid'
op|'='
name|'v'
op|'['
string|"'volumeID'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'found_count'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'VolumeNotFound'
op|'('
name|'volume_id'
op|'='
name|'snapshot'
op|'['
string|"'volume_id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'found_count'
op|'!='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'DuplicateSfVolumeNames'
op|'('
nl|'\n'
name|'vol_name'
op|'='
string|"'OS-VOLID-%s'"
op|'%'
name|'snapshot'
op|'['
string|"'volume_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'params'
op|'='
op|'{'
string|"'volumeID'"
op|':'
name|'int'
op|'('
name|'volid'
op|')'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'snapshot_name'
op|','
nl|'\n'
string|"'attributes'"
op|':'
op|'{'
string|"'OriginatingVolume'"
op|':'
name|'volid'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_issue_api_request'
op|'('
string|"'CloneVolume'"
op|','
name|'params'
op|')'
newline|'\n'
name|'if'
string|"'result'"
name|'not'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'SolidFireAPIDataException'
op|'('
name|'data'
op|'='
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
name|'data'
op|','
name|'sfaccount'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_snapshot
dedent|''
name|'def'
name|'delete_snapshot'
op|'('
name|'self'
op|','
name|'snapshot'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'delete_volume'
op|'('
name|'snapshot'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_snapshot
dedent|''
name|'def'
name|'create_snapshot'
op|'('
name|'self'
op|','
name|'snapshot'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'snapshot_name'
op|'='
string|"'OS-SNAPID-%s'"
op|'%'
op|'('
nl|'\n'
name|'snapshot'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
op|'('
name|'data'
op|','
name|'sf_account'
op|')'
op|'='
name|'self'
op|'.'
name|'_do_create_snapshot'
op|'('
name|'snapshot'
op|','
name|'snapshot_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_volume_from_snapshot
dedent|''
name|'def'
name|'create_volume_from_snapshot'
op|'('
name|'self'
op|','
name|'volume'
op|','
name|'snapshot'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cluster_info'
op|'='
name|'self'
op|'.'
name|'_get_cluster_info'
op|'('
op|')'
newline|'\n'
name|'iscsi_portal'
op|'='
name|'cluster_info'
op|'['
string|"'clusterInfo'"
op|']'
op|'['
string|"'svip'"
op|']'
op|'+'
string|"':3260'"
newline|'\n'
name|'sfaccount'
op|'='
name|'self'
op|'.'
name|'_create_sfaccount'
op|'('
name|'snapshot'
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
name|'chap_secret'
op|'='
name|'sfaccount'
op|'['
string|"'targetSecret'"
op|']'
newline|'\n'
name|'snapshot_name'
op|'='
string|"'OS-VOLID-%s'"
op|'%'
name|'volume'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
op|'('
name|'data'
op|','
name|'sf_account'
op|')'
op|'='
name|'self'
op|'.'
name|'_do_create_snapshot'
op|'('
name|'snapshot'
op|','
name|'snapshot_name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'result'"
name|'not'
name|'in'
name|'data'
name|'or'
string|"'volumeID'"
name|'not'
name|'in'
name|'data'
op|'['
string|"'result'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'SolidFireAPIDataException'
op|'('
name|'data'
op|'='
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'volume_id'
op|'='
name|'data'
op|'['
string|"'result'"
op|']'
op|'['
string|"'volumeID'"
op|']'
newline|'\n'
name|'volume_list'
op|'='
name|'self'
op|'.'
name|'_get_volumes_by_sfaccount'
op|'('
name|'sf_account'
op|'['
string|"'accountID'"
op|']'
op|')'
newline|'\n'
name|'iqn'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'v'
name|'in'
name|'volume_list'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'v'
op|'['
string|"'volumeID'"
op|']'
op|'=='
name|'volume_id'
op|':'
newline|'\n'
indent|'                '
name|'iqn'
op|'='
name|'v'
op|'['
string|"'iqn'"
op|']'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'model_update'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|'# NOTE(john-griffith): SF volumes are always at lun 0'
nl|'\n'
name|'model_update'
op|'['
string|"'provider_location'"
op|']'
op|'='
op|'('
string|"'%s %s %s'"
nl|'\n'
op|'%'
op|'('
name|'iscsi_portal'
op|','
name|'iqn'
op|','
number|'0'
op|')'
op|')'
newline|'\n'
name|'model_update'
op|'['
string|"'provider_auth'"
op|']'
op|'='
op|'('
string|"'CHAP %s %s'"
nl|'\n'
op|'%'
op|'('
name|'sfaccount'
op|'['
string|"'username'"
op|']'
op|','
nl|'\n'
name|'chap_secret'
op|')'
op|')'
newline|'\n'
name|'return'
name|'model_update'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
