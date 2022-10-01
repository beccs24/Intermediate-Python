class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return f'(Apartment) Rent: ${self.rent}, Distance From UCSB: {self.metersFromUCSB}m, Condition: {self.condition}'

    def __gt__(self, rhs):
        if self.rent > rhs.rent:
            return True
        elif self.rent < rhs.rent:
            return False
        else:
            if self.metersFromUCSB > rhs.metersFromUCSB:
                return True
            elif self.metersFromUCSB < rhs.metersFromUCSB:
                return False
            else:
                if (self.condition == 'bad' and rhs.condition == 'average') or (self.condition == 'bad' and rhs.condition == 'excellent') or (self.condition == 'average' and rhs.condition == 'excellent'):
                    return True
                else:
                    return False
                
    def __eq__(self, rhs):
        if self.rent == rhs.rent and self.metersFromUCSB == rhs.metersFromUCSB and self.condition == rhs.condition:
            return True
        else:
            return False

    def __lt__(self, rhs):
        if self.rent > rhs.rent:
            return False
        elif self.rent < rhs.rent:
            return True
        else:
            if self.metersFromUCSB > rhs.metersFromUCSB:
                return False
            elif self.metersFromUCSB < rhs.metersFromUCSB:
                return True
            else:
                if (self.condition == 'excellent' and rhs.condition == 'average') or (self.condition == 'excellent' and rhs.condition == 'bad') or (self.condition == 'average' and rhs.condition == 'bad'):
                    return True
                else:
                    return False
