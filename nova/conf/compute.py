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
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
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
name|'compute_opts'
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
name|'compute_opts'
newline|'\n'
dedent|''
endmarker|''
end_unit
