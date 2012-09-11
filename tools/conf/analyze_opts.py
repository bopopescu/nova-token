begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012, Cloudscaling'
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
string|"'''\nfind_unused_options.py\n\nCompare the nova.conf file with the nova.conf.sample file to find any unused\noptions or default values in nova.conf\n'''"
newline|'\n'
name|'import'
name|'argparse'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'sys'
op|'.'
name|'path'
op|'.'
name|'append'
op|'('
name|'os'
op|'.'
name|'getcwd'
op|'('
op|')'
op|')'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'iniparser'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PropertyCollecter
name|'class'
name|'PropertyCollecter'
op|'('
name|'iniparser'
op|'.'
name|'BaseParser'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
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
name|'PropertyCollecter'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'key_value_pairs'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|assignment
dedent|''
name|'def'
name|'assignment'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'key_value_pairs'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
DECL|member|new_section
dedent|''
name|'def'
name|'new_section'
op|'('
name|'self'
op|','
name|'section'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|collect_properties
name|'def'
name|'collect_properties'
op|'('
name|'cls'
op|','
name|'lineiter'
op|','
name|'sample_format'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
DECL|function|clean_sample
indent|'        '
name|'def'
name|'clean_sample'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'line'
name|'in'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'line'
op|'.'
name|'startswith'
op|'('
string|'"# "'
op|')'
name|'and'
name|'line'
op|'!='
string|"'# nova.conf sample #\\n'"
op|':'
newline|'\n'
indent|'                    '
name|'line'
op|'='
name|'line'
op|'['
number|'2'
op|':'
op|']'
newline|'\n'
dedent|''
name|'yield'
name|'line'
newline|'\n'
dedent|''
dedent|''
name|'pc'
op|'='
name|'cls'
op|'('
op|')'
newline|'\n'
name|'if'
name|'sample_format'
op|':'
newline|'\n'
indent|'            '
name|'lineiter'
op|'='
name|'clean_sample'
op|'('
name|'lineiter'
op|')'
newline|'\n'
dedent|''
name|'pc'
op|'.'
name|'parse'
op|'('
name|'lineiter'
op|')'
newline|'\n'
name|'return'
name|'pc'
op|'.'
name|'key_value_pairs'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|"'__main__'"
op|':'
newline|'\n'
indent|'    '
name|'parser'
op|'='
name|'argparse'
op|'.'
name|'ArgumentParser'
op|'('
name|'description'
op|'='
string|"'''Compare the nova.conf\n    file with the nova.conf.sample file to find any unused options or\n    default values in nova.conf'''"
op|')'
newline|'\n'
nl|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'-c'"
op|','
name|'action'
op|'='
string|"'store'"
op|','
nl|'\n'
name|'default'
op|'='
string|"'/etc/nova/nova.conf'"
op|','
nl|'\n'
name|'help'
op|'='
string|"'path to nova.conf\\\n                        (defaults to /etc/nova/nova.conf)'"
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'-s'"
op|','
name|'default'
op|'='
string|"'./etc/nova/nova.conf.sample'"
op|','
nl|'\n'
name|'help'
op|'='
string|"'path to nova.conf.sample\\\n                        (defaults to ./etc/nova/nova.conf.sample'"
op|')'
newline|'\n'
DECL|variable|options
name|'options'
op|'='
name|'parser'
op|'.'
name|'parse_args'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|variable|conf_file_options
name|'conf_file_options'
op|'='
name|'PropertyCollecter'
op|'.'
name|'collect_properties'
op|'('
name|'open'
op|'('
name|'options'
op|'.'
name|'c'
op|')'
op|')'
newline|'\n'
DECL|variable|sample_conf_file_options
name|'sample_conf_file_options'
op|'='
name|'PropertyCollecter'
op|'.'
name|'collect_properties'
op|'('
nl|'\n'
name|'open'
op|'('
name|'options'
op|'.'
name|'s'
op|')'
op|','
name|'sample_format'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'sorted'
op|'('
name|'conf_file_options'
op|'.'
name|'items'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'k'
name|'not'
name|'in'
name|'sample_conf_file_options'
op|':'
newline|'\n'
indent|'            '
name|'print'
string|'"Unused:"'
op|','
name|'k'
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'sorted'
op|'('
name|'conf_file_options'
op|'.'
name|'items'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'k'
name|'in'
name|'sample_conf_file_options'
name|'and'
name|'v'
op|'=='
name|'sample_conf_file_options'
op|'['
name|'k'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'print'
string|'"Default valued:"'
op|','
name|'k'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
