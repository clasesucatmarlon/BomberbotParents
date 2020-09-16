import storage.impl as st
from flask import Flask

#proy = st.new_id(st.proy)

st.saved = st.mongocon.find_all()


print(st.from_key("011f5098-f847-11ea-b1bf-e86a64f158a1"))


#st.mongocon.insert_all([st.push_data(proy, title="speedcoders")], mirror=True)
