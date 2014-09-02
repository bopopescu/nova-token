begin_unit
comment|'# Copyright 2014 Rackspace, Andrew Melton'
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
comment|'#     http://www.apache.org/licenses/LICENSE-2.0'
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
string|'"""\n##########\nIDMapShift\n##########\n\nIDMapShift is a tool that properly sets the ownership of a filesystem for use\nwith linux user namespaces.\n\n=====\nUsage\n=====\n\n    nova-idmapshift -i -u 0:10000:2000 -g 0:10000:2000 path\n\nThis command will idempotently shift `path` to proper ownership using\nthe provided uid and gid mappings.\n\n=========\nArguments\n=========\n\n    nova-idmapshift -i -c -d -v\n                    -u [[guest-uid:host-uid:count],...]\n                    -g [[guest-gid:host-gid:count],...]\n                    -n [nobody-id]\n                    path\n\npath: Root path of the filesystem to be shifted\n\n-i, --idempotent: Shift operation will only be performed if filesystem\nappears unshifted\n\n-c, --confirm: Will perform check on filesystem\nReturns 0 when filesystem appears shifted\nReturns 1 when filesystem appears unshifted\n\n-d, --dry-run: Print chown operations, but won\'t perform them\n\n-v, --verbose: Print chown operations while performing them\n\n-u, --uid: User ID mappings, maximum of 3 ranges\n\n-g, --gid: Group ID mappings, maximum of 3 ranges\n\n-n, --nobody: ID to map all unmapped uid and gids to.\n\n=======\nPurpose\n=======\n\nWhen using user namespaces with linux containers, the filesystem of the\ncontainer must be owned by the targeted user and group ids being applied\nto that container. Otherwise, processes inside the container won\'t be able\nto access the filesystem.\n\nFor example, when using the id map string \'0:10000:2000\', this means that\nuser ids inside the container between 0 and 1999 will map to user ids on\nthe host between 10000 and 11999. Root (0) becomes 10000, user 1 becomes\n10001, user 50 becomes 10050 and user 1999 becomes 11999. This means that\nfiles that are owned by root need to actually be owned by user 10000, and\nfiles owned by 50 need to be owned by 10050, and so on.\n\nIDMapShift will take the uid and gid strings used for user namespaces and\nproperly set up the filesystem for use by those users. Uids and gids outside\nof provided ranges will be mapped to nobody (max uid/gid) so that they are\ninaccessible inside the container.\n"""'
newline|'\n'
nl|'\n'
nl|'\n'
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
DECL|variable|NOBODY_ID
name|'NOBODY_ID'
op|'='
number|'65534'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_target_id
name|'def'
name|'find_target_id'
op|'('
name|'fsid'
op|','
name|'mappings'
op|','
name|'nobody'
op|','
name|'memo'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'fsid'
name|'not'
name|'in'
name|'memo'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'start'
op|','
name|'target'
op|','
name|'count'
name|'in'
name|'mappings'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'start'
op|'<='
name|'fsid'
op|'<'
name|'start'
op|'+'
name|'count'
op|':'
newline|'\n'
indent|'                '
name|'memo'
op|'['
name|'fsid'
op|']'
op|'='
op|'('
name|'fsid'
op|'-'
name|'start'
op|')'
op|'+'
name|'target'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'memo'
op|'['
name|'fsid'
op|']'
op|'='
name|'nobody'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'memo'
op|'['
name|'fsid'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|print_chown
dedent|''
name|'def'
name|'print_chown'
op|'('
name|'path'
op|','
name|'uid'
op|','
name|'gid'
op|','
name|'target_uid'
op|','
name|'target_gid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'print'
op|'('
string|"'%s %s:%s -> %s:%s'"
op|'%'
op|'('
name|'path'
op|','
name|'uid'
op|','
name|'gid'
op|','
name|'target_uid'
op|','
name|'target_gid'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|shift_path
dedent|''
name|'def'
name|'shift_path'
op|'('
name|'path'
op|','
name|'uid_mappings'
op|','
name|'gid_mappings'
op|','
name|'nobody'
op|','
name|'uid_memo'
op|','
name|'gid_memo'
op|','
nl|'\n'
name|'dry_run'
op|'='
name|'False'
op|','
name|'verbose'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'stat'
op|'='
name|'os'
op|'.'
name|'lstat'
op|'('
name|'path'
op|')'
newline|'\n'
name|'uid'
op|'='
name|'stat'
op|'.'
name|'st_uid'
newline|'\n'
name|'gid'
op|'='
name|'stat'
op|'.'
name|'st_gid'
newline|'\n'
name|'target_uid'
op|'='
name|'find_target_id'
op|'('
name|'uid'
op|','
name|'uid_mappings'
op|','
name|'nobody'
op|','
name|'uid_memo'
op|')'
newline|'\n'
name|'target_gid'
op|'='
name|'find_target_id'
op|'('
name|'gid'
op|','
name|'gid_mappings'
op|','
name|'nobody'
op|','
name|'gid_memo'
op|')'
newline|'\n'
name|'if'
name|'verbose'
op|':'
newline|'\n'
indent|'        '
name|'print_chown'
op|'('
name|'path'
op|','
name|'uid'
op|','
name|'gid'
op|','
name|'target_uid'
op|','
name|'target_gid'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'dry_run'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'lchown'
op|'('
name|'path'
op|','
name|'target_uid'
op|','
name|'target_gid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|shift_dir
dedent|''
dedent|''
name|'def'
name|'shift_dir'
op|'('
name|'fsdir'
op|','
name|'uid_mappings'
op|','
name|'gid_mappings'
op|','
name|'nobody'
op|','
nl|'\n'
name|'dry_run'
op|'='
name|'False'
op|','
name|'verbose'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'uid_memo'
op|'='
name|'dict'
op|'('
op|')'
newline|'\n'
name|'gid_memo'
op|'='
name|'dict'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|shift_path_short
name|'def'
name|'shift_path_short'
op|'('
name|'p'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'shift_path'
op|'('
name|'p'
op|','
name|'uid_mappings'
op|','
name|'gid_mappings'
op|','
name|'nobody'
op|','
nl|'\n'
name|'dry_run'
op|'='
name|'dry_run'
op|','
name|'verbose'
op|'='
name|'verbose'
op|','
nl|'\n'
name|'uid_memo'
op|'='
name|'uid_memo'
op|','
name|'gid_memo'
op|'='
name|'gid_memo'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'shift_path_short'
op|'('
name|'fsdir'
op|')'
newline|'\n'
name|'for'
name|'root'
op|','
name|'dirs'
op|','
name|'files'
name|'in'
name|'os'
op|'.'
name|'walk'
op|'('
name|'fsdir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'d'
name|'in'
name|'dirs'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'root'
op|','
name|'d'
op|')'
newline|'\n'
name|'shift_path_short'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'f'
name|'in'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'root'
op|','
name|'f'
op|')'
newline|'\n'
name|'shift_path_short'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|confirm_path
dedent|''
dedent|''
dedent|''
name|'def'
name|'confirm_path'
op|'('
name|'path'
op|','
name|'uid_ranges'
op|','
name|'gid_ranges'
op|','
name|'nobody'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'stat'
op|'='
name|'os'
op|'.'
name|'lstat'
op|'('
name|'path'
op|')'
newline|'\n'
name|'uid'
op|'='
name|'stat'
op|'.'
name|'st_uid'
newline|'\n'
name|'gid'
op|'='
name|'stat'
op|'.'
name|'st_gid'
newline|'\n'
nl|'\n'
name|'uid_in_range'
op|'='
name|'True'
name|'if'
name|'uid'
op|'=='
name|'nobody'
name|'else'
name|'False'
newline|'\n'
name|'gid_in_range'
op|'='
name|'True'
name|'if'
name|'gid'
op|'=='
name|'nobody'
name|'else'
name|'False'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'uid_in_range'
name|'or'
name|'not'
name|'gid_in_range'
op|':'
newline|'\n'
indent|'        '
name|'for'
op|'('
name|'start'
op|','
name|'end'
op|')'
name|'in'
name|'uid_ranges'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'start'
op|'<='
name|'uid'
op|'<='
name|'end'
op|':'
newline|'\n'
indent|'                '
name|'uid_in_range'
op|'='
name|'True'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'for'
op|'('
name|'start'
op|','
name|'end'
op|')'
name|'in'
name|'gid_ranges'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'start'
op|'<='
name|'gid'
op|'<='
name|'end'
op|':'
newline|'\n'
indent|'                '
name|'gid_in_range'
op|'='
name|'True'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'uid_in_range'
name|'and'
name|'gid_in_range'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_ranges
dedent|''
name|'def'
name|'get_ranges'
op|'('
name|'maps'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
op|'('
name|'target'
op|','
name|'target'
op|'+'
name|'count'
op|'-'
number|'1'
op|')'
name|'for'
op|'('
name|'start'
op|','
name|'target'
op|','
name|'count'
op|')'
name|'in'
name|'maps'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|confirm_dir
dedent|''
name|'def'
name|'confirm_dir'
op|'('
name|'fsdir'
op|','
name|'uid_mappings'
op|','
name|'gid_mappings'
op|','
name|'nobody'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'uid_ranges'
op|'='
name|'get_ranges'
op|'('
name|'uid_mappings'
op|')'
newline|'\n'
name|'gid_ranges'
op|'='
name|'get_ranges'
op|'('
name|'gid_mappings'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'confirm_path'
op|'('
name|'fsdir'
op|','
name|'uid_ranges'
op|','
name|'gid_ranges'
op|','
name|'nobody'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'for'
name|'root'
op|','
name|'dirs'
op|','
name|'files'
name|'in'
name|'os'
op|'.'
name|'walk'
op|'('
name|'fsdir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'d'
name|'in'
name|'dirs'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'root'
op|','
name|'d'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'confirm_path'
op|'('
name|'path'
op|','
name|'uid_ranges'
op|','
name|'gid_ranges'
op|','
name|'nobody'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'f'
name|'in'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'root'
op|','
name|'f'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'confirm_path'
op|'('
name|'path'
op|','
name|'uid_ranges'
op|','
name|'gid_ranges'
op|','
name|'nobody'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|id_map_type
dedent|''
name|'def'
name|'id_map_type'
op|'('
name|'val'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'maps'
op|'='
name|'val'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
newline|'\n'
name|'id_maps'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'m'
name|'in'
name|'maps'
op|':'
newline|'\n'
indent|'        '
name|'map_vals'
op|'='
name|'m'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'map_vals'
op|')'
op|'!='
number|'3'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
string|"'Invalid id map %s, correct syntax is '"
nl|'\n'
string|"'guest-id:host-id:count.'"
op|')'
newline|'\n'
name|'raise'
name|'argparse'
op|'.'
name|'ArgumentTypeError'
op|'('
name|'msg'
op|'%'
name|'val'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vals'
op|'='
op|'['
name|'int'
op|'('
name|'i'
op|')'
name|'for'
name|'i'
name|'in'
name|'map_vals'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
string|"'Invalid id map %s, values must be integers'"
op|'%'
name|'val'
newline|'\n'
name|'raise'
name|'argparse'
op|'.'
name|'ArgumentTypeError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'id_maps'
op|'.'
name|'append'
op|'('
name|'tuple'
op|'('
name|'vals'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'id_maps'
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
name|'parser'
op|'='
name|'argparse'
op|'.'
name|'ArgumentParser'
op|'('
string|"'User Namespace FS Owner Shift'"
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'path'"
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'-u'"
op|','
string|"'--uid'"
op|','
name|'type'
op|'='
name|'id_map_type'
op|','
name|'default'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'-g'"
op|','
string|"'--gid'"
op|','
name|'type'
op|'='
name|'id_map_type'
op|','
name|'default'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'-n'"
op|','
string|"'--nobody'"
op|','
name|'default'
op|'='
name|'NOBODY_ID'
op|','
name|'type'
op|'='
name|'int'
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'-i'"
op|','
string|"'--idempotent'"
op|','
name|'action'
op|'='
string|"'store_true'"
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'-c'"
op|','
string|"'--confirm'"
op|','
name|'action'
op|'='
string|"'store_true'"
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'-d'"
op|','
string|"'--dry-run'"
op|','
name|'action'
op|'='
string|"'store_true'"
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'-v'"
op|','
string|"'--verbose'"
op|','
name|'action'
op|'='
string|"'store_true'"
op|')'
newline|'\n'
name|'args'
op|'='
name|'parser'
op|'.'
name|'parse_args'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'args'
op|'.'
name|'idempotent'
name|'or'
name|'args'
op|'.'
name|'confirm'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'confirm_dir'
op|'('
name|'args'
op|'.'
name|'path'
op|','
name|'args'
op|'.'
name|'uid'
op|','
name|'args'
op|'.'
name|'gid'
op|','
name|'args'
op|'.'
name|'nobody'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'sys'
op|'.'
name|'exit'
op|'('
number|'0'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'args'
op|'.'
name|'confirm'
op|':'
newline|'\n'
indent|'                '
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'shift_dir'
op|'('
name|'args'
op|'.'
name|'path'
op|','
name|'args'
op|'.'
name|'uid'
op|','
name|'args'
op|'.'
name|'gid'
op|','
name|'args'
op|'.'
name|'nobody'
op|','
nl|'\n'
name|'dry_run'
op|'='
name|'args'
op|'.'
name|'dry_run'
op|','
name|'verbose'
op|'='
name|'args'
op|'.'
name|'verbose'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
