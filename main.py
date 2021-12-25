import vk_api
from config import TOKEN, TIME
from time import sleep

def start():
    try:
        vk_auth = vk_api.VkApi(token=TOKEN)
        vk = vk_auth.get_api()
        print("Авторизация прошла успешно")
    except:
        print("Ошибка авторизации")

    num = 1000
    while True:
        try:
            if num <= 0:
                num = 1000
            
            vk.status.set(text=f"{num} - 7")
            num-=7
            print("Статус установлен.")
        except:
            print("Ошибка, не могу поставить цитату.")
            break
    
        sleep(TIME)

    start()
    
start()
