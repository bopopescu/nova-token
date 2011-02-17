begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\r\n'
nl|'\r\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\r\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\r\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\r\n'
comment|'#    a copy of the License at'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\r\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\r\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\r\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\r\n'
comment|'#    under the License.'
nl|'\r\n'
nl|'\r\n'
name|'import'
name|'ZSI'
newline|'\r\n'
name|'import'
name|'httplib'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'VimService_services'
newline|'\r\n'
nl|'\r\n'
DECL|variable|RESP_NOT_XML_ERROR
name|'RESP_NOT_XML_ERROR'
op|'='
string|'\'Response is "text/html", not "text/xml\''
newline|'\r\n'
DECL|variable|CONN_ABORT_ERROR
name|'CONN_ABORT_ERROR'
op|'='
string|"'Software caused connection abort'"
newline|'\r\n'
DECL|variable|ADDRESS_IN_USE_ERROR
name|'ADDRESS_IN_USE_ERROR'
op|'='
string|"'Address already in use'"
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|VimException
name|'class'
name|'VimException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    The VIM Exception class\r\n    """'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'exception_summary'
op|','
name|'excep'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Initializer\r\n        """'
newline|'\r\n'
name|'Exception'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'exception_summary'
op|'='
name|'exception_summary'
newline|'\r\n'
name|'self'
op|'.'
name|'exception_obj'
op|'='
name|'excep'
newline|'\r\n'
nl|'\r\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        The informal string representation of the object\r\n        """'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'exception_summary'
op|'+'
name|'str'
op|'('
name|'self'
op|'.'
name|'exception_obj'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|SessionOverLoadException
dedent|''
dedent|''
name|'class'
name|'SessionOverLoadException'
op|'('
name|'VimException'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Session Overload Exception\r\n    """'
newline|'\r\n'
name|'pass'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|SessionFaultyException
dedent|''
name|'class'
name|'SessionFaultyException'
op|'('
name|'VimException'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Session Faulty Exception\r\n    """'
newline|'\r\n'
name|'pass'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|VimAttributeError
dedent|''
name|'class'
name|'VimAttributeError'
op|'('
name|'VimException'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Attribute Error\r\n    """'
newline|'\r\n'
name|'pass'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|Vim
dedent|''
name|'class'
name|'Vim'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    The VIM Object\r\n    """'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
nl|'\r\n'
name|'protocol'
op|'='
string|'"https"'
op|','
nl|'\r\n'
name|'host'
op|'='
string|'"localhost"'
op|','
nl|'\r\n'
name|'trace'
op|'='
name|'None'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Initializer\r\n\r\n        protocol: http or https\r\n        host    : ESX IPAddress[:port] or ESX Hostname[:port]\r\n        trace   : File handle (eg. sys.stdout, sys.stderr ,\r\n                    open("file.txt",w), Use it only for debugging\r\n                    SOAP Communication\r\n        Creates the necessary Communication interfaces, Gets the\r\n        ServiceContent for initiating SOAP transactions\r\n        """'
newline|'\r\n'
name|'self'
op|'.'
name|'_protocol'
op|'='
name|'protocol'
newline|'\r\n'
name|'self'
op|'.'
name|'_host_name'
op|'='
name|'host'
newline|'\r\n'
name|'service_locator'
op|'='
name|'VimService_services'
op|'.'
name|'VimServiceLocator'
op|'('
op|')'
newline|'\r\n'
name|'connect_string'
op|'='
string|'"%s://%s/sdk"'
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
newline|'\r\n'
name|'if'
name|'trace'
op|'=='
name|'None'
op|':'
newline|'\r\n'
indent|'            '
name|'self'
op|'.'
name|'proxy'
op|'='
name|'service_locator'
op|'.'
name|'getVimPortType'
op|'('
name|'url'
op|'='
name|'connect_string'
op|')'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'            '
name|'self'
op|'.'
name|'proxy'
op|'='
name|'service_locator'
op|'.'
name|'getVimPortType'
op|'('
name|'url'
op|'='
name|'connect_string'
op|','
nl|'\r\n'
name|'tracefile'
op|'='
name|'trace'
op|')'
newline|'\r\n'
dedent|''
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
newline|'\r\n'
nl|'\r\n'
DECL|member|get_service_content
dedent|''
name|'def'
name|'get_service_content'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Gets the service content object\r\n        """'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'_service_content'
newline|'\r\n'
nl|'\r\n'
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
newline|'\r\n'
indent|'        '
string|'"""\r\n        Makes the API calls and gets the result\r\n        """'
newline|'\r\n'
name|'try'
op|':'
newline|'\r\n'
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
newline|'\r\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\r\n'
nl|'\r\n'
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
newline|'\r\n'
indent|'                '
string|'"""\r\n                   managed_object    : Managed Object Reference or Managed\r\n                                       Object Name\r\n                   **kw              : Keyword arguments of the call\r\n                """'
newline|'\r\n'
comment|'#Dynamic handler for VI SDK Calls'
nl|'\r\n'
name|'response'
op|'='
name|'None'
newline|'\r\n'
name|'try'
op|':'
newline|'\r\n'
indent|'                    '
name|'request_msg'
op|'='
name|'self'
op|'.'
name|'_request_message_builder'
op|'('
name|'attr_name'
op|','
nl|'\r\n'
name|'managed_object'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\r\n'
name|'request'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'proxy'
op|','
name|'attr_name'
op|')'
newline|'\r\n'
name|'response'
op|'='
name|'request'
op|'('
name|'request_msg'
op|')'
newline|'\r\n'
name|'if'
name|'response'
op|'=='
name|'None'
op|':'
newline|'\r\n'
indent|'                        '
name|'return'
name|'None'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'                        '
name|'try'
op|':'
newline|'\r\n'
indent|'                            '
name|'return'
name|'getattr'
op|'('
name|'response'
op|','
string|'"_returnval"'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'AttributeError'
op|','
name|'excep'
op|':'
newline|'\r\n'
indent|'                            '
name|'return'
name|'None'
newline|'\r\n'
dedent|''
dedent|''
dedent|''
name|'except'
name|'AttributeError'
op|','
name|'excep'
op|':'
newline|'\r\n'
indent|'                    '
name|'raise'
name|'VimAttributeError'
op|'('
string|'"No such SOAP method \'%s\'"'
nl|'\r\n'
string|'" provided by VI SDK"'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'ZSI'
op|'.'
name|'FaultException'
op|','
name|'excep'
op|':'
newline|'\r\n'
indent|'                    '
name|'raise'
name|'SessionFaultyException'
op|'('
string|'"<ZSI.FaultException> in"'
nl|'\r\n'
string|'" %s:"'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'ZSI'
op|'.'
name|'EvaluateException'
op|','
name|'excep'
op|':'
newline|'\r\n'
indent|'                    '
name|'raise'
name|'SessionFaultyException'
op|'('
string|'"<ZSI.EvaluateException> in"'
nl|'\r\n'
string|'" %s:"'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\r\n'
dedent|''
name|'except'
op|'('
name|'httplib'
op|'.'
name|'CannotSendRequest'
op|','
nl|'\r\n'
name|'httplib'
op|'.'
name|'ResponseNotReady'
op|','
nl|'\r\n'
name|'httplib'
op|'.'
name|'CannotSendHeader'
op|')'
op|','
name|'excep'
op|':'
newline|'\r\n'
indent|'                    '
name|'raise'
name|'SessionOverLoadException'
op|'('
string|'"httplib errror in"'
nl|'\r\n'
string|'" %s: "'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'excep'
op|':'
newline|'\r\n'
comment|'# Socket errors which need special handling for they'
nl|'\r\n'
comment|'# might be caused by ESX API call overload'
nl|'\r\n'
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
nl|'\r\n'
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
op|':'
newline|'\r\n'
indent|'                        '
name|'raise'
name|'SessionOverLoadException'
op|'('
string|'"Socket error in"'
nl|'\r\n'
string|'" %s: "'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\r\n'
comment|'# Type error that needs special handling for it might be'
nl|'\r\n'
comment|'# caused by ESX host API call overload'
nl|'\r\n'
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
newline|'\r\n'
indent|'                        '
name|'raise'
name|'SessionOverLoadException'
op|'('
string|'"Type error in "'
nl|'\r\n'
string|'" %s: "'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'                        '
name|'raise'
name|'VimException'
op|'('
nl|'\r\n'
string|'"Exception in %s "'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\r\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'vim_request_handler'
newline|'\r\n'
nl|'\r\n'
DECL|member|_request_message_builder
dedent|''
dedent|''
name|'def'
name|'_request_message_builder'
op|'('
name|'self'
op|','
name|'method_name'
op|','
name|'managed_object'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Builds the Request Message\r\n        """'
newline|'\r\n'
comment|'#Request Message Builder'
nl|'\r\n'
name|'request_msg'
op|'='
name|'getattr'
op|'('
name|'VimService_services'
op|','
name|'method_name'
op|'+'
string|'"RequestMsg"'
op|')'
op|'('
op|')'
newline|'\r\n'
name|'element'
op|'='
name|'request_msg'
op|'.'
name|'new__this'
op|'('
name|'managed_object'
op|')'
newline|'\r\n'
name|'if'
name|'type'
op|'('
name|'managed_object'
op|')'
op|'=='
name|'type'
op|'('
string|'""'
op|')'
op|':'
newline|'\r\n'
indent|'            '
name|'element'
op|'.'
name|'set_attribute_type'
op|'('
name|'managed_object'
op|')'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'            '
name|'element'
op|'.'
name|'set_attribute_type'
op|'('
name|'managed_object'
op|'.'
name|'get_attribute_type'
op|'('
op|')'
op|')'
newline|'\r\n'
dedent|''
name|'request_msg'
op|'.'
name|'set_element__this'
op|'('
name|'element'
op|')'
newline|'\r\n'
name|'for'
name|'key'
name|'in'
name|'kwargs'
op|':'
newline|'\r\n'
indent|'            '
name|'getattr'
op|'('
name|'request_msg'
op|','
string|'"set_element_"'
op|'+'
name|'key'
op|')'
op|'('
name|'kwargs'
op|'['
name|'key'
op|']'
op|')'
newline|'\r\n'
dedent|''
name|'return'
name|'request_msg'
newline|'\r\n'
nl|'\r\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        The official string representation\r\n        """'
newline|'\r\n'
name|'return'
string|'"VIM Object"'
newline|'\r\n'
nl|'\r\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        The informal string representation\r\n        """'
newline|'\r\n'
name|'return'
string|'"VIM Object"'
newline|'\r\n'
dedent|''
dedent|''
endmarker|''
end_unit
