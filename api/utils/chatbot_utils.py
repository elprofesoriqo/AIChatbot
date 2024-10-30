# Przykładowe funkcje do obsługi chatbota

def get_classification(message: str) -> str:
    # Funkcja, która klasyfikuje intencję użytkownika na podstawie tekstu wiadomości
    # Może korzystać z modelu NLP lub prostego algorytmu regex do identyfikacji intencji
    if "order" in message:
        return "order_intent"
    elif "details" in message:
        return "details_intent"
    elif "recommend" in message:
        return "recommend_intent"
    else:
        return "unknown_intent"

def get_product_details(product_id: str) -> dict:
    # Funkcja, która pobiera szczegóły o produkcie z bazy danych lub innego źródła
    product_data = {
        "product_name": "Latte",
        "price": 4.99,
        "description": "A creamy coffee made with espresso and steamed milk."
    }
    # Zwraca słownik z informacjami o produkcie
    return product_data

def create_order(order_details: dict) -> dict:
    # Funkcja, która tworzy zamówienie i zwraca potwierdzenie
    order_id = "order1234"  # Generuje unikalne ID zamówienia
    return {
        "order_id": order_id,
        "status": "confirmed",
        "details": order_details
    }

def get_recommendations(preferences: dict) -> list:
    # Funkcja generująca rekomendacje na podstawie preferencji użytkownika
    recommendations = [
        {"product_name": "Espresso", "price": 2.99},
        {"product_name": "Cappuccino", "price": 3.99}
    ]
    return recommendations
