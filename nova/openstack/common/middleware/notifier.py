begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2013 eNovance'
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
string|'"""\nSend notifications on request\n\n"""'
newline|'\n'
name|'import'
name|'os'
op|'.'
name|'path'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'traceback'
name|'as'
name|'tb'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'context'
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
comment|'# noqa'
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
name|'middleware'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'notifier'
name|'import'
name|'api'
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
nl|'\n'
DECL|function|log_and_ignore_error
name|'def'
name|'log_and_ignore_error'
op|'('
name|'fn'
op|')'
op|':'
newline|'\n'
DECL|function|wrapped
indent|'    '
name|'def'
name|'wrapped'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fn'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'An exception occurred processing '"
nl|'\n'
string|"'the API call: %s '"
op|')'
op|'%'
name|'e'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'wrapped'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RequestNotifier
dedent|''
name|'class'
name|'RequestNotifier'
op|'('
name|'base'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Send notification on request."""'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|factory
name|'def'
name|'factory'
op|'('
name|'cls'
op|','
name|'global_conf'
op|','
op|'**'
name|'local_conf'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Factory method for paste.deploy."""'
newline|'\n'
name|'conf'
op|'='
name|'global_conf'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'update'
op|'('
name|'local_conf'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_factory
name|'def'
name|'_factory'
op|'('
name|'app'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'('
name|'app'
op|','
op|'**'
name|'conf'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_factory'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'app'
op|','
op|'**'
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'service_name'
op|'='
name|'conf'
op|'.'
name|'get'
op|'('
string|"'service_name'"
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ignore_req_list'
op|'='
op|'['
name|'x'
op|'.'
name|'upper'
op|'('
op|')'
op|'.'
name|'strip'
op|'('
op|')'
name|'for'
name|'x'
name|'in'
nl|'\n'
name|'conf'
op|'.'
name|'get'
op|'('
string|"'ignore_req_list'"
op|','
string|"''"
op|')'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
op|']'
newline|'\n'
name|'super'
op|'('
name|'RequestNotifier'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'app'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|environ_to_dict
name|'def'
name|'environ_to_dict'
op|'('
name|'environ'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Following PEP 333, server variables are lower case, so don\'t\n        include them.\n\n        """'
newline|'\n'
name|'return'
name|'dict'
op|'('
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'environ'
op|'.'
name|'iteritems'
op|'('
op|')'
nl|'\n'
name|'if'
name|'k'
op|'.'
name|'isupper'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'log_and_ignore_error'
newline|'\n'
DECL|member|process_request
name|'def'
name|'process_request'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'.'
name|'environ'
op|'['
string|"'HTTP_X_SERVICE_NAME'"
op|']'
op|'='
name|'self'
op|'.'
name|'service_name'
name|'or'
name|'request'
op|'.'
name|'host'
newline|'\n'
name|'payload'
op|'='
op|'{'
nl|'\n'
string|"'request'"
op|':'
name|'self'
op|'.'
name|'environ_to_dict'
op|'('
name|'request'
op|'.'
name|'environ'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'api'
op|'.'
name|'notify'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'api'
op|'.'
name|'publisher_id'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|')'
op|')'
op|','
nl|'\n'
string|"'http.request'"
op|','
nl|'\n'
name|'api'
op|'.'
name|'INFO'
op|','
nl|'\n'
name|'payload'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'log_and_ignore_error'
newline|'\n'
DECL|member|process_response
name|'def'
name|'process_response'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'response'
op|','
nl|'\n'
name|'exception'
op|'='
name|'None'
op|','
name|'traceback'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'payload'
op|'='
op|'{'
nl|'\n'
string|"'request'"
op|':'
name|'self'
op|'.'
name|'environ_to_dict'
op|'('
name|'request'
op|'.'
name|'environ'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'response'
op|':'
newline|'\n'
indent|'            '
name|'payload'
op|'['
string|"'response'"
op|']'
op|'='
op|'{'
nl|'\n'
string|"'status'"
op|':'
name|'response'
op|'.'
name|'status'
op|','
nl|'\n'
string|"'headers'"
op|':'
name|'response'
op|'.'
name|'headers'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'exception'
op|':'
newline|'\n'
indent|'            '
name|'payload'
op|'['
string|"'exception'"
op|']'
op|'='
op|'{'
nl|'\n'
string|"'value'"
op|':'
name|'repr'
op|'('
name|'exception'
op|')'
op|','
nl|'\n'
string|"'traceback'"
op|':'
name|'tb'
op|'.'
name|'format_tb'
op|'('
name|'traceback'
op|')'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'api'
op|'.'
name|'notify'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'api'
op|'.'
name|'publisher_id'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|')'
op|')'
op|','
nl|'\n'
string|"'http.response'"
op|','
nl|'\n'
name|'api'
op|'.'
name|'INFO'
op|','
nl|'\n'
name|'payload'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'req'
op|'.'
name|'method'
name|'in'
name|'self'
op|'.'
name|'ignore_req_list'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'application'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'process_request'
op|'('
name|'req'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'response'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'application'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'type'
op|','
name|'value'
op|','
name|'traceback'
op|'='
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'process_response'
op|'('
name|'req'
op|','
name|'None'
op|','
name|'value'
op|','
name|'traceback'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'process_response'
op|'('
name|'req'
op|','
name|'response'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'response'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
