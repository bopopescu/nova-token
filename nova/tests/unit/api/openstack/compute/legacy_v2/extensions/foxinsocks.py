begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FoxInSocksController
name|'class'
name|'FoxInSocksController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|index
indent|'    '
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"Try to say this Mr. Knox, sir..."'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FoxInSocksServerControllerExtension
dedent|''
dedent|''
name|'class'
name|'FoxInSocksServerControllerExtension'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'add_tweedle'"
op|')'
newline|'\n'
DECL|member|_add_tweedle
name|'def'
name|'_add_tweedle'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'return'
string|'"Tweedle Beetle Added."'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'delete_tweedle'"
op|')'
newline|'\n'
DECL|member|_delete_tweedle
name|'def'
name|'_delete_tweedle'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'return'
string|'"Tweedle Beetle Deleted."'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'fail'"
op|')'
newline|'\n'
DECL|member|_fail
name|'def'
name|'_fail'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
string|"'Tweedle fail'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FoxInSocksFlavorGooseControllerExtension
dedent|''
dedent|''
name|'class'
name|'FoxInSocksFlavorGooseControllerExtension'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
comment|'# NOTE: This only handles JSON responses.'
nl|'\n'
comment|'# You can use content type header to test for XML.'
nl|'\n'
indent|'        '
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'googoose'"
op|']'
op|'='
name|'req'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|"'chewing'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FoxInSocksFlavorBandsControllerExtension
dedent|''
dedent|''
name|'class'
name|'FoxInSocksFlavorBandsControllerExtension'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
comment|'# NOTE: This only handles JSON responses.'
nl|'\n'
comment|'# You can use content type header to test for XML.'
nl|'\n'
indent|'        '
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'big_bands'"
op|']'
op|'='
string|"'Pig Bands!'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Foxinsocks
dedent|''
dedent|''
name|'class'
name|'Foxinsocks'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Fox In Socks Extension."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Fox In Socks"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"FOXNSOX"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://www.fox.in.socks/api/ext/pie/v1.0"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-01-22T13:25:27-06:00"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ext_mgr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext_mgr'
op|'.'
name|'register'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_resources
dedent|''
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
name|'resource'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'foxnsocks'"
op|','
nl|'\n'
name|'FoxInSocksController'
op|'('
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'resource'
op|')'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'extension_list'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'extension_set'
op|'='
op|'['
nl|'\n'
op|'('
name|'FoxInSocksServerControllerExtension'
op|','
string|"'servers'"
op|')'
op|','
nl|'\n'
op|'('
name|'FoxInSocksFlavorGooseControllerExtension'
op|','
string|"'flavors'"
op|')'
op|','
nl|'\n'
op|'('
name|'FoxInSocksFlavorBandsControllerExtension'
op|','
string|"'flavors'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'for'
name|'klass'
op|','
name|'collection'
name|'in'
name|'extension_set'
op|':'
newline|'\n'
indent|'            '
name|'controller'
op|'='
name|'klass'
op|'('
op|')'
newline|'\n'
name|'ext'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
name|'self'
op|','
name|'collection'
op|','
name|'controller'
op|')'
newline|'\n'
name|'extension_list'
op|'.'
name|'append'
op|'('
name|'ext'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'extension_list'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit