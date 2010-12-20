begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
name|'from'
name|'os'
name|'import'
name|'system'
op|','
name|'popen4'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'simplejson'
name|'as'
name|'json'
newline|'\n'
name|'from'
name|'itertools'
name|'import'
name|'chain'
newline|'\n'
nl|'\n'
comment|'# order is important, mmmkay? 1 is domid, 2  command, 3 is vif'
nl|'\n'
comment|'# when we add rules, we delete first, to make sure we only keep the one rule we need'
nl|'\n'
nl|'\n'
DECL|function|main
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'  '
name|'fin'
op|','
name|'fout'
op|'='
name|'popen4'
op|'('
string|'"/usr/bin/xenstore-ls /local/domain/%s/vm-data/networking"'
op|'%'
name|'sys'
op|'.'
name|'argv'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'macs'
op|'='
name|'fout'
op|'.'
name|'read'
op|'('
op|')'
op|'.'
name|'split'
op|'('
string|'"\\n"'
op|')'
op|'['
number|'0'
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'mac'
name|'in'
name|'macs'
op|':'
newline|'\n'
indent|'    '
name|'m'
op|'='
name|'mac'
op|'.'
name|'split'
op|'('
string|'"="'
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'fin'
op|','
name|'fout'
op|'='
name|'popen4'
op|'('
string|'"/usr/bin/xenstore-read /local/domain/%s/vm-data/networking/%s"'
op|'%'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'1'
op|']'
op|','
name|'m'
op|')'
op|')'
newline|'\n'
name|'mjson'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'fout'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
name|'for'
name|'ip'
name|'in'
name|'mjson'
op|'['
string|"'ips'"
op|']'
op|':'
newline|'\n'
indent|'      '
name|'if'
name|'mjson'
op|'['
string|'"label"'
op|']'
op|'=='
string|'"public"'
op|':'
newline|'\n'
indent|'        '
name|'label'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'label'
op|'='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
name|'VIF'
op|'='
string|'"vif%s.%s"'
op|'%'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'1'
op|']'
op|','
name|'label'
op|')'
newline|'\n'
nl|'\n'
name|'if'
op|'('
name|'len'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
op|'=='
number|'4'
name|'and'
name|'sys'
op|'.'
name|'argv'
op|'['
number|'3'
op|']'
op|'=='
name|'VIF'
op|')'
name|'or'
op|'('
name|'len'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
op|'=='
number|'3'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'run_rules'
op|'('
nl|'\n'
name|'IP'
op|'='
name|'ip'
op|'['
string|"'ip'"
op|']'
op|','
nl|'\n'
name|'VIF'
op|'='
name|'VIF'
op|','
nl|'\n'
name|'MAC'
op|'='
name|'mjson'
op|'['
string|"'mac'"
op|']'
op|','
nl|'\n'
name|'STATUS'
op|'='
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'2'
op|']'
op|'=='
string|"'online'"
op|')'
name|'and'
string|"'-A'"
name|'or'
string|"'-D'"
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|function|run_rules
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'run_rules'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'  '
name|'map'
op|'('
name|'system'
op|','
name|'chain'
op|'('
name|'ebtables'
op|'('
op|'**'
name|'kwargs'
op|')'
op|','
name|'arptables'
op|'('
op|'**'
name|'kwargs'
op|')'
op|','
name|'iptables'
op|'('
op|'**'
name|'kwargs'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|iptables
dedent|''
name|'def'
name|'iptables'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'  '
name|'return'
op|'['
nl|'\n'
string|'"/sbin/iptables -D FORWARD -m physdev --physdev-in %s -s %s -j ACCEPT 2>&1 > /dev/null"'
op|'%'
op|'('
name|'kwargs'
op|'['
string|"'VIF'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'IP'"
op|']'
op|')'
op|','
nl|'\n'
string|'"/sbin/iptables %s FORWARD -m physdev --physdev-in %s -s %s -j ACCEPT"'
op|'%'
op|'('
name|'kwargs'
op|'['
string|"'STATUS'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'VIF'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'IP'"
op|']'
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|function|arptables
dedent|''
name|'def'
name|'arptables'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'  '
name|'return'
op|'['
nl|'\n'
string|'"/sbin/arptables -D FORWARD --opcode Request --in-interface %s --source-ip %s --source-mac %s -j ACCEPT 2>&1 > /dev/null"'
op|'%'
op|'('
name|'kwargs'
op|'['
string|"'VIF'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'IP'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'MAC'"
op|']'
op|')'
op|','
nl|'\n'
string|'"/sbin/arptables -D FORWARD --opcode Reply --in-interface %s --source-ip %s --source-mac %s -j ACCEPT 2>&1 > /dev/null"'
op|'%'
op|'('
name|'kwargs'
op|'['
string|"'VIF'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'IP'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'MAC'"
op|']'
op|')'
op|','
nl|'\n'
string|'"/sbin/arptables %s FORWARD --opcode Request --in-interface %s --source-ip %s --source-mac %s -j ACCEPT"'
op|'%'
op|'('
name|'kwargs'
op|'['
string|"'STATUS'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'VIF'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'IP'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'MAC'"
op|']'
op|')'
op|','
nl|'\n'
string|'"/sbin/arptables %s FORWARD --opcode Reply --in-interface %s --source-ip %s --source-mac %s -j ACCEPT"'
op|'%'
op|'('
name|'kwargs'
op|'['
string|"'STATUS'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'VIF'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'IP'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'MAC'"
op|']'
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|function|ebtables
dedent|''
name|'def'
name|'ebtables'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'  '
name|'cmds'
op|'='
op|'['
nl|'\n'
string|'"/sbin/ebtables -D FORWARD -p 0806 -o %s --arp-ip-dst %s -j ACCEPT 2>&1 >> /dev/null"'
op|'%'
op|'('
name|'kwargs'
op|'['
string|"'VIF'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'IP'"
op|']'
op|')'
op|','
nl|'\n'
string|'"/sbin/ebtables -D FORWARD -p 0800 -o %s --ip-dst %s -j ACCEPT 2>&1 >> /dev/null"'
op|'%'
op|'('
name|'kwargs'
op|'['
string|"'VIF'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'IP'"
op|']'
op|')'
op|','
nl|'\n'
string|'"/sbin/ebtables %s FORWARD -p 0806 -o %s --arp-ip-dst %s -j ACCEPT 2>&1 "'
op|'%'
op|'('
name|'kwargs'
op|'['
string|"'STATUS'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'VIF'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'IP'"
op|']'
op|')'
op|','
nl|'\n'
string|'"/sbin/ebtables %s FORWARD -p 0800 -o %s --ip-dst %s -j ACCEPT 2>&1 "'
op|'%'
op|'('
name|'kwargs'
op|'['
string|"'STATUS'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'VIF'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'IP'"
op|']'
op|')'
nl|'\n'
op|']'
newline|'\n'
name|'if'
name|'kwargs'
op|'['
string|"'STATUS'"
op|']'
op|'=='
string|'"-A"'
op|':'
newline|'\n'
indent|'    '
name|'cmds'
op|'.'
name|'append'
op|'('
string|'"/sbin/ebtables -D FORWARD -s ! %s -i %s -j DROP 2>&1 > /dev/null"'
op|'%'
op|'('
name|'kwargs'
op|'['
string|"'MAC'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'VIF'"
op|']'
op|')'
op|')'
newline|'\n'
name|'cmds'
op|'.'
name|'append'
op|'('
string|'"/sbin/ebtables -I FORWARD 1 -s ! %s -i %s -j DROP"'
op|'%'
op|'('
name|'kwargs'
op|'['
string|"'MAC'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'VIF'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'    '
name|'cmds'
op|'.'
name|'append'
op|'('
string|'"/sbin/ebtables %s FORWARD -s ! %s -i %s -j DROP"'
op|'%'
op|'('
name|'kwargs'
op|'['
string|"'STATUS'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'MAC'"
op|']'
op|','
name|'kwargs'
op|'['
string|"'VIF'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cmds'
newline|'\n'
nl|'\n'
DECL|function|usage
dedent|''
name|'def'
name|'usage'
op|'('
op|')'
op|':'
newline|'\n'
indent|'  '
name|'print'
string|'"Usage: slice_vifs.py <DOMID> <online|offline> optional: <vif>"'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'  '
name|'if'
name|'len'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
op|'<'
number|'3'
op|':'
newline|'\n'
indent|'    '
name|'usage'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'    '
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
