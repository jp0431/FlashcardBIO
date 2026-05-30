from utilities import inicializa_dict, nova_imatge, st, random

st.set_page_config("FLASHCARDS BIO")
st.title("FLASHCARDS BIO")

img_vist = []
resposta_correctes = 0
resposta_incorrecte = 0

dict_ = inicializa_dict()
if "fase" not in st.session_state:
    st.session_state.fase = "pregunta"
if "img_idx" not in st.session_state:
    st.session_state.img_idx = random.randint(0, len(dict_) - 1)
if "img_vist" not in st.session_state:
    st.session_state.img_vist = []
if "correctes" not in st.session_state:
    st.session_state.correctes = 0
if "incorrectes" not in st.session_state:
    st.session_state.incorrectes = 0


img_val = dict_.get(str(st.session_state.img_idx))
if st.session_state.fase == "pregunta":
    st.metric(label=f"Imatge {len(st.session_state.img_vist)} de {len(dict_)}", value="")
    ruta = img_val["ruta"]
    st.image(ruta)
    resposta = st.text_input("Escriu el nom exacte de l'espècie o gènere (+ sp): ",key="input_resposta", value="")
    if st.button("Valida"):
            st.session_state.ultima_resposta = resposta
            if resposta.strip().lower() == img_val["nombre"].strip():
                st.session_state.correctes += 1
                st.session_state.resultat = "correcte"
            else:
                st.session_state.incorrectes += 1
                st.session_state.resultat = "incorrecte"
            st.session_state.fase = "resultat"
            st.rerun() 
elif st.session_state.fase == "resultat":
    st.image(img_val["ruta"])

    if st.session_state.resultat == "correcte":
        st.success("✅ Resposta correcte!")
    else:
        st.error(f"❌ Incorrecte. La resposta correcta és: **{img_val['nombre']}**")

    if st.button("Següent imatge ➡️"):
        if len(st.session_state.img_vist) < len(dict_):
            #st.session_state.img_vist.append(st.session_state.img_idx)
            nova_imatge(dict_)
            st.session_state.input_resposta = ""

        else:
            st.session_state.fase = "acabat"
        st.rerun()


elif st.session_state.fase == "acabat":
    st.header(" JOC ACABAT")
    st.write(f"✅ Correctes: {st.session_state.correctes} | ❌ Incorrectes: {st.session_state.incorrectes}")
    if st.button("Torna a començar"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
    st.rerun()
