import copy
from typing import Optional


# import aiogram.dispatcher.filters.state
# from aiogram.dispatcher.filters.state import StatesGroup


class Storage:
    states: dict = {}

    def set_state(self, user_id: int, state: Optional[str], data: dict = None):
        if data is None:
            data = {}
        if user_id in self.states.keys():
            self.states[user_id]["current_state_name"] = state
            self.states[user_id]["data"].update(data)
        else:
            self.states.update({user_id: {"current_state_name": state, "data": data}})

    def current_state(self, user_id: int) -> Optional[str]:
        state = self.states.get(user_id)
        if state is None:
            return None
        else:
            return state.get("current_state_name")

    def update_data(self, user_id: int, data: dict):
        if user_id in self.states.keys():
            self.states[user_id]["data"].update(data)
        else:
            self.set_state(user_id, None, data)

    def get_data(self, user_id: int) -> Optional[dict]:
        state = self.states.get(user_id)
        if state is None:
            return None
        else:
            return copy.deepcopy(state.get("data"))

    def finish(self, user_id: int):
        if user_id in self.states.keys():
            self.states[user_id] = {"current_state_name": None, "data": {}}

    def clean_data(self, user_id: int):
        if user_id in self.states.keys():
            self.states[user_id]["data"] = {}

