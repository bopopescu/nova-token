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
string|'"""\nInstance Monitoring:\n\n    Optionally may be run on each compute node. Provides RRD\n    based statistics and graphs and makes them internally available\n    in the object store.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'boto'
newline|'\n'
name|'import'
name|'boto'
op|'.'
name|'s3'
newline|'\n'
name|'import'
name|'rrdtool'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'task'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'application'
name|'import'
name|'service'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'connection'
name|'as'
name|'virt_connection'
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
name|'DEFINE_integer'
op|'('
string|"'monitoring_instances_delay'"
op|','
number|'5'
op|','
nl|'\n'
string|"'Sleep time between updates'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'monitoring_instances_step'"
op|','
number|'300'
op|','
nl|'\n'
string|"'Interval of RRD updates'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'monitoring_rrd_path'"
op|','
string|"'$state_path/monitor/instances'"
op|','
nl|'\n'
string|"'Location of RRD files'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|RRD_VALUES
name|'RRD_VALUES'
op|'='
op|'{'
nl|'\n'
string|"'cpu'"
op|':'
op|'['
nl|'\n'
string|"'DS:cpu:GAUGE:600:0:100'"
op|','
nl|'\n'
string|"'RRA:AVERAGE:0.5:1:800'"
op|','
nl|'\n'
string|"'RRA:AVERAGE:0.5:6:800'"
op|','
nl|'\n'
string|"'RRA:AVERAGE:0.5:24:800'"
op|','
nl|'\n'
string|"'RRA:AVERAGE:0.5:288:800'"
op|','
nl|'\n'
string|"'RRA:MAX:0.5:1:800'"
op|','
nl|'\n'
string|"'RRA:MAX:0.5:6:800'"
op|','
nl|'\n'
string|"'RRA:MAX:0.5:24:800'"
op|','
nl|'\n'
string|"'RRA:MAX:0.5:288:800'"
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
string|"'net'"
op|':'
op|'['
nl|'\n'
string|"'DS:rx:COUNTER:600:0:1250000'"
op|','
nl|'\n'
string|"'DS:tx:COUNTER:600:0:1250000'"
op|','
nl|'\n'
string|"'RRA:AVERAGE:0.5:1:800'"
op|','
nl|'\n'
string|"'RRA:AVERAGE:0.5:6:800'"
op|','
nl|'\n'
string|"'RRA:AVERAGE:0.5:24:800'"
op|','
nl|'\n'
string|"'RRA:AVERAGE:0.5:288:800'"
op|','
nl|'\n'
string|"'RRA:MAX:0.5:1:800'"
op|','
nl|'\n'
string|"'RRA:MAX:0.5:6:800'"
op|','
nl|'\n'
string|"'RRA:MAX:0.5:24:800'"
op|','
nl|'\n'
string|"'RRA:MAX:0.5:288:800'"
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
string|"'disk'"
op|':'
op|'['
nl|'\n'
string|"'DS:rd:COUNTER:600:U:U'"
op|','
nl|'\n'
string|"'DS:wr:COUNTER:600:U:U'"
op|','
nl|'\n'
string|"'RRA:AVERAGE:0.5:1:800'"
op|','
nl|'\n'
string|"'RRA:AVERAGE:0.5:6:800'"
op|','
nl|'\n'
string|"'RRA:AVERAGE:0.5:24:800'"
op|','
nl|'\n'
string|"'RRA:AVERAGE:0.5:288:800'"
op|','
nl|'\n'
string|"'RRA:MAX:0.5:1:800'"
op|','
nl|'\n'
string|"'RRA:MAX:0.5:6:800'"
op|','
nl|'\n'
string|"'RRA:MAX:0.5:24:800'"
op|','
nl|'\n'
string|"'RRA:MAX:0.5:444:800'"
op|','
nl|'\n'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|utcnow
name|'utcnow'
op|'='
name|'utils'
op|'.'
name|'utcnow'
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
string|"'nova.compute.monitor'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|update_rrd
name|'def'
name|'update_rrd'
op|'('
name|'instance'
op|','
name|'name'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Updates the specified RRD file.\n    """'
newline|'\n'
name|'filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'instance'
op|'.'
name|'get_rrd_path'
op|'('
op|')'
op|','
string|"'%s.rrd'"
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'init_rrd'
op|'('
name|'instance'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'timestamp'
op|'='
name|'int'
op|'('
name|'time'
op|'.'
name|'mktime'
op|'('
name|'utcnow'
op|'('
op|')'
op|'.'
name|'timetuple'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'rrdtool'
op|'.'
name|'update'
op|'('
name|'filename'
op|','
string|"'%d:%s'"
op|'%'
op|'('
name|'timestamp'
op|','
name|'data'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|init_rrd
dedent|''
name|'def'
name|'init_rrd'
op|'('
name|'instance'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Initializes the specified RRD file.\n    """'
newline|'\n'
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'monitoring_rrd_path'
op|','
name|'instance'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
string|"'%s.rrd'"
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rrdtool'
op|'.'
name|'create'
op|'('
nl|'\n'
name|'filename'
op|','
nl|'\n'
string|"'--step'"
op|','
string|"'%d'"
op|'%'
name|'FLAGS'
op|'.'
name|'monitoring_instances_step'
op|','
nl|'\n'
string|"'--start'"
op|','
string|"'0'"
op|','
nl|'\n'
op|'*'
name|'RRD_VALUES'
op|'['
name|'name'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|graph_cpu
dedent|''
dedent|''
name|'def'
name|'graph_cpu'
op|'('
name|'instance'
op|','
name|'duration'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Creates a graph of cpu usage for the specified instance and duration.\n    """'
newline|'\n'
name|'path'
op|'='
name|'instance'
op|'.'
name|'get_rrd_path'
op|'('
op|')'
newline|'\n'
name|'filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
string|"'cpu-%s.png'"
op|'%'
name|'duration'
op|')'
newline|'\n'
nl|'\n'
name|'rrdtool'
op|'.'
name|'graph'
op|'('
nl|'\n'
name|'filename'
op|','
nl|'\n'
string|"'--disable-rrdtool-tag'"
op|','
nl|'\n'
string|"'--imgformat'"
op|','
string|"'PNG'"
op|','
nl|'\n'
string|"'--width'"
op|','
string|"'400'"
op|','
nl|'\n'
string|"'--height'"
op|','
string|"'120'"
op|','
nl|'\n'
string|"'--start'"
op|','
string|"'now-%s'"
op|'%'
name|'duration'
op|','
nl|'\n'
string|"'--vertical-label'"
op|','
string|"'% cpu used'"
op|','
nl|'\n'
string|"'-l'"
op|','
string|"'0'"
op|','
nl|'\n'
string|"'-u'"
op|','
string|"'100'"
op|','
nl|'\n'
string|"'DEF:cpu=%s:cpu:AVERAGE'"
op|'%'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
string|"'cpu.rrd'"
op|')'
op|','
nl|'\n'
string|"'AREA:cpu#eacc00:% CPU'"
op|','
op|')'
newline|'\n'
nl|'\n'
name|'store_graph'
op|'('
name|'instance'
op|'.'
name|'instance_id'
op|','
name|'filename'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|graph_net
dedent|''
name|'def'
name|'graph_net'
op|'('
name|'instance'
op|','
name|'duration'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Creates a graph of network usage for the specified instance and duration.\n    """'
newline|'\n'
name|'path'
op|'='
name|'instance'
op|'.'
name|'get_rrd_path'
op|'('
op|')'
newline|'\n'
name|'filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
string|"'net-%s.png'"
op|'%'
name|'duration'
op|')'
newline|'\n'
nl|'\n'
name|'rrdtool'
op|'.'
name|'graph'
op|'('
nl|'\n'
name|'filename'
op|','
nl|'\n'
string|"'--disable-rrdtool-tag'"
op|','
nl|'\n'
string|"'--imgformat'"
op|','
string|"'PNG'"
op|','
nl|'\n'
string|"'--width'"
op|','
string|"'400'"
op|','
nl|'\n'
string|"'--height'"
op|','
string|"'120'"
op|','
nl|'\n'
string|"'--start'"
op|','
string|"'now-%s'"
op|'%'
name|'duration'
op|','
nl|'\n'
string|"'--vertical-label'"
op|','
string|"'bytes/s'"
op|','
nl|'\n'
string|"'--logarithmic'"
op|','
nl|'\n'
string|"'--units'"
op|','
string|"'si'"
op|','
nl|'\n'
string|"'--lower-limit'"
op|','
string|"'1000'"
op|','
nl|'\n'
string|"'--rigid'"
op|','
nl|'\n'
string|"'DEF:rx=%s:rx:AVERAGE'"
op|'%'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
string|"'net.rrd'"
op|')'
op|','
nl|'\n'
string|"'DEF:tx=%s:tx:AVERAGE'"
op|'%'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
string|"'net.rrd'"
op|')'
op|','
nl|'\n'
string|"'AREA:rx#00FF00:In traffic'"
op|','
nl|'\n'
string|"'LINE1:tx#0000FF:Out traffic'"
op|','
op|')'
newline|'\n'
nl|'\n'
name|'store_graph'
op|'('
name|'instance'
op|'.'
name|'instance_id'
op|','
name|'filename'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|graph_disk
dedent|''
name|'def'
name|'graph_disk'
op|'('
name|'instance'
op|','
name|'duration'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Creates a graph of disk usage for the specified duration.\n    """'
newline|'\n'
name|'path'
op|'='
name|'instance'
op|'.'
name|'get_rrd_path'
op|'('
op|')'
newline|'\n'
name|'filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
string|"'disk-%s.png'"
op|'%'
name|'duration'
op|')'
newline|'\n'
nl|'\n'
name|'rrdtool'
op|'.'
name|'graph'
op|'('
nl|'\n'
name|'filename'
op|','
nl|'\n'
string|"'--disable-rrdtool-tag'"
op|','
nl|'\n'
string|"'--imgformat'"
op|','
string|"'PNG'"
op|','
nl|'\n'
string|"'--width'"
op|','
string|"'400'"
op|','
nl|'\n'
string|"'--height'"
op|','
string|"'120'"
op|','
nl|'\n'
string|"'--start'"
op|','
string|"'now-%s'"
op|'%'
name|'duration'
op|','
nl|'\n'
string|"'--vertical-label'"
op|','
string|"'bytes/s'"
op|','
nl|'\n'
string|"'--logarithmic'"
op|','
nl|'\n'
string|"'--units'"
op|','
string|"'si'"
op|','
nl|'\n'
string|"'--lower-limit'"
op|','
string|"'1000'"
op|','
nl|'\n'
string|"'--rigid'"
op|','
nl|'\n'
string|"'DEF:rd=%s:rd:AVERAGE'"
op|'%'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
string|"'disk.rrd'"
op|')'
op|','
nl|'\n'
string|"'DEF:wr=%s:wr:AVERAGE'"
op|'%'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
string|"'disk.rrd'"
op|')'
op|','
nl|'\n'
string|"'AREA:rd#00FF00:Read'"
op|','
nl|'\n'
string|"'LINE1:wr#0000FF:Write'"
op|','
op|')'
newline|'\n'
nl|'\n'
name|'store_graph'
op|'('
name|'instance'
op|'.'
name|'instance_id'
op|','
name|'filename'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|store_graph
dedent|''
name|'def'
name|'store_graph'
op|'('
name|'instance_id'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Transmits the specified graph file to internal object store on cloud\n    controller.\n    """'
newline|'\n'
comment|'# TODO(devcamcar): Need to use an asynchronous method to make this'
nl|'\n'
comment|'#       connection. If boto has some separate method that generates'
nl|'\n'
comment|'#       the request it would like to make and another method to parse'
nl|'\n'
comment|'#       the response we can make our own client that does the actual'
nl|'\n'
comment|'#       request and hands it off to the response parser.'
nl|'\n'
name|'s3'
op|'='
name|'boto'
op|'.'
name|'s3'
op|'.'
name|'connection'
op|'.'
name|'S3Connection'
op|'('
nl|'\n'
name|'aws_access_key_id'
op|'='
name|'FLAGS'
op|'.'
name|'aws_access_key_id'
op|','
nl|'\n'
name|'aws_secret_access_key'
op|'='
name|'FLAGS'
op|'.'
name|'aws_secret_access_key'
op|','
nl|'\n'
name|'is_secure'
op|'='
name|'False'
op|','
nl|'\n'
name|'calling_format'
op|'='
name|'boto'
op|'.'
name|'s3'
op|'.'
name|'connection'
op|'.'
name|'OrdinaryCallingFormat'
op|'('
op|')'
op|','
nl|'\n'
name|'port'
op|'='
name|'FLAGS'
op|'.'
name|'s3_port'
op|','
nl|'\n'
name|'host'
op|'='
name|'FLAGS'
op|'.'
name|'s3_host'
op|')'
newline|'\n'
name|'bucket_name'
op|'='
string|"'_%s.monitor'"
op|'%'
name|'instance_id'
newline|'\n'
nl|'\n'
comment|"# Object store isn't creating the bucket like it should currently"
nl|'\n'
comment|'# when it is first requested, so have to catch and create manually.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'bucket'
op|'='
name|'s3'
op|'.'
name|'get_bucket'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'bucket'
op|'='
name|'s3'
op|'.'
name|'create_bucket'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'key'
op|'='
name|'boto'
op|'.'
name|'s3'
op|'.'
name|'Key'
op|'('
name|'bucket'
op|')'
newline|'\n'
name|'key'
op|'.'
name|'key'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'filename'
op|')'
newline|'\n'
name|'key'
op|'.'
name|'set_contents_from_filename'
op|'('
name|'filename'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Instance
dedent|''
name|'class'
name|'Instance'
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
op|','
name|'conn'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'conn'
op|'='
name|'conn'
newline|'\n'
name|'self'
op|'.'
name|'instance_id'
op|'='
name|'instance_id'
newline|'\n'
name|'self'
op|'.'
name|'last_updated'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'min'
newline|'\n'
name|'self'
op|'.'
name|'cputime'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'cputime_last_updated'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'init_rrd'
op|'('
name|'self'
op|','
string|"'cpu'"
op|')'
newline|'\n'
name|'init_rrd'
op|'('
name|'self'
op|','
string|"'net'"
op|')'
newline|'\n'
name|'init_rrd'
op|'('
name|'self'
op|','
string|"'disk'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|needs_update
dedent|''
name|'def'
name|'needs_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Indicates whether this instance is due to have its statistics updated.\n        """'
newline|'\n'
name|'delta'
op|'='
name|'utcnow'
op|'('
op|')'
op|'-'
name|'self'
op|'.'
name|'last_updated'
newline|'\n'
name|'return'
name|'delta'
op|'.'
name|'seconds'
op|'>='
name|'FLAGS'
op|'.'
name|'monitoring_instances_step'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Updates the instances statistics and stores the resulting graphs\n        in the internal object store on the cloud controller.\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'updating %s...'"
op|')'
op|','
name|'self'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'='
name|'self'
op|'.'
name|'fetch_cpu_stats'
op|'('
op|')'
newline|'\n'
name|'if'
name|'data'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'CPU: %s'"
op|','
name|'data'
op|')'
newline|'\n'
name|'update_rrd'
op|'('
name|'self'
op|','
string|"'cpu'"
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'data'
op|'='
name|'self'
op|'.'
name|'fetch_net_stats'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'NET: %s'"
op|','
name|'data'
op|')'
newline|'\n'
name|'update_rrd'
op|'('
name|'self'
op|','
string|"'net'"
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'fetch_disk_stats'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'DISK: %s'"
op|','
name|'data'
op|')'
newline|'\n'
name|'update_rrd'
op|'('
name|'self'
op|','
string|"'disk'"
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(devcamcar): Turn these into pool.ProcessPool.execute() calls'
nl|'\n'
comment|'# and make the methods @defer.inlineCallbacks.'
nl|'\n'
name|'graph_cpu'
op|'('
name|'self'
op|','
string|"'1d'"
op|')'
newline|'\n'
name|'graph_cpu'
op|'('
name|'self'
op|','
string|"'1w'"
op|')'
newline|'\n'
name|'graph_cpu'
op|'('
name|'self'
op|','
string|"'1m'"
op|')'
newline|'\n'
nl|'\n'
name|'graph_net'
op|'('
name|'self'
op|','
string|"'1d'"
op|')'
newline|'\n'
name|'graph_net'
op|'('
name|'self'
op|','
string|"'1w'"
op|')'
newline|'\n'
name|'graph_net'
op|'('
name|'self'
op|','
string|"'1m'"
op|')'
newline|'\n'
nl|'\n'
name|'graph_disk'
op|'('
name|'self'
op|','
string|"'1d'"
op|')'
newline|'\n'
name|'graph_disk'
op|'('
name|'self'
op|','
string|"'1w'"
op|')'
newline|'\n'
name|'graph_disk'
op|'('
name|'self'
op|','
string|"'1m'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'unexpected error during update'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'last_updated'
op|'='
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_rrd_path
dedent|''
name|'def'
name|'get_rrd_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Returns the path to where RRD files are stored.\n        """'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'monitoring_rrd_path'
op|','
name|'self'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fetch_cpu_stats
dedent|''
name|'def'
name|'fetch_cpu_stats'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Returns cpu usage statistics for this instance.\n        """'
newline|'\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_info'
op|'('
name|'self'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get the previous values.'
nl|'\n'
name|'cputime_last'
op|'='
name|'self'
op|'.'
name|'cputime'
newline|'\n'
name|'cputime_last_updated'
op|'='
name|'self'
op|'.'
name|'cputime_last_updated'
newline|'\n'
nl|'\n'
comment|'# Get the raw CPU time used in nanoseconds.'
nl|'\n'
name|'self'
op|'.'
name|'cputime'
op|'='
name|'float'
op|'('
name|'info'
op|'['
string|"'cpu_time'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cputime_last_updated'
op|'='
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'CPU: %d'"
op|','
name|'self'
op|'.'
name|'cputime'
op|')'
newline|'\n'
nl|'\n'
comment|'# Skip calculation on first pass. Need delta to get a meaningful value.'
nl|'\n'
name|'if'
name|'cputime_last_updated'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
comment|'# Calculate the number of seconds between samples.'
nl|'\n'
dedent|''
name|'d'
op|'='
name|'self'
op|'.'
name|'cputime_last_updated'
op|'-'
name|'cputime_last_updated'
newline|'\n'
name|'t'
op|'='
name|'d'
op|'.'
name|'days'
op|'*'
number|'86400'
op|'+'
name|'d'
op|'.'
name|'seconds'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'t = %d'"
op|','
name|'t'
op|')'
newline|'\n'
nl|'\n'
comment|'# Calculate change over time in number of nanoseconds of CPU time used.'
nl|'\n'
name|'cputime_delta'
op|'='
name|'self'
op|'.'
name|'cputime'
op|'-'
name|'cputime_last'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'cputime_delta = %s'"
op|','
name|'cputime_delta'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get the number of virtual cpus in this domain.'
nl|'\n'
name|'vcpus'
op|'='
name|'int'
op|'('
name|'info'
op|'['
string|"'num_cpu'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'vcpus = %d'"
op|','
name|'vcpus'
op|')'
newline|'\n'
nl|'\n'
comment|'# Calculate CPU % used and cap at 100.'
nl|'\n'
name|'return'
name|'min'
op|'('
name|'cputime_delta'
op|'/'
op|'('
name|'t'
op|'*'
name|'vcpus'
op|'*'
number|'1.0e9'
op|')'
op|'*'
number|'100'
op|','
number|'100'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fetch_disk_stats
dedent|''
name|'def'
name|'fetch_disk_stats'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Returns disk usage statistics for this instance.\n        """'
newline|'\n'
name|'rd'
op|'='
number|'0'
newline|'\n'
name|'wr'
op|'='
number|'0'
newline|'\n'
nl|'\n'
name|'disks'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_disks'
op|'('
name|'self'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Aggregate the read and write totals.'
nl|'\n'
name|'for'
name|'disk'
name|'in'
name|'disks'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'rd_req'
op|','
name|'rd_bytes'
op|','
name|'wr_req'
op|','
name|'wr_bytes'
op|','
name|'errs'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'block_stats'
op|'('
name|'self'
op|'.'
name|'instance_id'
op|','
name|'disk'
op|')'
newline|'\n'
name|'rd'
op|'+='
name|'rd_bytes'
newline|'\n'
name|'wr'
op|'+='
name|'wr_bytes'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'                '
name|'iid'
op|'='
name|'self'
op|'.'
name|'instance_id'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'\'Cannot get blockstats for "%(disk)s"\''
nl|'\n'
string|'\' on "%(iid)s"\''
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
string|"'%d:%d'"
op|'%'
op|'('
name|'rd'
op|','
name|'wr'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fetch_net_stats
dedent|''
name|'def'
name|'fetch_net_stats'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Returns network usage statistics for this instance.\n        """'
newline|'\n'
name|'rx'
op|'='
number|'0'
newline|'\n'
name|'tx'
op|'='
number|'0'
newline|'\n'
nl|'\n'
name|'interfaces'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_interfaces'
op|'('
name|'self'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Aggregate the in and out totals.'
nl|'\n'
name|'for'
name|'interface'
name|'in'
name|'interfaces'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'stats'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'interface_stats'
op|'('
name|'self'
op|'.'
name|'instance_id'
op|','
name|'interface'
op|')'
newline|'\n'
name|'rx'
op|'+='
name|'stats'
op|'['
number|'0'
op|']'
newline|'\n'
name|'tx'
op|'+='
name|'stats'
op|'['
number|'4'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'                '
name|'iid'
op|'='
name|'self'
op|'.'
name|'instance_id'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'\'Cannot get ifstats for "%(interface)s"\''
nl|'\n'
string|'\' on "%(iid)s"\''
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
string|"'%d:%d'"
op|'%'
op|'('
name|'rx'
op|','
name|'tx'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceMonitor
dedent|''
dedent|''
name|'class'
name|'InstanceMonitor'
op|'('
name|'object'
op|','
name|'service'
op|'.'
name|'Service'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Monitors the running instances of the current machine.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initialize the monitoring loop.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_instances'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_loop'
op|'='
name|'task'
op|'.'
name|'LoopingCall'
op|'('
name|'self'
op|'.'
name|'updateInstances'
op|')'
newline|'\n'
nl|'\n'
DECL|member|startService
dedent|''
name|'def'
name|'startService'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_instances'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_loop'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
name|'FLAGS'
op|'.'
name|'monitoring_instances_delay'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'Service'
op|'.'
name|'startService'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stopService
dedent|''
name|'def'
name|'stopService'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_loop'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'service'
op|'.'
name|'Service'
op|'.'
name|'stopService'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|updateInstances
dedent|''
name|'def'
name|'updateInstances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Update resource usage for all running instances.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'conn'
op|'='
name|'virt_connection'
op|'.'
name|'get_connection'
op|'('
name|'read_only'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'exn'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'unexpected exception getting connection'"
op|')'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
name|'FLAGS'
op|'.'
name|'monitoring_instances_delay'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'domain_ids'
op|'='
name|'conn'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'updateInstances_'
op|'('
name|'conn'
op|','
name|'domain_ids'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'exn'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
string|"'updateInstances_'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|updateInstances_
dedent|''
dedent|''
name|'def'
name|'updateInstances_'
op|'('
name|'self'
op|','
name|'conn'
op|','
name|'domain_ids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'domain_id'
name|'in'
name|'domain_ids'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'domain_id'
name|'in'
name|'self'
op|'.'
name|'_instances'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'='
name|'Instance'
op|'('
name|'conn'
op|','
name|'domain_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_instances'
op|'['
name|'domain_id'
op|']'
op|'='
name|'instance'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Found instance: %s'"
op|')'
op|','
name|'domain_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'key'
name|'in'
name|'self'
op|'.'
name|'_instances'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_instances'
op|'['
name|'key'
op|']'
newline|'\n'
name|'if'
name|'instance'
op|'.'
name|'needs_update'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'.'
name|'update'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
