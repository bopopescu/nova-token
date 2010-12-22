begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
string|'"""\nA connection to XenServer or Xen Cloud Platform.\n\nThe concurrency model for this class is as follows:\n\nAll XenAPI calls are on a thread (using t.i.t.deferToThread, via the decorator\ndeferredToThread).  They are remote calls, and so may hang for the usual\nreasons.  They should not be allowed to block the reactor thread.\n\nAll long-running XenAPI calls (VM.start, VM.reboot, etc) are called async\n(using XenAPI.VM.async_start etc).  These return a task, which can then be\npolled for completion.  Polling is handled using reactor.callLater.\n\nThis combination of techniques means that we don\'t block the reactor thread at\nall, and at the same time we don\'t hold lots of threads waiting for\nlong-running operations.\n\nFIXME: get_info currently doesn\'t conform to these rules, and will block the\nreactor thread if the VM.get_by_name_label or VM.get_record calls block.\n\n**Related Flags**\n\n:xenapi_connection_url:  URL for connection to XenServer/Xen Cloud Platform.\n:xenapi_connection_username:  Username for connection to XenServer/Xen Cloud\n                              Platform (default: root).\n:xenapi_connection_password:  Password for connection to XenServer/Xen Cloud\n                              Platform.\n:xenapi_task_poll_interval:  The interval (seconds) used for polling of\n                             remote tasks (Async.VM.start, etc)\n                             (default: 0.5).\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'xmlrpclib'
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
name|'tpool'
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
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'vmops'
name|'import'
name|'VMOps'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'volumeops'
name|'import'
name|'VolumeOps'
newline|'\n'
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
string|"'xenapi_connection_url'"
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
string|"'URL for connection to XenServer/Xen Cloud Platform.'"
nl|'\n'
string|"' Required if connection_type=xenapi.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'xenapi_connection_username'"
op|','
nl|'\n'
string|"'root'"
op|','
nl|'\n'
string|"'Username for connection to XenServer/Xen Cloud Platform.'"
nl|'\n'
string|"' Used only if connection_type=xenapi.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'xenapi_connection_password'"
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
string|"'Password for connection to XenServer/Xen Cloud Platform.'"
nl|'\n'
string|"' Used only if connection_type=xenapi.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_float'
op|'('
string|"'xenapi_task_poll_interval'"
op|','
nl|'\n'
number|'0.5'
op|','
nl|'\n'
string|"'The interval used for polling of remote tasks '"
nl|'\n'
string|"'(Async.VM.start, etc).  Used only if '"
nl|'\n'
string|"'connection_type=xenapi.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_float'
op|'('
string|"'xenapi_vhd_coalesce_poll_interval'"
op|','
nl|'\n'
number|'5.0'
op|','
nl|'\n'
string|"'The interval used for polling of coalescing vhds.'"
nl|'\n'
string|"'  Used only if connection_type=xenapi.'"
op|')'
newline|'\n'
DECL|variable|XenAPI
name|'XenAPI'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_connection
name|'def'
name|'get_connection'
op|'('
name|'_'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Note that XenAPI doesn\'t have a read-only connection mode, so\n    the read_only parameter is ignored."""'
newline|'\n'
comment|"# This is loaded late so that there's no need to install this"
nl|'\n'
comment|'# library when not using XenAPI.'
nl|'\n'
name|'global'
name|'XenAPI'
newline|'\n'
name|'if'
name|'XenAPI'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'XenAPI'
op|'='
name|'__import__'
op|'('
string|"'XenAPI'"
op|')'
newline|'\n'
dedent|''
name|'url'
op|'='
name|'FLAGS'
op|'.'
name|'xenapi_connection_url'
newline|'\n'
name|'username'
op|'='
name|'FLAGS'
op|'.'
name|'xenapi_connection_username'
newline|'\n'
name|'password'
op|'='
name|'FLAGS'
op|'.'
name|'xenapi_connection_password'
newline|'\n'
name|'if'
name|'not'
name|'url'
name|'or'
name|'password'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Must specify xenapi_connection_url, '"
nl|'\n'
string|"'xenapi_connection_username (optionally), and '"
nl|'\n'
string|"'xenapi_connection_password to use '"
nl|'\n'
string|"'connection_type=xenapi'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'XenAPIConnection'
op|'('
name|'url'
op|','
name|'username'
op|','
name|'password'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIConnection
dedent|''
name|'class'
name|'XenAPIConnection'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A connection to XenServer or Xen Cloud Platform"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'XenAPISession'
op|'('
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'='
name|'VMOps'
op|'('
name|'session'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'='
name|'VolumeOps'
op|'('
name|'session'
op|')'
newline|'\n'
nl|'\n'
DECL|member|list_instances
dedent|''
name|'def'
name|'list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List VM instances"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|spawn
dedent|''
name|'def'
name|'spawn'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create VM instance"""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'spawn'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|snapshot
dedent|''
name|'def'
name|'snapshot'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Create snapshot from a running VM instance """'
newline|'\n'
comment|'#TODO(sirp): Add quiesce and VSS locking support when Windows support'
nl|'\n'
comment|'# is added'
nl|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'snapshot'
op|'('
name|'instance'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reboot
dedent|''
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboot VM instance"""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'reboot'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy VM instance"""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'destroy'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|pause
dedent|''
name|'def'
name|'pause'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Pause VM instance"""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'pause'
op|'('
name|'instance'
op|','
name|'callback'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unpause
dedent|''
name|'def'
name|'unpause'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unpause paused VM instance"""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'unpause'
op|'('
name|'instance'
op|','
name|'callback'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about VM instance"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_info'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_diagnostics
dedent|''
name|'def'
name|'get_diagnostics'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about VM diagnostics"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_diagnostics'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_console_output
dedent|''
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return snapshot of console"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_console_output'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'device_path'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach volume storage to VM instance"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'attach_volume'
op|'('
name|'instance_name'
op|','
nl|'\n'
name|'device_path'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_volume
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach volume storage to VM instance"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'detach_volume'
op|'('
name|'instance_name'
op|','
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPISession
dedent|''
dedent|''
name|'class'
name|'XenAPISession'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The session to invoke XenAPI SDK calls"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_session'
op|'='
name|'XenAPI'
op|'.'
name|'Session'
op|'('
name|'url'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'login_with_password'
op|'('
name|'user'
op|','
name|'pw'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_xenapi
dedent|''
name|'def'
name|'get_xenapi'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the xenapi object"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
newline|'\n'
nl|'\n'
DECL|member|get_xenapi_host
dedent|''
name|'def'
name|'get_xenapi_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the xenapi host"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'session'
op|'.'
name|'get_this_host'
op|'('
name|'self'
op|'.'
name|'_session'
op|'.'
name|'handle'
op|')'
newline|'\n'
nl|'\n'
DECL|member|call_xenapi
dedent|''
name|'def'
name|'call_xenapi'
op|'('
name|'self'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call the specified XenAPI method on a background thread."""'
newline|'\n'
name|'f'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
newline|'\n'
name|'for'
name|'m'
name|'in'
name|'method'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'='
name|'f'
op|'.'
name|'__getattr__'
op|'('
name|'m'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'tpool'
op|'.'
name|'execute'
op|'('
name|'f'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|async_call_plugin
dedent|''
name|'def'
name|'async_call_plugin'
op|'('
name|'self'
op|','
name|'plugin'
op|','
name|'fn'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call Async.host.call_plugin on a background thread."""'
newline|'\n'
name|'return'
name|'tpool'
op|'.'
name|'execute'
op|'('
name|'_unwrap_plugin_exceptions'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'Async'
op|'.'
name|'host'
op|'.'
name|'call_plugin'
op|','
nl|'\n'
name|'self'
op|'.'
name|'get_xenapi_host'
op|'('
op|')'
op|','
name|'plugin'
op|','
name|'fn'
op|','
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait_for_task
dedent|''
name|'def'
name|'wait_for_task'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'task'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a Deferred that will give the result of the given task.\n        The task is polled until it completes."""'
newline|'\n'
nl|'\n'
name|'done'
op|'='
name|'event'
op|'.'
name|'Event'
op|'('
op|')'
newline|'\n'
name|'loop'
op|'='
name|'utils'
op|'.'
name|'LoopingCall'
op|'('
name|'self'
op|'.'
name|'_poll_task'
op|','
name|'instance_id'
op|','
name|'task'
op|','
name|'done'
op|')'
newline|'\n'
name|'loop'
op|'.'
name|'start'
op|'('
name|'FLAGS'
op|'.'
name|'xenapi_task_poll_interval'
op|','
name|'now'
op|'='
name|'True'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'done'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'loop'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
DECL|member|_poll_task
dedent|''
name|'def'
name|'_poll_task'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'task'
op|','
name|'done'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Poll the given XenAPI task, and fire the given Deferred if we\n        get a result."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'task'
op|'.'
name|'get_name_label'
op|'('
name|'task'
op|')'
newline|'\n'
name|'status'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'task'
op|'.'
name|'get_status'
op|'('
name|'task'
op|')'
newline|'\n'
name|'action'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'instance_id'
op|'='
name|'int'
op|'('
name|'instance_id'
op|')'
op|','
nl|'\n'
name|'action'
op|'='
name|'name'
op|','
nl|'\n'
name|'error'
op|'='
name|'None'
op|')'
newline|'\n'
name|'if'
name|'status'
op|'=='
string|'"pending"'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
name|'elif'
name|'status'
op|'=='
string|'"success"'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'task'
op|'.'
name|'get_result'
op|'('
name|'task'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Task [%s] %s status: success    %s"'
op|')'
op|'%'
op|'('
nl|'\n'
name|'name'
op|','
nl|'\n'
name|'task'
op|','
nl|'\n'
name|'result'
op|')'
op|')'
newline|'\n'
name|'done'
op|'.'
name|'send'
op|'('
name|'_parse_xmlrpc_value'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'error_info'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'task'
op|'.'
name|'get_error_info'
op|'('
name|'task'
op|')'
newline|'\n'
name|'action'
op|'['
string|'"error"'
op|']'
op|'='
name|'str'
op|'('
name|'error_info'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Task [%s] %s status: %s    %s"'
op|')'
op|'%'
op|'('
nl|'\n'
name|'name'
op|','
nl|'\n'
name|'task'
op|','
nl|'\n'
name|'status'
op|','
nl|'\n'
name|'error_info'
op|')'
op|')'
newline|'\n'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
name|'error_info'
op|')'
op|')'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'instance_action_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'action'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'done'
op|'.'
name|'send_exception'
op|'('
op|'*'
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_unwrap_plugin_exceptions
dedent|''
dedent|''
dedent|''
name|'def'
name|'_unwrap_plugin_exceptions'
op|'('
name|'func'
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
string|'"""Parse exception details"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'func'
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
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Got exception: %s"'
op|')'
op|','
name|'exc'
op|')'
newline|'\n'
name|'if'
op|'('
name|'len'
op|'('
name|'exc'
op|'.'
name|'details'
op|')'
op|'=='
number|'4'
name|'and'
nl|'\n'
name|'exc'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'=='
string|"'XENAPI_PLUGIN_EXCEPTION'"
name|'and'
nl|'\n'
name|'exc'
op|'.'
name|'details'
op|'['
number|'2'
op|']'
op|'=='
string|"'Failure'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'params'
op|'='
name|'eval'
op|'('
name|'exc'
op|'.'
name|'details'
op|'['
number|'3'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exc'
newline|'\n'
dedent|''
name|'raise'
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
name|'params'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'xmlrpclib'
op|'.'
name|'ProtocolError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Got exception: %s"'
op|')'
op|','
name|'exc'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_parse_xmlrpc_value
dedent|''
dedent|''
name|'def'
name|'_parse_xmlrpc_value'
op|'('
name|'val'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse the given value as if it were an XML-RPC value.  This is\n    sometimes used as the format for the task.result field."""'
newline|'\n'
name|'if'
name|'not'
name|'val'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'val'
newline|'\n'
dedent|''
name|'x'
op|'='
name|'xmlrpclib'
op|'.'
name|'loads'
op|'('
nl|'\n'
string|'\'<?xml version="1.0"?><methodResponse><params><param>\''
op|'+'
nl|'\n'
name|'val'
op|'+'
nl|'\n'
string|"'</param></params></methodResponse>'"
op|')'
newline|'\n'
name|'return'
name|'x'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
