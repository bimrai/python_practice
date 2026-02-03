class UNSC():
    def __init__(self, name, service_number, rank, soldier_type, team, companion):
        self.name = name
        self.service_number = service_number
        self.rank = rank
        self.soldier_type = soldier_type
        self.team = team
        self.companion = companion
        
    def identify(self):
        return "Name: {}, Rank: {}, Service Number: {}, Type: {}, AI Companion: {}".format(self.name, self.rank, self.service_number, self.soldier_type, self.companion)
    
    
master_chief = UNSC('JOHN', 117, 'MASTER CHIEF PETTY OFFICER', 'SPARTAN-II', 'BLUE', 'CORTANA')
print(master_chief.identify())

fred = UNSC('FRED', 104, 'LIEUTENANT JUNIOR GRADE', 'SPARTAN-II', 'BLUE', 'DAMON')
print(fred.identify())

cortana = UNSC('CORTANA', 'CTN 0452-9', 'N/A', 'AI - CONSTRUCT','N/A', 'MASTER CHIEF')
print(cortana.identify())
