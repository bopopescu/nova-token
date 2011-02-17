begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\r\n'
nl|'\r\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\r\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\r\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\r\n'
comment|'#    a copy of the License at'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\r\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\r\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\r\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\r\n'
comment|'#    under the License.'
nl|'\r\n'
nl|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'VimService_services_types'
name|'import'
name|'ns0'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|build_datastore_path
name|'def'
name|'build_datastore_path'
op|'('
name|'datastore_name'
op|','
name|'path'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Build the datastore compliant path\r\n    """'
newline|'\r\n'
name|'return'
string|'"[%s] %s"'
op|'%'
op|'('
name|'datastore_name'
op|','
name|'path'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|split_datastore_path
dedent|''
name|'def'
name|'split_datastore_path'
op|'('
name|'datastore_path'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Split the VMWare style datastore path to get the Datastore name and the\r\n    entity path\r\n    """'
newline|'\r\n'
name|'spl'
op|'='
name|'datastore_path'
op|'.'
name|'split'
op|'('
string|"'['"
op|','
number|'1'
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'split'
op|'('
string|"']'"
op|','
number|'1'
op|')'
newline|'\r\n'
name|'path'
op|'='
string|'""'
newline|'\r\n'
name|'if'
name|'len'
op|'('
name|'spl'
op|')'
op|'=='
number|'1'
op|':'
newline|'\r\n'
indent|'        '
name|'datastore_url'
op|'='
name|'spl'
op|'['
number|'0'
op|']'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'        '
name|'datastore_url'
op|','
name|'path'
op|'='
name|'spl'
newline|'\r\n'
dedent|''
name|'return'
name|'datastore_url'
op|','
name|'path'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_vm_create_spec
dedent|''
name|'def'
name|'get_vm_create_spec'
op|'('
name|'instance'
op|','
name|'data_store_name'
op|','
name|'network_name'
op|'='
string|'"vmnet0"'
op|','
nl|'\r\n'
name|'os_type'
op|'='
string|'"otherGuest"'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Builds the VM Create spec\r\n    """'
newline|'\r\n'
name|'config_spec'
op|'='
name|'ns0'
op|'.'
name|'VirtualMachineConfigSpec_Def'
op|'('
nl|'\r\n'
string|'"VirtualMachineConfigSpec"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
name|'config_spec'
op|'.'
name|'_name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'_guestId'
op|'='
name|'os_type'
newline|'\r\n'
nl|'\r\n'
name|'vm_file_info'
op|'='
name|'ns0'
op|'.'
name|'VirtualMachineFileInfo_Def'
op|'('
nl|'\r\n'
string|'"VirtualMachineFileInfo"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'vm_file_info'
op|'.'
name|'_vmPathName'
op|'='
string|'"["'
op|'+'
name|'data_store_name'
op|'+'
string|'"]"'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'_files'
op|'='
name|'vm_file_info'
newline|'\r\n'
nl|'\r\n'
name|'tools_info'
op|'='
name|'ns0'
op|'.'
name|'ToolsConfigInfo_Def'
op|'('
string|'"ToolsConfigInfo"'
op|')'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'_afterPowerOn'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'_afterResume'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'_beforeGuestStandby'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'_bbeforeGuestShutdown'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'_beforeGuestReboot'
op|'='
name|'True'
newline|'\r\n'
nl|'\r\n'
name|'config_spec'
op|'.'
name|'_tools'
op|'='
name|'tools_info'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'_numCPUs'
op|'='
name|'int'
op|'('
name|'instance'
op|'.'
name|'vcpus'
op|')'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'_memoryMB'
op|'='
name|'int'
op|'('
name|'instance'
op|'.'
name|'memory_mb'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'nic_spec'
op|'='
name|'create_network_spec'
op|'('
name|'network_name'
op|','
name|'instance'
op|'.'
name|'mac_address'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'device_config_spec'
op|'='
op|'['
name|'nic_spec'
op|']'
newline|'\r\n'
nl|'\r\n'
name|'config_spec'
op|'.'
name|'_deviceChange'
op|'='
name|'device_config_spec'
newline|'\r\n'
name|'return'
name|'config_spec'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|create_controller_spec
dedent|''
name|'def'
name|'create_controller_spec'
op|'('
name|'key'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Builds a Config Spec for the LSI Logic Controller\'s addition which acts\r\n    as the controller for the Virtual Hard disk to be attached to the VM\r\n    """'
newline|'\r\n'
comment|'#Create a controller for the Virtual Hard Disk'
nl|'\r\n'
name|'virtual_device_config'
op|'='
name|'ns0'
op|'.'
name|'VirtualDeviceConfigSpec_Def'
op|'('
string|'"VirtualDeviceConfigSpec"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'virtual_device_config'
op|'.'
name|'_operation'
op|'='
string|'"add"'
newline|'\r\n'
name|'virtual_lsi'
op|'='
name|'ns0'
op|'.'
name|'VirtualLsiLogicController_Def'
op|'('
nl|'\r\n'
string|'"VirtualLsiLogicController"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'virtual_lsi'
op|'.'
name|'_key'
op|'='
name|'key'
newline|'\r\n'
name|'virtual_lsi'
op|'.'
name|'_busNumber'
op|'='
number|'0'
newline|'\r\n'
name|'virtual_lsi'
op|'.'
name|'_sharedBus'
op|'='
string|'"noSharing"'
newline|'\r\n'
name|'virtual_device_config'
op|'.'
name|'_device'
op|'='
name|'virtual_lsi'
newline|'\r\n'
nl|'\r\n'
name|'return'
name|'virtual_device_config'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|create_network_spec
dedent|''
name|'def'
name|'create_network_spec'
op|'('
name|'network_name'
op|','
name|'mac_address'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Builds a config spec for the addition of a new network adapter to the VM\r\n    """'
newline|'\r\n'
name|'network_spec'
op|'='
name|'ns0'
op|'.'
name|'VirtualDeviceConfigSpec_Def'
op|'('
string|'"VirtualDeviceConfigSpec"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'network_spec'
op|'.'
name|'_operation'
op|'='
string|'"add"'
newline|'\r\n'
nl|'\r\n'
comment|'#Get the recommended card type for the VM based on the guest OS of the VM'
nl|'\r\n'
name|'net_device'
op|'='
name|'ns0'
op|'.'
name|'VirtualPCNet32_Def'
op|'('
string|'"VirtualPCNet32"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
name|'backing'
op|'='
name|'ns0'
op|'.'
name|'VirtualEthernetCardNetworkBackingInfo_Def'
op|'('
nl|'\r\n'
string|'"VirtualEthernetCardNetworkBackingInfo"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'backing'
op|'.'
name|'_deviceName'
op|'='
name|'network_name'
newline|'\r\n'
nl|'\r\n'
name|'connectable_spec'
op|'='
name|'ns0'
op|'.'
name|'VirtualDeviceConnectInfo_Def'
op|'('
string|'"VirtualDeviceConnectInfo"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'connectable_spec'
op|'.'
name|'_startConnected'
op|'='
name|'True'
newline|'\r\n'
name|'connectable_spec'
op|'.'
name|'_allowGuestControl'
op|'='
name|'True'
newline|'\r\n'
name|'connectable_spec'
op|'.'
name|'_connected'
op|'='
name|'True'
newline|'\r\n'
nl|'\r\n'
name|'net_device'
op|'.'
name|'_connectable'
op|'='
name|'connectable_spec'
newline|'\r\n'
name|'net_device'
op|'.'
name|'_backing'
op|'='
name|'backing'
newline|'\r\n'
nl|'\r\n'
comment|'#The Server assigns a Key to the device. Here we pass a -ve temporary key.'
nl|'\r\n'
comment|"#-ve because actual keys are +ve numbers and we don't"
nl|'\r\n'
comment|'#want a clash with the key that server might associate with the device'
nl|'\r\n'
name|'net_device'
op|'.'
name|'_key'
op|'='
op|'-'
number|'47'
newline|'\r\n'
name|'net_device'
op|'.'
name|'_addressType'
op|'='
string|'"manual"'
newline|'\r\n'
name|'net_device'
op|'.'
name|'_macAddress'
op|'='
name|'mac_address'
newline|'\r\n'
name|'net_device'
op|'.'
name|'_wakeOnLanEnabled'
op|'='
name|'True'
newline|'\r\n'
nl|'\r\n'
name|'network_spec'
op|'.'
name|'_device'
op|'='
name|'net_device'
newline|'\r\n'
name|'return'
name|'network_spec'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_datastore_search_sepc
dedent|''
name|'def'
name|'get_datastore_search_sepc'
op|'('
name|'pattern'
op|'='
name|'None'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Builds the datastore search spec.\r\n    """'
newline|'\r\n'
name|'host_datastore_browser_search_spec'
op|'='
name|'ns0'
op|'.'
name|'HostDatastoreBrowserSearchSpec_Def'
op|'('
nl|'\r\n'
string|'"HostDatastoreBrowserSearchSpec"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'file_query_flags'
op|'='
name|'ns0'
op|'.'
name|'FileQueryFlags_Def'
op|'('
string|'"FileQueryFlags"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'file_query_flags'
op|'.'
name|'_modification'
op|'='
name|'False'
newline|'\r\n'
name|'file_query_flags'
op|'.'
name|'_fileSize'
op|'='
name|'True'
newline|'\r\n'
name|'file_query_flags'
op|'.'
name|'_fileType'
op|'='
name|'True'
newline|'\r\n'
name|'file_query_flags'
op|'.'
name|'_fileOwner'
op|'='
name|'True'
newline|'\r\n'
name|'host_datastore_browser_search_spec'
op|'.'
name|'_details'
op|'='
name|'file_query_flags'
newline|'\r\n'
name|'if'
name|'pattern'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\r\n'
indent|'        '
name|'host_datastore_browser_search_spec'
op|'.'
name|'_matchPattern'
op|'='
name|'pattern'
newline|'\r\n'
dedent|''
name|'return'
name|'host_datastore_browser_search_spec'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_vmdk_attach_config_sepc
dedent|''
name|'def'
name|'get_vmdk_attach_config_sepc'
op|'('
name|'disksize'
op|','
name|'file_path'
op|','
name|'adapter_type'
op|'='
string|'"lsiLogic"'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Builds the vmdk attach config spec.\r\n    """'
newline|'\r\n'
name|'config_spec'
op|'='
name|'ns0'
op|'.'
name|'VirtualMachineConfigSpec_Def'
op|'('
nl|'\r\n'
string|'"VirtualMachineConfigSpec"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
comment|'#The controller Key pertains to the Key of the LSI Logic Controller, which'
nl|'\r\n'
comment|'#controls this Hard Disk'
nl|'\r\n'
name|'device_config_spec'
op|'='
op|'['
op|']'
newline|'\r\n'
comment|'#For IDE devices, there are these two default controllers created in the'
nl|'\r\n'
comment|'#VM having keys 200 and 201'
nl|'\r\n'
name|'if'
name|'adapter_type'
op|'=='
string|'"ide"'
op|':'
newline|'\r\n'
indent|'        '
name|'controller_key'
op|'='
number|'200'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'        '
name|'controller_key'
op|'='
op|'-'
number|'101'
newline|'\r\n'
name|'controller_spec'
op|'='
name|'create_controller_spec'
op|'('
name|'controller_key'
op|')'
newline|'\r\n'
name|'device_config_spec'
op|'.'
name|'append'
op|'('
name|'controller_spec'
op|')'
newline|'\r\n'
dedent|''
name|'virtual_device_config_spec'
op|'='
name|'create_virtual_disk_spec'
op|'('
name|'disksize'
op|','
nl|'\r\n'
name|'controller_key'
op|','
name|'file_path'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'device_config_spec'
op|'.'
name|'append'
op|'('
name|'virtual_device_config_spec'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'config_spec'
op|'.'
name|'_deviceChange'
op|'='
name|'device_config_spec'
newline|'\r\n'
name|'return'
name|'config_spec'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_vmdk_file_path_and_adapter_type
dedent|''
name|'def'
name|'get_vmdk_file_path_and_adapter_type'
op|'('
name|'hardware_devices'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Gets the vmdk file path and the storage adapter type\r\n    """'
newline|'\r\n'
name|'if'
name|'isinstance'
op|'('
name|'hardware_devices'
op|'.'
name|'typecode'
op|','
name|'ns0'
op|'.'
name|'ArrayOfVirtualDevice_Def'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'hardware_devices'
op|'='
name|'hardware_devices'
op|'.'
name|'VirtualDevice'
newline|'\r\n'
dedent|''
name|'vmdk_file_path'
op|'='
name|'None'
newline|'\r\n'
name|'vmdk_controler_key'
op|'='
name|'None'
newline|'\r\n'
nl|'\r\n'
name|'adapter_type_dict'
op|'='
op|'{'
op|'}'
newline|'\r\n'
name|'for'
name|'device'
name|'in'
name|'hardware_devices'
op|':'
newline|'\r\n'
indent|'        '
name|'if'
op|'('
name|'isinstance'
op|'('
name|'device'
op|'.'
name|'typecode'
op|','
name|'ns0'
op|'.'
name|'VirtualDisk_Def'
op|')'
name|'and'
nl|'\r\n'
name|'isinstance'
op|'('
name|'device'
op|'.'
name|'Backing'
op|'.'
name|'typecode'
op|','
nl|'\r\n'
name|'ns0'
op|'.'
name|'VirtualDiskFlatVer2BackingInfo_Def'
op|')'
op|')'
op|':'
newline|'\r\n'
indent|'            '
name|'vmdk_file_path'
op|'='
name|'device'
op|'.'
name|'Backing'
op|'.'
name|'FileName'
newline|'\r\n'
name|'vmdk_controler_key'
op|'='
name|'device'
op|'.'
name|'ControllerKey'
newline|'\r\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'device'
op|'.'
name|'typecode'
op|','
name|'ns0'
op|'.'
name|'VirtualLsiLogicController_Def'
op|')'
op|':'
newline|'\r\n'
indent|'            '
name|'adapter_type_dict'
op|'['
name|'device'
op|'.'
name|'Key'
op|']'
op|'='
string|'"lsiLogic"'
newline|'\r\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'device'
op|'.'
name|'typecode'
op|','
name|'ns0'
op|'.'
name|'VirtualBusLogicController_Def'
op|')'
op|':'
newline|'\r\n'
indent|'            '
name|'adapter_type_dict'
op|'['
name|'device'
op|'.'
name|'Key'
op|']'
op|'='
string|'"busLogic"'
newline|'\r\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'device'
op|'.'
name|'typecode'
op|','
name|'ns0'
op|'.'
name|'VirtualIDEController_Def'
op|')'
op|':'
newline|'\r\n'
indent|'            '
name|'adapter_type_dict'
op|'['
name|'device'
op|'.'
name|'Key'
op|']'
op|'='
string|'"ide"'
newline|'\r\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'device'
op|'.'
name|'typecode'
op|','
name|'ns0'
op|'.'
name|'VirtualLsiLogicSASController_Def'
op|')'
op|':'
newline|'\r\n'
indent|'            '
name|'adapter_type_dict'
op|'['
name|'device'
op|'.'
name|'Key'
op|']'
op|'='
string|'"lsiLogic"'
newline|'\r\n'
nl|'\r\n'
dedent|''
dedent|''
name|'adapter_type'
op|'='
name|'adapter_type_dict'
op|'.'
name|'get'
op|'('
name|'vmdk_controler_key'
op|','
string|'""'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'return'
name|'vmdk_file_path'
op|','
name|'adapter_type'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_copy_virtual_disk_spec
dedent|''
name|'def'
name|'get_copy_virtual_disk_spec'
op|'('
name|'adapter_type'
op|'='
string|'"lsilogic"'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Builds the Virtual Disk copy spec.\r\n    """'
newline|'\r\n'
name|'dest_spec'
op|'='
name|'ns0'
op|'.'
name|'VirtualDiskSpec_Def'
op|'('
string|'"VirtualDiskSpec"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'dest_spec'
op|'.'
name|'AdapterType'
op|'='
name|'adapter_type'
newline|'\r\n'
name|'dest_spec'
op|'.'
name|'DiskType'
op|'='
string|'"thick"'
newline|'\r\n'
name|'return'
name|'dest_spec'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_vmdk_create_spec
dedent|''
name|'def'
name|'get_vmdk_create_spec'
op|'('
name|'size_in_kb'
op|','
name|'adapter_type'
op|'='
string|'"lsiLogic"'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Builds the virtual disk create sepc.\r\n    """'
newline|'\r\n'
name|'create_vmdk_spec'
op|'='
name|'ns0'
op|'.'
name|'FileBackedVirtualDiskSpec_Def'
op|'('
string|'"VirtualDiskSpec"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'create_vmdk_spec'
op|'.'
name|'_adapterType'
op|'='
name|'adapter_type'
newline|'\r\n'
name|'create_vmdk_spec'
op|'.'
name|'_diskType'
op|'='
string|'"thick"'
newline|'\r\n'
name|'create_vmdk_spec'
op|'.'
name|'_capacityKb'
op|'='
name|'size_in_kb'
newline|'\r\n'
name|'return'
name|'create_vmdk_spec'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|create_virtual_disk_spec
dedent|''
name|'def'
name|'create_virtual_disk_spec'
op|'('
name|'disksize'
op|','
name|'controller_key'
op|','
name|'file_path'
op|'='
name|'None'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Creates a Spec for the addition/attaching of a Virtual Disk to the VM\r\n    """'
newline|'\r\n'
name|'virtual_device_config'
op|'='
name|'ns0'
op|'.'
name|'VirtualDeviceConfigSpec_Def'
op|'('
string|'"VirtualDeviceConfigSpec"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'virtual_device_config'
op|'.'
name|'_operation'
op|'='
string|'"add"'
newline|'\r\n'
name|'if'
name|'file_path'
name|'is'
name|'None'
op|':'
newline|'\r\n'
indent|'        '
name|'virtual_device_config'
op|'.'
name|'_fileOperation'
op|'='
string|'"create"'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'virtual_disk'
op|'='
name|'ns0'
op|'.'
name|'VirtualDisk_Def'
op|'('
string|'"VirtualDisk"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
name|'disk_file_backing'
op|'='
name|'ns0'
op|'.'
name|'VirtualDiskFlatVer2BackingInfo_Def'
op|'('
nl|'\r\n'
string|'"VirtualDiskFlatVer2BackingInfo"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'disk_file_backing'
op|'.'
name|'_diskMode'
op|'='
string|'"persistent"'
newline|'\r\n'
name|'disk_file_backing'
op|'.'
name|'_thinProvisioned'
op|'='
name|'False'
newline|'\r\n'
name|'if'
name|'file_path'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\r\n'
indent|'        '
name|'disk_file_backing'
op|'.'
name|'_fileName'
op|'='
name|'file_path'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'        '
name|'disk_file_backing'
op|'.'
name|'_fileName'
op|'='
string|'""'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'connectable_spec'
op|'='
name|'ns0'
op|'.'
name|'VirtualDeviceConnectInfo_Def'
op|'('
nl|'\r\n'
string|'"VirtualDeviceConnectInfo"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'connectable_spec'
op|'.'
name|'_startConnected'
op|'='
name|'True'
newline|'\r\n'
name|'connectable_spec'
op|'.'
name|'_allowGuestControl'
op|'='
name|'False'
newline|'\r\n'
name|'connectable_spec'
op|'.'
name|'_connected'
op|'='
name|'True'
newline|'\r\n'
nl|'\r\n'
name|'virtual_disk'
op|'.'
name|'_backing'
op|'='
name|'disk_file_backing'
newline|'\r\n'
name|'virtual_disk'
op|'.'
name|'_connectable'
op|'='
name|'connectable_spec'
newline|'\r\n'
nl|'\r\n'
comment|'#The Server assigns a Key to the device. Here we pass a -ve temporary key.'
nl|'\r\n'
comment|"#-ve because actual keys are +ve numbers and we don't"
nl|'\r\n'
comment|'#want a clash with the key that server might associate with the device'
nl|'\r\n'
name|'virtual_disk'
op|'.'
name|'_key'
op|'='
op|'-'
number|'100'
newline|'\r\n'
name|'virtual_disk'
op|'.'
name|'_controllerKey'
op|'='
name|'controller_key'
newline|'\r\n'
name|'virtual_disk'
op|'.'
name|'_unitNumber'
op|'='
number|'0'
newline|'\r\n'
name|'virtual_disk'
op|'.'
name|'_capacityInKB'
op|'='
name|'disksize'
newline|'\r\n'
nl|'\r\n'
name|'virtual_device_config'
op|'.'
name|'_device'
op|'='
name|'virtual_disk'
newline|'\r\n'
nl|'\r\n'
name|'return'
name|'virtual_device_config'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_dummy_vm_create_spec
dedent|''
name|'def'
name|'get_dummy_vm_create_spec'
op|'('
name|'name'
op|','
name|'data_store_name'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Builds the dummy VM create spec\r\n    """'
newline|'\r\n'
name|'config_spec'
op|'='
name|'ns0'
op|'.'
name|'VirtualMachineConfigSpec_Def'
op|'('
nl|'\r\n'
string|'"VirtualMachineConfigSpec"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
name|'config_spec'
op|'.'
name|'_name'
op|'='
name|'name'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'_guestId'
op|'='
string|'"otherGuest"'
newline|'\r\n'
nl|'\r\n'
name|'vm_file_info'
op|'='
name|'ns0'
op|'.'
name|'VirtualMachineFileInfo_Def'
op|'('
nl|'\r\n'
string|'"VirtualMachineFileInfo"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'vm_file_info'
op|'.'
name|'_vmPathName'
op|'='
string|'"["'
op|'+'
name|'data_store_name'
op|'+'
string|'"]"'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'_files'
op|'='
name|'vm_file_info'
newline|'\r\n'
nl|'\r\n'
name|'tools_info'
op|'='
name|'ns0'
op|'.'
name|'ToolsConfigInfo_Def'
op|'('
string|'"ToolsConfigInfo"'
op|')'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'_afterPowerOn'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'_afterResume'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'_beforeGuestStandby'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'_bbeforeGuestShutdown'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'_beforeGuestReboot'
op|'='
name|'True'
newline|'\r\n'
nl|'\r\n'
name|'config_spec'
op|'.'
name|'_tools'
op|'='
name|'tools_info'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'_numCPUs'
op|'='
number|'1'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'_memoryMB'
op|'='
number|'4'
newline|'\r\n'
nl|'\r\n'
name|'controller_key'
op|'='
op|'-'
number|'101'
newline|'\r\n'
name|'controller_spec'
op|'='
name|'create_controller_spec'
op|'('
name|'controller_key'
op|')'
newline|'\r\n'
name|'disk_spec'
op|'='
name|'create_virtual_disk_spec'
op|'('
number|'1024'
op|','
name|'controller_key'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'device_config_spec'
op|'='
op|'['
name|'controller_spec'
op|','
name|'disk_spec'
op|']'
newline|'\r\n'
nl|'\r\n'
name|'config_spec'
op|'.'
name|'_deviceChange'
op|'='
name|'device_config_spec'
newline|'\r\n'
name|'return'
name|'config_spec'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_machine_id_change_spec
dedent|''
name|'def'
name|'get_machine_id_change_spec'
op|'('
name|'mac'
op|','
name|'ip_addr'
op|','
name|'netmask'
op|','
name|'gateway'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Builds the machine id change config spec\r\n    """'
newline|'\r\n'
name|'machine_id_str'
op|'='
string|'"%s;%s;%s;%s"'
op|'%'
op|'('
name|'mac'
op|','
name|'ip_addr'
op|','
name|'netmask'
op|','
name|'gateway'
op|')'
newline|'\r\n'
name|'virtual_machine_config_spec'
op|'='
name|'ns0'
op|'.'
name|'VirtualMachineConfigSpec_Def'
op|'('
nl|'\r\n'
string|'"VirtualMachineConfigSpec"'
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'opt'
op|'='
name|'ns0'
op|'.'
name|'OptionValue_Def'
op|'('
string|"'OptionValue'"
op|')'
op|'.'
name|'pyclass'
op|'('
op|')'
newline|'\r\n'
name|'opt'
op|'.'
name|'_key'
op|'='
string|'"machine.id"'
newline|'\r\n'
name|'opt'
op|'.'
name|'_value'
op|'='
name|'machine_id_str'
newline|'\r\n'
name|'virtual_machine_config_spec'
op|'.'
name|'_extraConfig'
op|'='
op|'['
name|'opt'
op|']'
newline|'\r\n'
name|'return'
name|'virtual_machine_config_spec'
newline|'\r\n'
dedent|''
endmarker|''
end_unit
