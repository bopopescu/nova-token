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
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
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
DECL|variable|notifier_opts
name|'notifier_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_notification_level'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'INFO'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Default notification level for outgoing notifications'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_publisher_id'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$host'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Default publisher_id for outgoing notifications'"
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
name|'notifier_opts'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|WARN
name|'WARN'
op|'='
string|"'WARN'"
newline|'\n'
DECL|variable|INFO
name|'INFO'
op|'='
string|"'INFO'"
newline|'\n'
DECL|variable|ERROR
name|'ERROR'
op|'='
string|"'ERROR'"
newline|'\n'
DECL|variable|CRITICAL
name|'CRITICAL'
op|'='
string|"'CRITICAL'"
newline|'\n'
DECL|variable|DEBUG
name|'DEBUG'
op|'='
string|"'DEBUG'"
newline|'\n'
nl|'\n'
DECL|variable|log_levels
name|'log_levels'
op|'='
op|'('
name|'DEBUG'
op|','
name|'WARN'
op|','
name|'INFO'
op|','
name|'ERROR'
op|','
name|'CRITICAL'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BadPriorityException
name|'class'
name|'BadPriorityException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify_decorator
dedent|''
name|'def'
name|'notify_decorator'
op|'('
name|'name'
op|','
name|'fn'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" decorator for notify which is used from utils.monkey_patch()\n\n        :param name: name of the function\n        :param function: - object of the function\n        :returns: function -- decorated function\n\n    """'
newline|'\n'
DECL|function|wrapped_func
name|'def'
name|'wrapped_func'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwarg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'body'
op|'['
string|"'args'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'body'
op|'['
string|"'kwarg'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'arg'
name|'in'
name|'args'
op|':'
newline|'\n'
indent|'            '
name|'body'
op|'['
string|"'args'"
op|']'
op|'.'
name|'append'
op|'('
name|'arg'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'key'
name|'in'
name|'kwarg'
op|':'
newline|'\n'
indent|'            '
name|'body'
op|'['
string|"'kwarg'"
op|']'
op|'['
name|'key'
op|']'
op|'='
name|'kwarg'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'context'
op|'='
name|'exception'
op|'.'
name|'get_context_from_function_and_args'
op|'('
name|'fn'
op|','
name|'args'
op|','
name|'kwarg'
op|')'
newline|'\n'
name|'notify'
op|'('
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'default_publisher_id'
op|','
nl|'\n'
name|'name'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'default_notification_level'
op|','
nl|'\n'
name|'body'
op|')'
newline|'\n'
name|'return'
name|'fn'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwarg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'wrapped_func'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|publisher_id
dedent|''
name|'def'
name|'publisher_id'
op|'('
name|'service'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'host'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'FLAGS'
op|'.'
name|'host'
newline|'\n'
dedent|''
name|'return'
string|'"%s.%s"'
op|'%'
op|'('
name|'service'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify
dedent|''
name|'def'
name|'notify'
op|'('
name|'context'
op|','
name|'publisher_id'
op|','
name|'event_type'
op|','
name|'priority'
op|','
name|'payload'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a notification using the specified driver\n\n    :param publisher_id: the source worker_type.host of the message\n    :param event_type:   the literal type of event (ex. Instance Creation)\n    :param priority:     patterned after the enumeration of Python logging\n                         levels in the set (DEBUG, WARN, INFO, ERROR, CRITICAL)\n    :param payload:       A python dictionary of attributes\n\n    Outgoing message format includes the above parameters, and appends the\n    following:\n\n    message_id\n      a UUID representing the id for this notification\n\n    timestamp\n      the GMT timestamp the notification was sent at\n\n    The composite message will be constructed as a dictionary of the above\n    attributes, which will then be sent via the transport mechanism defined\n    by the driver.\n\n    Message example::\n\n        {\'message_id\': str(uuid.uuid4()),\n         \'publisher_id\': \'compute.host1\',\n         \'timestamp\': utils.utcnow(),\n         \'priority\': \'WARN\',\n         \'event_type\': \'compute.create_instance\',\n         \'payload\': {\'instance_id\': 12, ... }}\n\n    """'
newline|'\n'
name|'if'
name|'priority'
name|'not'
name|'in'
name|'log_levels'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'BadPriorityException'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'%s not in valid priorities'"
op|')'
op|'%'
name|'priority'
op|')'
newline|'\n'
nl|'\n'
comment|'# Ensure everything is JSON serializable.'
nl|'\n'
dedent|''
name|'payload'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'payload'
op|','
name|'convert_instances'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'driver'
op|'='
name|'importutils'
op|'.'
name|'import_module'
op|'('
name|'FLAGS'
op|'.'
name|'notification_driver'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'dict'
op|'('
name|'message_id'
op|'='
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
name|'publisher_id'
op|'='
name|'publisher_id'
op|','
nl|'\n'
name|'event_type'
op|'='
name|'event_type'
op|','
nl|'\n'
name|'priority'
op|'='
name|'priority'
op|','
nl|'\n'
name|'payload'
op|'='
name|'payload'
op|','
nl|'\n'
name|'timestamp'
op|'='
name|'str'
op|'('
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'driver'
op|'.'
name|'notify'
op|'('
name|'context'
op|','
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Problem \'%(e)s\' attempting to "'
nl|'\n'
string|'"send to notification system. Payload=%(payload)s"'
op|')'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
