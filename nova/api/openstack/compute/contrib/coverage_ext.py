begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 IBM Corp.'
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
comment|'# See: http://wiki.openstack.org/Nova/CoverageExtension for more information'
nl|'\n'
comment|'# and usage explanation for this API extension'
nl|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'telnetlib'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'baserpc'
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
op|'.'
name|'gettextutils'
name|'import'
name|'_'
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
op|'.'
name|'rpc'
name|'import'
name|'common'
name|'as'
name|'rpc_common'
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
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'coverage_ext'"
op|')'
newline|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CoverageController
name|'class'
name|'CoverageController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Coverage report API controller for the OpenStack API."""'
newline|'\n'
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
name|'data_path'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'services'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'combine'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'_cover_inst'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
name|'CONF'
op|'.'
name|'host'
newline|'\n'
name|'super'
op|'('
name|'CoverageController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|coverInst
name|'def'
name|'coverInst'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_cover_inst'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'import'
name|'coverage'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'data_path'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'data_path'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
name|'prefix'
op|'='
string|"'nova-coverage_'"
op|')'
newline|'\n'
dedent|''
name|'data_out'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'data_path'
op|','
string|"'.nova-coverage.api'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_cover_inst'
op|'='
name|'coverage'
op|'.'
name|'coverage'
op|'('
name|'data_file'
op|'='
name|'data_out'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_cover_inst'
newline|'\n'
nl|'\n'
DECL|member|_find_services
dedent|''
name|'def'
name|'_find_services'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of services."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'serv'
name|'in'
name|'services'
op|':'
newline|'\n'
indent|'            '
name|'hosts'
op|'.'
name|'append'
op|'('
op|'{'
string|'"service"'
op|':'
name|'serv'
op|'['
string|'"topic"'
op|']'
op|','
string|'"host"'
op|':'
name|'serv'
op|'['
string|'"host"'
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'hosts'
newline|'\n'
nl|'\n'
DECL|member|_find_ports
dedent|''
name|'def'
name|'_find_ports'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of backdoor ports for all services in the list."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'ports'
op|'='
op|'['
op|']'
newline|'\n'
comment|'#TODO(mtreinish): Figure out how to bind the backdoor socket to 0.0.0.0'
nl|'\n'
comment|'# Currently this will only work if the host is resolved as loopback on'
nl|'\n'
comment|'# the same host as api-server'
nl|'\n'
name|'for'
name|'host'
name|'in'
name|'hosts'
op|':'
newline|'\n'
indent|'            '
name|'base'
op|'='
name|'baserpc'
op|'.'
name|'BaseAPI'
op|'('
name|'host'
op|'['
string|"'service'"
op|']'
op|')'
newline|'\n'
name|'_host'
op|'='
name|'host'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'_host'
op|'['
string|"'port'"
op|']'
op|'='
name|'base'
op|'.'
name|'get_backdoor_port'
op|'('
name|'context'
op|','
name|'host'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rpc_common'
op|'.'
name|'UnsupportedRpcVersion'
op|':'
newline|'\n'
indent|'                '
name|'_host'
op|'['
string|"'port'"
op|']'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|"#NOTE(mtreinish): if the port is None then it wasn't set in"
nl|'\n'
comment|'# the configuration file for this service. However, that'
nl|'\n'
comment|"# doesn't necessarily mean that we don't have backdoor ports"
nl|'\n'
comment|'# for all the services. So, skip the telnet connection for'
nl|'\n'
comment|'# this service.'
nl|'\n'
dedent|''
name|'if'
name|'_host'
op|'['
string|"'port'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'ports'
op|'.'
name|'append'
op|'('
name|'_host'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Can\'t connect to service: %s, no port"'
nl|'\n'
string|'"specified\\n"'
op|')'
op|','
name|'host'
op|'['
string|"'service'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'ports'
newline|'\n'
nl|'\n'
DECL|member|_start_coverage_telnet
dedent|''
name|'def'
name|'_start_coverage_telnet'
op|'('
name|'self'
op|','
name|'tn'
op|','
name|'service'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'data_path'
op|','
nl|'\n'
string|"'.nova-coverage.%s'"
op|'%'
name|'str'
op|'('
name|'service'
op|')'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
string|"'import sys\\n'"
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
string|"'from coverage import coverage\\n'"
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
string|'"coverInst = coverage(data_file=\'%s\') "'
nl|'\n'
string|'"if \'coverInst\' not in locals() "'
nl|'\n'
string|'"else coverInst\\n"'
op|'%'
name|'data_file'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
string|"'coverInst.skipModules = sys.modules.keys()\\n'"
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
string|'"coverInst.start()\\n"'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
string|'"print \'finished\'\\n"'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'expect'
op|'('
op|'['
name|'re'
op|'.'
name|'compile'
op|'('
string|"'finished'"
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_start_coverage
dedent|''
name|'def'
name|'_start_coverage'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Begin recording coverage information.'''"
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Coverage begin"'
op|')'
op|')'
newline|'\n'
name|'body'
op|'='
name|'body'
op|'['
string|"'start'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'combine'
op|'='
name|'False'
newline|'\n'
name|'if'
string|"'combine'"
name|'in'
name|'body'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'combine'
op|'='
name|'bool'
op|'('
name|'body'
op|'['
string|"'combine'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'coverInst'
op|'.'
name|'skipModules'
op|'='
name|'sys'
op|'.'
name|'modules'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coverInst'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'_find_services'
op|'('
name|'req'
op|')'
newline|'\n'
name|'ports'
op|'='
name|'self'
op|'.'
name|'_find_ports'
op|'('
name|'req'
op|','
name|'hosts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'services'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'service'
name|'in'
name|'ports'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'service'
op|'['
string|"'telnet'"
op|']'
op|'='
name|'telnetlib'
op|'.'
name|'Telnet'
op|'('
name|'service'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
name|'service'
op|'['
string|"'port'"
op|']'
op|')'
newline|'\n'
comment|'# NOTE(mtreinish): Fallback to try connecting to lo if'
nl|'\n'
comment|'# ECONNREFUSED is raised. If using the hostname that is returned'
nl|'\n'
comment|'# for the service from the service_get_all() DB query raises'
nl|'\n'
comment|'# ECONNREFUSED it most likely means that the hostname in the DB'
nl|'\n'
comment|"# doesn't resolve to 127.0.0.1. Currently backdoors only open on"
nl|'\n'
comment|'# loopback so this is for covering the common single host use case'
nl|'\n'
dedent|''
name|'except'
name|'socket'
op|'.'
name|'error'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'exc_info'
op|'='
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
newline|'\n'
name|'if'
string|"'ECONNREFUSED'"
name|'in'
name|'e'
name|'and'
name|'service'
op|'['
string|"'host'"
op|']'
op|'=='
name|'self'
op|'.'
name|'host'
op|':'
newline|'\n'
indent|'                        '
name|'service'
op|'['
string|"'telnet'"
op|']'
op|'='
name|'telnetlib'
op|'.'
name|'Telnet'
op|'('
string|"'127.0.0.1'"
op|','
nl|'\n'
name|'service'
op|'['
string|"'port'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exc_info'
op|'['
number|'0'
op|']'
op|','
name|'exc_info'
op|'['
number|'1'
op|']'
op|','
name|'exc_info'
op|'['
number|'2'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'services'
op|'.'
name|'append'
op|'('
name|'service'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_start_coverage_telnet'
op|'('
name|'service'
op|'['
string|"'telnet'"
op|']'
op|','
name|'service'
op|'['
string|"'service'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_stop_coverage_telnet
dedent|''
dedent|''
name|'def'
name|'_stop_coverage_telnet'
op|'('
name|'self'
op|','
name|'tn'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tn'
op|'.'
name|'write'
op|'('
string|'"coverInst.stop()\\n"'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
string|'"coverInst.save()\\n"'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
string|'"print \'finished\'\\n"'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'expect'
op|'('
op|'['
name|'re'
op|'.'
name|'compile'
op|'('
string|"'finished'"
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_coverage
dedent|''
name|'def'
name|'_check_coverage'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'coverInst'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coverInst'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AssertionError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|_stop_coverage
dedent|''
name|'def'
name|'_stop_coverage'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'service'
name|'in'
name|'self'
op|'.'
name|'services'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_stop_coverage_telnet'
op|'('
name|'service'
op|'['
string|"'telnet'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_check_coverage'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Coverage not running"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'path'"
op|':'
name|'self'
op|'.'
name|'data_path'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_report_coverage_telnet
dedent|''
name|'def'
name|'_report_coverage_telnet'
op|'('
name|'self'
op|','
name|'tn'
op|','
name|'path'
op|','
name|'xml'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'xml'
op|':'
newline|'\n'
indent|'            '
name|'execute'
op|'='
name|'str'
op|'('
string|'"coverInst.xml_report(outfile=\'%s\')\\n"'
op|'%'
name|'path'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
name|'execute'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
string|'"print \'finished\'\\n"'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'expect'
op|'('
op|'['
name|'re'
op|'.'
name|'compile'
op|'('
string|"'finished'"
op|')'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'execute'
op|'='
name|'str'
op|'('
string|'"output = open(\'%s\', \'w\')\\n"'
op|'%'
name|'path'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
name|'execute'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
string|'"coverInst.report(file=output)\\n"'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
string|'"output.close()\\n"'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
string|'"print \'finished\'\\n"'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'expect'
op|'('
op|'['
name|'re'
op|'.'
name|'compile'
op|'('
string|"'finished'"
op|')'
op|']'
op|')'
newline|'\n'
dedent|''
name|'tn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_report_coverage
dedent|''
name|'def'
name|'_report_coverage'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_stop_coverage'
op|'('
name|'req'
op|')'
newline|'\n'
name|'xml'
op|'='
name|'False'
newline|'\n'
name|'html'
op|'='
name|'False'
newline|'\n'
name|'path'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'body'
op|'['
string|"'report'"
op|']'
newline|'\n'
name|'if'
string|"'file'"
name|'in'
name|'body'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'body'
op|'['
string|"'file'"
op|']'
newline|'\n'
name|'if'
name|'path'
op|'!='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid path"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'data_path'
op|','
name|'path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"No path given for report file"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
string|"'xml'"
name|'in'
name|'body'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'xml'
op|'='
name|'body'
op|'['
string|"'xml'"
op|']'
newline|'\n'
dedent|''
name|'elif'
string|"'html'"
name|'in'
name|'body'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'combine'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"You can\'t use html reports without combining"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'html'
op|'='
name|'body'
op|'['
string|"'html'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'combine'
op|':'
newline|'\n'
indent|'            '
name|'data_out'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'data_path'
op|','
string|"'.nova-coverage'"
op|')'
newline|'\n'
name|'import'
name|'coverage'
newline|'\n'
name|'coverInst'
op|'='
name|'coverage'
op|'.'
name|'coverage'
op|'('
name|'data_file'
op|'='
name|'data_out'
op|')'
newline|'\n'
name|'coverInst'
op|'.'
name|'combine'
op|'('
op|')'
newline|'\n'
name|'if'
name|'xml'
op|':'
newline|'\n'
indent|'                '
name|'coverInst'
op|'.'
name|'xml_report'
op|'('
name|'outfile'
op|'='
name|'path'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'html'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Directory conflict: %s already exists"'
op|')'
op|'%'
name|'path'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'coverInst'
op|'.'
name|'html_report'
op|'('
name|'directory'
op|'='
name|'path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'output'
op|'='
name|'open'
op|'('
name|'path'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'coverInst'
op|'.'
name|'report'
op|'('
name|'file'
op|'='
name|'output'
op|')'
newline|'\n'
name|'output'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'for'
name|'service'
name|'in'
name|'self'
op|'.'
name|'services'
op|':'
newline|'\n'
indent|'                '
name|'service'
op|'['
string|"'telnet'"
op|']'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'xml'
op|':'
newline|'\n'
indent|'                '
name|'apipath'
op|'='
name|'path'
op|'+'
string|"'.api'"
newline|'\n'
name|'self'
op|'.'
name|'coverInst'
op|'.'
name|'xml_report'
op|'('
name|'outfile'
op|'='
name|'apipath'
op|')'
newline|'\n'
name|'for'
name|'service'
name|'in'
name|'self'
op|'.'
name|'services'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_report_coverage_telnet'
op|'('
name|'service'
op|'['
string|"'telnet'"
op|']'
op|','
nl|'\n'
name|'path'
op|'+'
string|"'.%s'"
nl|'\n'
op|'%'
name|'service'
op|'['
string|"'service'"
op|']'
op|','
nl|'\n'
name|'xml'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'output'
op|'='
name|'open'
op|'('
name|'path'
op|'+'
string|"'.api'"
op|','
string|"'w'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coverInst'
op|'.'
name|'report'
op|'('
name|'file'
op|'='
name|'output'
op|')'
newline|'\n'
name|'for'
name|'service'
name|'in'
name|'self'
op|'.'
name|'services'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_report_coverage_telnet'
op|'('
name|'service'
op|'['
string|"'telnet'"
op|']'
op|','
nl|'\n'
name|'path'
op|'+'
string|"'.%s'"
op|'%'
name|'service'
op|'['
string|"'service'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'output'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
op|'{'
string|"'path'"
op|':'
name|'path'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_reset_coverage_telnet
dedent|''
name|'def'
name|'_reset_coverage_telnet'
op|'('
name|'self'
op|','
name|'tn'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tn'
op|'.'
name|'write'
op|'('
string|'"coverInst.erase()\\n"'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'write'
op|'('
string|'"print \'finished\'\\n"'
op|')'
newline|'\n'
name|'tn'
op|'.'
name|'expect'
op|'('
op|'['
name|'re'
op|'.'
name|'compile'
op|'('
string|"'finished'"
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_reset_coverage
dedent|''
name|'def'
name|'_reset_coverage'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
comment|'# Reopen telnet connections if they are closed.'
nl|'\n'
indent|'        '
name|'for'
name|'service'
name|'in'
name|'self'
op|'.'
name|'services'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'service'
op|'['
string|"'telnet'"
op|']'
op|'.'
name|'get_socket'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'service'
op|'['
string|"'telnet'"
op|']'
op|'.'
name|'open'
op|'('
name|'service'
op|'['
string|"'host'"
op|']'
op|','
name|'service'
op|'['
string|"'port'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Stop coverage if it is started.'
nl|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_stop_coverage'
op|'('
name|'req'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'service'
name|'in'
name|'self'
op|'.'
name|'services'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_reset_coverage_telnet'
op|'('
name|'service'
op|'['
string|"'telnet'"
op|']'
op|')'
newline|'\n'
name|'service'
op|'['
string|"'telnet'"
op|']'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'coverInst'
op|'.'
name|'erase'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|action
dedent|''
name|'def'
name|'action'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_actions'
op|'='
op|'{'
nl|'\n'
string|"'start'"
op|':'
name|'self'
op|'.'
name|'_start_coverage'
op|','
nl|'\n'
string|"'stop'"
op|':'
name|'self'
op|'.'
name|'_stop_coverage'
op|','
nl|'\n'
string|"'report'"
op|':'
name|'self'
op|'.'
name|'_report_coverage'
op|','
nl|'\n'
string|"'reset'"
op|':'
name|'self'
op|'.'
name|'_reset_coverage'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'authorize'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'coverInst'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Python coverage module is not installed."'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPServiceUnavailable'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'action'
op|','
name|'data'
name|'in'
name|'body'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'action'
op|'=='
string|"'stop'"
name|'or'
name|'action'
op|'=='
string|"'reset'"
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'_actions'
op|'['
name|'action'
op|']'
op|'('
name|'req'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'action'
op|'=='
string|"'report'"
name|'or'
name|'action'
op|'=='
string|"'start'"
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'_actions'
op|'['
name|'action'
op|']'
op|'('
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Coverage doesn\'t have %s action"'
op|')'
op|'%'
name|'action'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Invalid request body"'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Coverage_ext
dedent|''
dedent|''
name|'class'
name|'Coverage_ext'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Enable Nova Coverage."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Coverage"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-coverage"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"coverage/api/v2"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-10-15T00:00:00+00:00"'
newline|'\n'
nl|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-coverage'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'CoverageController'
op|'('
op|')'
op|','
nl|'\n'
name|'collection_actions'
op|'='
op|'{'
string|'"action"'
op|':'
string|'"POST"'
op|'}'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
