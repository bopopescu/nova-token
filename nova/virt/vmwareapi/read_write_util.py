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
name|'httplib'
newline|'\r\n'
name|'import'
name|'json'
newline|'\r\n'
name|'import'
name|'logging'
newline|'\r\n'
name|'import'
name|'os'
newline|'\r\n'
name|'import'
name|'urllib'
newline|'\r\n'
name|'import'
name|'urllib2'
newline|'\r\n'
name|'import'
name|'urlparse'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
name|'import'
name|'AuthManager'
newline|'\r\n'
nl|'\r\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\r\n'
nl|'\r\n'
DECL|variable|READ_CHUNKSIZE
name|'READ_CHUNKSIZE'
op|'='
number|'2'
op|'*'
number|'1024'
op|'*'
number|'1024'
newline|'\r\n'
nl|'\r\n'
DECL|variable|USER_AGENT
name|'USER_AGENT'
op|'='
string|'"OpenStack-ESX-Adapter"'
newline|'\r\n'
nl|'\r\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.virt.vmwareapi.read_write_util"'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|ImageServiceFile
name|'class'
name|'ImageServiceFile'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    The base image service Class\r\n    """'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'file_handle'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Initialize the file handle.\r\n        """'
newline|'\r\n'
name|'self'
op|'.'
name|'eof'
op|'='
name|'False'
newline|'\r\n'
name|'self'
op|'.'
name|'file_handle'
op|'='
name|'file_handle'
newline|'\r\n'
nl|'\r\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Write data to the file\r\n        """'
newline|'\r\n'
name|'raise'
name|'NotImplementedError'
newline|'\r\n'
nl|'\r\n'
DECL|member|read
dedent|''
name|'def'
name|'read'
op|'('
name|'self'
op|','
name|'chunk_size'
op|'='
name|'READ_CHUNKSIZE'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Read a chunk of data from the file\r\n        """'
newline|'\r\n'
name|'raise'
name|'NotImplementedError'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_size
dedent|''
name|'def'
name|'get_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Get the size of the file whose data is to be read\r\n        """'
newline|'\r\n'
name|'raise'
name|'NotImplementedError'
newline|'\r\n'
nl|'\r\n'
DECL|member|set_eof
dedent|''
name|'def'
name|'set_eof'
op|'('
name|'self'
op|','
name|'eof'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Set the end of file marker.\r\n        """'
newline|'\r\n'
name|'self'
op|'.'
name|'eof'
op|'='
name|'eof'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_eof
dedent|''
name|'def'
name|'get_eof'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Check if the file end has been reached or not.\r\n        """'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'eof'
newline|'\r\n'
nl|'\r\n'
DECL|member|close
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Close the file handle.\r\n        """'
newline|'\r\n'
name|'try'
op|':'
newline|'\r\n'
indent|'            '
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'close'
op|'('
op|')'
newline|'\r\n'
dedent|''
name|'except'
op|':'
newline|'\r\n'
indent|'            '
name|'pass'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_image_properties
dedent|''
dedent|''
name|'def'
name|'get_image_properties'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Get the image properties\r\n        """'
newline|'\r\n'
name|'raise'
name|'NotImplementedError'
newline|'\r\n'
nl|'\r\n'
DECL|member|__del__
dedent|''
name|'def'
name|'__del__'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Destructor. Close the file handle if the same has been forgotten.\r\n        """'
newline|'\r\n'
name|'self'
op|'.'
name|'close'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|GlanceHTTPWriteFile
dedent|''
dedent|''
name|'class'
name|'GlanceHTTPWriteFile'
op|'('
name|'ImageServiceFile'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Glance file write handler Class\r\n    """'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'port'
op|','
name|'image_id'
op|','
name|'file_size'
op|','
name|'os_type'
op|','
name|'adapter_type'
op|','
nl|'\r\n'
name|'version'
op|'='
number|'1'
op|','
name|'scheme'
op|'='
string|'"http"'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Initialize with the glance host specifics.\r\n        """'
newline|'\r\n'
name|'base_url'
op|'='
string|'"%s://%s:%s/images/%s"'
op|'%'
op|'('
name|'scheme'
op|','
name|'host'
op|','
name|'port'
op|','
name|'image_id'
op|')'
newline|'\r\n'
op|'('
name|'scheme'
op|','
name|'netloc'
op|','
name|'path'
op|','
name|'params'
op|','
name|'query'
op|','
name|'fragment'
op|')'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'base_url'
op|')'
newline|'\r\n'
name|'if'
name|'scheme'
op|'=='
string|'"http"'
op|':'
newline|'\r\n'
indent|'            '
name|'conn'
op|'='
name|'httplib'
op|'.'
name|'HTTPConnection'
op|'('
name|'netloc'
op|')'
newline|'\r\n'
dedent|''
name|'elif'
name|'scheme'
op|'=='
string|'"https"'
op|':'
newline|'\r\n'
indent|'            '
name|'conn'
op|'='
name|'httplib'
op|'.'
name|'HTTPSConnection'
op|'('
name|'netloc'
op|')'
newline|'\r\n'
dedent|''
name|'conn'
op|'.'
name|'putrequest'
op|'('
string|'"PUT"'
op|','
name|'path'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"User-Agent"'
op|','
name|'USER_AGENT'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"Content-Length"'
op|','
name|'file_size'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"Content-Type"'
op|','
string|'"application/octet-stream"'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"x-image-meta-store"'
op|','
string|'"file"'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"x-image-meta-is_public"'
op|','
string|'"True"'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"x-image-meta-type"'
op|','
string|'"raw"'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"x-image-meta-size"'
op|','
name|'file_size'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"x-image-meta-property-kernel_id"'
op|','
string|'""'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"x-image-meta-property-ramdisk_id"'
op|','
string|'""'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"x-image-meta-property-vmware_ostype"'
op|','
name|'os_type'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"x-image-meta-property-vmware_adaptertype"'
op|','
nl|'\r\n'
name|'adapter_type'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"x-image-meta-property-vmware_image_version"'
op|','
name|'version'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'endheaders'
op|'('
op|')'
newline|'\r\n'
name|'ImageServiceFile'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'conn'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Write data to the file\r\n        """'
newline|'\r\n'
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'send'
op|'('
name|'data'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|GlanceHTTPReadFile
dedent|''
dedent|''
name|'class'
name|'GlanceHTTPReadFile'
op|'('
name|'ImageServiceFile'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Glance file read handler Class\r\n    """'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'port'
op|','
name|'image_id'
op|','
name|'scheme'
op|'='
string|'"http"'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Initialize with the glance host specifics.\r\n        """'
newline|'\r\n'
name|'base_url'
op|'='
string|'"%s://%s:%s/images/%s"'
op|'%'
op|'('
name|'scheme'
op|','
name|'host'
op|','
name|'port'
op|','
nl|'\r\n'
name|'urllib'
op|'.'
name|'pathname2url'
op|'('
name|'image_id'
op|')'
op|')'
newline|'\r\n'
name|'headers'
op|'='
op|'{'
string|"'User-Agent'"
op|':'
name|'USER_AGENT'
op|'}'
newline|'\r\n'
name|'request'
op|'='
name|'urllib2'
op|'.'
name|'Request'
op|'('
name|'base_url'
op|','
name|'None'
op|','
name|'headers'
op|')'
newline|'\r\n'
name|'conn'
op|'='
name|'urllib2'
op|'.'
name|'urlopen'
op|'('
name|'request'
op|')'
newline|'\r\n'
name|'ImageServiceFile'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'conn'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|read
dedent|''
name|'def'
name|'read'
op|'('
name|'self'
op|','
name|'chunk_size'
op|'='
name|'READ_CHUNKSIZE'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Read a chunk of data.\r\n        """'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'read'
op|'('
name|'chunk_size'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_size
dedent|''
name|'def'
name|'get_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Get the size of the file to be read.\r\n        """'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|'"X-Image-Meta-Size"'
op|','
op|'-'
number|'1'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_image_properties
dedent|''
name|'def'
name|'get_image_properties'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Get the image properties like say OS Type and the Adapter Type\r\n        """'
newline|'\r\n'
name|'return'
op|'{'
string|'"vmware_ostype"'
op|':'
nl|'\r\n'
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
nl|'\r\n'
string|'"X-Image-Meta-Property-Vmware_ostype"'
op|')'
op|','
nl|'\r\n'
string|'"vmware_adaptertype"'
op|':'
nl|'\r\n'
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
nl|'\r\n'
string|'"X-Image-Meta-Property-Vmware_adaptertype"'
op|')'
op|','
nl|'\r\n'
string|'"vmware_image_version"'
op|':'
nl|'\r\n'
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
nl|'\r\n'
string|'"X-Image-Meta-Property-Vmware_image_version"'
op|')'
op|'}'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|FakeFileRead
dedent|''
dedent|''
name|'class'
name|'FakeFileRead'
op|'('
name|'ImageServiceFile'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Local file read handler class\r\n    """'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Initialize the file path\r\n        """'
newline|'\r\n'
name|'self'
op|'.'
name|'path'
op|'='
name|'path'
newline|'\r\n'
name|'file_handle'
op|'='
name|'open'
op|'('
name|'path'
op|','
string|'"rb"'
op|')'
newline|'\r\n'
name|'ImageServiceFile'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'file_handle'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_size
dedent|''
name|'def'
name|'get_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Get size of the file to be read\r\n        """'
newline|'\r\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'getsize'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'self'
op|'.'
name|'path'
op|')'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|read
dedent|''
name|'def'
name|'read'
op|'('
name|'self'
op|','
name|'chunk_size'
op|'='
name|'READ_CHUNKSIZE'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Read a chunk of data\r\n        """'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'read'
op|'('
name|'chunk_size'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_image_properties
dedent|''
name|'def'
name|'get_image_properties'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Get the image properties like say OS Type and the Adapter Type\r\n        """'
newline|'\r\n'
name|'return'
op|'{'
string|'"vmware_ostype"'
op|':'
string|'"otherGuest"'
op|','
nl|'\r\n'
string|'"vmware_adaptertype"'
op|':'
string|'"lsiLogic"'
op|','
nl|'\r\n'
string|'"vmware_image_version"'
op|':'
string|'"1"'
op|'}'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|FakeFileWrite
dedent|''
dedent|''
name|'class'
name|'FakeFileWrite'
op|'('
name|'ImageServiceFile'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Local file write handler Class\r\n    """'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Initialize the file path.\r\n        """'
newline|'\r\n'
name|'file_handle'
op|'='
name|'open'
op|'('
name|'path'
op|','
string|'"wb"'
op|')'
newline|'\r\n'
name|'ImageServiceFile'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'file_handle'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Write data to the file.\r\n        """'
newline|'\r\n'
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|VMwareHTTPFile
dedent|''
dedent|''
name|'class'
name|'VMwareHTTPFile'
op|'('
name|'object'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Base Class for HTTP file.\r\n    """'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'file_handle'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Intialize the file handle.\r\n        """'
newline|'\r\n'
name|'self'
op|'.'
name|'eof'
op|'='
name|'False'
newline|'\r\n'
name|'self'
op|'.'
name|'file_handle'
op|'='
name|'file_handle'
newline|'\r\n'
nl|'\r\n'
DECL|member|set_eof
dedent|''
name|'def'
name|'set_eof'
op|'('
name|'self'
op|','
name|'eof'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Set the end of file marker.\r\n        """'
newline|'\r\n'
name|'self'
op|'.'
name|'eof'
op|'='
name|'eof'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_eof
dedent|''
name|'def'
name|'get_eof'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Check if the end of file has been reached.\r\n        """'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'eof'
newline|'\r\n'
nl|'\r\n'
DECL|member|close
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Close the file handle.\r\n        """'
newline|'\r\n'
name|'try'
op|':'
newline|'\r\n'
indent|'            '
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'close'
op|'('
op|')'
newline|'\r\n'
dedent|''
name|'except'
op|':'
newline|'\r\n'
indent|'            '
name|'pass'
newline|'\r\n'
nl|'\r\n'
DECL|member|__del__
dedent|''
dedent|''
name|'def'
name|'__del__'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Destructor. Close the file handle if the same has been forgotten.\r\n        """'
newline|'\r\n'
name|'self'
op|'.'
name|'close'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|_build_vim_cookie_headers
dedent|''
name|'def'
name|'_build_vim_cookie_headers'
op|'('
name|'self'
op|','
name|'vim_cookies'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Build ESX host session cookie headers.\r\n        """'
newline|'\r\n'
name|'cookie'
op|'='
name|'str'
op|'('
name|'vim_cookies'
op|')'
op|'.'
name|'split'
op|'('
string|'":"'
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\r\n'
name|'cookie'
op|'='
name|'cookie'
op|'['
op|':'
name|'cookie'
op|'.'
name|'find'
op|'('
string|"';'"
op|')'
op|']'
newline|'\r\n'
name|'return'
name|'cookie'
newline|'\r\n'
nl|'\r\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Write data to the file.\r\n        """'
newline|'\r\n'
name|'raise'
name|'NotImplementedError'
newline|'\r\n'
nl|'\r\n'
DECL|member|read
dedent|''
name|'def'
name|'read'
op|'('
name|'self'
op|','
name|'chunk_size'
op|'='
name|'READ_CHUNKSIZE'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Read a chunk of data.\r\n        """'
newline|'\r\n'
name|'raise'
name|'NotImplementedError'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_size
dedent|''
name|'def'
name|'get_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Get size of the file to be read.\r\n        """'
newline|'\r\n'
name|'raise'
name|'NotImplementedError'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|VMWareHTTPWriteFile
dedent|''
dedent|''
name|'class'
name|'VMWareHTTPWriteFile'
op|'('
name|'VMwareHTTPFile'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    VMWare file write handler Class\r\n    """'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'data_center_name'
op|','
name|'datastore_name'
op|','
name|'cookies'
op|','
nl|'\r\n'
name|'file_path'
op|','
name|'file_size'
op|','
name|'scheme'
op|'='
string|'"https"'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Initialize the file specifics.\r\n        """'
newline|'\r\n'
name|'base_url'
op|'='
string|'"%s://%s/folder/%s"'
op|'%'
op|'('
name|'scheme'
op|','
name|'host'
op|','
name|'file_path'
op|')'
newline|'\r\n'
name|'param_list'
op|'='
op|'{'
string|'"dcPath"'
op|':'
name|'data_center_name'
op|','
string|'"dsName"'
op|':'
name|'datastore_name'
op|'}'
newline|'\r\n'
name|'base_url'
op|'='
name|'base_url'
op|'+'
string|'"?"'
op|'+'
name|'urllib'
op|'.'
name|'urlencode'
op|'('
name|'param_list'
op|')'
newline|'\r\n'
op|'('
name|'scheme'
op|','
name|'netloc'
op|','
name|'path'
op|','
name|'params'
op|','
name|'query'
op|','
name|'fragment'
op|')'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'base_url'
op|')'
newline|'\r\n'
name|'if'
name|'scheme'
op|'=='
string|'"http"'
op|':'
newline|'\r\n'
indent|'            '
name|'conn'
op|'='
name|'httplib'
op|'.'
name|'HTTPConnection'
op|'('
name|'netloc'
op|')'
newline|'\r\n'
dedent|''
name|'elif'
name|'scheme'
op|'=='
string|'"https"'
op|':'
newline|'\r\n'
indent|'            '
name|'conn'
op|'='
name|'httplib'
op|'.'
name|'HTTPSConnection'
op|'('
name|'netloc'
op|')'
newline|'\r\n'
dedent|''
name|'conn'
op|'.'
name|'putrequest'
op|'('
string|'"PUT"'
op|','
name|'path'
op|'+'
string|'"?"'
op|'+'
name|'query'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"User-Agent"'
op|','
name|'USER_AGENT'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"Content-Length"'
op|','
name|'file_size'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"Cookie"'
op|','
name|'self'
op|'.'
name|'_build_vim_cookie_headers'
op|'('
name|'cookies'
op|')'
op|')'
newline|'\r\n'
name|'conn'
op|'.'
name|'endheaders'
op|'('
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'conn'
newline|'\r\n'
name|'VMwareHTTPFile'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'conn'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Write to the file.\r\n        """'
newline|'\r\n'
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'send'
op|'('
name|'data'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|close
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Get the response and close the connection\r\n        """'
newline|'\r\n'
name|'try'
op|':'
newline|'\r\n'
indent|'            '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'getresponse'
op|'('
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'excep'
op|':'
newline|'\r\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Exception during close of connection in "'
nl|'\r\n'
string|'"VMWareHTTpWrite. Exception is %s"'
op|'%'
name|'excep'
op|')'
newline|'\r\n'
dedent|''
name|'super'
op|'('
name|'VMWareHTTPWriteFile'
op|','
name|'self'
op|')'
op|'.'
name|'close'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|VmWareHTTPReadFile
dedent|''
dedent|''
name|'class'
name|'VmWareHTTPReadFile'
op|'('
name|'VMwareHTTPFile'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    VMWare file read handler Class\r\n    """'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'data_center_name'
op|','
name|'datastore_name'
op|','
name|'cookies'
op|','
nl|'\r\n'
name|'file_path'
op|','
name|'scheme'
op|'='
string|'"https"'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Initialize the file specifics.\r\n        """'
newline|'\r\n'
name|'base_url'
op|'='
string|'"%s://%s/folder/%s"'
op|'%'
op|'('
name|'scheme'
op|','
name|'host'
op|','
nl|'\r\n'
name|'urllib'
op|'.'
name|'pathname2url'
op|'('
name|'file_path'
op|')'
op|')'
newline|'\r\n'
name|'param_list'
op|'='
op|'{'
string|'"dcPath"'
op|':'
name|'data_center_name'
op|','
string|'"dsName"'
op|':'
name|'datastore_name'
op|'}'
newline|'\r\n'
name|'base_url'
op|'='
name|'base_url'
op|'+'
string|'"?"'
op|'+'
name|'urllib'
op|'.'
name|'urlencode'
op|'('
name|'param_list'
op|')'
newline|'\r\n'
name|'headers'
op|'='
op|'{'
string|"'User-Agent'"
op|':'
name|'USER_AGENT'
op|','
nl|'\r\n'
string|"'Cookie'"
op|':'
name|'self'
op|'.'
name|'_build_vim_cookie_headers'
op|'('
name|'cookies'
op|')'
op|'}'
newline|'\r\n'
name|'request'
op|'='
name|'urllib2'
op|'.'
name|'Request'
op|'('
name|'base_url'
op|','
name|'None'
op|','
name|'headers'
op|')'
newline|'\r\n'
name|'conn'
op|'='
name|'urllib2'
op|'.'
name|'urlopen'
op|'('
name|'request'
op|')'
newline|'\r\n'
name|'VMwareHTTPFile'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'conn'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|read
dedent|''
name|'def'
name|'read'
op|'('
name|'self'
op|','
name|'chunk_size'
op|'='
name|'READ_CHUNKSIZE'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Read a chunk of data.\r\n        """'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'read'
op|'('
name|'chunk_size'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_size
dedent|''
name|'def'
name|'get_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Get size of the file to be read.\r\n        """'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|'"Content-Length"'
op|','
op|'-'
number|'1'
op|')'
newline|'\r\n'
dedent|''
dedent|''
endmarker|''
end_unit
