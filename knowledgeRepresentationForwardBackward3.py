class Rule:
    def __init__(self,premises,conclusion):
        self.premises,self.conclusion=premises,conclusion


rules=[
    Rule(["cough","fever"],"flu"),
    Rule(["flu","bodypain"],"ViralInfection"),
    Rule(["ViralInfection"],"Medicine"),
    Rule(["sneezing"],"cold"),
    Rule(["cold"],"rest")
]

def forward_chaining(facts,rules):
    known_facts=set(facts)
    print("\nInitial Facts : ",known_facts)
    changed=True

    while changed:
        changed=False

        for rule in rules:
            if all(p in known_facts for p in rule.premises):
                if rule.conclusion not in known_facts:
                    known_facts.add(rule.conclusion)
                    print("Rule Fired : ",rule.premises," -> ",rule.conclusion)
                    changed=True
    return known_facts


def backward_chaining(goal,facts,rules,visited=None):

    if visited is None:
        visited=set()

    if goal in facts:
        print(goal , " is known fact.")
        return True

    if goal in visited:
        return False

    for rule in rules:
        if rule.conclusion == goal:
            print("Trying Rules : ",rule.premises," -> ",rule.conclusion)
            if all(backward_chaining(p,facts,rules,visited) for p in rule.premises):
                print("Goal ",goal," Proved")
                return True

    return False


facts = {"fever","cough","bodypain"}

print("\n============forward chaininh====================")
result=forward_chaining(facts,rules)

print("\n==============Final Facts===========================")
for fact in sorted(result):
    print(fact)

print("\n==================================")

goal="Medicine"

print("\n=====================backward chaining===========================")
if backward_chaining(goal,facts,rules):
    print("\nGoal Achieved : ",goal)
else:
    print("\ngoal cannot be proved")