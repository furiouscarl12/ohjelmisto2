
#teht1
class Publication:

    def __init__(self, title):
        self.title = title
class Book(Publication):

    def __init__(self, title, author, page_count):
        super().__init__(title)
        self.author = author
        self.page_count = page_count

    def print_info_book(self):
        print(f"Book Title: {self.title}\nAuthor: {self.author}\nPage Count: {self.page_count}\n")


class Magazine(Publication):

    def __init__(self, title, eic):
        super().__init__(title)
        self.eic = eic

    def print_info_mag(self):
        print(f"Magazine Title: {self.title}\nEditor-in-Chief: {self.eic}\n")


pub_mag = Magazine("Aku Ankka", "Aki Hyyppä")
pub_mag.print_info_mag()
pub_book = Book("Hytti ", "Rosa Liksom",)
pub_book.print_info_book()

#teht2

class Car:
    def __init__(self, plate, top_speed, curr_speed=0, dist=0):
        self.plate = plate
        self.top_speed = top_speed
        self.curr_speed = curr_speed
        self.dist = dist

    def accelerate(self, acc):
        self.curr_speed = self.curr_speed + acc
        if self.curr_speed > self.top_speed:
            self.curr_speed = self.top_speed
        elif self.curr_speed < 0:
            self.curr_speed = 0

    def travel(self, hour):
        self.dist = self.dist + self.curr_speed * hour


class Electric(Car):

    def __init__(self, plate, top_speed, battery):
        super().__init__(self, battery)
        self.plate = plate
        self.top_speed = top_speed
        self.battery = battery


class Engine(Car):

    def __init__(self, plate, top_speed, tank):
        super().__init__(self, tank)
        self.plate = plate
        self.top_speed = top_speed
        self.tank = tank


ev1 = Electric("ABC-15", 180, 52.5)
eng1 = Engine("ACD-123", 165, 32.3)

