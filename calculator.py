import streamlit as st
st.title('CALCULATOR APP USING STREAMLIT')
st.write('------------------------------------------------')

num1 = st.number_input(label = 'Enter the First Number')
num2 = st.number_input(label = 'Enter the Second Number')
operation = st.radio('Select the Operation',('Add','Subtract','Multiply','Divide'))

ans = 0
def calculate():
    if operation == 'Add':
        ans = num1 + num2
    elif operation == 'Subtract':
        ans = num1 - num2
    elif operation == 'Multiply':
        ans = num1 * num2
    elif operation == 'Divide':
        ans = num1/num2
    else:
        ans = 'Not Defined'
    st.success(f'Answer = {ans}')

if st.button('Calculate Result'):
    calculate()
