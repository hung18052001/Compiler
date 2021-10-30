def init_automat():
    automat = []
    
    automat.append(['Global', ['library']])
    automat.append(['Global', ['standard', 'end_cmd']])
    automat.append(['Global', ['Class']])
    automat.append(['Global', ['math_type','Define', 'end_cmd']])
    automat.append(['Global', ['bool_type', 'Bool_define', 'end_cmd']])
    automat.append(['Global', ['math_type', 'Func']])
    automat.append(['Global', ['bool_type', 'Func']])
    automat.append(['Global', ['void', 'Func_Void']])
    automat.append(['Define', ['Define', 'comma', 'Define']])
    automat.append(['Define', ['definition', 'equal_assign', 'Expression']])
    automat.append(['Define', ['definition']])

    automat.append(['Class', ['class_func', 'definition', 'start_inner_cmd', 'Global', 'end_inner_cmd']])

    automat.append(['Bool_define', ['definition', 'equal_assign', 'true/false']])
    automat.append(['Bool_define', ['definition', 'equal_assign', 'Condition']])
    automat.append(['Bool_define', ['definition']])
    
    automat.append(['Expression', ['int_lit']])
    automat.append(['Expression', ['float_lit']])
    automat.append(['Expression', ['definition']])
    
    automat.append(['Expression', ['Expression', 'add_oper', 'Expression']])
    automat.append(['Expression', ['Expression', 'arithmetic_operators', 'Expression']])
    automat.append(['Expression', ['start_oper', 'Expression', 'end_oper']])
    



    automat.append(['Global', ['comment']])
    automat.append(['Global', ['start_inner_cmd', 'Global', 'end_inner_cmd']])
    automat.append(['Global', ['Assign', 'end_cmd']])
    
    
    # MinhCao /*
    automat.append(['Global', ['for_key','start_inner_cmd', 'LobalFor', 'end_inner_cmd']]) 
    automat.append(['LobalFor', ['LobalFor', 'break_key']])
    automat.append(['LobalFor', ['LobalFor', 'continue_key']])
    automat.append(['LobalFor', ['start_inner_cmd', 'LobalFor', 'end_inner_cmd']]) 
    automat.append(['LobalFor', ['Global']])  
    # MinhCao */
    
    
    automat.append(['Assign', ['definition', 'double_arithmetic_operators']])
    automat.append(['Assign', ['definition', 'equal_assign', 'Expression']])
    automat.append(['Assign', ['definition','add_assign', 'Expression']])
    automat.append(['Assign', ['definition','oper_assign', 'Expression']])


    automat.append(['Global', ['cout', 'out_oper', 'Value', 'end_cmd']])
    automat.append(['Value', ['Value', 'out_oper', 'Value']])
    automat.append(['Value', ['definition']])
    automat.append(['Value', ['Expression']])
    automat.append(['Value', ['int_lit']])
    automat.append(['Value', ['float_lit']])
    automat.append(['Value', ['string_lit']])


    automat.append(['Func', ['function', 'Parameter', 'end_oper', 'start_inner_cmd', 'Global', 'Return_state', 'end_inner_cmd']])
    automat.append(['Func', ['function', 'end_oper', 'start_inner_cmd', 'Global', 'Return_state', 'end_inner_cmd']])
    automat.append(['Func', ['function', 'Parameter', 'end_oper', 'start_inner_cmd', 'Return_state', 'end_inner_cmd']])
    automat.append(['Func', ['function', 'end_oper', 'start_inner_cmd', 'Return_state', 'end_inner_cmd']])
    automat.append(['Func_Void', ['function', 'Parameter', 'end_oper', 'start_inner_cmd', 'Global', 'end_inner_cmd']])
    automat.append(['Func_Void', ['function', 'end_oper', 'start_inner_cmd', 'Global', 'end_inner_cmd']])

    automat.append(['Parameter', ['Parameter', 'comma', 'Parameter']])
    automat.append(['Parameter', ['math_type', 'Single_define']])
    automat.append(['Single_define', ['definition']])
    automat.append(['Single_define', ['definition', 'equal_assign', 'Expression']])

    automat.append(['Global', ['for_key', 'start_oper', 'math_type', 'definition', 'equal_assign','Expression', 'end_cmd', 'Condition', 'end_cmd', 'Assign', 'end_oper']])
    automat.append(['If_state', ['if_key', 'start_oper', 'Condition', 'end_oper']])
    automat.append(['Else_state', ['else_key']])

    automat.append(['Global', ['while_key', 'start_oper', 'Condition', 'end_oper']])
    
    automat.append(['Condition', ['Expression', 'equal_oper', 'Expression']])
    automat.append(['Condition', ['Expression', 'relational_oper', 'Expression']])
    automat.append(['Condition', ['start_oper', 'Condition', 'end_oper']])
    automat.append(['Condition', ['Condition', 'logical_operators', 'Condition']])
    automat.append(['Condition', ['single_logical_operators', 'Condition']])
    

    
    automat.append(['Return_state', ['return_key', 'Expression', 'end_cmd']])
    automat.append(['Global', ['If_state', 'Else_state']])
    automat.append(['Global', ['If_state', 'Global', 'Else_state']])
    automat.append(['Global', ['Global', 'Global']])

    return automat








