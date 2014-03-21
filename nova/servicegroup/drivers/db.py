begin_unit
comment|'# Copyright 2012 IBM Corp.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'# you may not use this file except in compliance with the License.'
nl|'\n'
comment|'# You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or'
nl|'\n'
comment|'# implied.'
nl|'\n'
comment|'# See the License for the specific language governing permissions and'
nl|'\n'
comment|'# limitations under the License.'
nl|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'conductor'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'servicegroup'
name|'import'
name|'api'
newline|'\n'
nl|'\n'
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
name|'import_opt'
op|'('
string|"'service_down_time'"
op|','
string|"'nova.service'"
op|')'
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
nl|'\n'
DECL|class|DbDriver
name|'class'
name|'DbDriver'
op|'('
name|'api'
op|'.'
name|'ServiceGroupDriver'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
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
name|'self'
op|'.'
name|'db_allowed'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'db_allowed'"
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conductor_api'
op|'='
name|'conductor'
op|'.'
name|'API'
op|'('
name|'use_local'
op|'='
name|'self'
op|'.'
name|'db_allowed'
op|')'
newline|'\n'
nl|'\n'
DECL|member|join
dedent|''
name|'def'
name|'join'
op|'('
name|'self'
op|','
name|'member_id'
op|','
name|'group_id'
op|','
name|'service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Join the given service with it\'s group."""'
newline|'\n'
nl|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|"'DB_Driver: join new ServiceGroup member %(member_id)s to '"
nl|'\n'
string|"'the %(group_id)s group, service = %(service)s'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|','
op|'{'
string|"'member_id'"
op|':'
name|'member_id'
op|','
string|"'group_id'"
op|':'
name|'group_id'
op|','
nl|'\n'
string|"'service'"
op|':'
name|'service'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'service'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|"'service is a mandatory argument for DB based'"
nl|'\n'
string|"' ServiceGroup driver'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'report_interval'
op|'='
name|'service'
op|'.'
name|'report_interval'
newline|'\n'
name|'if'
name|'report_interval'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'.'
name|'tg'
op|'.'
name|'add_timer'
op|'('
name|'report_interval'
op|','
name|'self'
op|'.'
name|'_report_state'
op|','
nl|'\n'
name|'api'
op|'.'
name|'INITIAL_REPORTING_DELAY'
op|','
name|'service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_up
dedent|''
dedent|''
name|'def'
name|'is_up'
op|'('
name|'self'
op|','
name|'service_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Moved from nova.utils\n        Check whether a service is up based on last heartbeat.\n        """'
newline|'\n'
name|'last_heartbeat'
op|'='
name|'service_ref'
op|'['
string|"'updated_at'"
op|']'
name|'or'
name|'service_ref'
op|'['
string|"'created_at'"
op|']'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'last_heartbeat'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(russellb) If this service_ref came in over rpc via'
nl|'\n'
comment|'# conductor, then the timestamp will be a string and needs to be'
nl|'\n'
comment|'# converted back to a datetime.'
nl|'\n'
indent|'            '
name|'last_heartbeat'
op|'='
name|'timeutils'
op|'.'
name|'parse_strtime'
op|'('
name|'last_heartbeat'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Objects have proper UTC timezones, but the timeutils comparison'
nl|'\n'
comment|'# below does not (and will fail)'
nl|'\n'
indent|'            '
name|'last_heartbeat'
op|'='
name|'last_heartbeat'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'None'
op|')'
newline|'\n'
comment|'# Timestamps in DB are UTC.'
nl|'\n'
dedent|''
name|'elapsed'
op|'='
name|'timeutils'
op|'.'
name|'delta_seconds'
op|'('
name|'last_heartbeat'
op|','
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'DB_Driver.is_up last_heartbeat = %(lhb)s elapsed = %(el)s'"
op|','
nl|'\n'
op|'{'
string|"'lhb'"
op|':'
name|'str'
op|'('
name|'last_heartbeat'
op|')'
op|','
string|"'el'"
op|':'
name|'str'
op|'('
name|'elapsed'
op|')'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'abs'
op|'('
name|'elapsed'
op|')'
op|'<='
name|'CONF'
op|'.'
name|'service_down_time'
newline|'\n'
nl|'\n'
DECL|member|get_all
dedent|''
name|'def'
name|'get_all'
op|'('
name|'self'
op|','
name|'group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns ALL members of the given group\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'DB_Driver: get_all members of the %s group'"
op|')'
op|'%'
name|'group_id'
op|')'
newline|'\n'
name|'rs'
op|'='
op|'['
op|']'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'services'
op|'='
name|'self'
op|'.'
name|'conductor_api'
op|'.'
name|'service_get_all_by_topic'
op|'('
name|'ctxt'
op|','
name|'group_id'
op|')'
newline|'\n'
name|'for'
name|'service'
name|'in'
name|'services'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'is_up'
op|'('
name|'service'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'rs'
op|'.'
name|'append'
op|'('
name|'service'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'rs'
newline|'\n'
nl|'\n'
DECL|member|_report_state
dedent|''
name|'def'
name|'_report_state'
op|'('
name|'self'
op|','
name|'service'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update the state of this service in the datastore."""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'state_catalog'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'report_count'
op|'='
name|'service'
op|'.'
name|'service_ref'
op|'['
string|"'report_count'"
op|']'
op|'+'
number|'1'
newline|'\n'
name|'state_catalog'
op|'['
string|"'report_count'"
op|']'
op|'='
name|'report_count'
newline|'\n'
nl|'\n'
name|'service'
op|'.'
name|'service_ref'
op|'='
name|'self'
op|'.'
name|'conductor_api'
op|'.'
name|'service_update'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'service'
op|'.'
name|'service_ref'
op|','
name|'state_catalog'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(termie): make this pattern be more elegant.'
nl|'\n'
name|'if'
name|'getattr'
op|'('
name|'service'
op|','
string|"'model_disconnected'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'service'
op|'.'
name|'model_disconnected'
op|'='
name|'False'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Recovered model server connection!'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(vish): this should probably only catch connection errors'
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
comment|'# pylint: disable=W0702'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'getattr'
op|'('
name|'service'
op|','
string|"'model_disconnected'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'service'
op|'.'
name|'model_disconnected'
op|'='
name|'True'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'model server went away'"
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
