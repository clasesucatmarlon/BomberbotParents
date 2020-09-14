""" from flask import Flask, render_template

app = Flask(__name__)

@app.route("/main")
def main_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True) """

import storage.impl as st

st.saved = st.get_json_data()
# manera insegura
st.saved[st.idx("89912788-f63e-11ea-b695-e86a64f158a1")]["email"] = "jeje"

st.commit("jsonfile")