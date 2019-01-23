echo "start run................."
function rand(){
    min=$1
    max=$(($2-$min+1))
    num=$(($RANDOM+1000000000)) #增加一个10位的数再求余
    echo $(($num%$max+$min))
}
randstr() {
  index=0
  str=""
  for i in {a..z}; do arr[index]=$i; index=`expr ${index} + 1`; done
  for i in {A..Z}; do arr[index]=$i; index=`expr ${index} + 1`; done
for i in {1..12}; do str="$str${arr[$RANDOM%$index]}"; done
  echo $str
}
while true
do
	zone=$(randstr)'.com'
	domain='www.'$zone
	zone2='zone "'$zone'" IN{'	
	echo $zone2
#修改/etc/name.rfc1912.zones
	sed -i "41c$zone2" /etc/name.rfc1912.zones
	ttl_pre=$(rand 30 300)
	ttl='$TTL '$ttl_pre
	echo $ttl
	ip=$(rand 1 200).$(rand 1 200).$(rand 1 200).$(rand 1 200)
	ipaddr=$domain".           IN      A       "$ip
	echo $ipaddr
	sed -i "1c$ttl" /var/named/data/nstl.com.zone
	sed -i "11c$ipaddr" /var/named/data/nstl.com.zone
	systemctl restart named.service
#发送dns请求包
	python /home/dnssend.py $domain
#5秒钟修改一次配置，发送一次DNS包
	sleep 5
done
