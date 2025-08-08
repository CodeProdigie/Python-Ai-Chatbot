import streamlit as st
# page config
st.set_page_config(
    page_title="Python Basic",
    page_icon="🕸"
)
#title and markdown
st.title("🧠Learn Python Basics With Techbrains Today")
st.markdown("welcome!! This Simple App Will Help You Interactively understand Basic Python Concept.")
#sidebar with navigations
option = st.sidebar.selectbox("Choose Your Topic",{"Variable","Conditional Statement","Loop","Function"})
if option == "Variable":
    st.header("📦 python Variable")
    st.write("in python,Variable store data values.")
    name=st.text_input("Enter your full names")
    age=st.number_input("Enter you age",min_value=1, max_value=120,step=1)
    if name:
        st.success(f"{name} if {age} year old")
        st.code(
            f"name ={name}\nage= {age}"
        )
elif option == "Conditional Statement":
    st.header("📌 Conditional Statement")
    st.write("it make use of the `if`, `elif` and `else` to fulfil a Condition")
    number = st.number_input("Enter a number" ,step=1)
    if number % 2 ==0:
        st.success(f"{number} is even")
        st.code(f"number = {number}\nif number%2 ==0:\n  print(`{number} is even`)\nelse:\nprint({number} is odd`)")
    else:
        st.warning(f"{number} is odd")
#Loop
elif option == "Loop":
    st.header("💎 Loop")
    st.write("there are three type of loop `do-loop`,`while-loop` and `do-while loop`")
    for i in range(1,11,2):
        st.success(i)
    st.code( f"for i in range (1,11,2):print (i+3)")
#Function
elif option == "Function":
    st.header("🧸Function")
    st.write("to declare a Function the word `def` is used")
    number = st.number_input("Enter a number",min_value=1,max_value=100,step=1)
    def factorial(num):
        fact=1
        for i in range (1,num + 1):
            fact=fact*i
            return fact
    number = int (input("Enter a number"))
    st.success(factorial(number))
    st.code( f"for i in range (1,num + 1)" )