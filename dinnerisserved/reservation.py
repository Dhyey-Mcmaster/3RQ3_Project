# noinspection PyMethodMayBeStatic
class Reservation:
    # noinspection PyMethodMayBeStatic
    def Book_Reservation(self, num_reservation):
        if 1 <= num_reservation <= 5:  # When the customer has successfully booked a table
            return 1
        elif num_reservation == 0 and num_reservation > 5:        # When the customer fails to book a table for
            return 0

    def Confirm_Reservation(self, num_confirm_reserve):
        if num_confirm_reserve == 1:    #When the reservation is confirmed
            return 1
        else:                           #When the reservation is not confirmed
            return 0