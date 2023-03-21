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
    list_of_messages_that_have_been_answered = []
    messages_and_user = {}
    user_with_the_number_of_responses = {}
    for message in generate_chat_history():
        messages_and_user[message['id']] = message['sent_by']
        list_of_messages_that_have_been_answered.append(message['reply_for'])
    for id_of_messages_that_have_been_answered in list_of_messages_that_have_been_answered:
        if id_of_messages_that_have_been_answered is None:
            continue
        if messages_and_user[id_of_messages_that_have_been_answered] in user_with_the_number_of_responses:
            user_with_the_number_of_responses[messages_and_user[id_of_messages_that_have_been_answered]] += 1 
        else:
            user_with_the_number_of_responses[messages_and_user[id_of_messages_that_have_been_answered]] = 1
    
    max_number_of_responses = max(user_with_the_number_of_responses.items(), key=lambda item: item[1])
    print(f'id пользователя с наибольшим количеством ответов на его сообщения: {max_number_of_responses}')  


#3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
    id_response = {}
    user_and_who_viewed_the_message = {}
    for message in generate_chat_history():
        if message['sent_by'] in user_and_who_viewed_the_message:
            user_and_who_viewed_the_message[message['sent_by']] += message['seen_by']
        else:
            user_and_who_viewed_the_message[message['sent_by']] = message['seen_by']
    
    for id_user,id_who_viewed_the_message in user_and_who_viewed_the_message.items():
        id_response[id_user] = len(list(set(id_who_viewed_the_message)))
       
    max_number_of_views = max(id_response.items(), key=lambda item: item[1])
    print(f'id пользователя с наибольшим количеством просмотров его сообщения: {max_number_of_views}')





# messages = [ 
#     {
#         "id": 1,
#         "sent_by": 46,  # id пользователя-отправителя
#         "reply_for": 2,  # id сообщение, на которое это сообщение является ответом (может быть None)
#         "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
#         "text": "А когда ревью будет?",
#     },
#     {
#         "id": 2,
#         "sent_by": 50,  # id пользователя-отправителя
#         "reply_for": 3,  # id сообщение, на которое это сообщение является ответом (может быть None)
#         "seen_by": [4, 1, 181], # идентификаторы пользователей, которые видели это сообщение
#         "text": "А когда ревью будет?",
#     },
#     {
#         "id": 3,
#         "sent_by": 46,  # id пользователя-отправителя
#         "reply_for": None,  # id сообщение, на которое это сообщение является ответом (может быть None)
#         "seen_by": [26, 21, 71, 22], # идентификаторы пользователей, которые видели это сообщение
#         "text": "А когда ревью будет?",
#     },
#     {
#         "id": 4,
#         "sent_by": 48,  # id пользователя-отправителя
#         "reply_for": 3,  # id сообщение, на которое это сообщение является ответом (может быть None)
#         "seen_by": [26, 33, 71], # идентификаторы пользователей, которые видели это сообщение
#         "text": "А когда ревью будет?",
#     }
# ]

