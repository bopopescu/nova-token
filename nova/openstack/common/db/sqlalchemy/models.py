begin_unit
comment|'# Copyright (c) 2011 X.commerce, a business unit of eBay Inc.'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright 2011 Piston Cloud Computing, Inc.'
nl|'\n'
comment|'# Copyright 2012 Cloudscaling Group, Inc.'
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
string|'"""\nSQLAlchemy models.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Column'
op|','
name|'Integer'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'DateTime'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'orm'
name|'import'
name|'object_mapper'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ModelBase
name|'class'
name|'ModelBase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for models."""'
newline|'\n'
DECL|variable|__table_initialized__
name|'__table_initialized__'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|save
name|'def'
name|'save'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Save this object."""'
newline|'\n'
nl|'\n'
comment|'# NOTE(boris-42): This part of code should be look like:'
nl|'\n'
comment|'#                       session.add(self)'
nl|'\n'
comment|'#                       session.flush()'
nl|'\n'
comment|'#                 But there is a bug in sqlalchemy and eventlet that'
nl|'\n'
comment|'#                 raises NoneType exception if there is no running'
nl|'\n'
comment|'#                 transaction and rollback is called. As long as'
nl|'\n'
comment|'#                 sqlalchemy has this bug we have to create transaction'
nl|'\n'
comment|'#                 explicitly.'
nl|'\n'
name|'with'
name|'session'
op|'.'
name|'begin'
op|'('
name|'subtransactions'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
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
DECL|member|__setitem__
dedent|''
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
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'default'
op|'='
name|'None'
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
op|','
name|'default'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|_extra_keys
name|'def'
name|'_extra_keys'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Specifies custom fields\n\n        Subclasses can override this property to return a list\n        of custom fields that should be included in their dict\n        representation.\n\n        For reference check tests/db/sqlalchemy/test_models.py\n        """'
newline|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|__iter__
dedent|''
name|'def'
name|'__iter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'columns'
op|'='
name|'dict'
op|'('
name|'object_mapper'
op|'('
name|'self'
op|')'
op|'.'
name|'columns'
op|')'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(russellb): Allow models to specify other keys that can be looked'
nl|'\n'
comment|"# up, beyond the actual db columns.  An example would be the 'name'"
nl|'\n'
comment|'# property for an Instance.'
nl|'\n'
name|'columns'
op|'.'
name|'extend'
op|'('
name|'self'
op|'.'
name|'_extra_keys'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_i'
op|'='
name|'iter'
op|'('
name|'columns'
op|')'
newline|'\n'
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|next
dedent|''
name|'def'
name|'next'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'n'
op|'='
name|'six'
op|'.'
name|'advance_iterator'
op|'('
name|'self'
op|'.'
name|'_i'
op|')'
newline|'\n'
name|'return'
name|'n'
op|','
name|'getattr'
op|'('
name|'self'
op|','
name|'n'
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
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make the model object behave like a dict."""'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'values'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
nl|'\n'
DECL|member|iteritems
dedent|''
dedent|''
name|'def'
name|'iteritems'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make the model object behave like a dict.\n\n        Includes attributes from joins.\n        """'
newline|'\n'
name|'local'
op|'='
name|'dict'
op|'('
name|'self'
op|')'
newline|'\n'
name|'joined'
op|'='
name|'dict'
op|'('
op|'['
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'self'
op|'.'
name|'__dict__'
op|')'
nl|'\n'
name|'if'
name|'not'
name|'k'
op|'['
number|'0'
op|']'
op|'=='
string|"'_'"
op|']'
op|')'
newline|'\n'
name|'local'
op|'.'
name|'update'
op|'('
name|'joined'
op|')'
newline|'\n'
name|'return'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'local'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TimestampMixin
dedent|''
dedent|''
name|'class'
name|'TimestampMixin'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|created_at
indent|'    '
name|'created_at'
op|'='
name|'Column'
op|'('
name|'DateTime'
op|','
name|'default'
op|'='
name|'lambda'
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
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
name|'lambda'
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SoftDeleteMixin
dedent|''
name|'class'
name|'SoftDeleteMixin'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|deleted_at
indent|'    '
name|'deleted_at'
op|'='
name|'Column'
op|'('
name|'DateTime'
op|')'
newline|'\n'
DECL|variable|deleted
name|'deleted'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'default'
op|'='
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|soft_delete
name|'def'
name|'soft_delete'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Mark this object as deleted."""'
newline|'\n'
name|'self'
op|'.'
name|'deleted'
op|'='
name|'self'
op|'.'
name|'id'
newline|'\n'
name|'self'
op|'.'
name|'deleted_at'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
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
dedent|''
dedent|''
endmarker|''
end_unit
