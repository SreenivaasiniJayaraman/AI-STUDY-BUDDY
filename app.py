import streamlit as st

st.set_page_config(page_title="AI Study Buddy")
st.title("📘 AI Study Buddy (Offline Dynamic)")

# Streamlit input
question = st.text_input("Enter your question")

if st.button("Explain"):
    if question.strip() == "":
        st.warning("Please enter a question")
    else:
        q_lower = question.lower()

        # Predefined dynamic answers
        if "operating system" in q_lower:
            answer = "An operating system is system software that manages computer hardware and software resources."
        elif "dbms" in q_lower or "database" in q_lower:
            answer = "DBMS stands for Database Management System. It helps store, manage, and retrieve data efficiently."
        elif "machine learning" in q_lower:
            answer = "Machine Learning is a field of AI where computers learn patterns from data to make predictions or decisions."
        elif "python" in q_lower:
            answer = "Python is a high-level programming language used for web development, data analysis, AI, and more."
        elif "cloud computing" in q_lower:
            answer = "Cloud computing delivers computing services like storage and processing over the internet."
        elif "network" in q_lower:
            answer = "Computer networking is the practice of connecting computers to share data and resources."
        elif "html" in q_lower:
            answer = "HTML is a markup language used to structure web pages."
        elif "javascript" in q_lower:
            answer = "JavaScript is a programming language used for interactive web development."
        elif "nature" in q_lower:
            answer = "Nature refers to the physical world, including plants, animals, landscapes, and natural phenomena."
        elif "environment" in q_lower:
            answer = "The environment includes all living and non-living things that surround us, and it’s important to protect it."
        else:
            answer = f"**{question}** is an important topic. Please refer to standard resources for more information."

        st.subheader("Explanation")
        st.write(answer)