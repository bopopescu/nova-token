begin_unit
comment|'# Copyright 2015 OpenStack Foundation'
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
comment|'# This package got introduced during the Mitaka cycle in 2015 to'
nl|'\n'
comment|'# have a central place where the config options of Nova can be maintained.'
nl|'\n'
comment|'# For more background see the blueprint "centralize-config-options"'
nl|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'scheduler'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'serial_console'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
name|'scheduler'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'serial_console'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
endmarker|''
end_unit