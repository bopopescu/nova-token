begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2011 Cloudscaling Group, Inc'
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
string|'"""\nThe MatchMaker classes should except a Topic or Fanout exchange key and\nreturn keys for direct exchanges, per (approximate) AMQP parlance.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'contextlib'
newline|'\n'
name|'import'
name|'itertools'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
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
nl|'\n'
DECL|variable|matchmaker_opts
name|'matchmaker_opts'
op|'='
op|'['
nl|'\n'
comment|'# Matchmaker ring file'
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'matchmaker_ringfile'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'/etc/nova/matchmaker_ring.json'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Matchmaker ring file (JSON)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'matchmaker_heartbeat_freq'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'300'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Heartbeat frequency'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'matchmaker_heartbeat_ttl'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Heartbeat time-to-live.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'matchmaker_opts'
op|')'
newline|'\n'
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
DECL|variable|contextmanager
name|'contextmanager'
op|'='
name|'contextlib'
op|'.'
name|'contextmanager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MatchMakerException
name|'class'
name|'MatchMakerException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Signified a match could not be found."""'
newline|'\n'
DECL|variable|message
name|'message'
op|'='
name|'_'
op|'('
string|'"Match not found by MatchMaker."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Exchange
dedent|''
name|'class'
name|'Exchange'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Implements lookups.\n    Subclass this to support hashtables, dns, etc.\n    """'
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
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|run
dedent|''
name|'def'
name|'run'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Binding
dedent|''
dedent|''
name|'class'
name|'Binding'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A binding on which to perform a lookup.\n    """'
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
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|test
dedent|''
name|'def'
name|'test'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MatchMakerBase
dedent|''
dedent|''
name|'class'
name|'MatchMakerBase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Match Maker Base Class.\n    Build off HeartbeatMatchMakerBase if building a\n    heartbeat-capable MatchMaker.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Array of tuples. Index [2] toggles negation, [3] is last-if-true'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'bindings'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'no_heartbeat_msg'
op|'='
name|'_'
op|'('
string|"'Matchmaker does not implement '"
nl|'\n'
string|"'registration or heartbeat.'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|register
dedent|''
name|'def'
name|'register'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Register a host on a backend.\n        Heartbeats, if applicable, may keepalive registration.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|ack_alive
dedent|''
name|'def'
name|'ack_alive'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Acknowledge that a key.host is alive.\n        Used internally for updating heartbeats,\n        but may also be used publically to acknowledge\n        a system is alive (i.e. rpc message successfully\n        sent to host)\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|is_alive
dedent|''
name|'def'
name|'is_alive'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Checks if a host is alive.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|expire
dedent|''
name|'def'
name|'expire'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Explicitly expire a host\'s registration.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|send_heartbeats
dedent|''
name|'def'
name|'send_heartbeats'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Send all heartbeats.\n        Use start_heartbeat to spawn a heartbeat greenthread,\n        which loops this method.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|unregister
dedent|''
name|'def'
name|'unregister'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Unregister a topic.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|start_heartbeat
dedent|''
name|'def'
name|'start_heartbeat'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Spawn heartbeat greenthread.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|stop_heartbeat
dedent|''
name|'def'
name|'stop_heartbeat'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Destroys the heartbeat greenthread.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|add_binding
dedent|''
name|'def'
name|'add_binding'
op|'('
name|'self'
op|','
name|'binding'
op|','
name|'rule'
op|','
name|'last'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'bindings'
op|'.'
name|'append'
op|'('
op|'('
name|'binding'
op|','
name|'rule'
op|','
name|'False'
op|','
name|'last'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'#NOTE(ewindisch): kept the following method in case we implement the'
nl|'\n'
comment|'#                 underlying support.'
nl|'\n'
comment|'#def add_negate_binding(self, binding, rule, last=True):'
nl|'\n'
comment|'#    self.bindings.append((binding, rule, True, last))'
nl|'\n'
nl|'\n'
DECL|member|queues
dedent|''
name|'def'
name|'queues'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'workers'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|'# bit is for negate bindings - if we choose to implement it.'
nl|'\n'
comment|'# last stops processing rules if this matches.'
nl|'\n'
name|'for'
op|'('
name|'binding'
op|','
name|'exchange'
op|','
name|'bit'
op|','
name|'last'
op|')'
name|'in'
name|'self'
op|'.'
name|'bindings'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'binding'
op|'.'
name|'test'
op|'('
name|'key'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'workers'
op|'.'
name|'extend'
op|'('
name|'exchange'
op|'.'
name|'run'
op|'('
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Support last.'
nl|'\n'
name|'if'
name|'last'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'workers'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'workers'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HeartbeatMatchMakerBase
dedent|''
dedent|''
name|'class'
name|'HeartbeatMatchMakerBase'
op|'('
name|'MatchMakerBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Base for a heart-beat capable MatchMaker.\n    Provides common methods for registering,\n    unregistering, and maintaining heartbeats.\n    """'
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
name|'self'
op|'.'
name|'hosts'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_heart'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'host_topic'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'HeartbeatMatchMakerBase'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|send_heartbeats
dedent|''
name|'def'
name|'send_heartbeats'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Send all heartbeats.\n        Use start_heartbeat to spawn a heartbeat greenthread,\n        which loops this method.\n        """'
newline|'\n'
name|'for'
name|'key'
op|','
name|'host'
name|'in'
name|'self'
op|'.'
name|'host_topic'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ack_alive'
op|'('
name|'key'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|ack_alive
dedent|''
dedent|''
name|'def'
name|'ack_alive'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Acknowledge that a host.topic is alive.\n        Used internally for updating heartbeats,\n        but may also be used publically to acknowledge\n        a system is alive (i.e. rpc message successfully\n        sent to host)\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|'"Must implement ack_alive"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|backend_register
dedent|''
name|'def'
name|'backend_register'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Implements registration logic.\n        Called by register(self,key,host)\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|'"Must implement backend_register"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|backend_unregister
dedent|''
name|'def'
name|'backend_unregister'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'key_host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Implements de-registration logic.\n        Called by unregister(self,key,host)\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|'"Must implement backend_unregister"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|register
dedent|''
name|'def'
name|'register'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Register a host on a backend.\n        Heartbeats, if applicable, may keepalive registration.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'hosts'
op|'.'
name|'add'
op|'('
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_topic'
op|'['
op|'('
name|'key'
op|','
name|'host'
op|')'
op|']'
op|'='
name|'host'
newline|'\n'
name|'key_host'
op|'='
string|"'.'"
op|'.'
name|'join'
op|'('
op|'('
name|'key'
op|','
name|'host'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'backend_register'
op|'('
name|'key'
op|','
name|'key_host'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ack_alive'
op|'('
name|'key'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unregister
dedent|''
name|'def'
name|'unregister'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Unregister a topic.\n        """'
newline|'\n'
name|'if'
op|'('
name|'key'
op|','
name|'host'
op|')'
name|'in'
name|'self'
op|'.'
name|'host_topic'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'self'
op|'.'
name|'host_topic'
op|'['
op|'('
name|'key'
op|','
name|'host'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'hosts'
op|'.'
name|'discard'
op|'('
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'backend_unregister'
op|'('
name|'key'
op|','
string|"'.'"
op|'.'
name|'join'
op|'('
op|'('
name|'key'
op|','
name|'host'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Matchmaker unregistered: %s, %s"'
op|'%'
op|'('
name|'key'
op|','
name|'host'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|start_heartbeat
dedent|''
name|'def'
name|'start_heartbeat'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Implementation of MatchMakerBase.start_heartbeat\n        Launches greenthread looping send_heartbeats(),\n        yielding for CONF.matchmaker_heartbeat_freq seconds\n        between iterations.\n        """'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'self'
op|'.'
name|'hosts'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'MatchMakerException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Register before starting heartbeat."'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|do_heartbeat
dedent|''
name|'def'
name|'do_heartbeat'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'send_heartbeats'
op|'('
op|')'
newline|'\n'
name|'eventlet'
op|'.'
name|'sleep'
op|'('
name|'CONF'
op|'.'
name|'matchmaker_heartbeat_freq'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_heart'
op|'='
name|'eventlet'
op|'.'
name|'spawn'
op|'('
name|'do_heartbeat'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop_heartbeat
dedent|''
name|'def'
name|'stop_heartbeat'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Destroys the heartbeat greenthread.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_heart'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_heart'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DirectBinding
dedent|''
dedent|''
dedent|''
name|'class'
name|'DirectBinding'
op|'('
name|'Binding'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Specifies a host in the key via a \'.\' character\n    Although dots are used in the key, the behavior here is\n    that it maps directly to a host, thus direct.\n    """'
newline|'\n'
DECL|member|test
name|'def'
name|'test'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'.'"
name|'in'
name|'key'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TopicBinding
dedent|''
dedent|''
name|'class'
name|'TopicBinding'
op|'('
name|'Binding'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Where a \'bare\' key without dots.\n    AMQP generally considers topic exchanges to be those *with* dots,\n    but we deviate here in terminology as the behavior here matches\n    that of a topic exchange (whereas where there are dots, behavior\n    matches that of a direct exchange.\n    """'
newline|'\n'
DECL|member|test
name|'def'
name|'test'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'.'"
name|'not'
name|'in'
name|'key'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FanoutBinding
dedent|''
dedent|''
name|'class'
name|'FanoutBinding'
op|'('
name|'Binding'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Match on fanout keys, where key starts with \'fanout.\' string."""'
newline|'\n'
DECL|member|test
name|'def'
name|'test'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
op|'.'
name|'startswith'
op|'('
string|"'fanout~'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|StubExchange
dedent|''
dedent|''
name|'class'
name|'StubExchange'
op|'('
name|'Exchange'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Exchange that does nothing."""'
newline|'\n'
DECL|member|run
name|'def'
name|'run'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|'('
name|'key'
op|','
name|'None'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RingExchange
dedent|''
dedent|''
name|'class'
name|'RingExchange'
op|'('
name|'Exchange'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Match Maker where hosts are loaded from a static file containing\n    a hashmap (JSON formatted).\n\n    __init__ takes optional ring dictionary argument, otherwise\n    loads the ringfile from CONF.mathcmaker_ringfile.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ring'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'RingExchange'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'ring'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ring'
op|'='
name|'ring'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'fh'
op|'='
name|'open'
op|'('
name|'CONF'
op|'.'
name|'matchmaker_ringfile'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ring'
op|'='
name|'json'
op|'.'
name|'load'
op|'('
name|'fh'
op|')'
newline|'\n'
name|'fh'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'ring0'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'self'
op|'.'
name|'ring'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ring0'
op|'['
name|'k'
op|']'
op|'='
name|'itertools'
op|'.'
name|'cycle'
op|'('
name|'self'
op|'.'
name|'ring'
op|'['
name|'k'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_ring_has
dedent|''
dedent|''
name|'def'
name|'_ring_has'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
name|'in'
name|'self'
op|'.'
name|'ring0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RoundRobinRingExchange
dedent|''
dedent|''
name|'class'
name|'RoundRobinRingExchange'
op|'('
name|'RingExchange'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A Topic Exchange based on a hashmap."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ring'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'RoundRobinRingExchange'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'ring'
op|')'
newline|'\n'
nl|'\n'
DECL|member|run
dedent|''
name|'def'
name|'run'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_ring_has'
op|'('
name|'key'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"No key defining hosts for topic \'%s\', "'
nl|'\n'
string|'"see ringfile"'
op|')'
op|'%'
op|'('
name|'key'
op|','
op|')'
nl|'\n'
op|')'
newline|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
name|'host'
op|'='
name|'next'
op|'('
name|'self'
op|'.'
name|'ring0'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
name|'return'
op|'['
op|'('
name|'key'
op|'+'
string|"'.'"
op|'+'
name|'host'
op|','
name|'host'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FanoutRingExchange
dedent|''
dedent|''
name|'class'
name|'FanoutRingExchange'
op|'('
name|'RingExchange'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fanout Exchange based on a hashmap."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ring'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FanoutRingExchange'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'ring'
op|')'
newline|'\n'
nl|'\n'
DECL|member|run
dedent|''
name|'def'
name|'run'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
comment|'# Assume starts with "fanout~", strip it for lookup.'
nl|'\n'
indent|'        '
name|'nkey'
op|'='
name|'key'
op|'.'
name|'split'
op|'('
string|"'fanout~'"
op|')'
op|'['
number|'1'
op|':'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_ring_has'
op|'('
name|'nkey'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"No key defining hosts for topic \'%s\', "'
nl|'\n'
string|'"see ringfile"'
op|')'
op|'%'
op|'('
name|'nkey'
op|','
op|')'
nl|'\n'
op|')'
newline|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
name|'return'
name|'map'
op|'('
name|'lambda'
name|'x'
op|':'
op|'('
name|'key'
op|'+'
string|"'.'"
op|'+'
name|'x'
op|','
name|'x'
op|')'
op|','
name|'self'
op|'.'
name|'ring'
op|'['
name|'nkey'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LocalhostExchange
dedent|''
dedent|''
name|'class'
name|'LocalhostExchange'
op|'('
name|'Exchange'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Exchange where all direct topics are local."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|'='
string|"'localhost'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'host'
op|'='
name|'host'
newline|'\n'
name|'super'
op|'('
name|'Exchange'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|run
dedent|''
name|'def'
name|'run'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|'('
string|"'.'"
op|'.'
name|'join'
op|'('
op|'('
name|'key'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|'['
number|'0'
op|']'
op|','
name|'self'
op|'.'
name|'host'
op|')'
op|')'
op|','
name|'self'
op|'.'
name|'host'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DirectExchange
dedent|''
dedent|''
name|'class'
name|'DirectExchange'
op|'('
name|'Exchange'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Exchange where all topic keys are split, sending to second half.\n    i.e. "compute.host" sends a message to "compute.host" running on "host"\n    """'
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
name|'super'
op|'('
name|'Exchange'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|run
dedent|''
name|'def'
name|'run'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'e'
op|'='
name|'key'
op|'.'
name|'split'
op|'('
string|"'.'"
op|','
number|'1'
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'return'
op|'['
op|'('
name|'key'
op|','
name|'e'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MatchMakerRing
dedent|''
dedent|''
name|'class'
name|'MatchMakerRing'
op|'('
name|'MatchMakerBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Match Maker where hosts are loaded from a static hashmap.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ring'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'MatchMakerRing'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'add_binding'
op|'('
name|'FanoutBinding'
op|'('
op|')'
op|','
name|'FanoutRingExchange'
op|'('
name|'ring'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'add_binding'
op|'('
name|'DirectBinding'
op|'('
op|')'
op|','
name|'DirectExchange'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'add_binding'
op|'('
name|'TopicBinding'
op|'('
op|')'
op|','
name|'RoundRobinRingExchange'
op|'('
name|'ring'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MatchMakerLocalhost
dedent|''
dedent|''
name|'class'
name|'MatchMakerLocalhost'
op|'('
name|'MatchMakerBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Match Maker where all bare topics resolve to localhost.\n    Useful for testing.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|'='
string|"'localhost'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'MatchMakerLocalhost'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'add_binding'
op|'('
name|'FanoutBinding'
op|'('
op|')'
op|','
name|'LocalhostExchange'
op|'('
name|'host'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'add_binding'
op|'('
name|'DirectBinding'
op|'('
op|')'
op|','
name|'DirectExchange'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'add_binding'
op|'('
name|'TopicBinding'
op|'('
op|')'
op|','
name|'LocalhostExchange'
op|'('
name|'host'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MatchMakerStub
dedent|''
dedent|''
name|'class'
name|'MatchMakerStub'
op|'('
name|'MatchMakerBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Match Maker where topics are untouched.\n    Useful for testing, or for AMQP/brokered queues.\n    Will not work where knowledge of hosts is known (i.e. zeromq)\n    """'
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
name|'super'
op|'('
name|'MatchMakerLocalhost'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'add_binding'
op|'('
name|'FanoutBinding'
op|'('
op|')'
op|','
name|'StubExchange'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'add_binding'
op|'('
name|'DirectBinding'
op|'('
op|')'
op|','
name|'StubExchange'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'add_binding'
op|'('
name|'TopicBinding'
op|'('
op|')'
op|','
name|'StubExchange'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
