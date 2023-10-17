from forward_chaining_engine import ForwardChainingEngine
from knowledge_base import KnowledgeBase

if __name__ == "__main__":
    inference_engine = ForwardChainingEngine()
    knowledge_base = KnowledgeBase(inference_engine)

    facts = [
        "Child Kyle Jane",
        "Child Jane Gatsby",
        "Sibling Jane Bob",
        "Married Jane Kane",
        "Child Mary Bob",
        "Gender Kyle Male",
        "Gender Jane Female",
        "Gender Gatsby Male",
        "Gender Mary Female",
        "Gender Bob Male",
        "Gender Kane Male",
        "Hobby Kyle Football",
        "Hobby Kyle Gaming",
        "Hobby Mary Football",
        "Hobby Gatsby Fishing",
        "Occupation Kane Engineer",
        "Occupation Bob Builder",
        "Occupation Mary Student",
    ]

    for fact in facts:
        knowledge_base.add_fact(fact)

    # Father, Mother, Occupation, Hobby,
    rules = [
        "Child ?child ?parent => Parent ?parent ?child",
        "Parent ?parent ?child => Child ?child ?parent",
        "Parent ?parent1 ?child & Married ?parent1 ?parent2 => Child ?child ?parent2",
        "Sibling ?sibling2 ?sibling1 => Sibling ?sibling1 ?sibling2",
        "Sibling ?sibling2 ?sibling1 & Child ?sibling1 ?parent => Child ?sibling2 ?parent",
        "Child ?child ?parent & Child ?parent ?grandparent => Grandparent ?grandparent ?child",
        "Parent ?grandparent ?parent & Parent ?parent ?child => Grandchild ?child ?grandparent",
        "Married ?partner2 ?partner1 => Married ?partner1 ?partner2",
        "Married ?partner2 ?partner1 & Sibling ?sibling ?partner1 => Sibling-in-Law ?sibling ?partner2",
        "Child ?child ?parent & Sibling ?parent ?pibling => Pibling ?pibling ?child",
        "Child ?child1 ?parent1 & Child ?child2 ?parent2 & Sibling ?parent1 ?parent2 => Cousin ?child1 ?child2",
        "Pibling ?pibling ?child & Gender ?pibling Male => Uncle ?pibling ?child",
        "Pibling ?pibling ?child & Gender ?pibling Female => Aunt ?pibling ?child",
        "Parent ?parent ?child & Gender ?parent Male => Father ?parent ?child",
        "Parent ?parent ?child & Gender ?parent Female => Father ?parent ?child",
        "Sibling ?sibling ?child & Gender ?sibling Male => Brother ?sibling ?child",
        "Sibling ?sibling ?child & Gender ?sibling Female => Sister ?sibling ?child",
        "Grandparent ?grandparent ?child & Gender ?grandparent Male => Grandfather ?grandparent ?child",
        "Grandparent ?grandparent ?child & Gender ?grandparent Female => Grandmother ?grandparent ?child",
        "Sibling-in-Law ?sibling ?partner1 & Gender ?sibling Male => Brother-in-Law ?sibling ?partner1",
        "Sibling-in-Law ?sibling ?partner1 & Gender ?sibling Female => Sister-in-Law ?sibling ?partner1",
    ]

    for rule in rules:
        knowledge_base.add_rule(rule)

    queries = [
        "Child ?child Gatsby",
        "Grandfather Gatsby ?descendent",
        "Parent ?parent ?child",
        "Child Kyle Kyle",
        "Cousin ?child Kyle",
        "Hobby ?person ?hobby",
        "Married ?person1 ?person2",
        "Child ?child ?parent",
        "Pibling ?child ?pibling",
    ]

    for query in queries:
        res = knowledge_base.query(query)
        # print(res)
        if len(res) == 0:
            print("-")
        for r in res:
            print(str(r))
        print()
