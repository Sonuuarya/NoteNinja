import threading

from sqlalchemy import Column, String

from NoteNinja.modules.sql import BASE, SESSION


class NoteNinjaChats(BASE):
    __tablename__ = "NoteNinja_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


NoteNinjaChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_NoteNinja(chat_id):
    try:
        chat = SESSION.query(NoteNinjaChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_NoteNinja(chat_id):
    with INSERTION_LOCK:
        NoteNinjachat = SESSION.query(NoteNinjaChats).get(str(chat_id))
        if not NoteNinjachat:
            NoteNinjachat = NoteNinjaChats(str(chat_id))
        SESSION.add(NoteNinjachat)
        SESSION.commit()


def rem_NoteNinja(chat_id):
    with INSERTION_LOCK:
        NoteNinjachat = SESSION.query(NoteNinjaChats).get(str(chat_id))
        if NoteNinjachat:
            SESSION.delete(NoteNinjachat)
        SESSION.commit()
