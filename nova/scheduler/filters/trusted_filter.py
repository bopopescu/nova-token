begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 Intel, Inc.'
nl|'\n'
comment|'# Copyright (c) 2011-2012 OpenStack Foundation'
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
string|'"""\nFilter to add support for Trusted Computing Pools.\n\nFilter that only schedules tasks on a host if the integrity (trust)\nof that host matches the trust requested in the `extra_specs\' for the\nflavor.  The `extra_specs\' will contain a key/value pair where the\nkey is `trust\'.  The value of this pair (`trusted\'/`untrusted\') must\nmatch the integrity of that host (obtained from the Attestation\nservice) before the task can be scheduled on that host.\n\nNote that the parameters to control access to the Attestation Service\nare in the `nova.conf\' file in a separate `trust\' section.  For example,\nthe config file will look something like:\n\n    [DEFAULT]\n    verbose=True\n    ...\n    [trust]\n    server=attester.mynetwork.com\n\nDetails on the specific parameters can be found in the file `trust_attest.py\'.\n\nDetails on setting up and using an Attestation Service can be found at\nthe Open Attestation project at:\n\n    https://github.com/OpenAttestation/OpenAttestation\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'httplib'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'ssl'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
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
DECL|variable|trusted_opts
name|'trusted_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'attestation_server'"
op|','
nl|'\n'
comment|'# deprecated in Grizzly'
nl|'\n'
DECL|variable|deprecated_name
name|'deprecated_name'
op|'='
string|"'server'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'attestation server http'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'attestation_server_ca_file'"
op|','
nl|'\n'
DECL|variable|deprecated_name
name|'deprecated_name'
op|'='
string|"'server_ca_file'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'attestation server Cert file for Identity verification'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'attestation_port'"
op|','
nl|'\n'
DECL|variable|deprecated_name
name|'deprecated_name'
op|'='
string|"'port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'8443'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'attestation server port'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'attestation_api_url'"
op|','
nl|'\n'
DECL|variable|deprecated_name
name|'deprecated_name'
op|'='
string|"'api_url'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'/OpenAttestationWebServices/V1.0'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'attestation web API URL'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'attestation_auth_blob'"
op|','
nl|'\n'
DECL|variable|deprecated_name
name|'deprecated_name'
op|'='
string|"'auth_blob'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'attestation authorization blob - must change'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'attestation_auth_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Attestation status cache valid period length'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|trust_group
name|'trust_group'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
name|'name'
op|'='
string|"'trusted_computing'"
op|','
name|'title'
op|'='
string|"'Trust parameters'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_group'
op|'('
name|'trust_group'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'trusted_opts'
op|','
name|'group'
op|'='
name|'trust_group'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HTTPSClientAuthConnection
name|'class'
name|'HTTPSClientAuthConnection'
op|'('
name|'httplib'
op|'.'
name|'HTTPSConnection'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Class to make a HTTPS connection, with support for full client-based\n    SSL Authentication\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'port'
op|','
name|'key_file'
op|','
name|'cert_file'
op|','
name|'ca_file'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'httplib'
op|'.'
name|'HTTPSConnection'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
nl|'\n'
name|'key_file'
op|'='
name|'key_file'
op|','
nl|'\n'
name|'cert_file'
op|'='
name|'cert_file'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'port'
op|'='
name|'port'
newline|'\n'
name|'self'
op|'.'
name|'key_file'
op|'='
name|'key_file'
newline|'\n'
name|'self'
op|'.'
name|'cert_file'
op|'='
name|'cert_file'
newline|'\n'
name|'self'
op|'.'
name|'ca_file'
op|'='
name|'ca_file'
newline|'\n'
name|'self'
op|'.'
name|'timeout'
op|'='
name|'timeout'
newline|'\n'
nl|'\n'
DECL|member|connect
dedent|''
name|'def'
name|'connect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Connect to a host on a given (SSL) port.\n        If ca_file is pointing somewhere, use it to check Server Certificate.\n\n        Redefined/copied and extended from httplib.py:1105 (Python 2.6.x).\n        This is needed to pass cert_reqs=ssl.CERT_REQUIRED as parameter to\n        ssl.wrap_socket(), which forces SSL to check server certificate\n        against our client certificate.\n        """'
newline|'\n'
name|'sock'
op|'='
name|'socket'
op|'.'
name|'create_connection'
op|'('
op|'('
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'port'
op|')'
op|','
name|'self'
op|'.'
name|'timeout'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'sock'
op|'='
name|'ssl'
op|'.'
name|'wrap_socket'
op|'('
name|'sock'
op|','
name|'self'
op|'.'
name|'key_file'
op|','
name|'self'
op|'.'
name|'cert_file'
op|','
nl|'\n'
name|'ca_certs'
op|'='
name|'self'
op|'.'
name|'ca_file'
op|','
nl|'\n'
name|'cert_reqs'
op|'='
name|'ssl'
op|'.'
name|'CERT_REQUIRED'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AttestationService
dedent|''
dedent|''
name|'class'
name|'AttestationService'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
comment|'# Provide access wrapper to attestation server to get integrity report.'
nl|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'api_url'
op|'='
name|'CONF'
op|'.'
name|'trusted_computing'
op|'.'
name|'attestation_api_url'
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
name|'CONF'
op|'.'
name|'trusted_computing'
op|'.'
name|'attestation_server'
newline|'\n'
name|'self'
op|'.'
name|'port'
op|'='
name|'CONF'
op|'.'
name|'trusted_computing'
op|'.'
name|'attestation_port'
newline|'\n'
name|'self'
op|'.'
name|'auth_blob'
op|'='
name|'CONF'
op|'.'
name|'trusted_computing'
op|'.'
name|'attestation_auth_blob'
newline|'\n'
name|'self'
op|'.'
name|'key_file'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'cert_file'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'ca_file'
op|'='
name|'CONF'
op|'.'
name|'trusted_computing'
op|'.'
name|'attestation_server_ca_file'
newline|'\n'
name|'self'
op|'.'
name|'request_count'
op|'='
number|'100'
newline|'\n'
nl|'\n'
DECL|member|_do_request
dedent|''
name|'def'
name|'_do_request'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'action_url'
op|','
name|'body'
op|','
name|'headers'
op|')'
op|':'
newline|'\n'
comment|'# Connects to the server and issues a request.'
nl|'\n'
comment|'# :returns: result data'
nl|'\n'
comment|'# :raises: IOError if the request fails'
nl|'\n'
nl|'\n'
indent|'        '
name|'action_url'
op|'='
string|'"%s/%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'api_url'
op|','
name|'action_url'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'c'
op|'='
name|'HTTPSClientAuthConnection'
op|'('
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'port'
op|','
nl|'\n'
name|'key_file'
op|'='
name|'self'
op|'.'
name|'key_file'
op|','
nl|'\n'
name|'cert_file'
op|'='
name|'self'
op|'.'
name|'cert_file'
op|','
nl|'\n'
name|'ca_file'
op|'='
name|'self'
op|'.'
name|'ca_file'
op|')'
newline|'\n'
name|'c'
op|'.'
name|'request'
op|'('
name|'method'
op|','
name|'action_url'
op|','
name|'body'
op|','
name|'headers'
op|')'
newline|'\n'
name|'res'
op|'='
name|'c'
op|'.'
name|'getresponse'
op|'('
op|')'
newline|'\n'
name|'status_code'
op|'='
name|'res'
op|'.'
name|'status'
newline|'\n'
name|'if'
name|'status_code'
name|'in'
op|'('
name|'httplib'
op|'.'
name|'OK'
op|','
nl|'\n'
name|'httplib'
op|'.'
name|'CREATED'
op|','
nl|'\n'
name|'httplib'
op|'.'
name|'ACCEPTED'
op|','
nl|'\n'
name|'httplib'
op|'.'
name|'NO_CONTENT'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'httplib'
op|'.'
name|'OK'
op|','
name|'res'
newline|'\n'
dedent|''
name|'return'
name|'status_code'
op|','
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
op|'('
name|'socket'
op|'.'
name|'error'
op|','
name|'IOError'
op|')'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'IOError'
op|','
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_request
dedent|''
dedent|''
name|'def'
name|'_request'
op|'('
name|'self'
op|','
name|'cmd'
op|','
name|'subcmd'
op|','
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'body'
op|'['
string|"'count'"
op|']'
op|'='
name|'len'
op|'('
name|'hosts'
op|')'
newline|'\n'
name|'body'
op|'['
string|"'hosts'"
op|']'
op|'='
name|'hosts'
newline|'\n'
name|'cooked'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'headers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'auth_blob'
op|':'
newline|'\n'
indent|'            '
name|'headers'
op|'['
string|"'x-auth-blob'"
op|']'
op|'='
name|'self'
op|'.'
name|'auth_blob'
newline|'\n'
dedent|''
name|'status'
op|','
name|'res'
op|'='
name|'self'
op|'.'
name|'_do_request'
op|'('
name|'cmd'
op|','
name|'subcmd'
op|','
name|'cooked'
op|','
name|'headers'
op|')'
newline|'\n'
name|'if'
name|'status'
op|'=='
name|'httplib'
op|'.'
name|'OK'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'='
name|'res'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'return'
name|'status'
op|','
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'status'
op|','
name|'None'
newline|'\n'
nl|'\n'
DECL|member|do_attestation
dedent|''
dedent|''
name|'def'
name|'do_attestation'
op|'('
name|'self'
op|','
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attests compute nodes through OAT service.\n\n        :param hosts: hosts list to be attested\n        :returns: dictionary for trust level and validate time\n        """'
newline|'\n'
name|'result'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'status'
op|','
name|'data'
op|'='
name|'self'
op|'.'
name|'_request'
op|'('
string|'"POST"'
op|','
string|'"PollHosts"'
op|','
name|'hosts'
op|')'
newline|'\n'
name|'if'
name|'data'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'hosts'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeAttestationCache
dedent|''
dedent|''
name|'class'
name|'ComputeAttestationCache'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Cache for compute node attestation\n\n    Cache compute node\'s trust level for sometime,\n    if the cache is out of date, poll OAT service to flush the\n    cache.\n\n    OAT service may have cache also. OAT service\'s cache valid time\n    should be set shorter than trusted filter\'s cache valid time.\n    """'
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
name|'self'
op|'.'
name|'attestservice'
op|'='
name|'AttestationService'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_nodes'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'admin'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Fetch compute node list to initialize the compute_nodes,'
nl|'\n'
comment|"# so that we don't need poll OAT service one by one for each"
nl|'\n'
comment|'# host in the first round that scheduler invokes us.'
nl|'\n'
name|'computes'
op|'='
name|'db'
op|'.'
name|'compute_node_get_all'
op|'('
name|'admin'
op|')'
newline|'\n'
name|'for'
name|'compute'
name|'in'
name|'computes'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'='
name|'compute'
op|'['
string|"'service'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'service'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"No service for compute ID %s"'
op|')'
op|'%'
name|'compute'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'host'
op|'='
name|'service'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_init_cache_entry'
op|'('
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_cache_valid
dedent|''
dedent|''
name|'def'
name|'_cache_valid'
op|'('
name|'self'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cachevalid'
op|'='
name|'False'
newline|'\n'
name|'if'
name|'host'
name|'in'
name|'self'
op|'.'
name|'compute_nodes'
op|':'
newline|'\n'
indent|'            '
name|'node_stats'
op|'='
name|'self'
op|'.'
name|'compute_nodes'
op|'.'
name|'get'
op|'('
name|'host'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'timeutils'
op|'.'
name|'is_older_than'
op|'('
nl|'\n'
name|'node_stats'
op|'['
string|"'vtime'"
op|']'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'trusted_computing'
op|'.'
name|'attestation_auth_timeout'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'cachevalid'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'cachevalid'
newline|'\n'
nl|'\n'
DECL|member|_init_cache_entry
dedent|''
name|'def'
name|'_init_cache_entry'
op|'('
name|'self'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'compute_nodes'
op|'['
name|'host'
op|']'
op|'='
op|'{'
nl|'\n'
string|"'trust_lvl'"
op|':'
string|"'unknown'"
op|','
nl|'\n'
string|"'vtime'"
op|':'
name|'timeutils'
op|'.'
name|'normalize_time'
op|'('
nl|'\n'
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
string|'"1970-01-01T00:00:00Z"'
op|')'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_invalidate_caches
dedent|''
name|'def'
name|'_invalidate_caches'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'host'
name|'in'
name|'self'
op|'.'
name|'compute_nodes'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_init_cache_entry'
op|'('
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_update_cache_entry
dedent|''
dedent|''
name|'def'
name|'_update_cache_entry'
op|'('
name|'self'
op|','
name|'state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'entry'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'host'
op|'='
name|'state'
op|'['
string|"'host_name'"
op|']'
newline|'\n'
name|'entry'
op|'['
string|"'trust_lvl'"
op|']'
op|'='
name|'state'
op|'['
string|"'trust_lvl'"
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# Normalize as naive object to interoperate with utcnow().'
nl|'\n'
indent|'            '
name|'entry'
op|'['
string|"'vtime'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'normalize_time'
op|'('
nl|'\n'
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
name|'state'
op|'['
string|"'vtime'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
comment|'# Mark the system as un-trusted if get invalid vtime.'
nl|'\n'
indent|'            '
name|'entry'
op|'['
string|"'trust_lvl'"
op|']'
op|'='
string|"'unknown'"
newline|'\n'
name|'entry'
op|'['
string|"'vtime'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'compute_nodes'
op|'['
name|'host'
op|']'
op|'='
name|'entry'
newline|'\n'
nl|'\n'
DECL|member|_update_cache
dedent|''
name|'def'
name|'_update_cache'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_invalidate_caches'
op|'('
op|')'
newline|'\n'
name|'states'
op|'='
name|'self'
op|'.'
name|'attestservice'
op|'.'
name|'do_attestation'
op|'('
name|'self'
op|'.'
name|'compute_nodes'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'states'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'for'
name|'state'
name|'in'
name|'states'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_update_cache_entry'
op|'('
name|'state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_host_attestation
dedent|''
dedent|''
name|'def'
name|'get_host_attestation'
op|'('
name|'self'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check host\'s trust level."""'
newline|'\n'
name|'if'
name|'host'
name|'not'
name|'in'
name|'self'
op|'.'
name|'compute_nodes'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_init_cache_entry'
op|'('
name|'host'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'_cache_valid'
op|'('
name|'host'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_update_cache'
op|'('
op|')'
newline|'\n'
dedent|''
name|'level'
op|'='
name|'self'
op|'.'
name|'compute_nodes'
op|'.'
name|'get'
op|'('
name|'host'
op|')'
op|'.'
name|'get'
op|'('
string|"'trust_lvl'"
op|')'
newline|'\n'
name|'return'
name|'level'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeAttestation
dedent|''
dedent|''
name|'class'
name|'ComputeAttestation'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'caches'
op|'='
name|'ComputeAttestationCache'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_trusted
dedent|''
name|'def'
name|'is_trusted'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'trust'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'level'
op|'='
name|'self'
op|'.'
name|'caches'
op|'.'
name|'get_host_attestation'
op|'('
name|'host'
op|')'
newline|'\n'
name|'return'
name|'trust'
op|'=='
name|'level'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TrustedFilter
dedent|''
dedent|''
name|'class'
name|'TrustedFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Trusted filter to support Trusted Compute Pools."""'
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
name|'self'
op|'.'
name|'compute_attestation'
op|'='
name|'ComputeAttestation'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|host_passes
dedent|''
name|'def'
name|'host_passes'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'instance_type'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'extra'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'extra_specs'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'trust'
op|'='
name|'extra'
op|'.'
name|'get'
op|'('
string|"'trust:trusted_host'"
op|')'
newline|'\n'
name|'host'
op|'='
name|'host_state'
op|'.'
name|'host'
newline|'\n'
name|'if'
name|'trust'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'compute_attestation'
op|'.'
name|'is_trusted'
op|'('
name|'host'
op|','
name|'trust'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
