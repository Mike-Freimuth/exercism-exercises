"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letters = ['A', 'B', 'C', 'D']
    counter = 0
    
    while counter < number:
        
        yield letters[counter % 4]
        counter += 1
    


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    
    letters = ['A', 'B', 'C', 'D']
    seat_number = 0
    seats_generated = 0
    
    while seats_generated < number:
    
        yield str((seat_number // 4) + 1) + letters[seat_number % 4]
        
        seat_number +=1
        
        if seat_number == 48:
            seat_number += 4
        
        seats_generated += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seat_assignments ={}
    seat = generate_seats(len(passengers))
    
    for passenger in passengers:
        seat_assignments[passenger] = next(seat)
        
    return seat_assignments

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    
    tickets_printed = 0
    total_tickets = len(seat_numbers)
    
    while tickets_printed < total_tickets:
        yield seat_numbers[tickets_printed] + flight_id + '0' * (12-len(seat_numbers[tickets_printed] + flight_id))
        tickets_printed += 1