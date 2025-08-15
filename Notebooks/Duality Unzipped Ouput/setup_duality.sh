#!/bin/sh
# Simple example script — adjust interfaces and ports as needed.

AGENT_PORT=8088

# Add iptables mangle rule to set DSCP for agent-marked packets (EF=46)
iptables -t mangle -C OUTPUT -p udp --dport $AGENT_PORT -j DSCP --set-dscp 46 2>/dev/null || iptables -t mangle -A OUTPUT -p udp --dport $AGENT_PORT -j DSCP --set-dscp 46

# Ensure SQM (CAKE) is enabled on WAN
uci set sqm.@queue[0].enabled='1'
uci commit sqm
/etc/init.d/sqm restart

echo "DUALITY DSCP + SQM configured. Verify with: iptables -t mangle -L -v"
