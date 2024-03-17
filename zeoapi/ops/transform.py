import zeoapi.helper

def transform(dest, args, seq, var_dict):
    assert len(args)==1, "Interpret [addmm] fail, please check it."
    # TO-DO: support multiple width and type
    # TO-DO: enable real LOAD/STORE
    # seq+=make_instr_1op("LOAD32", "_", var_dict[args
    seq += make_instr_3op("32TRANSFORM", args[0], var_dict[args[0]][1], dest, var_dict[dest][1] ) 



# test
#seq=[]
#dictt={ "Y": ("f32",[4,5]), "b": ("f32",[4,5]), "W": ("f32",[4,3]), "X":("f32",[3,5]), "Xf":("f32",[15]) }

#transform("Y", ["b","W","X"], seq, dictt)
