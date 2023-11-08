from ..utils.state import State


class Filter:

    def __init__(self, state=None, text=None, content_type='text'):
        self._state = state
        self._type = content_type
        self._text = text

    def __call__(self, *args, **kwargs):
        self._msg = args[0]
        state = State.get_state(self._msg.chat.id)
        text = self._msg.text

        return (state == self._state or self._state is None) and (
                self._msg.content_type == self._type or self._type is None) and (
                self._text == text or self._text is None)
