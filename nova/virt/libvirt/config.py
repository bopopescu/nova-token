begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 Red Hat, Inc.'
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
string|'"""\nConfiguration for libvirt objects.\n\nClasses to represent the configuration of various libvirt objects\nand support conversion to/from XML\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
nl|'\n'
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
DECL|class|LibvirtConfigObject
name|'class'
name|'LibvirtConfigObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'super'
op|'('
name|'LibvirtConfigObject'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'root_name'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"root_name"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ns_prefix'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'ns_prefix'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ns_uri'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'ns_uri'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|'"xml_str"'
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'parse_dom'
op|'('
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"xml_str"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_text_node
dedent|''
dedent|''
name|'def'
name|'_text_node'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'child'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
name|'name'
op|')'
newline|'\n'
name|'child'
op|'.'
name|'text'
op|'='
name|'str'
op|'('
name|'value'
op|')'
newline|'\n'
name|'return'
name|'child'
newline|'\n'
nl|'\n'
DECL|member|format_dom
dedent|''
name|'def'
name|'format_dom'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'ns_uri'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'etree'
op|'.'
name|'Element'
op|'('
name|'self'
op|'.'
name|'root_name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"{"'
op|'+'
name|'self'
op|'.'
name|'ns_uri'
op|'+'
string|'"}"'
op|'+'
name|'self'
op|'.'
name|'root_name'
op|','
nl|'\n'
name|'nsmap'
op|'='
op|'{'
name|'self'
op|'.'
name|'ns_prefix'
op|':'
name|'self'
op|'.'
name|'ns_uri'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|parse_dom
dedent|''
dedent|''
name|'def'
name|'parse_dom'
op|'('
name|'xmldoc'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|to_xml
dedent|''
name|'def'
name|'to_xml'
op|'('
name|'self'
op|','
name|'pretty_print'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'self'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'xml_str'
op|'='
name|'etree'
op|'.'
name|'tostring'
op|'('
name|'root'
op|','
name|'pretty_print'
op|'='
name|'pretty_print'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Generated XML %s "'
op|'%'
op|'('
name|'xml_str'
op|','
op|')'
op|')'
newline|'\n'
name|'return'
name|'xml_str'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestDevice
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestDevice'
op|'('
name|'LibvirtConfigObject'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'super'
op|'('
name|'LibvirtConfigGuestDevice'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestDisk
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestDisk'
op|'('
name|'LibvirtConfigGuestDevice'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'super'
op|'('
name|'LibvirtConfigGuestDisk'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'root_name'
op|'='
string|'"disk"'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'source_type'
op|'='
string|'"file"'
newline|'\n'
name|'self'
op|'.'
name|'source_device'
op|'='
string|'"disk"'
newline|'\n'
name|'self'
op|'.'
name|'driver_name'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'driver_format'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'driver_cache'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'source_path'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'source_protocol'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'source_host'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'target_dev'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'target_path'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'target_bus'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|format_dom
dedent|''
name|'def'
name|'format_dom'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev'
op|'='
name|'super'
op|'('
name|'LibvirtConfigGuestDisk'
op|','
name|'self'
op|')'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'dev'
op|'.'
name|'set'
op|'('
string|'"type"'
op|','
name|'self'
op|'.'
name|'source_type'
op|')'
newline|'\n'
name|'dev'
op|'.'
name|'set'
op|'('
string|'"device"'
op|','
name|'self'
op|'.'
name|'source_device'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'driver_name'
name|'is'
name|'not'
name|'None'
name|'or'
name|'self'
op|'.'
name|'driver_format'
name|'is'
name|'not'
name|'None'
name|'or'
name|'self'
op|'.'
name|'driver_cache'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'drv'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"driver"'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'driver_name'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'drv'
op|'.'
name|'set'
op|'('
string|'"name"'
op|','
name|'self'
op|'.'
name|'driver_name'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'driver_format'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'drv'
op|'.'
name|'set'
op|'('
string|'"type"'
op|','
name|'self'
op|'.'
name|'driver_format'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'driver_cache'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'drv'
op|'.'
name|'set'
op|'('
string|'"cache"'
op|','
name|'self'
op|'.'
name|'driver_cache'
op|')'
newline|'\n'
dedent|''
name|'dev'
op|'.'
name|'append'
op|'('
name|'drv'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'source_type'
op|'=='
string|'"file"'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"source"'
op|','
name|'file'
op|'='
name|'self'
op|'.'
name|'source_path'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'source_type'
op|'=='
string|'"block"'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"source"'
op|','
name|'dev'
op|'='
name|'self'
op|'.'
name|'source_path'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'source_type'
op|'=='
string|'"mount"'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"source"'
op|','
name|'dir'
op|'='
name|'self'
op|'.'
name|'source_path'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'source_type'
op|'=='
string|'"network"'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"source"'
op|','
name|'protocol'
op|'='
name|'self'
op|'.'
name|'source_protocol'
op|','
nl|'\n'
name|'name'
op|'='
name|'self'
op|'.'
name|'source_host'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'source_type'
op|'=='
string|'"mount"'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"target"'
op|','
name|'dir'
op|'='
name|'self'
op|'.'
name|'target_path'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"target"'
op|','
name|'dev'
op|'='
name|'self'
op|'.'
name|'target_dev'
op|','
nl|'\n'
name|'bus'
op|'='
name|'self'
op|'.'
name|'target_bus'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dev'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestFilesys
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestFilesys'
op|'('
name|'LibvirtConfigGuestDevice'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'super'
op|'('
name|'LibvirtConfigGuestFilesys'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'root_name'
op|'='
string|'"filesystem"'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'source_type'
op|'='
string|'"mount"'
newline|'\n'
name|'self'
op|'.'
name|'source_dir'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'target_dir'
op|'='
string|'"/"'
newline|'\n'
nl|'\n'
DECL|member|format_dom
dedent|''
name|'def'
name|'format_dom'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev'
op|'='
name|'super'
op|'('
name|'LibvirtConfigGuestFilesys'
op|','
name|'self'
op|')'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'dev'
op|'.'
name|'set'
op|'('
string|'"type"'
op|','
name|'self'
op|'.'
name|'source_type'
op|')'
newline|'\n'
nl|'\n'
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"source"'
op|','
name|'dir'
op|'='
name|'self'
op|'.'
name|'source_dir'
op|')'
op|')'
newline|'\n'
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"target"'
op|','
name|'dir'
op|'='
name|'self'
op|'.'
name|'target_dir'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'dev'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestInterface
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestInterface'
op|'('
name|'LibvirtConfigGuestDevice'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'super'
op|'('
name|'LibvirtConfigGuestInterface'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
nl|'\n'
name|'root_name'
op|'='
string|'"interface"'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'net_type'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'target_dev'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'model'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'mac_addr'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'script'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'source_dev'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'vporttype'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'vportparams'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'filtername'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'filterparams'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|format_dom
dedent|''
name|'def'
name|'format_dom'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev'
op|'='
name|'super'
op|'('
name|'LibvirtConfigGuestInterface'
op|','
name|'self'
op|')'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'dev'
op|'.'
name|'set'
op|'('
string|'"type"'
op|','
name|'self'
op|'.'
name|'net_type'
op|')'
newline|'\n'
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"mac"'
op|','
name|'address'
op|'='
name|'self'
op|'.'
name|'mac_addr'
op|')'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'model'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"model"'
op|','
name|'type'
op|'='
name|'self'
op|'.'
name|'model'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'net_type'
op|'=='
string|'"ethernet"'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'script'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"script"'
op|','
name|'path'
op|'='
name|'self'
op|'.'
name|'script'
op|')'
op|')'
newline|'\n'
dedent|''
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"target"'
op|','
name|'dev'
op|'='
name|'self'
op|'.'
name|'target_dev'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'net_type'
op|'=='
string|'"direct"'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"source"'
op|','
name|'dev'
op|'='
name|'self'
op|'.'
name|'source_dev'
op|','
nl|'\n'
name|'mode'
op|'='
string|'"private"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"source"'
op|','
name|'bridge'
op|'='
name|'self'
op|'.'
name|'source_dev'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'vporttype'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'vport'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"virtualport"'
op|','
name|'type'
op|'='
name|'self'
op|'.'
name|'vporttype'
op|')'
newline|'\n'
name|'for'
name|'p'
name|'in'
name|'self'
op|'.'
name|'vportparams'
op|':'
newline|'\n'
indent|'                '
name|'param'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"parameters"'
op|')'
newline|'\n'
name|'param'
op|'.'
name|'set'
op|'('
name|'p'
op|'['
string|"'key'"
op|']'
op|','
name|'p'
op|'['
string|"'value'"
op|']'
op|')'
newline|'\n'
name|'vport'
op|'.'
name|'append'
op|'('
name|'param'
op|')'
newline|'\n'
dedent|''
name|'dev'
op|'.'
name|'append'
op|'('
name|'vport'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'filtername'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'filter'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"filterref"'
op|','
name|'filter'
op|'='
name|'self'
op|'.'
name|'filtername'
op|')'
newline|'\n'
name|'for'
name|'p'
name|'in'
name|'self'
op|'.'
name|'filterparams'
op|':'
newline|'\n'
indent|'                '
name|'filter'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"parameter"'
op|','
nl|'\n'
name|'name'
op|'='
name|'p'
op|'['
string|"'key'"
op|']'
op|','
nl|'\n'
name|'value'
op|'='
name|'p'
op|'['
string|"'value'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'dev'
op|'.'
name|'append'
op|'('
name|'filter'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dev'
newline|'\n'
nl|'\n'
DECL|member|add_filter_param
dedent|''
name|'def'
name|'add_filter_param'
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
name|'self'
op|'.'
name|'filterparams'
op|'.'
name|'append'
op|'('
op|'{'
string|"'key'"
op|':'
name|'key'
op|','
string|"'value'"
op|':'
name|'value'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_vport_param
dedent|''
name|'def'
name|'add_vport_param'
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
name|'self'
op|'.'
name|'vportparams'
op|'.'
name|'append'
op|'('
op|'{'
string|"'key'"
op|':'
name|'key'
op|','
string|"'value'"
op|':'
name|'value'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestInput
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestInput'
op|'('
name|'LibvirtConfigGuestDevice'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'super'
op|'('
name|'LibvirtConfigGuestInput'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'root_name'
op|'='
string|'"input"'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'type'
op|'='
string|'"tablet"'
newline|'\n'
name|'self'
op|'.'
name|'bus'
op|'='
string|'"usb"'
newline|'\n'
nl|'\n'
DECL|member|format_dom
dedent|''
name|'def'
name|'format_dom'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev'
op|'='
name|'super'
op|'('
name|'LibvirtConfigGuestInput'
op|','
name|'self'
op|')'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'dev'
op|'.'
name|'set'
op|'('
string|'"type"'
op|','
name|'self'
op|'.'
name|'type'
op|')'
newline|'\n'
name|'dev'
op|'.'
name|'set'
op|'('
string|'"bus"'
op|','
name|'self'
op|'.'
name|'bus'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'dev'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestGraphics
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestGraphics'
op|'('
name|'LibvirtConfigGuestDevice'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'super'
op|'('
name|'LibvirtConfigGuestGraphics'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'root_name'
op|'='
string|'"graphics"'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'type'
op|'='
string|'"vnc"'
newline|'\n'
name|'self'
op|'.'
name|'autoport'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'keymap'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'listen'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|format_dom
dedent|''
name|'def'
name|'format_dom'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev'
op|'='
name|'super'
op|'('
name|'LibvirtConfigGuestGraphics'
op|','
name|'self'
op|')'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'dev'
op|'.'
name|'set'
op|'('
string|'"type"'
op|','
name|'self'
op|'.'
name|'type'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'autoport'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'set'
op|'('
string|'"autoport"'
op|','
string|'"yes"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'set'
op|'('
string|'"autoport"'
op|','
string|'"no"'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'keymap'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'set'
op|'('
string|'"keymap"'
op|','
name|'self'
op|'.'
name|'keymap'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'listen'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'set'
op|'('
string|'"listen"'
op|','
name|'self'
op|'.'
name|'listen'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dev'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestChar
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestChar'
op|'('
name|'LibvirtConfigGuestDevice'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'super'
op|'('
name|'LibvirtConfigGuestChar'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'type'
op|'='
string|'"pty"'
newline|'\n'
name|'self'
op|'.'
name|'source_path'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'target_port'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|format_dom
dedent|''
name|'def'
name|'format_dom'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev'
op|'='
name|'super'
op|'('
name|'LibvirtConfigGuestChar'
op|','
name|'self'
op|')'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'dev'
op|'.'
name|'set'
op|'('
string|'"type"'
op|','
name|'self'
op|'.'
name|'type'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'type'
op|'=='
string|'"file"'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"source"'
op|','
name|'path'
op|'='
name|'self'
op|'.'
name|'source_path'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'target_port'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'dev'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"target"'
op|','
name|'port'
op|'='
name|'str'
op|'('
name|'self'
op|'.'
name|'target_port'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dev'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestSerial
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestSerial'
op|'('
name|'LibvirtConfigGuestChar'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'super'
op|'('
name|'LibvirtConfigGuestSerial'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'root_name'
op|'='
string|'"serial"'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestConsole
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestConsole'
op|'('
name|'LibvirtConfigGuestChar'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'super'
op|'('
name|'LibvirtConfigGuestConsole'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'root_name'
op|'='
string|'"console"'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuest
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuest'
op|'('
name|'LibvirtConfigObject'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'super'
op|'('
name|'LibvirtConfigGuest'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'root_name'
op|'='
string|'"domain"'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'virt_type'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'uuid'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'memory'
op|'='
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'500'
newline|'\n'
name|'self'
op|'.'
name|'vcpus'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'acpi'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'os_type'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'os_kernel'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'os_initrd'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'os_cmdline'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'os_root'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'os_init_path'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'os_boot_dev'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'devices'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|_format_basic_props
dedent|''
name|'def'
name|'_format_basic_props'
op|'('
name|'self'
op|','
name|'root'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_text_node'
op|'('
string|'"uuid"'
op|','
name|'self'
op|'.'
name|'uuid'
op|')'
op|')'
newline|'\n'
name|'root'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_text_node'
op|'('
string|'"name"'
op|','
name|'self'
op|'.'
name|'name'
op|')'
op|')'
newline|'\n'
name|'root'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_text_node'
op|'('
string|'"memory"'
op|','
name|'self'
op|'.'
name|'memory'
op|')'
op|')'
newline|'\n'
name|'root'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_text_node'
op|'('
string|'"vcpu"'
op|','
name|'self'
op|'.'
name|'vcpus'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_format_os
dedent|''
name|'def'
name|'_format_os'
op|'('
name|'self'
op|','
name|'root'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"os"'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_text_node'
op|'('
string|'"type"'
op|','
name|'self'
op|'.'
name|'os_type'
op|')'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'os_kernel'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_text_node'
op|'('
string|'"kernel"'
op|','
name|'self'
op|'.'
name|'os_kernel'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'os_initrd'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_text_node'
op|'('
string|'"initrd"'
op|','
name|'self'
op|'.'
name|'os_initrd'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'os_cmdline'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_text_node'
op|'('
string|'"cmdline"'
op|','
name|'self'
op|'.'
name|'os_cmdline'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'os_root'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_text_node'
op|'('
string|'"root"'
op|','
name|'self'
op|'.'
name|'os_root'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'os_init_path'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_text_node'
op|'('
string|'"init"'
op|','
name|'self'
op|'.'
name|'os_init_path'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'os_boot_dev'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"boot"'
op|','
name|'dev'
op|'='
name|'self'
op|'.'
name|'os_boot_dev'
op|')'
op|')'
newline|'\n'
dedent|''
name|'root'
op|'.'
name|'append'
op|'('
name|'os'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_format_features
dedent|''
name|'def'
name|'_format_features'
op|'('
name|'self'
op|','
name|'root'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'acpi'
op|':'
newline|'\n'
indent|'            '
name|'features'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"features"'
op|')'
newline|'\n'
name|'features'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"acpi"'
op|')'
op|')'
newline|'\n'
name|'root'
op|'.'
name|'append'
op|'('
name|'features'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_format_devices
dedent|''
dedent|''
name|'def'
name|'_format_devices'
op|'('
name|'self'
op|','
name|'root'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'len'
op|'('
name|'self'
op|'.'
name|'devices'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'devices'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"devices"'
op|')'
newline|'\n'
name|'for'
name|'dev'
name|'in'
name|'self'
op|'.'
name|'devices'
op|':'
newline|'\n'
indent|'            '
name|'devices'
op|'.'
name|'append'
op|'('
name|'dev'
op|'.'
name|'format_dom'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'root'
op|'.'
name|'append'
op|'('
name|'devices'
op|')'
newline|'\n'
nl|'\n'
DECL|member|format_dom
dedent|''
name|'def'
name|'format_dom'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'super'
op|'('
name|'LibvirtConfigGuest'
op|','
name|'self'
op|')'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|'"type"'
op|','
name|'self'
op|'.'
name|'virt_type'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_format_basic_props'
op|'('
name|'root'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_format_os'
op|'('
name|'root'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_format_features'
op|'('
name|'root'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_format_devices'
op|'('
name|'root'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'root'
newline|'\n'
nl|'\n'
DECL|member|add_device
dedent|''
name|'def'
name|'add_device'
op|'('
name|'self'
op|','
name|'dev'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'devices'
op|'.'
name|'append'
op|'('
name|'dev'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigCPU
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigCPU'
op|'('
name|'LibvirtConfigObject'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'super'
op|'('
name|'LibvirtConfigCPU'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'root_name'
op|'='
string|'"cpu"'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'arch'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'model'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'vendor'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'sockets'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'cores'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'threads'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'features'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|add_feature
dedent|''
name|'def'
name|'add_feature'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'features'
op|'.'
name|'append'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|format_dom
dedent|''
name|'def'
name|'format_dom'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cpu'
op|'='
name|'super'
op|'('
name|'LibvirtConfigCPU'
op|','
name|'self'
op|')'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'arch'
op|':'
newline|'\n'
indent|'            '
name|'cpu'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_text_node'
op|'('
string|'"arch"'
op|','
name|'self'
op|'.'
name|'arch'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'model'
op|':'
newline|'\n'
indent|'            '
name|'cpu'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_text_node'
op|'('
string|'"model"'
op|','
name|'self'
op|'.'
name|'model'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'vendor'
op|':'
newline|'\n'
indent|'            '
name|'cpu'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_text_node'
op|'('
string|'"vendor"'
op|','
name|'self'
op|'.'
name|'vendor'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'self'
op|'.'
name|'sockets'
name|'is'
name|'not'
name|'None'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'cores'
name|'is'
name|'not'
name|'None'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'threads'
name|'is'
name|'not'
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cpu'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"topology"'
op|','
nl|'\n'
name|'sockets'
op|'='
name|'str'
op|'('
name|'self'
op|'.'
name|'sockets'
op|')'
op|','
nl|'\n'
name|'cores'
op|'='
name|'str'
op|'('
name|'self'
op|'.'
name|'cores'
op|')'
op|','
nl|'\n'
name|'threads'
op|'='
name|'str'
op|'('
name|'self'
op|'.'
name|'threads'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'f'
name|'in'
name|'self'
op|'.'
name|'features'
op|':'
newline|'\n'
indent|'            '
name|'cpu'
op|'.'
name|'append'
op|'('
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"feature"'
op|','
nl|'\n'
name|'name'
op|'='
name|'f'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'cpu'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
