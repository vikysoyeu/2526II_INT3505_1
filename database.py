users = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Binh"},
    {"id": 3, "name": "Cuong"}
]

def get_all_users():
    return users

def get_user(user_id):
    for u in users:
        if u["id"] == user_id:
            return u
    return None