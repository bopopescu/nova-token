begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""Nova logging handler.\n\nThis module adds to logging functionality by adding the option to specify\na context object when calling the various log methods.  If the context object\nis not specified, default formatting is used. Additionally, an instance uuid\nmay be passed as part of the log message, which is intended to make it easier\nfor admins to find messages related to a specific instance.\n\nIt also allows setting of formatting information through flags.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'cStringIO'
newline|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'itertools'
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
name|'config'
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
name|'stat'
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
name|'local'
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
name|'import'
name|'version'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|log_opts
name|'log_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'logging_context_format_string'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'%(asctime)s %(levelname)s %(name)s [%(request_id)s '"
nl|'\n'
string|"'%(user_id)s %(project_id)s] %(instance)s'"
nl|'\n'
string|"'%(message)s'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'format string to use for log messages with context'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'logging_default_format_string'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'%(asctime)s %(levelname)s %(name)s [-] %(instance)s'"
nl|'\n'
string|"'%(message)s'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'format string to use for log messages without context'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'logging_debug_format_suffix'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'from (pid=%(process)d) %(funcName)s '"
nl|'\n'
string|"'%(pathname)s:%(lineno)d'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'data to append to log format when level is DEBUG'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'logging_exception_prefix'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'(%(name)s): TRACE: '"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'prefix each line of exception output with this format'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'instance_format'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'[instance: %(uuid)s] '"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'If an instance is passed with the log message, format '"
nl|'\n'
string|"'it like this'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'default_log_levels'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
nl|'\n'
string|"'amqplib=WARN'"
op|','
nl|'\n'
string|"'sqlalchemy=WARN'"
op|','
nl|'\n'
string|"'boto=WARN'"
op|','
nl|'\n'
string|"'suds=INFO'"
op|','
nl|'\n'
string|"'eventlet.wsgi.server=WARN'"
nl|'\n'
op|']'
op|','
nl|'\n'
name|'help'
op|'='
string|"'list of logger=LEVEL pairs'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'publish_errors'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'publish error events'"
op|')'
op|','
nl|'\n'
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
name|'log_opts'
op|')'
newline|'\n'
nl|'\n'
comment|'# our new audit level'
nl|'\n'
comment|'# NOTE(jkoelker) Since we synthesized an audit level, make the logging'
nl|'\n'
comment|'#                module aware of it so it acts like other levels.'
nl|'\n'
name|'logging'
op|'.'
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
name|'logging'
op|'.'
name|'AUDIT'
op|','
string|"'AUDIT'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
DECL|variable|NullHandler
indent|'    '
name|'NullHandler'
op|'='
name|'logging'
op|'.'
name|'NullHandler'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
comment|'# NOTE(jkoelker) NullHandler added in Python 2.7'
newline|'\n'
DECL|class|NullHandler
indent|'    '
name|'class'
name|'NullHandler'
op|'('
name|'logging'
op|'.'
name|'Handler'
op|')'
op|':'
newline|'\n'
DECL|member|handle
indent|'        '
name|'def'
name|'handle'
op|'('
name|'self'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|emit
dedent|''
name|'def'
name|'emit'
op|'('
name|'self'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|createLock
dedent|''
name|'def'
name|'createLock'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'lock'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_dictify_context
dedent|''
dedent|''
dedent|''
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
name|'logfile'
op|'='
name|'FLAGS'
op|'.'
name|'log_file'
name|'or'
name|'FLAGS'
op|'.'
name|'logfile'
newline|'\n'
name|'logdir'
op|'='
name|'FLAGS'
op|'.'
name|'log_dir'
name|'or'
name|'FLAGS'
op|'.'
name|'logdir'
newline|'\n'
nl|'\n'
name|'if'
name|'logfile'
name|'and'
name|'not'
name|'logdir'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'logfile'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'logfile'
name|'and'
name|'logdir'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'logdir'
op|','
name|'logfile'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
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
name|'logdir'
op|','
name|'binary'
op|')'
op|','
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaContextAdapter
dedent|''
dedent|''
name|'class'
name|'NovaContextAdapter'
op|'('
name|'logging'
op|'.'
name|'LoggerAdapter'
op|')'
op|':'
newline|'\n'
DECL|variable|warn
indent|'    '
name|'warn'
op|'='
name|'logging'
op|'.'
name|'LoggerAdapter'
op|'.'
name|'warning'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'logger'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'logger'
op|'='
name|'logger'
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
name|'self'
op|'.'
name|'log'
op|'('
name|'logging'
op|'.'
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
nl|'\n'
DECL|member|process
dedent|''
name|'def'
name|'process'
op|'('
name|'self'
op|','
name|'msg'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'extra'"
name|'not'
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'['
string|"'extra'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'extra'
op|'='
name|'kwargs'
op|'['
string|"'extra'"
op|']'
newline|'\n'
nl|'\n'
name|'context'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'context'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'context'
op|':'
newline|'\n'
indent|'            '
name|'context'
op|'='
name|'getattr'
op|'('
name|'local'
op|'.'
name|'store'
op|','
string|"'context'"
op|','
name|'None'
op|')'
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
nl|'\n'
dedent|''
name|'instance'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'instance'"
op|','
name|'None'
op|')'
newline|'\n'
name|'instance_extra'
op|'='
string|"''"
newline|'\n'
name|'if'
name|'instance'
op|':'
newline|'\n'
indent|'            '
name|'instance_extra'
op|'='
name|'FLAGS'
op|'.'
name|'instance_format'
op|'%'
name|'instance'
newline|'\n'
dedent|''
name|'extra'
op|'.'
name|'update'
op|'('
op|'{'
string|"'instance'"
op|':'
name|'instance_extra'
op|'}'
op|')'
newline|'\n'
nl|'\n'
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
name|'extra'
op|'['
string|"'extra'"
op|']'
op|'='
name|'extra'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'return'
name|'msg'
op|','
name|'kwargs'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|JSONFormatter
dedent|''
dedent|''
name|'class'
name|'JSONFormatter'
op|'('
name|'logging'
op|'.'
name|'Formatter'
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
name|'fmt'
op|'='
name|'None'
op|','
name|'datefmt'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(jkoelker) we ignore the fmt argument, but its still there'
nl|'\n'
comment|'#                since logging.config.fileConfig passes it.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'datefmt'
op|'='
name|'datefmt'
newline|'\n'
nl|'\n'
DECL|member|formatException
dedent|''
name|'def'
name|'formatException'
op|'('
name|'self'
op|','
name|'ei'
op|','
name|'strip_newlines'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'lines'
op|'='
name|'traceback'
op|'.'
name|'format_exception'
op|'('
op|'*'
name|'ei'
op|')'
newline|'\n'
name|'if'
name|'strip_newlines'
op|':'
newline|'\n'
indent|'            '
name|'lines'
op|'='
op|'['
name|'itertools'
op|'.'
name|'ifilter'
op|'('
name|'lambda'
name|'x'
op|':'
name|'x'
op|','
nl|'\n'
name|'line'
op|'.'
name|'rstrip'
op|'('
op|')'
op|'.'
name|'splitlines'
op|'('
op|')'
op|')'
nl|'\n'
name|'for'
name|'line'
name|'in'
name|'lines'
op|']'
newline|'\n'
name|'lines'
op|'='
name|'list'
op|'('
name|'itertools'
op|'.'
name|'chain'
op|'('
op|'*'
name|'lines'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'lines'
newline|'\n'
nl|'\n'
DECL|member|format
dedent|''
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
name|'message'
op|'='
op|'{'
string|"'message'"
op|':'
name|'record'
op|'.'
name|'getMessage'
op|'('
op|')'
op|','
nl|'\n'
string|"'asctime'"
op|':'
name|'self'
op|'.'
name|'formatTime'
op|'('
name|'record'
op|','
name|'self'
op|'.'
name|'datefmt'
op|')'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'record'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'msg'"
op|':'
name|'record'
op|'.'
name|'msg'
op|','
nl|'\n'
string|"'args'"
op|':'
name|'record'
op|'.'
name|'args'
op|','
nl|'\n'
string|"'levelname'"
op|':'
name|'record'
op|'.'
name|'levelname'
op|','
nl|'\n'
string|"'levelno'"
op|':'
name|'record'
op|'.'
name|'levelno'
op|','
nl|'\n'
string|"'pathname'"
op|':'
name|'record'
op|'.'
name|'pathname'
op|','
nl|'\n'
string|"'filename'"
op|':'
name|'record'
op|'.'
name|'filename'
op|','
nl|'\n'
string|"'module'"
op|':'
name|'record'
op|'.'
name|'module'
op|','
nl|'\n'
string|"'lineno'"
op|':'
name|'record'
op|'.'
name|'lineno'
op|','
nl|'\n'
string|"'funcname'"
op|':'
name|'record'
op|'.'
name|'funcName'
op|','
nl|'\n'
string|"'created'"
op|':'
name|'record'
op|'.'
name|'created'
op|','
nl|'\n'
string|"'msecs'"
op|':'
name|'record'
op|'.'
name|'msecs'
op|','
nl|'\n'
string|"'relative_created'"
op|':'
name|'record'
op|'.'
name|'relativeCreated'
op|','
nl|'\n'
string|"'thread'"
op|':'
name|'record'
op|'.'
name|'thread'
op|','
nl|'\n'
string|"'thread_name'"
op|':'
name|'record'
op|'.'
name|'threadName'
op|','
nl|'\n'
string|"'process_name'"
op|':'
name|'record'
op|'.'
name|'processName'
op|','
nl|'\n'
string|"'process'"
op|':'
name|'record'
op|'.'
name|'process'
op|','
nl|'\n'
string|"'traceback'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'hasattr'
op|'('
name|'record'
op|','
string|"'extra'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'message'
op|'['
string|"'extra'"
op|']'
op|'='
name|'record'
op|'.'
name|'extra'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'record'
op|'.'
name|'exc_info'
op|':'
newline|'\n'
indent|'            '
name|'message'
op|'['
string|"'traceback'"
op|']'
op|'='
name|'self'
op|'.'
name|'formatException'
op|'('
name|'record'
op|'.'
name|'exc_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LegacyNovaFormatter
dedent|''
dedent|''
name|'class'
name|'LegacyNovaFormatter'
op|'('
name|'logging'
op|'.'
name|'Formatter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A nova.context.RequestContext aware formatter configured through flags.\n\n    The flags used to set format strings are: logging_context_format_string\n    and logging_default_format_string.  You can also specify\n    logging_debug_format_suffix to append extra formatting if the log level is\n    debug.\n\n    For information about what variables are available for the formatter see:\n    http://docs.python.org/library/logging.html#formatter\n\n    """'
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
string|"'instance'"
name|'not'
name|'in'
name|'record'
op|'.'
name|'__dict__'
op|':'
newline|'\n'
indent|'            '
name|'record'
op|'.'
name|'__dict__'
op|'['
string|"'instance'"
op|']'
op|'='
string|"''"
newline|'\n'
nl|'\n'
dedent|''
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
nl|'\n'
dedent|''
name|'if'
op|'('
name|'record'
op|'.'
name|'levelno'
op|'=='
name|'logging'
op|'.'
name|'DEBUG'
name|'and'
nl|'\n'
name|'FLAGS'
op|'.'
name|'logging_debug_format_suffix'
op|')'
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
nl|'\n'
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
DECL|class|PublishErrorsHandler
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
name|'if'
string|"'list_notifier_drivers'"
name|'in'
name|'FLAGS'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'nova.notifier.log_notifier'"
name|'in'
name|'FLAGS'
op|'.'
name|'list_notifier_drivers'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'nova'
op|'.'
name|'notifier'
op|'.'
name|'api'
op|'.'
name|'notify'
op|'('
string|"'nova.error.publisher'"
op|','
string|"'error_notification'"
op|','
nl|'\n'
name|'nova'
op|'.'
name|'notifier'
op|'.'
name|'api'
op|'.'
name|'ERROR'
op|','
name|'dict'
op|'('
name|'error'
op|'='
name|'record'
op|'.'
name|'msg'
op|')'
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
name|'getLogger'
op|'('
op|')'
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
DECL|function|setup
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
name|'sys'
op|'.'
name|'excepthook'
op|'='
name|'handle_exception'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'log_config'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'config'
op|'.'
name|'fileConfig'
op|'('
name|'FLAGS'
op|'.'
name|'log_config'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'traceback'
op|'.'
name|'print_exc'
op|'('
op|')'
newline|'\n'
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'_setup_logging_from_flags'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_find_facility_from_flags
dedent|''
dedent|''
name|'def'
name|'_find_facility_from_flags'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'facility_names'
op|'='
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'SysLogHandler'
op|'.'
name|'facility_names'
newline|'\n'
name|'facility'
op|'='
name|'getattr'
op|'('
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'SysLogHandler'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'syslog_log_facility'
op|','
nl|'\n'
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'facility'
name|'is'
name|'None'
name|'and'
name|'FLAGS'
op|'.'
name|'syslog_log_facility'
name|'in'
name|'facility_names'
op|':'
newline|'\n'
indent|'        '
name|'facility'
op|'='
name|'facility_names'
op|'.'
name|'get'
op|'('
name|'FLAGS'
op|'.'
name|'syslog_log_facility'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'facility'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'valid_facilities'
op|'='
name|'facility_names'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
name|'consts'
op|'='
op|'['
string|"'LOG_AUTH'"
op|','
string|"'LOG_AUTHPRIV'"
op|','
string|"'LOG_CRON'"
op|','
string|"'LOG_DAEMON'"
op|','
nl|'\n'
string|"'LOG_FTP'"
op|','
string|"'LOG_KERN'"
op|','
string|"'LOG_LPR'"
op|','
string|"'LOG_MAIL'"
op|','
string|"'LOG_NEWS'"
op|','
nl|'\n'
string|"'LOG_AUTH'"
op|','
string|"'LOG_SYSLOG'"
op|','
string|"'LOG_USER'"
op|','
string|"'LOG_UUCP'"
op|','
nl|'\n'
string|"'LOG_LOCAL0'"
op|','
string|"'LOG_LOCAL1'"
op|','
string|"'LOG_LOCAL2'"
op|','
string|"'LOG_LOCAL3'"
op|','
nl|'\n'
string|"'LOG_LOCAL4'"
op|','
string|"'LOG_LOCAL5'"
op|','
string|"'LOG_LOCAL6'"
op|','
string|"'LOG_LOCAL7'"
op|']'
newline|'\n'
name|'valid_facilities'
op|'.'
name|'extend'
op|'('
name|'consts'
op|')'
newline|'\n'
name|'raise'
name|'TypeError'
op|'('
name|'_'
op|'('
string|"'syslog facility must be one of: %s'"
op|')'
op|'%'
nl|'\n'
string|"', '"
op|'.'
name|'join'
op|'('
string|'"\'%s\'"'
op|'%'
name|'fac'
nl|'\n'
name|'for'
name|'fac'
name|'in'
name|'valid_facilities'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'facility'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_setup_logging_from_flags
dedent|''
name|'def'
name|'_setup_logging_from_flags'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'nova_root'
op|'='
name|'getLogger'
op|'('
op|')'
op|'.'
name|'logger'
newline|'\n'
name|'for'
name|'handler'
name|'in'
name|'nova_root'
op|'.'
name|'handlers'
op|':'
newline|'\n'
indent|'        '
name|'nova_root'
op|'.'
name|'removeHandler'
op|'('
name|'handler'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'use_syslog'
op|':'
newline|'\n'
indent|'        '
name|'facility'
op|'='
name|'_find_facility_from_flags'
op|'('
op|')'
newline|'\n'
name|'syslog'
op|'='
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'SysLogHandler'
op|'('
name|'address'
op|'='
string|"'/dev/log'"
op|','
nl|'\n'
name|'facility'
op|'='
name|'facility'
op|')'
newline|'\n'
name|'nova_root'
op|'.'
name|'addHandler'
op|'('
name|'syslog'
op|')'
newline|'\n'
nl|'\n'
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
indent|'        '
name|'filelog'
op|'='
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'WatchedFileHandler'
op|'('
name|'logpath'
op|')'
newline|'\n'
name|'nova_root'
op|'.'
name|'addHandler'
op|'('
name|'filelog'
op|')'
newline|'\n'
nl|'\n'
name|'mode'
op|'='
name|'int'
op|'('
name|'FLAGS'
op|'.'
name|'logfile_mode'
op|','
number|'8'
op|')'
newline|'\n'
name|'st'
op|'='
name|'os'
op|'.'
name|'stat'
op|'('
name|'logpath'
op|')'
newline|'\n'
name|'if'
name|'st'
op|'.'
name|'st_mode'
op|'!='
op|'('
name|'stat'
op|'.'
name|'S_IFREG'
op|'|'
name|'mode'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'chmod'
op|'('
name|'logpath'
op|','
name|'mode'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'use_stderr'
op|':'
newline|'\n'
indent|'        '
name|'streamlog'
op|'='
name|'logging'
op|'.'
name|'StreamHandler'
op|'('
op|')'
newline|'\n'
name|'nova_root'
op|'.'
name|'addHandler'
op|'('
name|'streamlog'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'elif'
name|'not'
name|'FLAGS'
op|'.'
name|'log_file'
op|':'
newline|'\n'
indent|'        '
name|'streamlog'
op|'='
name|'logging'
op|'.'
name|'StreamHandler'
op|'('
name|'stream'
op|'='
name|'sys'
op|'.'
name|'stdout'
op|')'
newline|'\n'
name|'nova_root'
op|'.'
name|'addHandler'
op|'('
name|'streamlog'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'publish_errors'
op|':'
newline|'\n'
indent|'        '
name|'nova_root'
op|'.'
name|'addHandler'
op|'('
name|'PublishErrorsHandler'
op|'('
name|'logging'
op|'.'
name|'ERROR'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'handler'
name|'in'
name|'nova_root'
op|'.'
name|'handlers'
op|':'
newline|'\n'
indent|'        '
name|'datefmt'
op|'='
name|'FLAGS'
op|'.'
name|'log_date_format'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'log_format'
op|':'
newline|'\n'
indent|'            '
name|'handler'
op|'.'
name|'setFormatter'
op|'('
name|'logging'
op|'.'
name|'Formatter'
op|'('
name|'fmt'
op|'='
name|'FLAGS'
op|'.'
name|'log_format'
op|','
nl|'\n'
name|'datefmt'
op|'='
name|'datefmt'
op|')'
op|')'
newline|'\n'
dedent|''
name|'handler'
op|'.'
name|'setFormatter'
op|'('
name|'LegacyNovaFormatter'
op|'('
name|'datefmt'
op|'='
name|'datefmt'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'verbose'
name|'or'
name|'FLAGS'
op|'.'
name|'debug'
op|':'
newline|'\n'
indent|'        '
name|'nova_root'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'nova_root'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'INFO'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'level'
op|'='
name|'logging'
op|'.'
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
indent|'        '
name|'mod'
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
name|'level'
op|'='
name|'logging'
op|'.'
name|'getLevelName'
op|'('
name|'level_name'
op|')'
newline|'\n'
name|'logger'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'mod'
op|')'
newline|'\n'
name|'logger'
op|'.'
name|'setLevel'
op|'('
name|'level'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(jkoelker) Clear the handlers for the root logger that was setup'
nl|'\n'
comment|'#                by basicConfig in nova/__init__.py and install the'
nl|'\n'
comment|'#                NullHandler.'
nl|'\n'
dedent|''
name|'root'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
newline|'\n'
name|'for'
name|'handler'
name|'in'
name|'root'
op|'.'
name|'handlers'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'.'
name|'removeHandler'
op|'('
name|'handler'
op|')'
newline|'\n'
dedent|''
name|'handler'
op|'='
name|'NullHandler'
op|'('
op|')'
newline|'\n'
name|'handler'
op|'.'
name|'setFormatter'
op|'('
name|'logging'
op|'.'
name|'Formatter'
op|'('
op|')'
op|')'
newline|'\n'
name|'root'
op|'.'
name|'addHandler'
op|'('
name|'handler'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_loggers
dedent|''
name|'_loggers'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|getLogger
name|'def'
name|'getLogger'
op|'('
name|'name'
op|'='
string|"'nova'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'name'
name|'not'
name|'in'
name|'_loggers'
op|':'
newline|'\n'
indent|'        '
name|'_loggers'
op|'['
name|'name'
op|']'
op|'='
name|'NovaContextAdapter'
op|'('
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'name'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_loggers'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WritableLogger
dedent|''
name|'class'
name|'WritableLogger'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A thin wrapper that responds to `write` and logs."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'logger'
op|','
name|'level'
op|'='
name|'logging'
op|'.'
name|'INFO'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'logger'
op|'='
name|'logger'
newline|'\n'
name|'self'
op|'.'
name|'level'
op|'='
name|'level'
newline|'\n'
nl|'\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'logger'
op|'.'
name|'log'
op|'('
name|'self'
op|'.'
name|'level'
op|','
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
