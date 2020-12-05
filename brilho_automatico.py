#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Trocando o brilho da tela
import screen_brightness_control as bc
import datetime as d
from time import sleep
import subprocess
from daemonize import Daemonize

# Definindo o valor do brilho de acordo com o horário
def brightness_value_by_time():
    now = d.datetime.now()
    if now.hour == 16:
        return 80
    if now.hour == 17:
        return 70
    if now.hour == 18:
        return 60
    if now.hour == 19:
        return 50
    if now.hour == 8:
        return 80
    if now.hour == 7:
        return 70
    if now.hour == 6:
        return 60
    if now.hour == 5:
        return 50
    # valor para as horas demais
    return 90

# troca o brilho pegando possíveis erros
def changeBrightness(value):
    try:
        bc.fade_brightness(value, bc.get_brightness())
    except bc.ScreenBrightnessError as error:
        print(error)

# enviando notificação
def send_notification():
    messagem = f"O brilho atual foi configurado para {brightness_value_by_time}%."
    subprocess.Popen(['notify-send', messagem])
    return

# função que executa o programa
def main():
    while True:
        # troca o brilho
        changeBrightness(brightness_value_by_time())
        send_notification()
        sleep(60*30) #30 minutos em segundos

# executando como daemon
pid = "/tmp/brightness_changer.pid"
daemon = Daemonize(app="brightness_changer", pid=pid, action=main)
daemon.start()
