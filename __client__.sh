a="\033[30;1m"
m="\033[31;1m"
h="\033[32;1m"
k="\033[33;1m"
b="\033[34;1m"
c="\033[35;1m"
pu="\033[36;1m"
p1="\033[37;1m"
m1="\033[38;1m"
p="\033[39;1m"
hi="\033[40;1m"
clear
echo "${m}      ╔═══════════════════════════╗"
echo "${m}      ║${c}╔╦╗╔═╗╦  ╦╔═╔═╗╔╦╗╔═╗╔═╗╦  ${m}║"
echo "${b}      ║ ${h}║ ║╣ ║  ╠╩╗║ ║║║║╚═╗║╣ ║  ${m}║"
echo "${b}      ║ ${k}╩ ╚═╝╩═╝╩ ╩╚═╝╩ ╩╚═╝╚═╝╩═╝${m}║                 "
echo "${b}      ╚═══════════════════════════╝"
echo "${m}         ${k} ***     ${h}┣▇▇▇═─${k}   * *"
echo "${m}         ${k}(o o)            (o o)"
echo "${m}     ooO--${k}(_)${m}--Ooo    ooO--${k}(_)${m}--Ooo"
echo "${b}     ██████${m}╗ ${b}██████${m}╗${b}  ██████${m}╗${b} ██${m}╗  ${b}██${m}╗								"
echo "${b}    ██${m}╔═══${b}██${m}╗${b}██${m}╔══${b}██${m}╗${b}██${m}╔═══${b}██${m}╗${b}██${m}║ ${b}██${m}╔╝						"
echo "${b}    ██${m}║   ${b}██${m}║${b}██████${m}╔╝${b}██${m}║ ${b}  ██${m}║${b}█████${m}╔╝ 					"
echo "${b}    ██${m}║  ${b} ██${m}║${b}██${m}╔═══╝${b} ██${m}║ ${b}  ██${m}║${b}██${m}╔═${b}██${m}╗ 					"
echo "${m}    ╚${b}██████${m}╔╝${b}██${m}║     ╚${b}██████${m}╔╝${b}██${m}║ ${b} ██${m}╗					"
echo "${m}     ╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═╝						"
echo "${b} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬${k}ஜ۩🔰۩ஜ${b}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
echo "${h} Author${m}:${p}Mr.Tr3v!0n${m}|${h}Team${m}:${p}Black Coder Crush"
echo "${h}    Versi${m}:${p}1.0 *_*${m}|${h}Coders${m}:${p}Python+Shell"
echo "${b} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
echo
echo "${p}[${h}01${p}]${c} Subscribe Gratis"
echo "${p}[${h}02${p}]${c} Restart Inject"
echo "${p}"
read -p "Pilih No: " inject
if [ $inject = 01 ] || [ $inject = 1 ];then
python2 __ssh__.py
elif [ $inject = 02 ] || [ $inject = 2 ];then
sh ___bug_server__.sh
python2 polosan-tsel.py
else
echo
echo "	     ${k} ┌${p2}∩${k}┐(${m}◣${p2}_${m}◢${k})┌${p2}∩${k}┐"
echo "	      ${m}WRONG INPUT !!!!"
echo
sleep 1
sh __client__.sh
fi
