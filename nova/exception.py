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
string|'"""Nova base exception handling.\n\nIncludes decorator for re-raising Nova-type exceptions.\n\nSHOULD include dedicated exception logging.\n\n"""'
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
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.exception'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProcessExecutionError
name|'class'
name|'ProcessExecutionError'
op|'('
name|'IOError'
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
name|'stdout'
op|'='
name|'None'
op|','
name|'stderr'
op|'='
name|'None'
op|','
name|'exit_code'
op|'='
name|'None'
op|','
name|'cmd'
op|'='
name|'None'
op|','
nl|'\n'
name|'description'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'description'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'description'
op|'='
name|'_'
op|'('
string|"'Unexpected error while running command.'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'exit_code'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'exit_code'
op|'='
string|"'-'"
newline|'\n'
dedent|''
name|'message'
op|'='
name|'_'
op|'('
string|"'%(description)s\\nCommand: %(cmd)s\\n'"
nl|'\n'
string|"'Exit code: %(exit_code)s\\nStdout: %(stdout)r\\n'"
nl|'\n'
string|"'Stderr: %(stderr)r'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'IOError'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Error
dedent|''
dedent|''
name|'class'
name|'Error'
op|'('
name|'Exception'
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
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Error'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ApiError
dedent|''
dedent|''
name|'class'
name|'ApiError'
op|'('
name|'Error'
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
name|'message'
op|'='
string|"'Unknown'"
op|','
name|'code'
op|'='
string|"'ApiError'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'message'
op|'='
name|'message'
newline|'\n'
name|'self'
op|'.'
name|'code'
op|'='
name|'code'
newline|'\n'
name|'super'
op|'('
name|'ApiError'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
string|"'%s: %s'"
op|'%'
op|'('
name|'code'
op|','
name|'message'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Duplicate
dedent|''
dedent|''
name|'class'
name|'Duplicate'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotAuthorized
dedent|''
name|'class'
name|'NotAuthorized'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotEmpty
dedent|''
name|'class'
name|'NotEmpty'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidInputException
dedent|''
name|'class'
name|'InvalidInputException'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidContentType
dedent|''
name|'class'
name|'InvalidContentType'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TimeoutException
dedent|''
name|'class'
name|'TimeoutException'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DBError
dedent|''
name|'class'
name|'DBError'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wraps an implementation specific exception."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'inner_exception'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'inner_exception'
op|'='
name|'inner_exception'
newline|'\n'
name|'super'
op|'('
name|'DBError'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'str'
op|'('
name|'inner_exception'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wrap_db_error
dedent|''
dedent|''
name|'def'
name|'wrap_db_error'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
DECL|function|_wrap
indent|'    '
name|'def'
name|'_wrap'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'f'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'DB exception wrapped.'"
op|')'
op|')'
newline|'\n'
name|'raise'
name|'DBError'
op|'('
name|'e'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'_wrap'
newline|'\n'
name|'_wrap'
op|'.'
name|'func_name'
op|'='
name|'f'
op|'.'
name|'func_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wrap_exception
dedent|''
name|'def'
name|'wrap_exception'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
DECL|function|_wrap
indent|'    '
name|'def'
name|'_wrap'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'f'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'e'
op|','
name|'Error'
op|')'
op|':'
newline|'\n'
comment|'#exc_type, exc_value, exc_traceback = sys.exc_info()'
nl|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Uncaught exception'"
op|')'
op|')'
newline|'\n'
comment|'#logging.error(traceback.extract_stack(exc_traceback))'
nl|'\n'
name|'raise'
name|'Error'
op|'('
name|'str'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
dedent|''
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'_wrap'
op|'.'
name|'func_name'
op|'='
name|'f'
op|'.'
name|'func_name'
newline|'\n'
name|'return'
name|'_wrap'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaException
dedent|''
name|'class'
name|'NovaException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base Nova Exception\n\n    To correctly use this class, inherit from it and define\n    a \'message\' property. That message will get printf\'d\n    with the keyword arguments provided to the constructor.\n\n    """'
newline|'\n'
DECL|variable|message
name|'message'
op|'='
name|'_'
op|'('
string|'"An unknown exception occurred."'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_error_string'
op|'='
name|'self'
op|'.'
name|'message'
op|'%'
name|'kwargs'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
comment|'# at least get the core message out if something happened'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_error_string'
op|'='
name|'self'
op|'.'
name|'message'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
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
name|'_error_string'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'#TODO(bcwaldon): EOL this exception!'
nl|'\n'
DECL|class|Invalid
dedent|''
dedent|''
name|'class'
name|'Invalid'
op|'('
name|'NovaException'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceNotRunning
dedent|''
name|'class'
name|'InstanceNotRunning'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Instance %(instance_id)s is not running."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceNotSuspended
dedent|''
name|'class'
name|'InstanceNotSuspended'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Instance %(instance_id)s is not suspended."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceNotInRescueMode
dedent|''
name|'class'
name|'InstanceNotInRescueMode'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Instance %(instance_id)s is not in rescue mode"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceSuspendFailure
dedent|''
name|'class'
name|'InstanceSuspendFailure'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Failed to suspend instance"'
op|')'
op|'+'
string|'": %(reason)s"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceResumeFailure
dedent|''
name|'class'
name|'InstanceResumeFailure'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Failed to resume server"'
op|')'
op|'+'
string|'": %(reason)s."'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceRebootFailure
dedent|''
name|'class'
name|'InstanceRebootFailure'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Failed to reboot instance"'
op|')'
op|'+'
string|'": %(reason)s"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceUnavailable
dedent|''
name|'class'
name|'ServiceUnavailable'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Service is unavailable at this time."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeServiceUnavailable
dedent|''
name|'class'
name|'VolumeServiceUnavailable'
op|'('
name|'ServiceUnavailable'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Volume service is unavailable at this time."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeServiceUnavailable
dedent|''
name|'class'
name|'ComputeServiceUnavailable'
op|'('
name|'ServiceUnavailable'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Compute service is unavailable at this time."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UnableToMigrateToSelf
dedent|''
name|'class'
name|'UnableToMigrateToSelf'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Unable to migrate instance (%(instance_id)s) "'
nl|'\n'
string|'"to current host (%(host)s)."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SourceHostUnavailable
dedent|''
name|'class'
name|'SourceHostUnavailable'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Original compute host is unavailable at this time."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidHypervisorType
dedent|''
name|'class'
name|'InvalidHypervisorType'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"The supplied hypervisor type of is invalid."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DestinationHypervisorTooOld
dedent|''
name|'class'
name|'DestinationHypervisorTooOld'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"The instance requires a newer hypervisor version than "'
nl|'\n'
string|'"has been provided."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidDevicePath
dedent|''
name|'class'
name|'InvalidDevicePath'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"The supplied device path (%(path)s) is invalid."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidCPUInfo
dedent|''
name|'class'
name|'InvalidCPUInfo'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Unacceptable CPU info"'
op|')'
op|'+'
string|'": %(reason)s"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidVLANTag
dedent|''
name|'class'
name|'InvalidVLANTag'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"VLAN tag is not appropriate for the port group "'
nl|'\n'
string|'"%(bridge)s. Expected VLAN tag is %(tag)s, "'
nl|'\n'
string|'"but the one associated with the port group is %(pgroup)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidVLANPortGroup
dedent|''
name|'class'
name|'InvalidVLANPortGroup'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"vSwitch which contains the port group %(bridge)s is "'
nl|'\n'
string|'"not associated with the desired physical adapter. "'
nl|'\n'
string|'"Expected vSwitch is %(expected)s, but the one associated "'
nl|'\n'
string|'"is %(actual)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidDiskFormat
dedent|''
name|'class'
name|'InvalidDiskFormat'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Disk format %(disk_format)s is not acceptable"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageUnacceptable
dedent|''
name|'class'
name|'ImageUnacceptable'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Image %(image_id)s is unacceptable"'
op|')'
op|'+'
string|'": %(reason)s"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceUnacceptable
dedent|''
name|'class'
name|'InstanceUnacceptable'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Instance %(instance_id)s is unacceptable"'
op|')'
op|'+'
string|'": %(reason)s"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotFound
dedent|''
name|'class'
name|'NotFound'
op|'('
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Resource could not be found."'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NotFound'
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
DECL|class|InstanceNotFound
dedent|''
dedent|''
name|'class'
name|'InstanceNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Instance %(instance_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeNotFound
dedent|''
name|'class'
name|'VolumeNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Volume %(volume_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeNotFoundForInstance
dedent|''
name|'class'
name|'VolumeNotFoundForInstance'
op|'('
name|'VolumeNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Volume not found for instance %(instance_id)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExportDeviceNotFoundForVolume
dedent|''
name|'class'
name|'ExportDeviceNotFoundForVolume'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"No export device found for volume %(volume_id)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ISCSITargetNotFoundForVolume
dedent|''
name|'class'
name|'ISCSITargetNotFoundForVolume'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"No target id found for volume %(volume_id)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DiskNotFound
dedent|''
name|'class'
name|'DiskNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"No disk at %(location)s"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageNotFound
dedent|''
name|'class'
name|'ImageNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Image %(image_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|KernelNotFoundForImage
dedent|''
name|'class'
name|'KernelNotFoundForImage'
op|'('
name|'ImageNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Kernel not found for image %(image_id)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RamdiskNotFoundForImage
dedent|''
name|'class'
name|'RamdiskNotFoundForImage'
op|'('
name|'ImageNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Ramdisk not found for image %(image_id)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UserNotFound
dedent|''
name|'class'
name|'UserNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"User %(user_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProjectNotFound
dedent|''
name|'class'
name|'ProjectNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Project %(project_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProjectMembershipNotFound
dedent|''
name|'class'
name|'ProjectMembershipNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"User %(user_id)s is not a member of project %(project_id)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UserRoleNotFound
dedent|''
name|'class'
name|'UserRoleNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Role %(role_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|StorageRepositoryNotFound
dedent|''
name|'class'
name|'StorageRepositoryNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Cannot find SR to read/write VDI."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkNotFound
dedent|''
name|'class'
name|'NetworkNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Network %(network_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkNotFoundForBridge
dedent|''
name|'class'
name|'NetworkNotFoundForBridge'
op|'('
name|'NetworkNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Network could not be found for bridge %(bridge)s"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkNotFoundForCidr
dedent|''
name|'class'
name|'NetworkNotFoundForCidr'
op|'('
name|'NetworkNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Network could not be found with cidr %(cidr)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkNotFoundForInstance
dedent|''
name|'class'
name|'NetworkNotFoundForInstance'
op|'('
name|'NetworkNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Network could not be found for instance %(instance_id)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoNetworksFound
dedent|''
name|'class'
name|'NoNetworksFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"No networks defined."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DatastoreNotFound
dedent|''
name|'class'
name|'DatastoreNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Could not find the datastore reference(s) which the VM uses."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoFixedIpsFoundForInstance
dedent|''
name|'class'
name|'NoFixedIpsFoundForInstance'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Instance %(instance_id)s has zero fixed ips."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIpNotFound
dedent|''
name|'class'
name|'FloatingIpNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Floating ip not found for fixed address %(fixed_ip)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoFloatingIpsDefined
dedent|''
name|'class'
name|'NoFloatingIpsDefined'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Zero floating ips could be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoFloatingIpsDefinedForHost
dedent|''
name|'class'
name|'NoFloatingIpsDefinedForHost'
op|'('
name|'NoFloatingIpsDefined'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Zero floating ips defined for host %(host)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoFloatingIpsDefinedForInstance
dedent|''
name|'class'
name|'NoFloatingIpsDefinedForInstance'
op|'('
name|'NoFloatingIpsDefined'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Zero floating ips defined for instance %(instance_id)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|KeypairNotFound
dedent|''
name|'class'
name|'KeypairNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Keypair %(keypair_name)s not found for user %(user_id)s"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CertificateNotFound
dedent|''
name|'class'
name|'CertificateNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Certificate %(certificate_id)s not found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceNotFound
dedent|''
name|'class'
name|'ServiceNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Service %(service_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostNotFound
dedent|''
name|'class'
name|'HostNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Host %(host)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeHostNotFound
dedent|''
name|'class'
name|'ComputeHostNotFound'
op|'('
name|'HostNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Compute host %(host)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostBinaryNotFound
dedent|''
name|'class'
name|'HostBinaryNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Could not find binary %(binary)s on host %(host)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AuthTokenNotFound
dedent|''
name|'class'
name|'AuthTokenNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Auth token %(token)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AccessKeyNotFound
dedent|''
name|'class'
name|'AccessKeyNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Access Key %(access_key)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaNotFound
dedent|''
name|'class'
name|'QuotaNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Quota could not be found"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProjectQuotaNotFound
dedent|''
name|'class'
name|'ProjectQuotaNotFound'
op|'('
name|'QuotaNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Quota for project %(project_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupNotFound
dedent|''
name|'class'
name|'SecurityGroupNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Security group %(security_group_id)s not found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupNotFoundForProject
dedent|''
name|'class'
name|'SecurityGroupNotFoundForProject'
op|'('
name|'SecurityGroupNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Security group %(security_group_id)s not found "'
nl|'\n'
string|'"for project %(project_id)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupNotFoundForRule
dedent|''
name|'class'
name|'SecurityGroupNotFoundForRule'
op|'('
name|'SecurityGroupNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Security group with rule %(rule_id)s not found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MigrationNotFound
dedent|''
name|'class'
name|'MigrationNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Migration %(migration_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MigrationNotFoundByStatus
dedent|''
name|'class'
name|'MigrationNotFoundByStatus'
op|'('
name|'MigrationNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Migration not found for instance %(instance_id)s "'
nl|'\n'
string|'"with status %(status)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsolePoolNotFound
dedent|''
name|'class'
name|'ConsolePoolNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Console pool %(pool_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsolePoolNotFoundForHostType
dedent|''
name|'class'
name|'ConsolePoolNotFoundForHostType'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Console pool of type %(console_type)s "'
nl|'\n'
string|'"for compute host %(compute_host)s "'
nl|'\n'
string|'"on proxy host %(host)s not found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleNotFound
dedent|''
name|'class'
name|'ConsoleNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Console %(console_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleNotFoundForInstance
dedent|''
name|'class'
name|'ConsoleNotFoundForInstance'
op|'('
name|'ConsoleNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Console for instance %(instance_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleNotFoundInPoolForInstance
dedent|''
name|'class'
name|'ConsoleNotFoundInPoolForInstance'
op|'('
name|'ConsoleNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Console for instance %(instance_id)s "'
nl|'\n'
string|'"in pool %(pool_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoInstanceTypesFound
dedent|''
name|'class'
name|'NoInstanceTypesFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Zero instance types found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceTypeNotFound
dedent|''
name|'class'
name|'InstanceTypeNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Instance type %(instance_type_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceTypeNotFoundByName
dedent|''
name|'class'
name|'InstanceTypeNotFoundByName'
op|'('
name|'InstanceTypeNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Instance type with name %(instance_type_name)s "'
nl|'\n'
string|'"could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorNotFound
dedent|''
name|'class'
name|'FlavorNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Flavor %(flavor_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ZoneNotFound
dedent|''
name|'class'
name|'ZoneNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Zone %(zone_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceMetadataNotFound
dedent|''
name|'class'
name|'InstanceMetadataNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Instance %(instance_id)s has no metadata with "'
nl|'\n'
string|'"key %(metadata_key)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LDAPObjectNotFound
dedent|''
name|'class'
name|'LDAPObjectNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"LDAP object could not be found"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LDAPUserNotFound
dedent|''
name|'class'
name|'LDAPUserNotFound'
op|'('
name|'LDAPObjectNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"LDAP user %(user_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LDAPGroupNotFound
dedent|''
name|'class'
name|'LDAPGroupNotFound'
op|'('
name|'LDAPObjectNotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"LDAP group %(group_id)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LDAPGroupMembershipNotFound
dedent|''
name|'class'
name|'LDAPGroupMembershipNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"LDAP user %(user_id)s is not a member of group %(group_id)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FileNotFound
dedent|''
name|'class'
name|'FileNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"File %(file_path)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoFilesFound
dedent|''
name|'class'
name|'NoFilesFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Zero files could be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SwitchNotFoundForNetworkAdapter
dedent|''
name|'class'
name|'SwitchNotFoundForNetworkAdapter'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Virtual switch associated with the "'
nl|'\n'
string|'"network adapter %(adapter)s not found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkAdapterNotFound
dedent|''
name|'class'
name|'NetworkAdapterNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Network adapter %(adapter)s could not be found."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ClassNotFound
dedent|''
name|'class'
name|'ClassNotFound'
op|'('
name|'NotFound'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Class %(class_name)s could not be found"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotAllowed
dedent|''
name|'class'
name|'NotAllowed'
op|'('
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Action not allowed."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GlobalRoleNotAllowed
dedent|''
name|'class'
name|'GlobalRoleNotAllowed'
op|'('
name|'NotAllowed'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Unable to use global role %(role_id)s"'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
