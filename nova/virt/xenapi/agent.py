begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2010-2012 OpenStack LLC.'
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
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'binascii'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
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
name|'import'
name|'utils'
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
DECL|variable|xenapi_agent_opts
name|'xenapi_agent_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'agent_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'30'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'number of seconds to wait for agent reply'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'agent_version_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'300'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'number of seconds to wait for agent '"
nl|'\n'
string|"'to be fully operational'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'agent_resetnetwork_timeout'"
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
string|"'number of seconds to wait for agent reply '"
nl|'\n'
string|"'to resetnetwork request'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'xenapi_agent_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'usr/sbin/xe-update-networking'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Specifies the path in which the xenapi guest agent '"
nl|'\n'
string|"'should be located. If the agent is present, network '"
nl|'\n'
string|"'configuration is not injected into the image. '"
nl|'\n'
string|"'Used if compute_driver=xenapi.XenAPIDriver and '"
nl|'\n'
string|"' flat_injected=True'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'xenapi_disable_agent'"
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
string|"'Disable XenAPI agent. Reduces the amount of time '"
nl|'\n'
string|"'it takes nova to detect that a VM has started, when '"
nl|'\n'
string|"'that VM does not have the agent installed'"
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
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'xenapi_agent_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_call_agent
name|'def'
name|'_call_agent'
op|'('
name|'session'
op|','
name|'instance'
op|','
name|'vm_ref'
op|','
name|'method'
op|','
name|'addl_args'
op|'='
name|'None'
op|','
nl|'\n'
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Abstracts out the interaction with the agent xenapi plugin."""'
newline|'\n'
name|'if'
name|'addl_args'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'addl_args'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'if'
name|'timeout'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'timeout'
op|'='
name|'CONF'
op|'.'
name|'agent_timeout'
newline|'\n'
nl|'\n'
dedent|''
name|'vm_rec'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VM.get_record"'
op|','
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
name|'args'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'dom_id'"
op|':'
name|'vm_rec'
op|'['
string|"'domid'"
op|']'
op|','
nl|'\n'
string|"'timeout'"
op|':'
name|'str'
op|'('
name|'timeout'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'args'
op|'.'
name|'update'
op|'('
name|'addl_args'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'ret'
op|'='
name|'session'
op|'.'
name|'call_plugin'
op|'('
string|"'agent'"
op|','
name|'method'
op|','
name|'args'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'err_msg'
op|'='
name|'e'
op|'.'
name|'details'
op|'['
op|'-'
number|'1'
op|']'
op|'.'
name|'splitlines'
op|'('
op|')'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'if'
string|"'TIMEOUT:'"
name|'in'
name|'err_msg'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'TIMEOUT: The call to %(method)s timed out. '"
nl|'\n'
string|"'args=%(args)r'"
op|')'
op|','
name|'locals'
op|'('
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'returncode'"
op|':'
string|"'timeout'"
op|','
string|"'message'"
op|':'
name|'err_msg'
op|'}'
newline|'\n'
dedent|''
name|'elif'
string|"'NOT IMPLEMENTED:'"
name|'in'
name|'err_msg'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'NOT IMPLEMENTED: The call to %(method)s is not'"
nl|'\n'
string|"' supported by the agent. args=%(args)r'"
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'returncode'"
op|':'
string|"'notimplemented'"
op|','
string|"'message'"
op|':'
name|'err_msg'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'The call to %(method)s returned an error: %(e)s. '"
nl|'\n'
string|"'args=%(args)r'"
op|')'
op|','
name|'locals'
op|'('
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'returncode'"
op|':'
string|"'error'"
op|','
string|"'message'"
op|':'
name|'err_msg'
op|'}'
newline|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'ret'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'ret'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'ret'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'The agent call to %(method)s returned an invalid'"
nl|'\n'
string|"' response: %(ret)r. path=%(path)s; args=%(args)r'"
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'returncode'"
op|':'
string|"'error'"
op|','
nl|'\n'
string|"'message'"
op|':'
string|"'unable to deserialize response'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_agent_version
dedent|''
dedent|''
name|'def'
name|'_get_agent_version'
op|'('
name|'session'
op|','
name|'instance'
op|','
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'resp'
op|'='
name|'_call_agent'
op|'('
name|'session'
op|','
name|'instance'
op|','
name|'vm_ref'
op|','
string|"'version'"
op|')'
newline|'\n'
name|'if'
name|'resp'
op|'['
string|"'returncode'"
op|']'
op|'!='
string|"'0'"
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Failed to query agent version: %(resp)r'"
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
comment|'# Some old versions of the Windows agent have a trailing \\\\r\\\\n'
nl|'\n'
comment|'# (ie CRLF escaped) for some reason. Strip that off.'
nl|'\n'
dedent|''
name|'return'
name|'resp'
op|'['
string|"'message'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'\\\\r\\\\n'"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIBasedAgent
dedent|''
name|'class'
name|'XenAPIBasedAgent'
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
name|'session'
op|','
name|'instance'
op|','
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'='
name|'session'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'instance'
newline|'\n'
name|'self'
op|'.'
name|'vm_ref'
op|'='
name|'vm_ref'
newline|'\n'
nl|'\n'
DECL|member|get_agent_version
dedent|''
name|'def'
name|'get_agent_version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the version of the agent running on the VM instance."""'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Querying agent version'"
op|')'
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|'# The agent can be slow to start for a variety of reasons. On Windows,'
nl|'\n'
comment|'# it will generally perform a setup process on first boot that can'
nl|'\n'
comment|'# take a couple of minutes and then reboot. On Linux, the system can'
nl|'\n'
comment|'# also take a while to boot. So we need to be more patient than'
nl|'\n'
comment|'# normal as well as watch for domid changes'
nl|'\n'
nl|'\n'
name|'expiration'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'+'
name|'CONF'
op|'.'
name|'agent_version_timeout'
newline|'\n'
name|'while'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'<'
name|'expiration'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'='
name|'_get_agent_version'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'vm_ref'
op|')'
newline|'\n'
name|'if'
name|'ret'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Reached maximum time attempting to query agent version'"
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|agent_update
dedent|''
name|'def'
name|'agent_update'
op|'('
name|'self'
op|','
name|'agent_build'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update agent on the VM instance."""'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Updating agent to %s'"
op|')'
op|','
name|'agent_build'
op|'['
string|"'version'"
op|']'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|'# Send the encrypted password'
nl|'\n'
name|'args'
op|'='
op|'{'
string|"'url'"
op|':'
name|'agent_build'
op|'['
string|"'url'"
op|']'
op|','
string|"'md5sum'"
op|':'
name|'agent_build'
op|'['
string|"'md5hash'"
op|']'
op|'}'
newline|'\n'
name|'resp'
op|'='
name|'_call_agent'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'vm_ref'
op|','
string|"'agentupdate'"
op|','
name|'args'
op|')'
newline|'\n'
name|'if'
name|'resp'
op|'['
string|"'returncode'"
op|']'
op|'!='
string|"'0'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Failed to update agent: %(resp)r'"
op|')'
op|','
name|'locals'
op|'('
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'resp'
op|'['
string|"'message'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|set_admin_password
dedent|''
name|'def'
name|'set_admin_password'
op|'('
name|'self'
op|','
name|'new_pass'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Set the root/admin password on the VM instance.\n\n        This is done via an agent running on the VM. Communication between nova\n        and the agent is done via writing xenstore records. Since communication\n        is done over the XenAPI RPC calls, we need to encrypt the password.\n        We\'re using a simple Diffie-Hellman class instead of a more advanced\n        library (such as M2Crypto) for compatibility with the agent code.\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Setting admin password'"
op|')'
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'dh'
op|'='
name|'SimpleDH'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Exchange keys'
nl|'\n'
name|'args'
op|'='
op|'{'
string|"'pub'"
op|':'
name|'str'
op|'('
name|'dh'
op|'.'
name|'get_public'
op|'('
op|')'
op|')'
op|'}'
newline|'\n'
name|'resp'
op|'='
name|'_call_agent'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'vm_ref'
op|','
string|"'key_init'"
op|','
name|'args'
op|')'
newline|'\n'
nl|'\n'
comment|"# Successful return code from key_init is 'D0'"
nl|'\n'
name|'if'
name|'resp'
op|'['
string|"'returncode'"
op|']'
op|'!='
string|"'D0'"
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Failed to exchange keys: %(resp)r'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
comment|'# Some old versions of the Windows agent have a trailing \\\\r\\\\n'
nl|'\n'
comment|'# (ie CRLF escaped) for some reason. Strip that off.'
nl|'\n'
dedent|''
name|'agent_pub'
op|'='
name|'int'
op|'('
name|'resp'
op|'['
string|"'message'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'\\\\r\\\\n'"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
name|'dh'
op|'.'
name|'compute_shared'
op|'('
name|'agent_pub'
op|')'
newline|'\n'
nl|'\n'
comment|'# Some old versions of Linux and Windows agent expect trailing \\n'
nl|'\n'
comment|'# on password to work correctly.'
nl|'\n'
name|'enc_pass'
op|'='
name|'dh'
op|'.'
name|'encrypt'
op|'('
name|'new_pass'
op|'+'
string|"'\\n'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Send the encrypted password'
nl|'\n'
name|'args'
op|'='
op|'{'
string|"'enc_pass'"
op|':'
name|'enc_pass'
op|'}'
newline|'\n'
name|'resp'
op|'='
name|'_call_agent'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'vm_ref'
op|','
string|"'password'"
op|','
name|'args'
op|')'
newline|'\n'
nl|'\n'
comment|"# Successful return code from password is '0'"
nl|'\n'
name|'if'
name|'resp'
op|'['
string|"'returncode'"
op|']'
op|'!='
string|"'0'"
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Failed to update password: %(resp)r'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'resp'
op|'['
string|"'message'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|inject_file
dedent|''
name|'def'
name|'inject_file'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'contents'
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
string|"'Injecting file path: %r'"
op|')'
op|','
name|'path'
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|'# Files/paths must be base64-encoded for transmission to agent'
nl|'\n'
name|'b64_path'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'path'
op|')'
newline|'\n'
name|'b64_contents'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'contents'
op|')'
newline|'\n'
nl|'\n'
name|'args'
op|'='
op|'{'
string|"'b64_path'"
op|':'
name|'b64_path'
op|','
string|"'b64_contents'"
op|':'
name|'b64_contents'
op|'}'
newline|'\n'
nl|'\n'
comment|"# If the agent doesn't support file injection, a NotImplementedError"
nl|'\n'
comment|'# will be raised with the appropriate message.'
nl|'\n'
name|'resp'
op|'='
name|'_call_agent'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'vm_ref'
op|','
string|"'inject_file'"
op|','
name|'args'
op|')'
newline|'\n'
name|'if'
name|'resp'
op|'['
string|"'returncode'"
op|']'
op|'!='
string|"'0'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Failed to inject file: %(resp)r'"
op|')'
op|','
name|'locals'
op|'('
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'resp'
op|'['
string|"'message'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|resetnetwork
dedent|''
name|'def'
name|'resetnetwork'
op|'('
name|'self'
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
string|"'Resetting network'"
op|')'
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'resp'
op|'='
name|'_call_agent'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'vm_ref'
op|','
string|"'resetnetwork'"
op|','
nl|'\n'
name|'timeout'
op|'='
name|'CONF'
op|'.'
name|'agent_resetnetwork_timeout'
op|')'
newline|'\n'
name|'if'
name|'resp'
op|'['
string|"'returncode'"
op|']'
op|'!='
string|"'0'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Failed to reset network: %(resp)r'"
op|')'
op|','
name|'locals'
op|'('
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'resp'
op|'['
string|"'message'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_guest_agent
dedent|''
dedent|''
name|'def'
name|'find_guest_agent'
op|'('
name|'base_dir'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    tries to locate a guest agent at the path\n    specificed by agent_rel_path\n    """'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'xenapi_disable_agent'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'agent_rel_path'
op|'='
name|'CONF'
op|'.'
name|'xenapi_agent_path'
newline|'\n'
name|'agent_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'base_dir'
op|','
name|'agent_rel_path'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isfile'
op|'('
name|'agent_path'
op|')'
op|':'
newline|'\n'
comment|'# The presence of the guest agent'
nl|'\n'
comment|'# file indicates that this instance can'
nl|'\n'
comment|'# reconfigure the network from xenstore data,'
nl|'\n'
comment|'# so manipulation of files in /etc is not'
nl|'\n'
comment|'# required'
nl|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'XenServer tools installed in this '"
nl|'\n'
string|"'image are capable of network injection.  '"
nl|'\n'
string|"'Networking files will not be'"
nl|'\n'
string|"'manipulated'"
op|')'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'xe_daemon_filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'base_dir'
op|','
nl|'\n'
string|"'usr'"
op|','
string|"'sbin'"
op|','
string|"'xe-daemon'"
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isfile'
op|'('
name|'xe_daemon_filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'XenServer tools are present '"
nl|'\n'
string|"'in this image but are not capable '"
nl|'\n'
string|"'of network injection'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'XenServer tools are not '"
nl|'\n'
string|"'installed in this image'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleDH
dedent|''
name|'class'
name|'SimpleDH'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    This class wraps all the functionality needed to implement\n    basic Diffie-Hellman-Merkle key exchange in Python. It features\n    intelligent defaults for the prime and base numbers needed for the\n    calculation, while allowing you to supply your own. It requires that\n    the openssl binary be installed on the system on which this is run,\n    as it uses that to handle the encryption and decryption. If openssl\n    is not available, a RuntimeError will be raised.\n    """'
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
name|'_prime'
op|'='
number|'162259276829213363391578010288127'
newline|'\n'
name|'self'
op|'.'
name|'_base'
op|'='
number|'5'
newline|'\n'
name|'self'
op|'.'
name|'_public'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_shared'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'generate_private'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|generate_private
dedent|''
name|'def'
name|'generate_private'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_private'
op|'='
name|'int'
op|'('
name|'binascii'
op|'.'
name|'hexlify'
op|'('
name|'os'
op|'.'
name|'urandom'
op|'('
number|'10'
op|')'
op|')'
op|','
number|'16'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_private'
newline|'\n'
nl|'\n'
DECL|member|get_public
dedent|''
name|'def'
name|'get_public'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_public'
op|'='
name|'self'
op|'.'
name|'mod_exp'
op|'('
name|'self'
op|'.'
name|'_base'
op|','
name|'self'
op|'.'
name|'_private'
op|','
name|'self'
op|'.'
name|'_prime'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_public'
newline|'\n'
nl|'\n'
DECL|member|compute_shared
dedent|''
name|'def'
name|'compute_shared'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_shared'
op|'='
name|'self'
op|'.'
name|'mod_exp'
op|'('
name|'other'
op|','
name|'self'
op|'.'
name|'_private'
op|','
name|'self'
op|'.'
name|'_prime'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_shared'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|mod_exp
name|'def'
name|'mod_exp'
op|'('
name|'num'
op|','
name|'exp'
op|','
name|'mod'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Efficient implementation of (num ** exp) % mod."""'
newline|'\n'
name|'result'
op|'='
number|'1'
newline|'\n'
name|'while'
name|'exp'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'exp'
op|'&'
number|'1'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
op|'('
name|'result'
op|'*'
name|'num'
op|')'
op|'%'
name|'mod'
newline|'\n'
dedent|''
name|'exp'
op|'='
name|'exp'
op|'>>'
number|'1'
newline|'\n'
name|'num'
op|'='
op|'('
name|'num'
op|'*'
name|'num'
op|')'
op|'%'
name|'mod'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|_run_ssl
dedent|''
name|'def'
name|'_run_ssl'
op|'('
name|'self'
op|','
name|'text'
op|','
name|'decrypt'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cmd'
op|'='
op|'['
string|"'openssl'"
op|','
string|"'aes-128-cbc'"
op|','
string|"'-A'"
op|','
string|"'-a'"
op|','
string|"'-pass'"
op|','
nl|'\n'
string|"'pass:%s'"
op|'%'
name|'self'
op|'.'
name|'_shared'
op|','
string|"'-nosalt'"
op|']'
newline|'\n'
name|'if'
name|'decrypt'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'.'
name|'append'
op|'('
string|"'-d'"
op|')'
newline|'\n'
dedent|''
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|','
name|'process_input'
op|'='
name|'text'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|"'OpenSSL error: %s'"
op|')'
op|'%'
name|'err'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'out'
newline|'\n'
nl|'\n'
DECL|member|encrypt
dedent|''
name|'def'
name|'encrypt'
op|'('
name|'self'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_run_ssl'
op|'('
name|'text'
op|')'
op|'.'
name|'strip'
op|'('
string|"'\\n'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|decrypt
dedent|''
name|'def'
name|'decrypt'
op|'('
name|'self'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_run_ssl'
op|'('
name|'text'
op|','
name|'decrypt'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
