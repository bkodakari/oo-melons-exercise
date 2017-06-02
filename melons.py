"""Classes for melon orders."""

import random
import datetime


class AbstractMelonOrder(object):
    """Global melon orders."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species.lower() == "christmas melon":
            base_price = base_price * 1.5

        if self.order_type.lower() == "international" and self.qty < 10:
            flat_fee = 3
        else:
            flat_fee = 0

        total = ((1 + self.tax) * self.qty * base_price) + flat_fee

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_base_price(self):
        """ Get a random base price between 5 and 9."""

        week_day = datetime.datetime.today().weekday()

        day_hour = datetime.datetime.now().hour

        if week_day in range(0, 5) and day_hour in range(8, 12):
            base_price = random.randint(5, 9) + 4
        else:
            base_price = random.randint(5, 9)
        return base_price


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", .08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, "international", .17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """ The government does not have taxes, but goes through security. """

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty, "government", 0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Mark the inspection as passed for government orders."""

        self.passed_inspection = passed
