begin_unit
comment|'# Copyright 2015 NTT corp.'
nl|'\n'
comment|'# All Rights Reserved.'
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
nl|'\n'
name|'import'
name|'collections'
newline|'\n'
name|'import'
name|'errno'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'signal'
newline|'\n'
nl|'\n'
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
op|'.'
name|'i18n'
name|'import'
name|'_LE'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LW'
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
nl|'\n'
DECL|class|InstanceJobTracker
name|'class'
name|'InstanceJobTracker'
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
name|'jobs'
op|'='
name|'collections'
op|'.'
name|'defaultdict'
op|'('
name|'list'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_job
dedent|''
name|'def'
name|'add_job'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'pid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Appends process_id of instance to cache.\n\n        This method will store the pid of a process in cache as\n        a key: value pair which will be used to kill the process if it\n        is running while deleting the instance. Instance uuid is used as\n        a key in the cache and pid will be the value.\n\n        :param instance: Object of instance\n        :param pid: Id of the process\n        """'
newline|'\n'
name|'self'
op|'.'
name|'jobs'
op|'['
name|'instance'
op|'.'
name|'uuid'
op|']'
op|'.'
name|'append'
op|'('
name|'pid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_job
dedent|''
name|'def'
name|'remove_job'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'pid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes pid of process from cache.\n\n        This method will remove the pid of a process from the cache.\n\n        :param instance: Object of instance\n        :param pid: Id of the process\n        """'
newline|'\n'
name|'uuid'
op|'='
name|'instance'
op|'.'
name|'uuid'
newline|'\n'
name|'if'
name|'uuid'
name|'in'
name|'self'
op|'.'
name|'jobs'
name|'and'
name|'pid'
name|'in'
name|'self'
op|'.'
name|'jobs'
op|'['
name|'uuid'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'jobs'
op|'['
name|'uuid'
op|']'
op|'.'
name|'remove'
op|'('
name|'pid'
op|')'
newline|'\n'
nl|'\n'
comment|"# remove instance.uuid if no pid's remaining"
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'jobs'
op|'['
name|'uuid'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'jobs'
op|'.'
name|'pop'
op|'('
name|'uuid'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|terminate_jobs
dedent|''
dedent|''
name|'def'
name|'terminate_jobs'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Kills the running processes for given instance.\n\n        This method is used to kill all running processes of the instance if\n        it is deleted in between.\n\n        :param instance: Object of instance\n        """'
newline|'\n'
name|'pids_to_remove'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'jobs'
op|'.'
name|'get'
op|'('
name|'instance'
op|'.'
name|'uuid'
op|','
op|'['
op|']'
op|')'
op|')'
newline|'\n'
name|'for'
name|'pid'
name|'in'
name|'pids_to_remove'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
comment|'# Try to kill the process'
nl|'\n'
indent|'                '
name|'os'
op|'.'
name|'kill'
op|'('
name|'pid'
op|','
name|'signal'
op|'.'
name|'SIGKILL'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'exc'
op|'.'
name|'errno'
op|'!='
name|'errno'
op|'.'
name|'ESRCH'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|"'Failed to kill process %(pid)s '"
nl|'\n'
string|"'due to %(reason)s, while deleting the '"
nl|'\n'
string|"'instance.'"
op|')'
op|','
op|'{'
string|"'pid'"
op|':'
name|'pid'
op|','
string|"'reason'"
op|':'
name|'exc'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# Check if the process is still alive.'
nl|'\n'
indent|'                '
name|'os'
op|'.'
name|'kill'
op|'('
name|'pid'
op|','
number|'0'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'exc'
op|'.'
name|'errno'
op|'!='
name|'errno'
op|'.'
name|'ESRCH'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|"'Unexpected error while checking process '"
nl|'\n'
string|"'%(pid)s.'"
op|')'
op|','
op|'{'
string|"'pid'"
op|':'
name|'pid'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# The process is still around'
nl|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_LW'
op|'('
string|'"Failed to kill a long running process "'
nl|'\n'
string|'"%(pid)s related to the instance when "'
nl|'\n'
string|'"deleting it."'
op|')'
op|','
op|'{'
string|"'pid'"
op|':'
name|'pid'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'remove_job'
op|'('
name|'instance'
op|','
name|'pid'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit