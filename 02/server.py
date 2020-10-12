import socket
from json import loads as json_to_dict,dumps as dict_to_json
from time import time,ctime
from threading import Timer

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(11)
online_list = {}
timer_start_time = 0

def restart_timer():
	timer_start_time = 0

print(f'{ctime(time())} : Сервер успішно запущено')

while True:
	clientsocet, address = s.accept()

	conection_time = time()
	print(f'{ctime(conection_time)} : нове з`єднання від {address}')

	if time() - timer_start_time > 11:
		timer_start_time = 0
	if timer_start_time == 0:
		timer_start_time = time()
		print(f'{ctime(timer_start_time)} : таймер стартував')		

	data = json_to_dict(clientsocet.recv(1024).decode('utf-8'))

	online_list[str(data['id'])] = {'id':data['id'],'surname':data['surname'],'date':conection_time,'timer_start':timer_start_time}

	def sendResult(clientsocet,id):
		clientsocet.send(bytes(dict_to_json(online_list),'utf-8'))
		clientsocet.close()
		print(f'{ctime(time())} : 11 секунд вийшло, дані надіслано до {online_list[str(id)]["surname"]}, з`єднання завершено')

	t = Timer(11 - (time() - online_list[str(data['id'])]['timer_start']),sendResult,[clientsocet,data['id']])
	t.start()