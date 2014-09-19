begin_unit
comment|'# Copyright 2012 IBM Corp.'
nl|'\n'
comment|'# Copyright (c) AT&T Labs Inc. 2012 Yun Mao <yunmao@gmail.com>'
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
string|'"""Define APIs for the servicegroup access."""'
newline|'\n'
nl|'\n'
name|'import'
name|'random'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'utils'
name|'import'
name|'importutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
op|','
name|'_LW'
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
DECL|variable|_default_driver
name|'_default_driver'
op|'='
string|"'db'"
newline|'\n'
DECL|variable|servicegroup_driver_opt
name|'servicegroup_driver_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'servicegroup_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'_default_driver'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The driver for servicegroup '"
nl|'\n'
string|"'service (valid options are: '"
nl|'\n'
string|"'db, zk, mc)'"
op|')'
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
name|'register_opt'
op|'('
name|'servicegroup_driver_opt'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(geekinutah): By default drivers wait 5 seconds before reporting'
nl|'\n'
DECL|variable|INITIAL_REPORTING_DELAY
name|'INITIAL_REPORTING_DELAY'
op|'='
number|'5'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|API
name|'class'
name|'API'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|_driver
indent|'    '
name|'_driver'
op|'='
name|'None'
newline|'\n'
DECL|variable|_driver_name_class_mapping
name|'_driver_name_class_mapping'
op|'='
op|'{'
nl|'\n'
string|"'db'"
op|':'
string|"'nova.servicegroup.drivers.db.DbDriver'"
op|','
nl|'\n'
string|"'zk'"
op|':'
string|"'nova.servicegroup.drivers.zk.ZooKeeperDriver'"
op|','
nl|'\n'
string|"'mc'"
op|':'
string|"'nova.servicegroup.drivers.mc.MemcachedDriver'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__new__
name|'def'
name|'__new__'
op|'('
name|'cls'
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
string|"'''Create an instance of the servicegroup API.\n\n        args and kwargs are passed down to the servicegroup driver when it gets\n        created.  No args currently exist, though.  Valid kwargs are:\n\n        db_allowed - Boolean. False if direct db access is not allowed and\n                     alternative data access (conductor) should be used\n                     instead.\n        '''"
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'cls'
op|'.'
name|'_driver'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'ServiceGroup driver defined as an instance of %s'"
op|','
nl|'\n'
name|'str'
op|'('
name|'CONF'
op|'.'
name|'servicegroup_driver'
op|')'
op|')'
newline|'\n'
name|'driver_name'
op|'='
name|'CONF'
op|'.'
name|'servicegroup_driver'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'driver_class'
op|'='
name|'cls'
op|'.'
name|'_driver_name_class_mapping'
op|'['
name|'driver_name'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'TypeError'
op|'('
name|'_'
op|'('
string|'"unknown ServiceGroup driver name: %s"'
op|')'
nl|'\n'
op|'%'
name|'driver_name'
op|')'
newline|'\n'
dedent|''
name|'cls'
op|'.'
name|'_driver'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'driver_class'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'check_isinstance'
op|'('
name|'cls'
op|'.'
name|'_driver'
op|','
name|'ServiceGroupDriver'
op|')'
newline|'\n'
comment|"# we don't have to check that cls._driver is not NONE,"
nl|'\n'
comment|'# check_isinstance does it'
nl|'\n'
dedent|''
name|'return'
name|'super'
op|'('
name|'API'
op|','
name|'cls'
op|')'
op|'.'
name|'__new__'
op|'('
name|'cls'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
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
name|'basic_config_check'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|basic_config_check
dedent|''
name|'def'
name|'basic_config_check'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Perform basic config check."""'
newline|'\n'
comment|'# Make sure report interval is less than service down time'
nl|'\n'
name|'report_interval'
op|'='
name|'CONF'
op|'.'
name|'report_interval'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'service_down_time'
op|'<='
name|'report_interval'
op|':'
newline|'\n'
indent|'            '
name|'new_service_down_time'
op|'='
name|'int'
op|'('
name|'report_interval'
op|'*'
number|'2.5'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Report interval must be less than service down "'
nl|'\n'
string|'"time. Current config: <service_down_time: "'
nl|'\n'
string|'"%(service_down_time)s, report_interval: "'
nl|'\n'
string|'"%(report_interval)s>. Setting service_down_time "'
nl|'\n'
string|'"to: %(new_service_down_time)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'service_down_time'"
op|':'
name|'CONF'
op|'.'
name|'service_down_time'
op|','
nl|'\n'
string|"'report_interval'"
op|':'
name|'report_interval'
op|','
nl|'\n'
string|"'new_service_down_time'"
op|':'
name|'new_service_down_time'
op|'}'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'service_down_time'"
op|','
name|'new_service_down_time'
op|')'
newline|'\n'
nl|'\n'
DECL|member|join
dedent|''
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
string|'"""Add a new member to the ServiceGroup\n\n        @param member_id: the joined member ID\n        @param group_id: the group name, of the joined member\n        @param service: the parameter can be used for notifications about\n        disconnect mode and update some internals\n        """'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Join new ServiceGroup member %(member_id)s to the '"
nl|'\n'
string|"'%(group_id)s group, service = %(service)s'"
op|','
nl|'\n'
op|'{'
string|"'member_id'"
op|':'
name|'member_id'
op|','
nl|'\n'
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
name|'return'
name|'self'
op|'.'
name|'_driver'
op|'.'
name|'join'
op|'('
name|'member_id'
op|','
name|'group_id'
op|','
name|'service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_is_up
dedent|''
name|'def'
name|'service_is_up'
op|'('
name|'self'
op|','
name|'member'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if the given member is up."""'
newline|'\n'
comment|'# NOTE(johngarbutt) no logging in this method,'
nl|'\n'
comment|"# so this doesn't slow down the scheduler"
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_driver'
op|'.'
name|'is_up'
op|'('
name|'member'
op|')'
newline|'\n'
nl|'\n'
DECL|member|leave
dedent|''
name|'def'
name|'leave'
op|'('
name|'self'
op|','
name|'member_id'
op|','
name|'group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Explicitly remove the given member from the ServiceGroup\n        monitoring.\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Explicitly remove the given member %(member_id)s from the'"
nl|'\n'
string|"'%(group_id)s group monitoring'"
op|','
nl|'\n'
op|'{'
string|"'member_id'"
op|':'
name|'member_id'
op|','
string|"'group_id'"
op|':'
name|'group_id'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_driver'
op|'.'
name|'leave'
op|'('
name|'member_id'
op|','
name|'group_id'
op|')'
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
string|'"""Returns ALL members of the given group."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Returns ALL members of the [%s] '"
nl|'\n'
string|"'ServiceGroup'"
op|','
name|'group_id'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_driver'
op|'.'
name|'get_all'
op|'('
name|'group_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_one
dedent|''
name|'def'
name|'get_one'
op|'('
name|'self'
op|','
name|'group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns one member of the given group. The strategy to select\n        the member is decided by the driver (e.g. random or round-robin).\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Returns one member of the [%s] group'"
op|','
name|'group_id'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_driver'
op|'.'
name|'get_one'
op|'('
name|'group_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceGroupDriver
dedent|''
dedent|''
name|'class'
name|'ServiceGroupDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for ServiceGroup drivers."""'
newline|'\n'
nl|'\n'
DECL|member|join
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
string|'"""Join the given service with its group."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_up
dedent|''
name|'def'
name|'is_up'
op|'('
name|'self'
op|','
name|'member'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check whether the given member is up."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|leave
dedent|''
name|'def'
name|'leave'
op|'('
name|'self'
op|','
name|'member_id'
op|','
name|'group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove the given member from the ServiceGroup monitoring."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
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
string|'"""Returns ALL members of the given group."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_one
dedent|''
name|'def'
name|'get_one'
op|'('
name|'self'
op|','
name|'group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The default behavior of get_one is to randomly pick one from\n        the result of get_all(). This is likely to be overridden in the\n        actual driver implementation.\n        """'
newline|'\n'
name|'members'
op|'='
name|'self'
op|'.'
name|'get_all'
op|'('
name|'group_id'
op|')'
newline|'\n'
name|'if'
name|'members'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'length'
op|'='
name|'len'
op|'('
name|'members'
op|')'
newline|'\n'
name|'if'
name|'length'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'random'
op|'.'
name|'choice'
op|'('
name|'members'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
