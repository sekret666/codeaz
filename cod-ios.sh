mesaj = "Codeaz Yükleyici"
mesaj += "Telegram: @Codeaz"
mesaj += "Çıxan her şeye Y ardından enterleyin."
clear
echo $mesaj
echo "Python yüklenir"
apk add python3
clear
echo $mesaj
echo "TeleThon yüklenir"
pip3 install telethon
pip3 install bs4
pip3 install requests
clear
echo $mesaj
echo "Fayl yazılır"
curl "https://raw.githubusercontent.com/Texnocom/Codeaz/master/dto.py" --output "codeaz.py"
echo $mesaj
echo "Qurulum hazırdır, İndi StringSessionu ala bilersiz"
python3 codeaz.py
