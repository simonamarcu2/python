import sys

# from changer.cash_machine_bootstrap import CashMachineBootstrap

CashMachineBootstrap = 900
def run_cash_machine():
    if len(sys.argv) != 2:
        print('Please provide one argument represented by the input file')
        return
    cash_machine_bootstrap = CashMachineBootstrap()
    with open(sys.argv[1]) as f:
        output = cash_machine_bootstrap.bootstrap_machine_from_file(f)
        print(output)

if __name__ == '__main__':
    run_cash_machine()
