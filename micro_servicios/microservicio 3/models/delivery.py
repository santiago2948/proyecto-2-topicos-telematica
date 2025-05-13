from extensions import db

class DeliveryProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    coverage_area = db.Column(db.String(150))
    cost = db.Column(db.Float)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "coverage_area": self.coverage_area,
            "cost": self.cost
        }