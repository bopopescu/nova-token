begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright (c) 2013 dotCloud, Inc.'
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
string|'"""\nA Docker Hypervisor which allows running Linux Containers instead of VMs.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
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
name|'flavors'
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
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'units'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
name|'import'
name|'hostinfo'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|docker_opts
name|'docker_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'registry_default_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'5042'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Default TCP port to find the '"
nl|'\n'
string|"'docker-registry container'"
op|')'
op|','
nl|'\n'
DECL|variable|deprecated_group
name|'deprecated_group'
op|'='
string|"'DEFAULT'"
op|','
nl|'\n'
DECL|variable|deprecated_name
name|'deprecated_name'
op|'='
string|"'docker_registry_default_port'"
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
name|'docker_opts'
op|','
string|"'docker'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'my_ip'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'log'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DockerDriver
name|'class'
name|'DockerDriver'
op|'('
name|'driver'
op|'.'
name|'ComputeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Docker hypervisor driver."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'virtapi'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'DockerDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'virtapi'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_docker'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|docker
name|'def'
name|'docker'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_docker'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_docker'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_docker'
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
indent|'        '
name|'if'
name|'self'
op|'.'
name|'is_daemon_running'
op|'('
op|')'
name|'is'
name|'False'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|"'Docker daemon is not running or '"
nl|'\n'
string|"'is not reachable (check the rights on /var/run/docker.sock)'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_daemon_running
dedent|''
dedent|''
name|'def'
name|'is_daemon_running'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'docker'
op|'.'
name|'list_containers'
op|'('
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'socket'
op|'.'
name|'error'
op|':'
newline|'\n'
comment|"# NOTE(samalba): If the daemon is not running, we'll get a socket"
nl|'\n'
comment|'# error. The list_containers call is safe to call often, there'
nl|'\n'
comment|'# is an internal hard limit in docker if the amount of containers'
nl|'\n'
comment|'# is huge.'
nl|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|list_instances
dedent|''
dedent|''
name|'def'
name|'list_instances'
op|'('
name|'self'
op|','
name|'inspect'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'res'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'container'
name|'in'
name|'self'
op|'.'
name|'docker'
op|'.'
name|'list_containers'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'info'
op|'='
name|'self'
op|'.'
name|'docker'
op|'.'
name|'inspect_container'
op|'('
name|'container'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'inspect'
op|':'
newline|'\n'
indent|'                '
name|'res'
op|'.'
name|'append'
op|'('
name|'info'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'res'
op|'.'
name|'append'
op|'('
name|'info'
op|'['
string|"'Config'"
op|']'
op|'.'
name|'get'
op|'('
string|"'Hostname'"
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'res'
newline|'\n'
nl|'\n'
DECL|member|plug_vifs
dedent|''
name|'def'
name|'plug_vifs'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Plug VIFs into networks."""'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"VIF plugging is not supported by the Docker driver."'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unplug_vifs
dedent|''
name|'def'
name|'unplug_vifs'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unplug VIFs from networks."""'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"VIF unplugging is not supported by the Docker driver."'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|find_container_by_name
dedent|''
name|'def'
name|'find_container_by_name'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'info'
name|'in'
name|'self'
op|'.'
name|'list_instances'
op|'('
name|'inspect'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'info'
op|'['
string|"'Config'"
op|']'
op|'.'
name|'get'
op|'('
string|"'Hostname'"
op|')'
op|'=='
name|'name'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'info'
newline|'\n'
dedent|''
dedent|''
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'container'
op|'='
name|'self'
op|'.'
name|'find_container_by_name'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'container'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'running'
op|'='
name|'container'
op|'['
string|"'State'"
op|']'
op|'.'
name|'get'
op|'('
string|"'Running'"
op|')'
newline|'\n'
name|'info'
op|'='
op|'{'
nl|'\n'
string|"'max_mem'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'mem'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'num_cpu'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'cpu_time'"
op|':'
number|'0'
nl|'\n'
op|'}'
newline|'\n'
name|'info'
op|'['
string|"'state'"
op|']'
op|'='
name|'power_state'
op|'.'
name|'RUNNING'
name|'if'
name|'running'
name|'else'
name|'power_state'
op|'.'
name|'SHUTDOWN'
newline|'\n'
name|'return'
name|'info'
newline|'\n'
nl|'\n'
DECL|member|get_host_stats
dedent|''
name|'def'
name|'get_host_stats'
op|'('
name|'self'
op|','
name|'refresh'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hostname'
op|'='
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
newline|'\n'
name|'memory'
op|'='
name|'hostinfo'
op|'.'
name|'get_memory_usage'
op|'('
op|')'
newline|'\n'
name|'disk'
op|'='
name|'hostinfo'
op|'.'
name|'get_disk_usage'
op|'('
op|')'
newline|'\n'
name|'stats'
op|'='
name|'self'
op|'.'
name|'get_available_resource'
op|'('
name|'hostname'
op|')'
newline|'\n'
name|'stats'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|'='
name|'stats'
op|'['
string|"'hypervisor_hostname'"
op|']'
newline|'\n'
name|'stats'
op|'['
string|"'host_hostname'"
op|']'
op|'='
name|'stats'
op|'['
string|"'hypervisor_hostname'"
op|']'
newline|'\n'
name|'stats'
op|'['
string|"'host_name_label'"
op|']'
op|'='
name|'stats'
op|'['
string|"'hypervisor_hostname'"
op|']'
newline|'\n'
name|'return'
name|'stats'
newline|'\n'
nl|'\n'
DECL|member|get_available_resource
dedent|''
name|'def'
name|'get_available_resource'
op|'('
name|'self'
op|','
name|'nodename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'self'
op|','
string|"'_nodename'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_nodename'
op|'='
name|'nodename'
newline|'\n'
dedent|''
name|'if'
name|'nodename'
op|'!='
name|'self'
op|'.'
name|'_nodename'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Hostname has changed from %(old)s to %(new)s. '"
nl|'\n'
string|"'A restart is required to take effect.'"
nl|'\n'
op|')'
op|'%'
op|'{'
string|"'old'"
op|':'
name|'self'
op|'.'
name|'_nodename'
op|','
nl|'\n'
string|"'new'"
op|':'
name|'nodename'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'memory'
op|'='
name|'hostinfo'
op|'.'
name|'get_memory_usage'
op|'('
op|')'
newline|'\n'
name|'disk'
op|'='
name|'hostinfo'
op|'.'
name|'get_disk_usage'
op|'('
op|')'
newline|'\n'
name|'stats'
op|'='
op|'{'
nl|'\n'
string|"'vcpus'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'vcpus_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'memory'
op|'['
string|"'total'"
op|']'
op|'/'
name|'units'
op|'.'
name|'Mi'
op|','
nl|'\n'
string|"'memory_mb_used'"
op|':'
name|'memory'
op|'['
string|"'used'"
op|']'
op|'/'
name|'units'
op|'.'
name|'Mi'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'disk'
op|'['
string|"'total'"
op|']'
op|'/'
name|'units'
op|'.'
name|'Gi'
op|','
nl|'\n'
string|"'local_gb_used'"
op|':'
name|'disk'
op|'['
string|"'used'"
op|']'
op|'/'
name|'units'
op|'.'
name|'Gi'
op|','
nl|'\n'
string|"'disk_available_least'"
op|':'
name|'disk'
op|'['
string|"'available'"
op|']'
op|'/'
name|'units'
op|'.'
name|'Gi'
op|','
nl|'\n'
string|"'hypervisor_type'"
op|':'
string|"'docker'"
op|','
nl|'\n'
string|"'hypervisor_version'"
op|':'
name|'utils'
op|'.'
name|'convert_version_to_int'
op|'('
string|"'1.0'"
op|')'
op|','
nl|'\n'
string|"'hypervisor_hostname'"
op|':'
name|'self'
op|'.'
name|'_nodename'
op|','
nl|'\n'
string|"'cpu_info'"
op|':'
string|"'?'"
op|','
nl|'\n'
string|"'supported_instances'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'['
nl|'\n'
op|'('
string|"'i686'"
op|','
string|"'docker'"
op|','
string|"'lxc'"
op|')'
op|','
nl|'\n'
op|'('
string|"'x86_64'"
op|','
string|"'docker'"
op|','
string|"'lxc'"
op|')'
nl|'\n'
op|']'
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'stats'
newline|'\n'
nl|'\n'
DECL|member|_find_container_pid
dedent|''
name|'def'
name|'_find_container_pid'
op|'('
name|'self'
op|','
name|'container_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cgroup_path'
op|'='
name|'hostinfo'
op|'.'
name|'get_cgroup_devices_path'
op|'('
op|')'
newline|'\n'
name|'lxc_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'cgroup_path'
op|','
string|"'lxc'"
op|')'
newline|'\n'
name|'tasks_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'lxc_path'
op|','
name|'container_id'
op|','
string|"'tasks'"
op|')'
newline|'\n'
name|'n'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
comment|'# NOTE(samalba): We wait for the process to be spawned inside the'
nl|'\n'
comment|'# container in order to get the the "container pid". This is'
nl|'\n'
comment|'# usually really fast. To avoid race conditions on a slow'
nl|'\n'
comment|'# machine, we allow 10 seconds as a hard limit.'
nl|'\n'
indent|'            '
name|'if'
name|'n'
op|'>'
number|'20'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'open'
op|'('
name|'tasks_path'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                    '
name|'pids'
op|'='
name|'f'
op|'.'
name|'readlines'
op|'('
op|')'
newline|'\n'
name|'if'
name|'pids'
op|':'
newline|'\n'
indent|'                        '
name|'return'
name|'int'
op|'('
name|'pids'
op|'['
number|'0'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'0.5'
op|')'
newline|'\n'
name|'n'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|_find_fixed_ip
dedent|''
dedent|''
name|'def'
name|'_find_fixed_ip'
op|'('
name|'self'
op|','
name|'subnets'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'subnet'
name|'in'
name|'subnets'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'ip'
name|'in'
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'ip'
op|'['
string|"'type'"
op|']'
op|'=='
string|"'fixed'"
name|'and'
name|'ip'
op|'['
string|"'address'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'ip'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_setup_network
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_setup_network'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'network_info'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'container_id'
op|'='
name|'self'
op|'.'
name|'find_container_by_name'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'container_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'network_info'
op|'='
name|'network_info'
op|'['
number|'0'
op|']'
op|'['
string|"'network'"
op|']'
newline|'\n'
name|'netns_path'
op|'='
string|"'/var/run/netns'"
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'netns_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|"'mkdir'"
op|','
string|"'-p'"
op|','
name|'netns_path'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'nspid'
op|'='
name|'self'
op|'.'
name|'_find_container_pid'
op|'('
name|'container_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'nspid'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'\'Cannot find any PID under container "{0}"\''
op|')'
newline|'\n'
name|'raise'
name|'RuntimeError'
op|'('
name|'msg'
op|'.'
name|'format'
op|'('
name|'container_id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'netns_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'netns_path'
op|','
name|'container_id'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|"'ln'"
op|','
string|"'-sf'"
op|','
string|"'/proc/{0}/ns/net'"
op|'.'
name|'format'
op|'('
name|'nspid'
op|')'
op|','
nl|'\n'
string|"'/var/run/netns/{0}'"
op|'.'
name|'format'
op|'('
name|'container_id'
op|')'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'rand'
op|'='
name|'random'
op|'.'
name|'randint'
op|'('
number|'0'
op|','
number|'100000'
op|')'
newline|'\n'
name|'if_local_name'
op|'='
string|"'pvnetl{0}'"
op|'.'
name|'format'
op|'('
name|'rand'
op|')'
newline|'\n'
name|'if_remote_name'
op|'='
string|"'pvnetr{0}'"
op|'.'
name|'format'
op|'('
name|'rand'
op|')'
newline|'\n'
name|'bridge'
op|'='
name|'network_info'
op|'['
string|"'bridge'"
op|']'
newline|'\n'
name|'ip'
op|'='
name|'self'
op|'.'
name|'_find_fixed_ip'
op|'('
name|'network_info'
op|'['
string|"'subnets'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'ip'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|"'Cannot set fixed ip'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'undo_mgr'
op|'='
name|'utils'
op|'.'
name|'UndoManager'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|"'ip'"
op|','
string|"'link'"
op|','
string|"'add'"
op|','
string|"'name'"
op|','
name|'if_local_name'
op|','
string|"'type'"
op|','
nl|'\n'
string|"'veth'"
op|','
string|"'peer'"
op|','
string|"'name'"
op|','
name|'if_remote_name'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'undo_mgr'
op|'.'
name|'undo_with'
op|'('
name|'lambda'
op|':'
name|'utils'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|"'ip'"
op|','
string|"'link'"
op|','
string|"'delete'"
op|','
name|'if_local_name'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
comment|'# NOTE(samalba): Deleting the interface will delete all associated'
nl|'\n'
comment|'# resources (remove from the bridge, its pair, etc...)'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|"'brctl'"
op|','
string|"'addif'"
op|','
name|'bridge'
op|','
name|'if_local_name'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|"'ip'"
op|','
string|"'link'"
op|','
string|"'set'"
op|','
name|'if_local_name'
op|','
string|"'up'"
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|"'ip'"
op|','
string|"'link'"
op|','
string|"'set'"
op|','
name|'if_remote_name'
op|','
string|"'netns'"
op|','
name|'nspid'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|"'ip'"
op|','
string|"'netns'"
op|','
string|"'exec'"
op|','
name|'container_id'
op|','
string|"'ifconfig'"
op|','
nl|'\n'
name|'if_remote_name'
op|','
name|'ip'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Failed to setup the network, rolling back'"
op|')'
newline|'\n'
name|'undo_mgr'
op|'.'
name|'rollback_and_reraise'
op|'('
name|'msg'
op|'='
name|'msg'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_memory_limit_bytes
dedent|''
dedent|''
name|'def'
name|'_get_memory_limit_bytes'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'system_meta'
op|'='
name|'utils'
op|'.'
name|'instance_sys_meta'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'system_meta'
op|'.'
name|'get'
op|'('
string|"'instance_type_memory_mb'"
op|','
number|'0'
op|')'
op|')'
op|'*'
name|'units'
op|'.'
name|'Mi'
newline|'\n'
nl|'\n'
DECL|member|_get_image_name
dedent|''
name|'def'
name|'_get_image_name'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'image'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fmt'
op|'='
name|'image'
op|'['
string|"'container_format'"
op|']'
newline|'\n'
name|'if'
name|'fmt'
op|'!='
string|"'docker'"
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Image container format not supported ({0})'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InstanceDeployFailure'
op|'('
name|'msg'
op|'.'
name|'format'
op|'('
name|'fmt'
op|')'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'registry_port'
op|'='
name|'self'
op|'.'
name|'_get_registry_port'
op|'('
op|')'
newline|'\n'
name|'return'
string|"'{0}:{1}/{2}'"
op|'.'
name|'format'
op|'('
name|'CONF'
op|'.'
name|'my_ip'
op|','
nl|'\n'
name|'registry_port'
op|','
nl|'\n'
name|'image'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_default_cmd
dedent|''
name|'def'
name|'_get_default_cmd'
op|'('
name|'self'
op|','
name|'image_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'default_cmd'
op|'='
op|'['
string|"'sh'"
op|']'
newline|'\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'docker'
op|'.'
name|'inspect_image'
op|'('
name|'image_name'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'info'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'default_cmd'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'info'
op|'['
string|"'container_config'"
op|']'
op|'['
string|"'Cmd'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'default_cmd'
newline|'\n'
nl|'\n'
DECL|member|spawn
dedent|''
dedent|''
name|'def'
name|'spawn'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'image_meta'
op|','
name|'injected_files'
op|','
nl|'\n'
name|'admin_password'
op|','
name|'network_info'
op|'='
name|'None'
op|','
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_name'
op|'='
name|'self'
op|'.'
name|'_get_image_name'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'image_meta'
op|')'
newline|'\n'
name|'args'
op|'='
op|'{'
nl|'\n'
string|"'Hostname'"
op|':'
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'Image'"
op|':'
name|'image_name'
op|','
nl|'\n'
string|"'Memory'"
op|':'
name|'self'
op|'.'
name|'_get_memory_limit_bytes'
op|'('
name|'instance'
op|')'
op|','
nl|'\n'
string|"'CpuShares'"
op|':'
name|'self'
op|'.'
name|'_get_cpu_shares'
op|'('
name|'instance'
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'default_cmd'
op|'='
name|'self'
op|'.'
name|'_get_default_cmd'
op|'('
name|'image_name'
op|')'
newline|'\n'
name|'if'
name|'default_cmd'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'['
string|"'Cmd'"
op|']'
op|'='
name|'default_cmd'
newline|'\n'
dedent|''
name|'container_id'
op|'='
name|'self'
op|'.'
name|'docker'
op|'.'
name|'create_container'
op|'('
name|'args'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'container_id'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'\'Image name "{0}" does not exist, fetching it...\''
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'msg'
op|'.'
name|'format'
op|'('
name|'image_name'
op|')'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'docker'
op|'.'
name|'pull_repository'
op|'('
name|'image_name'
op|')'
newline|'\n'
name|'if'
name|'res'
name|'is'
name|'False'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InstanceDeployFailure'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Cannot pull missing image'"
op|')'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'container_id'
op|'='
name|'self'
op|'.'
name|'docker'
op|'.'
name|'create_container'
op|'('
name|'args'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'container_id'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InstanceDeployFailure'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Cannot create container'"
op|')'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'docker'
op|'.'
name|'start_container'
op|'('
name|'container_id'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_setup_network'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Cannot setup network: {0}'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InstanceDeployFailure'
op|'('
name|'msg'
op|'.'
name|'format'
op|'('
name|'e'
op|')'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|'='
name|'None'
op|','
nl|'\n'
name|'destroy_disks'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'container_id'
op|'='
name|'self'
op|'.'
name|'find_container_by_name'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'container_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'docker'
op|'.'
name|'stop_container'
op|'('
name|'container_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'docker'
op|'.'
name|'destroy_container'
op|'('
name|'container_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|cleanup
dedent|''
name|'def'
name|'cleanup'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|'='
name|'None'
op|','
nl|'\n'
name|'destroy_disks'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Cleanup after instance being destroyed by Hypervisor."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|reboot
dedent|''
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'reboot_type'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|','
name|'bad_volumes_callback'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'container_id'
op|'='
name|'self'
op|'.'
name|'find_container_by_name'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'container_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'docker'
op|'.'
name|'stop_container'
op|'('
name|'container_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Cannot stop the container, '"
nl|'\n'
string|"'please check docker logs'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'docker'
op|'.'
name|'start_container'
op|'('
name|'container_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Cannot restart the container, '"
nl|'\n'
string|"'please check docker logs'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|power_on
dedent|''
dedent|''
name|'def'
name|'power_on'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'container_id'
op|'='
name|'self'
op|'.'
name|'find_container_by_name'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'container_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'docker'
op|'.'
name|'start_container'
op|'('
name|'container_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|power_off
dedent|''
name|'def'
name|'power_off'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'container_id'
op|'='
name|'self'
op|'.'
name|'find_container_by_name'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'container_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'docker'
op|'.'
name|'stop_container'
op|'('
name|'container_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_console_output
dedent|''
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'container_id'
op|'='
name|'self'
op|'.'
name|'find_container_by_name'
op|'('
name|'instance'
op|'.'
name|'name'
op|')'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'container_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'docker'
op|'.'
name|'get_container_logs'
op|'('
name|'container_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_registry_port
dedent|''
name|'def'
name|'_get_registry_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'default_port'
op|'='
name|'CONF'
op|'.'
name|'docker'
op|'.'
name|'registry_default_port'
newline|'\n'
name|'registry'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'container'
name|'in'
name|'self'
op|'.'
name|'docker'
op|'.'
name|'list_containers'
op|'('
name|'_all'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'container'
op|'='
name|'self'
op|'.'
name|'docker'
op|'.'
name|'inspect_container'
op|'('
name|'container'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'if'
string|"'docker-registry'"
name|'in'
name|'container'
op|'['
string|"'Path'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'registry'
op|'='
name|'container'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'registry'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'default_port'
newline|'\n'
comment|'# NOTE(samalba): The registry service always binds on port 5000 in the'
nl|'\n'
comment|'# container'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'container'
op|'['
string|"'NetworkSettings'"
op|']'
op|'['
string|"'PortMapping'"
op|']'
op|'['
string|"'Tcp'"
op|']'
op|'['
string|"'5000'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'KeyError'
op|','
name|'TypeError'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(samalba): Falling back to a default port allows more'
nl|'\n'
comment|'# flexibility (run docker-registry outside a container)'
nl|'\n'
indent|'            '
name|'return'
name|'default_port'
newline|'\n'
nl|'\n'
DECL|member|snapshot
dedent|''
dedent|''
name|'def'
name|'snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'image_href'
op|','
name|'update_task_state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'container_id'
op|'='
name|'self'
op|'.'
name|'find_container_by_name'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'container_id'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotRunning'
op|'('
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'update_task_state'
op|'('
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'IMAGE_PENDING_UPLOAD'
op|')'
newline|'\n'
op|'('
name|'image_service'
op|','
name|'image_id'
op|')'
op|'='
name|'glance'
op|'.'
name|'get_remote_image_service'
op|'('
nl|'\n'
name|'context'
op|','
name|'image_href'
op|')'
newline|'\n'
name|'image'
op|'='
name|'image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'registry_port'
op|'='
name|'self'
op|'.'
name|'_get_registry_port'
op|'('
op|')'
newline|'\n'
name|'name'
op|'='
name|'image'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'default_tag'
op|'='
op|'('
string|"':'"
name|'not'
name|'in'
name|'name'
op|')'
newline|'\n'
name|'name'
op|'='
string|"'{0}:{1}/{2}'"
op|'.'
name|'format'
op|'('
name|'CONF'
op|'.'
name|'my_ip'
op|','
nl|'\n'
name|'registry_port'
op|','
nl|'\n'
name|'name'
op|')'
newline|'\n'
name|'commit_name'
op|'='
name|'name'
name|'if'
name|'not'
name|'default_tag'
name|'else'
name|'name'
op|'+'
string|"':latest'"
newline|'\n'
name|'self'
op|'.'
name|'docker'
op|'.'
name|'commit_container'
op|'('
name|'container_id'
op|','
name|'commit_name'
op|')'
newline|'\n'
name|'update_task_state'
op|'('
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'IMAGE_UPLOADING'
op|','
nl|'\n'
name|'expected_state'
op|'='
name|'task_states'
op|'.'
name|'IMAGE_PENDING_UPLOAD'
op|')'
newline|'\n'
name|'headers'
op|'='
op|'{'
string|"'X-Meta-Glance-Image-Id'"
op|':'
name|'image_href'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'docker'
op|'.'
name|'push_repository'
op|'('
name|'name'
op|','
name|'headers'
op|'='
name|'headers'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_cpu_shares
dedent|''
name|'def'
name|'_get_cpu_shares'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get allocated CPUs from configured flavor.\n\n        Docker/lxc supports relative CPU allocation.\n\n        cgroups specifies following:\n         /sys/fs/cgroup/lxc/cpu.shares = 1024\n         /sys/fs/cgroup/cpu.shares = 1024\n\n        For that reason we use 1024 as multiplier.\n        This multiplier allows to divide the CPU\n        resources fair with containers started by\n        the user (e.g. docker registry) which has\n        the default CpuShares value of zero.\n        """'
newline|'\n'
name|'flavor'
op|'='
name|'flavors'
op|'.'
name|'extract_flavor'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'flavor'
op|'['
string|"'vcpus'"
op|']'
op|')'
op|'*'
number|'1024'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
