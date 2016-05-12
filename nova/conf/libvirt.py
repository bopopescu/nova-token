begin_unit
comment|'# Copyright 2016 OpenStack Foundation'
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
name|'import'
name|'itertools'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'paths'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
comment|'# Downtime period in milliseconds'
nl|'\n'
DECL|variable|LIVE_MIGRATION_DOWNTIME_MIN
name|'LIVE_MIGRATION_DOWNTIME_MIN'
op|'='
number|'100'
newline|'\n'
comment|'# Step count'
nl|'\n'
DECL|variable|LIVE_MIGRATION_DOWNTIME_STEPS_MIN
name|'LIVE_MIGRATION_DOWNTIME_STEPS_MIN'
op|'='
number|'3'
newline|'\n'
comment|'# Delay in seconds'
nl|'\n'
DECL|variable|LIVE_MIGRATION_DOWNTIME_DELAY_MIN
name|'LIVE_MIGRATION_DOWNTIME_DELAY_MIN'
op|'='
number|'10'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_group
name|'libvirt_group'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
string|'"libvirt"'
op|','
nl|'\n'
DECL|variable|title
name|'title'
op|'='
string|'"Libvirt Options"'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nLibvirt options allows cloud administrator to configure related\nlibvirt hypervisor driver to be used within an OpenStack deployment.\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_general_opts
name|'libvirt_general_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'rescue_image_id'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Rescue ami image. This will not be used if an image id '"
nl|'\n'
string|"'is provided by the user.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'rescue_kernel_id'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Rescue aki image'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'rescue_ramdisk_id'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Rescue ari image'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'virt_type'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'kvm'"
op|','
nl|'\n'
DECL|variable|choices
name|'choices'
op|'='
op|'('
string|"'kvm'"
op|','
string|"'lxc'"
op|','
string|"'qemu'"
op|','
string|"'uml'"
op|','
string|"'xen'"
op|','
string|"'parallels'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Libvirt domain type'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'connection_uri'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Override the default libvirt URI '"
nl|'\n'
string|"'(which is dependent on virt_type)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'inject_password'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Inject the admin password at boot time, '"
nl|'\n'
string|"'without an agent.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'inject_key'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Inject the ssh public key at boot time'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'inject_partition'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'-'
number|'2'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The partition to inject to : '"
nl|'\n'
string|"'-2 => disable, -1 => inspect (libguestfs only), '"
nl|'\n'
string|"'0 => not partitioned, >0 => partition number'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_usb_tablet'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Sync virtual and real mouse cursors in Windows VMs'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'live_migration_inbound_addr'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Live migration target ip or hostname '"
nl|'\n'
string|"'(if this option is set to None, which is the default, '"
nl|'\n'
string|"'the hostname of the migration target '"
nl|'\n'
string|"'compute node will be used)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'live_migration_uri'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Override the default libvirt live migration target URI '"
nl|'\n'
string|"'(which is dependent on virt_type) '"
nl|'\n'
string|'\'(any included "%s" is replaced with \''
nl|'\n'
string|"'the migration target hostname)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'live_migration_flag'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'VIR_MIGRATE_UNDEFINE_SOURCE, VIR_MIGRATE_PEER2PEER, '"
nl|'\n'
string|"'VIR_MIGRATE_LIVE, VIR_MIGRATE_TUNNELLED'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Migration flags to be set for live migration'"
op|','
nl|'\n'
DECL|variable|deprecated_for_removal
name|'deprecated_for_removal'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|deprecated_reason
name|'deprecated_reason'
op|'='
string|"'The correct live migration flags can be '"
nl|'\n'
string|"'inferred from the new '"
nl|'\n'
string|"'live_migration_tunnelled config option. '"
nl|'\n'
string|"'live_migration_flag will be removed to '"
nl|'\n'
string|"'avoid potential misconfiguration.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'block_migration_flag'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'VIR_MIGRATE_UNDEFINE_SOURCE, VIR_MIGRATE_PEER2PEER, '"
nl|'\n'
string|"'VIR_MIGRATE_LIVE, VIR_MIGRATE_TUNNELLED, '"
nl|'\n'
string|"'VIR_MIGRATE_NON_SHARED_INC'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Migration flags to be set for block migration'"
op|','
nl|'\n'
DECL|variable|deprecated_for_removal
name|'deprecated_for_removal'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|deprecated_reason
name|'deprecated_reason'
op|'='
string|"'The correct block migration flags can be '"
nl|'\n'
string|"'inferred from the new '"
nl|'\n'
string|"'live_migration_tunnelled config option. '"
nl|'\n'
string|"'block_migration_flag will be removed to '"
nl|'\n'
string|"'avoid potential misconfiguration.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'live_migration_tunnelled'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Whether to use tunnelled migration, where migration '"
nl|'\n'
string|"'data is transported over the libvirtd connection. If '"
nl|'\n'
string|"'True, we use the VIR_MIGRATE_TUNNELLED migration flag, '"
nl|'\n'
string|"'avoiding the need to configure the network to allow '"
nl|'\n'
string|"'direct hypervisor to hypervisor communication. If '"
nl|'\n'
string|"'False, use the native transport. If not set, Nova '"
nl|'\n'
string|"'will choose a sensible default based on, for example '"
nl|'\n'
string|"'the availability of native encryption support in the '"
nl|'\n'
string|"'hypervisor.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'live_migration_bandwidth'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Maximum bandwidth(in MiB/s) to be used during migration. '"
nl|'\n'
string|"'If set to 0, will choose a suitable default. Some '"
nl|'\n'
string|"'hypervisors do not support this feature and will return '"
nl|'\n'
string|"'an error if bandwidth is not 0. Please refer to the '"
nl|'\n'
string|"'libvirt documentation for further details'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'live_migration_downtime'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'500'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Maximum permitted downtime, in milliseconds, for live '"
nl|'\n'
string|"'migration switchover. Will be rounded up to a minimum '"
nl|'\n'
string|"'of %dms. Use a large value if guest liveness is '"
nl|'\n'
string|"'unimportant.'"
op|'%'
name|'LIVE_MIGRATION_DOWNTIME_MIN'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'live_migration_downtime_steps'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of incremental steps to reach max downtime value. '"
nl|'\n'
string|"'Will be rounded up to a minimum of %d steps'"
op|'%'
nl|'\n'
name|'LIVE_MIGRATION_DOWNTIME_STEPS_MIN'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'live_migration_downtime_delay'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'75'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Time to wait, in seconds, between each step increase '"
nl|'\n'
string|"'of the migration downtime. Minimum delay is %d seconds. '"
nl|'\n'
string|"'Value is per GiB of guest RAM + disk to be transferred, '"
nl|'\n'
string|"'with lower bound of a minimum of 2 GiB per device'"
op|'%'
nl|'\n'
name|'LIVE_MIGRATION_DOWNTIME_DELAY_MIN'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'live_migration_completion_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'800'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Time to wait, in seconds, for migration to successfully '"
nl|'\n'
string|"'complete transferring data before aborting the '"
nl|'\n'
string|"'operation. Value is per GiB of guest RAM + disk to be '"
nl|'\n'
string|"'transferred, with lower bound of a minimum of 2 GiB. '"
nl|'\n'
string|"'Should usually be larger than downtime delay * downtime '"
nl|'\n'
string|"'steps. Set to 0 to disable timeouts.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'live_migration_progress_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'150'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Time to wait, in seconds, for migration to make forward '"
nl|'\n'
string|"'progress in transferring data before aborting the '"
nl|'\n'
string|"'operation. Set to 0 to disable timeouts.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'snapshot_image_format'"
op|','
nl|'\n'
DECL|variable|choices
name|'choices'
op|'='
op|'('
string|"'raw'"
op|','
string|"'qcow2'"
op|','
string|"'vmdk'"
op|','
string|"'vdi'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Snapshot image format. Defaults to same as source image'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'disk_prefix'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Override the default disk prefix for the devices attached'"
nl|'\n'
string|"' to a server, which is dependent on virt_type. '"
nl|'\n'
string|"'(valid options are: sd, xvd, uvd, vd)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'wait_soft_reboot_seconds'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'120'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of seconds to wait for instance to shut down after'"
nl|'\n'
string|"' soft reboot request is made. We fall back to hard reboot'"
nl|'\n'
string|"' if instance does not shutdown within this window.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cpu_mode'"
op|','
nl|'\n'
DECL|variable|choices
name|'choices'
op|'='
op|'('
string|"'host-model'"
op|','
string|"'host-passthrough'"
op|','
string|"'custom'"
op|','
string|"'none'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'\'Set to "host-model" to clone the host CPU feature flags; \''
nl|'\n'
string|'\'to "host-passthrough" to use the host CPU model exactly; \''
nl|'\n'
string|'\'to "custom" to use a named CPU model; \''
nl|'\n'
string|'\'to "none" to not set any CPU model. \''
nl|'\n'
string|'\'If virt_type="kvm|qemu", it will default to \''
nl|'\n'
string|'\'"host-model", otherwise it will default to "none"\''
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cpu_model'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set to a named libvirt CPU model (see names listed '"
nl|'\n'
string|"'in /usr/share/libvirt/cpu_map.xml). Only has effect if '"
nl|'\n'
string|'\'cpu_mode="custom" and virt_type="kvm|qemu"\''
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'snapshots_directory'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$instances_path/snapshots'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Location where libvirt driver will store snapshots '"
nl|'\n'
string|"'before uploading them to image service'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'xen_hvmloader_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'/usr/lib/xen/boot/hvmloader'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Location where the Xen hvmloader is kept'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'disk_cachemodes'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Specific cachemodes to use for different disk types '"
nl|'\n'
string|"'e.g: file=directsync,block=none'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'rng_dev_path'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'A path to a device that will be used as source of '"
nl|'\n'
string|"'entropy on the host. Permitted options are: '"
nl|'\n'
string|"'/dev/random or /dev/hwrng'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'hw_machine_type'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'For qemu or KVM guests, set this option to specify '"
nl|'\n'
string|"'a default machine type per host architecture. '"
nl|'\n'
string|"'You can find a list of supported machine types '"
nl|'\n'
string|"'in your environment by checking the output of '"
nl|'\n'
string|'\'the "virsh capabilities"command. The format of the \''
nl|'\n'
string|"'value for this config option is host-arch=machine-type. '"
nl|'\n'
string|"'For example: x86_64=machinetype1,armv7l=machinetype2'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'sysinfo_serial'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'auto'"
op|','
nl|'\n'
DECL|variable|choices
name|'choices'
op|'='
op|'('
string|"'none'"
op|','
string|"'os'"
op|','
string|"'hardware'"
op|','
string|"'auto'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'\'The data source used to the populate the host "serial" \''
nl|'\n'
string|"'UUID exposed to guest in the virtual BIOS.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'mem_stats_period_seconds'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'A number of seconds to memory usage statistics period. '"
nl|'\n'
string|"'Zero or negative value mean to disable memory usage '"
nl|'\n'
string|"'statistics.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'uid_maps'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'List of uid targets and ranges.'"
nl|'\n'
string|"'Syntax is guest-uid:host-uid:count'"
nl|'\n'
string|"'Maximum of 5 allowed.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'gid_maps'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'List of guid targets and ranges.'"
nl|'\n'
string|"'Syntax is guest-gid:host-gid:count'"
nl|'\n'
string|"'Maximum of 5 allowed.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'realtime_scheduler_priority'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'In a realtime host context vCPUs for guest will run in '"
nl|'\n'
string|"'that scheduling priority. Priority depends on the host '"
nl|'\n'
string|"'kernel (usually 1-99)'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_imagebackend_opts
name|'libvirt_imagebackend_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'images_type'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'default'"
op|','
nl|'\n'
DECL|variable|choices
name|'choices'
op|'='
op|'('
string|"'raw'"
op|','
string|"'qcow2'"
op|','
string|"'lvm'"
op|','
string|"'rbd'"
op|','
string|"'ploop'"
op|','
string|"'default'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'VM Images format. If default is specified, then'"
nl|'\n'
string|"' use_cow_images flag is used instead of this one.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'images_volume_group'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'LVM Volume Group that is used for VM images, when you'"
nl|'\n'
string|"' specify images_type=lvm.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'sparse_logical_volumes'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Create sparse logical volumes (with virtualsize)'"
nl|'\n'
string|"' if this flag is set to True.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'images_rbd_pool'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'rbd'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The RADOS pool in which rbd volumes are stored'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'images_rbd_ceph_conf'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
comment|'# default determined by librados'
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Path to the ceph configuration file to use'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'hw_disk_discard'"
op|','
nl|'\n'
DECL|variable|choices
name|'choices'
op|'='
op|'('
string|"'ignore'"
op|','
string|"'unmap'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Discard option for nova managed disks. Need'"
nl|'\n'
string|"' Libvirt(1.0.6) Qemu1.5 (raw format) Qemu1.6(qcow2'"
nl|'\n'
string|"' format)'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_imagecache_opts
name|'libvirt_imagecache_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'image_info_filename_pattern'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$instances_path/$image_cache_subdirectory_name/'"
nl|'\n'
string|"'%(image)s.info'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Allows image information files to be stored in '"
nl|'\n'
string|"'non-standard locations'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'remove_unused_kernels'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|deprecated_for_removal
name|'deprecated_for_removal'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'DEPRECATED: Should unused kernel images be removed? '"
nl|'\n'
string|"'This is only safe to enable if all compute nodes have '"
nl|'\n'
string|"'been updated to support this option (running Grizzly or '"
nl|'\n'
string|"'newer level compute). This will be the default behavior '"
nl|'\n'
string|"'in the 13.0.0 release.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'remove_unused_resized_minimum_age_seconds'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Unused resized base images younger than this will not be '"
nl|'\n'
string|"'removed'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'checksum_base_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Write a checksum for files in _base to disk'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'checksum_interval_seconds'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'How frequently to checksum base images'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_lvm_opts
name|'libvirt_lvm_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'volume_clear'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'zero'"
op|','
nl|'\n'
DECL|variable|choices
name|'choices'
op|'='
op|'('
string|"'none'"
op|','
string|"'zero'"
op|','
string|"'shred'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Method used to wipe old volumes.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'volume_clear_size'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
name|'help'
op|'='
string|"'Size in MiB to wipe at start of old volumes. 0 => all'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_utils_opts
name|'libvirt_utils_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'snapshot_compression'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Compress snapshot images when possible. This '"
nl|'\n'
string|"'currently applies exclusively to qcow2 images'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_vif_opts
name|'libvirt_vif_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_virtio_for_bridges'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Use virtio for bridge interfaces with KVM/QEMU'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_volume_opts
name|'libvirt_volume_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'qemu_allowed_storage_drivers'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Protocols listed here will be accessed directly '"
nl|'\n'
string|"'from QEMU. Currently supported protocols: [gluster]'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_volume_aoe_opts
name|'libvirt_volume_aoe_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'num_aoe_discover_tries'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of times to rediscover AoE target to find volume'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_volume_glusterfs_opts
name|'libvirt_volume_glusterfs_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'glusterfs_mount_point_base'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'paths'
op|'.'
name|'state_path_def'
op|'('
string|"'mnt'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Directory where the glusterfs volume is mounted on the '"
nl|'\n'
string|"'compute node'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_volume_iscsi_opts
name|'libvirt_volume_iscsi_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'num_iscsi_scan_tries'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'5'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of times to rescan iSCSI target to find volume'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'iscsi_use_multipath'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Use multipath connection of the iSCSI or FC volume'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'iscsi_iface'"
op|','
nl|'\n'
DECL|variable|deprecated_name
name|'deprecated_name'
op|'='
string|"'iscsi_transport'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The iSCSI transport iface to use to connect to target in '"
nl|'\n'
string|"'case offload support is desired. Default format is of '"
nl|'\n'
string|"'the form <transport_name>.<hwaddress> where '"
nl|'\n'
string|"'<transport_name> is one of (be2iscsi, bnx2i, cxgb3i, '"
nl|'\n'
string|"'cxgb4i, qla4xxx, ocs) and <hwaddress> is the MAC address '"
nl|'\n'
string|"'of the interface and can be generated via the '"
nl|'\n'
string|"'iscsiadm -m iface command. Do not confuse the '"
nl|'\n'
string|"'iscsi_iface parameter to be provided here with the '"
nl|'\n'
string|"'actual transport name.'"
op|')'
op|','
nl|'\n'
comment|'# iser is also supported, but use LibvirtISERVolumeDriver'
nl|'\n'
comment|'# instead'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_volume_iser_opts
name|'libvirt_volume_iser_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'num_iser_scan_tries'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'5'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of times to rescan iSER target to find volume'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'iser_use_multipath'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Use multipath connection of the iSER volume'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_volume_net_opts
name|'libvirt_volume_net_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'rbd_user'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The RADOS client name for accessing rbd volumes'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'rbd_secret_uuid'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The libvirt UUID of the secret for the rbd_user'"
nl|'\n'
string|"'volumes'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_volume_nfs_opts
name|'libvirt_volume_nfs_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'nfs_mount_point_base'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'paths'
op|'.'
name|'state_path_def'
op|'('
string|"'mnt'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Directory where the NFS volume is mounted on the'"
nl|'\n'
string|"' compute node'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'nfs_mount_options'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Mount options passed to the NFS client. See section '"
nl|'\n'
string|"'of the nfs man page for details'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_volume_quobyte_opts
name|'libvirt_volume_quobyte_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'quobyte_mount_point_base'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'paths'
op|'.'
name|'state_path_def'
op|'('
string|"'mnt'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Directory where the Quobyte volume is mounted on the '"
nl|'\n'
string|"'compute node'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'quobyte_client_cfg'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Path to a Quobyte Client configuration file.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_volume_scality_opts
name|'libvirt_volume_scality_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'scality_sofs_config'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Path or URL to Scality SOFS configuration file'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'scality_sofs_mount_point'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$state_path/scality'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Base dir where Scality SOFS shall be mounted'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_volume_smbfs_opts
name|'libvirt_volume_smbfs_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'smbfs_mount_point_base'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'paths'
op|'.'
name|'state_path_def'
op|'('
string|"'mnt'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Directory where the SMBFS shares are mounted on the '"
nl|'\n'
string|"'compute node'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'smbfs_mount_options'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Mount options passed to the SMBFS client. See '"
nl|'\n'
string|"'mount.cifs man page for details. Note that the '"
nl|'\n'
string|"'libvirt-qemu uid and gid must be specified.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|ALL_OPTS
name|'ALL_OPTS'
op|'='
name|'list'
op|'('
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
name|'libvirt_general_opts'
op|','
nl|'\n'
name|'libvirt_imagebackend_opts'
op|','
nl|'\n'
name|'libvirt_imagecache_opts'
op|','
nl|'\n'
name|'libvirt_lvm_opts'
op|','
nl|'\n'
name|'libvirt_utils_opts'
op|','
nl|'\n'
name|'libvirt_vif_opts'
op|','
nl|'\n'
name|'libvirt_volume_opts'
op|','
nl|'\n'
name|'libvirt_volume_aoe_opts'
op|','
nl|'\n'
name|'libvirt_volume_glusterfs_opts'
op|','
nl|'\n'
name|'libvirt_volume_iscsi_opts'
op|','
nl|'\n'
name|'libvirt_volume_iser_opts'
op|','
nl|'\n'
name|'libvirt_volume_net_opts'
op|','
nl|'\n'
name|'libvirt_volume_nfs_opts'
op|','
nl|'\n'
name|'libvirt_volume_quobyte_opts'
op|','
nl|'\n'
name|'libvirt_volume_scality_opts'
op|','
nl|'\n'
name|'libvirt_volume_smbfs_opts'
op|','
nl|'\n'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_opts
name|'def'
name|'register_opts'
op|'('
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conf'
op|'.'
name|'register_group'
op|'('
name|'libvirt_group'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'ALL_OPTS'
op|','
name|'group'
op|'='
name|'libvirt_group'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(hieulq): if not using group name, oslo config will generate duplicate'
nl|'\n'
comment|'# config section. This need to be remove when completely move all libvirt'
nl|'\n'
comment|'# options to this place.'
nl|'\n'
DECL|function|list_opts
dedent|''
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
name|'libvirt_group'
op|'.'
name|'name'
op|':'
name|'ALL_OPTS'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit
