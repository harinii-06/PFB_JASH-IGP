import csv
from pathlib import Path  

from cash_on_hand import cash_on_hand
from overheads import find_highest_overhead  
from profit_and_loss import profit_and_loss

# Specify the output file path
output_file_path = "Summary_report.txt"

# Open the output file in write mode
with open(output_file_path, 'w') as output_file:
    # Find highest overhead
    highest_overhead = find_highest_overhead('overheads-day-90.csv')
    print(highest_overhead, file=output_file)

    # Cash on hand
    top3_coh_deficitelist = cash_on_hand('cash-on-hand-sgd-day 11 to 90.csv', output_file)
    for i in range(3):
        print(f"[{i+1} HIGHEST CASH DEFICIT] DAY: {top3_coh_deficitelist[i][0]}, AMOUNT: USD{top3_coh_deficitelist[i][1]}", file=output_file)

    # Profit and loss
    top3_pnl_deficitelist = profit_and_loss('profit-and-loss-sgd day 11 to 90.csv', output_file)
    for i in range(3):
        print(f"[{i+1} HIGHEST NET PROFIT DEFICIT] DAY: {top3_pnl_deficitelist[i][0]}, AMOUNT: USD{int(top3_pnl_deficitelist[i][1])}", file=output_file)