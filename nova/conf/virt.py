begin_unit
comment|'# Copyright 2015 Intel Corporation'
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
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'types'
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
DECL|variable|vcpu_pin_set
name|'vcpu_pin_set'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'vcpu_pin_set'"
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Defines which physical CPUs (pCPUs) can be used by instance\nvirtual CPUs (vCPUs).\n\nPossible values:\n\n* A comma-separated list of physical CPU numbers that virtual CPUs can be\n  allocated to by default. Each element should be either a single CPU number,\n  a range of CPU numbers, or a caret followed by a CPU number to be\n  excluded from a previous range. For example:\n\n    vcpu_pin_set = "4-12,^8,15"\n\nServices which consume this:\n\n* ``nova-scheduler``\n* ``nova-compute``\n\nInterdependencies to other options:\n\n* None\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|compute_driver
name|'compute_driver'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'compute_driver'"
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Defines which driver to use for controlling virtualization.\n\nPossible values:\n\n* ``libvirt.LibvirtDriver``\n* ``xenapi.XenAPIDriver``\n* ``fake.FakeDriver``\n* ``ironic.IronicDriver``\n* ``vmwareapi.VMwareVCDriver``\n* ``hyperv.HyperVDriver``\n\nServices which consume this:\n\n* ``nova-compute``\n\nInterdependencies to other options:\n\n* None\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|default_ephemeral_format
name|'default_ephemeral_format'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'default_ephemeral_format'"
op|','
nl|'\n'
name|'help'
op|'='
string|'"""The default format an ephemeral_volume will be formatted\nwith on creation.\n\nPossible values:\n\n* ``ext2``\n* ``ext3``\n* ``ext4``\n* ``xfs``\n* ``ntfs`` (only for Windows guests)\n\nServices which consume this:\n\n* ``nova-compute``\n\nInterdependencies to other options:\n\n* None\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|preallocate_images
name|'preallocate_images'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'preallocate_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'none'"
op|','
nl|'\n'
DECL|variable|choices
name|'choices'
op|'='
op|'('
string|"'none'"
op|','
string|"'space'"
op|')'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""The image preallocation mode to use. Image preallocation allows\nstorage for instance images to be allocated up front when the instance is\ninitially provisioned. This ensures immediate feedback is given if enough\nspace isn\'t available. In addition, it should significantly improve\nperformance on writes to new blocks and may even improve I/O performance to\nprewritten blocks due to reduced fragmentation.\n\nPossible values:\n\n* "none"  => no storage provisioning is done up front\n* "space" => storage is fully allocated at instance start\n\nServices which consume this:\n\n* ``nova-compute``\n\nInterdependencies to other options:\n\n* None\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|use_cow_images
name|'use_cow_images'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|"'use_cow_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Enable use of copy-on-write (cow) images.\n\nQEMU/KVM allow the use of qcow2 as backing files. By disabling this,\nbacking files will not be used.\n\nPossible values:\n\n* True: Enable use of cow images\n* False: Disable use of cow images\n\nServices which consume this:\n\n* ``nova-compute``\n\nInterdependencies to other options:\n\n* None\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|vif_plugging_is_fatal
name|'vif_plugging_is_fatal'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|"'vif_plugging_is_fatal'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Determine if instance should boot or fail on VIF plugging timeout.\n\nNova sends a port update to Neutron after an instance has been scheduled,\nproviding Neutron with the necessary information to finish setup of the port.\nOnce completed, Neutron notifies Nova that it has finished setting up the\nport, at which point Nova resumes the boot of the instance since network\nconnectivity is now supposed to be present. A timeout will occur if the reply\nis not received after a given interval.\n\nThis option determines what Nova does when the VIF plugging timeout event\nhappens. When enabled, the instance will error out. When disabled, the\ninstance will continue to boot on the assumption that the port is ready.\n\nPossible values:\n\n* True: Instances should fail after VIF plugging timeout\n* False: Instances should continue booting after VIF plugging timeout\n\nServices which consume this:\n\n* ``nova-compute``\n\nInterdependencies to other options:\n\n* None\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|vif_plugging_timeout
name|'vif_plugging_timeout'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
nl|'\n'
string|"'vif_plugging_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'300'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Timeout for Neutron VIF plugging event message arrival.\n\nNumber of seconds to wait for Neutron vif plugging events to\narrive before continuing or failing (see \'vif_plugging_is_fatal\'). If this is\nset to zero and \'vif_plugging_is_fatal\' is False, events should not be\nexpected to arrive at all.\n\nPossible values:\n\n* A time interval in seconds\n\nServices which consume this:\n\n* ``nova-compute``\n\nInterdependencies to other options:\n\n* None\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|firewall_driver
name|'firewall_driver'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'firewall_driver'"
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Firewall driver to use with ``nova-network`` service.\n\nThis option only applies when using the ``nova-network`` service. When using\nanother networking services, such as Neutron, this should be to set to the\n``NoopFirewallDriver``.\n\nIf unset (the default), this will default to the hypervisor-specified\ndefault driver.\n\nPossible values:\n\n* nova.virt.firewall.IptablesFirewallDriver\n* nova.virt.firewall.NoopFirewallDriver\n* nova.virt.libvirt.firewall.IptablesFirewallDriver\n* [...]\n\nServices which consume this:\n\n* nova-network\n\nInterdependencies to other options:\n\n* ``use_neutron``: This must be set to ``False`` to enable ``nova-network``\n  networking\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|allow_same_net_traffic
name|'allow_same_net_traffic'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|"'allow_same_net_traffic'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Determine whether to allow network traffic from same network.\n\nWhen set to true, hosts on the same subnet are not filtered and are allowed\nto pass all types of traffic between them. On a flat network, this allows\nall instances from all projects unfiltered communication. With VLAN\nnetworking, this allows access between instances within the same project.\n\nThis option only applies when using the ``nova-network`` service. When using\nanother networking services, such as Neutron, security groups or other\napproaches should be used.\n\nPossible values:\n\n* True: Network traffic should be allowed pass between all instances on the\n  same network, regardless of their tenant and security policies\n* False: Network traffic should not be allowed pass between instances unless\n  it is unblocked in a security group\n\nServices which consume this:\n\n* nova-network\n\nInterdependencies to other options:\n\n* ``use_neutron``: This must be set to ``False`` to enable ``nova-network``\n  networking\n* ``firewall_driver``: This must be set to\n  ``nova.virt.libvirt.firewall.IptablesFirewallDriver`` to ensure the\n  libvirt firewall driver is enabled.\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|force_raw_images
name|'force_raw_images'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|"'force_raw_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Force conversion of backing images to raw format.\n\nPossible values:\n\n* True: Backing image files will be converted to raw image format\n* False: Backing image files will not be converted\n\nServices which consume this:\n\n* nova-compute\n\nInterdependencies to other options:\n\n* ``compute_driver``: Only the libvirt driver uses this option.\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|injected_network_template
name|'injected_network_template'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'injected_network_template'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'paths'
op|'.'
name|'basedir_def'
op|'('
string|"'nova/virt/interfaces.template'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Template file for injected network'"
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(yamahata): ListOpt won't work because the command may include a comma."
nl|'\n'
comment|'# For example:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#     mkfs.ext4 -O dir_index,extent -E stride=8,stripe-width=16'
nl|'\n'
comment|'#       --label %(fs_label)s %(target)s'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# list arguments are comma separated and there is no way to escape such'
nl|'\n'
comment|'# commas.'
nl|'\n'
DECL|variable|virt_mkfs
name|'virt_mkfs'
op|'='
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
nl|'\n'
string|"'virt_mkfs'"
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
string|"'Name of the mkfs commands for ephemeral device. '"
nl|'\n'
string|"'The format is <os_type>=<mkfs command>'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|resize_fs_using_block_device
name|'resize_fs_using_block_device'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|"'resize_fs_using_block_device'"
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
string|"'Attempt to resize the filesystem by accessing the '"
nl|'\n'
string|"'image over a block device. This is done by the host '"
nl|'\n'
string|"'and may not be necessary if the image contains a recent '"
nl|'\n'
string|"'version of cloud-init. Possible mechanisms require '"
nl|'\n'
string|"'the nbd driver (for qcow and raw), or loop (for raw).'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|timeout_nbd
name|'timeout_nbd'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
nl|'\n'
string|"'timeout_nbd'"
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
string|"'Amount of time, in seconds, to wait for NBD '"
nl|'\n'
string|"'device start up.'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|image_cache_manager_interval
name|'image_cache_manager_interval'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
nl|'\n'
string|"'image_cache_manager_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'2400'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of seconds to wait between runs of the image '"
nl|'\n'
string|"'cache manager. Set to -1 to disable. '"
nl|'\n'
string|"'Setting this to 0 will run at the default rate.'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|image_cache_subdirectory_name
name|'image_cache_subdirectory_name'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'image_cache_subdirectory_name'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'_base'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Where cached images are stored under $instances_path. '"
nl|'\n'
string|"'This is NOT the full path - just a folder name. '"
nl|'\n'
string|"'For per-compute-host cached images, set to _base_$my_ip'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|remove_unused_base_images
name|'remove_unused_base_images'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|"'remove_unused_base_images'"
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
string|"'Should unused base images be removed?'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|remove_unused_original_minimum_age_seconds
name|'remove_unused_original_minimum_age_seconds'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
nl|'\n'
string|"'remove_unused_original_minimum_age_seconds'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'('
number|'24'
op|'*'
number|'3600'
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Unused unresized base images younger than this will not '"
nl|'\n'
string|"'be removed'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|pointer_model
name|'pointer_model'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'pointer_model'"
op|','
nl|'\n'
name|'default'
op|'='
name|'None'
op|','
name|'choices'
op|'='
op|'['
name|'None'
op|','
string|"'usbtablet'"
op|']'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Generic property to specify the pointer type.\n\nInput devices allow interaction with a graphical framebuffer. For\nexample to provide a graphic tablet for absolute cursor movement.\n\nPossible values:\n\n* None: Uses relative movement. Mouse connected by PS2\n* usbtablet: Uses absolute movement. Tablet connect by USB\n\nServices which consume this:\n\n* nova-compute\n\nInterdependencies to other options:\n\n* usbtablet must be configured with VNC enabled or SPICE enabled and SPICE\n  agent disabled. When used with libvirt the instance mode should be\n  configured as HVM.\n """'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|reserved_huge_pages
name|'reserved_huge_pages'
op|'='
name|'cfg'
op|'.'
name|'MultiOpt'
op|'('
nl|'\n'
string|'"reserved_huge_pages"'
op|','
nl|'\n'
DECL|variable|item_type
name|'item_type'
op|'='
name|'types'
op|'.'
name|'Dict'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Reserves a number of huge/large memory pages per NUMA host cells\n\nPossible values:\n\n* A list of valid key=value which reflect NUMA node ID, page size\n  (Default unit is KiB) and number of pages to be reserved.\n\n    reserved_huge_pages = node=0,size=2048,count=64\n    reserved_huge_pages = node=1,size=1GB,count=1\n\n  In this example we are reserving on NUMA node 0 64 pages of 2MiB\n  and on NUMA node 1 1 page of 1GiB.\n\nServices which consume this:\n\n* nova-compute\n\nRelated options:\n\n* None"""'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALL_OPTS
name|'ALL_OPTS'
op|'='
op|'['
name|'vcpu_pin_set'
op|','
nl|'\n'
name|'compute_driver'
op|','
nl|'\n'
name|'default_ephemeral_format'
op|','
nl|'\n'
name|'preallocate_images'
op|','
nl|'\n'
name|'use_cow_images'
op|','
nl|'\n'
name|'vif_plugging_is_fatal'
op|','
nl|'\n'
name|'vif_plugging_timeout'
op|','
nl|'\n'
name|'firewall_driver'
op|','
nl|'\n'
name|'allow_same_net_traffic'
op|','
nl|'\n'
name|'force_raw_images'
op|','
nl|'\n'
name|'injected_network_template'
op|','
nl|'\n'
name|'virt_mkfs'
op|','
nl|'\n'
name|'resize_fs_using_block_device'
op|','
nl|'\n'
name|'timeout_nbd'
op|','
nl|'\n'
name|'image_cache_manager_interval'
op|','
nl|'\n'
name|'image_cache_subdirectory_name'
op|','
nl|'\n'
name|'remove_unused_base_images'
op|','
nl|'\n'
name|'remove_unused_original_minimum_age_seconds'
op|','
nl|'\n'
name|'pointer_model'
op|','
nl|'\n'
name|'reserved_huge_pages'
op|']'
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
comment|'# TODO(sfinucan): This should be moved to a virt or hardware group'
nl|'\n'
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
