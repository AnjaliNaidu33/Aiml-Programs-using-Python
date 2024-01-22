def mc_pitts(inputs,weights,threshold):
    assert len(inputs)==len(weights)
    weighted_sum=sum(x*w for x,w in zip(inputs,weights))
    output=1 if weighted_sum>=threshold else 0
    return output

def test_logic_gate(logic_gate):
    print(f"{logic_gate} gate:")

    if logic_gate=="AND":
        inputs=[(0,0),(0,1),(1,0),(0,0)]
        weights=(1,1)
        threshold=2

    elif logic_gate=="OR":
        inputs=[(0,0),(0,1),(1,0),(0,0)]
        weights=(1,1)
        threshold=1

    elif logic_gate=="XOR":
        inputs=[(0,0),(0,1),(1,0),(0,0)]
        and_weights=(1,1)
        or_weights=(1,1)
        not_weights=(-1,)
        threshold=1

        for input_pair in inputs:
            input1,input2=input_pair

            and_result=mc_pitts(input_pair,and_weights,threshold)
            or_result=mc_pitts(input_pair,or_weights,threshold)
            not_result=mc_pitts((and_result,),not_weights,threshold)

            xor_result=mc_pitts((or_result,not_result),and_weights,threshold)

            print(f"{input_pair} : {xor_result}")
        return
    
    elif logic_gate=="AND NOT":
        inputs=[(0,0),(0,1),(1,0),(0,0)]
        weights=(1,-1)
        threshold=1

    else:
        print("invalid")
        return 
    
    for input_pair in inputs:
        result=mc_pitts(input_pair,weights,threshold)
        print(f"{input_pair} : {result}")

test_logic_gate("AND")
test_logic_gate("OR")
test_logic_gate("XOR")
test_logic_gate("AND NOT")