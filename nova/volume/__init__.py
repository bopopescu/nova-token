begin_unit
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
name|'import'
name|'oslo_config'
op|'.'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'importutils'
newline|'\n'
nl|'\n'
DECL|variable|_volume_opts
name|'_volume_opts'
op|'='
op|'['
nl|'\n'
name|'oslo_config'
op|'.'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'volume_api_class'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.volume.cinder.API'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'DEPRECATED: The full class name of the volume API class to use'"
op|','
nl|'\n'
DECL|variable|deprecated_for_removal
name|'deprecated_for_removal'
op|'='
name|'True'
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'oslo_config'
op|'.'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'_volume_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|API
name|'def'
name|'API'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volume_api_class'
op|'='
name|'oslo_config'
op|'.'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'volume_api_class'
newline|'\n'
name|'cls'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'volume_api_class'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
