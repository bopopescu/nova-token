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
string|'"""Nova logging handler.\n\nThis module adds to logging functionality by adding the option to specify\na context object when calling the various log methods.  If the context object\nis not specified, default formatting is used.\n\nIt also allows setting of formatting information through flags.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'cStringIO'
newline|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'logging'
op|'.'
name|'handlers'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'traceback'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'version'
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
string|"'logging_context_format_string'"
op|','
nl|'\n'
string|"'%(asctime)s %(levelname)s %(name)s '"
nl|'\n'
string|"'[%(request_id)s %(user)s '"
nl|'\n'
string|"'%(project)s] %(message)s'"
op|','
nl|'\n'
string|"'format string to use for log messages with context'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'logging_default_format_string'"
op|','
nl|'\n'
string|"'%(asctime)s %(levelname)s %(name)s [-] '"
nl|'\n'
string|"'%(message)s'"
op|','
nl|'\n'
string|"'format string to use for log messages without context'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'logging_debug_format_suffix'"
op|','
nl|'\n'
string|"'from (pid=%(process)d) %(funcName)s'"
nl|'\n'
string|"' %(pathname)s:%(lineno)d'"
op|','
nl|'\n'
string|"'data to append to log format when level is DEBUG'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'logging_exception_prefix'"
op|','
nl|'\n'
string|"'(%(name)s): TRACE: '"
op|','
nl|'\n'
string|"'prefix each line of exception output with this format'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_list'
op|'('
string|"'default_log_levels'"
op|','
nl|'\n'
op|'['
string|"'amqplib=WARN'"
op|','
nl|'\n'
string|"'sqlalchemy=WARN'"
op|','
nl|'\n'
string|"'boto=WARN'"
op|','
nl|'\n'
string|"'eventlet.wsgi.server=WARN'"
op|']'
op|','
nl|'\n'
string|"'list of logger=LEVEL pairs'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_bool'
op|'('
string|"'use_syslog'"
op|','
name|'False'
op|','
string|"'output to syslog'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_bool'
op|'('
string|"'publish_errors'"
op|','
name|'False'
op|','
string|"'publish error events'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'logfile'"
op|','
name|'None'
op|','
string|"'output to named file'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# A list of things we want to replicate from logging.'
nl|'\n'
comment|'# levels'
nl|'\n'
DECL|variable|CRITICAL
name|'CRITICAL'
op|'='
name|'logging'
op|'.'
name|'CRITICAL'
newline|'\n'
DECL|variable|FATAL
name|'FATAL'
op|'='
name|'logging'
op|'.'
name|'FATAL'
newline|'\n'
DECL|variable|ERROR
name|'ERROR'
op|'='
name|'logging'
op|'.'
name|'ERROR'
newline|'\n'
DECL|variable|WARNING
name|'WARNING'
op|'='
name|'logging'
op|'.'
name|'WARNING'
newline|'\n'
DECL|variable|WARN
name|'WARN'
op|'='
name|'logging'
op|'.'
name|'WARN'
newline|'\n'
DECL|variable|INFO
name|'INFO'
op|'='
name|'logging'
op|'.'
name|'INFO'
newline|'\n'
DECL|variable|DEBUG
name|'DEBUG'
op|'='
name|'logging'
op|'.'
name|'DEBUG'
newline|'\n'
DECL|variable|NOTSET
name|'NOTSET'
op|'='
name|'logging'
op|'.'
name|'NOTSET'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# methods'
nl|'\n'
DECL|variable|getLogger
name|'getLogger'
op|'='
name|'logging'
op|'.'
name|'getLogger'
newline|'\n'
DECL|variable|debug
name|'debug'
op|'='
name|'logging'
op|'.'
name|'debug'
newline|'\n'
DECL|variable|info
name|'info'
op|'='
name|'logging'
op|'.'
name|'info'
newline|'\n'
DECL|variable|warning
name|'warning'
op|'='
name|'logging'
op|'.'
name|'warning'
newline|'\n'
DECL|variable|warn
name|'warn'
op|'='
name|'logging'
op|'.'
name|'warn'
newline|'\n'
DECL|variable|error
name|'error'
op|'='
name|'logging'
op|'.'
name|'error'
newline|'\n'
DECL|variable|exception
name|'exception'
op|'='
name|'logging'
op|'.'
name|'exception'
newline|'\n'
DECL|variable|critical
name|'critical'
op|'='
name|'logging'
op|'.'
name|'critical'
newline|'\n'
DECL|variable|log
name|'log'
op|'='
name|'logging'
op|'.'
name|'log'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# handlers'
nl|'\n'
DECL|variable|StreamHandler
name|'StreamHandler'
op|'='
name|'logging'
op|'.'
name|'StreamHandler'
newline|'\n'
DECL|variable|WatchedFileHandler
name|'WatchedFileHandler'
op|'='
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'WatchedFileHandler'
newline|'\n'
comment|'# logging.SysLogHandler is nicer than logging.logging.handler.SysLogHandler.'
nl|'\n'
DECL|variable|SysLogHandler
name|'SysLogHandler'
op|'='
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'SysLogHandler'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# our new audit level'
nl|'\n'
DECL|variable|AUDIT
name|'AUDIT'
op|'='
name|'logging'
op|'.'
name|'INFO'
op|'+'
number|'1'
newline|'\n'
name|'logging'
op|'.'
name|'addLevelName'
op|'('
name|'AUDIT'
op|','
string|"'AUDIT'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_dictify_context
name|'def'
name|'_dictify_context'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'context'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'context'
op|','
name|'dict'
op|')'
name|'and'
name|'getattr'
op|'('
name|'context'
op|','
string|"'to_dict'"
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'context'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_binary_name
dedent|''
name|'def'
name|'_get_binary_name'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'inspect'
op|'.'
name|'stack'
op|'('
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_log_file_path
dedent|''
name|'def'
name|'_get_log_file_path'
op|'('
name|'binary'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'FLAGS'
op|'.'
name|'logfile'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FLAGS'
op|'.'
name|'logfile'
newline|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'logdir'
op|':'
newline|'\n'
indent|'        '
name|'binary'
op|'='
name|'binary'
name|'or'
name|'_get_binary_name'
op|'('
op|')'
newline|'\n'
name|'return'
string|"'%s.log'"
op|'%'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'logdir'
op|','
name|'binary'
op|')'
op|','
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaLogger
dedent|''
dedent|''
name|'class'
name|'NovaLogger'
op|'('
name|'logging'
op|'.'
name|'Logger'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""NovaLogger manages request context and formatting.\n\n    This becomes the class that is instanciated by logging.getLogger.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'level'
op|'='
name|'NOTSET'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'Logger'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'level'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'setup_from_flags'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_from_flags
dedent|''
name|'def'
name|'setup_from_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Setup logger from flags."""'
newline|'\n'
name|'level'
op|'='
name|'NOTSET'
newline|'\n'
name|'for'
name|'pair'
name|'in'
name|'FLAGS'
op|'.'
name|'default_log_levels'
op|':'
newline|'\n'
indent|'            '
name|'logger'
op|','
name|'_sep'
op|','
name|'level_name'
op|'='
name|'pair'
op|'.'
name|'partition'
op|'('
string|"'='"
op|')'
newline|'\n'
comment|'# NOTE(todd): if we set a.b, we want a.b.c to have the same level'
nl|'\n'
comment|'#             (but not a.bc, so we check the dot)'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'name'
op|'=='
name|'logger'
name|'or'
name|'self'
op|'.'
name|'name'
op|'.'
name|'startswith'
op|'('
string|'"%s."'
op|'%'
name|'logger'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'level'
op|'='
name|'globals'
op|'('
op|')'
op|'['
name|'level_name'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'setLevel'
op|'('
name|'level'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_log
dedent|''
name|'def'
name|'_log'
op|'('
name|'self'
op|','
name|'level'
op|','
name|'msg'
op|','
name|'args'
op|','
name|'exc_info'
op|'='
name|'None'
op|','
name|'extra'
op|'='
name|'None'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Extract context from any log call."""'
newline|'\n'
name|'if'
name|'not'
name|'extra'
op|':'
newline|'\n'
indent|'            '
name|'extra'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'if'
name|'context'
op|':'
newline|'\n'
indent|'            '
name|'extra'
op|'.'
name|'update'
op|'('
name|'_dictify_context'
op|'('
name|'context'
op|')'
op|')'
newline|'\n'
dedent|''
name|'extra'
op|'.'
name|'update'
op|'('
op|'{'
string|'"nova_version"'
op|':'
name|'version'
op|'.'
name|'version_string_with_vcs'
op|'('
op|')'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'logging'
op|'.'
name|'Logger'
op|'.'
name|'_log'
op|'('
name|'self'
op|','
name|'level'
op|','
name|'msg'
op|','
name|'args'
op|','
name|'exc_info'
op|','
name|'extra'
op|')'
newline|'\n'
nl|'\n'
DECL|member|addHandler
dedent|''
name|'def'
name|'addHandler'
op|'('
name|'self'
op|','
name|'handler'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Each handler gets our custom formatter."""'
newline|'\n'
name|'handler'
op|'.'
name|'setFormatter'
op|'('
name|'_formatter'
op|')'
newline|'\n'
name|'return'
name|'logging'
op|'.'
name|'Logger'
op|'.'
name|'addHandler'
op|'('
name|'self'
op|','
name|'handler'
op|')'
newline|'\n'
nl|'\n'
DECL|member|audit
dedent|''
name|'def'
name|'audit'
op|'('
name|'self'
op|','
name|'msg'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Shortcut for our AUDIT level."""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'isEnabledFor'
op|'('
name|'AUDIT'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_log'
op|'('
name|'AUDIT'
op|','
name|'msg'
op|','
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|exception
dedent|''
dedent|''
name|'def'
name|'exception'
op|'('
name|'self'
op|','
name|'msg'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Logging.exception doesn\'t handle kwargs, so breaks context."""'
newline|'\n'
name|'if'
name|'not'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'exc_info'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'['
string|"'exc_info'"
op|']'
op|'='
number|'1'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'error'
op|'('
name|'msg'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
comment|'# NOTE(todd): does this really go here, or in _log ?'
nl|'\n'
name|'extra'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'extra'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'extra'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'env'
op|'='
name|'extra'
op|'.'
name|'get'
op|'('
string|"'environment'"
op|')'
newline|'\n'
name|'if'
name|'env'
op|':'
newline|'\n'
indent|'            '
name|'env'
op|'='
name|'env'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'env'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'env'
op|'['
name|'k'
op|']'
op|','
name|'str'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'env'
op|'.'
name|'pop'
op|'('
name|'k'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'message'
op|'='
string|"'Environment: %s'"
op|'%'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'env'
op|')'
newline|'\n'
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'exc_info'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'error'
op|'('
name|'message'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaFormatter
dedent|''
dedent|''
dedent|''
name|'class'
name|'NovaFormatter'
op|'('
name|'logging'
op|'.'
name|'Formatter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A nova.context.RequestContext aware formatter configured through flags.\n\n    The flags used to set format strings are: logging_context_foramt_string\n    and logging_default_format_string.  You can also specify\n    logging_debug_format_suffix to append extra formatting if the log level is\n    debug.\n\n    For information about what variables are available for the formatter see:\n    http://docs.python.org/library/logging.html#formatter\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|format
name|'def'
name|'format'
op|'('
name|'self'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Uses contextstring if request_id is set, otherwise default."""'
newline|'\n'
name|'if'
name|'record'
op|'.'
name|'__dict__'
op|'.'
name|'get'
op|'('
string|"'request_id'"
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_fmt'
op|'='
name|'FLAGS'
op|'.'
name|'logging_context_format_string'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_fmt'
op|'='
name|'FLAGS'
op|'.'
name|'logging_default_format_string'
newline|'\n'
dedent|''
name|'if'
name|'record'
op|'.'
name|'levelno'
op|'=='
name|'logging'
op|'.'
name|'DEBUG'
name|'and'
name|'FLAGS'
op|'.'
name|'logging_debug_format_suffix'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_fmt'
op|'+='
string|'" "'
op|'+'
name|'FLAGS'
op|'.'
name|'logging_debug_format_suffix'
newline|'\n'
comment|'# Cache this on the record, Logger will respect our formated copy'
nl|'\n'
dedent|''
name|'if'
name|'record'
op|'.'
name|'exc_info'
op|':'
newline|'\n'
indent|'            '
name|'record'
op|'.'
name|'exc_text'
op|'='
name|'self'
op|'.'
name|'formatException'
op|'('
name|'record'
op|'.'
name|'exc_info'
op|','
name|'record'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'logging'
op|'.'
name|'Formatter'
op|'.'
name|'format'
op|'('
name|'self'
op|','
name|'record'
op|')'
newline|'\n'
nl|'\n'
DECL|member|formatException
dedent|''
name|'def'
name|'formatException'
op|'('
name|'self'
op|','
name|'exc_info'
op|','
name|'record'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Format exception output with FLAGS.logging_exception_prefix."""'
newline|'\n'
name|'if'
name|'not'
name|'record'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'logging'
op|'.'
name|'Formatter'
op|'.'
name|'formatException'
op|'('
name|'self'
op|','
name|'exc_info'
op|')'
newline|'\n'
dedent|''
name|'stringbuffer'
op|'='
name|'cStringIO'
op|'.'
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'traceback'
op|'.'
name|'print_exception'
op|'('
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
op|','
nl|'\n'
name|'None'
op|','
name|'stringbuffer'
op|')'
newline|'\n'
name|'lines'
op|'='
name|'stringbuffer'
op|'.'
name|'getvalue'
op|'('
op|')'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
newline|'\n'
name|'stringbuffer'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'formatted_lines'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'lines'
op|':'
newline|'\n'
indent|'            '
name|'pl'
op|'='
name|'FLAGS'
op|'.'
name|'logging_exception_prefix'
op|'%'
name|'record'
op|'.'
name|'__dict__'
newline|'\n'
name|'fl'
op|'='
string|"'%s%s'"
op|'%'
op|'('
name|'pl'
op|','
name|'line'
op|')'
newline|'\n'
name|'formatted_lines'
op|'.'
name|'append'
op|'('
name|'fl'
op|')'
newline|'\n'
dedent|''
name|'return'
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'formatted_lines'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_formatter
dedent|''
dedent|''
name|'_formatter'
op|'='
name|'NovaFormatter'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaRootLogger
name|'class'
name|'NovaRootLogger'
op|'('
name|'NovaLogger'
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
name|'name'
op|','
name|'level'
op|'='
name|'NOTSET'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'logpath'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'filelog'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'streamlog'
op|'='
name|'StreamHandler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'syslog'
op|'='
name|'None'
newline|'\n'
name|'NovaLogger'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'level'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_from_flags
dedent|''
name|'def'
name|'setup_from_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Setup logger from flags."""'
newline|'\n'
name|'global'
name|'_filelog'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_syslog'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'syslog'
op|'='
name|'SysLogHandler'
op|'('
name|'address'
op|'='
string|"'/dev/log'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addHandler'
op|'('
name|'self'
op|'.'
name|'syslog'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'syslog'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'removeHandler'
op|'('
name|'self'
op|'.'
name|'syslog'
op|')'
newline|'\n'
dedent|''
name|'logpath'
op|'='
name|'_get_log_file_path'
op|'('
op|')'
newline|'\n'
name|'if'
name|'logpath'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'removeHandler'
op|'('
name|'self'
op|'.'
name|'streamlog'
op|')'
newline|'\n'
name|'if'
name|'logpath'
op|'!='
name|'self'
op|'.'
name|'logpath'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'removeHandler'
op|'('
name|'self'
op|'.'
name|'filelog'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'filelog'
op|'='
name|'WatchedFileHandler'
op|'('
name|'logpath'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addHandler'
op|'('
name|'self'
op|'.'
name|'filelog'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'logpath'
op|'='
name|'logpath'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'removeHandler'
op|'('
name|'self'
op|'.'
name|'filelog'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addHandler'
op|'('
name|'self'
op|'.'
name|'streamlog'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'publish_errors'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'addHandler'
op|'('
name|'PublishErrorsHandler'
op|'('
name|'ERROR'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'verbose'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'setLevel'
op|'('
name|'DEBUG'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'setLevel'
op|'('
name|'INFO'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PublishErrorsHandler
dedent|''
dedent|''
dedent|''
name|'class'
name|'PublishErrorsHandler'
op|'('
name|'logging'
op|'.'
name|'Handler'
op|')'
op|':'
newline|'\n'
DECL|member|emit
indent|'    '
name|'def'
name|'emit'
op|'('
name|'self'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nova'
op|'.'
name|'notifier'
op|'.'
name|'notify'
op|'('
string|"'error'"
op|','
name|'record'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|handle_exception
dedent|''
dedent|''
name|'def'
name|'handle_exception'
op|'('
name|'type'
op|','
name|'value'
op|','
name|'tb'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'extra'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'verbose'
op|':'
newline|'\n'
indent|'        '
name|'extra'
op|'['
string|"'exc_info'"
op|']'
op|'='
op|'('
name|'type'
op|','
name|'value'
op|','
name|'tb'
op|')'
newline|'\n'
dedent|''
name|'logging'
op|'.'
name|'root'
op|'.'
name|'critical'
op|'('
name|'str'
op|'('
name|'value'
op|')'
op|','
op|'**'
name|'extra'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|reset
dedent|''
name|'def'
name|'reset'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Resets logging handlers.  Should be called if FLAGS changes."""'
newline|'\n'
name|'for'
name|'logger'
name|'in'
name|'NovaLogger'
op|'.'
name|'manager'
op|'.'
name|'loggerDict'
op|'.'
name|'itervalues'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'logger'
op|','
name|'NovaLogger'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'logger'
op|'.'
name|'setup_from_flags'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|setup
dedent|''
dedent|''
dedent|''
name|'def'
name|'setup'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Setup nova logging."""'
newline|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'logging'
op|'.'
name|'root'
op|','
name|'NovaRootLogger'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'_acquireLock'
op|'('
op|')'
newline|'\n'
name|'for'
name|'handler'
name|'in'
name|'logging'
op|'.'
name|'root'
op|'.'
name|'handlers'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'root'
op|'.'
name|'removeHandler'
op|'('
name|'handler'
op|')'
newline|'\n'
dedent|''
name|'logging'
op|'.'
name|'root'
op|'='
name|'NovaRootLogger'
op|'('
string|'"nova"'
op|')'
newline|'\n'
name|'NovaLogger'
op|'.'
name|'root'
op|'='
name|'logging'
op|'.'
name|'root'
newline|'\n'
name|'NovaLogger'
op|'.'
name|'manager'
op|'.'
name|'root'
op|'='
name|'logging'
op|'.'
name|'root'
newline|'\n'
name|'for'
name|'logger'
name|'in'
name|'NovaLogger'
op|'.'
name|'manager'
op|'.'
name|'loggerDict'
op|'.'
name|'itervalues'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'logger'
op|'.'
name|'root'
op|'='
name|'logging'
op|'.'
name|'root'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'logger'
op|','
name|'logging'
op|'.'
name|'Logger'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'NovaLogger'
op|'.'
name|'manager'
op|'.'
name|'_fixupParents'
op|'('
name|'logger'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'NovaLogger'
op|'.'
name|'manager'
op|'.'
name|'loggerDict'
op|'['
string|'"nova"'
op|']'
op|'='
name|'logging'
op|'.'
name|'root'
newline|'\n'
name|'logging'
op|'.'
name|'_releaseLock'
op|'('
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'excepthook'
op|'='
name|'handle_exception'
newline|'\n'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|root
dedent|''
dedent|''
name|'root'
op|'='
name|'logging'
op|'.'
name|'root'
newline|'\n'
name|'logging'
op|'.'
name|'setLoggerClass'
op|'('
name|'NovaLogger'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|audit
name|'def'
name|'audit'
op|'('
name|'msg'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Shortcut for logging to root log with sevrity \'AUDIT\'."""'
newline|'\n'
name|'logging'
op|'.'
name|'root'
op|'.'
name|'log'
op|'('
name|'AUDIT'
op|','
name|'msg'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
