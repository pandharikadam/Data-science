import streamlit as st
st.title('Classification model')
st.write('Will they hire an attorney?')

def create_page():
	insur=st.sidebar.selectbox('Insurance',[0,1])
	seat=st.sidebar.radio('Seatbelt',[0,1])
	age=st.sidebar.slider('Age',[0,1])
	gender=st.sidebar.radio('Gender',[0,1])
	loss=st.sidebar.number_input('Enter a loss amount')

	data={'CLMSEX':gender,
	'CLMINSUR':insur,
	'SEATBELT':seat,
	'CLMAGE':age,
	'LOSS':loss
	}
	features=pd.DataFrame(data,index=[0])
	return features

	

x_values=create_page

if st.sidebar.button('Submit'):
	st.write(x_values)
	