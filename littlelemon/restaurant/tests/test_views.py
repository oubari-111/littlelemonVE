
#maybe wrong 
class MenuViewTest(TestCase):
    def setup(self):
        # Create test instances of the Menu model
        Menu.objects.create(title='Dish 1', price=10.99)
        Menu.objects.create(title='Dish 2', price=15.49)
        # Add more instances as needed

    def test_getall(self):
        # Retrieve all Menu objects
        url = reverse('menu/')  # Replace 'menu-list' with the actual URL name for your Menu API endpoint
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Serialize the retrieved data
        serialized_data = MenuSerializer(Menu.objects.all(), many=True).data

        # Check if the serialized data in the response is equal to the expected serialized data
        self.assertEqual(response.data, serialized_data)