from Classes import *

def main():
    
    ticket_system = TicketSystem()
     
    tickets = [Ticket("Im locked out again", "Login", 1, "I really need to learn to type my password better"),
               Ticket("Where is my internet!?", "Network", 4, "I'm trying to watch youtu... I mean do important work things... but I cant connect?"),
               Ticket("THE SERVERS ARE ON FIRE", "Infrastructure", 7, "The servers seem to be reporting a temp of 6000 degrees, this may be an issue")]
    
    for ticket in tickets:
        print(f"{ticket.number} - {ticket.title} - {ticket.type} \n")
        print(ticket_system.submit_ticket(ticket))
        print("")
        
if __name__ == "__main__":
    main()