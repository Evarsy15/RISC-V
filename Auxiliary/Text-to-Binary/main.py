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
    input_name = prog_args.input
    input_file = open(input_name, 'r')
    riscv_text = input_file.readlines()
    
    riscv_insts = Parse_RISCV_Text(riscv_text)
    riscv_bin = Convert_RISCV_Inst(riscv_insts)
    
    output_name = prog_args.output
    if not output_name:
        i = input_name.find('.')
        prefix, suffix = input_name[:i], input_name[i+1:]
        output_name = prefix + '_out' + suffix
    output_file = open(output_name, 'w')
    output_file.writelines(riscv_bin)



