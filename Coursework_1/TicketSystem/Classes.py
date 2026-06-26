from abc import ABC, abstractmethod

#Request
class Ticket:
    _ticket_count = 0 #Global ticket count attribute
    def __init__(self, title, type, priority, desc): #Title = Title of the ticket. Type = type of ticket, i.e. login, network, etc. Priorty = 1 (lowest) -> 10 (Mission Critical) Desc = ticket description, i.e. whats wrong.
        Ticket._ticket_count += 1
        
        self.title = title
        self.number = Ticket._ticket_count
        self.type = type
        self.priority = priority
        self.desc = desc
        
#Interface
class HandlerInterface(ABC):
    def __init__(self):
        self._next_handler = None
    
    #Link    
    def next(self, handler):
        self._next_handler = handler
        return handler
    
    #Logic
    def handle (self, ticket):
        print(f"[LOG] Processing ticket {ticket.number} at {self.__class__.__name__}")
        if self.can_handle(ticket):
            return self.process(ticket)
        elif self._next_handler:
            return self._next_handler.handle(ticket)
        else:
            return self.unhandled(ticket)

    def unhandled(self, ticket):
        return print(f"Unable to find handler to process: {ticket.title}")
        
    @abstractmethod
    def can_handle(self, ticket):
        pass
    
    @abstractmethod
    def process(self, ticket):
        pass 

#(Concrete) Handlers               
class Level1Handler(HandlerInterface):
    def can_handle(self, ticket):
        if ticket.type == 'Login' and ticket.priority <=2:
            return True
        else:
            return False
    
    def process(self, ticket):
        return "Your ticket has been assigned to Level 1 Support."
      
class Level2Handler(HandlerInterface):
    def can_handle(self, ticket):
        if ticket.type == "Network":
            return True
        else:
            return False
    
    def process(self, ticket):
        return "Your ticket has been assigned to Level 2 Support."
        
class Level3Handler(HandlerInterface):
    def can_handle(self, ticket):
        if ticket.type == "Infrastructure":
            return True
        else:
            return False
    
    def process(self, ticket):
        return "Your ticket has been assigned to Level 3 Support."

#Chain Creator
class TicketSystem:
    def __init__(self):
        
        self.level1 = Level1Handler()
        self.level2 = Level2Handler()
        self.level3 = Level3Handler()
        
        self.level1.next(self.level2).next(self.level3)
        
        self.first = self.level1
        
    def submit_ticket(self, ticket):
        return self.first.handle(ticket)