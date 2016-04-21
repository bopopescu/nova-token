begin_unit
comment|'# Copyright 2015 Huawei Technology corp.'
nl|'\n'
comment|'# Copyright 2015 OpenStack Foundation'
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
name|'import'
name|'socket'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
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
DECL|variable|compute_opts
name|'compute_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'allow_resize_to_same_host'"
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
string|"'Allow destination machine to match source for resize. '"
nl|'\n'
string|"'Useful when testing in single-host environments.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_schedule_zone'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Availability zone to use when user doesn\\'t specify one'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'non_inheritable_image_properties'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'cache_in_nova'"
op|','
nl|'\n'
string|"'bittorrent'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'These are image properties which a snapshot should not'"
nl|'\n'
string|"' inherit from an instance'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'null_kernel'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nokernel'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Kernel image that indicates not to use a kernel, but to '"
nl|'\n'
string|"'use a raw disk image instead'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'multi_instance_display_name_template'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'%(name)s-%(count)d'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'When creating multiple instances with a single request '"
nl|'\n'
string|"'using the os-multiple-create API extension, this '"
nl|'\n'
string|"'template will be used to build the display name for '"
nl|'\n'
string|"'each instance. The benefit is that the instances '"
nl|'\n'
string|"'end up with different hostnames. To restore legacy '"
nl|'\n'
string|"'behavior of every instance having the same name, set '"
nl|'\n'
string|'\'this option to "%(name)s".  Valid keys for the \''
nl|'\n'
string|"'template are: name, uuid, count.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'max_local_block_devices'"
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
string|"'Maximum number of devices that will result '"
nl|'\n'
string|"'in a local image being created on the hypervisor node. '"
nl|'\n'
string|"'A negative number means unlimited. Setting '"
nl|'\n'
string|"'max_local_block_devices to 0 means that any request that '"
nl|'\n'
string|"'attempts to create a local disk will fail. This option '"
nl|'\n'
string|"'is meant to limit the number of local discs (so root '"
nl|'\n'
string|"'local disc that is the result of --image being used, and '"
nl|'\n'
string|"'any other ephemeral and swap disks). 0 does not mean '"
nl|'\n'
string|"'that images will be automatically converted to volumes '"
nl|'\n'
string|"'and boot instances from volumes - it just means that all '"
nl|'\n'
string|"'requests that attempt to create a local disk will fail.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|"'compute_available_monitors'"
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
string|"'Monitor classes available to the compute which may '"
nl|'\n'
string|"'be specified more than once. This option is '"
nl|'\n'
string|"'DEPRECATED and no longer used. Use setuptools entry '"
nl|'\n'
string|"'points to list available monitor plugins.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'compute_monitors'"
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
string|"'A list of monitors that can be used for getting '"
nl|'\n'
string|"'compute metrics. You can use the alias/name from '"
nl|'\n'
string|"'the setuptools entry points for nova.compute.monitors.* '"
nl|'\n'
string|'\'namespaces. If no namespace is supplied, the "cpu." \''
nl|'\n'
string|"'namespace is assumed for backwards-compatibility. '"
nl|'\n'
string|"'An example value that would enable both the CPU and '"
nl|'\n'
string|"'NUMA memory bandwidth monitors that used the virt '"
nl|'\n'
string|"'driver variant: '"
nl|'\n'
string|'\'["cpu.virt_driver", "numa_mem_bw.virt_driver"]\''
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|resource_tracker_opts
name|'resource_tracker_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'reserved_host_disk_mb'"
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
string|"'Amount of disk in MB to reserve for the host'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'reserved_host_memory_mb'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'512'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Amount of memory in MB to reserve for the host'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'compute_stats_class'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.compute.stats.Stats'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'DEPRECATED: Class that will manage stats for the '"
nl|'\n'
string|"'local compute host'"
op|','
nl|'\n'
DECL|variable|deprecated_for_removal
name|'deprecated_for_removal'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|allocation_ratio_opts
name|'allocation_ratio_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'cpu_allocation_ratio'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Virtual CPU to physical CPU allocation ratio which affects '"
nl|'\n'
string|"'all CPU filters. This configuration specifies a global ratio '"
nl|'\n'
string|"'for CoreFilter. For AggregateCoreFilter, it will fall back to '"
nl|'\n'
string|"'this configuration value if no per-aggregate setting found. '"
nl|'\n'
string|"'NOTE: This can be set per-compute, or if set to 0.0, the value '"
nl|'\n'
string|"'set on the scheduler node(s) will be used '"
nl|'\n'
string|"'and defaulted to 16.0'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'ram_allocation_ratio'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Virtual ram to physical ram allocation ratio which affects '"
nl|'\n'
string|"'all ram filters. This configuration specifies a global ratio '"
nl|'\n'
string|"'for RamFilter. For AggregateRamFilter, it will fall back to '"
nl|'\n'
string|"'this configuration value if no per-aggregate setting found. '"
nl|'\n'
string|"'NOTE: This can be set per-compute, or if set to 0.0, the value '"
nl|'\n'
string|"'set on the scheduler node(s) will be used '"
nl|'\n'
string|"'and defaulted to 1.5'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'disk_allocation_ratio'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'This is the virtual disk to physical disk allocation ratio used '"
nl|'\n'
string|"'by the disk_filter.py script to determine if a host has '"
nl|'\n'
string|"'sufficient disk space to fit a requested instance. A ratio '"
nl|'\n'
string|"'greater than 1.0 will result in over-subscription of the '"
nl|'\n'
string|"'available physical disk, which can be useful for more '"
nl|'\n'
string|"'efficiently packing instances created with images that do not '"
nl|'\n'
string|"'use the entire virtual disk,such as sparse or compressed '"
nl|'\n'
string|"'images. It can be set to a value between 0.0 and 1.0 in order '"
nl|'\n'
string|"'to preserve a percentage of the disk for uses other than '"
nl|'\n'
string|"'instances.'"
nl|'\n'
string|"'NOTE: This can be set per-compute, or if set to 0.0, the value '"
nl|'\n'
string|"'set on the scheduler node(s) will be used '"
nl|'\n'
string|"'and defaulted to 1.0'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|compute_manager_opts
name|'compute_manager_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'console_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Console proxy host to use to connect '"
nl|'\n'
string|"'to instances on this host.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_access_ip_network_name'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Name of network to use to set access IPs for instances'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'defer_iptables_apply'"
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
string|"'Whether to batch up the application of IPTables rules'"
nl|'\n'
string|"' during a host restart and apply all at the end of the'"
nl|'\n'
string|"' init phase'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'instances_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'paths'
op|'.'
name|'state_path_def'
op|'('
string|"'instances'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Where instances are stored on disk'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'instance_usage_audit'"
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
string|'"Generate periodic compute.instance.exists"'
nl|'\n'
string|'" notifications"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'live_migration_retry_count'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'30'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Number of 1 second retries needed in live_migration"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'resume_guests_state_on_host_boot'"
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
string|"'Whether to start guests that were running before the '"
nl|'\n'
string|"'host rebooted'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'network_allocate_retries'"
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
string|'"Number of times to retry network allocation on failures"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'max_concurrent_builds'"
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
string|"'Maximum number of instance builds to run concurrently'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'max_concurrent_live_migrations'"
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
string|"'Maximum number of live migrations to run concurrently. '"
nl|'\n'
string|"'This limit is enforced to avoid outbound live migrations '"
nl|'\n'
string|"'overwhelming the host/network and causing failures. It '"
nl|'\n'
string|"'is not recommended that you change this unless you are '"
nl|'\n'
string|"'very sure that doing so is safe and stable in your '"
nl|'\n'
string|"'environment.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'block_device_allocate_retries'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of times to retry block device '"
nl|'\n'
string|"'allocation on failures.\\n'"
nl|'\n'
string|"'Starting with Liberty, Cinder can use image volume '"
nl|'\n'
string|"'cache. This may help with block device allocation '"
nl|'\n'
string|"'performance. Look at the cinder '"
nl|'\n'
string|"'image_volume_cache_enabled configuration option.'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|interval_opts
name|'interval_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'bandwidth_poll_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Interval to pull network bandwidth usage info. Not '"
nl|'\n'
string|"'supported on all hypervisors. Set to -1 to disable. '"
nl|'\n'
string|"'Setting this to 0 will run at the default rate.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'sync_power_state_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Interval to sync power states between the database and '"
nl|'\n'
string|"'the hypervisor. Set to -1 to disable. '"
nl|'\n'
string|"'Setting this to 0 will run at the default rate.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"heal_instance_info_cache_interval"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Number of seconds between instance network information "'
nl|'\n'
string|'"cache updates"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'reclaim_instance_interval'"
op|','
nl|'\n'
DECL|variable|min
name|'min'
op|'='
number|'0'
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
string|"'Interval in seconds for reclaiming deleted instances. '"
nl|'\n'
string|"'It takes effect only when value is greater than 0.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'volume_usage_poll_interval'"
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
string|"'Interval in seconds for gathering volume usages'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'shelved_poll_interval'"
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
string|"'Interval in seconds for polling shelved instances to '"
nl|'\n'
string|"'offload. Set to -1 to disable.'"
nl|'\n'
string|"'Setting this to 0 will run at the default rate.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'shelved_offload_time'"
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
string|"'Time in seconds before a shelved instance is eligible '"
nl|'\n'
string|"'for removing from a host. -1 never offload, 0 offload '"
nl|'\n'
string|"'immediately when shelved'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'instance_delete_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'300'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Interval in seconds for retrying failed instance file '"
nl|'\n'
string|"'deletes. Set to -1 to disable. '"
nl|'\n'
string|"'Setting this to 0 will run at the default rate.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'block_device_allocate_retries_interval'"
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
string|"'Waiting time interval (seconds) between block'"
nl|'\n'
string|"' device allocation retries on failures'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'scheduler_instance_sync_interval'"
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
string|"'Waiting time interval (seconds) between sending the '"
nl|'\n'
string|"'scheduler a list of current instance UUIDs to verify '"
nl|'\n'
string|"'that its view of instances is in sync with nova. If the '"
nl|'\n'
string|"'CONF option `scheduler_tracks_instance_changes` is '"
nl|'\n'
string|"'False, changing this option will have no effect.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'update_resources_interval'"
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
string|"'Interval in seconds for updating compute resources. A '"
nl|'\n'
string|"'number less than 0 means to disable the task completely. '"
nl|'\n'
string|"'Leaving this at the default of 0 will cause this to run '"
nl|'\n'
string|"'at the default periodic interval. Setting it to any '"
nl|'\n'
string|"'positive value will cause it to run at approximately '"
nl|'\n'
string|"'that number of seconds.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|timeout_opts
name|'timeout_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"reboot_timeout"'
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
string|'"Automatically hard reboot an instance if it has been "'
nl|'\n'
string|'"stuck in a rebooting state longer than N seconds. "'
nl|'\n'
string|'"Set to 0 to disable."'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"instance_build_timeout"'
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
string|'"Amount of time in seconds an instance can be in BUILD "'
nl|'\n'
string|'"before going into ERROR status. "'
nl|'\n'
string|'"Set to 0 to disable."'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"rescue_timeout"'
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
string|'"Automatically unrescue an instance after N seconds. "'
nl|'\n'
string|'"Set to 0 to disable."'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"resize_confirm_window"'
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
string|'"Automatically confirm resizes after N seconds. "'
nl|'\n'
string|'"Set to 0 to disable."'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"shutdown_timeout"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Total amount of time to wait in seconds for an instance "'
nl|'\n'
string|'"to perform a clean shutdown."'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|running_deleted_opts
name|'running_deleted_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"running_deleted_instance_action"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"reap"'
op|','
nl|'\n'
DECL|variable|choices
name|'choices'
op|'='
op|'('
string|"'noop'"
op|','
string|"'log'"
op|','
string|"'shutdown'"
op|','
string|"'reap'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Action to take if a running deleted instance is detected."'
nl|'\n'
string|'"Set to \'noop\' to take no action."'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"running_deleted_instance_poll_interval"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1800'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Number of seconds to wait between runs of the cleanup "'
nl|'\n'
string|'"task."'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"running_deleted_instance_timeout"'
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
string|'"Number of seconds after being deleted when a running "'
nl|'\n'
string|'"instance should be considered eligible for cleanup."'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|instance_cleaning_opts
name|'instance_cleaning_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'maximum_instance_delete_attempts'"
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
string|"'The number of times to attempt to reap an instance\\'s '"
nl|'\n'
string|"'files.'"
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
name|'compute_opts'
op|','
nl|'\n'
name|'resource_tracker_opts'
op|','
nl|'\n'
name|'allocation_ratio_opts'
op|','
nl|'\n'
name|'compute_manager_opts'
op|','
nl|'\n'
name|'interval_opts'
op|','
nl|'\n'
name|'timeout_opts'
op|','
nl|'\n'
name|'running_deleted_opts'
op|','
nl|'\n'
name|'instance_cleaning_opts'
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
name|'register_opts'
op|'('
name|'ALL_OPTS'
op|')'
newline|'\n'
nl|'\n'
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
string|"'DEFAULT'"
op|':'
name|'ALL_OPTS'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit
