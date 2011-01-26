begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Cloud.com, Inc'
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
string|'"""\nA connection to Hyper-V .\nUses Windows Management Instrumentation (WMI) calls to interact with Hyper-V\nHyper-V WMI usage:\n    http://msdn.microsoft.com/en-us/library/cc723875%28v=VS.85%29.aspx\nThe Hyper-V object model briefly:\n    The physical computer and its hosted virtual machines are each represented\n    by the Msvm_ComputerSystem class.\n\n    Each virtual machine is associated with a\n    Msvm_VirtualSystemGlobalSettingData (vs_gs_data) instance and one or more\n    Msvm_VirtualSystemSettingData (vmsetting) instances. For each vmsetting\n    there is a series of Msvm_ResourceAllocationSettingData (rasd) objects.\n    The rasd objects describe the settings for each device in a VM.\n    Together, the vs_gs_data, vmsettings and rasds describe the configuration\n    of the virtual machine.\n\n    Creating new resources such as disks and nics involves cloning a default\n    rasd object and appropriately modifying the clone and calling the\n    AddVirtualSystemResources WMI method\n    Changing resources such as memory uses the ModifyVirtualSystemResources\n    WMI method\n\nUsing the Python WMI library:\n    Tutorial:\n        http://timgolden.me.uk/python/wmi/tutorial.html\n    Hyper-V WMI objects can be retrieved simply by using the class name\n    of the WMI object and optionally specifying a column to filter the\n    result set. More complex filters can be formed using WQL (sql-like)\n    queries.\n    The parameters and return tuples of WMI method calls can gleaned by\n    examining the doc string. For example:\n    >>> vs_man_svc.ModifyVirtualSystemResources.__doc__\n    ModifyVirtualSystemResources (ComputerSystem, ResourceSettingData[])\n                 => (Job, ReturnValue)\'\n    When passing setting data (ResourceSettingData) to the WMI method,\n    an XML representation of the data is passed in using GetText_(1).\n    Available methods on a service can be determined using method.keys():\n    >>> vs_man_svc.methods.keys()\n    vmsettings and rasds for a vm can be retrieved using the \'associators\'\n    method with the appropriate return class.\n    Long running WMI commands generally return a Job (an instance of\n    Msvm_ConcreteJob) whose state can be polled to determine when it finishes\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'images'
newline|'\n'
nl|'\n'
DECL|variable|wmi
name|'wmi'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.virt.hyperv'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|HYPERV_POWER_STATE
name|'HYPERV_POWER_STATE'
op|'='
op|'{'
nl|'\n'
number|'3'
op|':'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|','
nl|'\n'
number|'2'
op|':'
name|'power_state'
op|'.'
name|'RUNNING'
op|','
nl|'\n'
number|'32768'
op|':'
name|'power_state'
op|'.'
name|'PAUSED'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|REQ_POWER_STATE
name|'REQ_POWER_STATE'
op|'='
op|'{'
nl|'\n'
string|"'Enabled'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'Disabled'"
op|':'
number|'3'
op|','
nl|'\n'
string|"'Reboot'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'Reset'"
op|':'
number|'11'
op|','
nl|'\n'
string|"'Paused'"
op|':'
number|'32768'
op|','
nl|'\n'
string|"'Suspended'"
op|':'
number|'32769'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|WMI_JOB_STATUS_STARTED
name|'WMI_JOB_STATUS_STARTED'
op|'='
number|'4096'
newline|'\n'
DECL|variable|WMI_JOB_STATE_RUNNING
name|'WMI_JOB_STATE_RUNNING'
op|'='
number|'4'
newline|'\n'
DECL|variable|WMI_JOB_STATE_COMPLETED
name|'WMI_JOB_STATE_COMPLETED'
op|'='
number|'7'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_connection
name|'def'
name|'get_connection'
op|'('
name|'_'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'wmi'
newline|'\n'
name|'if'
name|'wmi'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'wmi'
op|'='
name|'__import__'
op|'('
string|"'wmi'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'HyperVConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HyperVConnection
dedent|''
name|'class'
name|'HyperVConnection'
op|'('
name|'object'
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
name|'self'
op|'.'
name|'_conn'
op|'='
name|'wmi'
op|'.'
name|'WMI'
op|'('
name|'moniker'
op|'='
string|"'//./root/virtualization'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_cim_conn'
op|'='
name|'wmi'
op|'.'
name|'WMI'
op|'('
name|'moniker'
op|'='
string|"'//./root/cimv2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
name|'def'
name|'init_host'
op|'('
name|'self'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
comment|'#FIXME(chiradeep): implement this'
nl|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'In init host'"
op|')'
op|')'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|list_instances
dedent|''
name|'def'
name|'list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Return the names of all the instances known to Hyper-V. """'
newline|'\n'
name|'vms'
op|'='
op|'['
name|'v'
op|'.'
name|'ElementName'
name|'for'
name|'v'
name|'in'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ComputerSystem'
op|'('
op|'['
string|"'ElementName'"
op|']'
op|')'
op|']'
newline|'\n'
name|'return'
name|'vms'
newline|'\n'
nl|'\n'
DECL|member|spawn
dedent|''
name|'def'
name|'spawn'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Create a new VM and start it."""'
newline|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Duplicate'
op|'('
name|'_'
op|'('
string|"'Attempt to create duplicate vm %s'"
op|')'
op|'%'
nl|'\n'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'user'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_user'
op|'('
name|'instance'
op|'['
string|"'user_id'"
op|']'
op|')'
newline|'\n'
name|'project'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_project'
op|'('
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
comment|'#Fetch the file, assume it is a VHD file.'
nl|'\n'
name|'base_vhd_filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'instances_path'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'vhdfile'
op|'='
string|'"%s.vhd"'
op|'%'
op|'('
name|'base_vhd_filename'
op|')'
newline|'\n'
name|'images'
op|'.'
name|'fetch'
op|'('
name|'instance'
op|'['
string|"'image_id'"
op|']'
op|','
name|'vhdfile'
op|','
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_create_vm'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_create_disk'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
name|'vhdfile'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_nic'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
name|'instance'
op|'['
string|"'mac_address'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Starting VM %s '"
op|')'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_set_vm_state'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
string|"'Enabled'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Started VM %s '"
op|')'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exn'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'spawn vm failed: %s'"
op|')'
op|','
name|'exn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'destroy'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_vm
dedent|''
dedent|''
name|'def'
name|'_create_vm'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a VM but don\'t start it.  """'
newline|'\n'
name|'vs_man_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'vs_gs_data'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemGlobalSettingData'
op|'.'
name|'new'
op|'('
op|')'
newline|'\n'
name|'vs_gs_data'
op|'.'
name|'ElementName'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
op|'('
name|'job'
op|','
name|'ret_val'
op|')'
op|'='
name|'vs_man_svc'
op|'.'
name|'DefineVirtualSystem'
op|'('
nl|'\n'
op|'['
op|']'
op|','
name|'None'
op|','
name|'vs_gs_data'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
op|')'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
name|'if'
name|'ret_val'
op|'=='
name|'WMI_JOB_STATUS_STARTED'
op|':'
newline|'\n'
indent|'            '
name|'success'
op|'='
name|'self'
op|'.'
name|'_check_job_status'
op|'('
name|'job'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'success'
op|'='
op|'('
name|'ret_val'
op|'=='
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'success'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Failed to create VM %s'"
op|')'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Created VM %s...'"
op|')'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ComputerSystem'
op|'('
name|'ElementName'
op|'='
name|'instance'
op|'.'
name|'name'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'vmsettings'
op|'='
name|'vm'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_VirtualSystemSettingData'"
op|')'
newline|'\n'
name|'vmsetting'
op|'='
op|'['
name|'s'
name|'for'
name|'s'
name|'in'
name|'vmsettings'
nl|'\n'
name|'if'
name|'s'
op|'.'
name|'SettingType'
op|'=='
number|'3'
op|']'
op|'['
number|'0'
op|']'
comment|'# avoid snapshots'
newline|'\n'
name|'memsetting'
op|'='
name|'vmsetting'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_MemorySettingData'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
comment|'#No Dynamic Memory, so reservation, limit and quantity are identical.'
nl|'\n'
name|'mem'
op|'='
name|'long'
op|'('
name|'str'
op|'('
name|'instance'
op|'['
string|"'memory_mb'"
op|']'
op|')'
op|')'
newline|'\n'
name|'memsetting'
op|'.'
name|'VirtualQuantity'
op|'='
name|'mem'
newline|'\n'
name|'memsetting'
op|'.'
name|'Reservation'
op|'='
name|'mem'
newline|'\n'
name|'memsetting'
op|'.'
name|'Limit'
op|'='
name|'mem'
newline|'\n'
nl|'\n'
op|'('
name|'job'
op|','
name|'ret_val'
op|')'
op|'='
name|'vs_man_svc'
op|'.'
name|'ModifyVirtualSystemResources'
op|'('
nl|'\n'
name|'vm'
op|'.'
name|'path_'
op|'('
op|')'
op|','
op|'['
name|'memsetting'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Set memory for vm %s...'"
op|')'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'procsetting'
op|'='
name|'vmsetting'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_ProcessorSettingData'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vcpus'
op|'='
name|'long'
op|'('
name|'instance'
op|'['
string|"'vcpus'"
op|']'
op|')'
newline|'\n'
name|'procsetting'
op|'.'
name|'VirtualQuantity'
op|'='
name|'vcpus'
newline|'\n'
name|'procsetting'
op|'.'
name|'Reservation'
op|'='
name|'vcpus'
newline|'\n'
name|'procsetting'
op|'.'
name|'Limit'
op|'='
name|'vcpus'
newline|'\n'
nl|'\n'
op|'('
name|'job'
op|','
name|'ret_val'
op|')'
op|'='
name|'vs_man_svc'
op|'.'
name|'ModifyVirtualSystemResources'
op|'('
nl|'\n'
name|'vm'
op|'.'
name|'path_'
op|'('
op|')'
op|','
op|'['
name|'procsetting'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Set vcpus for vm %s...'"
op|')'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_disk
dedent|''
name|'def'
name|'_create_disk'
op|'('
name|'self'
op|','
name|'vm_name'
op|','
name|'vhdfile'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a disk and attach it to the vm"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Creating disk for %(vm_name)s by attaching'"
nl|'\n'
string|"' disk file %(vhdfile)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
comment|'#Find the IDE controller for the vm.'
nl|'\n'
name|'vms'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'MSVM_ComputerSystem'
op|'('
name|'ElementName'
op|'='
name|'vm_name'
op|')'
newline|'\n'
name|'vm'
op|'='
name|'vms'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vmsettings'
op|'='
name|'vm'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_VirtualSystemSettingData'"
op|')'
newline|'\n'
name|'rasds'
op|'='
name|'vmsettings'
op|'['
number|'0'
op|']'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'MSVM_ResourceAllocationSettingData'"
op|')'
newline|'\n'
name|'ctrller'
op|'='
op|'['
name|'r'
name|'for'
name|'r'
name|'in'
name|'rasds'
nl|'\n'
name|'if'
name|'r'
op|'.'
name|'ResourceSubType'
op|'=='
string|"'Microsoft Emulated IDE Controller'"
name|'and'
name|'r'
op|'.'
name|'Address'
op|'=='
string|'"0"'
op|']'
newline|'\n'
comment|'#Find the default disk drive object for the vm and clone it.'
nl|'\n'
name|'diskdflt'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'query'
op|'('
nl|'\n'
string|'"SELECT * FROM Msvm_ResourceAllocationSettingData \\\n                WHERE ResourceSubType LIKE \'Microsoft Synthetic Disk Drive\'\\\n                AND InstanceID LIKE \'%Default%\'"'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'diskdrive'
op|'='
name|'self'
op|'.'
name|'_clone_wmi_obj'
op|'('
nl|'\n'
string|"'Msvm_ResourceAllocationSettingData'"
op|','
name|'diskdflt'
op|')'
newline|'\n'
comment|'#Set the IDE ctrller as parent.'
nl|'\n'
name|'diskdrive'
op|'.'
name|'Parent'
op|'='
name|'ctrller'
op|'['
number|'0'
op|']'
op|'.'
name|'path_'
op|'('
op|')'
newline|'\n'
name|'diskdrive'
op|'.'
name|'Address'
op|'='
number|'0'
newline|'\n'
comment|'#Add the cloned disk drive object to the vm.'
nl|'\n'
name|'new_resources'
op|'='
name|'self'
op|'.'
name|'_add_virt_resource'
op|'('
name|'diskdrive'
op|','
name|'vm'
op|')'
newline|'\n'
name|'if'
name|'new_resources'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Failed to add diskdrive to VM %s'"
op|')'
op|','
nl|'\n'
name|'vm_name'
op|')'
newline|'\n'
dedent|''
name|'diskdrive_path'
op|'='
name|'new_resources'
op|'['
number|'0'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'New disk drive path is %s'"
op|')'
op|','
name|'diskdrive_path'
op|')'
newline|'\n'
comment|'#Find the default VHD disk object.'
nl|'\n'
name|'vhddefault'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'query'
op|'('
nl|'\n'
string|'"SELECT * FROM Msvm_ResourceAllocationSettingData \\\n                 WHERE ResourceSubType LIKE \'Microsoft Virtual Hard Disk\' AND \\\n                 InstanceID LIKE \'%Default%\' "'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'#Clone the default and point it to the image file.'
nl|'\n'
name|'vhddisk'
op|'='
name|'self'
op|'.'
name|'_clone_wmi_obj'
op|'('
nl|'\n'
string|"'Msvm_ResourceAllocationSettingData'"
op|','
name|'vhddefault'
op|')'
newline|'\n'
comment|'#Set the new drive as the parent.'
nl|'\n'
name|'vhddisk'
op|'.'
name|'Parent'
op|'='
name|'diskdrive_path'
newline|'\n'
name|'vhddisk'
op|'.'
name|'Connection'
op|'='
op|'['
name|'vhdfile'
op|']'
newline|'\n'
nl|'\n'
comment|'#Add the new vhd object as a virtual hard disk to the vm.'
nl|'\n'
name|'new_resources'
op|'='
name|'self'
op|'.'
name|'_add_virt_resource'
op|'('
name|'vhddisk'
op|','
name|'vm'
op|')'
newline|'\n'
name|'if'
name|'new_resources'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Failed to add vhd file to VM %s'"
op|')'
op|','
nl|'\n'
name|'vm_name'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Created disk for %s'"
op|')'
op|','
name|'vm_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_nic
dedent|''
name|'def'
name|'_create_nic'
op|'('
name|'self'
op|','
name|'vm_name'
op|','
name|'mac'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a (emulated) nic and attach it to the vm"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Creating nic for %s '"
op|')'
op|','
name|'vm_name'
op|')'
newline|'\n'
comment|'#Find the vswitch that is connected to the physical nic.'
nl|'\n'
name|'vms'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ComputerSystem'
op|'('
name|'ElementName'
op|'='
name|'vm_name'
op|')'
newline|'\n'
name|'extswitch'
op|'='
name|'self'
op|'.'
name|'_find_external_network'
op|'('
op|')'
newline|'\n'
name|'vm'
op|'='
name|'vms'
op|'['
number|'0'
op|']'
newline|'\n'
name|'switch_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSwitchManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
comment|'#Find the default nic and clone it to create a new nic for the vm.'
nl|'\n'
comment|'#Use Msvm_SyntheticEthernetPortSettingData for Windows or Linux with'
nl|'\n'
comment|'#Linux Integration Components installed.'
nl|'\n'
name|'emulatednics_data'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_EmulatedEthernetPortSettingData'
op|'('
op|')'
newline|'\n'
name|'default_nic_data'
op|'='
op|'['
name|'n'
name|'for'
name|'n'
name|'in'
name|'emulatednics_data'
nl|'\n'
name|'if'
name|'n'
op|'.'
name|'InstanceID'
op|'.'
name|'rfind'
op|'('
string|"'Default'"
op|')'
op|'>'
number|'0'
op|']'
newline|'\n'
name|'new_nic_data'
op|'='
name|'self'
op|'.'
name|'_clone_wmi_obj'
op|'('
nl|'\n'
string|"'Msvm_EmulatedEthernetPortSettingData'"
op|','
nl|'\n'
name|'default_nic_data'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
comment|'#Create a port on the vswitch.'
nl|'\n'
op|'('
name|'new_port'
op|','
name|'ret_val'
op|')'
op|'='
name|'switch_svc'
op|'.'
name|'CreateSwitchPort'
op|'('
name|'vm_name'
op|','
name|'vm_name'
op|','
nl|'\n'
string|'""'
op|','
name|'extswitch'
op|'.'
name|'path_'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'ret_val'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Failed creating a port on the external vswitch'"
op|')'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Failed creating port for %s'"
op|')'
op|','
nl|'\n'
name|'vm_name'
op|')'
newline|'\n'
dedent|''
name|'ext_path'
op|'='
name|'extswitch'
op|'.'
name|'path_'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Created switch port %(vm_name)s on switch %(ext_path)s"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
comment|'#Connect the new nic to the new port.'
nl|'\n'
name|'new_nic_data'
op|'.'
name|'Connection'
op|'='
op|'['
name|'new_port'
op|']'
newline|'\n'
name|'new_nic_data'
op|'.'
name|'ElementName'
op|'='
name|'vm_name'
op|'+'
string|"' nic'"
newline|'\n'
name|'new_nic_data'
op|'.'
name|'Address'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
name|'mac'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
op|')'
newline|'\n'
name|'new_nic_data'
op|'.'
name|'StaticMacAddress'
op|'='
string|"'TRUE'"
newline|'\n'
comment|'#Add the new nic to the vm.'
nl|'\n'
name|'new_resources'
op|'='
name|'self'
op|'.'
name|'_add_virt_resource'
op|'('
name|'new_nic_data'
op|','
name|'vm'
op|')'
newline|'\n'
name|'if'
name|'new_resources'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Failed to add nic to VM %s'"
op|')'
op|','
nl|'\n'
name|'vm_name'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Created nic for %s "'
op|')'
op|','
name|'vm_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_add_virt_resource
dedent|''
name|'def'
name|'_add_virt_resource'
op|'('
name|'self'
op|','
name|'res_setting_data'
op|','
name|'target_vm'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add a new resource (disk/nic) to the VM"""'
newline|'\n'
name|'vs_man_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
op|'('
name|'job'
op|','
name|'new_resources'
op|','
name|'ret_val'
op|')'
op|'='
name|'vs_man_svc'
op|'.'
name|'AddVirtualSystemResources'
op|'('
op|'['
name|'res_setting_data'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
op|']'
op|','
nl|'\n'
name|'target_vm'
op|'.'
name|'path_'
op|'('
op|')'
op|')'
newline|'\n'
name|'success'
op|'='
name|'True'
newline|'\n'
name|'if'
name|'ret_val'
op|'=='
name|'WMI_JOB_STATUS_STARTED'
op|':'
newline|'\n'
indent|'            '
name|'success'
op|'='
name|'self'
op|'.'
name|'_check_job_status'
op|'('
name|'job'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'success'
op|'='
op|'('
name|'ret_val'
op|'=='
number|'0'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'success'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'new_resources'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
comment|'#TODO: use the reactor to poll instead of sleep'
nl|'\n'
DECL|member|_check_job_status
dedent|''
dedent|''
name|'def'
name|'_check_job_status'
op|'('
name|'self'
op|','
name|'jobpath'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Poll WMI job state for completion"""'
newline|'\n'
comment|'#Jobs have a path of the form:'
nl|'\n'
comment|'#\\\\WIN-P5IG7367DAG\\root\\virtualization:Msvm_ConcreteJob.InstanceID='
nl|'\n'
comment|'#"8A496B9C-AF4D-4E98-BD3C-1128CD85320D"'
nl|'\n'
name|'inst_id'
op|'='
name|'jobpath'
op|'.'
name|'split'
op|'('
string|"'='"
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
string|'\'"\''
op|')'
newline|'\n'
name|'jobs'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ConcreteJob'
op|'('
name|'InstanceID'
op|'='
name|'inst_id'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'jobs'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'job'
op|'='
name|'jobs'
op|'['
number|'0'
op|']'
newline|'\n'
name|'while'
name|'job'
op|'.'
name|'JobState'
op|'=='
name|'WMI_JOB_STATE_RUNNING'
op|':'
newline|'\n'
indent|'            '
name|'time'
op|'.'
name|'sleep'
op|'('
number|'0.1'
op|')'
newline|'\n'
name|'job'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ConcreteJob'
op|'('
name|'InstanceID'
op|'='
name|'inst_id'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'job'
op|'.'
name|'JobState'
op|'!='
name|'WMI_JOB_STATE_COMPLETED'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"WMI job failed: %s"'
op|')'
op|','
name|'job'
op|'.'
name|'ErrorSummaryDescription'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'desc'
op|'='
name|'job'
op|'.'
name|'Description'
newline|'\n'
name|'elap'
op|'='
name|'job'
op|'.'
name|'ElapsedTime'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"WMI job succeeded: %(desc)s, Elapsed=%(elap)s "'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_find_external_network
dedent|''
name|'def'
name|'_find_external_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find the vswitch that is connected to the physical nic.\n           Assumes only one physical nic on the host\n        """'
newline|'\n'
comment|'#If there are no physical nics connected to networks, return.'
nl|'\n'
name|'bound'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ExternalEthernetPort'
op|'('
name|'IsBound'
op|'='
string|"'TRUE'"
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'bound'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ExternalEthernetPort'
op|'('
name|'IsBound'
op|'='
string|"'TRUE'"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'associators'
op|'('
name|'wmi_result_class'
op|'='
string|"'Msvm_SwitchLANEndpoint'"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'associators'
op|'('
name|'wmi_result_class'
op|'='
string|"'Msvm_SwitchPort'"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'associators'
op|'('
name|'wmi_result_class'
op|'='
string|"'Msvm_VirtualSwitch'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_clone_wmi_obj
dedent|''
name|'def'
name|'_clone_wmi_obj'
op|'('
name|'self'
op|','
name|'wmi_class'
op|','
name|'wmi_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Clone a WMI object"""'
newline|'\n'
name|'cl'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'__getattr__'
op|'('
name|'wmi_class'
op|')'
comment|'# get the class'
newline|'\n'
name|'newinst'
op|'='
name|'cl'
op|'.'
name|'new'
op|'('
op|')'
newline|'\n'
comment|'#Copy the properties from the original.'
nl|'\n'
name|'for'
name|'prop'
name|'in'
name|'wmi_obj'
op|'.'
name|'_properties'
op|':'
newline|'\n'
indent|'            '
name|'newinst'
op|'.'
name|'Properties_'
op|'.'
name|'Item'
op|'('
name|'prop'
op|')'
op|'.'
name|'Value'
op|'='
name|'wmi_obj'
op|'.'
name|'Properties_'
op|'.'
name|'Item'
op|'('
name|'prop'
op|')'
op|'.'
name|'Value'
newline|'\n'
dedent|''
name|'return'
name|'newinst'
newline|'\n'
nl|'\n'
DECL|member|reboot
dedent|''
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboot the specified instance."""'
newline|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|"'instance not present %s'"
op|'%'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_set_vm_state'
op|'('
name|'instance'
op|'.'
name|'name'
op|','
string|"'Reboot'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy the VM. Also destroy the associated VHD disk files"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Got request to destroy vm %s"'
op|')'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'vm'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ComputerSystem'
op|'('
name|'ElementName'
op|'='
name|'instance'
op|'.'
name|'name'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vs_man_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
comment|'#Stop the VM first.'
nl|'\n'
name|'self'
op|'.'
name|'_set_vm_state'
op|'('
name|'instance'
op|'.'
name|'name'
op|','
string|"'Disabled'"
op|')'
newline|'\n'
name|'vmsettings'
op|'='
name|'vm'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_VirtualSystemSettingData'"
op|')'
newline|'\n'
name|'rasds'
op|'='
name|'vmsettings'
op|'['
number|'0'
op|']'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'MSVM_ResourceAllocationSettingData'"
op|')'
newline|'\n'
name|'disks'
op|'='
op|'['
name|'r'
name|'for'
name|'r'
name|'in'
name|'rasds'
name|'if'
name|'r'
op|'.'
name|'ResourceSubType'
op|'=='
string|"'Microsoft Virtual Hard Disk'"
op|']'
newline|'\n'
name|'diskfiles'
op|'='
op|'['
op|']'
newline|'\n'
comment|'#Collect disk file information before destroying the VM.'
nl|'\n'
name|'for'
name|'disk'
name|'in'
name|'disks'
op|':'
newline|'\n'
indent|'            '
name|'diskfiles'
op|'.'
name|'extend'
op|'('
op|'['
name|'c'
name|'for'
name|'c'
name|'in'
name|'disk'
op|'.'
name|'Connection'
op|']'
op|')'
newline|'\n'
comment|'#Nuke the VM. Does not destroy disks.'
nl|'\n'
dedent|''
op|'('
name|'job'
op|','
name|'ret_val'
op|')'
op|'='
name|'vs_man_svc'
op|'.'
name|'DestroyVirtualSystem'
op|'('
name|'vm'
op|'.'
name|'path_'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'ret_val'
op|'=='
name|'WMI_JOB_STATUS_STARTED'
op|':'
newline|'\n'
indent|'            '
name|'success'
op|'='
name|'self'
op|'.'
name|'_check_job_status'
op|'('
name|'job'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'ret_val'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'success'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'success'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Failed to destroy vm %s'"
op|')'
op|'%'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
comment|'#Delete associated vhd disk files.'
nl|'\n'
dedent|''
name|'for'
name|'disk'
name|'in'
name|'diskfiles'
op|':'
newline|'\n'
indent|'            '
name|'vhdfile'
op|'='
name|'self'
op|'.'
name|'_cim_conn'
op|'.'
name|'CIM_DataFile'
op|'('
name|'Name'
op|'='
name|'disk'
op|')'
newline|'\n'
name|'for'
name|'vf'
name|'in'
name|'vhdfile'
op|':'
newline|'\n'
indent|'                '
name|'vf'
op|'.'
name|'Delete'
op|'('
op|')'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Del: disk %(vhdfile)s vm %(instance_name)s"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get information about the VM"""'
newline|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|"'instance not present %s'"
op|'%'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'vm'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ComputerSystem'
op|'('
name|'ElementName'
op|'='
name|'instance_id'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vs_man_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vmsettings'
op|'='
name|'vm'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_VirtualSystemSettingData'"
op|')'
newline|'\n'
name|'settings_paths'
op|'='
op|'['
name|'v'
op|'.'
name|'path_'
op|'('
op|')'
name|'for'
name|'v'
name|'in'
name|'vmsettings'
op|']'
newline|'\n'
comment|'#See http://msdn.microsoft.com/en-us/library/cc160706%28VS.85%29.aspx'
nl|'\n'
name|'summary_info'
op|'='
name|'vs_man_svc'
op|'.'
name|'GetSummaryInformation'
op|'('
nl|'\n'
op|'['
number|'4'
op|','
number|'100'
op|','
number|'103'
op|','
number|'105'
op|']'
op|','
name|'settings_paths'
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'info'
op|'='
name|'summary_info'
op|'['
number|'0'
op|']'
newline|'\n'
name|'state'
op|'='
name|'str'
op|'('
name|'HYPERV_POWER_STATE'
op|'['
name|'info'
op|'.'
name|'EnabledState'
op|']'
op|')'
newline|'\n'
name|'memusage'
op|'='
name|'str'
op|'('
name|'info'
op|'.'
name|'MemoryUsage'
op|')'
newline|'\n'
name|'numprocs'
op|'='
name|'str'
op|'('
name|'info'
op|'.'
name|'NumberOfProcessors'
op|')'
newline|'\n'
name|'uptime'
op|'='
name|'str'
op|'('
name|'info'
op|'.'
name|'UpTime'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Got Info for vm %(instance_id)s: state=%(state)s,"'
nl|'\n'
string|'" mem=%(memusage)s, num_cpu=%(numprocs)s,"'
nl|'\n'
string|'" cpu_time=%(uptime)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'state'"
op|':'
name|'HYPERV_POWER_STATE'
op|'['
name|'info'
op|'.'
name|'EnabledState'
op|']'
op|','
nl|'\n'
string|"'max_mem'"
op|':'
name|'info'
op|'.'
name|'MemoryUsage'
op|','
nl|'\n'
string|"'mem'"
op|':'
name|'info'
op|'.'
name|'MemoryUsage'
op|','
nl|'\n'
string|"'num_cpu'"
op|':'
name|'info'
op|'.'
name|'NumberOfProcessors'
op|','
nl|'\n'
string|"'cpu_time'"
op|':'
name|'info'
op|'.'
name|'UpTime'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_lookup
dedent|''
name|'def'
name|'_lookup'
op|'('
name|'self'
op|','
name|'i'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vms'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ComputerSystem'
op|'('
name|'ElementName'
op|'='
name|'i'
op|')'
newline|'\n'
name|'n'
op|'='
name|'len'
op|'('
name|'vms'
op|')'
newline|'\n'
name|'if'
name|'n'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'elif'
name|'n'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'duplicate name found: %s'"
op|')'
op|'%'
name|'i'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'vms'
op|'['
number|'0'
op|']'
op|'.'
name|'ElementName'
newline|'\n'
nl|'\n'
DECL|member|_set_vm_state
dedent|''
dedent|''
name|'def'
name|'_set_vm_state'
op|'('
name|'self'
op|','
name|'vm_name'
op|','
name|'req_state'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Set the desired state of the VM"""'
newline|'\n'
name|'vms'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ComputerSystem'
op|'('
name|'ElementName'
op|'='
name|'vm_name'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'vms'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
op|'('
name|'job'
op|','
name|'ret_val'
op|')'
op|'='
name|'vms'
op|'['
number|'0'
op|']'
op|'.'
name|'RequestStateChange'
op|'('
name|'REQ_POWER_STATE'
op|'['
name|'req_state'
op|']'
op|')'
newline|'\n'
name|'success'
op|'='
name|'False'
newline|'\n'
name|'if'
name|'ret_val'
op|'=='
name|'WMI_JOB_STATUS_STARTED'
op|':'
newline|'\n'
indent|'            '
name|'success'
op|'='
name|'self'
op|'.'
name|'_check_job_status'
op|'('
name|'job'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'ret_val'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'success'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'elif'
name|'ret_val'
op|'=='
number|'32775'
op|':'
newline|'\n'
comment|'#Invalid state for current operation. Typically means it is'
nl|'\n'
comment|'#already in the state requested'
nl|'\n'
indent|'            '
name|'success'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'success'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Successfully changed vm state of %(vm_name)s"'
nl|'\n'
string|'" to %(req_state)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Failed to change vm state of %(vm_name)s"'
nl|'\n'
string|'" to %(req_state)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'device_path'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm'
op|'='
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|"'Cannot attach volume to missing %s vm'"
nl|'\n'
op|'%'
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_volume
dedent|''
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm'
op|'='
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|"'Cannot detach volume from missing %s '"
nl|'\n'
op|'%'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
