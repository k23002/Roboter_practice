class Controllers:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def start_application(self):
        user_name = self.view.get_user_name()
        restaurant_name = self.view.get_restaurant_name(user_name)

        self.model.update(restaurant_name)

        self.view.finish_application(user_name)