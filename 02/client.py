import socket
from json import loads as json_to_dict,dumps as dict_to_json
from time import time,ctime,sleep

def getUser(i):
	surnames = ['Алфьоров','Волосожар','Гладкий','Дворніцька','Збаровський','Карабінський','Кисельова','Кумпан','Лобунько','Лукашевич','Мишкарьова','Мумінов','Погребенко','Радченко','Сєров','Соловйова','Тарабара']
	return {'id':i,'surname':surnames[i%len(surnames)]+str(i//len(surnames))}

clients = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(11)]

for i in range(len(clients)):
	clients[i].connect((socket.gethostname(), 1234))
	clients[i].send(bytes(dict_to_json(getUser(i)),'utf-8'))
	# sleep(0.5)

for i in range(len(clients)):
	while True:
		data = clients[i].recv(4000)
		if data:
			data1 = json_to_dict(data.decode('utf-8'))
			print(f'Доброго дня {getUser(i)["surname"]} зараз онлайн:')
			print(' id |      прізвище      |       дата підключення       |      дата старту таймера     ')
			print('----+--------------------+------------------------------+------------------------------')
			for j in data1.keys():
				print('%3s |%19s |%29s |%29s ' % (data1[j]['id'],data1[j]['surname'],ctime(data1[j]['date']),ctime(data1[j]['timer_start']) ) )
			print('')
			break