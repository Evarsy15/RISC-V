from .riscv_inst import RISCV_Inst

def Parse_RISCV_Text(riscv_text : list[str]) -> list[RISCV_Inst]:
    result = []
    for riscv_asm in riscv_text:
        riscv_token = _impl_tokenize_riscv_asm(riscv_asm)
        riscv_inst = _impl_encode_riscv_token(riscv_token)
        result.append(riscv_inst)
    return result

def _impl_tokenize_riscv_asm(txt : str) -> list[str]:
    # Remove \n, replace \t to space
    _txt = txt.strip(' \n').replace('\t', ' ')
    _token = []

    # Find Opcode of RISC-V Assembly
    i = _txt.find(' ')
    if i >= 0:
        _riscv_op = _txt[:i]
        _txt = _txt[i+1:]
        _token.append(_riscv_op)
    else:
        # This includes:
        #   - Branch Labels
        #   - `ret`
        #   - or maybe something invalid text...
        _token.append(_txt)
        return _token
    
    # Remove all the spaces
    _txt = _txt.replace(' ', '')
    while _txt:
        # Find comma, the token delimeter.
        i = _txt.find(',')
        if i >= 0:
            _token.append(_txt[:i]) # Append Token
            _txt = _txt[i+1:]       # Remove Token from '_txt'
        else: # Last token
            _txt.append(_txt)
            _txt = ''
    
    return _token

def _impl_encode_riscv_token(token : list[str]) -> RISCV_Inst:
    pass