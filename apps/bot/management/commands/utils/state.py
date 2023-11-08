from ..bot import state as state_object, data_state


class State:

    @staticmethod
    def set_state(user_id: str, state_data):
        global state_object
        state_object[user_id] = state_data

    @staticmethod
    def get_state(user_id: str):
        return state_object.get(user_id)

    @staticmethod
    def clear_state(user_id: str):
        global state_object
        state_object.pop(user_id)

    @staticmethod
    def set_data(user_id, key, value):
        global data_state

        if not user_id in data_state:
            data_state[user_id] = {}

        data = data_state[user_id]
        data[key] = value
        data_state[user_id] = data

    @staticmethod
    def get_data(user_id: str, key, default=None):
        if not user_id in data_state:
            return default
        data = data_state.get(user_id)
        return data.get(key)

    @staticmethod
    def clear_data(user_id: str):
        global data_state
        data_state.pop(user_id)
