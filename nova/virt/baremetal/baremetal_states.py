begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
string|'"""\nPossible baremetal node states for instances.\n\nCompute instance baremetal states represent the state of an instance as it\npertains to a user or administrator. When combined with task states\n(task_states.py), a better picture can be formed regarding the instance\'s\nhealth.\n\n"""'
newline|'\n'
nl|'\n'
DECL|variable|NULL
name|'NULL'
op|'='
name|'None'
newline|'\n'
DECL|variable|INIT
name|'INIT'
op|'='
string|"'initializing'"
newline|'\n'
DECL|variable|ACTIVE
name|'ACTIVE'
op|'='
string|"'active'"
newline|'\n'
DECL|variable|BUILDING
name|'BUILDING'
op|'='
string|"'building'"
newline|'\n'
DECL|variable|DEPLOYING
name|'DEPLOYING'
op|'='
string|"'deploying'"
newline|'\n'
DECL|variable|DEPLOYFAIL
name|'DEPLOYFAIL'
op|'='
string|"'deploy failed'"
newline|'\n'
DECL|variable|DEPLOYDONE
name|'DEPLOYDONE'
op|'='
string|"'deploy complete'"
newline|'\n'
DECL|variable|DELETED
name|'DELETED'
op|'='
string|"'deleted'"
newline|'\n'
DECL|variable|ERROR
name|'ERROR'
op|'='
string|"'error'"
newline|'\n'
endmarker|''
end_unit
