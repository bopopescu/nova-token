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
string|'"""\nDatastore:\n\nMAKE Sure that ReDIS is running, and your flags are set properly,\nbefore trying to run this.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'redis'
newline|'\n'
nl|'\n'
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
name|'utils'
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
string|"'redis_host'"
op|','
string|"'127.0.0.1'"
op|','
nl|'\n'
string|"'Host that redis is running on.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'redis_port'"
op|','
number|'6379'
op|','
nl|'\n'
string|"'Port that redis is running on.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'redis_db'"
op|','
number|'0'
op|','
string|"'Multiple DB keeps tests away'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Redis
name|'class'
name|'Redis'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'hasattr'
op|'('
name|'self'
op|'.'
name|'__class__'
op|','
string|"'_instance'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|"'Attempted to instantiate singleton'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|instance
name|'def'
name|'instance'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'cls'
op|','
string|"'_instance'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'inst'
op|'='
name|'redis'
op|'.'
name|'Redis'
op|'('
name|'host'
op|'='
name|'FLAGS'
op|'.'
name|'redis_host'
op|','
nl|'\n'
name|'port'
op|'='
name|'FLAGS'
op|'.'
name|'redis_port'
op|','
nl|'\n'
name|'db'
op|'='
name|'FLAGS'
op|'.'
name|'redis_db'
op|')'
newline|'\n'
name|'cls'
op|'.'
name|'_instance'
op|'='
name|'inst'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_instance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConnectionError
dedent|''
dedent|''
name|'class'
name|'ConnectionError'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|absorb_connection_error
dedent|''
name|'def'
name|'absorb_connection_error'
op|'('
name|'fn'
op|')'
op|':'
newline|'\n'
DECL|function|_wrapper
indent|'    '
name|'def'
name|'_wrapper'
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
name|'fn'
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
name|'redis'
op|'.'
name|'exceptions'
op|'.'
name|'ConnectionError'
op|','
name|'ce'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ConnectionError'
op|'('
name|'str'
op|'('
name|'ce'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'_wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BasicModel
dedent|''
name|'class'
name|'BasicModel'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    All Redis-backed data derives from this class.\n\n    You MUST specify an identifier() property that returns a unique string\n    per instance.\n\n    You MUST have an initializer that takes a single argument that is a value\n    returned by identifier() to load a new class with.\n\n    You may want to specify a dictionary for default_state().\n\n    You may also specify override_type at the class left to use a key other\n    than __class__.__name__.\n\n    You override save and destroy calls to automatically build and destroy\n    associations.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|override_type
name|'override_type'
op|'='
name|'None'
newline|'\n'
nl|'\n'
op|'@'
name|'absorb_connection_error'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'state'
op|'='
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'hgetall'
op|'('
name|'self'
op|'.'
name|'__redis_key'
op|')'
newline|'\n'
name|'if'
name|'state'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'initial_state'
op|'='
name|'state'
newline|'\n'
name|'self'
op|'.'
name|'state'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'initial_state'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'initial_state'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'state'
op|'='
name|'self'
op|'.'
name|'default_state'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|default_state
dedent|''
dedent|''
name|'def'
name|'default_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""You probably want to define this in your subclass"""'
newline|'\n'
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_redis_name
name|'def'
name|'_redis_name'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'.'
name|'override_type'
name|'or'
name|'cls'
op|'.'
name|'__name__'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|lookup
name|'def'
name|'lookup'
op|'('
name|'cls'
op|','
name|'identifier'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rv'
op|'='
name|'cls'
op|'('
name|'identifier'
op|')'
newline|'\n'
name|'if'
name|'rv'
op|'.'
name|'is_new_record'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
op|'@'
name|'absorb_connection_error'
newline|'\n'
DECL|member|all
name|'def'
name|'all'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""yields all objects in the store"""'
newline|'\n'
name|'redis_set'
op|'='
name|'cls'
op|'.'
name|'_redis_set_name'
op|'('
name|'cls'
op|'.'
name|'__name__'
op|')'
newline|'\n'
name|'for'
name|'identifier'
name|'in'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'smembers'
op|'('
name|'redis_set'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'cls'
op|'('
name|'identifier'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|associated_to
name|'def'
name|'associated_to'
op|'('
name|'cls'
op|','
name|'foreign_type'
op|','
name|'foreign_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'identifier'
name|'in'
name|'cls'
op|'.'
name|'associated_keys'
op|'('
name|'foreign_type'
op|','
name|'foreign_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'cls'
op|'('
name|'identifier'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
op|'@'
name|'absorb_connection_error'
newline|'\n'
DECL|member|associated_keys
name|'def'
name|'associated_keys'
op|'('
name|'cls'
op|','
name|'foreign_type'
op|','
name|'foreign_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'redis_set'
op|'='
name|'cls'
op|'.'
name|'_redis_association_name'
op|'('
name|'foreign_type'
op|','
name|'foreign_id'
op|')'
newline|'\n'
name|'return'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'smembers'
op|'('
name|'redis_set'
op|')'
name|'or'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_redis_set_name
name|'def'
name|'_redis_set_name'
op|'('
name|'cls'
op|','
name|'kls_name'
op|')'
op|':'
newline|'\n'
comment|'# stupidly pluralize (for compatiblity with previous codebase)'
nl|'\n'
indent|'        '
name|'return'
name|'kls_name'
op|'.'
name|'lower'
op|'('
op|')'
op|'+'
string|'"s"'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_redis_association_name
name|'def'
name|'_redis_association_name'
op|'('
name|'cls'
op|','
name|'foreign_type'
op|','
name|'foreign_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'.'
name|'_redis_set_name'
op|'('
string|'"%s:%s:%s"'
op|'%'
nl|'\n'
op|'('
name|'foreign_type'
op|','
name|'foreign_id'
op|','
name|'cls'
op|'.'
name|'_redis_name'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|identifier
name|'def'
name|'identifier'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""You DEFINITELY want to define this in your subclass"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|'"Your subclass should define identifier"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|__redis_key
name|'def'
name|'__redis_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'%s:%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'_redis_name'
op|'('
op|')'
op|','
name|'self'
op|'.'
name|'identifier'
op|')'
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
string|'"<%s:%s>"'
op|'%'
op|'('
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|','
name|'self'
op|'.'
name|'identifier'
op|')'
newline|'\n'
nl|'\n'
DECL|member|keys
dedent|''
name|'def'
name|'keys'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'state'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|copy
dedent|''
name|'def'
name|'copy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'copyDict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'self'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'copyDict'
op|'['
name|'item'
op|']'
op|'='
name|'self'
op|'['
name|'item'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'copyDict'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'item'
op|','
name|'default'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'state'
op|'.'
name|'get'
op|'('
name|'item'
op|','
name|'default'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'update_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'state'
op|'.'
name|'update'
op|'('
name|'update_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setdefault
dedent|''
name|'def'
name|'setdefault'
op|'('
name|'self'
op|','
name|'item'
op|','
name|'default'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'state'
op|'.'
name|'setdefault'
op|'('
name|'item'
op|','
name|'default'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__contains__
dedent|''
name|'def'
name|'__contains__'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'item'
name|'in'
name|'self'
op|'.'
name|'state'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'state'
op|'['
name|'item'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'item'
op|','
name|'val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'state'
op|'['
name|'item'
op|']'
op|'='
name|'val'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'state'
op|'['
name|'item'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__delitem__
dedent|''
name|'def'
name|'__delitem__'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""We don\'t support this"""'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
string|'"Silly monkey, models NEED all their properties."'
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_new_record
dedent|''
name|'def'
name|'is_new_record'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'initial_state'
op|'=='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'absorb_connection_error'
newline|'\n'
DECL|member|add_to_index
name|'def'
name|'add_to_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Each insance of Foo has its id tracked int the set named Foos"""'
newline|'\n'
name|'set_name'
op|'='
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_redis_set_name'
op|'('
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|')'
newline|'\n'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'sadd'
op|'('
name|'set_name'
op|','
name|'self'
op|'.'
name|'identifier'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'absorb_connection_error'
newline|'\n'
DECL|member|remove_from_index
name|'def'
name|'remove_from_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove id of this instance from the set tracking ids of this type"""'
newline|'\n'
name|'set_name'
op|'='
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_redis_set_name'
op|'('
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|')'
newline|'\n'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'srem'
op|'('
name|'set_name'
op|','
name|'self'
op|'.'
name|'identifier'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'absorb_connection_error'
newline|'\n'
DECL|member|associate_with
name|'def'
name|'associate_with'
op|'('
name|'self'
op|','
name|'foreign_type'
op|','
name|'foreign_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add this class id into the set foreign_type:foreign_id:this_types"""'
newline|'\n'
comment|"# note the extra 's' on the end is for plurality"
nl|'\n'
comment|'# to match the old data without requiring a migration of any sort'
nl|'\n'
name|'self'
op|'.'
name|'add_associated_model_to_its_set'
op|'('
name|'foreign_type'
op|','
name|'foreign_id'
op|')'
newline|'\n'
name|'redis_set'
op|'='
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_redis_association_name'
op|'('
name|'foreign_type'
op|','
nl|'\n'
name|'foreign_id'
op|')'
newline|'\n'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'sadd'
op|'('
name|'redis_set'
op|','
name|'self'
op|'.'
name|'identifier'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'absorb_connection_error'
newline|'\n'
DECL|member|unassociate_with
name|'def'
name|'unassociate_with'
op|'('
name|'self'
op|','
name|'foreign_type'
op|','
name|'foreign_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete from foreign_type:foreign_id:this_types set"""'
newline|'\n'
name|'redis_set'
op|'='
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_redis_association_name'
op|'('
name|'foreign_type'
op|','
nl|'\n'
name|'foreign_id'
op|')'
newline|'\n'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'srem'
op|'('
name|'redis_set'
op|','
name|'self'
op|'.'
name|'identifier'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_associated_model_to_its_set
dedent|''
name|'def'
name|'add_associated_model_to_its_set'
op|'('
name|'self'
op|','
name|'model_type'
op|','
name|'model_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        When associating an X to a Y, save Y for newer timestamp, etc, and to\n        make sure to save it if Y is a new record.\n        If the model_type isn\'t found as a usable class, ignore it, this can\n        happen when associating to things stored in LDAP (user, project, ...).\n        """'
newline|'\n'
name|'table'
op|'='
name|'globals'
op|'('
op|')'
newline|'\n'
name|'klsname'
op|'='
name|'model_type'
op|'.'
name|'capitalize'
op|'('
op|')'
newline|'\n'
name|'if'
name|'table'
op|'.'
name|'has_key'
op|'('
name|'klsname'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'model_class'
op|'='
name|'table'
op|'['
name|'klsname'
op|']'
newline|'\n'
name|'model_inst'
op|'='
name|'model_class'
op|'('
name|'model_id'
op|')'
newline|'\n'
name|'model_inst'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'absorb_connection_error'
newline|'\n'
DECL|member|save
name|'def'
name|'save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        update the directory with the state from this model\n        also add it to the index of items of the same type\n        then set the initial_state = state so new changes are tracked\n        """'
newline|'\n'
comment|'# TODO(ja): implement hmset in redis-py and use it'
nl|'\n'
comment|'# instead of multiple calls to hset'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'is_new_record'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|'"create_time"'
op|']'
op|'='
name|'utils'
op|'.'
name|'isotime'
op|'('
op|')'
newline|'\n'
dedent|''
name|'for'
name|'key'
op|','
name|'val'
name|'in'
name|'self'
op|'.'
name|'state'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'hset'
op|'('
name|'self'
op|'.'
name|'__redis_key'
op|','
name|'key'
op|','
name|'val'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'add_to_index'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'initial_state'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'state'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'absorb_connection_error'
newline|'\n'
DECL|member|destroy
name|'def'
name|'destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""deletes all related records from datastore."""'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|'"Destroying datamodel for %s %s"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|','
name|'self'
op|'.'
name|'identifier'
op|')'
newline|'\n'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'__redis_key'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'remove_from_index'
op|'('
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
