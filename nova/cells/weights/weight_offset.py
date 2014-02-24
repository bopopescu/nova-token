begin_unit
comment|'# Copyright (c) 2012-2013 Rackspace Hosting'
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
string|'"""\nWeigh cells by their weight_offset in the DB.  Cells with higher\nweight_offsets in the DB will be preferred.\n"""'
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
op|'.'
name|'cells'
name|'import'
name|'weights'
newline|'\n'
nl|'\n'
DECL|variable|weigher_opts
name|'weigher_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'offset_weight_multiplier'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Multiplier used to weigh offset weigher.'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'weigher_opts'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WeightOffsetWeigher
name|'class'
name|'WeightOffsetWeigher'
op|'('
name|'weights'
op|'.'
name|'BaseCellWeigher'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Weight cell by weight_offset db field.\n    Originally designed so you can set a default cell by putting\n    its weight_offset to 999999999999999 (highest weight wins)\n    """'
newline|'\n'
nl|'\n'
DECL|member|weight_multiplier
name|'def'
name|'weight_multiplier'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'offset_weight_multiplier'
newline|'\n'
nl|'\n'
DECL|member|_weigh_object
dedent|''
name|'def'
name|'_weigh_object'
op|'('
name|'self'
op|','
name|'cell'
op|','
name|'weight_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns whatever was in the DB for weight_offset."""'
newline|'\n'
name|'return'
name|'cell'
op|'.'
name|'db_info'
op|'.'
name|'get'
op|'('
string|"'weight_offset'"
op|','
number|'0'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
