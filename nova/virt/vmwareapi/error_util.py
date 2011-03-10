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
string|'"""\r\nException classes and SOAP response error checking module\r\n"""'
newline|'\r\n'
nl|'\r\n'
DECL|variable|FAULT_NOT_AUTHENTICATED
name|'FAULT_NOT_AUTHENTICATED'
op|'='
string|'"NotAuthenticated"'
newline|'\r\n'
DECL|variable|FAULT_ALREADY_EXISTS
name|'FAULT_ALREADY_EXISTS'
op|'='
string|'"AlreadyExists"'
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
string|'"""The VIM Exception class"""'
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
string|'"""Session Overload Exception"""'
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
string|'"""VI Attribute Error"""'
newline|'\r\n'
name|'pass'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|VimFaultException
dedent|''
name|'class'
name|'VimFaultException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""The VIM Fault exception class"""'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'fault_list'
op|','
name|'excep'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'Exception'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'fault_list'
op|'='
name|'fault_list'
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
name|'return'
name|'str'
op|'('
name|'self'
op|'.'
name|'exception_obj'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|FaultCheckers
dedent|''
dedent|''
name|'class'
name|'FaultCheckers'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Methods for fault checking of SOAP response. Per Method error handlers\r\n    for which we desire error checking are defined. SOAP faults are\r\n    embedded in the SOAP as a property and not as a SOAP fault."""'
newline|'\r\n'
nl|'\r\n'
op|'@'
name|'classmethod'
newline|'\r\n'
DECL|member|retrieveproperties_fault_checker
name|'def'
name|'retrieveproperties_fault_checker'
op|'('
name|'self'
op|','
name|'resp_obj'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Checks the RetrieveProperties response for errors. Certain faults\r\n        are sent as a part of the SOAP body as property of missingSet.\r\n        For example NotAuthenticated fault"""'
newline|'\r\n'
name|'fault_list'
op|'='
op|'['
op|']'
newline|'\r\n'
name|'for'
name|'obj_cont'
name|'in'
name|'resp_obj'
op|':'
newline|'\r\n'
indent|'            '
name|'if'
name|'hasattr'
op|'('
name|'obj_cont'
op|','
string|'"missingSet"'
op|')'
op|':'
newline|'\r\n'
indent|'                '
name|'for'
name|'missing_elem'
name|'in'
name|'obj_cont'
op|'.'
name|'missingSet'
op|':'
newline|'\r\n'
indent|'                    '
name|'fault_type'
op|'='
name|'missing_elem'
op|'.'
name|'fault'
op|'.'
name|'fault'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
newline|'\r\n'
comment|'#Fault needs to be added to the type of fault for'
nl|'\r\n'
comment|'#uniformity in error checking as SOAP faults define'
nl|'\r\n'
name|'fault_list'
op|'.'
name|'append'
op|'('
name|'fault_type'
op|')'
newline|'\r\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'fault_list'
op|':'
newline|'\r\n'
indent|'            '
name|'exc_msg_list'
op|'='
string|"', '"
op|'.'
name|'join'
op|'('
name|'fault_list'
op|')'
newline|'\r\n'
name|'raise'
name|'VimFaultException'
op|'('
name|'fault_list'
op|','
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Error(s) %s "'
nl|'\r\n'
string|'"occurred in the call to RetrieveProperties"'
op|')'
op|'%'
nl|'\r\n'
name|'exc_msg_list'
op|')'
op|')'
newline|'\r\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
