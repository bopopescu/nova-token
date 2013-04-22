begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 IBM Corp.'
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
string|'"""PowerVM Logical Partition (LPAR)\n\nPowerVM LPAR configuration attributes.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'shlex'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'powervm'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|load_from_conf_data
name|'def'
name|'load_from_conf_data'
op|'('
name|'conf_data'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""LPAR configuration data parser.\n\n    The configuration data is a string representation of\n    the attributes of a Logical Partition. The attributes\n    consists of name/value pairs, which are in command separated\n    value format.\n    Example format: name=lpar_name,lpar_id=1,lpar_env=aixlinux\n\n    :param conf_data: string containing the LPAR configuration data.\n    :returns: LPAR -- LPAR object.\n    """'
newline|'\n'
comment|'# config_data can contain comma separated values within'
nl|'\n'
comment|'# double quotes, example: virtual_serial_adapters'
nl|'\n'
comment|"# and virtual_scsi_adapters attributes. So can't simply"
nl|'\n'
comment|"# split them by ','."
nl|'\n'
name|'cf_splitter'
op|'='
name|'shlex'
op|'.'
name|'shlex'
op|'('
name|'conf_data'
op|','
name|'posix'
op|'='
name|'True'
op|')'
newline|'\n'
name|'cf_splitter'
op|'.'
name|'whitespace'
op|'='
string|"','"
newline|'\n'
name|'cf_splitter'
op|'.'
name|'whitespace_split'
op|'='
name|'True'
newline|'\n'
name|'attribs'
op|'='
name|'dict'
op|'('
name|'item'
op|'.'
name|'split'
op|'('
string|'"="'
op|')'
name|'for'
name|'item'
name|'in'
name|'list'
op|'('
name|'cf_splitter'
op|')'
op|')'
newline|'\n'
name|'lpar'
op|'='
name|'LPAR'
op|'('
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'attribs'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'lpar'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'PowerVMLPARAttributeNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Encountered unknown LPAR attribute: %s\\n'"
nl|'\n'
string|"'Continuing without storing'"
op|')'
op|'%'
name|'key'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'lpar'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LPAR
dedent|''
name|'class'
name|'LPAR'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""\n    Simple class representing a logical partition and the attributes\n    for the partition and/or its selected profile.\n    """'
newline|'\n'
nl|'\n'
comment|'# Attributes for all logical partitions'
nl|'\n'
DECL|variable|LPAR_ATTRS
name|'LPAR_ATTRS'
op|'='
op|'('
nl|'\n'
string|"'name'"
op|','
nl|'\n'
string|"'lpar_id'"
op|','
nl|'\n'
string|"'lpar_env'"
op|','
nl|'\n'
string|"'state'"
op|','
nl|'\n'
string|"'resource_config'"
op|','
nl|'\n'
string|"'os_version'"
op|','
nl|'\n'
string|"'logical_serial_num'"
op|','
nl|'\n'
string|"'default_profile'"
op|','
nl|'\n'
string|"'profile_name'"
op|','
nl|'\n'
string|"'curr_profile'"
op|','
nl|'\n'
string|"'work_group_id'"
op|','
nl|'\n'
string|"'allow_perf_collection'"
op|','
nl|'\n'
string|"'power_ctrl_lpar_ids'"
op|','
nl|'\n'
string|"'boot_mode'"
op|','
nl|'\n'
string|"'lpar_keylock'"
op|','
nl|'\n'
string|"'auto_start'"
op|','
nl|'\n'
string|"'uptime'"
op|','
nl|'\n'
string|"'lpar_avail_priority'"
op|','
nl|'\n'
string|"'desired_lpar_proc_compat_mode'"
op|','
nl|'\n'
string|"'curr_lpar_proc_compat_mode'"
op|','
nl|'\n'
string|"'virtual_eth_mac_base_value'"
op|','
nl|'\n'
string|"'rmc_ipaddr'"
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
comment|'# Logical partitions may contain one or more profiles, which'
nl|'\n'
comment|'# may have the following attributes'
nl|'\n'
DECL|variable|LPAR_PROFILE_ATTRS
name|'LPAR_PROFILE_ATTRS'
op|'='
op|'('
nl|'\n'
string|"'name'"
op|','
nl|'\n'
string|"'lpar_name'"
op|','
nl|'\n'
string|"'lpar_id'"
op|','
nl|'\n'
string|"'os_type'"
op|','
nl|'\n'
string|"'all_resources'"
op|','
nl|'\n'
string|"'mem_mode'"
op|','
nl|'\n'
string|"'min_mem'"
op|','
nl|'\n'
string|"'desired_mem'"
op|','
nl|'\n'
string|"'max_mem'"
op|','
nl|'\n'
string|"'proc_mode'"
op|','
nl|'\n'
string|"'min_proc_units'"
op|','
nl|'\n'
string|"'desired_proc_units'"
op|','
nl|'\n'
string|"'max_proc_units'"
op|','
nl|'\n'
string|"'min_procs'"
op|','
nl|'\n'
string|"'desired_procs'"
op|','
nl|'\n'
string|"'max_procs'"
op|','
nl|'\n'
string|"'sharing_mode'"
op|','
nl|'\n'
string|"'uncap_weight'"
op|','
nl|'\n'
string|"'io_slots'"
op|','
nl|'\n'
string|"'lpar_io_pool_ids'"
op|','
nl|'\n'
string|"'max_virtual_slots'"
op|','
nl|'\n'
string|"'virtual_serial_adapters'"
op|','
nl|'\n'
string|"'virtual_scsi_adapters'"
op|','
nl|'\n'
string|"'virtual_eth_adapters'"
op|','
nl|'\n'
string|"'boot_mode'"
op|','
nl|'\n'
string|"'conn_monitoring'"
op|','
nl|'\n'
string|"'auto_start'"
op|','
nl|'\n'
string|"'power_ctrl_lpar_ids'"
op|','
nl|'\n'
string|"'lhea_logical_ports'"
op|','
nl|'\n'
string|"'lhea_capabilities'"
op|','
nl|'\n'
string|"'lpar_proc_compat_mode'"
op|','
nl|'\n'
string|"'virtual_fc_adapters'"
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'attributes'
op|'='
name|'dict'
op|'('
op|'['
name|'k'
op|','
name|'None'
op|']'
name|'for'
name|'k'
name|'in'
name|'self'
op|'.'
name|'LPAR_ATTRS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'profile_attributes'
op|'='
name|'dict'
op|'('
op|'['
name|'k'
op|','
name|'None'
op|']'
name|'for'
name|'k'
nl|'\n'
name|'in'
name|'self'
op|'.'
name|'LPAR_PROFILE_ATTRS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'attributes'
op|'.'
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'profile_attributes'
op|'.'
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'all_attrs'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'attributes'
op|'.'
name|'items'
op|'('
op|')'
nl|'\n'
op|'+'
name|'self'
op|'.'
name|'profile_attributes'
op|'.'
name|'items'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
name|'not'
name|'in'
name|'self'
op|'.'
name|'all_attrs'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PowerVMLPARAttributeNotFound'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'all_attrs'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
name|'not'
name|'in'
name|'self'
op|'.'
name|'all_attrs'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PowerVMLPARAttributeNotFound'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'all_attrs'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
DECL|member|__delitem__
dedent|''
name|'def'
name|'__delitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
name|'not'
name|'in'
name|'self'
op|'.'
name|'all_attrs'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PowerVMLPARAttributeNotFound'
op|'('
name|'key'
op|')'
newline|'\n'
comment|'# We set to None instead of removing the key...'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'all_attrs'
op|'['
name|'key'
op|']'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|to_string
dedent|''
name|'def'
name|'to_string'
op|'('
name|'self'
op|','
name|'exclude_attribs'
op|'='
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conf_data'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'self'
op|'.'
name|'all_attrs'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'in'
name|'exclude_attribs'
name|'or'
name|'value'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'conf_data'
op|'.'
name|'append'
op|'('
string|"'%s=%s'"
op|'%'
op|'('
name|'key'
op|','
name|'value'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
string|"','"
op|'.'
name|'join'
op|'('
name|'conf_data'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
