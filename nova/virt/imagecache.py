begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
nl|'\n'
DECL|variable|imagecache_opts
name|'imagecache_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
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
string|"'Setting this to 0 will disable, but this will change in '"
nl|'\n'
string|'\'the K release to mean "run at the default rate".\''
op|')'
op|','
nl|'\n'
comment|'# TODO(gilliard): Clean the above message after the K release'
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
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
op|','
nl|'\n'
DECL|variable|deprecated_name
name|'deprecated_name'
op|'='
string|"'base_dir_name'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
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
op|','
nl|'\n'
DECL|variable|deprecated_group
name|'deprecated_group'
op|'='
string|"'libvirt'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
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
op|','
nl|'\n'
DECL|variable|deprecated_group
name|'deprecated_group'
op|'='
string|"'libvirt'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'imagecache_opts'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'host'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageCacheManager
name|'class'
name|'ImageCacheManager'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for the image cache manager.\n\n    This class will provide a generic interface to the image cache manager.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'remove_unused_base_images'
op|'='
name|'CONF'
op|'.'
name|'remove_unused_base_images'
newline|'\n'
name|'self'
op|'.'
name|'resize_states'
op|'='
op|'['
name|'task_states'
op|'.'
name|'RESIZE_PREP'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'RESIZE_MIGRATING'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'RESIZE_MIGRATED'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'RESIZE_FINISH'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_base
dedent|''
name|'def'
name|'_get_base'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the base directory of the cached images."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_list_running_instances
dedent|''
name|'def'
name|'_list_running_instances'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'all_instances'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List running instances (on all compute nodes).\n\n        This method returns a dictionary with the following keys:\n            - used_images\n            - image_popularity\n            - instance_names\n        """'
newline|'\n'
name|'used_images'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'image_popularity'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'instance_names'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'instance'
name|'in'
name|'all_instances'
op|':'
newline|'\n'
comment|'# NOTE(mikal): "instance name" here means "the name of a directory'
nl|'\n'
comment|'# which might contain an instance" and therefore needs to include'
nl|'\n'
comment|'# historical permutations as well as the current one.'
nl|'\n'
indent|'            '
name|'instance_names'
op|'.'
name|'add'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'instance_names'
op|'.'
name|'add'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
op|'('
name|'instance'
op|'['
string|"'task_state'"
op|']'
name|'in'
name|'self'
op|'.'
name|'resize_states'
name|'or'
nl|'\n'
name|'instance'
op|'['
string|"'vm_state'"
op|']'
op|'=='
name|'vm_states'
op|'.'
name|'RESIZED'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'instance_names'
op|'.'
name|'add'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|'+'
string|"'_resize'"
op|')'
newline|'\n'
name|'instance_names'
op|'.'
name|'add'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|'+'
string|"'_resize'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'image_key'
name|'in'
op|'['
string|"'image_ref'"
op|','
string|"'kernel_id'"
op|','
string|"'ramdisk_id'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'image_ref_str'
op|'='
name|'str'
op|'('
name|'instance'
op|'['
name|'image_key'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'local'
op|','
name|'remote'
op|','
name|'insts'
op|'='
name|'used_images'
op|'.'
name|'get'
op|'('
name|'image_ref_str'
op|','
nl|'\n'
op|'('
number|'0'
op|','
number|'0'
op|','
op|'['
op|']'
op|')'
op|')'
newline|'\n'
name|'if'
name|'instance'
op|'['
string|"'host'"
op|']'
op|'=='
name|'CONF'
op|'.'
name|'host'
op|':'
newline|'\n'
indent|'                    '
name|'local'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'remote'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'insts'
op|'.'
name|'append'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'used_images'
op|'['
name|'image_ref_str'
op|']'
op|'='
op|'('
name|'local'
op|','
name|'remote'
op|','
name|'insts'
op|')'
newline|'\n'
nl|'\n'
name|'image_popularity'
op|'.'
name|'setdefault'
op|'('
name|'image_ref_str'
op|','
number|'0'
op|')'
newline|'\n'
name|'image_popularity'
op|'['
name|'image_ref_str'
op|']'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
op|'{'
string|"'used_images'"
op|':'
name|'used_images'
op|','
nl|'\n'
string|"'image_popularity'"
op|':'
name|'image_popularity'
op|','
nl|'\n'
string|"'instance_names'"
op|':'
name|'instance_names'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_list_base_images
dedent|''
name|'def'
name|'_list_base_images'
op|'('
name|'self'
op|','
name|'base_dir'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of the images present in _base.\n\n        This method returns a dictionary with the following keys:\n            - unexplained_images\n            - originals\n        """'
newline|'\n'
name|'return'
op|'{'
string|"'unexplained_images'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'originals'"
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_age_and_verify_cached_images
dedent|''
name|'def'
name|'_age_and_verify_cached_images'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'all_instances'
op|','
name|'base_dir'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ages and verfies cached images."""'
newline|'\n'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'all_instances'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The cache manager.\n\n        This will invoke the cache manager. This will update the cache\n        according to the defined cache management scheme. The information\n        populated in the cached stats will be used for the cache management.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
