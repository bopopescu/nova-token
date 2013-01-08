begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
comment|'# Importing full names to not pollute the namespace and cause possible'
nl|'\n'
comment|"# collisions with use of 'from nova.compute import <foo>' elsewhere."
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'cfg'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'importutils'
newline|'\n'
nl|'\n'
DECL|variable|_compute_opts
name|'_compute_opts'
op|'='
op|'['
nl|'\n'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'compute_api_class'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.compute.api.API'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The full class name of the '"
nl|'\n'
string|"'compute API class to use'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'_compute_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|API
name|'def'
name|'API'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'importutils'
op|'='
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'importutils'
newline|'\n'
name|'compute_api_class'
op|'='
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'compute_api_class'
newline|'\n'
name|'cls'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'compute_api_class'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
