from forward_chaining_engine import ForwardChainingEngine
from knowledge_base import KnowledgeBase

inference_engine = ForwardChainingEngine()
knowledge_base = KnowledgeBase(inference_engine)

facts = [
    "Year 1960",
    "Year 1813",
    "Year 1949",
    "Year 1925",
    "Year 1951",
    "Year 1937",
    "Author Harper_Lee",
    "Author George_Orwell",
    "Author Jane_Austen",
    "Author F_Scott_Fitzgerald",
    "Author J_D_Salinger",
    "Author J_R_R_Tolkien",
    "Availability Available",
    "Availability Checked_Out",
]

for fact in facts:
    knowledge_base.add_fact(fact)

#Father, Mother, Occupation, Hobby,
rules = [
    "Name ?name => Class ?class & Habitat ?habitat & Diet ?herbivore",
    "Year ?year => Book ?book",
    "Availability ?availability => Book ?book",
]

for rule in rules:
    knowledge_base.add_rule(rule)

queries = [
    "Child ?child grandpa",
    "Grandparent grandpa ?descendent",
    "Parent ?parent ?child",
    "Child son son",
    "Cousin ?child cousin",
]

for query in queries:
    res = knowledge_base.query(query)
    # print(res)
    if len(res) == 0:
        print("-")
    for r in res:
        print(str(r))
    print()