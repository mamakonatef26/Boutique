import streamlit as st

st.set_page_config(page_title="Boutique Africaine", layout="wide")

st.title("🛍️ Boutique de Costumes Africains")
st.write("Bienvenue dans notre boutique d'habits traditionnels africains")

# Liste des produits
products = [
    {
        "name": "Boubou Sénégalais",
        "price": 35000,
        "image": "https://i.imgur.com/8Km9tLL.jpg"
    },
    {
        "name": "Kaftan Royal",
        "price": 45000,
        "image": "https://i.imgur.com/2yaf2wb.jpg"
    },
    {
        "name": "Robe Africaine Wax",
        "price": 25000,
        "image": "https://i.imgur.com/ZF6s192.jpg"
    }
]

# Panier
if "cart" not in st.session_state:
    st.session_state.cart = []

cols = st.columns(3)

for i, product in enumerate(products):
    with cols[i % 3]:
        st.image(product["image"], use_column_width=True)
        st.subheader(product["name"])
        st.write(f"Prix : {product['price']} XOF")

        if st.button(f"Ajouter au panier {product['name']}"):
            st.session_state.cart.append(product)
            st.success("Produit ajouté au panier !")

# Affichage du panier
st.sidebar.title("🛒 Panier")

total = 0
for item in st.session_state.cart:
    st.sidebar.write(item["name"])
    total += item["price"]

st.sidebar.write(f"### Total : {total} XOF")