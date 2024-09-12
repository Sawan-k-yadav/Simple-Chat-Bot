import streamlit as st
import pandas as pd

# Predefined questions and answers in a DataFrame
df = pd.DataFrame({
    "question": ["What is the average lifespan of a dog?", "How often should I feed my dog?", "Can dogs see colors?", "How much exercise does a dog need?", "Can dogs hear better than humans?"],
    "answer": ["10-13 years", "2-3 times a day", "No, they are colorblind", "At least 30 minutes a day", "Yes, they can hear higher frequencies"]
})

# Chatbot UI
st.title("Dog Chatbot")
st.write("Ask me a question about dogs!")


# Display questions as instructions in the sidebar
st.sidebar.title("Try asking me these questions:")
for i, row in df.iterrows():
    st.sidebar.write(f"{i+1}. {row['question']}")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# This logic give one ans at a time and does not show last question and answer on top.
# user_input = st.text_input("")

# if user_input:
#     answer = df.loc[df["question"] == user_input, "answer"].values[0]
#     st.write("Answer:", answer)


# Logic to get response and show previous asked questions and answers as well
if user_input := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(user_input.capitalize())
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input.capitalize()})

    try:
        answer= df.loc[df["question"].str.lower() == user_input.lower(), "answer"].values[0]

    except IndexError:
        answer = "I couldn't find an answer to that question. Please try asking something the list."

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.write("Answer:", answer)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": answer})

# # Display conversation history
# st.write("Conversation History:")
# for i, row in df.iterrows():
#     st.write(f"Q: {row['question']}")
#     st.write(f"A: {row['answer']}")