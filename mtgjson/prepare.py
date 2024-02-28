import os
import json
import argparse

if not os.path.exists("input.txt2"):
    with open("./AllPrintings.json") as infile:
        js = json.load(infile)
        allsets = js["data"]
        mlen=0
        n = 0
        for cardset in allsets:
            for card in allsets[cardset]["cards"]:
                cardstr = ""
                if card["language"] != "English":
                    continue
                for attr in ["name",    
                        "convertedManaCost",    
                        "manaCost",
                        "type",
                        "subtypes",
                        "text",
                        "flavorText"]:
                    if attr not in card or not card[attr]:
                        continue
                    cardstr += f"{attr}: {card[attr]}" + "\n"
                if "toughness" in card:
                    cardstr += f"p/t: {card['power']}/{card['toughness']}" + "\n"
                cardstr += "\n"
                if len(cardstr) < 500:
                    print(cardstr)
