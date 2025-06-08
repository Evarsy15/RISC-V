from argparse import ArgumentParser
from riscv_parser import Parse_RISCV_Text

prog_args = ArgumentParser(
    prog = 'RISC-V : Text-to-Binary Converter',

    epilog = 'Developed by Nix (rabbitnix@postech.ac.kr)'
)

prog_args.add_argument('-i', '--input', type = str, required = True,
                       help = "Input RISC-V Assembly text file to convert into binary data.")
prog_args.add_argument('-o', '--output', type = str, default = '',
                       help = "Output text file")

if __name__ == '__main__':
    riscv_txt = open(prog_args.input, 'r');
    riscv_insts = Parse_RISCV_Text(riscv_txt.readlines())
    riscv_bin = Convert_RISCV_Inst(riscv_insts)
    
