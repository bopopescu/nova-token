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
string|'"""\nSQLAlchemy models for nova data\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
comment|'# TODO(vish): clean up these imports'
nl|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'orm'
name|'import'
name|'relationship'
op|','
name|'backref'
op|','
name|'validates'
op|','
name|'exc'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'sql'
name|'import'
name|'func'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Column'
op|','
name|'Integer'
op|','
name|'String'
op|','
name|'Table'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'ForeignKey'
op|','
name|'DateTime'
op|','
name|'Boolean'
op|','
name|'Text'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'ext'
op|'.'
name|'declarative'
name|'import'
name|'declarative_base'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'session'
name|'import'
name|'get_session'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'auth'
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
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|BASE
name|'BASE'
op|'='
name|'declarative_base'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaBase
name|'class'
name|'NovaBase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for Nova Models"""'
newline|'\n'
DECL|variable|__table_args__
name|'__table_args__'
op|'='
op|'{'
string|"'mysql_engine'"
op|':'
string|"'InnoDB'"
op|'}'
newline|'\n'
DECL|variable|__table_initialized__
name|'__table_initialized__'
op|'='
name|'False'
newline|'\n'
DECL|variable|__prefix__
name|'__prefix__'
op|'='
string|"'none'"
newline|'\n'
DECL|variable|created_at
name|'created_at'
op|'='
name|'Column'
op|'('
name|'DateTime'
op|','
name|'default'
op|'='
name|'func'
op|'.'
name|'now'
op|'('
op|')'
op|')'
newline|'\n'
DECL|variable|updated_at
name|'updated_at'
op|'='
name|'Column'
op|'('
name|'DateTime'
op|','
name|'onupdate'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'now'
op|')'
newline|'\n'
DECL|variable|deleted
name|'deleted'
op|'='
name|'Column'
op|'('
name|'Boolean'
op|','
name|'default'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|all
name|'def'
name|'all'
op|'('
name|'cls'
op|','
name|'session'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get all objects of this type"""'
newline|'\n'
name|'if'
name|'not'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'='
name|'get_session'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'session'
op|'.'
name|'query'
op|'('
name|'cls'
nl|'\n'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'deleted'
op|'='
name|'False'
nl|'\n'
op|')'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|count
name|'def'
name|'count'
op|'('
name|'cls'
op|','
name|'session'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Count objects of this type"""'
newline|'\n'
name|'if'
name|'not'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'='
name|'get_session'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'session'
op|'.'
name|'query'
op|'('
name|'cls'
nl|'\n'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'deleted'
op|'='
name|'False'
nl|'\n'
op|')'
op|'.'
name|'count'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|find
name|'def'
name|'find'
op|'('
name|'cls'
op|','
name|'obj_id'
op|','
name|'session'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find object by id"""'
newline|'\n'
name|'if'
name|'not'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'='
name|'get_session'
op|'('
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'session'
op|'.'
name|'query'
op|'('
name|'cls'
nl|'\n'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'id'
op|'='
name|'obj_id'
nl|'\n'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'deleted'
op|'='
name|'False'
nl|'\n'
op|')'
op|'.'
name|'one'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exc'
op|'.'
name|'NoResultFound'
op|':'
newline|'\n'
indent|'            '
name|'new_exc'
op|'='
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"No model for id %s"'
op|'%'
name|'obj_id'
op|')'
newline|'\n'
name|'raise'
name|'new_exc'
op|'.'
name|'__class__'
op|','
name|'new_exc'
op|','
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|'['
number|'2'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|find_by_str
name|'def'
name|'find_by_str'
op|'('
name|'cls'
op|','
name|'str_id'
op|','
name|'session'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find object by str_id"""'
newline|'\n'
name|'int_id'
op|'='
name|'int'
op|'('
name|'str_id'
op|'.'
name|'rpartition'
op|'('
string|"'-'"
op|')'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'find'
op|'('
name|'int_id'
op|','
name|'session'
op|'='
name|'session'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|str_id
name|'def'
name|'str_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get string id of object (generally prefix + \'-\' + id)"""'
newline|'\n'
name|'return'
string|'"%s-%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'__prefix__'
op|','
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|save
dedent|''
name|'def'
name|'save'
op|'('
name|'self'
op|','
name|'session'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Save this object"""'
newline|'\n'
name|'if'
name|'not'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'='
name|'get_session'
op|'('
op|')'
newline|'\n'
dedent|''
name|'session'
op|'.'
name|'add'
op|'('
name|'self'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'session'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete this object"""'
newline|'\n'
name|'self'
op|'.'
name|'deleted'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'save'
op|'('
name|'session'
op|'='
name|'session'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'setattr'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'getattr'
op|'('
name|'self'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(vish): Store images in the database instead of file system'
nl|'\n'
comment|'#class Image(BASE, NovaBase):'
nl|'\n'
comment|'#    """Represents an image in the datastore"""'
nl|'\n'
comment|"#    __tablename__ = 'images'"
nl|'\n'
comment|"#    __prefix__ = 'ami'"
nl|'\n'
comment|'#    id = Column(Integer, primary_key=True)'
nl|'\n'
comment|'#    user_id = Column(String(255))'
nl|'\n'
comment|'#    project_id = Column(String(255))'
nl|'\n'
comment|'#    image_type = Column(String(255))'
nl|'\n'
comment|'#    public = Column(Boolean, default=False)'
nl|'\n'
comment|'#    state = Column(String(255))'
nl|'\n'
comment|'#    location = Column(String(255))'
nl|'\n'
comment|'#    arch = Column(String(255))'
nl|'\n'
comment|'#    default_kernel_id = Column(String(255))'
nl|'\n'
comment|'#    default_ramdisk_id = Column(String(255))'
nl|'\n'
comment|'#'
nl|'\n'
comment|"#    @validates('image_type')"
nl|'\n'
comment|'#    def validate_image_type(self, key, image_type):'
nl|'\n'
comment|"#        assert(image_type in ['machine', 'kernel', 'ramdisk', 'raw'])"
nl|'\n'
comment|'#'
nl|'\n'
comment|"#    @validates('state')"
nl|'\n'
comment|'#    def validate_state(self, key, state):'
nl|'\n'
comment|"#        assert(state in ['available', 'pending', 'disabled'])"
nl|'\n'
comment|'#'
nl|'\n'
comment|"#    @validates('default_kernel_id')"
nl|'\n'
comment|'#    def validate_kernel_id(self, key, val):'
nl|'\n'
comment|"#        if val != 'machine':"
nl|'\n'
comment|'#            assert(val is None)'
nl|'\n'
comment|'#'
nl|'\n'
comment|"#    @validates('default_ramdisk_id')"
nl|'\n'
comment|'#    def validate_ramdisk_id(self, key, val):'
nl|'\n'
comment|"#        if val != 'machine':"
nl|'\n'
comment|'#            assert(val is None)'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# TODO(vish): To make this into its own table, we need a good place to'
nl|'\n'
comment|'#             create the host entries. In config somwhere? Or the first'
nl|'\n'
comment|'#             time any object sets host? This only becomes particularly'
nl|'\n'
comment|'#             important if we need to store per-host data.'
nl|'\n'
comment|'#class Host(BASE, NovaBase):'
nl|'\n'
comment|'#    """Represents a host where services are running"""'
nl|'\n'
comment|"#    __tablename__ = 'hosts'"
nl|'\n'
comment|'#    id = Column(String(255), primary_key=True)'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#'
nl|'\n'
DECL|class|Service
dedent|''
dedent|''
name|'class'
name|'Service'
op|'('
name|'BASE'
op|','
name|'NovaBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a running service on a host"""'
newline|'\n'
DECL|variable|__tablename__
name|'__tablename__'
op|'='
string|"'services'"
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|host
name|'host'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
comment|"# , ForeignKey('hosts.id'))"
newline|'\n'
DECL|variable|binary
name|'binary'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|topic
name|'topic'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|report_count
name|'report_count'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'nullable'
op|'='
name|'False'
op|','
name|'default'
op|'='
number|'0'
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|find_by_args
name|'def'
name|'find_by_args'
op|'('
name|'cls'
op|','
name|'host'
op|','
name|'binary'
op|','
name|'session'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'='
name|'get_session'
op|'('
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'session'
op|'.'
name|'query'
op|'('
name|'cls'
nl|'\n'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'host'
op|'='
name|'host'
nl|'\n'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'binary'
op|'='
name|'binary'
nl|'\n'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'deleted'
op|'='
name|'False'
nl|'\n'
op|')'
op|'.'
name|'one'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exc'
op|'.'
name|'NoResultFound'
op|':'
newline|'\n'
indent|'            '
name|'new_exc'
op|'='
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"No model for %s, %s"'
op|'%'
op|'('
name|'host'
op|','
nl|'\n'
name|'binary'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'new_exc'
op|'.'
name|'__class__'
op|','
name|'new_exc'
op|','
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|'['
number|'2'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Instance
dedent|''
dedent|''
dedent|''
name|'class'
name|'Instance'
op|'('
name|'BASE'
op|','
name|'NovaBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a guest vm"""'
newline|'\n'
DECL|variable|__tablename__
name|'__tablename__'
op|'='
string|"'instances'"
newline|'\n'
DECL|variable|__prefix__
name|'__prefix__'
op|'='
string|"'i'"
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|user_id
name|'user_id'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|project_id
name|'project_id'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'property'
newline|'\n'
DECL|member|user
name|'def'
name|'user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'auth'
op|'.'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_user'
op|'('
name|'self'
op|'.'
name|'user_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|project
name|'def'
name|'project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'auth'
op|'.'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_project'
op|'('
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|name
name|'def'
name|'name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'str_id'
newline|'\n'
nl|'\n'
DECL|variable|image_id
dedent|''
name|'image_id'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|kernel_id
name|'kernel_id'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|ramdisk_id
name|'ramdisk_id'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
comment|"#    image_id = Column(Integer, ForeignKey('images.id'), nullable=True)"
nl|'\n'
comment|"#    kernel_id = Column(Integer, ForeignKey('images.id'), nullable=True)"
nl|'\n'
comment|"#    ramdisk_id = Column(Integer, ForeignKey('images.id'), nullable=True)"
nl|'\n'
comment|"#    ramdisk = relationship(Ramdisk, backref=backref('instances', order_by=id))"
nl|'\n'
comment|"#    kernel = relationship(Kernel, backref=backref('instances', order_by=id))"
nl|'\n'
comment|"#    project = relationship(Project, backref=backref('instances', order_by=id))"
nl|'\n'
nl|'\n'
DECL|variable|launch_index
name|'launch_index'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|key_name
name|'key_name'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|key_data
name|'key_data'
op|'='
name|'Column'
op|'('
name|'Text'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|state
name|'state'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|state_description
name|'state_description'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|hostname
name|'hostname'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|host
name|'host'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
comment|"# , ForeignKey('hosts.id'))"
newline|'\n'
nl|'\n'
DECL|variable|instance_type
name|'instance_type'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|user_data
name|'user_data'
op|'='
name|'Column'
op|'('
name|'Text'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|reservation_id
name|'reservation_id'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|mac_address
name|'mac_address'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# TODO(vish): see Ewan's email about state improvements, probably"
nl|'\n'
comment|'#             should be in a driver base class or some such'
nl|'\n'
comment|'# vmstate_state = running, halted, suspended, paused'
nl|'\n'
comment|'# power_state = what we have'
nl|'\n'
comment|'# task_state = transitory and may trigger power state transition'
nl|'\n'
nl|'\n'
comment|"#@validates('state')"
nl|'\n'
comment|'#def validate_state(self, key, state):'
nl|'\n'
comment|"#    assert(state in ['nostate', 'running', 'blocked', 'paused',"
nl|'\n'
comment|"#                     'shutdown', 'shutoff', 'crashed'])"
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|Volume
dedent|''
name|'class'
name|'Volume'
op|'('
name|'BASE'
op|','
name|'NovaBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a block storage device that can be attached to a vm"""'
newline|'\n'
DECL|variable|__tablename__
name|'__tablename__'
op|'='
string|"'volumes'"
newline|'\n'
DECL|variable|__prefix__
name|'__prefix__'
op|'='
string|"'vol'"
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|user_id
name|'user_id'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|project_id
name|'project_id'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|host
name|'host'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
comment|"# , ForeignKey('hosts.id'))"
newline|'\n'
DECL|variable|size
name|'size'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|availability_zone
name|'availability_zone'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
comment|'# TODO(vish): foreign key?'
newline|'\n'
DECL|variable|instance_id
name|'instance_id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'ForeignKey'
op|'('
string|"'instances.id'"
op|')'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|instance
name|'instance'
op|'='
name|'relationship'
op|'('
name|'Instance'
op|','
name|'backref'
op|'='
name|'backref'
op|'('
string|"'volumes'"
op|')'
op|')'
newline|'\n'
DECL|variable|mountpoint
name|'mountpoint'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|attach_time
name|'attach_time'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
comment|'# TODO(vish): datetime'
newline|'\n'
DECL|variable|status
name|'status'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
comment|'# TODO(vish): enum?'
newline|'\n'
DECL|variable|attach_status
name|'attach_status'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
comment|'# TODO(vish): enum'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExportDevice
dedent|''
name|'class'
name|'ExportDevice'
op|'('
name|'BASE'
op|','
name|'NovaBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represates a shelf and blade that a volume can be exported on"""'
newline|'\n'
DECL|variable|__tablename__
name|'__tablename__'
op|'='
string|"'export_devices'"
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|shelf_id
name|'shelf_id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|blade_id
name|'blade_id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|volume_id
name|'volume_id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'ForeignKey'
op|'('
string|"'volumes.id'"
op|')'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|volume
name|'volume'
op|'='
name|'relationship'
op|'('
name|'Volume'
op|','
name|'backref'
op|'='
name|'backref'
op|'('
string|"'export_device'"
op|','
nl|'\n'
DECL|variable|uselist
name|'uselist'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|security_group_instance_association
dedent|''
name|'security_group_instance_association'
op|'='
name|'Table'
op|'('
string|"'security_group_instance_association'"
op|','
nl|'\n'
name|'BASE'
op|'.'
name|'metadata'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'security_group_id'"
op|','
name|'Integer'
op|','
nl|'\n'
name|'ForeignKey'
op|'('
string|"'security_group.id'"
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'instance_id'"
op|','
name|'Integer'
op|','
nl|'\n'
name|'ForeignKey'
op|'('
string|"'instances.id'"
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|class|SecurityGroup
name|'class'
name|'SecurityGroup'
op|'('
name|'BASE'
op|','
name|'NovaBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a security group"""'
newline|'\n'
DECL|variable|__tablename__
name|'__tablename__'
op|'='
string|"'security_group'"
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|description
name|'description'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|user_id
name|'user_id'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|project_id
name|'project_id'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|instances
name|'instances'
op|'='
name|'relationship'
op|'('
name|'Instance'
op|','
nl|'\n'
DECL|variable|secondary
name|'secondary'
op|'='
name|'security_group_instance_association'
op|','
nl|'\n'
DECL|variable|backref
name|'backref'
op|'='
string|"'security_groups'"
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'property'
newline|'\n'
DECL|member|user
name|'def'
name|'user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'auth'
op|'.'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_user'
op|'('
name|'self'
op|'.'
name|'user_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|project
name|'def'
name|'project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'auth'
op|'.'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_project'
op|'('
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupIngressRule
dedent|''
dedent|''
name|'class'
name|'SecurityGroupIngressRule'
op|'('
name|'BASE'
op|','
name|'NovaBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a rule in a security group"""'
newline|'\n'
DECL|variable|__tablename__
name|'__tablename__'
op|'='
string|"'security_group_rules'"
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|parent_group_id
name|'parent_group_id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'ForeignKey'
op|'('
string|"'security_group.id'"
op|')'
op|')'
newline|'\n'
DECL|variable|parent_group
name|'parent_group'
op|'='
name|'relationship'
op|'('
string|'"SecurityGroup"'
op|','
name|'backref'
op|'='
string|'"rules"'
op|','
nl|'\n'
DECL|variable|foreign_keys
name|'foreign_keys'
op|'='
name|'parent_group_id'
op|','
nl|'\n'
name|'primaryjoin'
op|'='
name|'parent_group_id'
op|'=='
name|'SecurityGroup'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|protocol
name|'protocol'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'5'
op|')'
op|')'
comment|'# "tcp", "udp", or "icmp"'
newline|'\n'
DECL|variable|from_port
name|'from_port'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|to_port
name|'to_port'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|cidr
name|'cidr'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# Note: This is not the parent SecurityGroup. It's SecurityGroup we're"
nl|'\n'
comment|'# granting access for.'
nl|'\n'
DECL|variable|group_id
name|'group_id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'ForeignKey'
op|'('
string|"'security_group.id'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Network
dedent|''
name|'class'
name|'Network'
op|'('
name|'BASE'
op|','
name|'NovaBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a network"""'
newline|'\n'
DECL|variable|__tablename__
name|'__tablename__'
op|'='
string|"'networks'"
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|injected
name|'injected'
op|'='
name|'Column'
op|'('
name|'Boolean'
op|','
name|'default'
op|'='
name|'False'
op|')'
newline|'\n'
DECL|variable|cidr
name|'cidr'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|netmask
name|'netmask'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|bridge
name|'bridge'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|gateway
name|'gateway'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|broadcast
name|'broadcast'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|dns
name|'dns'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|vlan
name|'vlan'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|vpn_public_address
name|'vpn_public_address'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|vpn_public_port
name|'vpn_public_port'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|vpn_private_address
name|'vpn_private_address'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|dhcp_start
name|'dhcp_start'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|project_id
name|'project_id'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|host
name|'host'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
comment|"# , ForeignKey('hosts.id'))"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkIndex
dedent|''
name|'class'
name|'NetworkIndex'
op|'('
name|'BASE'
op|','
name|'NovaBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a unique offset for a network\n\n    Currently vlan number, vpn port, and fixed ip ranges are keyed off of\n    this index. These may ultimately need to be converted to separate\n    pools.\n    """'
newline|'\n'
DECL|variable|__tablename__
name|'__tablename__'
op|'='
string|"'network_indexes'"
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|index
name|'index'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|network_id
name|'network_id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'ForeignKey'
op|'('
string|"'networks.id'"
op|')'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|network
name|'network'
op|'='
name|'relationship'
op|'('
name|'Network'
op|','
name|'backref'
op|'='
name|'backref'
op|'('
string|"'network_index'"
op|','
nl|'\n'
DECL|variable|uselist
name|'uselist'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(vish): can these both come from the same baseclass?'
nl|'\n'
DECL|class|FixedIp
dedent|''
name|'class'
name|'FixedIp'
op|'('
name|'BASE'
op|','
name|'NovaBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a fixed ip for an instance"""'
newline|'\n'
DECL|variable|__tablename__
name|'__tablename__'
op|'='
string|"'fixed_ips'"
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|address
name|'address'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|network_id
name|'network_id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'ForeignKey'
op|'('
string|"'networks.id'"
op|')'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|network
name|'network'
op|'='
name|'relationship'
op|'('
name|'Network'
op|','
name|'backref'
op|'='
name|'backref'
op|'('
string|"'fixed_ips'"
op|')'
op|')'
newline|'\n'
DECL|variable|instance_id
name|'instance_id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'ForeignKey'
op|'('
string|"'instances.id'"
op|')'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|instance
name|'instance'
op|'='
name|'relationship'
op|'('
name|'Instance'
op|','
name|'backref'
op|'='
name|'backref'
op|'('
string|"'fixed_ip'"
op|','
nl|'\n'
DECL|variable|uselist
name|'uselist'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
DECL|variable|allocated
name|'allocated'
op|'='
name|'Column'
op|'('
name|'Boolean'
op|','
name|'default'
op|'='
name|'False'
op|')'
newline|'\n'
DECL|variable|leased
name|'leased'
op|'='
name|'Column'
op|'('
name|'Boolean'
op|','
name|'default'
op|'='
name|'False'
op|')'
newline|'\n'
DECL|variable|reserved
name|'reserved'
op|'='
name|'Column'
op|'('
name|'Boolean'
op|','
name|'default'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'property'
newline|'\n'
DECL|member|str_id
name|'def'
name|'str_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'address'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|find_by_str
name|'def'
name|'find_by_str'
op|'('
name|'cls'
op|','
name|'str_id'
op|','
name|'session'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'='
name|'get_session'
op|'('
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'session'
op|'.'
name|'query'
op|'('
name|'cls'
nl|'\n'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'address'
op|'='
name|'str_id'
nl|'\n'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'deleted'
op|'='
name|'False'
nl|'\n'
op|')'
op|'.'
name|'one'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exc'
op|'.'
name|'NoResultFound'
op|':'
newline|'\n'
indent|'            '
name|'new_exc'
op|'='
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"No model for address %s"'
op|'%'
name|'str_id'
op|')'
newline|'\n'
name|'raise'
name|'new_exc'
op|'.'
name|'__class__'
op|','
name|'new_exc'
op|','
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|'['
number|'2'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIp
dedent|''
dedent|''
dedent|''
name|'class'
name|'FloatingIp'
op|'('
name|'BASE'
op|','
name|'NovaBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a floating ip that dynamically forwards to a fixed ip"""'
newline|'\n'
DECL|variable|__tablename__
name|'__tablename__'
op|'='
string|"'floating_ips'"
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|address
name|'address'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|fixed_ip_id
name|'fixed_ip_id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'ForeignKey'
op|'('
string|"'fixed_ips.id'"
op|')'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|fixed_ip
name|'fixed_ip'
op|'='
name|'relationship'
op|'('
name|'FixedIp'
op|','
name|'backref'
op|'='
name|'backref'
op|'('
string|"'floating_ips'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|project_id
name|'project_id'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|host
name|'host'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
comment|"# , ForeignKey('hosts.id'))"
newline|'\n'
nl|'\n'
op|'@'
name|'property'
newline|'\n'
DECL|member|str_id
name|'def'
name|'str_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'address'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|find_by_str
name|'def'
name|'find_by_str'
op|'('
name|'cls'
op|','
name|'str_id'
op|','
name|'session'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'='
name|'get_session'
op|'('
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'session'
op|'.'
name|'query'
op|'('
name|'cls'
nl|'\n'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'address'
op|'='
name|'str_id'
nl|'\n'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'deleted'
op|'='
name|'False'
nl|'\n'
op|')'
op|'.'
name|'one'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exc'
op|'.'
name|'NoResultFound'
op|':'
newline|'\n'
indent|'            '
name|'new_exc'
op|'='
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"No model for address %s"'
op|'%'
name|'str_id'
op|')'
newline|'\n'
name|'raise'
name|'new_exc'
op|'.'
name|'__class__'
op|','
name|'new_exc'
op|','
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|'['
number|'2'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_models
dedent|''
dedent|''
dedent|''
name|'def'
name|'register_models'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Register Models and create metadata"""'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'create_engine'
newline|'\n'
name|'models'
op|'='
op|'('
name|'Service'
op|','
name|'Instance'
op|','
name|'Volume'
op|','
name|'ExportDevice'
op|','
name|'FixedIp'
op|','
name|'FloatingIp'
op|','
nl|'\n'
name|'Network'
op|','
name|'NetworkIndex'
op|','
name|'SecurityGroup'
op|','
name|'SecurityGroupIngressRule'
op|')'
newline|'\n'
comment|'# , Image, Host'
nl|'\n'
name|'engine'
op|'='
name|'create_engine'
op|'('
name|'FLAGS'
op|'.'
name|'sql_connection'
op|','
name|'echo'
op|'='
name|'False'
op|')'
newline|'\n'
name|'for'
name|'model'
name|'in'
name|'models'
op|':'
newline|'\n'
indent|'        '
name|'model'
op|'.'
name|'metadata'
op|'.'
name|'create_all'
op|'('
name|'engine'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
