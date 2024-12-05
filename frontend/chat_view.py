import streamlit as st
import asyncio
import websockets
import uuid


if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.user_disabled = False

st.title("IAI Chat")
username = st.text_input(
    'Username',
    disabled=st.session_state.user_disabled,
    on_change=lambda: setattr(st.session_state, "user_disabled", True)
)

WS_URL = "ws://localhost:8000/chat"

USER_ID = uuid.uuid1()


async def send_message(message):
    async with websockets.connect(WS_URL) as websocket:
        await websocket.send(f"{username if username else 'Anonymus'}: {message}")


async def connect_and_listen():
    async with websockets.connect(WS_URL) as websocket:
        try:
            while True:
                response = await websocket.recv()
                st.session_state.messages.append(
                    {"role": "assistant", "content": response})
                st.rerun()
        except websockets.ConnectionClosed:
            st.error("Disconnected from server")


if message := st.chat_input("Do you have something to say?"):
    st.session_state.messages.append({"role": "user", "content": message})
    asyncio.run(send_message(message))
    st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if "listener_task" not in st.session_state:
    st.session_state.listener_task = asyncio.run(connect_and_listen())
