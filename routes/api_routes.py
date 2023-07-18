"""Simple router"""


from handlers.handle_interests import clients_interests_handler
from handlers.handle_score import online_score_handler

router = {
    "clients_interests": clients_interests_handler,
    "online_score": online_score_handler,
}
