os.system("cls")

print(f"{Fore.WHITE}[ {Fore.CYAN}§ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord Proxy {Fore.WHITE}LnX{Fore.LIGHTBLACK_EX} | Nuke bot {Fore.WHITE}proxy {Fore.LIGHTBLACK_EX}bot")
print(f"{Fore.WHITE}[ {Fore.CYAN}§ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}discord: {Fore.WHITE}proxy")
amount = int(input(f"\n{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}metti un numero di token  di un  bot da proxxare: {Fore.WHITE}"))
auto = input(f"\n{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy di raschiamento automatico {Fore.WHITE}(si/no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}In caso contrario, ogni controllo verrà eseguito su proxy casuale..")
mult = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX} Controlli multipli per proxy {Fore.WHITE}(si/no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")

def scrape():
    scraped = 0
    f = open("proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        scraped = scraped + 1 
        f.write((p)+"\n")
    f.close()
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Raschiato {Fore.WHITE}{scraped} {Fore.LIGHTBLACK_EX}proxies.")


if auto == "si":
    scrape()


print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generazione {Fore.WHITE}{amount}{Fore.LIGHTBLACK_EX} proxy")

fulla = amount


p = open(f"proxies.txt", encoding="UTF-8")


rproxy = p.read().split('\n')
for i in rproxy:
    if i == "" or i == " ":
        index = rproxy.index(i)
        del rproxy[index]


while amount > 0:
    f = open(f"token.txt","a", encoding="UTF-8")
    try:
        if not rproxy[0]:
            print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Tutti i proxy non sono validi!{Fore.WHITE}")
            exit()
    except:
        print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Tutti i proxy non sono validi!{Fore.WHITE}")
        exit()
    if mult == "si":
        proxi = rproxy[0]
    else:
        proxi = random.choice(rproxy)
    proxies = {
        "https": proxi
    }
    amount = amount - 1
    code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
    try:
        url = requests.get(f"https://canary.discord.com/api/v6/invite/{code}?with_counts=true", proxies=proxies, timeout=3)
        if url.status_code == 200:
            jurl = url.json()
            ginfo = jurl["guild"]
            gname = ginfo["name"]
            members = jurl["approximate_member_count"]
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Token al lavoro {Fore.WHITE}{code}{Fore.LIGHTBLACK_EX} | Nome {Fore.WHITE}{gname}{Fore.LIGHTBLACK_EX} | {Fore.WHITE}{members}{Fore.LIGHTBLACK_EX} membri")
            f.write(f"\ndiscord.gg/{code}     |     {members}     |     {gname}")
            f.close()
        elif url.status_code == 404:
            fulla = fulla - 1
            print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}invito non valido {Fore.WHITE}{code}")
        elif url.status_code == 429:
            fulla = fulla - 1
            if mult == "si":
                    print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} è limitato dal ratto! | Cambio del proxy")
            else:
                print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} è limitato dal ratto!")
            index = rproxy.index(proxi)
            del rproxy[index]
        else:
            fulla = fulla - 1
            print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Errore non valido! | Codice di stato {Fore.WHITE}{url.status_code}")
    except:
        index = rproxy.index(proxi)
        del rproxy[index]
        pw = open(f"proxies.txt","w", encoding="UTF-8")
        for i in rproxy:
            pw.write(i + "\n")
        pw.close()
        fulla = fulla - 1
        print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Connessione al proxy non riuscita {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} |Rimozione dall'elenco!")
        pass
