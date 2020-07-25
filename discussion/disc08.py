def sum_paths_gen(t):
    if is_leaf(t):
        yield label(t)
    for b in branches(t):
        for elem in sum_paths_gen(b)]:
            yield label(t) + elem


class Student:
    students = 0 # this is a class attribute
    def __init__(self, name, ta):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        ta.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)


class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}
    def add_student(self, student):
        self.students[student.name] = student
    def assist(self, student):
        student.understanding += 1


class Email:
    """Every email object has 3 instance attributes:
    the message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    """Each Server has an instance attribute clients,
    which is a dictionary that associates client names
    with client objects.
    """

    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the
        client it is addressed to.
        """
        # email.recipient_name.recieve(email)
        client = self.clients[email.recipient_name]
        client.receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds
        them to the clients instance attribute.
        """
        self.clients[client_name] = client


class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients),
    and inbox (a list of all emails the client has received). """

    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
        self.server.register_client(self, name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to
        the given recipient client.
        """
        self.server.send(Email(msg, self.name, recipient_name))

    def receive(self, email):
        """Take an email and add it to the inbox of this client.
        """
        self.inbox.append(email)


class Dog():
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name + " says woof!")


class Cat():
    def __init__(self, name, owner, lives=9):
        self.is_alive = True
        self.name = name
        self.owner = owner
        self.lives = lives

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name + " says meow!")


class Pet():
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!! self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)


class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives

    def talk(self):
        """ Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(f"{self.name} says meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive' becomes False. If this is called after lives has reached zero, print out that the cat has no more lives to lose.
        """
        if self.lives <= 0:
            if self.lives == 0:
                self.is_alive = False
            else:
                print('The pet has no more lives to lose')
        else:
            self.lives -= 1


class NoisyCat: # Fill me in!
    """A Cat that repeats things twice."""

    def __init__(self, name, owner, lives=9):
        # Cat.__init__(name, owner, lives)
                # Is this method necessary? Why or why not?
        pass

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        Cat.talk(self)
        Cat.talk(self)