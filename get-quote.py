def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  # print(quotes[0])
  print(quotes[13])

  if __name__== "__primary__":
    primary()
