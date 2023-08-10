from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="Current configuration:", parents=()),
    ConfigLine(config_line="ver 08.0.95gT211", parents=()),
    ConfigLine(config_line="stack unit 1", parents=()),
    ConfigLine(config_line="  module 1 icx7150-c12-poe-port-management-module", parents=("stack unit 1",)),
    ConfigLine(config_line="  module 2 icx7150-2-copper-port-2g-module", parents=("stack unit 1",)),
    ConfigLine(config_line="  module 3 icx7150-2-sfp-plus-port-20g-module", parents=("stack unit 1",)),
    ConfigLine(config_line="  stack-port 1/3/1", parents=("stack unit 1",)),
    ConfigLine(config_line="  stack-port 1/3/2", parents=("stack unit 1",)),
    ConfigLine(config_line="banner motd $", parents=()),
    ConfigLine(
        config_line="+----------------+ WARNING RUCKUS SWITCH +---------------+\n.\n.   Access to this system is limited to authorized\n.          users and for official purposes only\n.\n.       Your activities will be logged and abuse\n.                     will be reported!\n.\n+----------------+ WARNING RUCKUS SWITCH +---------------+$",
        parents=("banner motd $",),
    ),
    ConfigLine(config_line="vlan 1 name DEFAULT-VLAN by port", parents=()),
    ConfigLine(config_line=" no spanning-tree", parents=("vlan 1 name DEFAULT-VLAN by port",)),
    ConfigLine(config_line="vlan 2000 name MGMT-VLAN by port", parents=()),
    ConfigLine(
        config_line=" tagged ethe 1/2/1 to 1/2/2 ethe 1/3/1 to 1/3/2", parents=("vlan 2000 name MGMT-VLAN by port",)
    ),
    ConfigLine(
        config_line=" untagged ethe 1/1/1 ethe 1/1/3 ethe 1/1/5 ethe 1/1/7 ethe 1/1/9 ethe 1/1/11 to 1/1/12",
        parents=("vlan 2000 name MGMT-VLAN by port",),
    ),
    ConfigLine(config_line=" no spanning-tree", parents=("vlan 2000 name MGMT-VLAN by port",)),
    ConfigLine(config_line="vlan 3000 name Guest-WiFi by port", parents=()),
    ConfigLine(
        config_line=" tagged ethe 1/1/1 to 1/1/12 ethe 1/3/1 to 1/3/2", parents=("vlan 3000 name Guest-WiFi by port",)
    ),
    ConfigLine(config_line=" no spanning-tree", parents=("vlan 3000 name Guest-WiFi by port",)),
    ConfigLine(config_line="vlan 3001 by port", parents=()),
    ConfigLine(
        config_line=" tagged ethe 1/1/1 ethe 1/1/3 to 1/1/12 ethe 1/3/1 to 1/3/2", parents=("vlan 3001 by port",)
    ),
    ConfigLine(config_line=" untagged ethe 1/1/2", parents=("vlan 3001 by port",)),
    ConfigLine(config_line=" no spanning-tree", parents=("vlan 3001 by port",)),
    ConfigLine(config_line="vlan 3002 by port", parents=()),
    ConfigLine(
        config_line=" tagged ethe 1/1/1 to 1/1/3 ethe 1/1/5 to 1/1/12 ethe 1/3/1 to 1/3/2",
        parents=("vlan 3002 by port",),
    ),
    ConfigLine(config_line=" untagged ethe 1/1/4", parents=("vlan 3002 by port",)),
    ConfigLine(config_line=" no spanning-tree", parents=("vlan 3002 by port",)),
    ConfigLine(config_line="vlan 3003 by port", parents=()),
    ConfigLine(
        config_line=" tagged ethe 1/1/1 to 1/1/5 ethe 1/1/7 to 1/1/12 ethe 1/3/1 to 1/3/2",
        parents=("vlan 3003 by port",),
    ),
    ConfigLine(config_line=" untagged ethe 1/1/6", parents=("vlan 3003 by port",)),
    ConfigLine(config_line=" no spanning-tree", parents=("vlan 3003 by port",)),
    ConfigLine(config_line="vlan 3004 by port", parents=()),
    ConfigLine(
        config_line=" tagged ethe 1/1/1 to 1/1/7 ethe 1/1/9 to 1/1/12 ethe 1/3/1 to 1/3/2",
        parents=("vlan 3004 by port",),
    ),
    ConfigLine(config_line=" untagged ethe 1/1/8", parents=("vlan 3004 by port",)),
    ConfigLine(config_line=" no spanning-tree", parents=("vlan 3004 by port",)),
    ConfigLine(config_line="vlan 3005 by port", parents=()),
    ConfigLine(
        config_line=" tagged ethe 1/1/1 to 1/1/9 ethe 1/1/11 to 1/1/12 ethe 1/3/1 to 1/3/2",
        parents=("vlan 3005 by port",),
    ),
    ConfigLine(config_line=" untagged ethe 1/1/10", parents=("vlan 3005 by port",)),
    ConfigLine(config_line=" no spanning-tree", parents=("vlan 3005 by port",)),
    ConfigLine(config_line="vlan 3006 by port", parents=()),
    ConfigLine(config_line=" tagged ethe 1/1/1 to 1/1/12 ethe 1/3/1 to 1/3/2", parents=("vlan 3006 by port",)),
    ConfigLine(config_line=" no spanning-tree", parents=("vlan 3006 by port",)),
    ConfigLine(config_line="vlan 3007 by port", parents=()),
    ConfigLine(config_line=" tagged ethe 1/1/1 to 1/1/12 ethe 1/3/1 to 1/3/2", parents=("vlan 3007 by port",)),
    ConfigLine(config_line=" no spanning-tree", parents=("vlan 3007 by port",)),
    ConfigLine(config_line="vlan 3008 by port", parents=()),
    ConfigLine(config_line=" tagged ethe 1/1/1 to 1/1/12 ethe 1/3/1 to 1/3/2", parents=("vlan 3008 by port",)),
    ConfigLine(config_line=" no spanning-tree", parents=("vlan 3008 by port",)),
    ConfigLine(config_line="vlan 3009 by port", parents=()),
    ConfigLine(config_line=" tagged ethe 1/1/1 to 1/1/12 ethe 1/3/1 to 1/3/2", parents=("vlan 3009 by port",)),
    ConfigLine(config_line=" no spanning-tree", parents=("vlan 3009 by port",)),
    ConfigLine(config_line="vlan 3010 by port", parents=()),
    ConfigLine(config_line=" tagged ethe 1/1/1 to 1/1/12 ethe 1/3/1 to 1/3/2", parents=("vlan 3010 by port",)),
    ConfigLine(config_line=" no spanning-tree", parents=("vlan 3010 by port",)),
    ConfigLine(config_line="vlan 3995 name OfficeNetwork by port", parents=()),
    ConfigLine(
        config_line=" tagged ethe 1/1/1 to 1/1/12 ethe 1/3/1 to 1/3/2",
        parents=("vlan 3995 name OfficeNetwork by port",),
    ),
    ConfigLine(config_line=" no spanning-tree", parents=("vlan 3995 name OfficeNetwork by port",)),
    ConfigLine(config_line="mstp scope all", parents=()),
    ConfigLine(config_line="mstp instance 0 vlan 1", parents=()),
    ConfigLine(config_line="mstp instance 0 vlan 2000", parents=()),
    ConfigLine(config_line="mstp instance 0 vlan 3000 to 3010", parents=()),
    ConfigLine(config_line="mstp instance 0 vlan 3995", parents=()),
    ConfigLine(config_line="mstp start", parents=()),
    ConfigLine(config_line="errdisable recovery cause all", parents=()),
    ConfigLine(config_line="aaa authentication web-server default local", parents=()),
    ConfigLine(config_line="aaa authentication login default local", parents=()),
    ConfigLine(config_line="enable telnet authentication", parents=()),
    ConfigLine(config_line="enable aaa console", parents=()),
    ConfigLine(config_line="hostname NTC-Test-MDF", parents=()),
    ConfigLine(config_line="ip dhcp snooping vlan 2000", parents=()),
    ConfigLine(config_line="ip address 10.254.220.10 255.255.255.0", parents=()),
    ConfigLine(config_line="ip default-gateway 10.254.220.1", parents=()),
    ConfigLine(config_line="no telnet server", parents=()),
    ConfigLine(config_line="username admin password testpass", parents=()),
    ConfigLine(config_line="snmp-server community testcomm rw", parents=()),
    ConfigLine(config_line="manager registrar", parents=()),
    ConfigLine(config_line="manager port-list 987", parents=()),
    ConfigLine(config_line="interface ethernet 1/1/1", parents=()),
    ConfigLine(config_line=" port-name Unit-111-AP", parents=("interface ethernet 1/1/1",)),
    ConfigLine(config_line=" inline power power-limit 12000", parents=("interface ethernet 1/1/1",)),
    ConfigLine(config_line="interface ethernet 1/1/2", parents=()),
    ConfigLine(config_line=" port-name Unit-111-Wired", parents=("interface ethernet 1/1/2",)),
    ConfigLine(config_line="interface ethernet 1/1/3", parents=()),
    ConfigLine(config_line=" port-name Unit-112-AP", parents=("interface ethernet 1/1/3",)),
    ConfigLine(config_line=" inline power power-limit 12000", parents=("interface ethernet 1/1/3",)),
    ConfigLine(config_line="interface ethernet 1/1/4", parents=()),
    ConfigLine(config_line=" port-name Unit-112-Wired", parents=("interface ethernet 1/1/4",)),
    ConfigLine(config_line="interface ethernet 1/1/5", parents=()),
    ConfigLine(config_line=" port-name Unit-113-AP", parents=("interface ethernet 1/1/5",)),
    ConfigLine(config_line=" inline power power-limit 12000", parents=("interface ethernet 1/1/5",)),
    ConfigLine(config_line="interface ethernet 1/1/6", parents=()),
    ConfigLine(config_line=" port-name Unit-113-Wired", parents=("interface ethernet 1/1/6",)),
    ConfigLine(config_line="interface ethernet 1/1/7", parents=()),
    ConfigLine(config_line=" port-name Unit-114-AP", parents=("interface ethernet 1/1/7",)),
    ConfigLine(config_line=" inline power power-limit 12000", parents=("interface ethernet 1/1/7",)),
    ConfigLine(config_line="interface ethernet 1/1/8", parents=()),
    ConfigLine(config_line=" port-name Unit-114-Wired", parents=("interface ethernet 1/1/8",)),
    ConfigLine(config_line="interface ethernet 1/1/9", parents=()),
    ConfigLine(config_line=" port-name Unit-115-AP", parents=("interface ethernet 1/1/9",)),
    ConfigLine(config_line=" inline power power-limit 12000", parents=("interface ethernet 1/1/9",)),
    ConfigLine(config_line="interface ethernet 1/1/10", parents=()),
    ConfigLine(config_line=" port-name Unit-115-Wired", parents=("interface ethernet 1/1/10",)),
    ConfigLine(config_line="interface ethernet 1/1/11", parents=()),
    ConfigLine(config_line=" port-name UPS", parents=("interface ethernet 1/1/11",)),
    ConfigLine(config_line="interface ethernet 1/1/12", parents=()),
    ConfigLine(config_line=" port-name Tech-Test-port", parents=("interface ethernet 1/1/12",)),
    ConfigLine(config_line="interface ethernet 1/3/1", parents=()),
    ConfigLine(config_line=" dhcp snooping trust", parents=("interface ethernet 1/3/1",)),
    ConfigLine(config_line="interface ethernet 1/3/2", parents=()),
    ConfigLine(config_line=" dhcp snooping trust", parents=("interface ethernet 1/3/2",)),
    ConfigLine(config_line="no lldp run", parents=()),
    ConfigLine(config_line="overlay-gateway gateway1", parents=()),
    ConfigLine(config_line=" type layer2-extension", parents=("overlay-gateway gateway1",)),
    ConfigLine(config_line=" ip interface Loopback 1", parents=("overlay-gateway gateway1",)),
    ConfigLine(config_line=" map vlan 2 vni 3", parents=("overlay-gateway gateway1",)),
    ConfigLine(config_line=" site site1", parents=("overlay-gateway gateway1",)),
    ConfigLine(config_line="   ip address 67.67.67.1", parents=("overlay-gateway gateway1", " site site1")),
    ConfigLine(config_line="   extend vlan add 2", parents=("overlay-gateway gateway1", " site site1")),
    ConfigLine(config_line="end", parents=()),
]
