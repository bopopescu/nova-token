begin_unit
comment|'# Copyright (c) 2012 VMware, Inc.'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
string|'"""\nUtility classes for defining the time saving transfer of data from the reader\nto the write using a LightQueue as a Pipe between the reader and the writer.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'event'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'queue'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
op|','
name|'_LE'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'image'
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
DECL|variable|IMAGE_API
name|'IMAGE_API'
op|'='
name|'image'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|variable|IO_THREAD_SLEEP_TIME
name|'IO_THREAD_SLEEP_TIME'
op|'='
number|'.01'
newline|'\n'
DECL|variable|GLANCE_POLL_INTERVAL
name|'GLANCE_POLL_INTERVAL'
op|'='
number|'5'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ThreadSafePipe
name|'class'
name|'ThreadSafePipe'
op|'('
name|'queue'
op|'.'
name|'LightQueue'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The pipe to hold the data which the reader writes to and the writer\n    reads from.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'maxsize'
op|','
name|'transfer_size'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'queue'
op|'.'
name|'LightQueue'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'maxsize'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'transfer_size'
op|'='
name|'transfer_size'
newline|'\n'
name|'self'
op|'.'
name|'transferred'
op|'='
number|'0'
newline|'\n'
nl|'\n'
DECL|member|read
dedent|''
name|'def'
name|'read'
op|'('
name|'self'
op|','
name|'chunk_size'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Read data from the pipe.\n\n        Chunksize if ignored for we have ensured\n        that the data chunks written to the pipe by readers is the same as the\n        chunks asked for by the Writer.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'transfer_size'
op|'=='
number|'0'
name|'or'
name|'self'
op|'.'
name|'transferred'
op|'<'
name|'self'
op|'.'
name|'transfer_size'
op|':'
newline|'\n'
indent|'            '
name|'data_item'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'transferred'
op|'+='
name|'len'
op|'('
name|'data_item'
op|')'
newline|'\n'
name|'return'
name|'data_item'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'""'
newline|'\n'
nl|'\n'
DECL|member|write
dedent|''
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Put a data item in the pipe."""'
newline|'\n'
name|'self'
op|'.'
name|'put'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|seek
dedent|''
name|'def'
name|'seek'
op|'('
name|'self'
op|','
name|'offset'
op|','
name|'whence'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Set the file\'s current position at the offset."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|tell
dedent|''
name|'def'
name|'tell'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get size of the file to be read."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'transfer_size'
newline|'\n'
nl|'\n'
DECL|member|close
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""A place-holder to maintain consistency."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GlanceWriteThread
dedent|''
dedent|''
name|'class'
name|'GlanceWriteThread'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensures that image data is written to in the glance client and that\n    it is in correct (\'active\')state.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'input'
op|','
name|'image_id'
op|','
nl|'\n'
name|'image_meta'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'image_meta'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
newline|'\n'
name|'self'
op|'.'
name|'input'
op|'='
name|'input'
newline|'\n'
name|'self'
op|'.'
name|'image_id'
op|'='
name|'image_id'
newline|'\n'
name|'self'
op|'.'
name|'image_meta'
op|'='
name|'image_meta'
newline|'\n'
name|'self'
op|'.'
name|'_running'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'done'
op|'='
name|'event'
op|'.'
name|'Event'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|_inner
name|'def'
name|'_inner'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Function to do the image data transfer through an update\n            and thereon checks if the state is \'active\'.\n            """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'IMAGE_API'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'image_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'image_meta'
op|','
nl|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'input'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_running'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ImageNotAuthorized'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'while'
name|'self'
op|'.'
name|'_running'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'image_meta'
op|'='
name|'IMAGE_API'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'image_id'
op|')'
newline|'\n'
name|'image_status'
op|'='
name|'image_meta'
op|'.'
name|'get'
op|'('
string|'"status"'
op|')'
newline|'\n'
name|'if'
name|'image_status'
op|'=='
string|'"active"'
op|':'
newline|'\n'
indent|'                        '
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'done'
op|'.'
name|'send'
op|'('
name|'True'
op|')'
newline|'\n'
comment|'# If the state is killed, then raise an exception.'
nl|'\n'
dedent|''
name|'elif'
name|'image_status'
op|'=='
string|'"killed"'
op|':'
newline|'\n'
indent|'                        '
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Glance image %s is in killed state"'
op|')'
op|'%'
nl|'\n'
name|'self'
op|'.'
name|'image_id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'msg'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'image_status'
name|'in'
op|'['
string|'"saving"'
op|','
string|'"queued"'
op|']'
op|':'
newline|'\n'
indent|'                        '
name|'greenthread'
op|'.'
name|'sleep'
op|'('
name|'GLANCE_POLL_INTERVAL'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Glance image "'
nl|'\n'
string|'"%(image_id)s is in unknown state "'
nl|'\n'
string|'"- %(state)s"'
op|')'
op|'%'
op|'{'
nl|'\n'
string|'"image_id"'
op|':'
name|'self'
op|'.'
name|'image_id'
op|','
nl|'\n'
string|'"state"'
op|':'
name|'image_status'
op|'}'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'msg'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'greenthread'
op|'.'
name|'spawn'
op|'('
name|'_inner'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'done'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_running'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'done'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|close
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IOThread
dedent|''
dedent|''
name|'class'
name|'IOThread'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Class that reads chunks from the input file and writes them to the\n    output file till the transfer is completely done.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'input'
op|','
name|'output'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'input'
op|'='
name|'input'
newline|'\n'
name|'self'
op|'.'
name|'output'
op|'='
name|'output'
newline|'\n'
name|'self'
op|'.'
name|'_running'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'got_exception'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'done'
op|'='
name|'event'
op|'.'
name|'Event'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|_inner
name|'def'
name|'_inner'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Read data from the input and write the same to the output\n            until the transfer completes.\n            """'
newline|'\n'
name|'self'
op|'.'
name|'_running'
op|'='
name|'True'
newline|'\n'
name|'while'
name|'self'
op|'.'
name|'_running'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'data'
op|'='
name|'self'
op|'.'
name|'input'
op|'.'
name|'read'
op|'('
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'data'
op|':'
newline|'\n'
indent|'                        '
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'done'
op|'.'
name|'send'
op|'('
name|'True'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'output'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
name|'IO_THREAD_SLEEP_TIME'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|"'Read/Write data failed'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'greenthread'
op|'.'
name|'spawn'
op|'('
name|'_inner'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'done'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_running'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'done'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
