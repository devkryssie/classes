
class system:
    def __init__(self, name):
        self.name = name
        self.features = []
        self.benefits = []
        self.advantages = []
        
    def get_feature(self, feature):
        self.features.append(feature)
    def get_benefits(self, benefit):
        self.benefits.append(benefit)
    def get_advantages(self, advantage):
        self.advantages.append(advantage)
info = system("bfl")
info.get_feature("course Management", "education")
info.get_benefits("Learn anytime","Self-paced learning")
info.get_advantages("Flexible and convenient","Cost-effective")
print(info.get_features)
print(info.get_benefits)
print(info.get_advantages)
