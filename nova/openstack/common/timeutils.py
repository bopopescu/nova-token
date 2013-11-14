begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation.'
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
string|'"""\nTime related utilities and helper functions.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'calendar'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'iso8601'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# ISO 8601 extended time format with microseconds'
nl|'\n'
DECL|variable|_ISO8601_TIME_FORMAT_SUBSECOND
name|'_ISO8601_TIME_FORMAT_SUBSECOND'
op|'='
string|"'%Y-%m-%dT%H:%M:%S.%f'"
newline|'\n'
DECL|variable|_ISO8601_TIME_FORMAT
name|'_ISO8601_TIME_FORMAT'
op|'='
string|"'%Y-%m-%dT%H:%M:%S'"
newline|'\n'
DECL|variable|PERFECT_TIME_FORMAT
name|'PERFECT_TIME_FORMAT'
op|'='
name|'_ISO8601_TIME_FORMAT_SUBSECOND'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|isotime
name|'def'
name|'isotime'
op|'('
name|'at'
op|'='
name|'None'
op|','
name|'subsecond'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stringify time in ISO 8601 format."""'
newline|'\n'
name|'if'
name|'not'
name|'at'
op|':'
newline|'\n'
indent|'        '
name|'at'
op|'='
name|'utcnow'
op|'('
op|')'
newline|'\n'
dedent|''
name|'st'
op|'='
name|'at'
op|'.'
name|'strftime'
op|'('
name|'_ISO8601_TIME_FORMAT'
nl|'\n'
name|'if'
name|'not'
name|'subsecond'
nl|'\n'
name|'else'
name|'_ISO8601_TIME_FORMAT_SUBSECOND'
op|')'
newline|'\n'
name|'tz'
op|'='
name|'at'
op|'.'
name|'tzinfo'
op|'.'
name|'tzname'
op|'('
name|'None'
op|')'
name|'if'
name|'at'
op|'.'
name|'tzinfo'
name|'else'
string|"'UTC'"
newline|'\n'
name|'st'
op|'+='
op|'('
string|"'Z'"
name|'if'
name|'tz'
op|'=='
string|"'UTC'"
name|'else'
name|'tz'
op|')'
newline|'\n'
name|'return'
name|'st'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_isotime
dedent|''
name|'def'
name|'parse_isotime'
op|'('
name|'timestr'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse time from ISO 8601 format."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'iso8601'
op|'.'
name|'parse_date'
op|'('
name|'timestr'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'iso8601'
op|'.'
name|'ParseError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'ValueError'
op|'('
name|'six'
op|'.'
name|'text_type'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'ValueError'
op|'('
name|'six'
op|'.'
name|'text_type'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|strtime
dedent|''
dedent|''
name|'def'
name|'strtime'
op|'('
name|'at'
op|'='
name|'None'
op|','
name|'fmt'
op|'='
name|'PERFECT_TIME_FORMAT'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns formatted utcnow."""'
newline|'\n'
name|'if'
name|'not'
name|'at'
op|':'
newline|'\n'
indent|'        '
name|'at'
op|'='
name|'utcnow'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'at'
op|'.'
name|'strftime'
op|'('
name|'fmt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_strtime
dedent|''
name|'def'
name|'parse_strtime'
op|'('
name|'timestr'
op|','
name|'fmt'
op|'='
name|'PERFECT_TIME_FORMAT'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Turn a formatted time back into a datetime."""'
newline|'\n'
name|'return'
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'strptime'
op|'('
name|'timestr'
op|','
name|'fmt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|normalize_time
dedent|''
name|'def'
name|'normalize_time'
op|'('
name|'timestamp'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Normalize time in arbitrary timezone to UTC naive object."""'
newline|'\n'
name|'offset'
op|'='
name|'timestamp'
op|'.'
name|'utcoffset'
op|'('
op|')'
newline|'\n'
name|'if'
name|'offset'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'timestamp'
newline|'\n'
dedent|''
name|'return'
name|'timestamp'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'None'
op|')'
op|'-'
name|'offset'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_older_than
dedent|''
name|'def'
name|'is_older_than'
op|'('
name|'before'
op|','
name|'seconds'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return True if before is older than seconds."""'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'before'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'before'
op|'='
name|'parse_strtime'
op|'('
name|'before'
op|')'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'None'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'utcnow'
op|'('
op|')'
op|'-'
name|'before'
op|'>'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
name|'seconds'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_newer_than
dedent|''
name|'def'
name|'is_newer_than'
op|'('
name|'after'
op|','
name|'seconds'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return True if after is newer than seconds."""'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'after'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'after'
op|'='
name|'parse_strtime'
op|'('
name|'after'
op|')'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'None'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'after'
op|'-'
name|'utcnow'
op|'('
op|')'
op|'>'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
name|'seconds'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|utcnow_ts
dedent|''
name|'def'
name|'utcnow_ts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Timestamp version of our utcnow function."""'
newline|'\n'
name|'if'
name|'utcnow'
op|'.'
name|'override_time'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# NOTE(kgriffs): This is several times faster'
nl|'\n'
comment|'# than going through calendar.timegm(...)'
nl|'\n'
indent|'        '
name|'return'
name|'int'
op|'('
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'calendar'
op|'.'
name|'timegm'
op|'('
name|'utcnow'
op|'('
op|')'
op|'.'
name|'timetuple'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|utcnow
dedent|''
name|'def'
name|'utcnow'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Overridable version of utils.utcnow."""'
newline|'\n'
name|'if'
name|'utcnow'
op|'.'
name|'override_time'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'utcnow'
op|'.'
name|'override_time'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'utcnow'
op|'.'
name|'override_time'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|iso8601_from_timestamp
dedent|''
name|'def'
name|'iso8601_from_timestamp'
op|'('
name|'timestamp'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a iso8601 formated date from timestamp."""'
newline|'\n'
name|'return'
name|'isotime'
op|'('
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcfromtimestamp'
op|'('
name|'timestamp'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'utcnow'
op|'.'
name|'override_time'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_time_override
name|'def'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Overrides utils.utcnow.\n\n    Make it return a constant time or a list thereof, one at a time.\n\n    :param override_time: datetime instance or list thereof. If not\n                          given, defaults to the current UTC time.\n    """'
newline|'\n'
name|'utcnow'
op|'.'
name|'override_time'
op|'='
name|'override_time'
name|'or'
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|advance_time_delta
dedent|''
name|'def'
name|'advance_time_delta'
op|'('
name|'timedelta'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Advance overridden time using a datetime.timedelta."""'
newline|'\n'
name|'assert'
op|'('
name|'not'
name|'utcnow'
op|'.'
name|'override_time'
name|'is'
name|'None'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'dt'
name|'in'
name|'utcnow'
op|'.'
name|'override_time'
op|':'
newline|'\n'
indent|'            '
name|'dt'
op|'+='
name|'timedelta'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'        '
name|'utcnow'
op|'.'
name|'override_time'
op|'+='
name|'timedelta'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|advance_time_seconds
dedent|''
dedent|''
name|'def'
name|'advance_time_seconds'
op|'('
name|'seconds'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Advance overridden time by seconds."""'
newline|'\n'
name|'advance_time_delta'
op|'('
name|'datetime'
op|'.'
name|'timedelta'
op|'('
number|'0'
op|','
name|'seconds'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|clear_time_override
dedent|''
name|'def'
name|'clear_time_override'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Remove the overridden time."""'
newline|'\n'
name|'utcnow'
op|'.'
name|'override_time'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|marshall_now
dedent|''
name|'def'
name|'marshall_now'
op|'('
name|'now'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Make an rpc-safe datetime with microseconds.\n\n    Note: tzinfo is stripped, but not required for relative times.\n    """'
newline|'\n'
name|'if'
name|'not'
name|'now'
op|':'
newline|'\n'
indent|'        '
name|'now'
op|'='
name|'utcnow'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'day'
op|'='
name|'now'
op|'.'
name|'day'
op|','
name|'month'
op|'='
name|'now'
op|'.'
name|'month'
op|','
name|'year'
op|'='
name|'now'
op|'.'
name|'year'
op|','
name|'hour'
op|'='
name|'now'
op|'.'
name|'hour'
op|','
nl|'\n'
name|'minute'
op|'='
name|'now'
op|'.'
name|'minute'
op|','
name|'second'
op|'='
name|'now'
op|'.'
name|'second'
op|','
nl|'\n'
name|'microsecond'
op|'='
name|'now'
op|'.'
name|'microsecond'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|unmarshall_time
dedent|''
name|'def'
name|'unmarshall_time'
op|'('
name|'tyme'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unmarshall a datetime dict."""'
newline|'\n'
name|'return'
name|'datetime'
op|'.'
name|'datetime'
op|'('
name|'day'
op|'='
name|'tyme'
op|'['
string|"'day'"
op|']'
op|','
nl|'\n'
name|'month'
op|'='
name|'tyme'
op|'['
string|"'month'"
op|']'
op|','
nl|'\n'
name|'year'
op|'='
name|'tyme'
op|'['
string|"'year'"
op|']'
op|','
nl|'\n'
name|'hour'
op|'='
name|'tyme'
op|'['
string|"'hour'"
op|']'
op|','
nl|'\n'
name|'minute'
op|'='
name|'tyme'
op|'['
string|"'minute'"
op|']'
op|','
nl|'\n'
name|'second'
op|'='
name|'tyme'
op|'['
string|"'second'"
op|']'
op|','
nl|'\n'
name|'microsecond'
op|'='
name|'tyme'
op|'['
string|"'microsecond'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|delta_seconds
dedent|''
name|'def'
name|'delta_seconds'
op|'('
name|'before'
op|','
name|'after'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the difference between two timing objects.\n\n    Compute the difference in seconds between two date, time, or\n    datetime objects (as a float, to microsecond resolution).\n    """'
newline|'\n'
name|'delta'
op|'='
name|'after'
op|'-'
name|'before'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'delta'
op|'.'
name|'total_seconds'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
op|'('
name|'delta'
op|'.'
name|'days'
op|'*'
number|'24'
op|'*'
number|'3600'
op|')'
op|'+'
name|'delta'
op|'.'
name|'seconds'
op|'+'
nl|'\n'
name|'float'
op|'('
name|'delta'
op|'.'
name|'microseconds'
op|')'
op|'/'
op|'('
number|'10'
op|'**'
number|'6'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_soon
dedent|''
dedent|''
name|'def'
name|'is_soon'
op|'('
name|'dt'
op|','
name|'window'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determines if time is going to happen in the next window seconds.\n\n    :params dt: the time\n    :params window: minimum seconds to remain to consider the time not soon\n\n    :return: True if expiration is within the given duration\n    """'
newline|'\n'
name|'soon'
op|'='
op|'('
name|'utcnow'
op|'('
op|')'
op|'+'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
name|'window'
op|')'
op|')'
newline|'\n'
name|'return'
name|'normalize_time'
op|'('
name|'dt'
op|')'
op|'<='
name|'soon'
newline|'\n'
dedent|''
endmarker|''
end_unit
