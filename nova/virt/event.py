begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 Red Hat, Inc.'
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
string|'"""\nAsynchronous event notifications from virtualization drivers.\n\nThis module defines a set of classes representing data for\nvarious asynchronous events that can occurr in a virtualization\ndriver.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
DECL|variable|EVENT_LIFECYCLE_STARTED
name|'EVENT_LIFECYCLE_STARTED'
op|'='
number|'0'
newline|'\n'
DECL|variable|EVENT_LIFECYCLE_STOPPED
name|'EVENT_LIFECYCLE_STOPPED'
op|'='
number|'1'
newline|'\n'
DECL|variable|EVENT_LIFECYCLE_PAUSED
name|'EVENT_LIFECYCLE_PAUSED'
op|'='
number|'2'
newline|'\n'
DECL|variable|EVENT_LIFECYCLE_RESUMED
name|'EVENT_LIFECYCLE_RESUMED'
op|'='
number|'3'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Event
name|'class'
name|'Event'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for all events emitted by a hypervisor.\n\n    All events emitted by a virtualization driver are\n    subclasses of this base object. The only generic\n    information recorded in the base class is a timestamp\n    indicating when the event first occurred. The timestamp\n    is recorded as fractional seconds since the UNIX epoch.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'timestamp'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'timestamp'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'timestamp'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'timestamp'
op|'='
name|'timestamp'
newline|'\n'
nl|'\n'
DECL|member|get_timestamp
dedent|''
dedent|''
name|'def'
name|'get_timestamp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'timestamp'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceEvent
dedent|''
dedent|''
name|'class'
name|'InstanceEvent'
op|'('
name|'Event'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for all instance events.\n\n    All events emitted by a virtualization driver which\n    are associated with a virtual domain instance are\n    subclasses of this base object. This object records\n    the UUID associated with the instance.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'uuid'
op|','
name|'timestamp'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'InstanceEvent'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'timestamp'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'uuid'
op|'='
name|'uuid'
newline|'\n'
nl|'\n'
DECL|member|get_instance_uuid
dedent|''
name|'def'
name|'get_instance_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'uuid'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LifecycleEvent
dedent|''
dedent|''
name|'class'
name|'LifecycleEvent'
op|'('
name|'InstanceEvent'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Class for instance lifecycle state change events.\n\n    When a virtual domain instance lifecycle state changes,\n    events of this class are emitted. The EVENT_LIFECYCLE_XX\n    constants defined why lifecycle change occurred. This\n    event allows detection of an instance starting/stopping\n    without need for polling.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'uuid'
op|','
name|'transition'
op|','
name|'timestamp'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'LifecycleEvent'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'uuid'
op|','
name|'timestamp'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'transition'
op|'='
name|'transition'
newline|'\n'
nl|'\n'
DECL|member|get_transition
dedent|''
name|'def'
name|'get_transition'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'transition'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
