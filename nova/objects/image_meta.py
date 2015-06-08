begin_unit
comment|'# Copyright 2014 Red Hat, Inc'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'copy'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'hardware'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|NULLABLE_STRING_FIELDS
name|'NULLABLE_STRING_FIELDS'
op|'='
op|'['
string|"'name'"
op|','
string|"'checksum'"
op|','
string|"'owner'"
op|','
nl|'\n'
string|"'container_format'"
op|','
string|"'disk_format'"
op|']'
newline|'\n'
DECL|variable|NULLABLE_INTEGER_FIELDS
name|'NULLABLE_INTEGER_FIELDS'
op|'='
op|'['
string|"'size'"
op|','
string|"'virtual_size'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|ImageMeta
name|'class'
name|'ImageMeta'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: updated ImageMetaProps'
nl|'\n'
comment|'# Version 1.2: ImageMetaProps version 1.2'
nl|'\n'
comment|'# Version 1.3: ImageMetaProps version 1.3'
nl|'\n'
comment|'# Version 1.4: ImageMetaProps version 1.4'
nl|'\n'
comment|'# Version 1.5: ImageMetaProps version 1.5'
nl|'\n'
comment|'# Version 1.6: ImageMetaProps version 1.6'
nl|'\n'
comment|'# Version 1.7: ImageMetaProps version 1.7'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.7'"
newline|'\n'
nl|'\n'
comment|'# These are driven by what the image client API returns'
nl|'\n'
comment|'# to Nova from Glance. This is defined in the glance'
nl|'\n'
comment|'# code glance/api/v2/images.py get_base_properties()'
nl|'\n'
comment|'# method. A few things are currently left out:'
nl|'\n'
comment|'# self, file, schema - Nova does not appear to ever use'
nl|'\n'
comment|'# these field; locations - modelling the arbitrary'
nl|'\n'
comment|"# data in the 'metadata' subfield is non-trivial as"
nl|'\n'
comment|"# there's no clear spec."
nl|'\n'
comment|'#'
nl|'\n'
comment|'# TODO(ft): In version 2.0, these fields should be nullable:'
nl|'\n'
comment|'# name, checksum, owner, size, virtual_size, container_format, disk_format'
nl|'\n'
comment|'#'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'visibility'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'protected'"
op|':'
name|'fields'
op|'.'
name|'FlexibleBooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'checksum'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'owner'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'size'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'virtual_size'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'container_format'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'fields'
op|'.'
name|'DateTimeField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'fields'
op|'.'
name|'DateTimeField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'tags'"
op|':'
name|'fields'
op|'.'
name|'ListOfStringsField'
op|'('
op|')'
op|','
nl|'\n'
string|"'direct_url'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'min_ram'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'min_disk'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'properties'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'ImageMetaProps'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|obj_relationships
name|'obj_relationships'
op|'='
op|'{'
nl|'\n'
string|"'properties'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.0'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.1'"
op|','
string|"'1.1'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.2'"
op|','
string|"'1.2'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.3'"
op|','
string|"'1.3'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.4'"
op|','
string|"'1.4'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.5'"
op|','
string|"'1.5'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.6'"
op|','
string|"'1.6'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.7'"
op|','
string|"'1.7'"
op|')'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_dict
name|'def'
name|'from_dict'
op|'('
name|'cls'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create instance from image metadata dict\n\n        :param image_meta: image metadata dictionary\n\n        Creates a new object instance, initializing from the\n        properties associated with the image metadata instance\n\n        :returns: an ImageMeta instance\n        """'
newline|'\n'
name|'if'
name|'image_meta'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|"# We must turn 'properties' key dict into an object"
nl|'\n'
comment|'# so copy image_meta to avoid changing original'
nl|'\n'
dedent|''
name|'image_meta'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'image_meta'
op|')'
newline|'\n'
name|'image_meta'
op|'['
string|'"properties"'
op|']'
op|'='
name|'objects'
op|'.'
name|'ImageMetaProps'
op|'.'
name|'from_dict'
op|'('
nl|'\n'
name|'image_meta'
op|'.'
name|'get'
op|'('
string|'"properties"'
op|','
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Some fields are nullable in Glance DB schema, but was not marked that'
nl|'\n'
comment|'# in ImageMeta initially by mistake. To keep compatibility with compute'
nl|'\n'
comment|'# nodes which are run with previous versions these fields are still'
nl|'\n'
comment|'# not nullable in ImageMeta, but the code below converts None to'
nl|'\n'
comment|'# approppriate empty values.'
nl|'\n'
name|'for'
name|'fld'
name|'in'
name|'NULLABLE_STRING_FIELDS'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'fld'
name|'in'
name|'image_meta'
name|'and'
name|'image_meta'
op|'['
name|'fld'
op|']'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'image_meta'
op|'['
name|'fld'
op|']'
op|'='
string|"''"
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'fld'
name|'in'
name|'NULLABLE_INTEGER_FIELDS'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'fld'
name|'in'
name|'image_meta'
name|'and'
name|'image_meta'
op|'['
name|'fld'
op|']'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'image_meta'
op|'['
name|'fld'
op|']'
op|'='
number|'0'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'cls'
op|'('
op|'**'
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_instance
name|'def'
name|'from_instance'
op|'('
name|'cls'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create instance from instance system metadata\n\n        :param instance: Instance object\n\n        Creates a new object instance, initializing from the\n        system metadata "image_*" properties associated with\n        instance\n\n        :returns: an ImageMeta instance\n        """'
newline|'\n'
name|'sysmeta'
op|'='
name|'utils'
op|'.'
name|'instance_sys_meta'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'utils'
op|'.'
name|'get_image_from_system_metadata'
op|'('
name|'sysmeta'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'from_dict'
op|'('
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|ImageMetaProps
name|'class'
name|'ImageMetaProps'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: added os_require_quiesce field'
nl|'\n'
comment|'# Version 1.2: added img_hv_type and img_hv_requested_version fields'
nl|'\n'
comment|'# Version 1.3: HVSpec version 1.1'
nl|'\n'
comment|'# Version 1.4: added hw_vif_multiqueue_enabled field'
nl|'\n'
comment|'# Version 1.5: added os_admin_user field'
nl|'\n'
comment|"# Version 1.6: Added 'lxc' and 'uml' enum types to DiskBusField"
nl|'\n'
comment|'# Version 1.7: added img_config_drive field'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
name|'ImageMeta'
op|'.'
name|'VERSION'
newline|'\n'
nl|'\n'
comment|'# Maximum number of NUMA nodes permitted for the guest topology'
nl|'\n'
DECL|variable|NUMA_NODES_MAX
name|'NUMA_NODES_MAX'
op|'='
number|'128'
newline|'\n'
nl|'\n'
comment|"# 'hw_' - settings affecting the guest virtual machine hardware"
nl|'\n'
comment|"# 'img_' - settings affecting the use of images by the compute node"
nl|'\n'
comment|"# 'os_' - settings affecting the guest operating system setup"
nl|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
comment|'# name of guest hardware architecture eg i686, x86_64, ppc64'
nl|'\n'
string|"'hw_architecture'"
op|':'
name|'fields'
op|'.'
name|'ArchitectureField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# used to decide to expand root disk partition and fs to full size of'
nl|'\n'
comment|'# root disk'
nl|'\n'
string|"'hw_auto_disk_config'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# whether to display BIOS boot device menu'
nl|'\n'
string|"'hw_boot_menu'"
op|':'
name|'fields'
op|'.'
name|'FlexibleBooleanField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# name of the CDROM bus to use eg virtio, scsi, ide'
nl|'\n'
string|"'hw_cdrom_bus'"
op|':'
name|'fields'
op|'.'
name|'DiskBusField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# preferred number of CPU cores per socket'
nl|'\n'
string|"'hw_cpu_cores'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# preferred number of CPU sockets'
nl|'\n'
string|"'hw_cpu_sockets'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# maximum number of CPU cores per socket'
nl|'\n'
string|"'hw_cpu_max_cores'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# maximum number of CPU sockets'
nl|'\n'
string|"'hw_cpu_max_sockets'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# maximum number of CPU threads per core'
nl|'\n'
string|"'hw_cpu_max_threads'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# CPU thread allocation policy'
nl|'\n'
string|"'hw_cpu_policy'"
op|':'
name|'fields'
op|'.'
name|'CPUAllocationPolicyField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# preferred number of CPU threads per core'
nl|'\n'
string|"'hw_cpu_threads'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# guest ABI version for guest xentools either 1 or 2 (or 3 - depends on'
nl|'\n'
comment|'# Citrix PV tools version installed in image)'
nl|'\n'
string|"'hw_device_id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# name of the hard disk bus to use eg virtio, scsi, ide'
nl|'\n'
string|"'hw_disk_bus'"
op|':'
name|'fields'
op|'.'
name|'DiskBusField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# allocation mode eg 'preallocated'"
nl|'\n'
string|"'hw_disk_type'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# name of the floppy disk bus to use eg fd, scsi, ide'
nl|'\n'
string|"'hw_floppy_bus'"
op|':'
name|'fields'
op|'.'
name|'DiskBusField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# boolean - used to trigger code to inject networking when booting a CD'
nl|'\n'
comment|'# image with a network boot image'
nl|'\n'
string|"'hw_ipxe_boot'"
op|':'
name|'fields'
op|'.'
name|'FlexibleBooleanField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# There are sooooooooooo many possible machine types in'
nl|'\n'
comment|'# QEMU - several new ones with each new release - that it'
nl|'\n'
comment|'# is not practical to enumerate them all. So we use a free'
nl|'\n'
comment|'# form string'
nl|'\n'
string|"'hw_machine_type'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# One of the magic strings 'small', 'any', 'large'"
nl|'\n'
comment|'# or an explicit page size in KB (eg 4, 2048, ...)'
nl|'\n'
string|"'hw_mem_page_size'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# Number of guest NUMA nodes'
nl|'\n'
string|"'hw_numa_nodes'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# Each list entry corresponds to a guest NUMA node and the'
nl|'\n'
comment|'# set members indicate CPUs for that node'
nl|'\n'
string|"'hw_numa_cpus'"
op|':'
name|'fields'
op|'.'
name|'ListOfSetsOfIntegersField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# Each list entry corresponds to a guest NUMA node and the'
nl|'\n'
comment|'# list value indicates the memory size of that node.'
nl|'\n'
string|"'hw_numa_mem'"
op|':'
name|'fields'
op|'.'
name|'ListOfIntegersField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# boolean 'yes' or 'no' to enable QEMU guest agent"
nl|'\n'
string|"'hw_qemu_guest_agent'"
op|':'
name|'fields'
op|'.'
name|'FlexibleBooleanField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# name of the RNG device type eg virtio'
nl|'\n'
string|"'hw_rng_model'"
op|':'
name|'fields'
op|'.'
name|'RNGModelField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# number of serial ports to create'
nl|'\n'
string|"'hw_serial_port_count'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# name of the SCSI bus controller eg 'virtio-scsi', 'lsilogic', etc"
nl|'\n'
string|"'hw_scsi_model'"
op|':'
name|'fields'
op|'.'
name|'SCSIModelField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# name of the video adapter model to use, eg cirrus, vga, xen, qxl'
nl|'\n'
string|"'hw_video_model'"
op|':'
name|'fields'
op|'.'
name|'VideoModelField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# MB of video RAM to provide eg 64'
nl|'\n'
string|"'hw_video_ram'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# name of a NIC device model eg virtio, e1000, rtl8139'
nl|'\n'
string|"'hw_vif_model'"
op|':'
name|'fields'
op|'.'
name|'VIFModelField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# "xen" vs "hvm"'
nl|'\n'
string|"'hw_vm_mode'"
op|':'
name|'fields'
op|'.'
name|'VMModeField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# action to take when watchdog device fires eg reset, poweroff, pause,'
nl|'\n'
comment|'# none'
nl|'\n'
string|"'hw_watchdog_action'"
op|':'
name|'fields'
op|'.'
name|'WatchdogActionField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# boolean - If true, this will enable the virtio-multiqueue feature'
nl|'\n'
string|"'hw_vif_multiqueue_enabled'"
op|':'
name|'fields'
op|'.'
name|'FlexibleBooleanField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# if true download using bittorrent'
nl|'\n'
string|"'img_bittorrent'"
op|':'
name|'fields'
op|'.'
name|'FlexibleBooleanField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# Which data format the 'img_block_device_mapping' field is"
nl|'\n'
comment|'# using to represent the block device mapping'
nl|'\n'
string|"'img_bdm_v2'"
op|':'
name|'fields'
op|'.'
name|'FlexibleBooleanField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# Block device mapping - the may can be in one or two completely'
nl|'\n'
comment|"# different formats. The 'img_bdm_v2' field determines whether"
nl|'\n'
comment|'# it is in legacy format, or the new current format. Ideally'
nl|'\n'
comment|'# we would have a formal data type for this field instead of a'
nl|'\n'
comment|'# dict, but with 2 different formats to represent this is hard.'
nl|'\n'
comment|'# See nova/block_device.py from_legacy_mapping() for the complex'
nl|'\n'
comment|'# conversion code. So for now leave it as a dict and continue'
nl|'\n'
comment|'# to use existing code that is able to convert dict into the'
nl|'\n'
comment|'# desired internal BDM formats'
nl|'\n'
string|"'img_block_device_mapping'"
op|':'
nl|'\n'
name|'fields'
op|'.'
name|'ListOfDictOfNullableStringsField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# boolean - if True, and image cache set to "some" decides if image'
nl|'\n'
comment|'# should be cached on host when server is booted on that host'
nl|'\n'
string|"'img_cache_in_nova'"
op|':'
name|'fields'
op|'.'
name|'FlexibleBooleanField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# Compression level for images. (1-9)'
nl|'\n'
string|"'img_compression_level'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# hypervisor supported version, eg. '>=2.6'"
nl|'\n'
string|"'img_hv_requested_version'"
op|':'
name|'fields'
op|'.'
name|'VersionPredicateField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# type of the hypervisor, eg kvm, ironic, xen'
nl|'\n'
string|"'img_hv_type'"
op|':'
name|'fields'
op|'.'
name|'HVTypeField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# Whether the image needs/expected config drive'
nl|'\n'
string|"'img_config_drive'"
op|':'
name|'fields'
op|'.'
name|'ConfigDrivePolicyField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# boolean flag to set space-saving or performance behavior on the'
nl|'\n'
comment|'# Datastore'
nl|'\n'
string|"'img_linked_clone'"
op|':'
name|'fields'
op|'.'
name|'FlexibleBooleanField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# Image mappings - related to Block device mapping data - mapping'
nl|'\n'
comment|'# of virtual image names to device names. This could be represented'
nl|'\n'
comment|'# as a formatl data type, but is left as dict for same reason as'
nl|'\n'
comment|'# img_block_device_mapping field. It would arguably make sense for'
nl|'\n'
comment|'# the two to be combined into a single field and data type in the'
nl|'\n'
comment|'# future.'
nl|'\n'
string|"'img_mappings'"
op|':'
name|'fields'
op|'.'
name|'ListOfDictOfNullableStringsField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# image project id (set on upload)'
nl|'\n'
string|"'img_owner_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# root device name, used in snapshotting eg /dev/<blah>'
nl|'\n'
string|"'img_root_device_name'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# boolean - if false don't talk to nova agent"
nl|'\n'
string|"'img_use_agent'"
op|':'
name|'fields'
op|'.'
name|'FlexibleBooleanField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# integer value 1'
nl|'\n'
string|"'img_version'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# string of username with admin privileges'
nl|'\n'
string|"'os_admin_user'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# string of boot time command line arguments for the guest kernel'
nl|'\n'
string|"'os_command_line'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# the name of the specific guest operating system distro. This'
nl|'\n'
comment|'# is not done as an Enum since the list of operating systems is'
nl|'\n'
comment|'# growing incredibly fast, and valid values can be arbitrarily'
nl|'\n'
comment|'# user defined. Nova has no real need for strict validation so'
nl|'\n'
comment|'# leave it freeform'
nl|'\n'
string|"'os_distro'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# boolean - if true, then guest must support disk quiesce'
nl|'\n'
comment|'# or snapshot operation will be denied'
nl|'\n'
string|"'os_require_quiesce'"
op|':'
name|'fields'
op|'.'
name|'FlexibleBooleanField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# boolean - if using agent don't inject files, assume someone else is"
nl|'\n'
comment|'# doing that (cloud-init)'
nl|'\n'
string|"'os_skip_agent_inject_files_at_boot'"
op|':'
name|'fields'
op|'.'
name|'FlexibleBooleanField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# boolean - if using agent don't try inject ssh key, assume someone"
nl|'\n'
comment|'# else is doing that (cloud-init)'
nl|'\n'
string|"'os_skip_agent_inject_ssh'"
op|':'
name|'fields'
op|'.'
name|'FlexibleBooleanField'
op|'('
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# The guest operating system family such as 'linux', 'windows' - this"
nl|'\n'
comment|'# is a fairly generic type. For a detailed type consider os_distro'
nl|'\n'
comment|'# instead'
nl|'\n'
string|"'os_type'"
op|':'
name|'fields'
op|'.'
name|'OSTypeField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|'# The keys are the legacy property names and'
nl|'\n'
comment|'# the values are the current preferred names'
nl|'\n'
DECL|variable|_legacy_property_map
name|'_legacy_property_map'
op|'='
op|'{'
nl|'\n'
string|"'architecture'"
op|':'
string|"'hw_architecture'"
op|','
nl|'\n'
string|"'owner_id'"
op|':'
string|"'img_owner_id'"
op|','
nl|'\n'
string|"'vmware_disktype'"
op|':'
string|"'hw_disk_type'"
op|','
nl|'\n'
string|"'vmware_image_version'"
op|':'
string|"'img_version'"
op|','
nl|'\n'
string|"'vmware_ostype'"
op|':'
string|"'os_distro'"
op|','
nl|'\n'
string|"'auto_disk_config'"
op|':'
string|"'hw_auto_disk_config'"
op|','
nl|'\n'
string|"'ipxe_boot'"
op|':'
string|"'hw_ipxe_boot'"
op|','
nl|'\n'
string|"'xenapi_device_id'"
op|':'
string|"'hw_device_id'"
op|','
nl|'\n'
string|"'xenapi_image_compression_level'"
op|':'
string|"'img_compression_level'"
op|','
nl|'\n'
string|"'vmware_linked_clone'"
op|':'
string|"'img_linked_clone'"
op|','
nl|'\n'
string|"'xenapi_use_agent'"
op|':'
string|"'img_use_agent'"
op|','
nl|'\n'
string|"'xenapi_skip_agent_inject_ssh'"
op|':'
string|"'os_skip_agent_inject_ssh'"
op|','
nl|'\n'
string|"'xenapi_skip_agent_inject_files_at_boot'"
op|':'
nl|'\n'
string|"'os_skip_agent_inject_files_at_boot'"
op|','
nl|'\n'
string|"'cache_in_nova'"
op|':'
string|"'img_cache_in_nova'"
op|','
nl|'\n'
string|"'vm_mode'"
op|':'
string|"'hw_vm_mode'"
op|','
nl|'\n'
string|"'bittorrent'"
op|':'
string|"'img_bittorrent'"
op|','
nl|'\n'
string|"'mappings'"
op|':'
string|"'img_mappings'"
op|','
nl|'\n'
string|"'block_device_mapping'"
op|':'
string|"'img_block_device_mapping'"
op|','
nl|'\n'
string|"'bdm_v2'"
op|':'
string|"'img_bdm_v2'"
op|','
nl|'\n'
string|"'root_device_name'"
op|':'
string|"'img_root_device_name'"
op|','
nl|'\n'
string|"'hypervisor_version_requires'"
op|':'
string|"'img_hv_requested_version'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|'# TODO(berrange): Need to run this from a data migration'
nl|'\n'
comment|'# at some point so we can eventually kill off the compat'
nl|'\n'
DECL|member|_set_attr_from_legacy_names
name|'def'
name|'_set_attr_from_legacy_names'
op|'('
name|'self'
op|','
name|'image_props'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'legacy_key'
name|'in'
name|'self'
op|'.'
name|'_legacy_property_map'
op|':'
newline|'\n'
indent|'            '
name|'new_key'
op|'='
name|'self'
op|'.'
name|'_legacy_property_map'
op|'['
name|'legacy_key'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'legacy_key'
name|'not'
name|'in'
name|'image_props'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'setattr'
op|'('
name|'self'
op|','
name|'new_key'
op|','
name|'image_props'
op|'['
name|'legacy_key'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'vmware_adaptertype'
op|'='
name|'image_props'
op|'.'
name|'get'
op|'('
string|'"vmware_adaptertype"'
op|')'
newline|'\n'
name|'if'
name|'vmware_adaptertype'
op|'=='
string|'"ide"'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
string|'"hw_disk_bus"'
op|','
string|'"ide"'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'vmware_adaptertype'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
string|'"hw_disk_bus"'
op|','
string|'"scsi"'
op|')'
newline|'\n'
name|'setattr'
op|'('
name|'self'
op|','
string|'"hw_scsi_model"'
op|','
name|'vmware_adaptertype'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_numa_mem
dedent|''
dedent|''
name|'def'
name|'_set_numa_mem'
op|'('
name|'self'
op|','
name|'image_props'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hw_numa_mem'
op|'='
op|'['
op|']'
newline|'\n'
name|'hw_numa_mem_set'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'cellid'
name|'in'
name|'range'
op|'('
name|'ImageMetaProps'
op|'.'
name|'NUMA_NODES_MAX'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'memprop'
op|'='
string|'"hw_numa_mem.%d"'
op|'%'
name|'cellid'
newline|'\n'
name|'if'
name|'memprop'
name|'not'
name|'in'
name|'image_props'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'hw_numa_mem'
op|'.'
name|'append'
op|'('
name|'int'
op|'('
name|'image_props'
op|'['
name|'memprop'
op|']'
op|')'
op|')'
newline|'\n'
name|'hw_numa_mem_set'
op|'='
name|'True'
newline|'\n'
name|'del'
name|'image_props'
op|'['
name|'memprop'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'hw_numa_mem_set'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'hw_numa_mem'
op|'='
name|'hw_numa_mem'
newline|'\n'
nl|'\n'
DECL|member|_set_numa_cpus
dedent|''
dedent|''
name|'def'
name|'_set_numa_cpus'
op|'('
name|'self'
op|','
name|'image_props'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hw_numa_cpus'
op|'='
op|'['
op|']'
newline|'\n'
name|'hw_numa_cpus_set'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'cellid'
name|'in'
name|'range'
op|'('
name|'ImageMetaProps'
op|'.'
name|'NUMA_NODES_MAX'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cpuprop'
op|'='
string|'"hw_numa_cpus.%d"'
op|'%'
name|'cellid'
newline|'\n'
name|'if'
name|'cpuprop'
name|'not'
name|'in'
name|'image_props'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'hw_numa_cpus'
op|'.'
name|'append'
op|'('
nl|'\n'
name|'hardware'
op|'.'
name|'parse_cpu_spec'
op|'('
name|'image_props'
op|'['
name|'cpuprop'
op|']'
op|')'
op|')'
newline|'\n'
name|'hw_numa_cpus_set'
op|'='
name|'True'
newline|'\n'
name|'del'
name|'image_props'
op|'['
name|'cpuprop'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'hw_numa_cpus_set'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'hw_numa_cpus'
op|'='
name|'hw_numa_cpus'
newline|'\n'
nl|'\n'
DECL|member|_set_attr_from_current_names
dedent|''
dedent|''
name|'def'
name|'_set_attr_from_current_names'
op|'('
name|'self'
op|','
name|'image_props'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
name|'self'
op|'.'
name|'fields'
op|':'
newline|'\n'
comment|'# The two NUMA fields need special handling to'
nl|'\n'
comment|'# un-stringify them correctly'
nl|'\n'
indent|'            '
name|'if'
name|'key'
op|'=='
string|'"hw_numa_mem"'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_set_numa_mem'
op|'('
name|'image_props'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'key'
op|'=='
string|'"hw_numa_cpus"'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_set_numa_cpus'
op|'('
name|'image_props'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'key'
name|'not'
name|'in'
name|'image_props'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'setattr'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'image_props'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_dict
name|'def'
name|'from_dict'
op|'('
name|'cls'
op|','
name|'image_props'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create instance from image properties dict\n\n        :param image_props: dictionary of image metdata properties\n\n        Creates a new object instance, initializing from a\n        dictionary of image metadata properties\n\n        :returns: an ImageMetaProps instance\n        """'
newline|'\n'
name|'obj'
op|'='
name|'cls'
op|'('
op|')'
newline|'\n'
comment|'# We look to see if the dict has entries for any'
nl|'\n'
comment|'# of the legacy property names first. Then we use'
nl|'\n'
comment|'# the current property names. That way if both the'
nl|'\n'
comment|'# current and legacy names are set, the value'
nl|'\n'
comment|'# associated with the current name takes priority'
nl|'\n'
name|'obj'
op|'.'
name|'_set_attr_from_legacy_names'
op|'('
name|'image_props'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'_set_attr_from_current_names'
op|'('
name|'image_props'
op|')'
newline|'\n'
name|'return'
name|'obj'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'defvalue'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the value of an attribute\n        :param name: the attribute to request\n        :param defvalue: the default value if not set\n\n        This returns the value of an attribute if it is currently\n        set, otherwise it will return None.\n\n        This differs from accessing props.attrname, because that\n        will raise an exception if the attribute has no value set.\n\n        So instead of\n\n          if image_meta.properties.obj_attr_is_set("some_attr"):\n             val = image_meta.properties.some_attr\n          else\n             val = None\n\n        Callers can rely on unconditional access\n\n             val = image_meta.properties.get("some_attr")\n\n        :returns: the attribute value or None\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'defvalue'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'getattr'
op|'('
name|'self'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
