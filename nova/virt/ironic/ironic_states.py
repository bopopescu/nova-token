begin_unit
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
nl|'\n'
comment|'# Copyright 2010 OpenStack Foundation'
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
string|'"""\nMapping of bare metal node states.\n\nA node may have empty {} `properties` and `driver_info` in which case, it is\nsaid to be "initialized" but "not available", and the state is NOSTATE.\n\nWhen updating `properties`,  any data will be rejected if the data fails to be\nvalidated by the driver. Any node with non-empty `properties` is said to be\n"initialized", and the state is INIT.\n\nWhen the driver has received both `properties` and `driver_info`, it will check\nthe power status of the node and update the `power_state` accordingly. If the\ndriver fails to read the power state from the node, it will reject the\n`driver_info` change, and the state will remain as INIT. If the power status\ncheck succeeds, `power_state` will change to one of POWER_ON or POWER_OFF,\naccordingly.\n\nAt this point, the power state may be changed via the API, a console\nmay be started, and a tenant may be associated.\n\nThe `power_state` for a node always represents the current power state. Any\npower operation sets this to the actual state when done (whether successful or\nnot). It is set to ERROR only when unable to get the power state from a node.\n\nWhen `instance_uuid` is set to a non-empty / non-None value, the node is said\nto be "associated" with a tenant.\n\nAn associated node can not be deleted.\n\nThe `instance_uuid` field may be unset only if the node is in POWER_OFF or\nERROR states.\n"""'
newline|'\n'
nl|'\n'
DECL|variable|NOSTATE
name|'NOSTATE'
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
DECL|variable|DEPLOYWAIT
name|'DEPLOYWAIT'
op|'='
string|"'wait call-back'"
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
DECL|variable|DELETING
name|'DELETING'
op|'='
string|"'deleting'"
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
DECL|variable|REBUILD
name|'REBUILD'
op|'='
string|"'rebuild'"
newline|'\n'
nl|'\n'
DECL|variable|POWER_ON
name|'POWER_ON'
op|'='
string|"'power on'"
newline|'\n'
DECL|variable|POWER_OFF
name|'POWER_OFF'
op|'='
string|"'power off'"
newline|'\n'
DECL|variable|REBOOT
name|'REBOOT'
op|'='
string|"'rebooting'"
newline|'\n'
DECL|variable|SUSPEND
name|'SUSPEND'
op|'='
string|"'suspended'"
newline|'\n'
endmarker|''
end_unit
