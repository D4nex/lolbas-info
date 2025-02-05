import csv
import argparse
import time
from colorama import Fore, Style, Back

def readCsv(lolbas_csv):
  features = []
  with open(lolbas_csv, mode='r') as file:
    csv_handle = csv.DictReader(file)
    for feature in csv_handle:
      features.append(feature)
  return features

def removeDuplicates(features):
  seen = set()
  unique_features = []
  for feature in features:
    if feature["Filename"] not in seen:
      unique_features.append(feature)
      seen.add(feature["Filename"])
  return unique_features
    
def listLolbas(features):
  filenames = [feature["Filename"] for feature in features]
  filenames.sort()
    
  grouped_files = {}
  for filename in filenames:
    first_letter = filename[0].upper()
    if first_letter not in grouped_files:
      grouped_files[first_letter] = []
    grouped_files[first_letter].append(filename)
  letters = "ABCDEFGHIJLMNOPRSTUVWXZ"
  columns = 4
    
  for i in range(0, len(letters), columns):
    for letter in letters[i:i + columns]:
      if letter in grouped_files:
        print(f"{Fore.RED}=== {Style.RESET_ALL}{letter} {Fore.RED}==={Style.RESET_ALL}")
      for file in grouped_files[letter]:
        print(f" - {file}")
      print()
                
def searchLolbas(features, filename):
  for feature in features:
    if feature["Filename"] == filename:
      printLolbas(feature)
      return
  print(f"{Fore.RED + Style.DIM}[!] {Style.RESET_ALL}No entry found for LOLBAS: {filename}")

def printLolbas(feature):
  print(f"[{Fore.RED}+{Style.RESET_ALL}] Filename: {feature['Filename']}")
  print(f"[{Fore.RED}+{Style.RESET_ALL}] Description: {feature['Description']}")
  print(f"\t{Fore.CYAN}>_{Style.RESET_ALL} Command: {feature['Command']}")
  print(f"\t{Fore.CYAN}>_{Style.RESET_ALL} Command Description: {feature['Command Description']}")
  print(f"\t{Fore.CYAN}>_{Style.RESET_ALL} Command Usecase: {feature['Command Usecase']}")
  print(f"\t{Fore.CYAN}>_{Style.RESET_ALL} Command Category: [{feature['Command Category']}]")
  print(f"\t{Fore.CYAN}>_{Style.RESET_ALL} Command Privileges: [{feature['Command Privileges']}]")
  print(f"\t{Fore.CYAN}>_{Style.RESET_ALL} Operating System: [{feature['Operating System']}]")
  print(f"\t{Fore.CYAN + Style.DIM}*_{Style.RESET_ALL} Paths: [{feature['Paths']}]")
  print(f"\t{Fore.RED}!_ {Style.RESET_ALL}Detections: ({feature['Detections']})")
  print(f"\t{Fore.CYAN + Style.DIM}*_{Style.RESET_ALL} Resources: {feature['Resources']}")
  print(f"\t{Fore.CYAN + Style.DIM}*_{Style.RESET_ALL} URL: {feature['URL']}")
  print(f"\t{Fore.CYAN + Style.DIM}*_{Style.RESET_ALL} Tags: [{feature['Tags']}]")
  print("=================================================================================================")
  
def banner():
  print(f"""      __        __        __             ___  __  
{Fore.RED}|    /  \ |    |__)  /\  /__`    | |\ | |__  /  \ 
{Style.RESET_ALL}|___ \__/ |___ |__) /~~\ .__/    | | \| |    \__/ 
                      author: {Fore.RED}D4nex{Style.RESET_ALL}
                 
                 """)
  time.sleep(1)
  
def main():
  banner()
  parser = argparse.ArgumentParser(description="Search for information about LOLBAS more easy!")
  parser.add_argument('-l', '--list', action='store_true', help='List all lolbas in the lolbas csv file')
  parser.add_argument('-lol', '--lolbas', type=str, help='Display information for a specific lolbas', metavar='')

  args = parser.parse_args()
    
  lolbas_csv = "csv/lolbas.csv"
  features = readCsv(lolbas_csv)
  unique_features = removeDuplicates(features)

  if args.list:
    listLolbas(unique_features)
  if args.lolbas:
    searchLolbas(unique_features, args.lolbas)

if __name__ == "__main__":
  main()
