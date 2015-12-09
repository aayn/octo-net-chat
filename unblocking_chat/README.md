### Iptables commands necessary to enable cross-computer chat

 * sudo iptables -I INPUT 1 -p tcp -j ACCEPT
 * sudo iptables -I INPUT 1 -p udp -j ACCEPT