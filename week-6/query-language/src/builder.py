from matchers import All, Not, And, Or, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:
    def __init__(self, query=All()):
        self.query = query

    def build(self):
        return self.query

    def test(self, player):
        return self.query.test(player)

    def plays_in(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.query, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.query, HasFewerThan(value, attr)))

    def one_of(self, *query):
        return QueryBuilder(Or(*query))
