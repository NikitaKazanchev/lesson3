"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.
Есть набор сообщений из чата в следующем формате:
```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```
Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.
Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).
Весь код стоит разбить на логические части с помощью функций.
"""

import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages



if __name__ == "__main__":
#1. Вывести айди пользователя, который написал больше всех сообщений.   
    # number_of_messages_by_id = {}
    # for message in generate_chat_history():
    #     if message['sent_by'] in number_of_messages_by_id:
    #         number_of_messages_by_id[message['sent_by']] += 1
    #     else:
    #         number_of_messages_by_id[message['sent_by']] = 1
    # max_messages = max(number_of_messages_by_id, key=number_of_messages_by_id.get)
    # print(max_messages) # id с максимальным количеством сообщений


# 2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
    
    # посчитать количество ответов на сообщение 
    
    messages_id = {}
    for message in generate_chat_history():
        if message['reply_for'] in messages_id:
            messages_id[message['reply_for']] += 1
        else:
            messages_id[message['reply_for']] = 1
    # проверить по id сообщения к какому id пользователя оно относиться
        number_of_repetitions = {} 
        for i,v in messages_id.items():
            if i == message['reply_for']:
                number_of_repetitions[message['sent_by']] = v
        print(number_of_repetitions)
    # сложить значение у одинаковых ключах

    # вывести максимальное число ответов       
        
  


# #3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
#     number_of_views = {}
#     number_of_repetitions = {}
#     for message in generate_chat_history():
#         number_of_views[message['sent_by']] = len(message['seen_by'])
#         for sent_by,views in number_of_views.items():
#             if views > 3:
#                 number_of_repetitions[sent_by] = views
#     print(list(number_of_repetitions.keys()))


#4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
    # morning = 0
    # lunch = 0
    # evening = 0
    # for message in generate_chat_history():
    #     datetime_str = message['sent_at'].time()
    #     if        
                
        
            


#     messages = [
#     {
#         "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
#         "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
#         "sent_by": 46,  # id пользователя-отправителя
#         "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
#         "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
#         "text": "А когда ревью будет?",
#     }
# ]

