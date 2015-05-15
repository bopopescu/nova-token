begin_unit
comment|'# Copyright (c) 2014 VMware, Inc.'
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
string|'"""\nShared constants across the VMware driver\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
name|'as'
name|'network_model'
newline|'\n'
nl|'\n'
DECL|variable|DISK_FORMAT_ISO
name|'DISK_FORMAT_ISO'
op|'='
string|"'iso'"
newline|'\n'
DECL|variable|DISK_FORMAT_VMDK
name|'DISK_FORMAT_VMDK'
op|'='
string|"'vmdk'"
newline|'\n'
DECL|variable|DISK_FORMATS_ALL
name|'DISK_FORMATS_ALL'
op|'='
op|'['
name|'DISK_FORMAT_ISO'
op|','
name|'DISK_FORMAT_VMDK'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|DISK_TYPE_THIN
name|'DISK_TYPE_THIN'
op|'='
string|"'thin'"
newline|'\n'
DECL|variable|CONTAINER_FORMAT_BARE
name|'CONTAINER_FORMAT_BARE'
op|'='
string|"'bare'"
newline|'\n'
DECL|variable|CONTAINER_FORMAT_OVA
name|'CONTAINER_FORMAT_OVA'
op|'='
string|"'ova'"
newline|'\n'
DECL|variable|CONTAINER_FORMATS_ALL
name|'CONTAINER_FORMATS_ALL'
op|'='
op|'['
name|'CONTAINER_FORMAT_BARE'
op|','
name|'DISK_FORMAT_VMDK'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|DISK_TYPE_SPARSE
name|'DISK_TYPE_SPARSE'
op|'='
string|"'sparse'"
newline|'\n'
DECL|variable|DISK_TYPE_PREALLOCATED
name|'DISK_TYPE_PREALLOCATED'
op|'='
string|"'preallocated'"
newline|'\n'
DECL|variable|DISK_TYPE_STREAM_OPTIMIZED
name|'DISK_TYPE_STREAM_OPTIMIZED'
op|'='
string|"'streamOptimized'"
newline|'\n'
DECL|variable|DISK_TYPE_EAGER_ZEROED_THICK
name|'DISK_TYPE_EAGER_ZEROED_THICK'
op|'='
string|"'eagerZeroedThick'"
newline|'\n'
nl|'\n'
DECL|variable|DATASTORE_TYPE_VMFS
name|'DATASTORE_TYPE_VMFS'
op|'='
string|"'VMFS'"
newline|'\n'
DECL|variable|DATASTORE_TYPE_NFS
name|'DATASTORE_TYPE_NFS'
op|'='
string|"'NFS'"
newline|'\n'
DECL|variable|DATASTORE_TYPE_NFS41
name|'DATASTORE_TYPE_NFS41'
op|'='
string|"'NFS41'"
newline|'\n'
DECL|variable|DATASTORE_TYPE_VSAN
name|'DATASTORE_TYPE_VSAN'
op|'='
string|"'vsan'"
newline|'\n'
nl|'\n'
DECL|variable|DEFAULT_VIF_MODEL
name|'DEFAULT_VIF_MODEL'
op|'='
name|'network_model'
op|'.'
name|'VIF_MODEL_E1000'
newline|'\n'
DECL|variable|DEFAULT_OS_TYPE
name|'DEFAULT_OS_TYPE'
op|'='
string|'"otherGuest"'
newline|'\n'
DECL|variable|DEFAULT_ADAPTER_TYPE
name|'DEFAULT_ADAPTER_TYPE'
op|'='
string|'"lsiLogic"'
newline|'\n'
DECL|variable|DEFAULT_DISK_TYPE
name|'DEFAULT_DISK_TYPE'
op|'='
name|'DISK_TYPE_PREALLOCATED'
newline|'\n'
DECL|variable|DEFAULT_DISK_FORMAT
name|'DEFAULT_DISK_FORMAT'
op|'='
name|'DISK_FORMAT_VMDK'
newline|'\n'
DECL|variable|DEFAULT_CONTAINER_FORMAT
name|'DEFAULT_CONTAINER_FORMAT'
op|'='
name|'CONTAINER_FORMAT_BARE'
newline|'\n'
nl|'\n'
DECL|variable|IMAGE_VM_PREFIX
name|'IMAGE_VM_PREFIX'
op|'='
string|'"OSTACK_IMG"'
newline|'\n'
DECL|variable|SNAPSHOT_VM_PREFIX
name|'SNAPSHOT_VM_PREFIX'
op|'='
string|'"OSTACK_SNAP"'
newline|'\n'
nl|'\n'
DECL|variable|ADAPTER_TYPE_BUSLOGIC
name|'ADAPTER_TYPE_BUSLOGIC'
op|'='
string|'"busLogic"'
newline|'\n'
DECL|variable|ADAPTER_TYPE_IDE
name|'ADAPTER_TYPE_IDE'
op|'='
string|'"ide"'
newline|'\n'
DECL|variable|ADAPTER_TYPE_LSILOGICSAS
name|'ADAPTER_TYPE_LSILOGICSAS'
op|'='
string|'"lsiLogicsas"'
newline|'\n'
DECL|variable|ADAPTER_TYPE_PARAVIRTUAL
name|'ADAPTER_TYPE_PARAVIRTUAL'
op|'='
string|'"paraVirtual"'
newline|'\n'
nl|'\n'
DECL|variable|SUPPORTED_FLAT_VARIANTS
name|'SUPPORTED_FLAT_VARIANTS'
op|'='
op|'['
string|'"thin"'
op|','
string|'"preallocated"'
op|','
string|'"thick"'
op|','
string|'"eagerZeroedThick"'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|EXTENSION_KEY
name|'EXTENSION_KEY'
op|'='
string|"'org.openstack.compute'"
newline|'\n'
DECL|variable|EXTENSION_TYPE_INSTANCE
name|'EXTENSION_TYPE_INSTANCE'
op|'='
string|"'instance'"
newline|'\n'
nl|'\n'
comment|'# The max number of devices that can be connnected to one adapter'
nl|'\n'
comment|'# One adapter has 16 slots but one reserved for controller'
nl|'\n'
DECL|variable|SCSI_MAX_CONNECT_NUMBER
name|'SCSI_MAX_CONNECT_NUMBER'
op|'='
number|'15'
newline|'\n'
nl|'\n'
comment|'# This list was extracted from the installation iso image for ESX 5.5 Update 1.'
nl|'\n'
comment|'# It is contained in s.v00, which is gzipped. The list was obtained by'
nl|'\n'
comment|"# searching for the string 'otherGuest' in the uncompressed contents of that"
nl|'\n'
comment|"# file, copying out the full list less the 'family' ids at the end, and sorting"
nl|'\n'
comment|'# it. The contents of this list should be updated whenever there is a new'
nl|'\n'
comment|'# release of ESX.'
nl|'\n'
DECL|variable|VALID_OS_TYPES
name|'VALID_OS_TYPES'
op|'='
name|'set'
op|'('
op|'['
nl|'\n'
string|"'asianux3_64Guest'"
op|','
nl|'\n'
string|"'asianux3Guest'"
op|','
nl|'\n'
string|"'asianux4_64Guest'"
op|','
nl|'\n'
string|"'asianux4Guest'"
op|','
nl|'\n'
string|"'centos64Guest'"
op|','
nl|'\n'
string|"'centosGuest'"
op|','
nl|'\n'
string|"'darwin10_64Guest'"
op|','
nl|'\n'
string|"'darwin10Guest'"
op|','
nl|'\n'
string|"'darwin11_64Guest'"
op|','
nl|'\n'
string|"'darwin11Guest'"
op|','
nl|'\n'
string|"'darwin12_64Guest'"
op|','
nl|'\n'
string|"'darwin13_64Guest'"
op|','
nl|'\n'
string|"'darwin64Guest'"
op|','
nl|'\n'
string|"'darwinGuest'"
op|','
nl|'\n'
string|"'debian4_64Guest'"
op|','
nl|'\n'
string|"'debian4Guest'"
op|','
nl|'\n'
string|"'debian5_64Guest'"
op|','
nl|'\n'
string|"'debian5Guest'"
op|','
nl|'\n'
string|"'debian6_64Guest'"
op|','
nl|'\n'
string|"'debian6Guest'"
op|','
nl|'\n'
string|"'debian7_64Guest'"
op|','
nl|'\n'
string|"'debian7Guest'"
op|','
nl|'\n'
string|"'dosGuest'"
op|','
nl|'\n'
string|"'eComStation2Guest'"
op|','
nl|'\n'
string|"'eComStationGuest'"
op|','
nl|'\n'
string|"'fedora64Guest'"
op|','
nl|'\n'
string|"'fedoraGuest'"
op|','
nl|'\n'
string|"'freebsd64Guest'"
op|','
nl|'\n'
string|"'freebsdGuest'"
op|','
nl|'\n'
string|"'genericLinuxGuest'"
op|','
nl|'\n'
string|"'mandrakeGuest'"
op|','
nl|'\n'
string|"'mandriva64Guest'"
op|','
nl|'\n'
string|"'mandrivaGuest'"
op|','
nl|'\n'
string|"'netware4Guest'"
op|','
nl|'\n'
string|"'netware5Guest'"
op|','
nl|'\n'
string|"'netware6Guest'"
op|','
nl|'\n'
string|"'nld9Guest'"
op|','
nl|'\n'
string|"'oesGuest'"
op|','
nl|'\n'
string|"'openServer5Guest'"
op|','
nl|'\n'
string|"'openServer6Guest'"
op|','
nl|'\n'
string|"'opensuse64Guest'"
op|','
nl|'\n'
string|"'opensuseGuest'"
op|','
nl|'\n'
string|"'oracleLinux64Guest'"
op|','
nl|'\n'
string|"'oracleLinuxGuest'"
op|','
nl|'\n'
string|"'os2Guest'"
op|','
nl|'\n'
string|"'other24xLinux64Guest'"
op|','
nl|'\n'
string|"'other24xLinuxGuest'"
op|','
nl|'\n'
string|"'other26xLinux64Guest'"
op|','
nl|'\n'
string|"'other26xLinuxGuest'"
op|','
nl|'\n'
string|"'other3xLinux64Guest'"
op|','
nl|'\n'
string|"'other3xLinuxGuest'"
op|','
nl|'\n'
string|"'otherGuest'"
op|','
nl|'\n'
string|"'otherGuest64'"
op|','
nl|'\n'
string|"'otherLinux64Guest'"
op|','
nl|'\n'
string|"'otherLinuxGuest'"
op|','
nl|'\n'
string|"'redhatGuest'"
op|','
nl|'\n'
string|"'rhel2Guest'"
op|','
nl|'\n'
string|"'rhel3_64Guest'"
op|','
nl|'\n'
string|"'rhel3Guest'"
op|','
nl|'\n'
string|"'rhel4_64Guest'"
op|','
nl|'\n'
string|"'rhel4Guest'"
op|','
nl|'\n'
string|"'rhel5_64Guest'"
op|','
nl|'\n'
string|"'rhel5Guest'"
op|','
nl|'\n'
string|"'rhel6_64Guest'"
op|','
nl|'\n'
string|"'rhel6Guest'"
op|','
nl|'\n'
string|"'rhel7_64Guest'"
op|','
nl|'\n'
string|"'rhel7Guest'"
op|','
nl|'\n'
string|"'sjdsGuest'"
op|','
nl|'\n'
string|"'sles10_64Guest'"
op|','
nl|'\n'
string|"'sles10Guest'"
op|','
nl|'\n'
string|"'sles11_64Guest'"
op|','
nl|'\n'
string|"'sles11Guest'"
op|','
nl|'\n'
string|"'sles12_64Guest'"
op|','
nl|'\n'
string|"'sles12Guest'"
op|','
nl|'\n'
string|"'sles64Guest'"
op|','
nl|'\n'
string|"'slesGuest'"
op|','
nl|'\n'
string|"'solaris10_64Guest'"
op|','
nl|'\n'
string|"'solaris10Guest'"
op|','
nl|'\n'
string|"'solaris11_64Guest'"
op|','
nl|'\n'
string|"'solaris6Guest'"
op|','
nl|'\n'
string|"'solaris7Guest'"
op|','
nl|'\n'
string|"'solaris8Guest'"
op|','
nl|'\n'
string|"'solaris9Guest'"
op|','
nl|'\n'
string|"'turboLinux64Guest'"
op|','
nl|'\n'
string|"'turboLinuxGuest'"
op|','
nl|'\n'
string|"'ubuntu64Guest'"
op|','
nl|'\n'
string|"'ubuntuGuest'"
op|','
nl|'\n'
string|"'unixWare7Guest'"
op|','
nl|'\n'
string|"'vmkernel5Guest'"
op|','
nl|'\n'
string|"'vmkernelGuest'"
op|','
nl|'\n'
string|"'win2000AdvServGuest'"
op|','
nl|'\n'
string|"'win2000ProGuest'"
op|','
nl|'\n'
string|"'win2000ServGuest'"
op|','
nl|'\n'
string|"'win31Guest'"
op|','
nl|'\n'
string|"'win95Guest'"
op|','
nl|'\n'
string|"'win98Guest'"
op|','
nl|'\n'
string|"'windows7_64Guest'"
op|','
nl|'\n'
string|"'windows7Guest'"
op|','
nl|'\n'
string|"'windows7Server64Guest'"
op|','
nl|'\n'
string|"'windows8_64Guest'"
op|','
nl|'\n'
string|"'windows8Guest'"
op|','
nl|'\n'
string|"'windows8Server64Guest'"
op|','
nl|'\n'
string|"'windowsHyperVGuest'"
op|','
nl|'\n'
string|"'winLonghorn64Guest'"
op|','
nl|'\n'
string|"'winLonghornGuest'"
op|','
nl|'\n'
string|"'winMeGuest'"
op|','
nl|'\n'
string|"'winNetBusinessGuest'"
op|','
nl|'\n'
string|"'winNetDatacenter64Guest'"
op|','
nl|'\n'
string|"'winNetDatacenterGuest'"
op|','
nl|'\n'
string|"'winNetEnterprise64Guest'"
op|','
nl|'\n'
string|"'winNetEnterpriseGuest'"
op|','
nl|'\n'
string|"'winNetStandard64Guest'"
op|','
nl|'\n'
string|"'winNetStandardGuest'"
op|','
nl|'\n'
string|"'winNetWebGuest'"
op|','
nl|'\n'
string|"'winNTGuest'"
op|','
nl|'\n'
string|"'winVista64Guest'"
op|','
nl|'\n'
string|"'winVistaGuest'"
op|','
nl|'\n'
string|"'winXPHomeGuest'"
op|','
nl|'\n'
string|"'winXPPro64Guest'"
op|','
nl|'\n'
string|"'winXPProGuest'"
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
endmarker|''
end_unit
