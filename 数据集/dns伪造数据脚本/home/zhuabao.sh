ls_date=`date +%Y%m%d`
file="/tmp/"$ls_date
echo $file
if [ ! -d $file ];then
	mkdir $file

fi
count=1
while true
do
	
	tcpdump -i lo -c 2  udp port 53 -w $file/$count.cap
   	let count++
    	echo $count	
done
