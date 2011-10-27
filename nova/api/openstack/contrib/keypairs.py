begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'""" Keypair management extension"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'crypto'
newline|'\n'
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
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|KeypairController
name|'class'
name|'KeypairController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Keypair API controller for the Openstack API """'
newline|'\n'
nl|'\n'
comment|'# TODO(ja): both this file and nova.api.ec2.cloud.py have similar logic.'
nl|'\n'
comment|'# move the common keypair logic to nova.compute.API?'
nl|'\n'
nl|'\n'
DECL|member|_gen_key
name|'def'
name|'_gen_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Generate a key\n        """'
newline|'\n'
name|'private_key'
op|','
name|'public_key'
op|','
name|'fingerprint'
op|'='
name|'crypto'
op|'.'
name|'generate_key_pair'
op|'('
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'private_key'"
op|':'
name|'private_key'
op|','
nl|'\n'
string|"'public_key'"
op|':'
name|'public_key'
op|','
nl|'\n'
string|"'fingerprint'"
op|':'
name|'fingerprint'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create or import keypair.\n\n        Sending name will generate a key and return private_key\n        and fingerprint.\n\n        You can send a public_key to add an existing ssh key\n\n        params: keypair object with:\n            name (required) - string\n            public_key (optional) - string\n        """'
newline|'\n'
nl|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'params'
op|'='
name|'body'
op|'['
string|"'keypair'"
op|']'
newline|'\n'
name|'name'
op|'='
name|'params'
op|'['
string|"'name'"
op|']'
newline|'\n'
nl|'\n'
comment|'# NOTE(ja): generation is slow, so shortcut invalid name exception'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'key_pair_get'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'user_id'
op|','
name|'name'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'KeyPairExists'
op|'('
name|'key_name'
op|'='
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'keypair'
op|'='
op|'{'
string|"'user_id'"
op|':'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'name'
op|'}'
newline|'\n'
nl|'\n'
comment|'# import if public_key is sent'
nl|'\n'
name|'if'
string|"'public_key'"
name|'in'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'tmpdir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
name|'fn'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'import.pub'"
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'fn'
op|','
string|"'w'"
op|')'
name|'as'
name|'pub'
op|':'
newline|'\n'
indent|'                '
name|'pub'
op|'.'
name|'write'
op|'('
name|'params'
op|'['
string|"'public_key'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'fingerprint'
op|'='
name|'crypto'
op|'.'
name|'generate_fingerprint'
op|'('
name|'fn'
op|')'
newline|'\n'
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'tmpdir'
op|')'
newline|'\n'
name|'keypair'
op|'['
string|"'public_key'"
op|']'
op|'='
name|'params'
op|'['
string|"'public_key'"
op|']'
newline|'\n'
name|'keypair'
op|'['
string|"'fingerprint'"
op|']'
op|'='
name|'fingerprint'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'generated_key'
op|'='
name|'self'
op|'.'
name|'_gen_key'
op|'('
op|')'
newline|'\n'
name|'keypair'
op|'['
string|"'private_key'"
op|']'
op|'='
name|'generated_key'
op|'['
string|"'private_key'"
op|']'
newline|'\n'
name|'keypair'
op|'['
string|"'public_key'"
op|']'
op|'='
name|'generated_key'
op|'['
string|"'public_key'"
op|']'
newline|'\n'
name|'keypair'
op|'['
string|"'fingerprint'"
op|']'
op|'='
name|'generated_key'
op|'['
string|"'fingerprint'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'db'
op|'.'
name|'key_pair_create'
op|'('
name|'context'
op|','
name|'keypair'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'keypair'"
op|':'
name|'keypair'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Delete a keypair with a given name\n        """'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'db'
op|'.'
name|'key_pair_destroy'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'user_id'
op|','
name|'id'
op|')'
newline|'\n'
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
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
string|'"""\n        List of keypairs for a user\n        """'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'key_pairs'
op|'='
name|'db'
op|'.'
name|'key_pair_get_all_by_user'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'rval'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'key_pair'
name|'in'
name|'key_pairs'
op|':'
newline|'\n'
indent|'            '
name|'rval'
op|'.'
name|'append'
op|'('
op|'{'
string|"'keypair'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'key_pair'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'public_key'"
op|':'
name|'key_pair'
op|'['
string|"'public_key'"
op|']'
op|','
nl|'\n'
string|"'fingerprint'"
op|':'
name|'key_pair'
op|'['
string|"'fingerprint'"
op|']'
op|','
nl|'\n'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'keypairs'"
op|':'
name|'rval'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Keypairs
dedent|''
dedent|''
name|'class'
name|'Keypairs'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Keypair Support"""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Keypairs"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-keypairs"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/ext/keypairs/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-08-08T00:00:00+00:00"'
newline|'\n'
nl|'\n'
DECL|member|get_resources
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
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
string|"'os-keypairs'"
op|','
nl|'\n'
name|'KeypairController'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
