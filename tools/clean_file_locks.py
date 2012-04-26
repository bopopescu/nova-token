begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 La Honda Research Center, Inc.'
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
nl|'\n'
string|'"""clean_file_locks.py - Cleans stale interprocess locks\n\nThis rountine can be used to find and delete stale lock files from\nnova\'s interprocess synchroization.  It can be used safely while services\nare running.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'optparse'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'log'
op|'.'
name|'getLogger'
op|'('
string|"'nova.utils'"
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_options
name|'def'
name|'parse_options'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""process command line options."""'
newline|'\n'
nl|'\n'
name|'parser'
op|'='
name|'optparse'
op|'.'
name|'OptionParser'
op|'('
string|"'usage: %prog [options]'"
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_option'
op|'('
string|"'--verbose'"
op|','
name|'action'
op|'='
string|"'store_true'"
op|','
nl|'\n'
name|'help'
op|'='
string|"'List lock files found and deleted'"
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
name|'return'
name|'options'
op|','
name|'args'
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
string|'"""Main loop."""'
newline|'\n'
name|'options'
op|','
name|'args'
op|'='
name|'parse_options'
op|'('
op|')'
newline|'\n'
name|'verbose'
op|'='
name|'options'
op|'.'
name|'verbose'
newline|'\n'
nl|'\n'
name|'if'
name|'verbose'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'logger'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'logger'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'INFO'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'Cleaning stale locks from %s'"
op|'%'
name|'FLAGS'
op|'.'
name|'lock_path'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'cleanup_file_locks'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'Finished'"
op|')'
newline|'\n'
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
