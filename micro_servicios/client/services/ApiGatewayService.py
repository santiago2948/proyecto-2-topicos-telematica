import requests

class ApiGatewayService:
    def __init__(self, api_gateway_url):
        self.api_gateway_url = api_gateway_url

    def get_books(self):
        response = requests.get(f"{self.api_gateway_url}/catalog")  # Updated route
        response.raise_for_status()
        return response.json()

    def get_books_by_seller(self, seller_id):
        response = requests.post(f"{self.api_gateway_url}/my_books", json={"user_id": seller_id})  # Updated route and method
        response.raise_for_status()
        return response.json()

    def add_book(self, book_data):
        response = requests.post(f"{self.api_gateway_url}/add_book", json=book_data)  # Updated route
        response.raise_for_status()
        return response.json()

    def update_book(self, book_id, book_data):
        response = requests.post(f"{self.api_gateway_url}/edit_book/{book_id}", json=book_data)  # Updated route and method
        response.raise_for_status()
        return response.json()

    def delete_book(self, book_id, user_id):
        response = requests.post(f"{self.api_gateway_url}/delete_book/{book_id}", json={"user_id": user_id})  # Updated route and method
        response.raise_for_status()
        return response.status_code

    def get_delivery_providers(self):
        response = requests.get(f"{self.api_gateway_url}/providers")
        response.raise_for_status()
        return response.json()

    def assign_delivery(self, purchase_id, provider_id):
        response = requests.post(f"{self.api_gateway_url}/assign/{purchase_id}", json={"provider_id": provider_id})
        response.raise_for_status()
        return response.json()

    def process_payment(self, purchase_id, payment_data):
        response = requests.post(f"{self.api_gateway_url}/process/{purchase_id}", json=payment_data)
        response.raise_for_status()
        return response.json()

    def create_purchase(self, book_id, purchase_data):
        response = requests.post(f"{self.api_gateway_url}/buy/{book_id}", json=purchase_data)
        response.raise_for_status()
        return response.json()
