class DonationService:
    def request_donation(self, registered, amount):
        if not registered:
            return "Error: User not registered"
        if amount > 5:
            return "Rejected"
        return "Approved"