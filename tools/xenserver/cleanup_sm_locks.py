begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 OpenStack Foundation'
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
comment|'# http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'# See the License for the specific language governing permissions and'
nl|'\n'
comment|'# limitations under the License.'
nl|'\n'
string|'"""\nScript to cleanup old XenServer /var/lock/sm locks.\n\nXenServer 5.6 and 6.0 do not appear to always cleanup locks when using a\nFileSR. ext3 has a limit of 32K inode links, so when we have 32K-2 (31998)\nlocks laying around, builds will begin to fail because we can\'t create any\nadditional locks.  This cleanup script is something we can run periodically as\na stop-gap measure until this is fixed upstream.\n\nThis script should be run on the dom0 of the affected machine.\n"""'
newline|'\n'
name|'import'
name|'errno'
newline|'\n'
name|'import'
name|'optparse'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
DECL|variable|BASE
name|'BASE'
op|'='
string|"'/var/lock/sm'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_age_days
name|'def'
name|'_get_age_days'
op|'('
name|'secs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'float'
op|'('
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'-'
name|'secs'
op|')'
op|'/'
number|'86400'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_parse_args
dedent|''
name|'def'
name|'_parse_args'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'parser'
op|'='
name|'optparse'
op|'.'
name|'OptionParser'
op|'('
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_option'
op|'('
string|'"-d"'
op|','
string|'"--dry-run"'
op|','
nl|'\n'
name|'action'
op|'='
string|'"store_true"'
op|','
name|'dest'
op|'='
string|'"dry_run"'
op|','
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
name|'help'
op|'='
string|'"don\'t actually remove locks"'
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_option'
op|'('
string|'"-l"'
op|','
string|'"--limit"'
op|','
nl|'\n'
name|'action'
op|'='
string|'"store"'
op|','
name|'type'
op|'='
string|"'int'"
op|','
name|'dest'
op|'='
string|'"limit"'
op|','
nl|'\n'
name|'default'
op|'='
name|'sys'
op|'.'
name|'maxint'
op|','
nl|'\n'
name|'help'
op|'='
string|'"max number of locks to delete (default: no limit)"'
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_option'
op|'('
string|'"-v"'
op|','
string|'"--verbose"'
op|','
nl|'\n'
name|'action'
op|'='
string|'"store_true"'
op|','
name|'dest'
op|'='
string|'"verbose"'
op|','
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
name|'help'
op|'='
string|'"don\'t print status messages to stdout"'
op|')'
newline|'\n'
nl|'\n'
name|'options'
op|','
name|'args'
op|'='
name|'parser'
op|'.'
name|'parse_args'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'days_old'
op|'='
name|'int'
op|'('
name|'args'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'IndexError'
op|','
name|'ValueError'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'parser'
op|'.'
name|'print_help'
op|'('
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'options'
op|','
name|'days_old'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
dedent|''
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'options'
op|','
name|'days_old'
op|'='
name|'_parse_args'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'BASE'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
op|'>>'
name|'sys'
op|'.'
name|'stderr'
op|','
string|'"error: \'%s\' doesn\'t exist. Make sure you\'re"'
string|'" running this on the dom0."'
op|'%'
name|'BASE'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'lockpaths_removed'
op|'='
number|'0'
newline|'\n'
name|'nspaths_removed'
op|'='
number|'0'
newline|'\n'
nl|'\n'
name|'for'
name|'nsname'
name|'in'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'BASE'
op|')'
op|'['
op|':'
name|'options'
op|'.'
name|'limit'
op|']'
op|':'
newline|'\n'
indent|'        '
name|'nspath'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'BASE'
op|','
name|'nsname'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
name|'nspath'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# Remove old lockfiles'
nl|'\n'
dedent|''
name|'removed'
op|'='
number|'0'
newline|'\n'
name|'locknames'
op|'='
name|'os'
op|'.'
name|'listdir'
op|'('
name|'nspath'
op|')'
newline|'\n'
name|'for'
name|'lockname'
name|'in'
name|'locknames'
op|':'
newline|'\n'
indent|'            '
name|'lockpath'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'nspath'
op|','
name|'lockname'
op|')'
newline|'\n'
name|'lock_age_days'
op|'='
name|'_get_age_days'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'getmtime'
op|'('
name|'lockpath'
op|')'
op|')'
newline|'\n'
name|'if'
name|'lock_age_days'
op|'>'
name|'days_old'
op|':'
newline|'\n'
indent|'                '
name|'lockpaths_removed'
op|'+='
number|'1'
newline|'\n'
name|'removed'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
name|'if'
name|'options'
op|'.'
name|'verbose'
op|':'
newline|'\n'
indent|'                    '
name|'print'
string|"'Removing old lock: %03d %s'"
op|'%'
op|'('
name|'lock_age_days'
op|','
nl|'\n'
name|'lockpath'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'options'
op|'.'
name|'dry_run'
op|':'
newline|'\n'
indent|'                    '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'lockpath'
op|')'
newline|'\n'
nl|'\n'
comment|'# Remove empty namespace paths'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'len'
op|'('
name|'locknames'
op|')'
op|'=='
name|'removed'
op|':'
newline|'\n'
indent|'            '
name|'nspaths_removed'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
name|'if'
name|'options'
op|'.'
name|'verbose'
op|':'
newline|'\n'
indent|'                '
name|'print'
string|"'Removing empty namespace: %s'"
op|'%'
name|'nspath'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'options'
op|'.'
name|'dry_run'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'os'
op|'.'
name|'rmdir'
op|'('
name|'nspath'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'e'
op|'.'
name|'errno'
op|'=='
name|'errno'
op|'.'
name|'ENOTEMPTY'
op|':'
newline|'\n'
indent|'                        '
name|'print'
op|'>>'
name|'sys'
op|'.'
name|'stderr'
op|','
string|'"warning: directory \'%s\'"'
string|'" not empty"'
op|'%'
name|'nspath'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'if'
name|'options'
op|'.'
name|'dry_run'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"** Dry Run **"'
newline|'\n'
nl|'\n'
dedent|''
name|'print'
string|'"Total locks removed: "'
op|','
name|'lockpaths_removed'
newline|'\n'
name|'print'
string|'"Total namespaces removed: "'
op|','
name|'nspaths_removed'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|"'__main__'"
op|':'
newline|'\n'
indent|'    '
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
