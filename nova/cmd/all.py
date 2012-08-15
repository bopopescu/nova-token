begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'#    you may not use this file except in compliance with the License.'
nl|'\n'
comment|'#    You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#        http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'#    See the License for the specific language governing permissions and'
nl|'\n'
comment|'#    limitations under the License.'
nl|'\n'
nl|'\n'
string|'"""Starter script for all nova services.\n\nThis script attempts to start all the nova services in one process.  Each\nservice is started in its own greenthread.  Please note that exceptions and\nsys.exit() on the starting of a service are logged and the script will\ncontinue attempting to launch the rest of the services.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objectstore'
name|'import'
name|'s3server'
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
name|'service'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'vnc'
name|'import'
name|'xvp_proxy'
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
string|"'manager'"
op|','
string|"'nova.conductor.api'"
op|','
name|'group'
op|'='
string|"'conductor'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'topic'"
op|','
string|"'nova.conductor.api'"
op|','
name|'group'
op|'='
string|"'conductor'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'enabled_apis'"
op|','
string|"'nova.service'"
op|')'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.all'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'config'
op|'.'
name|'parse_args'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'setup'
op|'('
string|'"nova"'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'monkey_patch'
op|'('
op|')'
newline|'\n'
name|'launcher'
op|'='
name|'service'
op|'.'
name|'ProcessLauncher'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# nova-api'
nl|'\n'
name|'for'
name|'api'
name|'in'
name|'CONF'
op|'.'
name|'enabled_apis'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
name|'api'
op|')'
newline|'\n'
name|'launcher'
op|'.'
name|'launch_server'
op|'('
name|'server'
op|','
name|'workers'
op|'='
name|'server'
op|'.'
name|'workers'
name|'or'
number|'1'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'Exception'
op|','
name|'SystemExit'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Failed to load %s'"
op|')'
op|'%'
string|"'%s-api'"
op|'%'
name|'api'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'mod'
name|'in'
op|'['
name|'s3server'
op|','
name|'xvp_proxy'
op|']'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'launcher'
op|'.'
name|'launch_server'
op|'('
name|'mod'
op|'.'
name|'get_wsgi_server'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'Exception'
op|','
name|'SystemExit'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Failed to load %s'"
op|')'
op|'%'
name|'mod'
op|'.'
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'binary'
name|'in'
op|'['
string|"'nova-compute'"
op|','
string|"'nova-network'"
op|','
string|"'nova-scheduler'"
op|','
nl|'\n'
string|"'nova-cert'"
op|','
string|"'nova-conductor'"
op|']'
op|':'
newline|'\n'
nl|'\n'
comment|'# FIXME(sirp): Most service configs are defined in nova/service.py, but'
nl|'\n'
comment|'# conductor has set a new precedent of storing these configs'
nl|'\n'
comment|'# nova/<service>/api.py.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# We should update the existing services to use this new approach so we'
nl|'\n'
comment|"# don't have to treat conductor differently here."
nl|'\n'
indent|'        '
name|'if'
name|'binary'
op|'=='
string|"'nova-conductor'"
op|':'
newline|'\n'
indent|'            '
name|'topic'
op|'='
name|'CONF'
op|'.'
name|'conductor'
op|'.'
name|'topic'
newline|'\n'
name|'manager'
op|'='
name|'CONF'
op|'.'
name|'conductor'
op|'.'
name|'manager'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'topic'
op|'='
name|'None'
newline|'\n'
name|'manager'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'launcher'
op|'.'
name|'launch_server'
op|'('
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
name|'binary'
op|'='
name|'binary'
op|','
nl|'\n'
name|'topic'
op|'='
name|'topic'
op|','
nl|'\n'
name|'manager'
op|'='
name|'manager'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'Exception'
op|','
name|'SystemExit'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Failed to load %s'"
op|')'
op|','
name|'binary'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'launcher'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
