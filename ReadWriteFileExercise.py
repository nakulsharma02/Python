# Question1. poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and find out words with maximum occurance.
'''word_stat = {}
with open('D://Python//Files/poem.txt', 'r') as file:
    for line in file :
        words = line.split(" ")

        for word in words:
            if word in word_stat:
                word_stat[word] += 1
            else:
                word_stat[word] = 1
print(word_stat)

word_occurence = list(word_stat.values())
max_occurence = max(word_occurence)
print(f'Maximum Occurence of word is: {max_occurence}')
max_occurence_words = [word for word, count in word_stat.items() if count == max_occurence]
print(max_occurence_words)
'''
# Question2. stocks.csv contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file with financial metrics such as pe ratio and price to book ratio. These are calculated as,
# pe_ratio = stock_price / earnings_per_share
# price_to_book_ratio = stock_price / book_value

with open('D://Python//Files/stocks.csv', 'r') as file , open('D://Python//Files/stocks_output.csv', 'w') as out:
    out.write("CompanyName, PE_Ratio, PB_Ratio\n")
    next(file)  # Skip header line
    for line in file:
        line = line.split(",")
        company_name = line[0]
        stock_price = float(line[1])
        earnings_per_share = float(line[2])
        book_value = float(line[3])
        pe_ratio = stock_price / earnings_per_share if earnings_per_share != 0 else 0
        pb_ratio = stock_price / book_value if book_value != 0 else 0
        out.write(f"{company_name}, {pe_ratio:.2f}, {pb_ratio:.2f}\n")
    


