from query_lang import Predicate, Rule, Substitution


class KnowledgeBase:
    def __init__(self, inference_engine):
        self.facts = set()
        self.rules = set()
        self.inference_engine = inference_engine

    def query(self, q):
        predicate = Predicate(q)
        res = self.inference_engine.perform_query(self.facts, predicate)
        return [predicate.bind_substitution(substitution) for substitution in res]

    def add_fact(self, f):
        if any(str(e) == f for e in self.facts):
            return
        fact = Predicate(f)
        self.facts.add(fact)

    def add_rule(self, t):
        if any(str(e) == t for e in self.rules):
            return
        rule = Rule(t)
        self.rules.add(rule)
        matches = [Substitution({})]
        for predicate in rule.predicates:
            substitutions = []
            for s in matches:
                query_result = self.inference_engine.perform_query(self.facts, predicate.bind_substitution(s))
                for e in query_result:
                    new_substitution = Substitution({**s.data, **e.data})
                    substitutions.append(new_substitution)
            matches = substitutions
        for e in matches:
            self.add_fact(str(rule.res.bind_substitution(e)))
