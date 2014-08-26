begin_unit
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
string|'"""\nException classes and SOAP response error checking module.\n"""'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
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
name|'log'
name|'as'
name|'logging'
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
DECL|variable|ALREADY_EXISTS
name|'ALREADY_EXISTS'
op|'='
string|"'AlreadyExists'"
newline|'\n'
DECL|variable|CANNOT_DELETE_FILE
name|'CANNOT_DELETE_FILE'
op|'='
string|"'CannotDeleteFile'"
newline|'\n'
DECL|variable|FILE_ALREADY_EXISTS
name|'FILE_ALREADY_EXISTS'
op|'='
string|"'FileAlreadyExists'"
newline|'\n'
DECL|variable|FILE_FAULT
name|'FILE_FAULT'
op|'='
string|"'FileFault'"
newline|'\n'
DECL|variable|FILE_LOCKED
name|'FILE_LOCKED'
op|'='
string|"'FileLocked'"
newline|'\n'
DECL|variable|FILE_NOT_FOUND
name|'FILE_NOT_FOUND'
op|'='
string|"'FileNotFound'"
newline|'\n'
DECL|variable|INVALID_POWER_STATE
name|'INVALID_POWER_STATE'
op|'='
string|"'InvalidPowerState'"
newline|'\n'
DECL|variable|INVALID_PROPERTY
name|'INVALID_PROPERTY'
op|'='
string|"'InvalidProperty'"
newline|'\n'
DECL|variable|NO_PERMISSION
name|'NO_PERMISSION'
op|'='
string|"'NoPermission'"
newline|'\n'
DECL|variable|NOT_AUTHENTICATED
name|'NOT_AUTHENTICATED'
op|'='
string|"'NotAuthenticated'"
newline|'\n'
DECL|variable|TASK_IN_PROGRESS
name|'TASK_IN_PROGRESS'
op|'='
string|"'TaskInProgress'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VimException
name|'class'
name|'VimException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The VIM Exception class."""'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
name|'Exception'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'exception_summary'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
comment|'# we need this to protect against developers using'
nl|'\n'
comment|'# this method like VimFaultException'
nl|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"exception_summary must not be a list"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'exception_summary'
op|'='
name|'str'
op|'('
name|'exception_summary'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'exception_obj'
op|'='
name|'excep'
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
name|'self'
op|'.'
name|'exception_summary'
op|'+'
string|'": "'
op|'+'
name|'str'
op|'('
name|'self'
op|'.'
name|'exception_obj'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SessionOverLoadException
dedent|''
dedent|''
name|'class'
name|'SessionOverLoadException'
op|'('
name|'VimException'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Session Overload Exception."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SessionConnectionException
dedent|''
name|'class'
name|'SessionConnectionException'
op|'('
name|'VimException'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Session Connection Exception."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VimAttributeError
dedent|''
name|'class'
name|'VimAttributeError'
op|'('
name|'VimException'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VI Attribute Error."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VimFaultException
dedent|''
name|'class'
name|'VimFaultException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The VIM Fault exception class."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'fault_list'
op|','
name|'fault_string'
op|','
name|'details'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'Exception'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'fault_list'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"fault_list must be a list"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'fault_list'
op|'='
name|'fault_list'
newline|'\n'
name|'self'
op|'.'
name|'fault_string'
op|'='
name|'fault_string'
newline|'\n'
name|'self'
op|'.'
name|'details'
op|'='
name|'details'
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
name|'if'
name|'self'
op|'.'
name|'details'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'%s %s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'fault_string'
op|','
name|'self'
op|'.'
name|'details'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'fault_string'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FaultCheckers
dedent|''
dedent|''
name|'class'
name|'FaultCheckers'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Methods for fault checking of SOAP response. Per Method error handlers\n    for which we desire error checking are defined. SOAP faults are\n    embedded in the SOAP messages as properties and not as SOAP faults.\n    """'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|retrievepropertiesex_fault_checker
name|'def'
name|'retrievepropertiesex_fault_checker'
op|'('
name|'resp_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Checks the RetrievePropertiesEx response for errors. Certain faults\n        are sent as part of the SOAP body as property of missingSet.\n        For example NotAuthenticated fault.\n        """'
newline|'\n'
name|'fault_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'details'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'not'
name|'resp_obj'
op|':'
newline|'\n'
comment|'# This is the case when the session has timed out. ESX SOAP server'
nl|'\n'
comment|'# sends an empty RetrievePropertiesResponse. Normally missingSet in'
nl|'\n'
comment|"# the returnval field has the specifics about the error, but that's"
nl|'\n'
comment|'# not the case with a timed out idle session. It is as bad as a'
nl|'\n'
comment|'# terminated session for we cannot use the session. So setting'
nl|'\n'
comment|'# fault to NotAuthenticated fault.'
nl|'\n'
indent|'            '
name|'fault_list'
op|'='
op|'['
name|'NOT_AUTHENTICATED'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'obj_cont'
name|'in'
name|'resp_obj'
op|'.'
name|'objects'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'hasattr'
op|'('
name|'obj_cont'
op|','
string|'"missingSet"'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'for'
name|'missing_elem'
name|'in'
name|'obj_cont'
op|'.'
name|'missingSet'
op|':'
newline|'\n'
indent|'                        '
name|'fault_type'
op|'='
name|'missing_elem'
op|'.'
name|'fault'
op|'.'
name|'fault'
newline|'\n'
comment|'# Fault needs to be added to the type of fault for'
nl|'\n'
comment|'# uniformity in error checking as SOAP faults define'
nl|'\n'
name|'fault_list'
op|'.'
name|'append'
op|'('
name|'fault_type'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|')'
newline|'\n'
name|'if'
name|'fault_type'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
name|'NO_PERMISSION'
op|':'
newline|'\n'
indent|'                            '
name|'details'
op|'['
string|"'object'"
op|']'
op|'='
name|'fault_type'
op|'.'
name|'object'
op|'.'
name|'value'
newline|'\n'
name|'details'
op|'['
string|"'privilegeId'"
op|']'
op|'='
name|'fault_type'
op|'.'
name|'privilegeId'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'if'
name|'fault_list'
op|':'
newline|'\n'
indent|'            '
name|'exc_msg_list'
op|'='
string|"', '"
op|'.'
name|'join'
op|'('
name|'fault_list'
op|')'
newline|'\n'
name|'fault_string'
op|'='
name|'_'
op|'('
string|'"Error(s) %s occurred in the call to "'
nl|'\n'
string|'"RetrievePropertiesEx"'
op|')'
op|'%'
name|'exc_msg_list'
newline|'\n'
name|'raise'
name|'VimFaultException'
op|'('
name|'fault_list'
op|','
name|'fault_string'
op|','
name|'details'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMwareDriverException
dedent|''
dedent|''
dedent|''
name|'class'
name|'VMwareDriverException'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for all exceptions raised by the VMware Driver.\n\n    All exceptions raised by the VMwareAPI drivers should raise\n    an exception descended from this class as a root. This will\n    allow the driver to potentially trap problems related to its\n    own internal configuration before halting the nova-compute\n    node.\n    """'
newline|'\n'
DECL|variable|msg_fmt
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"VMware Driver fault."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMwareDriverConfigurationException
dedent|''
name|'class'
name|'VMwareDriverConfigurationException'
op|'('
name|'VMwareDriverException'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for all configuration exceptions.\n    """'
newline|'\n'
DECL|variable|msg_fmt
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"VMware Driver configuration fault."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UseLinkedCloneConfigurationFault
dedent|''
name|'class'
name|'UseLinkedCloneConfigurationFault'
op|'('
name|'VMwareDriverConfigurationException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'    '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"No default value for use_linked_clone found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MissingParameter
dedent|''
name|'class'
name|'MissingParameter'
op|'('
name|'VMwareDriverException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'    '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"Missing parameter : %(param)s"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoRootDiskDefined
dedent|''
name|'class'
name|'NoRootDiskDefined'
op|'('
name|'VMwareDriverException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'    '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"No root disk defined."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AlreadyExistsException
dedent|''
name|'class'
name|'AlreadyExistsException'
op|'('
name|'VMwareDriverException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'    '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"Resource already exists."'
op|')'
newline|'\n'
DECL|variable|code
name|'code'
op|'='
number|'409'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CannotDeleteFileException
dedent|''
name|'class'
name|'CannotDeleteFileException'
op|'('
name|'VMwareDriverException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'    '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"Cannot delete file."'
op|')'
newline|'\n'
DECL|variable|code
name|'code'
op|'='
number|'403'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FileAlreadyExistsException
dedent|''
name|'class'
name|'FileAlreadyExistsException'
op|'('
name|'VMwareDriverException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'    '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"File already exists."'
op|')'
newline|'\n'
DECL|variable|code
name|'code'
op|'='
number|'409'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FileFaultException
dedent|''
name|'class'
name|'FileFaultException'
op|'('
name|'VMwareDriverException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'    '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"File fault."'
op|')'
newline|'\n'
DECL|variable|code
name|'code'
op|'='
number|'409'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FileLockedException
dedent|''
name|'class'
name|'FileLockedException'
op|'('
name|'VMwareDriverException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'    '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"File locked."'
op|')'
newline|'\n'
DECL|variable|code
name|'code'
op|'='
number|'403'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FileNotFoundException
dedent|''
name|'class'
name|'FileNotFoundException'
op|'('
name|'VMwareDriverException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'    '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"File not found."'
op|')'
newline|'\n'
DECL|variable|code
name|'code'
op|'='
number|'404'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidPropertyException
dedent|''
name|'class'
name|'InvalidPropertyException'
op|'('
name|'VMwareDriverException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'    '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"Invalid property."'
op|')'
newline|'\n'
DECL|variable|code
name|'code'
op|'='
number|'400'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoPermissionException
dedent|''
name|'class'
name|'NoPermissionException'
op|'('
name|'VMwareDriverException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'    '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"No Permission."'
op|')'
newline|'\n'
DECL|variable|code
name|'code'
op|'='
number|'403'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotAuthenticatedException
dedent|''
name|'class'
name|'NotAuthenticatedException'
op|'('
name|'VMwareDriverException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'    '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"Not Authenticated."'
op|')'
newline|'\n'
DECL|variable|code
name|'code'
op|'='
number|'403'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidPowerStateException
dedent|''
name|'class'
name|'InvalidPowerStateException'
op|'('
name|'VMwareDriverException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'    '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"Invalid Power State."'
op|')'
newline|'\n'
DECL|variable|code
name|'code'
op|'='
number|'409'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TaskInProgress
dedent|''
name|'class'
name|'TaskInProgress'
op|'('
name|'VMwareDriverException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'    '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|'"Virtual machine is busy."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Populate the fault registry with the exceptions that have'
nl|'\n'
comment|'# special treatment.'
nl|'\n'
DECL|variable|_fault_classes_registry
dedent|''
name|'_fault_classes_registry'
op|'='
op|'{'
nl|'\n'
name|'ALREADY_EXISTS'
op|':'
name|'AlreadyExistsException'
op|','
nl|'\n'
name|'CANNOT_DELETE_FILE'
op|':'
name|'CannotDeleteFileException'
op|','
nl|'\n'
name|'FILE_ALREADY_EXISTS'
op|':'
name|'FileAlreadyExistsException'
op|','
nl|'\n'
name|'FILE_FAULT'
op|':'
name|'FileFaultException'
op|','
nl|'\n'
name|'FILE_LOCKED'
op|':'
name|'FileLockedException'
op|','
nl|'\n'
name|'FILE_NOT_FOUND'
op|':'
name|'FileNotFoundException'
op|','
nl|'\n'
name|'INVALID_POWER_STATE'
op|':'
name|'InvalidPowerStateException'
op|','
nl|'\n'
name|'INVALID_PROPERTY'
op|':'
name|'InvalidPropertyException'
op|','
nl|'\n'
name|'NO_PERMISSION'
op|':'
name|'NoPermissionException'
op|','
nl|'\n'
name|'NOT_AUTHENTICATED'
op|':'
name|'NotAuthenticatedException'
op|','
nl|'\n'
name|'TASK_IN_PROGRESS'
op|':'
name|'TaskInProgress'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fault_class
name|'def'
name|'get_fault_class'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get a named subclass of VMwareDriverException."""'
newline|'\n'
name|'name'
op|'='
name|'str'
op|'('
name|'name'
op|')'
newline|'\n'
name|'fault_class'
op|'='
name|'_fault_classes_registry'
op|'.'
name|'get'
op|'('
name|'name'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'fault_class'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Fault %s not matched.'"
op|')'
op|','
name|'name'
op|')'
newline|'\n'
name|'fault_class'
op|'='
name|'VMwareDriverException'
newline|'\n'
dedent|''
name|'return'
name|'fault_class'
newline|'\n'
dedent|''
endmarker|''
end_unit
