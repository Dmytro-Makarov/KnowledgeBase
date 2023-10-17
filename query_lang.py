class Value:
    def __init__(self, raw):
        self.raw = raw
        self.parsed = raw


class Variable:
    @staticmethod
    def is_variable(t):
        return t.startswith("?")

    def __init__(self, raw):
        self.raw = raw
        self.parsed = raw.replace("?", "")


class Predicate:
    def __init__(self, raw):
        relation, *terms = raw.split(" ")
        self.parsed = {
            "relation": relation,
            "terms": [Variable(term) if Variable.is_variable(term) else Value(term) for term in terms]
        }

    def __str__(self):
        return f"{self.parsed['relation']} {' '.join([term.raw for term in self.parsed['terms']])}"

    def map_terms(self, f):
        predicate = Predicate(str(self))
        predicate.parsed['terms'] = [f(term) for term in predicate.parsed['terms']]
        return Predicate(str(predicate))

    def bind_substitution(self, substitution):
        return self.map_terms(
            lambda t: substitution.data[t.parsed] if isinstance(t, Variable) and t.parsed in substitution.data else t)


class Substitution:
    def __init__(self, data: dict):
        self.data = data


class Rule:
    def __init__(self, text):
        predicates, res = text.split("=>")
        self.predicates = [Predicate(p.strip()) for p in predicates.split("&")]
        self.res = Predicate(res.strip())

    def __str__(self):
        return f"{' & '.join([str(p) for p in self.predicates])} => {str(self.res)}"
