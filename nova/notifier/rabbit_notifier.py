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
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'context'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
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
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
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
DECL|variable|notification_topic_opt
name|'notification_topic_opt'
op|'='
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'notification_topics'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'notifications'"
op|','
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'AMQP topic used for Nova notifications'"
op|')'
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
name|'register_opt'
op|'('
name|'notification_topic_opt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify
name|'def'
name|'notify'
op|'('
name|'context'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a notification to the RabbitMQ"""'
newline|'\n'
name|'if'
name|'not'
name|'context'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'nova'
op|'.'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
dedent|''
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
name|'for'
name|'topic'
name|'in'
name|'FLAGS'
op|'.'
name|'notification_topics'
op|':'
newline|'\n'
indent|'        '
name|'topic'
op|'='
string|"'%s.%s'"
op|'%'
op|'('
name|'topic'
op|','
name|'priority'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'rpc'
op|'.'
name|'notify'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'message'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
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
string|'"Could not send notification to %(topic)s. "'
nl|'\n'
string|'"Payload=%(message)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
