from datetime import datetime

class Invoice:
    """Represents an invoice for a collection of services rendered to a recipient"""

    def __init__(self,
                 sender_name,
                 recipient_name,
                 sender_address,
                 recipient_address,
                 sender_email,
                 recipient_email):
        # externally determined variables
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email

        # internally determined variables
        self.date = datetime.now()
        self.cost = 0
        self.items = []
        self.comments = []

    def add_item(self, name, price, tax):
        # python makes working with trivial data-objects quite easy
        item = {
            "name": name,
            "price": price,
            "tax": tax
        }

        # hold on to the unmodified item for later, we'll do tax/discount calculations on an as-needed basis
        self.items.append(item)

    def calculate_total(self, discount):
        # determine how much the invoice total should be by summing all individual item totals
        total = 0
        for item in self.items:
            price = item["price"]
            tax = item["tax"]

            total += price + price * tax
        # the bug here was how the disocunt was calculated
        # the discount applies to the whole of the invoice not each item
        total = total - (total * discount/100)
        return total

    def add_comments(self, string):
        self.comments.append(string)
    
    def print_comments(self):
        string = ""
        count = 0
        for com in self.comments:
            count += 1
            if count < len(self.comments):
                string += com + "\n"
            else:
                string += com
        return string

if __name__ == '__main__':
    invoice = Invoice(
        "Larry Jinkles",
        "Tod Hooper",
        "34 Windsor Ln.",
        "14 Manslow road",
        "lejank@billing.com",
        "discreetclorinator@hotmail.com"
    )

    invoice.add_item("34 floor building", 3400, 0.1)
    invoice.add_item("Equipment Rental", 1000, 0.1)
    invoice.add_item("Fear Tax", 340, 0.0)
    invoice.add_comments("Late payment")
    invoice.add_comments("Shortage of equipment")
    invoice.add_comments("damaged Material")
    invoice_total = invoice.calculate_total(20)
    all_comments = invoice.print_comments()
    print(invoice_total)
    print(all_comments)
