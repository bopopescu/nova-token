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
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
string|'"""\nA fake (in-memory) hypervisor+api. Allows nova testing w/o a hypervisor.\nThis module also documents the semantics of real hypervisor connections.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_connection
name|'def'
name|'get_connection'
op|'('
name|'_'
op|')'
op|':'
newline|'\n'
comment|'# The read_only parameter is ignored.'
nl|'\n'
indent|'    '
name|'return'
name|'FakeConnection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeConnection
dedent|''
name|'class'
name|'FakeConnection'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    The interface to this class talks in terms of \'instances\' (Amazon EC2 and\n    internal Nova terminology), by which we mean \'running virtual machine\'\n    (XenAPI terminology) or domain (Xen or libvirt terminology).\n\n    An instance has an ID, which is the identifier chosen by Nova to represent\n    the instance further up the stack.  This is unfortunately also called a\n    \'name\' elsewhere.  As far as this layer is concerned, \'instance ID\' and\n    \'instance name\' are synonyms.\n\n    Note that the instance ID or name is not human-readable or\n    customer-controlled -- it\'s an internal ID chosen by Nova.  At the\n    nova.virt layer, instances do not have human-readable names at all -- such\n    things are only known higher up the stack.\n\n    Most virtualization platforms will also have their own identity schemes,\n    to uniquely identify a VM or domain.  These IDs must stay internal to the\n    platform-specific layer, and never escape the connection interface.  The\n    platform-specific layer is responsible for keeping track of which instance\n    ID maps to which platform-specific ID, and vice versa.\n\n    In contrast, the list_disks and list_interfaces calls may return\n    platform-specific IDs.  These identify a specific virtual disk or specific\n    virtual network interface, and these IDs are opaque to the rest of Nova.\n\n    Some methods here take an instance of nova.compute.service.Instance.  This\n    is the datastructure used by nova.compute to store details regarding an\n    instance, and pass them into this layer.  This layer is responsible for\n    translating that generic datastructure into terms that are specific to the\n    virtualization platform.\n    """'
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
name|'self'
op|'.'
name|'instances'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
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
name|'cls'
op|'.'
name|'_instance'
op|'='
name|'cls'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_instance'
newline|'\n'
nl|'\n'
DECL|member|list_instances
dedent|''
name|'def'
name|'list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the names of all the instances known to the virtualization\n        layer, as a list.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'instances'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|spawn
dedent|''
name|'def'
name|'spawn'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create a new instance/VM/domain on the virtualization platform.\n\n        The given parameter is an instance of nova.compute.service.Instance.\n        This function should use the data there to guide the creation of\n        the new instance.\n\n        The work will be done asynchronously.  This function returns a\n        Deferred that allows the caller to detect when it is complete.\n\n        Once this successfully completes, the instance should be\n        running (power_state.RUNNING).\n\n        If this fails, any partial instance should be completely\n        cleaned up, and the virtualization platform should be in the state\n        that it was before this call began.\n        """'
newline|'\n'
nl|'\n'
name|'fake_instance'
op|'='
name|'FakeInstance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instances'
op|'['
name|'instance'
op|'.'
name|'name'
op|']'
op|'='
name|'fake_instance'
newline|'\n'
name|'fake_instance'
op|'.'
name|'_state'
op|'='
name|'power_state'
op|'.'
name|'RUNNING'
newline|'\n'
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reboot
dedent|''
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Reboot the specified instance.\n\n        The given parameter is an instance of nova.compute.service.Instance,\n        and so the instance is being specified as instance.name.\n\n        The work will be done asynchronously.  This function returns a\n        Deferred that allows the caller to detect when it is complete.\n        """'
newline|'\n'
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|rescue
dedent|''
name|'def'
name|'rescue'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Rescue the specified instance.\n        """'
newline|'\n'
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unrescue
dedent|''
name|'def'
name|'unrescue'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Unrescue the specified instance.\n        """'
newline|'\n'
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Destroy (shutdown and delete) the specified instance.\n\n        The given parameter is an instance of nova.compute.service.Instance,\n        and so the instance is being specified as instance.name.\n\n        The work will be done asynchronously.  This function returns a\n        Deferred that allows the caller to detect when it is complete.\n        """'
newline|'\n'
name|'del'
name|'self'
op|'.'
name|'instances'
op|'['
name|'instance'
op|'.'
name|'name'
op|']'
newline|'\n'
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'device_path'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach the disk at device_path to the instance at mountpoint"""'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|detach_volume
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach the disk attached to the instance at mountpoint"""'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Get a block of information about the given instance.  This is returned\n        as a dictionary containing \'state\': The power_state of the instance,\n        \'max_mem\': The maximum memory for the instance, in KiB, \'mem\': The\n        current memory the instance has, in KiB, \'num_cpu\': The current number\n        of virtual CPUs the instance has, \'cpu_time\': The total CPU time used\n        by the instance, in nanoseconds.\n\n        This method should raise exception.NotFound if the hypervisor has no\n        knowledge of the instance\n        """'
newline|'\n'
name|'if'
name|'instance_name'
name|'not'
name|'in'
name|'self'
op|'.'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"Instance %s Not Found"'
op|'%'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'i'
op|'='
name|'self'
op|'.'
name|'instances'
op|'['
name|'instance_name'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'state'"
op|':'
name|'i'
op|'.'
name|'_state'
op|','
nl|'\n'
string|"'max_mem'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'mem'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'num_cpu'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'cpu_time'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|list_disks
dedent|''
name|'def'
name|'list_disks'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the IDs of all the virtual disks attached to the specified\n        instance, as a list.  These IDs are opaque to the caller (they are\n        only useful for giving back to this layer as a parameter to\n        disk_stats).  These IDs only need to be unique for a given instance.\n\n        Note that this function takes an instance ID, not a\n        compute.service.Instance, so that it can be called by compute.monitor.\n        """'
newline|'\n'
name|'return'
op|'['
string|"'A_DISK'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|list_interfaces
dedent|''
name|'def'
name|'list_interfaces'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the IDs of all the virtual network interfaces attached to the\n        specified instance, as a list.  These IDs are opaque to the caller\n        (they are only useful for giving back to this layer as a parameter to\n        interface_stats).  These IDs only need to be unique for a given\n        instance.\n\n        Note that this function takes an instance ID, not a\n        compute.service.Instance, so that it can be called by compute.monitor.\n        """'
newline|'\n'
name|'return'
op|'['
string|"'A_VIF'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|block_stats
dedent|''
name|'def'
name|'block_stats'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'disk_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return performance counters associated with the given disk_id on the\n        given instance_name.  These are returned as [rd_req, rd_bytes, wr_req,\n        wr_bytes, errs], where rd indicates read, wr indicates write, req is\n        the total number of I/O requests made, bytes is the total number of\n        bytes transferred, and errs is the number of requests held up due to a\n        full pipeline.\n\n        All counters are long integers.\n\n        This method is optional.  On some platforms (e.g. XenAPI) performance\n        statistics can be retrieved directly in aggregate form, without Nova\n        having to do the aggregation.  On those platforms, this method is\n        unused.\n\n        Note that this function takes an instance ID, not a\n        compute.service.Instance, so that it can be called by compute.monitor.\n        """'
newline|'\n'
name|'return'
op|'['
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
name|'null'
op|']'
newline|'\n'
nl|'\n'
DECL|member|interface_stats
dedent|''
name|'def'
name|'interface_stats'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'iface_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return performance counters associated with the given iface_id on the\n        given instance_id.  These are returned as [rx_bytes, rx_packets,\n        rx_errs, rx_drop, tx_bytes, tx_packets, tx_errs, tx_drop], where rx\n        indicates receive, tx indicates transmit, bytes and packets indicate\n        the total number of bytes or packets transferred, and errs and dropped\n        is the total number of packets failed / dropped.\n\n        All counters are long integers.\n\n        This method is optional.  On some platforms (e.g. XenAPI) performance\n        statistics can be retrieved directly in aggregate form, without Nova\n        having to do the aggregation.  On those platforms, this method is\n        unused.\n\n        Note that this function takes an instance ID, not a\n        compute.service.Instance, so that it can be called by compute.monitor.\n        """'
newline|'\n'
name|'return'
op|'['
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_console_output
dedent|''
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'FAKE CONSOLE OUTPUT'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeInstance
dedent|''
dedent|''
name|'class'
name|'FakeInstance'
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
name|'self'
op|'.'
name|'_state'
op|'='
name|'power_state'
op|'.'
name|'NOSTATE'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
