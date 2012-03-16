begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 OpenStack, LLC.'
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
string|'"""\nScheduler that allows routing some calls to one driver and others to another.\n"""'
newline|'\n'
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
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|multi_scheduler_opts
name|'multi_scheduler_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'compute_scheduler_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.scheduler.'"
nl|'\n'
string|"'filter_scheduler.FilterScheduler'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Driver to use for scheduling compute calls'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'volume_scheduler_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.scheduler.chance.ChanceScheduler'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Driver to use for scheduling volume calls'"
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
name|'multi_scheduler_opts'
op|')'
newline|'\n'
nl|'\n'
comment|'# A mapping of methods to topics so we can figure out which driver to use.'
nl|'\n'
comment|'# There are currently no compute methods proxied through the map'
nl|'\n'
DECL|variable|_METHOD_MAP
name|'_METHOD_MAP'
op|'='
op|'{'
string|"'create_volume'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'create_volumes'"
op|':'
string|"'volume'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MultiScheduler
name|'class'
name|'MultiScheduler'
op|'('
name|'driver'
op|'.'
name|'Scheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A scheduler that holds multiple sub-schedulers.\n\n    This exists to allow flag-driven composibility of schedulers, allowing\n    third parties to integrate custom schedulers more easily.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'MultiScheduler'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'compute_driver'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'compute_scheduler_driver'
op|')'
newline|'\n'
name|'volume_driver'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'volume_scheduler_driver'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'drivers'
op|'='
op|'{'
string|"'compute'"
op|':'
name|'compute_driver'
op|','
nl|'\n'
string|"'volume'"
op|':'
name|'volume_driver'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'key'
op|'.'
name|'startswith'
op|'('
string|"'schedule_'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'AttributeError'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
name|'method'
op|'='
name|'key'
op|'['
name|'len'
op|'('
string|"'schedule_'"
op|')'
op|':'
op|']'
newline|'\n'
name|'if'
name|'method'
name|'not'
name|'in'
name|'_METHOD_MAP'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'AttributeError'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'drivers'
op|'['
name|'_METHOD_MAP'
op|'['
name|'method'
op|']'
op|']'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule
dedent|''
name|'def'
name|'schedule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|','
name|'method'
op|','
op|'*'
name|'_args'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'drivers'
op|'['
name|'topic'
op|']'
op|'.'
name|'schedule'
op|'('
name|'context'
op|','
name|'topic'
op|','
nl|'\n'
name|'method'
op|','
op|'*'
name|'_args'
op|','
op|'**'
name|'_kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_run_instance
dedent|''
name|'def'
name|'schedule_run_instance'
op|'('
name|'self'
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
name|'return'
name|'self'
op|'.'
name|'drivers'
op|'['
string|"'compute'"
op|']'
op|'.'
name|'schedule_run_instance'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_prep_resize
dedent|''
name|'def'
name|'schedule_prep_resize'
op|'('
name|'self'
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
name|'return'
name|'self'
op|'.'
name|'drivers'
op|'['
string|"'compute'"
op|']'
op|'.'
name|'schedule_prep_resize'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
