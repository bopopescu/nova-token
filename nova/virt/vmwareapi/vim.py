begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""\nClasses for making VMware VI SOAP calls.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'httplib'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'suds'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
DECL|variable|suds
indent|'    '
name|'suds'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'error_util'
newline|'\n'
nl|'\n'
DECL|variable|RESP_NOT_XML_ERROR
name|'RESP_NOT_XML_ERROR'
op|'='
string|'\'Response is "text/html", not "text/xml"\''
newline|'\n'
DECL|variable|CONN_ABORT_ERROR
name|'CONN_ABORT_ERROR'
op|'='
string|"'Software caused connection abort'"
newline|'\n'
DECL|variable|ADDRESS_IN_USE_ERROR
name|'ADDRESS_IN_USE_ERROR'
op|'='
string|"'Address already in use'"
newline|'\n'
nl|'\n'
name|'vmwareapi_wsdl_loc_opt'
op|'='
DECL|variable|vmwareapi_wsdl_loc_opt
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vmwareapi_wsdl_loc'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'VIM Service WSDL Location '"
nl|'\n'
string|"'e.g http://<server>/vimService.wsdl. '"
nl|'\n'
string|"'Due to a bug in vSphere ESX 4.1 default wsdl. '"
nl|'\n'
string|"'Refer readme-vmware to setup'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'add_option'
op|'('
name|'vmwareapi_wsdl_loc_opt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
name|'if'
name|'suds'
op|':'
newline|'\n'
nl|'\n'
DECL|class|VIMMessagePlugin
indent|'    '
name|'class'
name|'VIMMessagePlugin'
op|'('
name|'suds'
op|'.'
name|'plugin'
op|'.'
name|'MessagePlugin'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|addAttributeForValue
indent|'        '
name|'def'
name|'addAttributeForValue'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
comment|'# suds does not handle AnyType properly.'
nl|'\n'
comment|'# VI SDK requires type attribute to be set when AnyType is used'
nl|'\n'
indent|'            '
name|'if'
name|'node'
op|'.'
name|'name'
op|'=='
string|"'value'"
op|':'
newline|'\n'
indent|'                '
name|'node'
op|'.'
name|'set'
op|'('
string|"'xsi:type'"
op|','
string|"'xsd:string'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|marshalled
dedent|''
dedent|''
name|'def'
name|'marshalled'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""suds will send the specified soap envelope.\n            Provides the plugin with the opportunity to prune empty\n            nodes and fixup nodes before sending it to the server.\n            """'
newline|'\n'
comment|'# suds builds the entire request object based on the wsdl schema.'
nl|'\n'
comment|'# VI SDK throws server errors if optional SOAP nodes are sent'
nl|'\n'
comment|'# without values, e.g. <test/> as opposed to <test>test</test>'
nl|'\n'
name|'context'
op|'.'
name|'envelope'
op|'.'
name|'prune'
op|'('
op|')'
newline|'\n'
name|'context'
op|'.'
name|'envelope'
op|'.'
name|'walk'
op|'('
name|'self'
op|'.'
name|'addAttributeForValue'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Vim
dedent|''
dedent|''
dedent|''
name|'class'
name|'Vim'
op|':'
newline|'\n'
indent|'    '
string|'"""The VIM Object."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
nl|'\n'
name|'protocol'
op|'='
string|'"https"'
op|','
nl|'\n'
name|'host'
op|'='
string|'"localhost"'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Creates the necessary Communication interfaces and gets the\n        ServiceContent for initiating SOAP transactions.\n\n        protocol: http or https\n        host    : ESX IPAddress[:port] or ESX Hostname[:port]\n        """'
newline|'\n'
name|'if'
name|'not'
name|'suds'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Unable to import suds."'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_protocol'
op|'='
name|'protocol'
newline|'\n'
name|'self'
op|'.'
name|'_host_name'
op|'='
name|'host'
newline|'\n'
name|'wsdl_url'
op|'='
name|'FLAGS'
op|'.'
name|'vmwareapi_wsdl_loc'
newline|'\n'
name|'if'
name|'wsdl_url'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Must specify vmwareapi_wsdl_loc"'
op|')'
op|')'
newline|'\n'
comment|'# TODO(sateesh): Use this when VMware fixes their faulty wsdl'
nl|'\n'
comment|"#wsdl_url = '%s://%s/sdk/vimService.wsdl' % (self._protocol,"
nl|'\n'
comment|'#        self._host_name)'
nl|'\n'
dedent|''
name|'url'
op|'='
string|"'%s://%s/sdk'"
op|'%'
op|'('
name|'self'
op|'.'
name|'_protocol'
op|','
name|'self'
op|'.'
name|'_host_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'suds'
op|'.'
name|'client'
op|'.'
name|'Client'
op|'('
name|'wsdl_url'
op|','
name|'location'
op|'='
name|'url'
op|','
nl|'\n'
name|'plugins'
op|'='
op|'['
name|'VIMMessagePlugin'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_service_content'
op|'='
name|'self'
op|'.'
name|'RetrieveServiceContent'
op|'('
string|'"ServiceInstance"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_service_content
dedent|''
name|'def'
name|'get_service_content'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Gets the service content object."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_service_content'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'attr_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes the API calls and gets the result."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'object'
op|'.'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'attr_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
nl|'\n'
DECL|function|vim_request_handler
indent|'            '
name|'def'
name|'vim_request_handler'
op|'('
name|'managed_object'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'                '
string|'"""\n                Builds the SOAP message and parses the response for fault\n                checking and other errors.\n\n                managed_object    : Managed Object Reference or Managed\n                                    Object Name\n                **kwargs          : Keyword arguments of the call\n                """'
newline|'\n'
comment|'# Dynamic handler for VI SDK Calls'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'request_mo'
op|'='
name|'self'
op|'.'
name|'_request_managed_object_builder'
op|'('
name|'managed_object'
op|')'
newline|'\n'
name|'request'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'client'
op|'.'
name|'service'
op|','
name|'attr_name'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'('
name|'request_mo'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
comment|'# To check for the faults that are part of the message body'
nl|'\n'
comment|'# and not returned as Fault object response from the ESX'
nl|'\n'
comment|'# SOAP server'
nl|'\n'
name|'if'
name|'hasattr'
op|'('
name|'error_util'
op|'.'
name|'FaultCheckers'
op|','
nl|'\n'
name|'attr_name'
op|'.'
name|'lower'
op|'('
op|')'
op|'+'
string|'"_fault_checker"'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'fault_checker'
op|'='
name|'getattr'
op|'('
name|'error_util'
op|'.'
name|'FaultCheckers'
op|','
nl|'\n'
name|'attr_name'
op|'.'
name|'lower'
op|'('
op|')'
op|'+'
string|'"_fault_checker"'
op|')'
newline|'\n'
name|'fault_checker'
op|'('
name|'response'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'response'
newline|'\n'
comment|'# Catch the VimFaultException that is raised by the fault'
nl|'\n'
comment|'# check of the SOAP response'
nl|'\n'
dedent|''
name|'except'
name|'error_util'
op|'.'
name|'VimFaultException'
op|','
name|'excep'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
newline|'\n'
dedent|''
name|'except'
name|'suds'
op|'.'
name|'WebFault'
op|','
name|'excep'
op|':'
newline|'\n'
indent|'                    '
name|'doc'
op|'='
name|'excep'
op|'.'
name|'document'
newline|'\n'
name|'detail'
op|'='
name|'doc'
op|'.'
name|'childAtPath'
op|'('
string|'"/Envelope/Body/Fault/detail"'
op|')'
newline|'\n'
name|'fault_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'child'
name|'in'
name|'detail'
op|'.'
name|'getChildren'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'fault_list'
op|'.'
name|'append'
op|'('
name|'child'
op|'.'
name|'get'
op|'('
string|'"type"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'error_util'
op|'.'
name|'VimFaultException'
op|'('
name|'fault_list'
op|','
name|'excep'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|','
name|'excep'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'error_util'
op|'.'
name|'VimAttributeError'
op|'('
name|'_'
op|'('
string|'"No such SOAP method "'
nl|'\n'
string|'"\'%s\' provided by VI SDK"'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'httplib'
op|'.'
name|'CannotSendRequest'
op|','
nl|'\n'
name|'httplib'
op|'.'
name|'ResponseNotReady'
op|','
nl|'\n'
name|'httplib'
op|'.'
name|'CannotSendHeader'
op|')'
op|','
name|'excep'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'error_util'
op|'.'
name|'SessionOverLoadException'
op|'('
name|'_'
op|'('
string|'"httplib "'
nl|'\n'
string|'"error in %s: "'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'excep'
op|':'
newline|'\n'
comment|'# Socket errors which need special handling for they'
nl|'\n'
comment|'# might be caused by ESX API call overload'
nl|'\n'
indent|'                    '
name|'if'
op|'('
name|'str'
op|'('
name|'excep'
op|')'
op|'.'
name|'find'
op|'('
name|'ADDRESS_IN_USE_ERROR'
op|')'
op|'!='
op|'-'
number|'1'
name|'or'
nl|'\n'
name|'str'
op|'('
name|'excep'
op|')'
op|'.'
name|'find'
op|'('
name|'CONN_ABORT_ERROR'
op|')'
op|')'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                        '
name|'raise'
name|'error_util'
op|'.'
name|'SessionOverLoadException'
op|'('
name|'_'
op|'('
string|'"Socket "'
nl|'\n'
string|'"error in %s: "'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\n'
comment|'# Type error that needs special handling for it might be'
nl|'\n'
comment|'# caused by ESX host API call overload'
nl|'\n'
dedent|''
name|'elif'
name|'str'
op|'('
name|'excep'
op|')'
op|'.'
name|'find'
op|'('
name|'RESP_NOT_XML_ERROR'
op|')'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                        '
name|'raise'
name|'error_util'
op|'.'
name|'SessionOverLoadException'
op|'('
name|'_'
op|'('
string|'"Type "'
nl|'\n'
string|'"error in  %s: "'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'raise'
name|'error_util'
op|'.'
name|'VimException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Exception in %s "'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'vim_request_handler'
newline|'\n'
nl|'\n'
DECL|member|_request_managed_object_builder
dedent|''
dedent|''
name|'def'
name|'_request_managed_object_builder'
op|'('
name|'self'
op|','
name|'managed_object'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Builds the request managed object."""'
newline|'\n'
comment|'# Request Managed Object Builder'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'managed_object'
op|','
name|'str'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'mo'
op|'='
name|'suds'
op|'.'
name|'sudsobject'
op|'.'
name|'Property'
op|'('
name|'managed_object'
op|')'
newline|'\n'
name|'mo'
op|'.'
name|'_type'
op|'='
name|'managed_object'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'mo'
op|'='
name|'managed_object'
newline|'\n'
dedent|''
name|'return'
name|'mo'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"VIM Object"'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"VIM Object"'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
