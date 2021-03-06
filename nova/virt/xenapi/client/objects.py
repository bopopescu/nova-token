begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
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
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPISessionObject
name|'class'
name|'XenAPISessionObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wrapper to make calling and mocking the session easier\n\n    The XenAPI protocol is an XML RPC API that is based around the\n    XenAPI database, and operations you can do on each of the objects\n    stored in the database, such as VM, SR, VDI, etc.\n\n    For more details see the XenAPI docs:\n    http://docs.vmd.citrix.com/XenServer/6.2.0/1.0/en_gb/api/\n\n    Most, objects like VM, SR, VDI, etc, share a common set of methods:\n    * vm_ref = session.VM.create(vm_rec)\n    * vm_ref = session.VM.get_by_uuid(uuid)\n    * session.VM.destroy(vm_ref)\n    * vm_refs = session.VM.get_all()\n\n    Each object also has specific messages, or functions, such as:\n    * session.VM.clean_reboot(vm_ref)\n\n    Each object has fields, like "VBDs" that can be fetched like this:\n    * vbd_refs = session.VM.get_VBDs(vm_ref)\n\n    You can get all the fields by fetching the full record.\n    However please note this is much more expensive than just\n    fetching the field you require:\n    * vm_rec = session.VM.get_record(vm_ref)\n\n    When searching for particular objects, you may be tempted\n    to use get_all(), but this often leads to races as objects\n    get deleted under your feet. It is preferable to use the undocumented:\n    * vms = session.VM.get_all_records_where(\n    \'field "is_control_domain"="true"\')\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'='
name|'session'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
nl|'\n'
DECL|member|_call_method
dedent|''
name|'def'
name|'_call_method'
op|'('
name|'self'
op|','
name|'method_name'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'call'
op|'='
string|'"%s.%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'name'
op|','
name|'method_name'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_xenapi'
op|'('
name|'call'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'method_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'lambda'
op|'*'
name|'params'
op|':'
name|'self'
op|'.'
name|'_call_method'
op|'('
name|'method_name'
op|','
op|'*'
name|'params'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VM
dedent|''
dedent|''
name|'class'
name|'VM'
op|'('
name|'XenAPISessionObject'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Virtual Machine."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VM'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
string|'"VM"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VBD
dedent|''
dedent|''
name|'class'
name|'VBD'
op|'('
name|'XenAPISessionObject'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Virtual block device."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VBD'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
string|'"VBD"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|plug
dedent|''
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'vbd_ref'
op|','
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'xenapi-vbd-'"
op|'+'
name|'vm_ref'
op|')'
newline|'\n'
DECL|function|synchronized_plug
name|'def'
name|'synchronized_plug'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_call_method'
op|'('
string|'"plug"'
op|','
name|'vbd_ref'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(johngarbutt) we need to ensure there is only ever one'
nl|'\n'
comment|'# VBD.unplug or VBD.plug happening at once per VM'
nl|'\n'
comment|'# due to a bug in XenServer 6.1 and 6.2'
nl|'\n'
dedent|''
name|'synchronized_plug'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|unplug
dedent|''
name|'def'
name|'unplug'
op|'('
name|'self'
op|','
name|'vbd_ref'
op|','
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'xenapi-vbd-'"
op|'+'
name|'vm_ref'
op|')'
newline|'\n'
DECL|function|synchronized_unplug
name|'def'
name|'synchronized_unplug'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_call_method'
op|'('
string|'"unplug"'
op|','
name|'vbd_ref'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(johngarbutt) we need to ensure there is only ever one'
nl|'\n'
comment|'# VBD.unplug or VBD.plug happening at once per VM'
nl|'\n'
comment|'# due to a bug in XenServer 6.1 and 6.2'
nl|'\n'
dedent|''
name|'synchronized_unplug'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VDI
dedent|''
dedent|''
name|'class'
name|'VDI'
op|'('
name|'XenAPISessionObject'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Virtual disk image."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VDI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
string|'"VDI"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SR
dedent|''
dedent|''
name|'class'
name|'SR'
op|'('
name|'XenAPISessionObject'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Storage Repository."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'SR'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
string|'"SR"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PBD
dedent|''
dedent|''
name|'class'
name|'PBD'
op|'('
name|'XenAPISessionObject'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Physical block device."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'PBD'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
string|'"PBD"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PIF
dedent|''
dedent|''
name|'class'
name|'PIF'
op|'('
name|'XenAPISessionObject'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Physical Network Interface."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'PIF'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
string|'"PIF"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VLAN
dedent|''
dedent|''
name|'class'
name|'VLAN'
op|'('
name|'XenAPISessionObject'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VLAN."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VLAN'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
string|'"VLAN"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Host
dedent|''
dedent|''
name|'class'
name|'Host'
op|'('
name|'XenAPISessionObject'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""XenServer hosts."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Host'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
string|'"host"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Network
dedent|''
dedent|''
name|'class'
name|'Network'
op|'('
name|'XenAPISessionObject'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Networks that VIFs are attached to."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Network'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
string|'"network"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Pool
dedent|''
dedent|''
name|'class'
name|'Pool'
op|'('
name|'XenAPISessionObject'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Pool of hosts."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Pool'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
string|'"pool"'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
