import streamlit as st
import urllib.parse

# -------------------------
# CONFIG PAGE
# -------------------------
st.set_page_config(page_title="Boutique Africaine", page_icon="👗", layout="wide")

# -------------------------
# STYLE CSS
# -------------------------
st.markdown("""
<style>
body {
    background-color: #FFF8E7;
    font-family: 'Arial', sans-serif;
}
.stButton>button {
    background-color: #FF7F50;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px;
}
.payment-icon {
    height:30px;
    margin-right:10px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.markdown("## 👋 Bienvenue dans notre boutique de costumes africains !")
st.markdown("Découvrez nos habits traditionnels et passez votre commande facilement.")

# -------------------------
# PRODUITS
# -------------------------
products = [
    {"name": "Boubou Sénégalais", "price": 35000, "image": "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf"},
    {"name": "Kaftan Royal", "price": 45000, "image": "https://images.unsplash.com/photo-1593032465175-481ac7f401a0"},
    {"name": "Robe Africaine Wax", "price": 25000, "image": "https://images.unsplash.com/photo-1618354691373-d851c5c3a1f9"}
]

if "cart" not in st.session_state:
    st.session_state.cart = []

cols = st.columns(3)
for i, product in enumerate(products):
    with cols[i % 3]:
        st.image(product["image"], use_column_width=True)
        st.subheader(product["name"])
        st.write(f"Prix : {product['price']} XOF")
        if st.button(f"Ajouter {product['name']}", key=i):
            st.session_state.cart.append(product)
            st.success(f"✅ {product['name']} ajouté au panier !")

# -------------------------
# PANIER
# -------------------------
st.sidebar.title("🛒 Panier")
total = 0
for item in st.session_state.cart:
    st.sidebar.write(f"- {item['name']} ({item['price']} XOF)")
    total += item["price"]
st.sidebar.write(f"### Total : {total} XOF")

# -------------------------
# FORMULAIRE CLIENT
# -------------------------
st.markdown("---")
st.header("📦 Finaliser la commande")
name = st.text_input("Nom complet")
phone = st.text_input("Numéro WhatsApp (ex: 2217XXXXXXX)")
address = st.text_area("Adresse de livraison")

payment_method = st.radio(
    "Mode de paiement",
    ["PayPal 🅿️", "Wave 💧", "Orange Money 🍊", "Espèces 💵"]
)

# -------------------------
# BOUTON VALIDER
# -------------------------
if st.button("Valider la commande"):

    if len(st.session_state.cart) == 0:
        st.warning("⚠️ Votre panier est vide")
    elif not name or not phone or not address:
        st.warning("⚠️ Merci de remplir toutes vos informations")
    else:
        # Message WhatsApp
        order_details = ""
        for item in st.session_state.cart:
            order_details += f"{item['name']} - {item['price']} XOF\n"

        message = f"""
Nouvelle commande 🛍️

Nom: {name}
Téléphone: {phone}
Adresse: {address}

Produits:
{order_details}

Total: {total} XOF
Mode de paiement: {payment_method}
"""
        encoded_message = urllib.parse.quote(message)

        # Ton numéro WhatsApp
        whatsapp_number = "2217XXXXXXXX"
        whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_message}"

        st.success("✅ Merci pour votre commande ! Cliquez ci-dessous pour envoyer sur WhatsApp")
        st.markdown(f"[📲 Envoyer la commande sur WhatsApp]({whatsapp_url})", unsafe_allow_html=True)

        # Analyse simple
        st.markdown("### 📊 Analyse de la commande")
        st.write(f"Nombre d'articles : {len(st.session_state.cart)}")
        st.write(f"Montant total : {total} XOF")
        st.write(f"Mode choisi : {payment_method}")
