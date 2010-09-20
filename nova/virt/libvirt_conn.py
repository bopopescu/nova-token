begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
string|'"""\nA connection to a hypervisor (e.g. KVM) through libvirt.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'task'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'process'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'disk'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
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
name|'virt'
name|'import'
name|'images'
newline|'\n'
nl|'\n'
DECL|variable|libvirt
name|'libvirt'
op|'='
name|'None'
newline|'\n'
DECL|variable|libxml2
name|'libxml2'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'libvirt_xml_template'"
op|','
nl|'\n'
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'virt/libvirt.qemu.xml.template'"
op|')'
op|','
nl|'\n'
string|"'Libvirt XML Template for QEmu/KVM'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'libvirt_xen_xml_template'"
op|','
nl|'\n'
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'virt/libvirt.xen.xml.template'"
op|')'
op|','
nl|'\n'
string|"'Libvirt XML Template for Xen'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'libvirt_uml_xml_template'"
op|','
nl|'\n'
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'virt/libvirt.uml.xml.template'"
op|')'
op|','
nl|'\n'
string|"'Libvirt XML Template for user-mode-linux'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'injected_network_template'"
op|','
nl|'\n'
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'virt/interfaces.template'"
op|')'
op|','
nl|'\n'
string|"'Template file for injected network'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'libvirt_type'"
op|','
nl|'\n'
string|"'kvm'"
op|','
nl|'\n'
string|"'Libvirt domain type (valid options are: kvm, qemu, uml, xen)'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'libvirt_uri'"
op|','
nl|'\n'
string|"''"
op|','
nl|'\n'
string|"'Override the default libvirt URI (which is dependent'"
nl|'\n'
string|"' on libvirt_type)'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_connection
name|'def'
name|'get_connection'
op|'('
name|'read_only'
op|')'
op|':'
newline|'\n'
comment|"# These are loaded late so that there's no need to install these"
nl|'\n'
comment|'# libraries when not using libvirt.'
nl|'\n'
indent|'    '
name|'global'
name|'libvirt'
newline|'\n'
name|'global'
name|'libxml2'
newline|'\n'
name|'if'
name|'libvirt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'libvirt'
op|'='
name|'__import__'
op|'('
string|"'libvirt'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'libxml2'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'libxml2'
op|'='
name|'__import__'
op|'('
string|"'libxml2'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'LibvirtConnection'
op|'('
name|'read_only'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConnection
dedent|''
name|'class'
name|'LibvirtConnection'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'read_only'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'libvirt_uri'
op|','
name|'template_file'
op|'='
name|'self'
op|'.'
name|'get_uri_and_template'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'libvirt_xml'
op|'='
name|'open'
op|'('
name|'template_file'
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_wrapped_conn'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'read_only'
op|'='
name|'read_only'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|_conn
name|'def'
name|'_conn'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_wrapped_conn'
name|'or'
name|'not'
name|'self'
op|'.'
name|'_test_connection'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Connecting to libvirt: %s'"
op|'%'
name|'self'
op|'.'
name|'libvirt_uri'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_wrapped_conn'
op|'='
name|'self'
op|'.'
name|'_connect'
op|'('
name|'self'
op|'.'
name|'libvirt_uri'
op|','
name|'self'
op|'.'
name|'read_only'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_wrapped_conn'
newline|'\n'
nl|'\n'
DECL|member|_test_connection
dedent|''
name|'def'
name|'_test_connection'
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
name|'_wrapped_conn'
op|'.'
name|'getInfo'
op|'('
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'libvirt'
op|'.'
name|'libvirtError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'get_error_code'
op|'('
op|')'
op|'=='
name|'libvirt'
op|'.'
name|'VIR_ERR_SYSTEM_ERROR'
name|'and'
name|'e'
op|'.'
name|'get_error_domain'
op|'('
op|')'
op|'=='
name|'libvirt'
op|'.'
name|'VIR_FROM_REMOTE'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Connection to libvirt broke'"
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|get_uri_and_template
dedent|''
dedent|''
name|'def'
name|'get_uri_and_template'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'FLAGS'
op|'.'
name|'libvirt_type'
op|'=='
string|"'uml'"
op|':'
newline|'\n'
indent|'            '
name|'uri'
op|'='
name|'FLAGS'
op|'.'
name|'libvirt_uri'
name|'or'
string|"'uml:///system'"
newline|'\n'
name|'template_file'
op|'='
name|'FLAGS'
op|'.'
name|'libvirt_uml_xml_template'
newline|'\n'
dedent|''
name|'elif'
name|'FLAGS'
op|'.'
name|'libvirt_type'
op|'=='
string|"'xen'"
op|':'
newline|'\n'
indent|'            '
name|'uri'
op|'='
name|'FLAGS'
op|'.'
name|'libvirt_uri'
name|'or'
string|"'xen:///'"
newline|'\n'
name|'template_file'
op|'='
name|'FLAGS'
op|'.'
name|'libvirt_xen_xml_template'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'uri'
op|'='
name|'FLAGS'
op|'.'
name|'libvirt_uri'
name|'or'
string|"'qemu:///system'"
newline|'\n'
name|'template_file'
op|'='
name|'FLAGS'
op|'.'
name|'libvirt_xml_template'
newline|'\n'
dedent|''
name|'return'
name|'uri'
op|','
name|'template_file'
newline|'\n'
nl|'\n'
DECL|member|_connect
dedent|''
name|'def'
name|'_connect'
op|'('
name|'self'
op|','
name|'uri'
op|','
name|'read_only'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'auth'
op|'='
op|'['
op|'['
name|'libvirt'
op|'.'
name|'VIR_CRED_AUTHNAME'
op|','
name|'libvirt'
op|'.'
name|'VIR_CRED_NOECHOPROMPT'
op|']'
op|','
nl|'\n'
string|"'root'"
op|','
nl|'\n'
name|'None'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'read_only'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'libvirt'
op|'.'
name|'openReadOnly'
op|'('
name|'uri'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'libvirt'
op|'.'
name|'openAuth'
op|'('
name|'uri'
op|','
name|'auth'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|list_instances
dedent|''
dedent|''
name|'def'
name|'list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByID'
op|'('
name|'x'
op|')'
op|'.'
name|'name'
op|'('
op|')'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'listDomainsID'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'virt_dom'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByName'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'virt_dom'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'_err'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
comment|"# If the instance is already terminated, we're still happy"
nl|'\n'
dedent|''
name|'d'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
name|'_'
op|':'
name|'self'
op|'.'
name|'_cleanup'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
comment|'# FIXME: What does this comment mean?'
nl|'\n'
comment|'# TODO(termie): short-circuit me for tests'
nl|'\n'
comment|"# WE'LL save this for when we do shutdown,"
nl|'\n'
comment|'# instead of destroy - but destroy returns immediately'
nl|'\n'
name|'timer'
op|'='
name|'task'
op|'.'
name|'LoopingCall'
op|'('
name|'f'
op|'='
name|'None'
op|')'
newline|'\n'
DECL|function|_wait_for_shutdown
name|'def'
name|'_wait_for_shutdown'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'state'
op|'='
name|'self'
op|'.'
name|'get_info'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
op|'['
string|"'state'"
op|']'
newline|'\n'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'None'
op|','
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
name|'state'
op|')'
newline|'\n'
name|'if'
name|'state'
op|'=='
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|':'
newline|'\n'
indent|'                    '
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'d'
op|'.'
name|'callback'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'None'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'d'
op|'.'
name|'callback'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'timer'
op|'.'
name|'f'
op|'='
name|'_wait_for_shutdown'
newline|'\n'
name|'timer'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
number|'0.5'
op|','
name|'now'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
DECL|member|_cleanup
dedent|''
name|'def'
name|'_cleanup'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'target'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'instances_path'
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|"'instance %s: deleting instance files %s'"
op|','
nl|'\n'
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
name|'target'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'target'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'target'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|attach_volume
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'device_path'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|'"sudo virsh attach-disk %s %s %s"'
op|'%'
nl|'\n'
op|'('
name|'instance_name'
op|','
nl|'\n'
name|'device_path'
op|','
nl|'\n'
name|'mountpoint'
op|'.'
name|'rpartition'
op|'('
string|"'/dev/'"
op|')'
op|'['
number|'2'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|detach_volume
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): despite the documentation, virsh detach-disk just'
nl|'\n'
comment|'# wants the device name without the leading /dev/'
nl|'\n'
indent|'        '
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|'"sudo virsh detach-disk %s %s"'
op|'%'
nl|'\n'
op|'('
name|'instance_name'
op|','
nl|'\n'
name|'mountpoint'
op|'.'
name|'rpartition'
op|'('
string|"'/dev/'"
op|')'
op|'['
number|'2'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|reboot
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml'
op|'='
name|'self'
op|'.'
name|'to_xml'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByName'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'createXML'
op|'('
name|'xml'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'d'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'timer'
op|'='
name|'task'
op|'.'
name|'LoopingCall'
op|'('
name|'f'
op|'='
name|'None'
op|')'
newline|'\n'
DECL|function|_wait_for_reboot
name|'def'
name|'_wait_for_reboot'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'state'
op|'='
name|'self'
op|'.'
name|'get_info'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
op|'['
string|"'state'"
op|']'
newline|'\n'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'None'
op|','
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
name|'state'
op|')'
newline|'\n'
name|'if'
name|'state'
op|'=='
name|'power_state'
op|'.'
name|'RUNNING'
op|':'
newline|'\n'
indent|'                    '
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'instance %s: rebooted'"
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'d'
op|'.'
name|'callback'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'exn'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'error'
op|'('
string|"'_wait_for_reboot failed: %s'"
op|','
name|'exn'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'None'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'d'
op|'.'
name|'callback'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'timer'
op|'.'
name|'f'
op|'='
name|'_wait_for_reboot'
newline|'\n'
name|'timer'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
number|'0.5'
op|','
name|'now'
op|'='
name|'True'
op|')'
newline|'\n'
name|'yield'
name|'d'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|spawn
name|'def'
name|'spawn'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml'
op|'='
name|'self'
op|'.'
name|'to_xml'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'None'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'NOSTATE'
op|','
nl|'\n'
string|"'launching'"
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_create_image'
op|'('
name|'instance'
op|','
name|'xml'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'createXML'
op|'('
name|'xml'
op|','
number|'0'
op|')'
newline|'\n'
comment|'# TODO(termie): this should actually register'
nl|'\n'
comment|'# a callback to check for successful boot'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"instance %s: is running"'
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'local_d'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'timer'
op|'='
name|'task'
op|'.'
name|'LoopingCall'
op|'('
name|'f'
op|'='
name|'None'
op|')'
newline|'\n'
DECL|function|_wait_for_boot
name|'def'
name|'_wait_for_boot'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'state'
op|'='
name|'self'
op|'.'
name|'get_info'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
op|'['
string|"'state'"
op|']'
newline|'\n'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'None'
op|','
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
name|'state'
op|')'
newline|'\n'
name|'if'
name|'state'
op|'=='
name|'power_state'
op|'.'
name|'RUNNING'
op|':'
newline|'\n'
indent|'                    '
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'instance %s: booted'"
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'local_d'
op|'.'
name|'callback'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'exception'
op|'('
string|"'instance %s: failed to boot'"
op|','
nl|'\n'
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'None'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'local_d'
op|'.'
name|'callback'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'timer'
op|'.'
name|'f'
op|'='
name|'_wait_for_boot'
newline|'\n'
name|'timer'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
number|'0.5'
op|','
name|'now'
op|'='
name|'True'
op|')'
newline|'\n'
name|'yield'
name|'local_d'
newline|'\n'
nl|'\n'
DECL|member|_flush_xen_console
dedent|''
name|'def'
name|'_flush_xen_console'
op|'('
name|'self'
op|','
name|'virsh_output'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'info'
op|'('
string|"'virsh said: %r'"
op|'%'
op|'('
name|'virsh_output'
op|','
op|')'
op|')'
newline|'\n'
name|'virsh_output'
op|'='
name|'virsh_output'
op|'['
number|'0'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'virsh_output'
op|'.'
name|'startswith'
op|'('
string|"'/dev/'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'info'
op|'('
string|"'cool, it\\'s a device'"
op|')'
newline|'\n'
name|'d'
op|'='
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|'"sudo dd if=%s iflag=nonblock"'
op|'%'
name|'virsh_output'
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
name|'r'
op|':'
name|'r'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"''"
newline|'\n'
nl|'\n'
DECL|member|_append_to_file
dedent|''
dedent|''
name|'def'
name|'_append_to_file'
op|'('
name|'self'
op|','
name|'data'
op|','
name|'fpath'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'info'
op|'('
string|"'data: %r, fpath: %r'"
op|'%'
op|'('
name|'data'
op|','
name|'fpath'
op|')'
op|')'
newline|'\n'
name|'fp'
op|'='
name|'open'
op|'('
name|'fpath'
op|','
string|"'a+'"
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
name|'return'
name|'fpath'
newline|'\n'
nl|'\n'
DECL|member|_dump_file
dedent|''
name|'def'
name|'_dump_file'
op|'('
name|'self'
op|','
name|'fpath'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fp'
op|'='
name|'open'
op|'('
name|'fpath'
op|','
string|"'r+'"
op|')'
newline|'\n'
name|'contents'
op|'='
name|'fp'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|"'Contents: %r'"
op|'%'
op|'('
name|'contents'
op|','
op|')'
op|')'
newline|'\n'
name|'return'
name|'contents'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|get_console_output
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'console_log'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'instances_path'
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
string|"'console.log'"
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|"'console_log: %s'"
op|'%'
name|'console_log'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|"'FLAGS.libvirt_type: %s'"
op|'%'
name|'FLAGS'
op|'.'
name|'libvirt_type'
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'libvirt_type'
op|'=='
string|"'xen'"
op|':'
newline|'\n'
comment|'# Xen is spethial'
nl|'\n'
indent|'            '
name|'d'
op|'='
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|'"virsh ttyconsole %s"'
op|'%'
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'_flush_xen_console'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'_append_to_file'
op|','
name|'console_log'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'='
name|'defer'
op|'.'
name|'succeed'
op|'('
name|'console_log'
op|')'
newline|'\n'
dedent|''
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'_dump_file'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_create_image
name|'def'
name|'_create_image'
op|'('
name|'self'
op|','
name|'inst'
op|','
name|'libvirt_xml'
op|')'
op|':'
newline|'\n'
comment|'# syntactic nicety'
nl|'\n'
indent|'        '
name|'basepath'
op|'='
name|'lambda'
name|'fname'
op|'='
string|"''"
op|':'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'instances_path'
op|','
nl|'\n'
name|'inst'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'fname'
op|')'
newline|'\n'
nl|'\n'
comment|'# ensure directories exist and are writable'
nl|'\n'
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|"'mkdir -p %s'"
op|'%'
name|'basepath'
op|'('
op|')'
op|')'
newline|'\n'
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|"'chmod 0777 %s'"
op|'%'
name|'basepath'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(termie): these are blocking calls, it would be great'
nl|'\n'
comment|"#               if they weren't."
nl|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|"'instance %s: Creating image'"
op|','
name|'inst'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'f'
op|'='
name|'open'
op|'('
name|'basepath'
op|'('
string|"'libvirt.xml'"
op|')'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'f'
op|'.'
name|'write'
op|'('
name|'libvirt_xml'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'os'
op|'.'
name|'close'
op|'('
name|'os'
op|'.'
name|'open'
op|'('
name|'basepath'
op|'('
string|"'console.log'"
op|')'
op|','
name|'os'
op|'.'
name|'O_CREAT'
op|'|'
name|'os'
op|'.'
name|'O_WRONLY'
op|','
number|'0660'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'user'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_user'
op|'('
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|')'
newline|'\n'
name|'project'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_project'
op|'('
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'basepath'
op|'('
string|"'disk'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'           '
name|'yield'
name|'images'
op|'.'
name|'fetch'
op|'('
name|'inst'
op|'.'
name|'image_id'
op|','
name|'basepath'
op|'('
string|"'disk-raw'"
op|')'
op|','
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'basepath'
op|'('
string|"'kernel'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'           '
name|'yield'
name|'images'
op|'.'
name|'fetch'
op|'('
name|'inst'
op|'.'
name|'kernel_id'
op|','
name|'basepath'
op|'('
string|"'kernel'"
op|')'
op|','
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'basepath'
op|'('
string|"'ramdisk'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'           '
name|'yield'
name|'images'
op|'.'
name|'fetch'
op|'('
name|'inst'
op|'.'
name|'ramdisk_id'
op|','
name|'basepath'
op|'('
string|"'ramdisk'"
op|')'
op|','
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'execute'
op|'='
name|'lambda'
name|'cmd'
op|','
name|'process_input'
op|'='
name|'None'
op|':'
name|'process'
op|'.'
name|'simple_execute'
op|'('
name|'cmd'
op|'='
name|'cmd'
op|','
nl|'\n'
name|'process_input'
op|'='
name|'process_input'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'key'
op|'='
name|'str'
op|'('
name|'inst'
op|'['
string|"'key_data'"
op|']'
op|')'
newline|'\n'
name|'net'
op|'='
name|'None'
newline|'\n'
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'None'
op|','
name|'project'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'if'
name|'network_ref'
op|'['
string|"'injected'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'address'
op|'='
name|'db'
op|'.'
name|'instance_get_fixed_address'
op|'('
name|'None'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'FLAGS'
op|'.'
name|'injected_network_template'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'net'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
op|'%'
op|'{'
string|"'address'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'network'"
op|':'
name|'network_ref'
op|'['
string|"'network'"
op|']'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'network_ref'
op|'['
string|"'netmask'"
op|']'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'network_ref'
op|'['
string|"'gateway'"
op|']'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'network_ref'
op|'['
string|"'broadcast'"
op|']'
op|','
nl|'\n'
string|"'dns'"
op|':'
name|'network_ref'
op|'['
string|"'dns'"
op|']'
op|'}'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'key'
name|'or'
name|'net'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'info'
op|'('
string|"'instance %s: injecting key into image %s'"
op|','
nl|'\n'
name|'inst'
op|'['
string|"'name'"
op|']'
op|','
name|'inst'
op|'.'
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'net'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'info'
op|'('
string|"'instance %s: injecting net into image %s'"
op|','
nl|'\n'
name|'inst'
op|'['
string|"'name'"
op|']'
op|','
name|'inst'
op|'.'
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'yield'
name|'disk'
op|'.'
name|'inject_data'
op|'('
name|'basepath'
op|'('
string|"'disk-raw'"
op|')'
op|','
name|'key'
op|','
name|'net'
op|','
name|'execute'
op|'='
name|'execute'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'basepath'
op|'('
string|"'disk'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|"'rm -f %s'"
op|'%'
name|'basepath'
op|'('
string|"'disk'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'bytes'
op|'='
op|'('
name|'instance_types'
op|'.'
name|'INSTANCE_TYPES'
op|'['
name|'inst'
op|'.'
name|'instance_type'
op|']'
op|'['
string|"'local_gb'"
op|']'
nl|'\n'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|')'
newline|'\n'
name|'yield'
name|'disk'
op|'.'
name|'partition'
op|'('
nl|'\n'
name|'basepath'
op|'('
string|"'disk-raw'"
op|')'
op|','
name|'basepath'
op|'('
string|"'disk'"
op|')'
op|','
name|'bytes'
op|','
name|'execute'
op|'='
name|'execute'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'libvirt_type'
op|'=='
string|"'uml'"
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|"'sudo chown root %s'"
op|'%'
nl|'\n'
name|'basepath'
op|'('
string|"'disk'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|to_xml
dedent|''
dedent|''
name|'def'
name|'to_xml'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
comment|'# TODO(termie): cache?'
nl|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'instance %s: starting toXML method'"
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'network'
op|'='
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'None'
op|','
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
comment|'# FIXME(vish): stick this in db'
nl|'\n'
name|'instance_type'
op|'='
name|'instance_types'
op|'.'
name|'INSTANCE_TYPES'
op|'['
name|'instance'
op|'['
string|"'instance_type'"
op|']'
op|']'
newline|'\n'
name|'xml_info'
op|'='
op|'{'
string|"'type'"
op|':'
name|'FLAGS'
op|'.'
name|'libvirt_type'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'basepath'"
op|':'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'instances_path'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
op|','
nl|'\n'
string|"'memory_kb'"
op|':'
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
op|'*'
number|'1024'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'instance_type'
op|'['
string|"'vcpus'"
op|']'
op|','
nl|'\n'
string|"'bridge_name'"
op|':'
name|'network'
op|'['
string|"'bridge'"
op|']'
op|','
nl|'\n'
string|"'mac_address'"
op|':'
name|'instance'
op|'['
string|"'mac_address'"
op|']'
op|'}'
newline|'\n'
name|'libvirt_xml'
op|'='
name|'self'
op|'.'
name|'libvirt_xml'
op|'%'
name|'xml_info'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'instance %s: finished toXML method'"
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'libvirt_xml'
newline|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'virt_dom'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByName'
op|'('
name|'instance_name'
op|')'
newline|'\n'
op|'('
name|'state'
op|','
name|'max_mem'
op|','
name|'mem'
op|','
name|'num_cpu'
op|','
name|'cpu_time'
op|')'
op|'='
name|'virt_dom'
op|'.'
name|'info'
op|'('
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'state'"
op|':'
name|'state'
op|','
nl|'\n'
string|"'max_mem'"
op|':'
name|'max_mem'
op|','
nl|'\n'
string|"'mem'"
op|':'
name|'mem'
op|','
nl|'\n'
string|"'num_cpu'"
op|':'
name|'num_cpu'
op|','
nl|'\n'
string|"'cpu_time'"
op|':'
name|'cpu_time'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_disks
dedent|''
name|'def'
name|'get_disks'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Note that this function takes an instance name, not an Instance, so\n        that it can be called by monitor.\n\n        Returns a list of all block devices for this domain.\n        """'
newline|'\n'
name|'domain'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByName'
op|'('
name|'instance_name'
op|')'
newline|'\n'
comment|'# TODO(devcamcar): Replace libxml2 with etree.'
nl|'\n'
name|'xml'
op|'='
name|'domain'
op|'.'
name|'XMLDesc'
op|'('
number|'0'
op|')'
newline|'\n'
name|'doc'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'doc'
op|'='
name|'libxml2'
op|'.'
name|'parseDoc'
op|'('
name|'xml'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'ctx'
op|'='
name|'doc'
op|'.'
name|'xpathNewContext'
op|'('
op|')'
newline|'\n'
name|'disks'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'='
name|'ctx'
op|'.'
name|'xpathEval'
op|'('
string|"'/domain/devices/disk'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'node'
name|'in'
name|'ret'
op|':'
newline|'\n'
indent|'                '
name|'devdst'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'for'
name|'child'
name|'in'
name|'node'
op|'.'
name|'children'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'child'
op|'.'
name|'name'
op|'=='
string|"'target'"
op|':'
newline|'\n'
indent|'                        '
name|'devdst'
op|'='
name|'child'
op|'.'
name|'prop'
op|'('
string|"'dev'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'devdst'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'disks'
op|'.'
name|'append'
op|'('
name|'devdst'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ctx'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'ctx'
op|'.'
name|'xpathFreeContext'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'doc'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'doc'
op|'.'
name|'freeDoc'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'disks'
newline|'\n'
nl|'\n'
DECL|member|get_interfaces
dedent|''
name|'def'
name|'get_interfaces'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Note that this function takes an instance name, not an Instance, so\n        that it can be called by monitor.\n\n        Returns a list of all network interfaces for this instance.\n        """'
newline|'\n'
name|'domain'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByName'
op|'('
name|'instance_name'
op|')'
newline|'\n'
comment|'# TODO(devcamcar): Replace libxml2 with etree.'
nl|'\n'
name|'xml'
op|'='
name|'domain'
op|'.'
name|'XMLDesc'
op|'('
number|'0'
op|')'
newline|'\n'
name|'doc'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'doc'
op|'='
name|'libxml2'
op|'.'
name|'parseDoc'
op|'('
name|'xml'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'ctx'
op|'='
name|'doc'
op|'.'
name|'xpathNewContext'
op|'('
op|')'
newline|'\n'
name|'interfaces'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'='
name|'ctx'
op|'.'
name|'xpathEval'
op|'('
string|"'/domain/devices/interface'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'node'
name|'in'
name|'ret'
op|':'
newline|'\n'
indent|'                '
name|'devdst'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'for'
name|'child'
name|'in'
name|'node'
op|'.'
name|'children'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'child'
op|'.'
name|'name'
op|'=='
string|"'target'"
op|':'
newline|'\n'
indent|'                        '
name|'devdst'
op|'='
name|'child'
op|'.'
name|'prop'
op|'('
string|"'dev'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'devdst'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'interfaces'
op|'.'
name|'append'
op|'('
name|'devdst'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ctx'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'ctx'
op|'.'
name|'xpathFreeContext'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'doc'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'doc'
op|'.'
name|'freeDoc'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'interfaces'
newline|'\n'
nl|'\n'
DECL|member|block_stats
dedent|''
name|'def'
name|'block_stats'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'disk'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Note that this function takes an instance name, not an Instance, so\n        that it can be called by monitor.\n        """'
newline|'\n'
name|'domain'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByName'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'return'
name|'domain'
op|'.'
name|'blockStats'
op|'('
name|'disk'
op|')'
newline|'\n'
nl|'\n'
DECL|member|interface_stats
dedent|''
name|'def'
name|'interface_stats'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Note that this function takes an instance name, not an Instance, so\n        that it can be called by monitor.\n        """'
newline|'\n'
name|'domain'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByName'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'return'
name|'domain'
op|'.'
name|'interfaceStats'
op|'('
name|'interface'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
