begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify
name|'def'
name|'notify'
op|'('
name|'_context'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Notifies the recipient of the desired event given the model.\n    Log notifications using nova\'s default logging system"""'
newline|'\n'
nl|'\n'
name|'priority'
op|'='
name|'message'
op|'.'
name|'get'
op|'('
string|"'priority'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'default_notification_level'
op|')'
newline|'\n'
name|'priority'
op|'='
name|'priority'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'logger'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
nl|'\n'
string|"'nova.notification.%s'"
op|'%'
name|'message'
op|'['
string|"'event_type'"
op|']'
op|')'
newline|'\n'
name|'getattr'
op|'('
name|'logger'
op|','
name|'priority'
op|')'
op|'('
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'message'
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
